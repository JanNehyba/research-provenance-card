# Consultation Round 2 — Submission

**Towards a Global Reporting Standard for AI Disclosure in Research ("Vancouver Standard")**
Focus Track of WCRI 2026 · ISC · WCRIF · COPE · STM · GYA
Submission deadline: **16 October 2026** · Webform: <https://council.science/AIdisclosure>

---

## Respondent

| Field | Value |
|---|---|
| Name | Jan Nehyba |
| Role | Assistant Professor, Faculty of Education, Masaryk University, Brno, Czechia |
| ORCID | 0000-0003-4159-5576 |
| Capacity | Personal perspectives of a natural person |
| Discipline | Educational research / social sciences (qualitative methods) |
| Country | Czechia |
| Contact | *[institutional e-mail — fill in before submitting]* |

**Basis of this response.** The answers below are not a position paper. They report what happened when we built a working implementation of a structured AI-disclosure record and then applied it to our own manuscript. The implementation — the **Research Provenance Card (RPC) v0.1** — is public: JSON Schema, validator, reference-resolution checker, disclosure generator, registry, and rendered provenance panels (specification CC BY 4.0, code MIT): <https://github.com/JanNehyba/research-provenance-card>

RPC is deliberately positioned as an **implementation profile of this standard**, not a competitor to it. Where the eventual standard says *what* must be disclosed, RPC is one candidate answer to *how a machine-readable record of it can look and be validated*. Everything below is offered in that spirit: if the core team adopts a different taxonomy or vocabulary, we expect to map to it rather than argue with it.

**Suggested tick-box answers** for the non-open questions are marked ▶ so the whole submission can be transferred to the webform in one pass.

---

## 0 — Summary: nine concrete proposals

| # | Proposal | Question |
|---|---|---|
| **P1** | Give every taxonomy category a **stable, machine-readable identifier** (slug, not ordinal) and version the taxonomy itself, with a deprecation/replacement policy — the precedent is CRediT as ANSI/NISO Z39.104-2022. Without stable IDs, "machine-readable" cannot be delivered downstream. | 3 |
| **P2** | Make the unit of disclosure a **row, not a sentence**: one row per (task × actor × what-was-checked × trace). Narrative prose can accompany a row; it cannot replace it if disclosures are to be comparable. | 3 |
| **P3** | Add an **evidence/verification level** to every row, from a closed list. Round 1's criteria and the Focus Track's own "verification ladder" (attestation → review → audit → replication) already point here; a closed list is what makes it machine-readable. | 5 |
| **P4** | **Bind the disclosure to the version it describes** via a content hash (SHA-256) of the accepted file. Disclosures and verification claims currently attach to a title, not to a state of a file, so they survive silent replacement of content. | 4, 5 |
| **P5** | Keep **"reference exists" and "reference supports the claim" as two separate fields**. Automated tools resolve existence and metadata reliably; they do not reliably assess claim support. A single "citations verified" label conflating the two would be the most damaging artefact this standard could produce. | 5 |
| **P6** | For retained records, require **access conditions plus a hash — and, where a log is curated before publication, both hashes and the curation rule** (see Appendix B). A curated log is weaker evidence the more it was curated; publishing the selection rule is what keeps it evidence at all. | 5 |
| **P7** | Add **three missing categories**: (A) orchestration / agent operation, (B) verification performed by AI, (C) selection among multiple runs or outputs. (C) is the integrity-critical one: undisclosed cherry-picking across runs is currently invisible to every disclosure scheme we know of. | 3 |
| **P8** | Require the standard to be **machine-generatable in practice, not only in principle**: publish a reference serialisation and ask tool providers for an export. Retrospective reconstruction of provenance costs one to two orders of magnitude more effort than capture at the moment of use, and it stays incomplete. This is our main empirical finding (§6). | 1, 3, 6 |
| **P9** | Scope **null declarations** to a threshold version, a taxonomy version and the accepted manuscript version — otherwise a mandatory negative disclosure becomes exactly the unfalsifiable sentence the standard is replacing. | 4 |

---

## 1 — Which AI use should be disclosed? (Thresholds)

### 1A. Views on the proposed disclosure threshold

**We support the proposed qualitative threshold as written, including the explicit rejection of quantitative thresholds.** The footnote's reasoning is correct and worth stating even more firmly in the final standard: there is no unit, no instrument and no audit procedure for "percentage of AI contribution". Percentages invite two failure modes — authors guessing, and third-party detectors producing numbers ("this manuscript is 40% AI") that can be neither confirmed nor refuted. A role-based, task-based claim is a different kind of statement: it can be confronted with code, logs, outputs and named checkers.

We also support criterion (1) — that delegated or AI-shaped judgement is disclosure-worthy **even if a human later validated the result**. This is the single most important sentence in the draft, because it blocks the most common evasion ("I checked it, so it's mine").

Three refinements:

**(a) Do not let the threshold carry the whole burden.** A binary threshold with a uniform reporting cost above it creates a cliff: the author who crosses it pays full price, the author just below pays nothing, and the incentive at the margin is to argue oneself below. Pair the threshold with a **graded record** (P3), so a marginal use can be honestly reported in one cheap row at the lowest evidence level, and a heavy, well-documented use can be reported as such. What should be proportionate is not *whether* one discloses but *how much evidence the record carries*.

**(b) "Substantive" needs discipline-level exemplars, not a better definition.** The reviewer/reader test is the right formulation, and further abstract refinement will not help. What will help is a small, growing, citable set of worked examples per domain (a dozen per discipline, maintained as part of the living standard) — the way reporting-guideline networks accumulate exemplars. We would contribute educational-research examples.

**(c) Equity: language work must not be taxed by first language.** Category 17 (Translation) and the language part of category 18 create a structural asymmetry. A Czech, Ukrainian or Indonesian researcher who thinks and drafts in their own language and uses AI to produce English prose is doing the *same intellectual work* as an anglophone colleague, but under a literal reading of the threshold they must disclose more. Round 1 concluded the standard must not be harder to follow for less-resourced communities; this is where that principle bites. Our proposed wording: **translation of the author's own content, with meaning preserved and verified by the author, is a technical use below the threshold and is disclosed only where the journal requires it; AI-generated *content* in any language is above the threshold regardless of which language it was generated in.** The line is authorship of the content, not the language of production.

### 1B. Three examples from our field (educational research, qualitative methods)

1. **Requires disclosure.** An LLM performs first-pass thematic coding of interview transcripts; the researcher reviews, adjudicates and revises the codes. Judgement that would normally be expert-human was delegated; later human validation does not remove the disclosure duty (criterion 1). Taxonomy: *qualitative data analysis*.
2. **Does not require disclosure.** Spelling and punctuation correction plus reference-list reformatting of a text the author wrote and argued themselves. No effect on meaning, interpretation or substance.
3. **Doubtful — and we argue it is above the threshold.** Sustained use of an LLM as an adversarial sparring partner during conceptual design: the model is instructed to attack the author's framing, and the framing changes as a result. **No sentence and no code from the model reaches the manuscript**, so every text-centred disclosure rule reports nothing — yet the design of the work was shaped by the exchange. This is not a hypothetical: it is how the manuscript underlying this submission was developed, and seven design reversals are traceable to it. Under criteria (1) and (3) this is disclosable, but no existing category expresses it well (see 3B, missing category A). We flag it as the case where current disclosure practice is most systematically blind — precisely because the AI's contribution is invisible in the output.

### 1C. Position on the spectrum

▶ **In between — about as much as the above threshold says.**

Our disagreement with the draft is not about the height of the threshold. It is that a threshold alone decides only *whether* something is said, and says nothing about whether what is said is checkable.

### 1D. Agreement with statements

| Statement | Answer |
|---|---|
| AI use should be disclosed when it substantively influences the research process, interpretation, reported content, or results. | ▶ **Strongly agree** |
| The standard should define a minimum disclosure threshold, while allowing authors to disclose more if they wish. | ▶ **Strongly agree** |
| Routine spelling, grammar correction, reference formatting, or cosmetic editing should require disclosure. | ▶ **Rather disagree** |
| Repeated minor uses of AI can become disclosure-worthy when their cumulative influence shapes the work. | ▶ **Strongly agree** |

---

## 2 — Where should AI use be disclosed? (Placement)

### 2A. Placement

▶ **Both the main article content and a separate standalone statement can include information on AI use.**

### 2B. Which locations for which kinds of information

Three tiers, with a single source of truth:

1. **Methods and figure captions (narrative):** *why* AI was used, how it fit the design, what its use means for interpreting the results. This is methodological transparency and belongs where the method is described. It cannot be standardised beyond a controlled vocabulary, and should not be.
2. **A separate structured statement (comparable, machine-readable):** the rows — task, actor, verification level, trace, access conditions. Published next to author-contribution and COI statements, and available as data, not only as rendered prose. This is what makes cross-article comparison, editorial screening and automated screening possible.
3. **A repository record (evidence):** prompts, logs, code, outputs, with persistent identifiers, hashes and access status. Not in the article; referenced from it.

**Critical implementation detail:** tiers 1 and 2 must be generated from one record, not written twice. Two hand-written descriptions of the same facts diverge, and a divergence between them is indistinguishable from misconduct. In our implementation this is one JSON file from which publisher-specific statements are generated; the same file renders the human-readable panel. Recommendation for the standard: define the record, then define the renderings.

### 2C. Other comments on placement

The "may increase article length" objection is real and is solved by tier 2 being **data attached to the article rather than words in it** — the structured statement should not consume word count, exactly as a COI statement or a data-availability statement does not.

The stigmatisation objection deserves a direct answer: a separate statement singles out AI *today*, and will look transitional in ten years. That is acceptable. Author-contribution statements were also once a novelty motivated by a specific integrity problem. Design the record so it can be absorbed into a general contributorship record later (P1, P2) rather than avoiding it now.

---

## 3 — How should AI disclosure be structured? (Taxonomy)

### 3A. Adequacy of the proposed 18-category taxonomy

▶ **Mostly adequate, but a few categories are missing.**

### 3B. Views on the proposed taxonomy

We tested the 18 categories by mapping them onto a working implementation (CRediT roles plus five AI-specific extensions) and re-classifying our own manuscript with them. The full crosswalk, including where our own vocabulary is deficient, is published as a machine-readable file: [`taxonomy-crosswalk-v0.1.json`](./taxonomy-crosswalk-v0.1.json). Summary of what the exercise showed:

**Granularity is right, and slightly better than ours.** Splitting *quantitative* from *qualitative* data analysis (12/13) and *data visualization* from *figure or image generation* (14/15) are both correct calls that our own vocabulary got wrong by collapsing them into CRediT's coarser roles. We will adopt both splits. Categories 3, 4, 17 also expose real gaps in our vocabulary (literature summarisation, translation).

**Three missing categories.**

- **(A) Orchestration / agent operation.** Who configured, prompted and ran the system; which agent selected which sub-agents; which workflow was executed. Every one of the 18 categories describes a *research task the AI performed*; none describes *the human's act of directing it*, and none describes a supervisory agent's act of directing other agents. The Focus Track's own session 4.B made this point ("when supervisory agents select specialist agents, a disclosure statement has to say more than the name of one chatbot"), and it is the case from 1B example 3: substantive influence with zero output-side footprint. Without this category, agentic workflows are disclosable only as a list of tools.
- **(B) Verification performed by AI.** Category 10 says "code generation/refinement/**auditing**" and 11 says "cleaning/preprocessing/**auditing**": verification tasks are currently smuggled into production categories. But AI-run checking is a distinct act with distinct integrity properties — reference resolution, claim-support checking, statistical audit, code review, and increasingly "review by specialised AI agents", which was named in session 4.B. It must be recordable *as checking* (and see P5: which kind of checking).
- **(C) Selection among multiple runs or outputs.** Which run was reported, out of how many, under what selection rule. This is a research task with heavy integrity weight — undisclosed selection of the best run across many attempts is a known driver of inflated apparent quality in autonomous-research demonstrations — and it is invisible in every disclosure scheme we have seen, including this draft. A category makes it *possible* to disclose; making it *mandatory* for agentic pipelines is a separate policy choice we would support.

**Ambiguity and overlap to resolve.**

- 8 *Data collection (operations)* vs 9 *Data creation*: "creation" reads as synthetic/simulated data generation, but can be read as collection. Rename 9 to *Synthetic or simulated data generation* and define both.
- 4 *Literature summarization* vs 16 *Drafting text*: an AI-written literature-review section is both. State the rule (classify by the task, allow multiple categories per use).
- 18 bundles *editing/rewriting* with *reference lists*. Reference handling has a specific, checkable failure mode (non-resolving citations) and deserves separation from prose editing.
- 5/6/7 as `Design > …` sub-entries is good; make the parent/child relation explicit and machine-readable, otherwise implementers will flatten it inconsistently.

**Structural recommendations (the part that decides whether "machine-readable" is real).**

1. **Stable identifiers, slug-based, not ordinals** (P1). `vs:literature-search`, not "category 3". Ordinals break the moment a category is inserted or retired. Publish the list as a versioned machine-readable vocabulary (JSON/SKOS) with `deprecated` and `replaced_by`. CRediT's route via ANSI/NISO Z39.104-2022 is the precedent, and the reason CRediT is usable in metadata today.
2. **Rows, not sentences** (P2). A category alone does not carry a disclosure. The minimum row is: *task* (category ID) · *actor* (which AI system / which human) · *what was checked and by whom* · *trace* (what record exists and how it can be accessed). This is exactly the structure Round 1 asked for — a consistent core with room for free description — and it is what our implementation validates.
3. **Note that the taxonomy classifies tasks, and disclosure needs one more axis.** The draft says this ("merely a classification of research tasks"). We agree, and that is precisely the point: without the verification axis (§5), the taxonomy tells a reader what AI touched but not what anyone did about it.

---

## 4 — Should non-empty AI disclosure be mandatory?

### 4A. Agreement with statements

| Statement | Answer |
|---|---|
| Journals should require authors to include a non-empty disclosure (including a negative disclosure when they have not substantively used AI). | ▶ **Strongly agree** |
| Agreement with a publisher policy on AI disclosure is convincing enough to trust that AI reporting was accurate. | ▶ **Strongly disagree** |

### 4B. View on mandatory non-empty disclosure and "null" declarations

**Support, for a reason that is not the usual one.** The culture-change argument is fine but soft. The strong argument is evidentiary: silence cannot be falsified, whereas a null declaration is a **specific, dated, attributable assertion**. If evidence later shows substantive undisclosed AI use, silence yields an argument about interpretation ("nobody asked"), while a null declaration yields a documented false statement with a named author and a timestamp. Mandatory non-empty disclosure does not prevent dishonesty; it converts fog into a paper trail. That is a large gain for a one-line cost.

Three conditions, without which the null declaration becomes exactly the empty sentence the standard is replacing:

1. **Scope it to versions** (P9). *"Apart from the AI uses disclosed here, the authors did not use AI meeting the disclosure threshold of the Global Reporting Standard v1.0 (taxonomy v1.0) in the preparation of this work."* A declaration that does not name the threshold it was measured against cannot be assessed two years later, when the threshold has moved — and it will move; the standard is explicitly a living one.
2. **Bind it to the accepted version** (P4). A declaration made at submission and never re-affirmed is a claim about a file that no longer exists. Require re-affirmation at acceptance, attached to the accepted manuscript's content hash. This closes what we call the *dangling-attestation* problem: a check that outlives what it checked. It is cheap — a SHA-256 hash costs a second to compute and anyone can verify it — and it is the single most under-used mechanism available to this standard.
3. **Do not let the tick-box substitute for it.** Consenting to a publisher policy at submission is invisible to readers and unfalsifiable in retrospect. The declaration must be published with the article.

**On stigmatisation:** the risk is real but is mostly a function of wording. A null declaration phrased as an absence of *threshold-meeting* use, in the same block as the COI statement, normalises rather than singles out. The greater stigma risk today is the opposite one — that honest disclosers appear worse than silent non-disclosers.

---

## 5 — How to signal responsibility and accountability?

### 5A. Should a general responsibility statement be part of AI disclosure?

▶ **Yes, a default statement should be part of the disclosure standard.**

### 5B. View on general responsibility statements

Include it, but do not let it stand alone, and make it **attributable rather than collective**. "The authors take full responsibility" is true of every paper ever published and therefore carries no information; the box-ticking objection is correct as applied to that wording. What does carry information is a named person with a persistent identifier accepting responsibility for a specific AI use at a specific time — one guarantor per disclosed row where AI use was substantive, comparable to a corresponding-author role. In our implementation this is a required field (guarantor ORCID + timestamp), and it costs the author nothing they do not already know.

So: keep the default sentence for the general case, and require **named oversight per substantive use** (see 5E, last row, which we rate Essential).

### 5C. What information about verification and oversight should authors disclose

This is where we have the most to offer, because we built it and then failed at it ourselves.

**Structured, not narrative — with a narrative slot.** The example statements in the preparatory reading illustrate the problem: the "generic" example ("the authors reviewed and edited all AI-generated content") is unfalsifiable, and the "rigorous" and "descriptive" examples are excellent but cannot be compared across articles, screened at scale, or checked for internal consistency. A five-slot row per disclosed use is feasible in minutes and is comparable:

| Slot | Content | Why |
|---|---|---|
| 1. Task | taxonomy category ID | comparability |
| 2. Actor | which AI system (provider, model family, **version/snapshot**, interface) or which human | "we used an LLM" is not a description of a tool; a dated version is |
| 3. What was checked, by whom | closed list: *not checked* · *read-through by author* · *sampled (state fraction)* · *fully re-executed / recomputed* · *cross-checked against primary sources* · *checked by a named third party* · *independently reproduced* | this is the axis that turns disclosure into accountability |
| 4. Trace | what record exists (prompt/log/code/output), its identifier and hash, and its access status: *public · embargoed · on request · restricted · not retained* — with a reason whenever it is not public | prompts and logs frequently cannot be published (personal data, licensed text, third-party material); an unpublishable record can still be *hash-referenced*, which makes later substitution detectable |
| 5. What could not be checked | short free text, **required** | the most informative field in the whole record, and the first one that will be dropped if it is optional |

**The closed list in slot 3 is a ladder, and the Focus Track has already drawn it.** Session 4.B proposed attestation → review → audit → replication. Our implementation uses four evidence levels (*declared → artifact-linked → independently attested → reproduced*). These are two views of the same structure, and the difference is instructive: Perkins's ladder grades **the strength of the checking act**, ours grades **what a third party can verify about the claim**. Both axes are needed, because "I inspected the output" with no surviving trace is, evidentially, a level-1 claim:

| Session 4.B ladder | What it asserts | Evidence level once you ask what remains |
|---|---|---|
| Attestation — "I take responsibility" | responsibility | **declared** — a named person's word, visibly unverified |
| Review — "I inspected the output" | self-check | **declared**, or **artifact-linked** if the review left a durable trace |
| Audit — "I checked process and evidence" | process check | **artifact-linked** if author-run; **independently attested** if a named third party did it, with a stated scope |
| Replication — "I reproduced or cross-checked" | re-execution | **reproduced** |

Two consequences worth putting in the standard explicitly:

- **The existence of a log does not raise the level of a claim about the work.** A log may be incomplete or about something else. Our rule: an artifact raises a claim to level 2 (there is a trace) and never higher on its own. Only a named external checker or a re-execution goes higher.
- **Separate "resolved" from "supported"** (P5). Automated tools reliably establish that a cited source exists and that its metadata match. They do **not** reliably establish that the source supports the specific claim it is cited for. These must be two fields with two names, or the standard will produce a "citations verified" label that certifies only existence — a false assurance worse than no assurance. We keep three distinct concepts: *references resolved* (machine), *claim support assessed* (report, with method and confidence), *claim support attested* (named human, bounded scope).

### 5D. Where should verification and oversight information be findable?

▶ Tick: **In a separate statement in the article** · **In a repository, as complementary materials** · **Available on demand for reviewers, readers, journal**

Not "main content only" (not comparable), and not "recorded but inaccessible" (an unverifiable record is not evidence). The three-tier answer from 2B applies: pointer in the article, record in a repository, restricted artefacts on request — with **hashes published even for artefacts that are not**, so that restricted evidence is still tamper-evident.

### 5E. Desirability of specific information

| Item | Rating |
|---|---|
| Which risks were considered and mitigated (hallucination, inaccuracy, bias, privacy, security, copyright, IP) | ▶ **Moderately desirable** |
| What aspects of the work were reviewed, verified, or corrected by humans | ▶ **Essential** |
| How sources, citations, factual claims, data, or outputs were checked against reliable sources or primary data | ▶ **Essential** |
| Any limitations in verification, including aspects of AI outputs that could not be fully checked | ▶ **Essential** |
| Whether records of AI interactions, prompts, logs, or audit trails were retained, and under what conditions they are accessible | ▶ **Essential** |
| Who (which human) was responsible for oversight and verification of each AI use | ▶ **Essential** |

*Note on the first row.* We rate risk-mitigation narratives lower than the other five deliberately, and it is the only rating where we expect disagreement. Generic risk prose is the most easily produced and least checkable part of any disclosure; it will converge on boilerplate within one publication cycle. The other five items are all statements someone can be confronted with. Keep the risk field, make it optional and prompt it with the specific risks — but do not let it become the field authors fill in *instead* of the checkable ones.

### 5F. What the Reporting Standard should advise on making verification and oversight transparent

1. **Advise recording the absence of verification as explicitly as its presence.** A standard whose only positive signals are "checked" will be filled in with "checked". The value of a graded record is symmetric: it makes a missing check *legible* instead of *invisible*. Practically: an author who declares five substantive AI uses of which two were never independently checked has produced a more informative and more trustworthy document than one who asserts blanket review of everything.
2. **Advise binding every verification claim to a content hash** (P4). This is the one recommendation we would keep if forced to drop all others. A verification claim that names a file state cannot be inherited by a later, different file state. Without it, "verified" is a claim about a title.
3. **Advise on curated evidence, and require the curation rule** (P6, Appendix B). Raw logs and prompt histories are routinely *not publishable*: they contain personal data, licensed or third-party unpublished material, and dead ends. A curated log, however, is weaker evidence the more it was curated — and nobody can see what was removed. Our proposed rule, transferred from how the strict track of our own deployment plan handles agentic run selection: **publish the selection rule.** Concretely: compute the hash of the *complete* raw export and archive it non-publicly; publish the curated version with its own hash; record **both hashes, the curation criterion, and the kinds of material removed**. The claim stays at "artifact-linked", but a reader can see that the evidence is redacted and on what principle. Where even that is impossible, the honest move is to drop the claim to "declared". A standard that recognises "log retained" without asking *which* log and *under what selection* will get formalism instead of evidence.
4. **Advise that verification information be machine-generatable** (P8), and say so in a way tool providers can act on: publish a reference serialisation of the record and an example export. See §6 — this is where we have data rather than an opinion.
5. **Do not certify.** A structured verification record invites an aggregate score ("provenance quality: 8/10"). We recommend the standard state explicitly that no field or combination of fields constitutes a quality or truth judgement about the research. Certification carries liability a reporting standard cannot bear, aggregate scores get optimised rather than satisfied, and venues legitimately differ in what they require. Record who did what and what was evidenced; stop there.

---

## 6 — Summary and other feedback

**We applied this standard's logic to our own manuscript, and the two things that broke are our main contribution to Round 2.**

**(1) Retrospective provenance is one to two orders of magnitude more expensive than capture at source — and stays incomplete.** Reconstructing, after the work was finished, which model did what at which stage meant walking back through session histories and dating claims. Facts that cost a second to record at the moment of use cost tens of minutes to reconstruct afterwards, and several remained unresolvable. The consequence for the standard is direct: **a standard that relies on voluntary retrospective completion will be completed superficially, and disclosure quality will vary with how much effort the author had left rather than with how much AI was used.** Round 1 already asked for machine-generatability; we would strengthen it from a desirable property to a design requirement, and add two operational asks: publish a reference serialisation with worked examples, and open a channel to AI tool and platform providers for a **disclosure export** (task-level, timestamped, hash-anchored). The asymmetry is favourable: the heavier the AI involvement, the more automatable the record — agentic pipelines can emit it as they run. Tooling that captures beats guidance that asks.

**(2) Raw logs are not a publishable artefact — and curated logs are evidence only if the curation rule is public.** Our own first card asserted artifact-linked evidence pointing at a working-session log that we cannot release as-is: it contains third-party unpublished material, personal notes and personal data. There were exactly two honest options: publish a curated version *with its selection rule*, or drop the affected claims back to "declared". This was a failure of our own design, found only by using it, and the fix is Appendix B — the two-hash curation record. We recommend the Vancouver Standard include it, in whatever wording it prefers, because "log retained" without a curation rule will otherwise be the cheapest way to look evidenced without being evidenced.

We report a third observation as an argument for the ladder, not for us: **applying a graded record forced us to lower our own claims.** A disclosure format whose honest use costs the author something is doing its job; that is also the strongest reason to keep the levels closed and few.

**On process.** The three-round design, publishing the preparatory reading, and asking about placement and taxonomy separately have made this consultation unusually easy to engage with substantively. Two suggestions: (a) publish the round-2 outcome as a **versioned, machine-readable draft** (vocabulary file plus example records), not only as prose, so implementers can respond in round 3 with running code instead of comments; (b) invite at least one implementation report per round from someone who has tried to fill in the record — the failures are more informative than the endorsements.

**What we can contribute.** A working open implementation profile (schema, validator, reference-resolution check, publisher-statement generator, git-based registry, rendered panels; spec CC BY 4.0, code MIT); the taxonomy crosswalk in Appendix A as a maintained machine-readable file; pilot data from applying it to real manuscripts; and a mapping layer to whatever vocabulary the standard adopts. We are also happy to be a test implementer for a round-3 draft: give us a draft vocabulary and we will report back what validates and what does not.

**Honest limits of this submission.** This is a single-author project at an early stage. Its registry currently holds one card — our own. It has no independent attestations. Its self-application produced the two findings above by failing, not by succeeding. Nothing here is pilot evidence at scale; it is one implementation's experience, offered as such.

---

## Attribution and contact preferences

- **Optional attribution:** *Jan Nehyba, Assistant Professor, Faculty of Education, Masaryk University (Czechia)* — willing for open-text comments to be attributed. *(Change if you prefer to stay unattributed.)*
- **Contact after submission:** ▶ Yes, contact me about my answers · ▶ Yes, invite me for the 3rd Consultation Round · ▶ Yes, keep me updated on the final result
- **How I found out about this round:** ▶ Other → *"Following the Focus Track publicly (ISC website); developing an implementation profile for this standard."*
- **Relationship with AI systems:** ▶ Professional-heavy AI user
- **Role/career stage:** ▶ Active researcher (with PhD or equivalent) · ▶ Researcher with a permanent contract

---

## Appendix A — Crosswalk: proposed 18 categories ↔ a working implementation

Machine-readable version: [`taxonomy-crosswalk-v0.1.json`](./taxonomy-crosswalk-v0.1.json). Suggested identifiers are illustrative (slug form, per P1); `credit:*` are CRediT roles (ANSI/NISO Z39.104-2022), `rpc:*` are our AI extensions.

| # | Proposed category | Suggested ID | Maps to | Note |
|---|---|---|---|---|
| 1 | Idea generation | `vs:idea-generation` | `credit:conceptualization` | coarse on our side: 1 and 2 collapse |
| 2 | Hypothesis development | `vs:hypothesis-development` | `credit:conceptualization` | as above |
| 3 | Literature search | `vs:literature-search` | `rpc:source_retrieval` | exact match |
| 4 | Literature summarization | `vs:literature-summarization` | — | **gap on our side** → adding `rpc:literature_synthesis`; overlaps 16 |
| 5 | Design › study/experiment design | `vs:design-study` | `credit:methodology` | make parent/child explicit |
| 6 | Design › data collection methodology | `vs:design-data-collection` | `credit:methodology` | |
| 7 | Design › data analysis plan | `vs:design-analysis-plan` | `credit:methodology` | |
| 8 | Data collection (operations) | `vs:data-collection` | `credit:investigation` | ambiguous vs 9 |
| 9 | Data creation | `vs:synthetic-data-generation` | — | **rename**: synthetic/simulated data; gap on our side |
| 10 | Code generation/refinement/auditing | `vs:code-generation` | `credit:software`, `rpc:code_generation` | "auditing" belongs in missing category B |
| 11 | Data cleaning/preprocessing/auditing | `vs:data-preparation` | `credit:data_curation` | as above |
| 12 | Quantitative data analysis | `vs:quantitative-analysis` | `credit:formal_analysis` | their split is better than ours |
| 13 | Qualitative data analysis | `vs:qualitative-analysis` | `credit:formal_analysis` | **we will adopt this split** |
| 14 | Data visualization | `vs:data-visualization` | `credit:visualization` | |
| 15 | Figure or image generation | `vs:image-generation` | `credit:visualization` | **we will adopt this split**; integrity-critical |
| 16 | Drafting manuscript or abstract text | `vs:drafting-text` | `credit:writing_original_draft`, `rpc:text_generation` | |
| 17 | Translation | `vs:translation` | — | **gap on our side** → adding `rpc:translation`; equity note in 1A(c) |
| 18 | Editing or rewriting incl. reference lists | `vs:editing-rewriting` | `credit:writing_review_editing` | split reference handling out |
| **A** | *Orchestration / agent operation* | `vs:orchestration` | `rpc:prompt_orchestration`, `rpc:agent_operation` | **proposed addition** |
| **B** | *Verification performed by AI* | `vs:ai-verification` | recorded as machine `checks`, not activities | **proposed addition** |
| **C** | *Selection among runs/outputs* | `vs:output-selection` | proposed `rpc:run_selection` | **proposed addition**, integrity-critical |

## Appendix B — Proposed record for curated evidence (the two-hash rule)

Applies whenever a prompt/log/interaction record is published in edited form. Field names are ours; the requirement is what matters.

```json
{
  "id": "log_curated",
  "type": "log",
  "uri_or_pid": "<DOI of the deposited curated log>",
  "sha256": "<hash of the published curated version>",
  "access_status": "public",
  "curation": {
    "raw_sha256": "<hash of the complete raw export>",
    "raw_access_status": "restricted",
    "rule": "Removed passages containing third-party unpublished material, personal notes and personal data. Substantive content, including the model's incorrect statements and their corrections, left unchanged.",
    "removed_kinds": ["third-party unpublished material", "personal notes", "personal data"]
  }
}
```

Three requirements, independent of syntax:

1. The hash of the **complete raw export** is recorded and the raw export is archived, even when it is not published.
2. The **published** version carries its own hash and identifier.
3. The **curation criterion and the kinds of material removed** are stated.

Rationale: a redacted record is still tamper-evident (1, 2) and its evidential weight becomes assessable (3). Without (3), "log retained" is a formality; with it, a reader knows what kind of evidence they are looking at. Where none of the three can be satisfied, the associated claim should return to the lowest level rather than be reported as evidenced.

## Appendix C — How the six Round-1 criteria are met by a row-based record

| Round-1 criterion | How a row-based, hash-bound record delivers it |
|---|---|
| Easy to understand and easy to make | one row per disclosed use; the expensive fields (hashes, versions) are computed, not written; publisher statements generated from the record |
| Consistent structure, comparable and reproducible | closed vocabularies for task, actor kind, verification level, access status |
| Machine-readable **and machine-generatable** | one validated data file, schema-checked; agentic pipelines can emit it as they run (P8) |
| Flexible description of nature and extent | free-text description per row and a required "what could not be checked" field |
| Multiple tools and uses in a single work | actors and rows are lists; one work can carry many systems, versions and interfaces |
| Across disciplines and output types | task vocabulary is discipline-agnostic; discipline-specific exemplars and sub-categories hang off it (1A(b)) |

---

*Prepared for submission via <https://council.science/AIdisclosure> by 16 October 2026. Questions to Bert Seghers (office@enrio.eu) or, on survey ethics, Mike Perkins (mike.p@buv.edu.vn). Sources for all process facts cited here are listed in [`README.md`](./README.md).*
