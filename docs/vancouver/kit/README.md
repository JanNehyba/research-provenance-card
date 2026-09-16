# Implementation kit — Vancouver Standard, Consultation Round 2

A small, runnable kit produced while answering [Consultation Round 2](../README.md) of the
**Global Reporting Standard for AI Disclosure in Research**. It exists so that the round-2 proposal
can be tried against running code before it is finalised.

> **Unofficial.** Nothing here is published, endorsed or reviewed by the core team of the standard.
> The taxonomy in this folder is a *rendering of a proposal under public consultation*, not the
> standard. This project is an **implementation profile**, not a competing standard: if the core
> team adopts a different vocabulary, this kit maps to it rather than argues with it.

## Three commands

From the repository root, with `pip install -r requirements.txt` done:

```bash
# 1. A generic validator, which knows nothing about this vocabulary, checks the record.
python tools/validate.py "docs/vancouver/kit/examples/example-disclosure.json" \
  --schema docs/vancouver/kit/vs-disclosure-draft.schema.json

# 2. The same validator rejects an incomplete record (exit code 1).
python tools/validate.py "docs/vancouver/kit/examples/example-disclosure-broken.json" \
  --schema docs/vancouver/kit/vs-disclosure-draft.schema.json

# 3. One record renders into both an article statement and a Methods paragraph.
python tools/render_vs_statement.py docs/vancouver/kit/examples/example-disclosure.json
```

Command 2 fails with `'verification' is a required property` and `'not_verified' is a required
property` — the two fields a narrative disclosure lets an author omit silently. Command 3 prints
what is committed as [`examples/example-statement.md`](./examples/example-statement.md); `pytest`
checks that the committed file is byte-identical to the generated one.

**No new validator was written for this kit.** `tools/validate.py` already takes `--schema`. That
is deliberate: a disclosure format is machine-readable in a useful sense only if a generic tool can
check it without knowing the vocabulary.

## What is in the folder

| File | What it is |
|---|---|
| [`vs-taxonomy-round2.json`](./vs-taxonomy-round2.json) | The proposed 18 categories as data: stable slug identifiers, the `Design >` parent made explicit, deprecation metadata, three proposed additional categories, and implementer notes clearly separated from quoted labels. Definitions are `null` on purpose — the source document says definitions are still to be drafted, and inventing them would put words into the proposal. |
| [`vs-disclosure-draft.schema.json`](./vs-disclosure-draft.schema.json) | JSON Schema (Draft 2020-12) for a minimal disclosure record: work, guarantor, one row per disclosed use, null declaration, responsibility statement. Every property carries `x-origin: round2-proposal` or `x-origin: implementer-proposal`, so it is visible at a glance which concepts are the initiative's and which are ours. Deliberately smaller than [the RPC schema](../../../schema/rpc-v0.1.schema.json). |
| [`examples/example-disclosure.json`](./examples/example-disclosure.json) | A real record for this project's own manuscript, re-expressed in the round-2 categories. Honest values: mostly `read_through`, no third-party checks, working logs restricted, one prompt archive `not_retained`. |
| [`examples/example-disclosure-broken.json`](./examples/example-disclosure-broken.json) | Intentionally invalid, for command 2 and for the test suite. |
| [`examples/example-statement.md`](./examples/example-statement.md) | Generated output, committed so it can be read without running anything. |
| [`implementation-report.md`](./implementation-report.md) | Two pages on what happened when the taxonomy was filled in for a real manuscript: what was missing, what broke, and what we had to change about our own record as a result. |

Rendering is driven by [`tools/render_vs_statement.py`](../../../tools/render_vs_statement.py) and
[`tools/templates/vs_statement.txt`](../../../tools/templates/vs_statement.txt), which reuse
`render_template()` from the existing publisher-disclosure generator.

## The one design addition

The round-2 proposal describes verification in prose. This kit makes it a **closed field on every
row** (`not_checked`, `read_through`, `sampled`, `recomputed`, `cross_checked_primary_sources`,
`checked_by_named_third_party`, `independently_reproduced`) and pairs it with a **required**
free-text field for *what could not be checked*. In our own record, that required field is the most
informative column; if it were optional it would be empty. The list is ordered from weakest to
strongest but is **not a score**, and no combination of fields in the record is a quality or truth
judgement about the research.

## Rights

Category labels are quoted from the consultation document; rights in that wording rest with the
initiative (ISC, WCRIF, COPE, STM, GYA) and the quotation will be removed or relicensed on request.
The file structure, identifiers, notes, schema and tooling are this project's work: documents
CC BY 4.0, code MIT. If the core team wants a machine-readable vocabulary file, this one is offered
for adoption, amendment or replacement without conditions.

## See also

- [Round 2 submission](../round2-submission-en.md) — the answers this kit supports, with proposals P1–P9.
- [Taxonomy crosswalk](../taxonomy-crosswalk-v0.1.json) — the 18 categories against this project's role vocabulary, with gaps flagged in both directions.
- [`docs/vancouver/README.md`](../README.md) — verified process facts, sources and the pre-submission checklist.
