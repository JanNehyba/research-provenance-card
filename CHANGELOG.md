# Changelog

## 0.1.1 - 2026-07-31
- Corrected the first registry card (`registry/2026/rpc-2026-0001.json`): three AI activities that
  asserted `artifact_linked` pointed at a working-session log with no hash and no releasable version.
  The artifact record was removed and the three activities were lowered to `declared`, with a
  `description` added to every activity so the correction does not lose information.
  `paper.pdf_sha256` is unchanged (the manuscript did not change); `human_guarantor.assertion_timestamp`
  was updated, because a re-stated assertion is a new assertion. Effect on the rendered panel:
  `artifacts_linked` is now OFF, `version_bound` stays ON.
- Added the Vancouver Standard consultation round 2 materials and implementation kit under
  `docs/vancouver/`: submission, taxonomy crosswalk, taxonomy as data, a draft disclosure schema
  validated by the existing validator, worked examples, a statement renderer, and an implementation report.

## 0.1.0 - 2026-07-20
- Initial repository scaffold for Research Provenance Card (RPC).
- Added specification draft, roles vocabulary, and JSON Schema v0.1.
- Added CLI tools: validation, reference check report, disclosure generator.
- Added CI workflow and static site builder.
- Added implementation plan document.
