"""Tests for the parts of the literature pipeline that a silent bug would ruin.

Two of these exist because the pipeline already failed them once.

`test_windows_survive_a_dense_paper` is a regression test. The first version of
`candidate_windows` merged every overlapping hit and then sorted by length; in a
paper that uses words like taxonomy and dimension throughout, everything merged
into one span larger than the whole budget, the loop broke on it, and the paper
got **zero** windows. Two of the five papers in the first smoke test were
affected, including the one whose faceted model this review most needs.

`test_a_paraphrase_is_rejected` exists because a gate that never fires is not a
gate. The extraction runs showed 37 verified rows and no rejections, which is
the right outcome only if the check can still say no.
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.lit.extract import (canon, dehyphenate, _check_quote, candidate_windows,
                             WINDOW_TERMS, MAX_WINDOWS, MAX_WINDOW_BUDGET)
from src.lit.reliability import cohens_kappa, fleiss_kappa, interpret
from src.lit.sources import normalise_doi, normalise_title, _clean


# --------------------------------------------------------------------------
# The quote verification gate
# --------------------------------------------------------------------------

SOURCE = (
    "## 3.2 The Generation facet\n"
    "The Generation facet records who or what produced the initial text, using\n"
    "a five-level scale from G0 to G4. The author’s own wording is kept — even\n"
    "where it is awkward — because paraphrase would defeat the purpose."
)


def _prepared(text: str) -> tuple[str, str]:
    canonical = canon(text)
    return canonical, canonical.lower()


def test_an_exact_quote_is_found():
    ok, mode = _check_quote("The Generation facet records who or what produced",
                            *_prepared(SOURCE))
    assert ok and mode == "exact"


def test_a_quote_across_a_line_break_is_found():
    """Whitespace is collapsed, so a quote may span the source's line breaks."""
    ok, mode = _check_quote("produced the initial text, using a five-level scale",
                            *_prepared(SOURCE))
    assert ok and mode == "exact"


def test_typography_does_not_break_a_quote():
    """Curly quotes and em dashes are unified; PDF extraction changes both."""
    ok, mode = _check_quote("The author's own wording is kept - even where it is awkward",
                            *_prepared(SOURCE))
    assert ok and mode == "exact"


def test_case_only_difference_is_reported_as_caseless():
    ok, mode = _check_quote("the generation facet records who or what",
                            *_prepared(SOURCE))
    assert ok and mode == "caseless"


def test_a_paraphrase_is_rejected():
    """The gate has to be able to say no, or it proves nothing when it says yes."""
    ok, mode = _check_quote("The Generation facet captures which agent wrote the draft",
                           *_prepared(SOURCE))
    assert not ok and mode == "not_found"


def test_a_plausible_invention_is_rejected():
    """A scheme that is not in the source cannot enter the data."""
    ok, _ = _check_quote("The Accountability facet records who vouches for the text",
                         *_prepared(SOURCE))
    assert not ok


def test_an_empty_quote_is_rejected():
    ok, mode = _check_quote("", *_prepared(SOURCE))
    assert not ok and mode == "empty"


def test_a_line_break_hyphen_does_not_void_a_real_quote():
    """The commonest real cause of a voided row: PDF splits a word across lines.

    13 of the 25 rows voided in the first full run failed only because the
    source read "cate- gories" where the quote read "categories".
    """
    source = "The scheme records the CRediT cate-\ngories used by each author."
    canonical = canon(source)
    ok, mode = _check_quote("the CRediT categories used by each author",
                            canonical, canonical.lower())
    assert ok and mode == "dehyphenated"


def test_dehyphenation_does_not_rescue_a_paraphrase():
    """The looser mode stays a mode, not a licence."""
    source = canon("The scheme records the CRediT cate-\ngories used by each author.")
    ok, _ = _check_quote("the scheme captures each author's role categories",
                         source, source.lower())
    assert not ok


def test_dehyphenate_only_removes_a_hyphen_before_whitespace():
    assert dehyphenate("cate- gories") == "categories"
    assert dehyphenate("AI-assisted writing") == "AI-assisted writing"


def test_canon_folds_ligatures_and_drops_soft_hyphens():
    assert canon("classi­fication") == "classification"
    assert canon("deﬁnition") == "definition"


# --------------------------------------------------------------------------
# Candidate windows
# --------------------------------------------------------------------------

def test_windows_survive_a_dense_paper():
    """Regression: a paper using the terms throughout must still get windows.

    Built to reproduce the original failure exactly: the terms recur every few
    hundred characters across a text far longer than the window budget, so the
    old merge-everything-then-sort-by-length version returned an empty list.
    """
    filler = "Padding sentence that carries no scheme vocabulary at all. " * 6
    body = "".join(
        f"## Section {index}\nThis section discusses the {term} we propose, "
        f"and its dimension structure. {filler}"
        for index, term in enumerate(WINDOW_TERMS * 3)
    )
    windows = candidate_windows(body)
    assert windows, "a dense paper must not yield zero windows"
    assert len(windows) <= MAX_WINDOWS
    assert sum(len(w["text"]) for w in windows) <= MAX_WINDOW_BUDGET
    assert windows == sorted(windows, key=lambda w: w["starts_at_char"])


def test_windows_do_not_overlap():
    """Overlapping windows would send the same text twice in every packet."""
    body = ("".join(f"Section {i}: the taxonomy and its dimension structure here. "
                    f"{'filler words without scheme vocabulary. ' * 4}"
                    for i in range(40)))
    windows = candidate_windows(body)
    assert windows
    for earlier, later in zip(windows, windows[1:]):
        assert (earlier["starts_at_char"] + len(earlier["text"])
                <= later["starts_at_char"])


def test_windows_are_empty_only_when_nothing_matches():
    assert candidate_windows("A paper about bird migration in coastal wetlands.") == []
    assert candidate_windows("") == []


def test_a_window_does_not_start_mid_word():
    text = ("Introductory prose about many unrelated matters, at some length, so "
            "that the window has somewhere to start from. " * 6
            + "We now set out the taxonomy and its dimension structure in full.")
    windows = candidate_windows(text)
    assert windows
    first = windows[0]["text"]
    assert first[:1].strip(), "a window should not begin with whitespace"
    assert text.find(first) == windows[0]["starts_at_char"]


# --------------------------------------------------------------------------
# Agreement
# --------------------------------------------------------------------------

def test_cohens_kappa_matches_a_hand_computed_case():
    """Two raters, 10 items: observed 0.8, expected 0.5, kappa 0.6."""
    a = ["include"] * 5 + ["exclude"] * 5
    b = ["include"] * 4 + ["exclude"] * 1 + ["include"] * 1 + ["exclude"] * 4
    kappa, parts = cohens_kappa(a, b)
    assert parts["observed_agreement"] == 0.8
    assert parts["expected_agreement"] == 0.5
    assert abs(kappa - 0.6) < 1e-9
    assert interpret(kappa) == "moderate"


def test_perfect_agreement_on_one_category_is_undefined_not_perfect():
    """Both raters excluding everything tells us nothing, and must not read as 1.0.

    This is the case a library default would quietly turn into 0 or 1. A screener
    that excludes every record would otherwise look either perfect or terrible
    instead of uninformative.
    """
    kappa, parts = cohens_kappa(["exclude"] * 20, ["exclude"] * 20)
    assert math.isnan(kappa)
    assert "undefined" in parts["note"]
    assert interpret(kappa) == "undefined"


def test_total_disagreement_is_worse_than_chance():
    kappa, _ = cohens_kappa(["include", "exclude"] * 10, ["exclude", "include"] * 10)
    assert kappa < 0
    assert interpret(kappa) == "worse than chance"


def test_fleiss_kappa_on_full_agreement():
    kappa, parts = fleiss_kappa([["a", "a", "a"], ["b", "b", "b"], ["a", "a", "a"]])
    assert abs(kappa - 1.0) < 1e-9
    assert parts["raters_per_item"] == 3


def test_fleiss_kappa_drops_items_with_the_wrong_number_of_raters():
    ratings = [["a", "a", "a"], ["b", "b", "b"], ["a", "a"]]
    _, parts = fleiss_kappa(ratings)
    assert parts["items_dropped_for_uneven_raters"] == 1
    assert parts["n"] == 2


# --------------------------------------------------------------------------
# Record normalisation
# --------------------------------------------------------------------------

def test_doi_normalisation_strips_every_prefix_form():
    for form in ("https://doi.org/10.1000/ABC", "doi:10.1000/abc",
                 "https://dx.doi.org/10.1000/Abc", " 10.1000/abc "):
        assert normalise_doi(form) == "10.1000/abc"


def test_escaped_markup_is_removed_from_a_title():
    """Crossref escapes its own JATS, so entities must be unescaped first."""
    assert _clean("&lt;p&gt;&lt;b&gt;A Title&lt;/b&gt;&lt;/p&gt;") == "A Title"
    assert _clean("<jats:p>Another Title</jats:p>") == "Another Title"


def test_title_normalisation_ignores_punctuation_and_case():
    assert (normalise_title("AI Disclosure: A Taxonomy!")
            == normalise_title("ai disclosure a taxonomy"))
