# Review Handoff Summary

Date: 2026-07-20  
Repository: JanNehyba/research-provenance-card  
Branch: main

## Purpose

This document summarizes what was implemented so another LLM (or reviewer) can quickly audit the project state, verify assumptions, and suggest next improvements.

## Scope Completed

1. Repository scaffold for RPC v0.1 was created and published.
2. Core schema, examples, validation tooling, reference check utility, disclosure generator, tests, and CI were added.
3. First production card was created in the registry and validated.
4. GitHub Pages deployment via Actions was enabled and configured.
5. English manuscript was created as canonical and bound to a generated PDF hash.
6. Czech manuscript was updated with bilingual metadata marking English as canonical.
7. Submission-ready English disclosures for Elsevier and Springer templates were generated.

## Commit Timeline

- f38f8cc: initial RPC v0.1 repository scaffold
- c18078e: first production card + Pages workflow
- 0019521: canonical English manuscript + PDF + card binding update
- e07c24e: bilingual metadata in Czech file + generated disclosure outputs

## Key Files Added or Updated

### Project and Spec

- README.md
- spec/rpc-spec-v0.1.md
- spec/roles.md
- schema/rpc-v0.1.schema.json
- schema/examples/minimal.json
- schema/examples/full.json

### Tooling

- tools/validate.py
- tools/refcheck.py
- tools/generate_disclosure.py
- tools/templates/elsevier.txt
- tools/templates/springer.txt

### CI and Deployment

- .github/workflows/validate.yml
- .github/workflows/pages.yml
- site/build.py
- site/style.css

### Registry and Manuscripts

- registry/2026/rpc-2026-0001.json
- docs/rpc_preprint_en.md
- docs/rpc_preprint_en.html
- docs/rpc_preprint_en.pdf
- docs/rpc_preprint_cs.md
- docs/disclosure_elsevier_en.txt
- docs/disclosure_springer_en.txt

## Current Canonical Manuscript Policy

- Canonical manuscript: English version in docs/rpc_preprint_en.md
- Canonical bound artifact: docs/rpc_preprint_en.pdf
- Czech manuscript remains available as translation/reference source.

## First Production Card Status

File: registry/2026/rpc-2026-0001.json

Current card state:

1. Bound to English manuscript PDF SHA-256.
2. Uses evidence levels without global truth scoring.
3. Includes activity roles and artifact access policy.
4. Uses ORCID identifier discovered from public ORCID expanded search.

## Validation and Test Status

At last execution:

1. Pytest: passed (5/5).
2. Registry validation: passed for registry/2026/rpc-2026-0001.json.
3. Site build: successful with 1 card rendered.
4. GitHub Actions:
   - Validate RPC: successful
   - Deploy Pages: successful

## Known Constraints and Notes

1. English PDF was generated from local HTML using headless Chrome.
2. ORCID value was not provided manually; it was discovered from public ORCID API search for Jan Nehyba and Masaryk University affiliation.
3. The project intentionally avoids aggregate quality or truth labels.

## Suggested Review Focus for Another LLM

1. Check schema rigor and backward compatibility strategy for future versions.
2. Review whether evidence-level semantics are strict enough for cross-journal use.
3. Review reference-check boundary clarity (existence/metadata vs claim support).
4. Review pages renderer status derivation logic for edge cases.
5. Propose hardening steps for first external pilot usage.

## Optional Next Actions

1. Add a short canonical-language note to README.
2. Add explicit release checklist for v0.1.0 tagging.
3. Add small integration test for disclosure generation outputs.