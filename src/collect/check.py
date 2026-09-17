"""Acceptance checks over the corpus file.

The checks the author set before the corpus can be called built: no item
starts mid-sentence (lower-case first letter), no item contains its own
trigger phrase twice, no item contains an email address, and a summary of the
cell counts so coverage gaps are visible rather than silent.

    python check.py <path-to-corpus.jsonl>
"""

from __future__ import annotations

import io
import json
import random
import sys

from common import EMAIL_RE, GENRES


def check(path: str) -> int:
    rows = []
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))

    bad = 0
    counts: dict[tuple[str, str], int] = {}
    families: dict[str, int] = {}
    for row in rows:
        cell = (row["lang"], row["genre"])
        counts[cell] = counts.get(cell, 0) + 1
        family = row.get("template_family", "")
        families[family or "(free wording)"] = families.get(family or "(free wording)", 0) + 1
        problems = []
        first = next((ch for ch in row["text_verbatim"] if ch.isalpha()), "")
        if first and first.islower():
            problems.append("starts lower case")
        trigger = row.get("trigger_phrase", "")
        if trigger and row["text_verbatim"].lower().count(trigger.lower()) > 1:
            problems.append("trigger repeats")
        if EMAIL_RE.search(row["text_verbatim"]) or EMAIL_RE.search(row.get("context_note", "")):
            problems.append("email address")
        if problems:
            bad += 1
            print(f"FAIL {row['id']}: {'; '.join(problems)} :: {row['text_verbatim'][:60]}")

    print(f"\n{len(rows)} items, {bad} with problems")
    for lang in ("cs", "en"):
        for genre in GENRES:
            print(f"  {lang}/{genre}: {counts.get((lang, genre), 0)}")
    print("\nTemplate families:")
    for family, n in sorted(families.items(), key=lambda kv: -kv[1]):
        print(f"  {family}: {n}")

    print("\n20 random items for the manual read against source:")
    for row in random.sample(rows, min(20, len(rows))):
        print(f"  {row['id']} [{row['lang']}/{row['genre']}] {row['source_url']}")
        print(f"    trigger: {row.get('trigger_phrase', '')!r} family: {row.get('template_family', '')!r}")
        print(f"    text: {row['text_verbatim'][:160]}")
    return bad


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "data/corpus/corpus.jsonl"
    sys.exit(1 if check(target) else 0)
