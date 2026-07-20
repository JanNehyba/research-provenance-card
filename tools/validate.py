#!/usr/bin/env python3
import argparse
import glob
import json
import os
import sys

from jsonschema import Draft202012Validator


def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(path: str, validator: Draft202012Validator) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    errors = []
    for err in sorted(validator.iter_errors(payload), key=lambda e: e.path):
        loc = ".".join(str(p) for p in err.absolute_path) or "$"
        errors.append(f"{path}: {loc}: {err.message}")
    return errors


def expand_globs(patterns: list[str]) -> list[str]:
    matched: list[str] = []
    for pattern in patterns:
        results = glob.glob(pattern, recursive=True)
        if not results and os.path.isfile(pattern):
            results = [pattern]
        matched.extend(results)
    return sorted(set(matched))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate RPC JSON cards.")
    parser.add_argument("inputs", nargs="+", help="File paths or glob patterns")
    parser.add_argument(
        "--schema",
        default="schema/rpc-v0.1.schema.json",
        help="Path to JSON Schema file",
    )
    args = parser.parse_args()

    files = expand_globs(args.inputs)
    if not files:
        print("No input files matched.")
        return 2

    schema = load_schema(args.schema)
    validator = Draft202012Validator(schema)

    all_errors: list[str] = []
    for path in files:
        try:
            errs = validate_file(path, validator)
            if not errs:
                print(f"OK: {path}")
            all_errors.extend(errs)
        except Exception as exc:
            all_errors.append(f"{path}: failed to parse/validate: {exc}")

    if all_errors:
        for msg in all_errors:
            print(f"ERROR: {msg}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
