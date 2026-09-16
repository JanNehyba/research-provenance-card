"""Tests for the Vancouver Standard round-2 implementation kit.

Same shape as tests/test_schema.py: a Draft 2020-12 validator over committed examples,
plus a subprocess smoke test of the renderer, because that is how CI runs it.
"""
import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "docs" / "vancouver" / "kit"
KIT_SCHEMA_PATH = KIT / "vs-disclosure-draft.schema.json"
TAXONOMY_PATH = KIT / "vs-taxonomy-round2.json"
CROSSWALK_PATH = ROOT / "docs" / "vancouver" / "taxonomy-crosswalk-v0.1.json"
EXAMPLES = KIT / "examples"
STATEMENT_PATH = EXAMPLES / "example-statement.md"
RENDERER = ROOT / "tools" / "render_vs_statement.py"
TEMPLATE = ROOT / "tools" / "templates" / "vs_statement.txt"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def kit_validator():
    return Draft202012Validator(load_json(KIT_SCHEMA_PATH))


@pytest.fixture(scope="module")
def taxonomy():
    return load_json(TAXONOMY_PATH)


@pytest.fixture(scope="module")
def example():
    return load_json(EXAMPLES / "example-disclosure.json")


def test_example_disclosure_is_valid(kit_validator, example):
    assert list(kit_validator.iter_errors(example)) == []


def test_broken_disclosure_fails_on_the_missing_verification_fields(kit_validator):
    payload = load_json(EXAMPLES / "example-disclosure-broken.json")
    messages = [e.message for e in kit_validator.iter_errors(payload)]
    assert any("'verification' is a required property" in m for m in messages), messages
    assert any("'not_verified' is a required property" in m for m in messages), messages


def test_sampled_verification_requires_a_detail(kit_validator, example):
    payload = copy.deepcopy(example)
    payload["disclosures"][0]["verification"] = "sampled"
    messages = [e.message for e in kit_validator.iter_errors(payload)]
    assert any("verification_detail" in m for m in messages), messages


def test_curated_trace_requires_the_two_hash_record(kit_validator, example):
    """Appendix B of the submission: a published curated log must carry the raw hash,
    the curation rule and the kinds of material removed."""
    payload = copy.deepcopy(example)
    payload["disclosures"][0]["trace"] = {
        "type": "log",
        "uri_or_pid": "https://doi.org/10.0000/example",
        "sha256": "a" * 64,
        "access_status": "public",
        "curation": {
            "raw_sha256": "b" * 64,
            "raw_access_status": "restricted",
            "rule": "Removed passages containing third-party unpublished material and personal data.",
            "removed_kinds": ["third-party unpublished material", "personal data"],
        },
    }
    assert list(kit_validator.iter_errors(payload)) == []

    del payload["disclosures"][0]["trace"]["curation"]["rule"]
    messages = [e.message for e in kit_validator.iter_errors(payload)]
    assert any("'rule' is a required property" in m for m in messages), messages


def test_non_public_trace_requires_a_reason(kit_validator, example):
    payload = copy.deepcopy(example)
    payload["disclosures"][0]["trace"] = {"type": "log", "access_status": "restricted"}
    messages = [e.message for e in kit_validator.iter_errors(payload)]
    assert any("'restriction_reason' is a required property" in m for m in messages), messages


def test_taxonomy_has_eighteen_categories_with_unique_slugs(taxonomy):
    categories = taxonomy["categories"]
    assert len(categories) == 18
    assert [c["number"] for c in categories] == list(range(1, 19))

    slugs = [c["suggested_id"] for c in categories] + [
        a["suggested_id"] for a in taxonomy["proposed_additions"]
    ]
    assert len(slugs) == len(set(slugs))
    assert all(s.startswith("vs:") for s in slugs)


def test_taxonomy_invents_no_definitions(taxonomy):
    """The source document says definitions are still to be drafted. Supplying one here
    would put words into a proposal under consultation."""
    for entry in taxonomy["categories"] + taxonomy["proposed_additions"]:
        assert entry["definition"] is None, entry["suggested_id"]


def test_taxonomy_declares_its_unofficial_status_and_source(taxonomy):
    provenance = taxonomy["provenance"]
    assert "UNOFFICIAL" in provenance["status"]
    assert provenance["source_document"] == "WCRI2026FT_PrepReadingRound2_v45.pdf"
    assert provenance["source_retrieved"]
    assert taxonomy["rights"]["category_labels"]


def test_design_children_point_at_a_declared_parent(taxonomy):
    group_ids = {g["suggested_id"] for g in taxonomy["groups"]}
    parents = {c["parent"] for c in taxonomy["categories"] if c["parent"]}
    assert parents, "categories 5-7 should carry an explicit parent"
    assert parents <= group_ids


def test_taxonomy_and_crosswalk_agree_on_slugs(taxonomy):
    crosswalk = load_json(CROSSWALK_PATH)
    taxonomy_slugs = {c["number"]: c["suggested_id"] for c in taxonomy["categories"]}
    crosswalk_slugs = {c["number"]: c["suggested_id"] for c in crosswalk["categories"]}
    assert taxonomy_slugs == crosswalk_slugs

    taxonomy_labels = {c["number"]: c["label"] for c in taxonomy["categories"]}
    crosswalk_labels = {c["number"]: c["label"] for c in crosswalk["categories"]}
    assert taxonomy_labels == crosswalk_labels

    assert {a["suggested_id"] for a in taxonomy["proposed_additions"]} == {
        a["id"] for a in crosswalk["proposed_additions"]
    }


def test_every_task_in_the_example_resolves_in_the_taxonomy(taxonomy, example):
    known = {c["suggested_id"] for c in taxonomy["categories"]} | {
        a["suggested_id"] for a in taxonomy["proposed_additions"]
    }
    used = {row["task"] for row in example["disclosures"]}
    assert used <= known, used - known


def test_all_kit_json_files_parse():
    files = sorted((ROOT / "docs" / "vancouver").rglob("*.json"))
    assert files
    for path in files:
        json.loads(path.read_text(encoding="utf-8"))


def test_renderer_output_matches_the_committed_statement(tmp_path):
    out = tmp_path / "statement.md"
    result = subprocess.run(
        [
            sys.executable,
            str(RENDERER),
            str(EXAMPLES / "example-disclosure.json"),
            str(TEMPLATE),
            "--out",
            str(out),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    generated = out.read_bytes()
    committed = STATEMENT_PATH.read_bytes()
    assert generated == committed, (
        "docs/vancouver/kit/examples/example-statement.md is stale. Regenerate it:\n"
        "  python tools/render_vs_statement.py docs/vancouver/kit/examples/example-disclosure.json "
        "--out docs/vancouver/kit/examples/example-statement.md"
    )


def test_rendered_statement_leaves_no_placeholder_unfilled():
    text = STATEMENT_PATH.read_text(encoding="utf-8")
    assert "{{" not in text
    assert "not a quality, accuracy or truth certification" in text
