"""Title and abstract screening: batching, ingesting verdicts, agreement.

    python -m src.lit.screen prepare      write batches for the screeners
    python -m src.lit.screen ingest       read verdict files, merge, validate
    python -m src.lit.screen agreement    kappa between screeners, calibration
    python -m src.lit.screen decide       apply recall-first, write the included set
    python -m src.lit.screen sample       blind sample of 20 for the author

The screening itself is done by two LLM agents from the eligibility criteria in
`docs/scoping/protocol.md`. This module never asks a model anything; it only
prepares what they read and checks what they returned. That split is deliberate:
if the harness also held the prompt, a quiet change to the prompt would not show
up as a change to the data.

The order of records is shuffled with a seed derived from the protocol hash, so
the batching is reproducible and nobody chose which records sit together.
"""

from __future__ import annotations

import glob
import io
import json
import os
import random
import sys

from .reliability import cohens_kappa, interpret

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIT = os.path.join(ROOT, "data", "lit")
RECORDS = os.path.join(LIT, "records.jsonl")
FROZEN = os.path.join(LIT, "protocol-frozen.json")
SCREEN = os.path.join(LIT, "screen")
BATCHES = os.path.join(SCREEN, "batches")
VERDICTS = os.path.join(SCREEN, "verdicts")
MERGED = os.path.join(SCREEN, "verdicts.jsonl")
INCLUDED = os.path.join(LIT, "screened-in.jsonl")
AUTHOR_FORM = os.path.join(ROOT, "docs", "scoping", "author-screening-sample.md")

BATCH_SIZE = 50
ABSTRACT_CAP = 1800
AUTHOR_SAMPLE_SIZE = 20

DECISIONS = ("include", "exclude")
REASON_CODES = (
    "scheme_ai",              # include: a category scheme for AI disclosure
    "scheme_adjacent",        # include: a scheme in an adjacent disclosure tradition
    "effects_only",           # exclude: measures reactions, offers no scheme
    "detection",              # exclude: telling AI text from human text
    "watermarking",           # exclude: signal hiding without labelling semantics
    "system_documentation",   # exclude: model cards and datasheets
    "legal_exegesis",         # exclude: law commentary with no categories
    "no_text",                # exclude: nothing retrievable to extract from
    "no_structure",           # exclude: asserts a rule, enumerates nothing
    "off_topic",              # exclude: not about disclosure at all
)


def load_jsonl(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    out = []
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def write_jsonl(path: str, rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def seed_from_protocol() -> int:
    """A seed nobody chose: the first 8 hex digits of the protocol hash."""
    with io.open(FROZEN, encoding="utf-8") as fh:
        frozen = json.load(fh)
    return int(frozen["protocol"]["sha256"][:8], 16)


def prepare() -> int:
    records = load_jsonl(RECORDS)
    if not records:
        print("no records; run the search first")
        return 1
    order = list(records)
    random.Random(seed_from_protocol()).shuffle(order)

    os.makedirs(BATCHES, exist_ok=True)
    for old in glob.glob(os.path.join(BATCHES, "batch-*.json")):
        os.remove(old)

    written = 0
    for index in range(0, len(order), BATCH_SIZE):
        chunk = order[index:index + BATCH_SIZE]
        batch_id = f"{index // BATCH_SIZE + 1:03d}"
        payload = {
            "batch_id": batch_id,
            "criteria": "docs/scoping/protocol.md, section 3",
            "decisions": list(DECISIONS),
            "reason_codes": list(REASON_CODES),
            "records": [{
                "rec_id": row["rec_id"],
                "title": row["title"],
                "year": row["year"],
                "venue": row["venue"],
                "record_type": row["record_type"],
                "abstract": (row["abstract"][:ABSTRACT_CAP] +
                             (" [abstract truncated]" if len(row["abstract"]) > ABSTRACT_CAP
                              else "")),
            } for row in chunk],
        }
        path = os.path.join(BATCHES, f"batch-{batch_id}.json")
        with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        written += 1
    print(f"{len(order)} records into {written} batches of up to {BATCH_SIZE}")
    print(f"batches in {BATCHES}")
    return 0


def ingest() -> int:
    """Read verdict files, check them against the batches, merge."""
    batch_index: dict[str, set[str]] = {}
    for path in sorted(glob.glob(os.path.join(BATCHES, "batch-*.json"))):
        with io.open(path, encoding="utf-8") as fh:
            batch = json.load(fh)
        batch_index[batch["batch_id"]] = {r["rec_id"] for r in batch["records"]}

    rows: dict[tuple[str, str], dict] = {}
    problems: list[str] = []
    files = sorted(glob.glob(os.path.join(VERDICTS, "*.json")))
    if not files:
        print(f"no verdict files in {VERDICTS}")
        return 1

    for path in files:
        with io.open(path, encoding="utf-8") as fh:
            payload = json.load(fh)
        screener = payload.get("screener", "")
        batch_id = payload.get("batch_id", "")
        name = os.path.basename(path)
        if screener not in ("A", "B"):
            problems.append(f"{name}: screener must be A or B, got {screener!r}")
            continue
        expected = batch_index.get(batch_id)
        if expected is None:
            problems.append(f"{name}: unknown batch {batch_id!r}")
            continue
        seen = set()
        for verdict in payload.get("verdicts", []):
            rec_id = verdict.get("rec_id", "")
            if rec_id not in expected:
                problems.append(f"{name}: {rec_id} is not in batch {batch_id}")
                continue
            if verdict.get("decision") not in DECISIONS:
                problems.append(f"{name}: {rec_id} decision {verdict.get('decision')!r}")
                continue
            if verdict.get("reason_code") not in REASON_CODES:
                problems.append(f"{name}: {rec_id} reason {verdict.get('reason_code')!r}")
                continue
            seen.add(rec_id)
            rows[(rec_id, screener)] = {
                "rec_id": rec_id, "screener": screener, "batch_id": batch_id,
                "decision": verdict["decision"], "reason_code": verdict["reason_code"],
                "note": verdict.get("note", ""),
            }
        missing = expected - seen
        if missing:
            problems.append(f"{name}: {len(missing)} records in the batch got no verdict")

    write_jsonl(MERGED, list(rows.values()))
    print(f"{len(rows)} verdicts from {len(files)} files -> {MERGED}")
    if problems:
        print(f"\n{len(problems)} problems:")
        for problem in problems[:40]:
            print(f"  {problem}")
        if len(problems) > 40:
            print(f"  ... and {len(problems) - 40} more")
        return 1
    return 0


def _paired() -> tuple[list[str], list[str], list[str]]:
    """Records judged by both screeners, as two aligned decision lists."""
    verdicts = load_jsonl(MERGED)
    by_rec: dict[str, dict[str, str]] = {}
    for row in verdicts:
        by_rec.setdefault(row["rec_id"], {})[row["screener"]] = row["decision"]
    ids = sorted(rec for rec, seen in by_rec.items() if "A" in seen and "B" in seen)
    return ids, [by_rec[r]["A"] for r in ids], [by_rec[r]["B"] for r in ids]


def agreement() -> int:
    ids, a, b = _paired()
    if not ids:
        print("no record has a verdict from both screeners")
        return 1
    kappa, parts = cohens_kappa(a, b)
    print(f"records judged by both screeners: {len(ids)}")
    print(f"Cohen kappa A vs B: {kappa:.3f} ({interpret(kappa)})")
    for key, value in parts.items():
        print(f"  {key}: {value}")

    disagreed = [r for r, x, y in zip(ids, a, b) if x != y]
    print(f"\ndisagreements: {len(disagreed)} "
          f"({100 * len(disagreed) / len(ids):.1f} per cent), all of them included")

    with io.open(os.path.join(LIT, "queries.json"), encoding="utf-8") as fh:
        spec = json.load(fh)
    records = {row["rec_id"]: row for row in load_jsonl(RECORDS)}
    verdict_by_rec: dict[str, dict[str, str]] = {}
    for row in load_jsonl(MERGED):
        verdict_by_rec.setdefault(row["rec_id"], {})[row["screener"]] = row["decision"]

    print("\ncalibration items (expected verdict never shown to a screener):")
    for item in spec.get("calibration", []):
        ref = item["ref"].lower()
        hit = None
        for rec_id, row in records.items():
            if row.get("doi") == ref or row.get("arxiv_id") == item["ref"]:
                hit = rec_id
                break
        if hit is None:
            print(f"  {item['ref']}: not in the record set at all")
            continue
        got = verdict_by_rec.get(hit, {})
        agreed = [s for s, d in got.items() if d == item["expected"]]
        print(f"  {item['ref']}: expected {item['expected']}, "
              f"A={got.get('A', '-')} B={got.get('B', '-')} "
              f"({len(agreed)} of {len(got)} matched)")
    return 0


def decide() -> int:
    """Recall first: one include is enough to send a record to full text."""
    verdicts = load_jsonl(MERGED)
    if not verdicts:
        print("no verdicts")
        return 1
    by_rec: dict[str, list[dict]] = {}
    for row in verdicts:
        by_rec.setdefault(row["rec_id"], []).append(row)

    records = {row["rec_id"]: row for row in load_jsonl(RECORDS)}
    kept = []
    for rec_id, rows in by_rec.items():
        includes = [r for r in rows if r["decision"] == "include"]
        if not includes:
            continue
        record = dict(records.get(rec_id, {}))
        record["screening"] = {
            "included_by": sorted(r["screener"] for r in includes),
            "reason_codes": sorted({r["reason_code"] for r in includes}),
            "unanimous": len(includes) == len(rows),
            "notes": [r["note"] for r in rows if r["note"]],
        }
        kept.append(record)

    write_jsonl(INCLUDED, kept)
    unanimous = sum(1 for r in kept if r["screening"]["unanimous"])
    print(f"{len(by_rec)} records screened, {len(kept)} included "
          f"({unanimous} unanimously, {len(kept) - unanimous} on one screener's vote)")
    print(f"wrote {INCLUDED}")
    return 0


def sample() -> int:
    """A blind screening form for the author.

    He sees title, year, venue and abstract, and nothing about what the agents
    decided. The form is markdown because he will fill it in by hand.
    """
    records = load_jsonl(RECORDS)
    if not records:
        print("no records")
        return 1
    picked = random.Random(seed_from_protocol() + 1).sample(
        records, min(AUTHOR_SAMPLE_SIZE, len(records)))

    lines = [
        "# Blind screening sample for the author",
        "",
        f"{len(picked)} records drawn at random with a seed derived from the protocol",
        "hash. The agents' verdicts are deliberately not shown. Write `include` or",
        "`exclude` on each line, and a reason code from section 3 of the protocol if",
        "you have one. Human versus agent kappa is computed from this file.",
        "",
        "Criteria: `docs/scoping/protocol.md`, section 3.",
        "",
    ]
    for index, row in enumerate(picked, 1):
        abstract = row["abstract"][:900] + (" [...]" if len(row["abstract"]) > 900 else "")
        lines += [
            f"## {index}. {row['title'] or '(no title)'}",
            "",
            f"- rec_id: `{row['rec_id']}`",
            f"- {row['year'] or 'no year'}, {row['venue'] or 'no venue'}, "
            f"{row['record_type'] or 'no type'}",
            f"- abstract: {abstract or '(no abstract retrieved)'}",
            "",
            "**Your decision:** ",
            "",
        ]
    os.makedirs(os.path.dirname(AUTHOR_FORM), exist_ok=True)
    with io.open(AUTHOR_FORM, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines))
    print(f"wrote {AUTHOR_FORM} with {len(picked)} records")
    return 0


ACTIONS = {"prepare": prepare, "ingest": ingest, "agreement": agreement,
           "decide": decide, "sample": sample}


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action not in ACTIONS:
        print(__doc__)
        sys.exit(2)
    sys.exit(ACTIONS[action]())
