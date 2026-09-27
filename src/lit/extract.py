"""Extraction packets, schema validation, and the quote verification gate.

    python -m src.lit.extract prepare    build packets for the extraction agents
    python -m src.lit.extract verify     validate returned JSON, check every quote
    python -m src.lit.extract requeue    list the papers whose rows were voided

The gate is the point of this module. An agent returns a quote; this code checks
that the quote really is in the text that was retrieved. A quote that cannot be
located voids its whole row, and the paper goes on the requeue list.

Whitespace, quotation marks, dashes and soft hyphens are normalised before the
comparison, because PDF extraction changes all four and none of them changes
what a source says. Case is tried exactly first and then ignored, and which of
the two matched is recorded, so a report can say how many rows needed the looser
comparison. Nothing else is loosened: an approximate or paraphrased quote fails,
which is the whole idea.
"""

from __future__ import annotations

import glob
import io
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIT = os.path.join(ROOT, "data", "lit")
INCLUDED = os.path.join(LIT, "screened-in.jsonl")
RETRIEVAL = os.path.join(LIT, "retrieval.jsonl")
FULLTEXT = os.path.join(LIT, "fulltext")
EXTRACT = os.path.join(LIT, "extract")
PACKETS = os.path.join(EXTRACT, "packets")
RAW = os.path.join(EXTRACT, "raw")
SCHEMES = os.path.join(LIT, "schemes.jsonl")
REJECTED = os.path.join(EXTRACT, "rejected.jsonl")
FT_EXCLUDED = os.path.join(LIT, "fulltext-excluded.jsonl")
REQUEUE = os.path.join(EXTRACT, "requeue.json")

PACKET_SIZE_FULLTEXT = 3
PACKET_SIZE_ABSTRACT = 10
MAX_QUOTE_WORDS = 25
HARD_QUOTE_WORDS = 40

# Candidate windows. Reading every full text in full would cost more than the
# rest of the pipeline together, so `prepare` pre-cuts the places where a scheme
# is usually stated and puts them in the packet. This is navigation, not
# selection: the whole text stays on disk, the packet says so, and every quote is
# still verified against the whole text rather than against the windows. A window
# that misleads an extractor costs one reading; a window that hides a scheme is
# recoverable because the extractor can open the file.
WINDOW_TERMS = (
    "taxonomy", "typology", "framework", "facet", "dimension", "categor",
    "classification", "coding scheme", "codebook", "rubric", "checklist",
    "levels of", "level of", "five levels", "scale", "tier", "vocabulary",
    "ontology", "schema", "we coded", "were coded", "coding frame",
    "disclosure statement", "declaration", "attribution", "provenance",
    "contributorship", "CRediT",
)
WINDOW_CHARS = 1200
MAX_WINDOWS = 18
MAX_WINDOW_BUDGET = 24000

DOMAINS = ("research_publishing", "education_assessment", "journalism_media",
           "government", "software", "workplace", "advertising", "law_regulation",
           "other")
ARTIFACT_TYPES = ("empirical_study", "normative_proposal", "policy",
                  "reporting_guideline", "technical_standard")
GRANULARITY = ("document", "section", "paragraph", "sentence", "asset", "not_stated")
AUTHORITY = ("self_report", "editorial_requirement", "regulatory",
             "technical_standard", "not_stated")
CLOSED_OR_OPEN = ("closed_list", "open_text", "not_stated")

DASHES = dict.fromkeys(map(ord, "‐‑‒–—―−"), "-")
QUOTES = {ord("‘"): "'", ord("’"): "'", ord("‚"): "'",
          ord("“"): '"', ord("”"): '"', ord("„"): '"',
          ord("«"): '"', ord("»"): '"', ord("′"): "'",
          ord("­"): "", ord("​"): ""}


def canon(text: str) -> str:
    """Normalise away the differences PDF extraction introduces.

    NFKC folds ligatures, so `fi` extracted as one glyph matches `fi` typed as
    two letters. Dashes and quotation marks are unified because typesetting
    changes them. Soft hyphens and zero-width spaces are dropped. Whitespace is
    collapsed last, because a quote spanning a line break must still match.
    """
    text = unicodedata.normalize("NFKC", text)
    text = text.translate(DASHES).translate(QUOTES)
    return " ".join(text.split())


def load_jsonl(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    rows = []
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: str, rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def _heading_before(text: str, index: int) -> str:
    """Nearest preceding heading line, which the extractor can use as a locator.

    The retrieval step marks JATS section titles with `## `, so this finds a real
    section name for Europe PMC texts and usually a plausible one for HTML.
    """
    prefix = text[:index]
    cut = prefix.rfind("\n## ")
    if cut == -1:
        return ""
    line = prefix[cut + 4:].split("\n")[0]
    return line.strip()[:80]


def _snap(text: str, index: int, forward: bool) -> int:
    """Move an index to the nearest whitespace so a window does not start mid-word."""
    limit = 60
    step = 1 if forward else -1
    position = index
    for _ in range(limit):
        if position <= 0 or position >= len(text):
            break
        if text[position].isspace():
            return position + (1 if forward is False else 0)
        position += step
    return max(0, min(index, len(text)))


def candidate_windows(text: str) -> list[dict]:
    """Passages where a category scheme is usually stated.

    Hits are grouped into clusters no wider than one window, and clusters are
    ranked by how many distinct terms they contain, because density is the signal
    that a scheme is being laid out rather than mentioned in passing.

    An earlier version merged every overlapping hit and then sorted by length. In
    a paper that uses these words throughout, everything merged into one span
    larger than the whole budget, the loop broke on it, and the paper got zero
    windows: two of the five papers in the first smoke test, including the one
    whose six facets this review most needs. Hence the bounded clusters, and
    `continue` rather than `break` when a window does not fit the budget.
    """
    if not text:
        return []
    lower = text.lower()
    hits: list[tuple[int, str]] = []
    for term in WINDOW_TERMS:
        start = 0
        low_term = term.lower()
        while True:
            hit = lower.find(low_term, start)
            if hit == -1:
                break
            hits.append((hit, term))
            start = hit + len(low_term)
    if not hits:
        return []
    hits.sort()

    clusters: list[dict] = []
    for position, term in hits:
        if clusters and position - clusters[-1]["first"] <= WINDOW_CHARS:
            clusters[-1]["last"] = position
            clusters[-1]["terms"].add(term)
            clusters[-1]["hits"] += 1
        else:
            clusters.append({"first": position, "last": position,
                             "terms": {term}, "hits": 1})

    # Density first, then position, so a ranking tie is resolved by the paper's
    # own order rather than by dictionary order of the term list.
    clusters.sort(key=lambda c: (-len(c["terms"]), -c["hits"], c["first"]))

    chosen: list[tuple[int, int, set]] = []
    budget = 0
    for cluster in clusters:
        if len(chosen) >= MAX_WINDOWS:
            break
        begin = _snap(text, max(0, cluster["first"] - 250), forward=False)
        end = _snap(text, min(len(text), cluster["last"] + WINDOW_CHARS), forward=True)
        end = min(end, begin + 2 * WINDOW_CHARS)
        if budget + (end - begin) > MAX_WINDOW_BUDGET:
            continue
        budget += end - begin
        chosen.append((begin, end, set(cluster["terms"])))

    # Two windows can overlap: clusters are bounded by the distance between hits,
    # but each window runs on past its last hit. Sending the overlap twice buys
    # nothing and costs tokens in every packet, so overlapping ranges are merged.
    chosen.sort()
    merged: list[list] = []
    for begin, end, terms in chosen:
        if merged and begin <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
            merged[-1][2] |= terms
        else:
            merged.append([begin, end, set(terms)])

    return [{
        "heading_above": _heading_before(text, begin),
        "matched_terms": sorted(terms)[:6],
        "starts_at_char": begin,
        "text": text[begin:end],
    } for begin, end, terms in merged]


def prepare() -> int:
    retrieval = {row["rec_id"]: row for row in load_jsonl(RETRIEVAL)}
    records = load_jsonl(INCLUDED)
    if not records:
        print("nothing screened in yet")
        return 1

    usable = []
    for record in records:
        row = retrieval.get(record["rec_id"])
        if not row or row["status"] == "no_text":
            continue
        source_text = _read_source_text(record["rec_id"])
        usable.append({
            "rec_id": record["rec_id"],
            "title": record["title"],
            "year": record["year"],
            "venue": record["venue"],
            "source_ref": (f"doi:{record['doi']}" if record.get("doi")
                           else f"arXiv:{record['arxiv_id']}" if record.get("arxiv_id")
                           else record.get("url", "")),
            "retrieval_status": row["status"],
            "text_source": row["text_source"],
            "text_file": f"data/lit/fulltext/{record['rec_id']}.txt",
            "chars": row["chars"],
            "candidate_windows": candidate_windows(source_text),
        })

    os.makedirs(PACKETS, exist_ok=True)
    for old in glob.glob(os.path.join(PACKETS, "packet-*.json")):
        os.remove(old)

    # Two packet series, because the two kinds of paper cost very different
    # amounts to read. An abstract is one or two thousand characters, so ten fit
    # in a packet comfortably; a full text carries up to 24,000 characters of
    # windows, so three is already a lot to hold at once.
    full = [p for p in usable if p["retrieval_status"] == "fulltext_oa"]
    abstracts = [p for p in usable if p["retrieval_status"] != "fulltext_oa"]

    written = 0
    for prefix, group, size in (("ft", full, PACKET_SIZE_FULLTEXT),
                                ("ab", abstracts, PACKET_SIZE_ABSTRACT)):
        for index in range(0, len(group), size):
            packet_id = f"{prefix}-{index // size + 1:03d}"
            payload = {
                "packet_id": packet_id,
                "instructions": "docs/scoping/prompts/extractor.md",
                "papers": group[index:index + size],
            }
            with io.open(os.path.join(PACKETS, f"packet-{packet_id}.json"), "w",
                         encoding="utf-8", newline="\n") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=2)
                fh.write("\n")
            written += 1
    print(f"{len(usable)} papers with text into {written} packets")
    print(f"  {len(full)} full texts, {PACKET_SIZE_FULLTEXT} per packet (packet-ft-*)")
    print(f"  {len(abstracts)} abstracts, {PACKET_SIZE_ABSTRACT} per packet (packet-ab-*)")
    print(f"packets in {PACKETS}")
    return 0


def _read_source_text(rec_id: str) -> str:
    path = os.path.join(FULLTEXT, f"{rec_id}.txt")
    if not os.path.exists(path):
        return ""
    with io.open(path, encoding="utf-8") as fh:
        return fh.read()


def dehyphenate(text: str) -> str:
    """Remove a hyphen left by a line break, on both sides of the comparison.

    PDF extraction turns "categories" split across two lines into "cate-
    gories", which `canon` then collapses to "cate- gories". A quote copied with
    the word whole cannot match it, and that was the single most common reason
    rows were voided in the first full run: 13 of 25, all of them genuine quotes
    defeated by typesetting.

    Applied to the source text and the quote alike, so it can only ever match
    strings that differ by a line-break hyphen. It is tried last and recorded as
    its own match mode, because it is a looser comparison than the other two and
    the report should be able to say how many rows needed it.
    """
    return re.sub(r"-\s+", "", text)


def _check_quote(quote: str, canon_text: str, lower_text: str) -> tuple[bool, str]:
    if not quote:
        return False, "empty"
    needle = canon(quote)
    if needle in canon_text:
        return True, "exact"
    if needle.lower() in lower_text:
        return True, "caseless"
    if dehyphenate(needle.lower()) in dehyphenate(lower_text):
        return True, "dehyphenated"
    return False, "not_found"


def _enum_problem(field: str, value, allowed: tuple) -> str | None:
    if value not in allowed:
        return f"{field}={value!r} is not one of {allowed}"
    return None


def verify() -> int:
    files = sorted(glob.glob(os.path.join(RAW, "*.json")))
    if not files:
        print(f"no extraction output in {RAW}")
        return 1
    retrieval = {row["rec_id"]: row for row in load_jsonl(RETRIEVAL)}

    text_cache: dict[str, tuple[str, str]] = {}
    rows_ok: list[dict] = []
    rows_bad: list[dict] = []
    ft_excluded: list[dict] = []
    requeue: set[str] = set()
    problems: list[str] = []
    seen_recs: set[str] = set()

    for path in files:
        name = os.path.basename(path)
        try:
            with io.open(path, encoding="utf-8") as fh:
                payload = json.load(fh)
        except ValueError as exc:
            problems.append(f"{name}: not valid JSON ({exc})")
            continue
        papers = payload if isinstance(payload, list) else payload.get("papers", [payload])

        for paper in papers:
            rec_id = paper.get("rec_id", "")
            if not rec_id:
                problems.append(f"{name}: a paper entry has no rec_id")
                continue
            seen_recs.add(rec_id)
            if rec_id not in text_cache:
                source = _read_source_text(rec_id)
                text_cache[rec_id] = (canon(source), canon(source).lower())
            canon_text, lower_text = text_cache[rec_id]
            if not canon_text:
                problems.append(f"{name}: {rec_id} has no retrieved text on disk")
                requeue.add(rec_id)
                continue

            status = retrieval.get(rec_id, {}).get("status", "")
            if not paper.get("has_scheme", False):
                ft_excluded.append({
                    "rec_id": rec_id,
                    "reason": paper.get("reason", "no reason given"),
                    "retrieval_status": status,
                })
                continue

            for scheme in paper.get("schemes", []):
                scheme_problems = [p for p in (
                    _enum_problem("domain", scheme.get("domain"), DOMAINS),
                    _enum_problem("artifact_type", scheme.get("artifact_type"),
                                  ARTIFACT_TYPES),
                    _enum_problem("granularity", scheme.get("granularity"), GRANULARITY),
                    _enum_problem("authority", scheme.get("authority"), AUTHORITY),
                ) if p]
                if scheme_problems:
                    problems.append(f"{name}: {rec_id} "
                                    f"{scheme.get('scheme_id', '?')}: "
                                    f"{'; '.join(scheme_problems)}")
                    requeue.add(rec_id)
                    continue

                dimensions = scheme.get("dimensions", [])
                if not dimensions:
                    problems.append(f"{name}: {rec_id} "
                                    f"{scheme.get('scheme_id', '?')} has no dimensions")
                    requeue.add(rec_id)
                    continue

                for dim in dimensions:
                    row = {
                        "rec_id": rec_id,
                        "scheme_id": scheme.get("scheme_id", ""),
                        "scheme_name_verbatim": scheme.get("scheme_name_verbatim", ""),
                        "source_ref": scheme.get("source_ref", ""),
                        "domain": scheme.get("domain", ""),
                        "artifact_type": scheme.get("artifact_type", ""),
                        "granularity": scheme.get("granularity", ""),
                        "authority": scheme.get("authority", ""),
                        "empirical_basis": scheme.get("empirical_basis", "none"),
                        "machine_readable_artifact":
                            scheme.get("machine_readable_artifact", "none"),
                        "dimension_label_verbatim":
                            dim.get("dimension_label_verbatim", ""),
                        "definition_quote": dim.get("definition_quote", ""),
                        "value_list_verbatim": dim.get("value_list_verbatim", []),
                        "closed_or_open": dim.get("closed_or_open", ""),
                        "locator": dim.get("locator", ""),
                        "quote": dim.get("quote", ""),
                        "retrieval_status": status,
                        "extraction_file": name,
                    }

                    faults = []
                    bad_enum = _enum_problem("closed_or_open", row["closed_or_open"],
                                             CLOSED_OR_OPEN)
                    if bad_enum:
                        faults.append(bad_enum)
                    if not row["dimension_label_verbatim"]:
                        faults.append("dimension_label_verbatim is empty")
                    for field in ("quote", "definition_quote"):
                        words = len(row[field].split())
                        if words > HARD_QUOTE_WORDS:
                            faults.append(f"{field} is {words} words, over the hard cap")

                    quote_ok, quote_mode = _check_quote(row["quote"], canon_text,
                                                        lower_text)
                    def_ok, def_mode = _check_quote(row["definition_quote"],
                                                    canon_text, lower_text)
                    if not quote_ok:
                        faults.append(f"quote not found in the retrieved text "
                                      f"({quote_mode})")
                    if row["definition_quote"] and not def_ok:
                        faults.append(f"definition_quote not found ({def_mode})")

                    row["quote_match_mode"] = quote_mode
                    row["definition_match_mode"] = def_mode
                    row["quote_over_soft_cap"] = (
                        len(row["quote"].split()) > MAX_QUOTE_WORDS)
                    # A replacement character means PDF extraction lost a glyph,
                    # usually an em dash inside a label such as
                    # "Writing�Review & Editing". The label is still verbatim
                    # against the text we retrieved, so the row stands, but the
                    # report counts these rather than pretending the label is clean.
                    row["has_extraction_artifact"] = any(
                        "�" in str(row[field]) for field in
                        ("dimension_label_verbatim", "quote", "definition_quote",
                         "scheme_name_verbatim"))

                    if faults:
                        row["quote_verified"] = False
                        row["faults"] = faults
                        rows_bad.append(row)
                        requeue.add(rec_id)
                    else:
                        row["quote_verified"] = True
                        rows_ok.append(row)

    write_jsonl(SCHEMES, rows_ok)
    write_jsonl(REJECTED, rows_bad)
    write_jsonl(FT_EXCLUDED, ft_excluded)
    os.makedirs(EXTRACT, exist_ok=True)
    with io.open(REQUEUE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(sorted(requeue), fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    schemes_count = len({r["scheme_id"] for r in rows_ok})
    print(f"papers seen in output      : {len(seen_recs)}")
    print(f"excluded at full text      : {len(ft_excluded)}")
    print(f"verified dimension rows    : {len(rows_ok)} across {schemes_count} schemes")
    print(f"voided rows                : {len(rows_bad)}")
    print(f"papers to requeue          : {len(requeue)}")
    modes: dict[str, int] = {}
    for row in rows_ok:
        modes[row["quote_match_mode"]] = modes.get(row["quote_match_mode"], 0) + 1
    print(f"quote match modes          : {modes}")
    over = sum(1 for row in rows_ok if row["quote_over_soft_cap"])
    if over:
        print(f"quotes over {MAX_QUOTE_WORDS} words        : {over} (kept, flagged)")
    if problems:
        print(f"\nstructural problems ({len(problems)}):")
        for problem in problems[:30]:
            print(f"  {problem}")
        if len(problems) > 30:
            print(f"  ... and {len(problems) - 30} more")
    print(f"\nwrote {SCHEMES}\nwrote {REJECTED}\nwrote {FT_EXCLUDED}\nwrote {REQUEUE}")
    return 0


def requeue() -> int:
    if not os.path.exists(REQUEUE):
        print("nothing to requeue; run verify first")
        return 1
    with io.open(REQUEUE, encoding="utf-8") as fh:
        ids = json.load(fh)
    records = {row["rec_id"]: row for row in load_jsonl(INCLUDED)}
    print(f"{len(ids)} papers need a second extraction:\n")
    for rec_id in ids:
        record = records.get(rec_id, {})
        print(f"  {rec_id}  {record.get('title', '(unknown)')[:70]}")
    return 0


ACTIONS = {"prepare": prepare, "verify": verify, "requeue": requeue}

if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action not in ACTIONS:
        print(__doc__)
        sys.exit(2)
    sys.exit(ACTIONS[action]())
