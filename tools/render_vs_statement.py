#!/usr/bin/env python3
"""Render a human-readable statement from a draft AI disclosure record.

Companion to `tools/generate_disclosure.py`, which does the same job for RPC cards and
publisher templates. Reuses that module's `render_template` so both tools substitute
placeholders the same way.

The point of this tool is the answer to consultation question 2 (placement): the machine
table and the Methods paragraph are two renderings of one record, generated rather than
written twice. Two hand-written descriptions of the same facts diverge, and a divergence
between them is indistinguishable from misconduct.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_disclosure import render_template  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TAXONOMY = ROOT / "docs" / "vancouver" / "kit" / "vs-taxonomy-round2.json"

VERIFICATION_PHRASES = {
    "not_checked": "not checked",
    "read_through": "read through by the author",
    "sampled": "sampled",
    "recomputed": "re-executed and recomputed",
    "cross_checked_primary_sources": "cross-checked against primary sources",
    "checked_by_named_third_party": "checked by a named third party",
    "independently_reproduced": "independently reproduced",
}

ACCESS_PHRASES = {
    "public": "public",
    "embargoed": "embargoed",
    "on_request": "on request",
    "restricted": "restricted",
    "not_retained": "not retained",
}


def load_task_labels(taxonomy_path: Path) -> dict[str, str]:
    """Map task identifier -> label. Missing file or unknown id is not an error:
    the identifier is then printed as-is, which is what a consumer of an unknown
    vocabulary version should do."""
    if not taxonomy_path.is_file():
        return {}
    data = json.loads(taxonomy_path.read_text(encoding="utf-8"))
    labels = {}
    for entry in data.get("categories", []) + data.get("proposed_additions", []):
        key = entry.get("suggested_id")
        if key:
            labels[key] = entry.get("label", key)
    return labels


def describe_actor(actor: dict) -> str:
    if actor.get("kind") == "human":
        orcid = actor.get("orcid")
        return f"human ({orcid})" if orcid else "human"
    parts = [actor.get("provider", ""), actor.get("model_family", "")]
    name = " ".join(p for p in parts if p).strip() or "unspecified AI system"
    version = actor.get("model_version_or_snapshot")
    interface = actor.get("interface")
    if version:
        name = f"{name} {version}"
    if interface:
        name = f"{name}, {interface}"
    return name


def describe_trace(row: dict) -> str:
    trace = row.get("trace")
    if not trace:
        return "no record retained"
    bits = [f"{trace.get('type', 'record')}: {ACCESS_PHRASES.get(trace.get('access_status', ''), trace.get('access_status', ''))}"]
    if trace.get("uri_or_pid"):
        bits.append(trace["uri_or_pid"])
    if trace.get("sha256"):
        bits.append(f"sha256 {trace['sha256'][:12]}...")
    else:
        bits.append("no hash")
    if trace.get("curation"):
        bits.append("curated, two-hash record")
    return "; ".join(bits)


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def render_table(record: dict, labels: dict[str, str]) -> str:
    lines = [
        "| Task | Actor | What was checked | Trace | What could not be checked |",
        "|---|---|---|---|---|",
    ]
    for row in record.get("disclosures", []):
        task = row.get("task", "")
        label = labels.get(task, task)
        verification = VERIFICATION_PHRASES.get(row.get("verification", ""), row.get("verification", ""))
        detail = row.get("verification_detail")
        if detail:
            verification = f"{verification} ({detail})"
        lines.append(
            "| {task} <br>`{id}` | {actor} | {verification} | {trace} | {not_verified} |".format(
                task=md_escape(label),
                id=md_escape(task),
                actor=md_escape(describe_actor(row.get("actor", {}))),
                verification=md_escape(verification),
                trace=md_escape(describe_trace(row)),
                not_verified=md_escape(row.get("not_verified", "")),
            )
        )
    if len(lines) == 2:
        lines.append("| _no use met the disclosure threshold_ | | | | |")
    return "\n".join(lines)


def render_narrative(record: dict, labels: dict[str, str]) -> str:
    rows = record.get("disclosures", [])
    if not rows:
        return "No AI use meeting the disclosure threshold occurred in the preparation of this work."

    ai_rows = [r for r in rows if r.get("actor", {}).get("kind") == "ai"]
    human_rows = [r for r in rows if r.get("actor", {}).get("kind") != "ai"]

    sentences = []

    if ai_rows:
        systems = sorted({describe_actor(r.get("actor", {})) for r in ai_rows})
        tasks = [labels.get(r.get("task", ""), r.get("task", "")).lower() for r in ai_rows]
        sentences.append(
            "AI ({systems}) was used for: {tasks}.".format(
                systems="; ".join(systems),
                tasks=", ".join(tasks),
            )
        )

    for row in human_rows:
        sentences.append(
            "{label}: {actor}.".format(
                label=labels.get(row.get("task", ""), row.get("task", "")),
                actor=describe_actor(row.get("actor", {})),
            )
        )

    by_verification: dict[str, list[str]] = {}
    for row in rows:
        by_verification.setdefault(row.get("verification", ""), []).append(
            labels.get(row.get("task", ""), row.get("task", "")).lower()
        )
    checked_bits = [
        "{tasks} - {phrase}".format(
            tasks=", ".join(tasks),
            phrase=VERIFICATION_PHRASES.get(level, level),
        )
        for level, tasks in by_verification.items()
    ]
    sentences.append("Verification: " + "; ".join(checked_bits) + ".")

    def access_of(row: dict) -> str | None:
        trace = row.get("trace")
        return trace.get("access_status") if trace else None

    restricted = [r for r in rows if access_of(r) in ("embargoed", "on_request", "restricted")]
    if restricted:
        sentences.append(
            "Records of {count} of these uses exist but are not public; the reason is stated for each in the structured statement.".format(
                count=len(restricted)
            )
        )
    no_record = [r for r in rows if access_of(r) in (None, "not_retained")]
    if no_record:
        sentences.append(
            "For {count} of these uses no durable record was retained.".format(count=len(no_record))
        )

    sentences.append(
        "Limits of verification are stated per use in the structured statement rather than summarised here, "
        "because a summary is where they stop being checkable."
    )
    return " ".join(sentences)


def build_variables(record: dict, labels: dict[str, str], source: str) -> dict[str, str]:
    work = record.get("work", {})
    guarantor = record.get("guarantor", {})
    null_declaration = record.get("null_declaration", {})
    responsibility = record.get("responsibility_statement", {})
    taxonomy = record.get("taxonomy", {})

    guarantor_line = guarantor.get("name", "")
    if guarantor.get("orcid"):
        guarantor_line = f"{guarantor_line} (ORCID: {guarantor['orcid']})"

    null_text = null_declaration.get("statement", "")
    null_scope = "Threshold: {threshold}. Task vocabulary: {taxonomy}.".format(
        threshold=null_declaration.get("threshold_version", "unspecified"),
        taxonomy=null_declaration.get("taxonomy_version", "unspecified"),
    )
    if null_declaration.get("subject_sha256"):
        null_scope += " Asserted about the file with SHA-256 {sha}.".format(
            sha=null_declaration["subject_sha256"]
        )

    responsibility_text = responsibility.get("text", "")
    if responsibility.get("accepted_by"):
        accepted = responsibility["accepted_by"]
        if responsibility.get("accepted_by_orcid"):
            accepted = f"{accepted} (ORCID: {responsibility['accepted_by_orcid']})"
        responsibility_text = f"{responsibility_text} Accepted by: {accepted}."

    return {
        "work_title": str(work.get("title", "")),
        "work_version": str(work.get("version", "")),
        "work_sha256": str(work.get("pdf_sha256", "not bound to a content hash")),
        "guarantor": guarantor_line,
        "guarantor_timestamp": str(guarantor.get("timestamp", "")),
        "taxonomy": "{v} ({ver})".format(
            v=taxonomy.get("vocabulary", "unspecified"),
            ver=taxonomy.get("version", "unspecified"),
        ),
        "disclosure_table": render_table(record, labels),
        "disclosure_narrative": render_narrative(record, labels),
        "null_declaration": null_text,
        "null_declaration_scope": null_scope,
        "responsibility_statement": responsibility_text,
        "no_certification": str(
            record.get(
                "no_certification",
                "This record documents process and evidence. It is not a quality, accuracy or truth certification of the work.",
            )
        ),
        "source_file": source,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a human-readable statement from a draft AI disclosure record."
    )
    parser.add_argument("record_json", help="Path to a vs-disclosure-draft record")
    parser.add_argument(
        "template_txt",
        nargs="?",
        default=str(ROOT / "tools" / "templates" / "vs_statement.txt"),
        help="Template file path",
    )
    parser.add_argument("--taxonomy", default=str(DEFAULT_TAXONOMY), help="Taxonomy file for task labels")
    parser.add_argument("--out", help="Output file path; defaults to stdout")
    args = parser.parse_args()

    record = json.loads(Path(args.record_json).read_text(encoding="utf-8"))
    template = Path(args.template_txt).read_text(encoding="utf-8")
    labels = load_task_labels(Path(args.taxonomy))

    # Name the record relative to the repository, so the rendering is identical whether the
    # tool was called with a relative or an absolute path. The output is committed and
    # compared byte-for-byte in the test suite.
    resolved = Path(args.record_json).resolve()
    try:
        source = resolved.relative_to(ROOT).as_posix()
    except ValueError:
        source = Path(args.record_json).as_posix()

    output = render_template(template, build_variables(record, labels, source))

    if args.out:
        # newline="" keeps the LF endings of the template, so the committed rendering
        # stays byte-identical across platforms.
        with open(args.out, "w", encoding="utf-8", newline="") as f:
            f.write(output)
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
