# AI use statement

**Work:** "From Declaration to Evidence: Research Provenance Card as Version-Bound Infrastructure for AI-Involved Research" (preprint-v2-en)
**Version binding (SHA-256):** f4aa8c33486bb48789b0011f44f82ee08b7a36d68797e909af7da93e773066d6
**Guarantor:** Jan Nehyba (ORCID: 0000-0003-4159-5576), asserted 2026-07-31T15:28:04Z
**Task vocabulary:** Proposed research-task taxonomy, Consultation Round 2, Global Reporting Standard for AI Disclosure in Research (round2-proposal, rendering 0.1)

## Structured statement

| Task | Actor | What was checked | Trace | What could not be checked |
|---|---|---|---|---|
| Idea generation <br>`vs:idea-generation` | Anthropic Claude 2026-07, chat | read through by the author | log: restricted; no hash | Whether the resulting design changes are improvements cannot be verified from the record; only that every change was adjudicated by the author. This is the case the submission argues is least visible to output-centred disclosure rules. |
| Literature search <br>`vs:literature-search` | Anthropic Claude 2026-07, chat | read through by the author | log: restricted; no hash | The manuscript's own bibliography has not yet been run through automated reference resolution, so non-resolving citations would not have been detected; no third party re-ran the searches, so nothing is known about what the retrieval missed. |
| Literature summarization <br>`vs:literature-summarization` | Anthropic Claude 2026-07, chat | read through by the author | log: restricted; no hash | Individual statements in the landscape section were not traced back to page-level locations in the cited sources. This row and the drafting row below overlap, which is the category-overlap problem reported in the submission. |
| Drafting manuscript or abstract text <br>`vs:drafting-text` | Anthropic Claude 2026-07, chat | read through by the author | log: restricted; no hash | The author read and rewrote the full text, but no independent reader checked it before this record was written, and no record exists of which passages were rewritten and which were accepted as drafted. |
| Translation <br>`vs:translation` | Anthropic Claude 2026-07, chat | read through by the author | log: restricted; no hash | Neither language version was independently back-translated or checked by a second reader. Under the equity argument in the submission this use is a technical one and would sit below the threshold; it is disclosed here because the row costs nothing. |
| Orchestration / agent operation <br>`vs:orchestration` | human (0000-0003-4159-5576) | not checked | prompt: not retained; no hash | The prompts and the protocol that directed the model are not published, so a reader cannot tell what the model was asked to do. Writing the protocol down after the fact would produce a description, not a record - which is the retrospective-provenance finding reported in the submission. |

## Narrative for the Methods section

AI (Anthropic Claude 2026-07, chat) was used for: idea generation, literature search, literature summarization, drafting manuscript or abstract text, translation. Orchestration / agent operation: human (0000-0003-4159-5576). Verification: idea generation, literature search, literature summarization, drafting manuscript or abstract text, translation - read through by the author; orchestration / agent operation - not checked. Records of 5 of these uses exist but are not public; the reason is stated for each in the structured statement. For 1 of these uses no durable record was retained. Limits of verification are stated per use in the structured statement rather than summarised here, because a summary is where they stop being checkable.

## Null declaration

Apart from the uses disclosed above, the author did not use AI meeting the disclosure threshold proposed in Consultation Round 2 in the preparation of this work.

Threshold: Consultation Round 2 proposed threshold, preparatory reading v4.5 (8 July 2026). Task vocabulary: round2-proposal, rendering 0.1. Asserted about the file with SHA-256 f4aa8c33486bb48789b0011f44f82ee08b7a36d68797e909af7da93e773066d6.

## Responsibility

The author is responsible for the content of this work, including all AI-assisted parts, and for the accuracy of this disclosure record. Accepted by: Jan Nehyba (ORCID: 0000-0003-4159-5576).

---

This record documents process and evidence. It is not a quality, accuracy or truth certification of the work.

Both sections above are generated from `docs/vancouver/kit/examples/example-disclosure.json` by `tools/render_vs_statement.py`. The record is the source of truth; these are two renderings of it, not two descriptions of it.
