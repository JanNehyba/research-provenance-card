# Implementation report — filling in the Round 2 taxonomy on a real manuscript

Supporting material for the [Round 2 submission](../round2-submission-en.md).
Written 31 July 2026 · Jan Nehyba (ORCID 0000-0003-4159-5576), Faculty of Education, Masaryk University.

This is the item the core team cannot produce for itself: a report from someone who took the
proposed 18-category taxonomy and tried to fill it in for an actual manuscript, with a validator
attached, and wrote down what did not work. It is one implementation and one manuscript. It is not
pilot evidence at scale, and nothing here has any official standing.

---

## 1. What was done

The manuscript is the project's own preprint (*From Declaration to Evidence*, English canonical
version, SHA-256 `f4aa8c33…66d6`). It already had a structured provenance record in this project's
own format. The exercise was to re-express the same facts in the round-2 vocabulary, validate the
result, and generate an article-ready statement from it:

| Artefact | File |
|---|---|
| The 18 categories as a data file, with stable slugs and deprecation metadata | [`vs-taxonomy-round2.json`](./vs-taxonomy-round2.json) |
| A minimal record schema built from the round-2 concepts plus a verification axis | [`vs-disclosure-draft.schema.json`](./vs-disclosure-draft.schema.json) |
| The filled-in record for the manuscript | [`examples/example-disclosure.json`](./examples/example-disclosure.json) |
| The statement generated from it (table + Methods paragraph) | [`examples/example-statement.md`](./examples/example-statement.md) |
| Category-by-category mapping, including our own gaps | [`../taxonomy-crosswalk-v0.1.json`](../taxonomy-crosswalk-v0.1.json) |

No new validator was written: the project's existing `tools/validate.py` takes a `--schema`
argument, so the kit is checked by a validator that knows nothing about this vocabulary. That is
the point — a disclosure format is only machine-readable in a useful sense if a generic tool can
check it.

The whole exercise took a working afternoon, most of it spent not on the categories but on the two
problems in §3.

## 2. What the taxonomy showed

**The granularity is right, and in two places better than ours.** Splitting quantitative from
qualitative analysis (12/13) and data visualisation from figure or image generation (14/15) are
both correct calls that our own vocabulary got wrong by collapsing them into coarser CRediT roles.
We will adopt both splits.

**Five gaps on our side.** Categories 4 (literature summarisation), 9 (data creation), 13, 15 and
17 (translation) have no counterpart in our role vocabulary. All five are queued for v0.2. The
taxonomy improved our implementation before the standard exists, which is an argument for
publishing a machine-readable draft vocabulary early rather than at the end.

**Three categories are missing, and one of them mattered immediately.** Orchestration / agent
operation (A), verification performed by AI (B), selection among runs or outputs (C) — argued in
§3B of the submission. When filling in the record we hit (A) at once: the heaviest AI involvement
in this manuscript was sustained adversarial critique of the author's framing, which changed the
design and left **no sentence in the output**. Under the 18 categories there is no honest place to
put it; we filed it under `vs:idea-generation` and had to explain in free text what the row
actually was. A taxonomy of *tasks the AI performed on the output* cannot express *the AI shaping
the author's judgement*, and that is the case where disclosure is most needed and least visible.

**Three ambiguities to resolve:** 8 vs 9 (collection vs creation), 4 vs 16 (an AI-written
literature review is both), and 18 bundling reference handling with prose editing. Only the first
needs a decision; the other two need a stated rule that one use may carry several categories.

## 3. What broke

**(1) Retrospective provenance costs one to two orders of magnitude more than capture at source,
and stays incomplete.** Every fact that would have cost a second to record while working — which
model version, which interface, what was asked, what came back — cost tens of minutes to
reconstruct afterwards, and several could not be reconstructed at all. The record now says so:
one row carries `access_status: not_retained` with the reason "no prompt archive was exported at
the time of use". That row is honest and nearly worthless as evidence, which is exactly the
outcome a standard relying on voluntary retrospective completion should expect. The
recommendation that follows (P8) is not "encourage machine-generatability" but "publish a
reference serialisation and ask tool providers for an export": the heavier the AI involvement, the
more automatable the record, so the asymmetry favours the standard.

**(2) Raw logs are not a publishable artefact — and curated logs are evidence only if the curation
rule is public.** Our first registry card asserted `artifact_linked` evidence pointing at a
working-session log containing third-party unpublished material, personal notes and personal data.
It cannot be released as-is, no hash of it was ever computed, and no curated version exists. So the
claim was a formality: it looked evidenced and was not. There were two honest options — publish a
curated version *with its selection rule*, or drop the claims. We dropped them (§4). The general
fix is the two-hash rule in Appendix B of the submission: hash the complete raw export and archive
it even when it stays closed, publish the curated version with its own hash, and state the curation
criterion and the kinds of material removed. The draft schema in this kit implements it as an
optional `curation` object. Without something like it, "log retained" will be the cheapest way to
look evidenced without being evidenced.

**(3) A field that is optional is a field that is empty.** The one field we made required on every
row is *what could not be checked*. In our own record it is the most informative column by a wide
margin — it is where the reference-resolution gap, the missing prompt archive and the absent second
reader all became visible. If it is optional, it will be the first thing dropped, and the record
degrades into a list of things that went well.

## 4. What we changed about ourselves as a result

Applying a graded record forced us to lower our own claims. Three activities in
`registry/2026/rpc-2026-0001.json` moved from `artifact_linked` to `declared`, the unbacked
artifact record was removed, and a description was added to every activity so that the correction
lost no information (commit *fix(registry): drop unbacked artifact claim from first card*;
`CHANGELOG.md` 0.1.1). The rendered provenance panel now shows `artifacts_linked` **OFF** — the
project's own public page is weaker than it was last week, and correctly so.

Two things are worth saying about that. First, the failure was found only by *using* the format on
ourselves; reading the specification would never have surfaced it. Second, a disclosure format
whose honest use costs the author something is doing its job — which is also the strongest reason
to keep the verification list closed and short. Anything that can be satisfied by writing more
prose will be.

The manuscript's own bibliography has still not been run through reference resolution, and no
independent attestation exists for anything in the record. Both are stated in the record rather
than left to be inferred.

## 5. What follows for the standard

Short form of the nine proposals in the submission, in the order they matter for making
"machine-readable" real:

1. **Stable slug identifiers plus a versioned vocabulary file** with `deprecated` / `replaced_by`
   (P1). Ordinals break on the first insertion. Every disclosure must carry the vocabulary version.
2. **Rows, not sentences** (P2): task × actor × what was checked × trace, with free text alongside.
3. **A closed verification list** (P3), and a **required "what could not be checked" field**.
4. **Bind disclosures and verification claims to a content hash** (P4) — the cheapest mechanism
   available and the one that stops a check outliving what it checked.
5. **Keep "reference resolves" and "reference supports the claim" apart** (P5). A combined
   "citations verified" label would be the most damaging artefact this standard could produce.
6. **Require the curation rule for edited evidence** (P6, two-hash record).
7. **Add the three missing categories** (P7), (C) especially: undisclosed selection among runs is
   invisible to every scheme we have seen.
8. **Make machine-generatability a design requirement, not a wish** (P8): reference serialisation,
   worked examples, and a channel to tool providers for a disclosure export.
9. **Scope null declarations to a threshold version, a taxonomy version and a file** (P9).

And one thing to leave out: no aggregate score. A structured record invites "provenance quality:
8/10". The moment that exists it will be optimised rather than satisfied. Record who did what and
what was evidenced; stop there.

---

*Everything in this report is reproducible from the repository:
`python tools/validate.py "docs/vancouver/kit/examples/example-disclosure.json" --schema docs/vancouver/kit/vs-disclosure-draft.schema.json`
and `pytest`. Corrections welcome as issues or pull requests.*
