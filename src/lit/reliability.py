"""Inter-rater agreement, written from the definitions rather than borrowed.

The parent project's brief says this pattern is reimplemented from scratch and
no code is copied from the author's private QualReAI project. These are the
textbook formulas, with one decision made explicitly rather than left to a
library default: when expected agreement is 1, kappa is undefined, and this
module returns `nan` and says so instead of returning 0 or 1. That case happens
easily here, because a screener that includes everything produces exactly it,
and a silent 0 would read as terrible agreement rather than as no information.
"""

from __future__ import annotations

import math
from collections import Counter


def cohens_kappa(a: list[str], b: list[str]) -> tuple[float, dict]:
    """Cohen's kappa for two raters over the same items, plus the working parts."""
    if len(a) != len(b):
        raise ValueError("the two raters must have judged the same number of items")
    n = len(a)
    if n == 0:
        return float("nan"), {"n": 0, "note": "no items"}

    observed = sum(1 for x, y in zip(a, b) if x == y) / n
    count_a, count_b = Counter(a), Counter(b)
    categories = set(count_a) | set(count_b)
    expected = sum((count_a[c] / n) * (count_b[c] / n) for c in categories)

    parts = {
        "n": n,
        "observed_agreement": round(observed, 4),
        "expected_agreement": round(expected, 4),
        "rater_a_distribution": dict(count_a),
        "rater_b_distribution": dict(count_b),
    }
    if math.isclose(expected, 1.0):
        parts["note"] = ("expected agreement is 1, kappa is undefined; this happens "
                         "when both raters put every item in one category")
        return float("nan"), parts
    kappa = (observed - expected) / (1 - expected)
    return kappa, parts


def fleiss_kappa(ratings: list[list[str]]) -> tuple[float, dict]:
    """Fleiss kappa for a fixed number of raters per item.

    `ratings` is one list per item, each holding that item's category from every
    rater. Every item must have the same number of raters; an item judged by
    fewer is dropped and counted, because quietly rescaling the row would
    understate disagreement.
    """
    if not ratings:
        return float("nan"), {"n": 0, "note": "no items"}
    widths = Counter(len(row) for row in ratings)
    n_raters = widths.most_common(1)[0][0]
    usable = [row for row in ratings if len(row) == n_raters]
    dropped = len(ratings) - len(usable)
    n_items = len(usable)
    if n_items == 0 or n_raters < 2:
        return float("nan"), {"n": n_items, "note": "not enough raters"}

    categories = sorted({c for row in usable for c in row})
    counts = [[row.count(c) for c in categories] for row in usable]

    p_j = [sum(row[j] for row in counts) / (n_items * n_raters)
           for j in range(len(categories))]
    p_i = [(sum(v * v for v in row) - n_raters) / (n_raters * (n_raters - 1))
           for row in counts]
    p_bar = sum(p_i) / n_items
    p_e = sum(p * p for p in p_j)

    parts = {
        "n": n_items,
        "raters_per_item": n_raters,
        "items_dropped_for_uneven_raters": dropped,
        "observed_agreement": round(p_bar, 4),
        "expected_agreement": round(p_e, 4),
        "category_shares": {c: round(p, 4) for c, p in zip(categories, p_j)},
    }
    if math.isclose(p_e, 1.0):
        parts["note"] = "expected agreement is 1, kappa is undefined"
        return float("nan"), parts
    return (p_bar - p_e) / (1 - p_e), parts


def interpret(kappa: float) -> str:
    """Landis and Koch bands, named as bands and not as verdicts.

    The bands are a convention, not a threshold anyone agreed on. They are here
    so a report can say which band a figure falls in without implying that the
    band decides anything.
    """
    if math.isnan(kappa):
        return "undefined"
    if kappa < 0:
        return "worse than chance"
    if kappa < 0.21:
        return "slight"
    if kappa < 0.41:
        return "fair"
    if kappa < 0.61:
        return "moderate"
    if kappa < 0.81:
        return "substantial"
    return "almost perfect"
