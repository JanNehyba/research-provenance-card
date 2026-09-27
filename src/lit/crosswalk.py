"""Build the dimension vocabulary bottom up, then the crosswalk matrix.

    python -m src.lit.crosswalk labels    export every verbatim label for merging
    python -m src.lit.crosswalk check     validate dimensions.json against the labels
    python -m src.lit.crosswalk matrix    write docs/scoping/crosswalk.md

Merging labels is a judgement, so it is not done here. This module exports the
labels, checks the merge someone else proposed, and renders the result. The check
is what makes the merge auditable: every verbatim label must belong to exactly
one canonical dimension, so a label cannot be quietly dropped because it did not
fit, and cannot be counted twice to make a dimension look better attested.

The eight components of the parent project are mapped onto the vocabulary in a
separate file, read only by `matrix`, and only after the vocabulary is closed.
They are one column of the result, never the frame it was built in.
"""

from __future__ import annotations

import io
import json
import os
import sys

from .console import init as console_init
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIT = os.path.join(ROOT, "data", "lit")
SCHEMES = os.path.join(LIT, "schemes.jsonl")
LABELS = os.path.join(LIT, "labels.json")
DIMENSIONS = os.path.join(LIT, "dimensions.json")
EIGHT = os.path.join(LIT, "eight-components-map.json")
CROSSWALK = os.path.join(ROOT, "docs", "scoping", "crosswalk.md")


def load_jsonl(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    rows = []
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def norm_label(label: str) -> str:
    return " ".join(label.lower().replace("_", " ").split())


def labels() -> int:
    """Export the labels, pre-grouped by exact string match only.

    The pre-grouping is deliberately dumb. Anything cleverer would be the merge
    itself, done by a regex instead of by a reader, and it would not be visible
    in the output.
    """
    rows = load_jsonl(SCHEMES)
    if not rows:
        print("no verified schemes yet")
        return 1

    groups: dict[str, dict] = {}
    for row in rows:
        key = norm_label(row["dimension_label_verbatim"])
        group = groups.setdefault(key, {
            "normalised": key, "verbatim_variants": [], "schemes": [],
            "domains": [], "example_quote": "", "example_values": [],
        })
        if row["dimension_label_verbatim"] not in group["verbatim_variants"]:
            group["verbatim_variants"].append(row["dimension_label_verbatim"])
        if row["scheme_id"] not in group["schemes"]:
            group["schemes"].append(row["scheme_id"])
        if row["domain"] not in group["domains"]:
            group["domains"].append(row["domain"])
        if not group["example_quote"]:
            group["example_quote"] = row["quote"]
        if not group["example_values"] and row["value_list_verbatim"]:
            group["example_values"] = row["value_list_verbatim"]

    ordered = sorted(groups.values(), key=lambda g: (-len(g["schemes"]), g["normalised"]))
    payload = {
        "note": ("Every distinct dimension label from the verified rows, grouped only "
                 "by exact string match. The merge into canonical dimensions is a "
                 "separate, deliberate step and belongs in dimensions.json."),
        "distinct_labels": len(ordered),
        "labels": ordered,
    }
    with io.open(LABELS, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"{len(ordered)} distinct labels from {len(rows)} rows -> {LABELS}")
    print(f"labels appearing in more than one scheme: "
          f"{sum(1 for g in ordered if len(g['schemes']) > 1)}")
    return 0


def batches(size: int = 150) -> int:
    """Split the labels into agent-sized batches for the merge.

    1348 distinct labels came back and only 70 of them repeat, so the merge is
    semantic rather than lexical and cannot be done by string matching. It is
    also too large to do in one pass without losing consistency. The batches are
    ordered by how many schemes a label appears in, so the most attested labels
    are spread across the first batches rather than buried, and each entry
    carries an example quote so a reader can see what the label meant in context.
    """
    if not os.path.exists(LABELS):
        print("run `labels` first")
        return 1
    with io.open(LABELS, encoding="utf-8") as fh:
        groups = json.load(fh)["labels"]

    out_dir = os.path.join(LIT, "merge", "label-batches")
    os.makedirs(out_dir, exist_ok=True)
    for old in os.listdir(out_dir):
        os.remove(os.path.join(out_dir, old))

    written = 0
    for index in range(0, len(groups), size):
        batch_id = f"{index // size + 1:02d}"
        chunk = groups[index:index + size]
        payload = {
            "batch_id": batch_id,
            "labels": [{
                "normalised": g["normalised"],
                "verbatim_variants": g["verbatim_variants"][:4],
                "schemes": len(g["schemes"]),
                "domains": g["domains"],
                "example_values": g["example_values"][:6],
                "example_quote": g["example_quote"][:200],
            } for g in chunk],
        }
        with io.open(os.path.join(out_dir, f"labels-{batch_id}.json"), "w",
                     encoding="utf-8", newline="\n") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        written += 1
    print(f"{len(groups)} labels into {written} batches of up to {size}")
    print(f"batches in {out_dir}")
    return 0


def _load_dimensions() -> list[dict]:
    with io.open(DIMENSIONS, encoding="utf-8") as fh:
        return json.load(fh)["dimensions"]


def check() -> int:
    """Every verbatim label in exactly one canonical dimension, no exceptions."""
    if not os.path.exists(DIMENSIONS):
        print(f"no {DIMENSIONS}; run labels first, then write the merge")
        return 1
    rows = load_jsonl(SCHEMES)
    # Normalised, because that is the form the merge batches show an agent and
    # the form `labels` groups by. Comparing the raw verbatim string here would
    # report labels as unassigned purely because of capitalisation.
    all_labels = {norm_label(row["dimension_label_verbatim"]) for row in rows}
    dims = _load_dimensions()

    assigned: dict[str, list[str]] = defaultdict(list)
    for dim in dims:
        for variant in dim.get("variants", []):
            assigned[norm_label(variant)].append(dim["canonical_id"])

    unassigned = sorted(all_labels - set(assigned))
    doubled = {label: ids for label, ids in assigned.items() if len(ids) > 1}
    unknown = sorted(set(assigned) - all_labels)

    print(f"canonical dimensions : {len(dims)}")
    print(f"verbatim labels      : {len(all_labels)}")
    if unassigned:
        print(f"\nUNASSIGNED ({len(unassigned)}), the merge is incomplete:")
        for label in unassigned[:40]:
            print(f"  {label}")
        if len(unassigned) > 40:
            print(f"  ... and {len(unassigned) - 40} more")
    if doubled:
        print(f"\nASSIGNED TWICE ({len(doubled)}):")
        for label, ids in list(doubled.items())[:20]:
            print(f"  {label} -> {ids}")
    # A variant that matches nothing is reported but does not fail the check.
    # These are labels that existed when the open-coding batches were built and
    # were replaced when three packets were extracted again; they match nothing
    # and cost nothing, and deleting them would hide where the vocabulary came
    # from. A label missing from the merge, or counted twice, is a different
    # matter and still fails.
    if unknown:
        print(f"\nIn the merge but no longer in the data ({len(unknown)}). These are "
              f"stale labels from before a re-extraction, kept for provenance:")
        for label in unknown[:20]:
            print(f"  {label}")
    if unassigned or doubled:
        return 1
    print("\nevery label in the data is in exactly one canonical dimension")
    return 0


def matrix() -> int:
    rows = load_jsonl(SCHEMES)
    if not rows:
        print("no verified schemes")
        return 1
    dims = _load_dimensions()
    label_to_dim = {norm_label(variant): dim["canonical_id"]
                    for dim in dims for variant in dim.get("variants", [])}
    dim_by_id = {dim["canonical_id"]: dim for dim in dims}

    schemes: dict[str, dict] = {}
    for row in rows:
        scheme = schemes.setdefault(row["scheme_id"], {
            "scheme_id": row["scheme_id"],
            "name": row["scheme_name_verbatim"],
            "domain": row["domain"],
            "artifact_type": row["artifact_type"],
            "authority": row["authority"],
            "granularity": row["granularity"],
            "empirical_basis": row["empirical_basis"],
            "machine_readable": row["machine_readable_artifact"],
            "source_ref": row["source_ref"],
            "retrieval_status": row["retrieval_status"],
            "dimensions": set(),
        })
        canonical = label_to_dim.get(norm_label(row["dimension_label_verbatim"]))
        if canonical:
            scheme["dimensions"].add(canonical)

    by_domain: dict[str, Counter] = defaultdict(Counter)
    for scheme in schemes.values():
        for canonical in scheme["dimensions"]:
            by_domain[canonical][scheme["domain"]] += 1

    eight_map = {}
    if os.path.exists(EIGHT):
        with io.open(EIGHT, encoding="utf-8") as fh:
            eight_map = json.load(fh).get("components", {})
    component_of = {}
    for component, canonicals in eight_map.items():
        for canonical in canonicals:
            component_of.setdefault(canonical, []).append(component)

    domains = sorted({s["domain"] for s in schemes.values()})
    lines = [
        "# Crosswalk: dimensions by scheme and by domain",
        "",
        "Generated by `python -m src.lit.crosswalk matrix`. Do not edit by hand; edit",
        "`data/lit/dimensions.json` and regenerate.",
        "",
        f"{len(schemes)} scheme identifiers, {len(dims)} canonical dimensions, "
        f"{len(rows)} verified dimension rows.",
        "",
        "The rows below are keyed by the identifier each extraction agent invented, "
        "not by merged scheme, so an artefact several papers share appears more than "
        "once. `data/lit/scheme-merge.json` holds the merge and the report quotes the "
        "merged count.",
        "",
        "## How often each dimension appears, by domain",
        "",
        "| Dimension | Schemes | " + " | ".join(domains) + " | Eight components |",
        "|---|---:|" + "---:|" * len(domains) + "---|",
    ]
    ordered_dims = sorted(dims, key=lambda d: -sum(by_domain[d["canonical_id"]].values()))
    for dim in ordered_dims:
        canonical = dim["canonical_id"]
        counts = by_domain[canonical]
        total = sum(counts.values())
        cells = " | ".join(str(counts.get(domain, "")) or "." for domain in domains)
        component = ", ".join(component_of.get(canonical, [])) or "not in the eight"
        lines.append(f"| {dim['canonical_label']} | {total} | {cells} | {component} |")

    lines += ["", "## Schemes", "",
              "| Scheme | Domain | Type | Authority | Granularity | Dimensions | "
              "Empirical basis | Machine-readable | Source | Text |",
              "|---|---|---|---|---|---:|---|---|---|---|"]
    for scheme in sorted(schemes.values(), key=lambda s: (s["domain"], s["scheme_id"])):
        lines.append(
            f"| {scheme['name'] or scheme['scheme_id']} | {scheme['domain']} | "
            f"{scheme['artifact_type']} | {scheme['authority']} | "
            f"{scheme['granularity']} | {len(scheme['dimensions'])} | "
            f"{scheme['empirical_basis']} | {scheme['machine_readable']} | "
            f"{scheme['source_ref']} | {scheme['retrieval_status']} |")

    lines += ["", "## Dimensions that appear in only one domain", ""]
    for dim in ordered_dims:
        counts = by_domain[dim["canonical_id"]]
        if len(counts) == 1:
            domain, count = next(iter(counts.items()))
            lines.append(f"- **{dim['canonical_label']}**: {domain} only "
                         f"({count} scheme{'s' if count > 1 else ''})")

    os.makedirs(os.path.dirname(CROSSWALK), exist_ok=True)
    with io.open(CROSSWALK, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {CROSSWALK}: {len(schemes)} schemes, {len(dims)} dimensions")
    return 0


ACTIONS = {"labels": labels, "batches": batches, "check": check,
           "matrix": matrix}

if __name__ == "__main__":
    console_init()
    action = sys.argv[1] if len(sys.argv) > 1 else ""
    if action not in ACTIONS:
        print(__doc__)
        sys.exit(2)
    sys.exit(ACTIONS[action]())
