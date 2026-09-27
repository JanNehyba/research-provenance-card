# Gap analysis: what the literature models, and what the project claimed

Written 2026-09-27 from `data/lit/dimensions.json`, `data/lit/eight-components-map.json`
and `data/lit/schemes.jsonl`. Every figure here is countable from those files.

This document exists to answer RQ5 of the protocol, which was set up as a
falsification test of a claim the parent project makes. The protocol says: if the
three components the project calls unmodelled turn out to be modelled, the
finding is recorded and the project's claim is rewritten, not defended. One of
the three is modelled. That claim is withdrawn below.

---

## 1. What the review found

429 category schemes, drawn from 400 papers, carrying 1703 verified dimension
rows. (Extraction produced 475 identifiers; an agent working one packet at a time
cannot know another packet held the same artefact, so CRediT arrived under 13
names. 429 is the merged count and the one to quote.) Every row quotes its source and every quote was checked by script against
the retrieved text. The 1502 distinct verbatim labels merge into **193 canonical
dimensions**, built bottom up by eleven agents that could not see each other's
work and then consolidated once.

The strongest evidence that the vocabulary is not an artefact of one prompt:
seven of the nine main open-coding batches, working on disjoint slices, gave the
same axis the same name, **extent of AI involvement**. It is also the largest
dimension, with 81 verbatim labels behind it.

**Two of the 193 dimensions are measurement artefacts, not axes**, and any count
used in an argument should exclude them. `scheme-own-category-inventory` (31
labels) collects labels that name a scheme's own top-level list rather than a
property of a disclosure. `generic-study-methodology-reporting` (31 labels)
collects ordinary reporting-guideline sections (Title, Abstract, Methods) that
arrived because several AI reporting guidelines are extensions of general ones.
Both exist because extraction worked paper by paper and could not know this.

---

## 2. The eight components against the literature

| Component | Labels | Dimensions | Verdict |
|---|---:|---:|---|
| 2. Share of AI | 83 | 2 | widely modelled |
| 3. What the human did | 74 | 4 | widely modelled |
| 4. Accountability | 56 | 2 | **widely modelled, claim withdrawn** |
| 1. Role of AI | 55 | 3 | widely modelled |
| 8. Placement | 52 | 3 | widely modelled |
| 5. Certainty | 15 | 4 | thinly modelled, and displaced onto the machine |
| 7. Recipient expectation | 6 | 4 | modelled only in system design |
| 6. State of the output | 2 | 1 | **not modelled** |

Five of the eight are well attested. The three the project singled out are not
one finding but three different ones.

### 4. Accountability: the claim was wrong

`accountability-for-the-work` carries 23 verbatim labels and asks the project's
own question: who answers for the finished work, who gives final approval, who
stays responsible for AI-touched content. Add `authorship-criteria` (33 labels)
and the component is among the best attested in the review. **The project's
statement that accountability is unmodelled has to go.**

What survives is narrower and more interesting. Read the 23 labels and they are
all about **who**: author accountability, clinician accountability, final
approval, responsibility allocation statement, a liability-responsibility chain,
the principle of allocation. Not one of them is a **graded claim by the person
signing**. Nothing in the literature records the difference between "I take full
responsibility" and "I stand behind the facts; the wording is the model's".
Accountability is modelled as identity and as the allocation of liability between
parties, never as a partial or scoped assertion the signer makes about their own
text. That is a real gap and it is stateable in one sentence, which the original
claim was not.

### 6. State of the output: genuinely absent

Nothing among 193 dimensions records whether the thing being handed over is a
draft, a working version or a finished piece.
`maturity-level-of-the-thing-described` is the nearest match and its two labels
are "maturity level ml" and "maturity tier", describing how far a proposed
framework has got, not what state a text is in.
`integration-depth-of-ai-content` records how much editing the AI output
received, which is the machine's share again, not a declaration about the
deliverable.

This is the one component of the eight that the literature does not have at all,
and the absence is not for want of looking: 429 schemes, among them a dozen named
reporting guidelines with dozens of items each.

### 7. Recipient expectation: exists, but never as a disclosure field

Four dimensions touch it, with six labels between them: whether the reader
understands the AI's part, what the system surfaces to a user, whether an output
can be contested, whether alternatives are offered. Every one comes from
system-design or HCI work, and every one is a property of **an interface**, not a
field in which an author states what the reader is being asked to do with the
text.

So the honest form of this claim is not "nobody models it" but "it is modelled as
something a system does, never as something a writer says". As a disclosure field
it is absent.

### 5. Certainty: present, but pointed the wrong way

Fifteen labels across four dimensions, and three of the four are about the
machine rather than the person: the confidence the system displays, calibration
statistics, warnings an interface shows. Only
`limitations-and-validity-boundaries-disclosed` (8 labels) is the author saying
what their own account does not cover. The axis exists; the version where a human
states how sure they are about the text they are signing barely does.

---

## 3. What this changes for the project

1. **Withdraw the accountability claim** wherever it appears, including in
   `docs/zadani.md` and in anything derived from it. Replace it with the narrower
   finding: accountability is modelled as identity and allocation, not as a
   graded claim by the signer.
2. **Keep two of the three, in sharper form.** State of the output is absent.
   Recipient expectation exists only as a system property. Both are what follows
   from treating a disclosure as an utterance addressed to someone, which is the
   project's Goffman framing, so the framing now has evidence under it instead of
   an assertion.
3. **The code book should be built from the crosswalk, not from the eight
   components.** Five of the eight map onto dimensions with 50 to 83 labels
   behind them; a code book that ignores that is discarding the field's own
   vocabulary. The three thin ones stay in as the project's own additions, marked
   as such, and the code book records which components came from the literature
   and which did not.
4. **The inventory is itself a contribution.** Nobody had assembled these schemes
   and compared their dimensions across domains. That is now a file, with a
   quote behind every row.

---

## 4. What this analysis cannot say

- **It cannot say a dimension is absent from the literature, only from this
  corpus.** Grey literature was not searched systematically, so publisher author
  instructions, citation style manuals and university policies are represented
  only where a searched paper pointed at them.
- **It cannot rank dimensions by importance.** A label count measures how many
  schemes named an axis, which is attestation, not significance. A dimension with
  two labels may matter more than one with eighty.
- **The mapping of the eight components onto the vocabulary is an
  interpretation**, made by reading 193 glosses. It was deliberately not
  delegated, because an agent asked to find the project's own scheme in the data
  has every reason to find it. A reader who disagrees with a particular mapping
  can check it: `eight-components-map.json` names every dimension it counted.
- **Two records were dropped for language** after extraction, a Dutch C2PA report
  and a Portuguese conflict-of-interest form, which the protocol's English and
  Czech rule excludes and the screeners let through. Eight rows are affected.
