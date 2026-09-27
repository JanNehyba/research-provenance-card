"""Group the extracted schemes, and check the language rule.

    python -m src.lit.merge schemes    cluster candidates for the scheme merge
    python -m src.lit.merge language   flag records that are not English or Czech
    python -m src.lit.merge check      validate scheme-merge.json against the data

Two problems this module exists for, both discovered from the extraction output
rather than anticipated.

**The same scheme arrives under different names.** Each extraction agent works on
its own packet and invents its own `scheme_id`, so CRediT came back as
`credit-taxonomy`, `casrai-credit`, `credit-contributor-roles` and more. The
protocol says one scheme with several source references, but no agent could have
known that. Clustering therefore happens here, once, over everything.

**Records slipped through the language rule.** The protocol restricts the review
to English and Czech. Extraction turned up a Portuguese conflict-of-interest
form, a Dutch C2PA report and a Turkish advertising typology, which means the
screeners did not apply the rule reliably. Rather than quietly keep or quietly
drop them, this flags them by a stopword ratio so the count is reportable and the
decision is visible.
"""

from __future__ import annotations

import io
import json
import os
import re
import sys

from .console import init as console_init
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIT = os.path.join(ROOT, "data", "lit")
SCHEMES = os.path.join(LIT, "schemes.jsonl")
FULLTEXT = os.path.join(LIT, "fulltext")
GROUPS = os.path.join(LIT, "scheme-groups.json")
MERGE = os.path.join(LIT, "scheme-merge.json")
LANGUAGE = os.path.join(LIT, "language-flags.json")

SIMILARITY = 0.6

# Function words, which appear in any text of any length in their language and
# hardly ever elsewhere. Crude on purpose: the point is a number a reader can
# check, not a language identifier.
STOPWORDS = {
    "en": ("the", "and", "of", "that", "with", "which", "this", "from", "have"),
    "cs": ("je", "se", "na", "pro", "které", "být", "nebo", "podle", "však"),
    "de": ("der", "die", "und", "des", "nicht", "eine", "werden", "auch"),
    "nl": ("het", "een", "van", "niet", "wordt", "deze", "voor", "zijn"),
    "pt": ("que", "não", "para", "uma", "dos", "como", "pelo", "sua"),
    "es": ("que", "los", "una", "por", "con", "para", "como", "sus"),
    "fr": ("les", "des", "une", "pour", "dans", "est", "que", "sur"),
    "tr": ("bir", "ile", "olarak", "için", "bu", "ve", "olan", "daha"),
    "it": ("che", "per", "del", "una", "con", "non", "sono", "nella"),
}
ALLOWED = ("en", "cs")


def load_jsonl(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    rows = []
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def norm_name(name: str) -> str:
    name = re.sub(r"\(.*?\)", " ", name.lower())
    name = re.sub(r"\b(the|a|an|of|for|and|its|version)\b", " ", name)
    name = re.sub(r"\b(framework|taxonomy|typology|scheme|model|scale|checklist|"
                  r"guideline|guidelines|standard|index|instrument|rubric)\b", " ", name)
    return re.sub(r"[^a-z0-9]+", "", name)


def _scheme_view(rows: list[dict]) -> dict[str, dict]:
    view: dict[str, dict] = {}
    for row in rows:
        entry = view.setdefault(row["scheme_id"], {
            "scheme_id": row["scheme_id"],
            "names": set(),
            "domains": set(),
            "artifact_types": set(),
            "rec_ids": set(),
            "source_refs": set(),
            "labels": set(),
        })
        if row["scheme_name_verbatim"] and row["scheme_name_verbatim"] != "not_stated":
            entry["names"].add(row["scheme_name_verbatim"])
        entry["domains"].add(row["domain"])
        entry["artifact_types"].add(row["artifact_type"])
        entry["rec_ids"].add(row["rec_id"])
        entry["source_refs"].add(row["source_ref"])
        entry["labels"].add(row["dimension_label_verbatim"].lower().strip())
    return view


def schemes() -> int:
    rows = load_jsonl(SCHEMES)
    if not rows:
        print("no verified schemes yet")
        return 1
    view = _scheme_view(rows)

    # First pass: identical normalised name. Second pass: overlapping dimension
    # labels, which catches the schemes nobody named.
    by_name: dict[str, list[str]] = defaultdict(list)
    unnamed: list[str] = []
    for scheme_id, entry in view.items():
        keys = {norm_name(n) for n in entry["names"] if norm_name(n)}
        if keys:
            for key in keys:
                by_name[key].append(scheme_id)
        else:
            unnamed.append(scheme_id)

    clusters: list[dict] = []
    seen: set[str] = set()
    for key, members in sorted(by_name.items(), key=lambda kv: -len(kv[1])):
        members = [m for m in members if m not in seen]
        if not members:
            continue
        seen.update(members)
        clusters.append({
            "reason": "same normalised name",
            "key": key,
            "members": sorted(members),
            "names": sorted({n for m in members for n in view[m]["names"]}),
            "domains": sorted({d for m in members for d in view[m]["domains"]}),
            "papers": sum(len(view[m]["rec_ids"]) for m in members),
        })

    for scheme_id in unnamed:
        if scheme_id in seen:
            continue
        labels = view[scheme_id]["labels"]
        members = [scheme_id]
        for other in unnamed:
            if other == scheme_id or other in seen:
                continue
            other_labels = view[other]["labels"]
            if not labels or not other_labels:
                continue
            overlap = len(labels & other_labels) / len(labels | other_labels)
            if overlap >= SIMILARITY:
                members.append(other)
        seen.update(members)
        if len(members) > 1:
            clusters.append({
                "reason": f"dimension labels overlap at least {SIMILARITY}",
                "key": "",
                "members": sorted(members),
                "names": [],
                "domains": sorted({d for m in members for d in view[m]["domains"]}),
                "papers": sum(len(view[m]["rec_ids"]) for m in members),
            })

    singletons = sorted(set(view) - {m for c in clusters for m in c["members"]})
    payload = {
        "note": ("Candidate groupings only. The merge itself is a judgement and "
                 "belongs in scheme-merge.json, which `check` validates against "
                 "this data. Clustering by name is blind to schemes nobody named, "
                 "and clustering by label overlap will miss two renderings of one "
                 "scheme that use different words for the same axis."),
        "distinct_scheme_ids": len(view),
        "clusters": sorted(clusters, key=lambda c: -len(c["members"])),
        "singletons": singletons,
        "scheme_detail": {
            scheme_id: {
                "names": sorted(entry["names"]),
                "domains": sorted(entry["domains"]),
                "artifact_types": sorted(entry["artifact_types"]),
                "papers": sorted(entry["rec_ids"]),
                "source_refs": sorted(entry["source_refs"]),
                "dimension_count": len(entry["labels"]),
            } for scheme_id, entry in sorted(view.items())
        },
    }
    with io.open(GROUPS, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    multi = [c for c in clusters if len(c["members"]) > 1]
    print(f"{len(view)} distinct scheme ids")
    print(f"{len(multi)} candidate clusters with more than one member")
    print(f"{len(singletons)} singletons")
    print(f"wrote {GROUPS}")
    for cluster in multi[:12]:
        names = ", ".join(cluster["names"][:2]) or "(unnamed)"
        print(f"  {len(cluster['members']):>2} members  {names[:60]}")
    return 0


def guess_language(text: str) -> tuple[str, dict]:
    words = re.findall(r"[^\W\d_]+", text.lower(), flags=re.UNICODE)
    if len(words) < 50:
        return "unknown", {}
    counts = Counter(words)
    scores = {lang: sum(counts[w] for w in stops) / len(words)
              for lang, stops in STOPWORDS.items()}
    best = max(scores, key=lambda lang: scores[lang])
    return best, {lang: round(score, 5) for lang, score in
                  sorted(scores.items(), key=lambda kv: -kv[1])[:4]}


def language() -> int:
    rows = load_jsonl(SCHEMES)
    if not rows:
        print("no verified schemes yet")
        return 1
    rec_ids = sorted({row["rec_id"] for row in rows})
    flags = []
    for rec_id in rec_ids:
        path = os.path.join(FULLTEXT, f"{rec_id}.txt")
        if not os.path.exists(path):
            continue
        with io.open(path, encoding="utf-8") as fh:
            text = fh.read(20000)
        best, scores = guess_language(text)
        if best not in ALLOWED:
            flags.append({"rec_id": rec_id, "guessed": best, "scores": scores,
                          "rows": sum(1 for r in rows if r["rec_id"] == rec_id)})
    payload = {
        "note": ("A stopword ratio, not a language identifier. It is here because "
                 "extraction turned up Portuguese, Dutch and Turkish records, which "
                 "the protocol excludes, so the screeners did not apply the language "
                 "rule reliably. Each record below needs a decision that the report "
                 "states; the method is crude and its own false positives are part "
                 "of what has to be reported."),
        "allowed": list(ALLOWED),
        "records_checked": len(rec_ids),
        "flagged": flags,
    }
    with io.open(LANGUAGE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"checked {len(rec_ids)} records with verified rows")
    print(f"flagged as probably neither English nor Czech: {len(flags)}")
    for flag in flags[:15]:
        print(f"  {flag['rec_id']} guessed {flag['guessed']} "
              f"({flag['rows']} rows) {flag['scores']}")
    print(f"wrote {LANGUAGE}")
    return 0


def check() -> int:
    if not os.path.exists(MERGE):
        print(f"no {MERGE}; run `schemes` first, then write the merge")
        return 1
    rows = load_jsonl(SCHEMES)
    all_ids = {row["scheme_id"] for row in rows}
    with io.open(MERGE, encoding="utf-8") as fh:
        merge = json.load(fh)

    assigned: dict[str, list[str]] = defaultdict(list)
    for group in merge.get("canonical_schemes", []):
        for member in group.get("members", []):
            assigned[member].append(group["canonical_id"])
    out_of_scope = {row["scheme_id"] for row in merge.get("out_of_scope", [])}

    unassigned = sorted(all_ids - set(assigned) - out_of_scope)
    doubled = {sid: ids for sid, ids in assigned.items() if len(ids) > 1}
    unknown = sorted((set(assigned) | out_of_scope) - all_ids)
    both = sorted(set(assigned) & out_of_scope)

    print(f"scheme ids in the data     : {len(all_ids)}")
    print(f"canonical schemes          : {len(merge.get('canonical_schemes', []))}")
    print(f"marked out of scope        : {len(out_of_scope)}")
    for label, items in (("UNASSIGNED", unassigned), ("ASSIGNED TWICE", doubled),
                         ("NOT IN THE DATA", unknown),
                         ("BOTH MERGED AND OUT OF SCOPE", both)):
        if items:
            print(f"\n{label} ({len(items)}):")
            for item in list(items)[:30]:
                print(f"  {item}")
    if unassigned or doubled or unknown or both:
        return 1
    print("\nmerge is complete and one to one")
    return 0


ACTIONS = {"schemes": schemes, "language": language, "check": check}

if __name__ == "__main__":
    console_init()
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action not in ACTIONS:
        print(__doc__)
        sys.exit(2)
    sys.exit(ACTIONS[action]())
