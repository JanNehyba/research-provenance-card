# Research Provenance Card (RPC) Specification v0.1

## Scope
RPC records provenance assertions for one concrete research output version.

## Core Rules
1. `paper.pdf_sha256` is mandatory.
2. Every check and attestation includes `subject_sha256`.
3. RPC does not compute truth scores or global quality verdicts.
4. Claims are represented via role assignments and evidence levels.

## Evidence Levels
- `declared`
- `artifact_linked`
- `independently_attested`
- `reproduced`

## Status Panel Fields
- `rpc_available`
- `version_bound`
- `artifacts_linked`
- `references_resolved`
- `support_audit_available`
- `independently_attested`

## Notes
- These statuses are derived from card content.
- A status must never imply that scientific claims are true.
