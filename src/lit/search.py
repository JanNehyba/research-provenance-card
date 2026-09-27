"""Run the frozen query set and pool the results into one record file.

    python -m src.lit.search            run the searches, write data/lit/
    python -m src.lit.search --replay   re-run and report how the counts moved

Two things this module is careful about.

**Deduplication is two-stage.** First by identifier, then by normalised title,
because the same paper arrives from OpenAlex with a DOI and from arXiv without
one, and those produce different identifiers. The record that carries a DOI wins
and the others are merged into it, so nothing is lost: the merged record
remembers every API and every query that found it, which is what the PRISMA flow
needs.

**Replay is expected to disagree.** Indexes move. A replay that returned exactly
the same counts weeks later would be more suspicious than one that did not, so
the difference is printed rather than hidden, and the report cites it.
"""

from __future__ import annotations

import io
import json
import os
import sys
import time
from dataclasses import asdict

from . import sources
from .sources import Record

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUERIES = os.path.join(ROOT, "data", "lit", "queries.json")
RECORDS = os.path.join(ROOT, "data", "lit", "records.jsonl")
LOG = os.path.join(ROOT, "data", "lit", "search-log.json")

MIN_TITLE_FOR_DEDUP = 25


def load_queries() -> dict:
    with io.open(QUERIES, encoding="utf-8") as fh:
        return json.load(fh)


class Pool:
    """Records keyed by identifier, with title-level deduplication on top."""

    def __init__(self) -> None:
        self.by_id: dict[str, dict] = {}
        self.title_to_id: dict[str, str] = {}

    def add(self, rec: Record) -> bool:
        """Add a record. Returns True if it was new, False if merged into one."""
        row = asdict(rec)
        row["also_found_in"] = [rec.api]
        norm_title = sources.normalise_title(rec.title)

        target_id = None
        if rec.rec_id in self.by_id:
            target_id = rec.rec_id
        elif len(norm_title) >= MIN_TITLE_FOR_DEDUP and norm_title in self.title_to_id:
            target_id = self.title_to_id[norm_title]

        if target_id is None:
            self.by_id[rec.rec_id] = row
            if len(norm_title) >= MIN_TITLE_FOR_DEDUP:
                self.title_to_id[norm_title] = rec.rec_id
            return True

        self._merge(self.by_id[target_id], row)
        return False

    @staticmethod
    def _merge(kept: dict, incoming: dict) -> None:
        """Fill gaps in the kept record from the duplicate, never overwrite.

        A longer abstract does replace a shorter one: services truncate
        abstracts differently and the screeners read this field, so more text is
        strictly better. Everything else is first-come, because the first
        record's identifiers have already been used to key the pool.
        """
        for key in ("doi", "arxiv_id", "pmcid", "pmid", "venue", "year", "url",
                    "record_type", "oa_pdf_url"):
            if not kept.get(key) and incoming.get(key):
                kept[key] = incoming[key]
        if len(incoming.get("abstract", "")) > len(kept.get("abstract", "")):
            kept["abstract"] = incoming["abstract"]
        for key in ("found_by", "also_found_in"):
            merged = list(dict.fromkeys(kept.get(key, []) + incoming.get(key, [])))
            kept[key] = merged


def run_queries(spec: dict, pool: Pool) -> list[dict]:
    log_rows = []
    for entry in spec["queries"]:
        source_name = entry["source"]
        fn = sources.SEARCH_FUNCTIONS.get(source_name)
        if fn is None:
            print(f"[{entry['id']}] unknown source {source_name}, skipped")
            continue
        print(f"[{entry['id']}] {source_name}: {entry['query'][:70]}")
        found = fn(entry["query"], entry.get("max_records", 60), entry["id"])
        new = sum(1 for rec in found if pool.add(rec))
        print(f"    returned {len(found)}, new {new}")
        log_rows.append({
            "query_id": entry["id"], "block": entry["block"], "source": source_name,
            "query": entry["query"], "returned": len(found), "new": new,
            "ran_at": time.strftime("%Y-%m-%d %H:%M"),
        })
    return log_rows


def run_known_items(spec: dict, pool: Pool) -> list[dict]:
    """Fetch the schemes already named, so a gap in block 1 becomes visible."""
    log_rows = []
    for item in spec.get("known_ids", {}).get("arxiv", []):
        rec = sources.arxiv_by_id(item["id"])
        status = "not found"
        if rec:
            rec.found_by = [f"known:arxiv:{item['id']}"]
            status = "new" if pool.add(rec) else "already in pool"
        print(f"[known arxiv {item['id']}] {status}")
        log_rows.append({"query_id": f"known:arxiv:{item['id']}", "block": "known",
                         "source": "arxiv", "query": item["id"],
                         "returned": 1 if rec else 0, "new": int(status == "new"),
                         "ran_at": time.strftime("%Y-%m-%d %H:%M"), "why": item["why"]})
    for item in spec.get("known_ids", {}).get("doi", []):
        rec = sources.openalex_by_doi(item["id"])
        if rec is None:
            message = sources.crossref_by_doi(item["id"])
            rec = sources._crossref_record(message) if message else None
        status = "not found"
        if rec:
            rec.found_by = [f"known:doi:{item['id']}"]
            status = "new" if pool.add(rec) else "already in pool"
        print(f"[known doi {item['id']}] {status}")
        log_rows.append({"query_id": f"known:doi:{item['id']}", "block": "known",
                         "source": "openalex_or_crossref", "query": item["id"],
                         "returned": 1 if rec else 0, "new": int(status == "new"),
                         "ran_at": time.strftime("%Y-%m-%d %H:%M"), "why": item["why"]})
    return log_rows


def write_pool(pool: Pool, log_rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(RECORDS), exist_ok=True)
    with io.open(RECORDS, "w", encoding="utf-8", newline="\n") as fh:
        for row in pool.by_id.values():
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    returned = sum(row["returned"] for row in log_rows)
    payload = {
        "ran_at": time.strftime("%Y-%m-%d %H:%M"),
        "records_returned_total": returned,
        "records_unique": len(pool.by_id),
        "duplicates_merged": returned - len(pool.by_id),
        "queries": log_rows,
    }
    with io.open(LOG, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\nreturned {returned}, unique {len(pool.by_id)}, "
          f"merged {returned - len(pool.by_id)}")
    print(f"wrote {RECORDS}\nwrote {LOG}")


def replay() -> int:
    """Re-run the queries and report count movement, writing nothing."""
    if not os.path.exists(LOG):
        print("no search log to replay against")
        return 1
    with io.open(LOG, encoding="utf-8") as fh:
        old = {row["query_id"]: row for row in json.load(fh)["queries"]}
    spec = load_queries()
    pool = Pool()
    rows = run_queries(spec, pool)
    print("\nquery_id  then  now  change")
    moved = 0
    for row in rows:
        was = old.get(row["query_id"], {}).get("returned")
        if was is None:
            print(f"{row['query_id']:>8}  {'-':>4}  {row['returned']:>3}  new query")
            continue
        delta = row["returned"] - was
        if delta:
            moved += 1
        print(f"{row['query_id']:>8}  {was:>4}  {row['returned']:>3}  {delta:+d}")
    print(f"\n{moved} of {len(rows)} queries returned a different count. "
          "Index drift is expected; the report states this figure.")
    return 0


def main() -> int:
    if "--replay" in sys.argv:
        return replay()
    spec = load_queries()
    pool = Pool()
    log_rows = run_queries(spec, pool)
    log_rows += run_known_items(spec, pool)
    write_pool(pool, log_rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
