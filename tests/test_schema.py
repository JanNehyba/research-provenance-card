import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "rpc-v0.1.schema.json"
EXAMPLES_DIR = ROOT / "schema" / "examples"
BROKEN_DIR = EXAMPLES_DIR / "broken"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def validator():
    schema = load_json(SCHEMA_PATH)
    return Draft202012Validator(schema)


def test_minimal_example_is_valid(validator):
    payload = load_json(EXAMPLES_DIR / "minimal.json")
    errors = list(validator.iter_errors(payload))
    assert errors == []


def test_full_example_is_valid(validator):
    payload = load_json(EXAMPLES_DIR / "full.json")
    errors = list(validator.iter_errors(payload))
    assert errors == []


@pytest.mark.parametrize("filename", [
    "missing_pdf_sha.json",
    "invalid_enum.json",
    "restricted_without_reason.json",
])
def test_broken_examples_fail(filename, validator):
    payload = load_json(BROKEN_DIR / filename)
    errors = list(validator.iter_errors(payload))
    assert errors, f"Expected validation errors for {filename}"
