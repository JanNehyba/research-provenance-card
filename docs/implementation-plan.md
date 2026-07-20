# RPC Implementation Plan (Updated)

## Objective
Deliver RPC v0.1 as a usable open repository with schema, tools, registry structure, and first production card workflow.

## Phase 1: Foundation (Done)
- Repository structure and licenses.
- Human-readable spec and roles vocabulary.
- Dependency baseline and contribution docs.

## Phase 2: Data Model and Validation (In Progress)
- Finalize JSON Schema v0.1.
- Add valid and intentionally broken examples.
- Add tests for pass/fail behavior.

## Phase 3: Tooling
- `validate.py` for schema validation with non-zero exit codes.
- `refcheck.py` for DOI/reference resolution checks (Crossref/OpenAlex).
- `generate_disclosure.py` for publisher templates.

## Phase 4: Registry and Site
- Static site build for panel rendering.
- Card detail pages from `registry/**/*.json`.
- CI validation on pull requests.

## Phase 5: First Production Card
- Compute SHA-256 of the target PDF.
- Collect guarantor and AI activity details.
- Create `registry/2026/rpc-2026-0001.json`.

## Phase 6: Publication Readiness
- Release notes and tag `v0.1.0`.
- GitHub Pages activation.
- Zenodo linkage for DOI archival releases.
