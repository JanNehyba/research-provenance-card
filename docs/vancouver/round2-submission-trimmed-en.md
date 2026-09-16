# Consultation Round 2: Submission (trimmed version)

**Towards a Global Reporting Standard for AI Disclosure in Research ("Vancouver Standard")**
Focus Track of WCRI 2026 · ISC · WCRIF · COPE · STM · GYA
Submission deadline: **16 October 2026** · Webform: <https://council.science/AIdisclosure>

---

**About this version.** This is a trimmed submission derived from the full text in [`round2-submission-en.md`](./round2-submission-en.md). It keeps the four proposals that stand on their own and removes the earlier implementation work, its framing and its attachments. Before submitting, open the webform in a browser and check that the questions and options still match those of 29 July 2026. The recommended tick-box answers are marked ▶ so the whole submission can be transferred in one pass.

## Respondent

| Field | Value |
|---|---|
| Name | Jan Nehyba |
| Role | Assistant Professor, Faculty of Education, Masaryk University, Brno, Czechia |
| ORCID | 0000-0003-4159-5576 |
| Capacity | Personal perspectives of a natural person |
| Discipline | Educational research / social sciences (qualitative methods) |
| Country | Czechia |
| Contact | *[institutional e-mail: fill in before submitting]* |

**Basis of this response.** The answers below are not a position paper. They are the perspective of a qualitative researcher currently studying how people introduce, sign and label AI-assisted texts across genres: research articles, emails and chat messages, teaching and internal materials, and software projects. That work looks at the wording of disclosure statements and at which components of responsibility the wording actually carries. Nothing below rests on a formal implementation or on pilot findings; where an example is drawn from my own practice, it is marked as such.

---

## 0: Summary: four proposals

| # | Proposal | Question |
|---|---|---|
| **P1** | Give every taxonomy category a **stable, machine-readable identifier** (slug, not ordinal) and version the taxonomy itself, with a deprecation/replacement policy. The precedent is CRediT as ANSI/NISO Z39.104-2022. Without stable IDs, "machine-readable" cannot be delivered downstream. | 3 |
| **P2** | Make the unit of disclosure a **row, not a sentence**: one row per (task × actor × what-was-checked × trace). Narrative prose can accompany a row; it cannot replace it if disclosures are to be comparable. | 3 |
| **P3** | Add an **evidence/verification level** to every row, from a closed list. Round 1's criteria and the Focus Track's own "verification ladder" (attestation → review → audit → replication) already point here; a closed list is what makes it machine-readable. | 5 |
| **P4** | **Bind the disclosure to the version it describes** via a content hash (SHA-256) of the accepted file. Disclosures and verification claims currently attach to a title, not to a state of a file, so they survive silent replacement of content. | 4, 5 |

---

## 1: Which AI use should be disclosed? (Thresholds)

### 1A. Views on the proposed disclosure threshold

**I support the proposed qualitative threshold as written, including the explicit rejection of quantitative thresholds.** The footnote's reasoning is correct and worth stating even more firmly in the final standard: there is no unit, no instrument and no audit procedure for "percentage of AI contribution". Percentages invite two failure modes: authors guessing, and third-party detectors producing numbers ("this manuscript is 40% AI") that can be neither confirmed nor refuted. A role-based, task-based claim is a different kind of statement: it can be confronted with code, logs, outputs and named checkers.

I also support criterion (1), that delegated or AI-shaped judgement is disclosure-worthy **even if a human later validated the result**. This is the single most important sentence in the draft, because it blocks the most common evasion ("I checked it, so it's mine").

Three refinements:

**(a) Do not let the threshold carry the whole burden.** A binary threshold with a uniform reporting cost above it creates a cliff: the author who crosses it pays full price, the author just below pays nothing, and the incentive at the margin is to argue oneself below. Pair the threshold with a **graded record** (P3), so a marginal use can be honestly reported in one cheap row at the lowest evidence level, and a heavy, well-documented use can be reported as such. What should be proportionate is not *whether* one discloses but *how much evidence the record carries*.

**(b) "Substantive" needs discipline-level exemplars, not a better definition.** The reviewer/reader test is the right formulation, and further abstract refinement will not help. What will help is a small, growing, citable set of worked examples per domain (a dozen per discipline, maintained as part of the living standard), the way reporting-guideline networks accumulate exemplars. I can contribute educational-research examples.

**(c) Equity: language work must not be taxed by first language.** Category 17 (Translation) and the language part of category 18 create a structural asymmetry. A Czech, Ukrainian or Indonesian researcher who thinks and drafts in their own language and uses AI to produce English prose is doing the *same intellectual work* as an anglophone colleague, but under a literal reading of the threshold they must disclose more. Round 1 concluded the standard must not be harder to follow for less-resourced communities; this is where that principle bites. My proposed wording: **translation of the author's own content, with meaning preserved and verified by the author, is a technical use below the threshold and is disclosed only where the journal requires it; AI-generated *content* in any language is above the threshold regardless of which language it was generated in.** The line is authorship of the content, not the language of production.

### 1B. Three examples from my field (educational research, qualitative methods)

1. **Requires disclosure.** An LLM performs first-pass thematic coding of interview transcripts; the researcher reviews, adjudicates and revises the codes. Judgement that would normally be expert-human was delegated; later human validation does not remove the disclosure duty (criterion 1). Taxonomy: *qualitative data analysis*.
2. **Does not require disclosure.** Spelling and punctuation correction plus reference-list reformatting of a text the author wrote and argued themselves. No effect on meaning, interpretation or substance.
3. **Doubtful, and I argue it is above the threshold.** Sustained use of an LLM as an adversarial sparring partner during conceptual design: the model is instructed to attack the author's framing, and the framing changes as a result. **No sentence and no code from the model reaches the manuscript**, so every text-centred disclosure rule reports nothing, yet the design of the work was shaped by the exchange. This is not hypothetical: it is how the manuscript underlying this response was developed, and seven design reversals are traceable to it. Under criteria (1) and (3) this is disclosable, but no existing category expresses it well. I flag it as the case where current disclosure practice is most systematically blind, precisely because the AI's contribution is invisible in the output.

### 1C. Agreement with statements

| Statement | Answer |
|---|---|
| AI use that substantively shapes research content, interpretation, reported content, or results should be disclosed. | ▶ **Strongly agree** |
| The standard should define a minimum disclosure threshold, while allowing authors to disclose more if they wish. | ▶ **Strongly agree** |
| Routine spelling, grammar correction, reference formatting, or cosmetic editing should require disclosure. | ▶ **Rather disagree** |
| Repeated minor uses of AI can become disclosure-worthy when their cumulative influence shapes the work. | ▶ **Strongly agree** |

---

## 2: Where should AI use be disclosed? (Placement)

### 2A. Placement

▶ **Both the main article content and a separate standalone statement can include information on AI use.**

### 2B. Which locations for which kinds of information

Three tiers, with a single source of truth:

1. **Methods and figure captions (narrative):** *why* AI was used, how it fit the design, what its use means for interpreting the results. This is methodological transparency and belongs where the method is described. It cannot be standardised beyond a controlled vocabulary, and should not be.
2. **A separate structured statement (comparable, machine-readable):** the rows (task, actor, verification level, trace, access conditions). Published next to author-contribution and COI statements, and available as data, not only as rendered prose. This is what makes cross-article comparison, editorial screening and automated screening possible.
3. **A repository record (evidence):** prompts, logs, code, outputs, with persistent identifiers, hashes and access status. Not in the article; referenced from it.

**Critical implementation detail:** tiers 1 and 2 must be generated from one record, not written twice. Two hand-written descriptions of the same facts diverge, and a divergence between them is indistinguishable from misconduct. Recommendation for the standard: define the record, then define the renderings.

### 2C. Other comments on placement

The "may increase article length" objection is real and is solved by tier 2 being **data attached to the article rather than words in it**; the structured statement should not consume word count, exactly as a COI statement or a data-availability statement does not.

The stigmatisation objection deserves a direct answer: a separate statement singles out AI *today*, and will look transitional in ten years. That is acceptable. Author-contribution statements were also once a novelty motivated by a specific integrity problem. Design the record so it can be absorbed into a general contributorship record later (P1, P2) rather than avoiding it now.

---

## 3: How should AI disclosure be structured? (Taxonomy)

### 3A. Adequacy of the proposed 18-category taxonomy

▶ **Mostly adequate.**

### 3B. Views on the proposed taxonomy

The granularity is broadly right. Splitting *quantitative* from *qualitative* data analysis (12/13) and *data visualization* from *figure or image generation* (14/15) are both correct calls; both prevent real confusions about what the AI did.

**Ambiguity and overlap to resolve.**

- 8 *Data collection (operations)* vs 9 *Data creation*: "creation" reads as synthetic/simulated data generation, but can be read as collection. Rename 9 to *Synthetic or simulated data generation* and define both.
- 4 *Literature summarization* vs 16 *Drafting text*: an AI-written literature-review section is both. State the rule (classify by the task, allow multiple categories per use).
- 18 bundles *editing/rewriting* with *reference lists*. Reference handling has a specific, checkable failure mode (non-resolving citations) and deserves separation from prose editing.
- 5/6/7 as `Design > …` sub-entries is good; make the parent/child relation explicit and machine-readable, otherwise implementers will flatten it inconsistently.

**Structural recommendations (the part that decides whether "machine-readable" is real).**

1. **Stable identifiers, slug-based, not ordinals** (P1). `vs:literature-search`, not "category 3". Ordinals break the moment a category is inserted or retired. Publish the list as a versioned machine-readable vocabulary (JSON/SKOS) with `deprecated` and `replaced_by`. CRediT's route via ANSI/NISO Z39.104-2022 is the precedent, and the reason CRediT is usable in metadata today.
2. **Rows, not sentences** (P2). A category alone does not carry a disclosure. The minimum row is: *task* (category ID) · *actor* (which AI system / which human) · *what was checked and by whom* · *trace* (what record exists and how it can be accessed). This is exactly the structure Round 1 asked for: a consistent core with room for free description.
3. **Note that the taxonomy classifies tasks, and disclosure needs one more axis.** The draft says this ("merely a classification of research tasks"). I agree, and that is precisely the point: without the verification axis (§5), the taxonomy tells a reader what AI touched but not what anyone did about it.

---

## 4: Should non-empty AI disclosure be mandatory?

### 4A. Agreement with statements

| Statement | Answer |
|---|---|
| Journals should require authors to include a non-empty disclosure (including a negative disclosure when they have not substantively used AI). | ▶ **Strongly agree** |
| Agreement with a publisher policy on AI disclosure is convincing enough to trust that AI reporting was accurate. | ▶ **Strongly disagree** |

### 4B. View on mandatory non-empty disclosure and "null" declarations

**Support, for a reason that is not the usual one.** The culture-change argument is fine but soft. The strong argument is evidentiary: silence cannot be falsified, whereas a null declaration is a **specific, dated, attributable assertion**. If evidence later shows substantive undisclosed AI use, silence yields an argument about interpretation ("nobody asked"), while a null declaration yields a documented false statement with a named author and a timestamp. Mandatory non-empty disclosure does not prevent dishonesty; it converts fog into a paper trail. That is a large gain for a one-line cost.

Two conditions, without which the null declaration becomes exactly the empty sentence the standard is replacing:

1. **Bind it to the accepted version** (P4). A declaration made at submission and never re-affirmed is a claim about a file that no longer exists. Require re-affirmation at acceptance, attached to the accepted manuscript's content hash. This closes the *dangling-attestation* problem: a check that outlives what it checked. It is cheap, a SHA-256 hash costs a second to compute and anyone can verify it, and it is the single most under-used mechanism available to this standard.
2. **Do not let the tick-box substitute for it.** Consenting to a publisher policy at submission is invisible to readers and unfalsifiable in retrospect. The declaration must be published with the article.

**On stigmatisation:** the risk is real but is mostly a function of wording. A null declaration phrased as an absence of *threshold-meeting* use, in the same block as the COI statement, normalises rather than singles out. The greater stigma risk today is the opposite one: that honest disclosers appear worse than silent non-disclosers.

---

## 5: How to signal responsibility and accountability?

### 5A. Should a general responsibility statement be part of AI disclosure?

▶ **Yes, a default statement should be part of the disclosure standard.**

### 5B. View on general responsibility statements

Include it, but do not let it stand alone, and make it **attributable rather than collective**. "The authors take full responsibility" is true of every paper ever published and therefore carries no information; the box-ticking objection is correct as applied to that wording. What does carry information is a named person with a persistent identifier accepting responsibility for a specific AI use at a specific time: one guarantor per disclosed row where AI use was substantive, comparable to a corresponding-author role. It costs the author nothing they do not already know.

So: keep the default sentence for the general case, and require **named oversight per substantive use** (see 5E, last row, which I rate Essential).

**A perspective from genres the standard does not cover.** A disclosure is also a language act: its wording can be decomposed into who sends the text, who chose the words, and who vouches for the content. These components combine differently in genres outside the research article. An email that opens with "Here is an AI summary" tells the recipient something no article-style statement says; a slide deck signed with a name only claims authorship and accountability at once; a commit message trailer ("Generated-with: …") allocates them differently again; a thesis statement page does it in a form prescribed by an institution. A standard written for research articles will not cover emails, teaching materials or internal documents, where the same responsibility is handled by other means (signatures, review conventions, naming rules). I suggest the standard state its genre scope explicitly, and not imply that an article-style statement is the model for all communication.

### 5C. What information about verification and oversight should authors disclose

**Structured, not narrative, with a narrative slot.** The example statements in the preparatory reading illustrate the problem: the "generic" example ("the authors reviewed and edited all AI-generated content") is unfalsifiable, and the "rigorous" and "descriptive" examples are excellent but cannot be compared across articles, screened at scale, or checked for internal consistency. A five-slot row per disclosed use is feasible in minutes and is comparable:

| Slot | Content | Why |
|---|---|---|
| 1. Task | taxonomy category ID | comparability |
| 2. Actor | which AI system (provider, model family, **version/snapshot**, interface) or which human | "we used an LLM" is not a description of a tool; a dated version is |
| 3. What was checked, by whom | closed list: *not checked* · *read-through by author* · *sampled (state fraction)* · *fully re-executed / recomputed* · *cross-checked against primary sources* · *checked by a named third party* · *independently reproduced* | this is the axis that turns disclosure into accountability |
| 4. Trace | what record exists (prompt/log/code/output), its identifier and hash, and its access status: *public · embargoed · on request · restricted · not retained*, with a reason whenever it is not public | prompts and logs frequently cannot be published (personal data, licensed text, third-party material); an unpublishable record can still be *hash-referenced*, which makes later substitution detectable |
| 5. What could not be checked | short free text, **required** | the most informative field in the whole record, and the first one that will be dropped if it is optional |

**The closed list in slot 3 is a ladder, and the Focus Track has already drawn it.** Session 4.B proposed attestation → review → audit → replication. Two axes are hiding in it, and the difference is instructive: Perkins's ladder grades **the strength of the checking act**, and a complementary axis grades **what a third party can still verify about the claim**. Both are needed, because "I inspected the output" with no surviving trace is, evidentially, a bare assertion:

| Session 4.B ladder | What it asserts | What a third party can verify |
|---|---|---|
| Attestation, "I take responsibility" | responsibility | the claim itself, visibly unverified |
| Review, "I inspected the output" | self-check | nothing, unless the review left a durable trace |
| Audit, "I checked process and evidence" | process check | a trace if author-run; a named third party's check with stated scope |
| Replication, "I reproduced or cross-checked" | re-execution | the reproduction |

One consequence worth putting in the standard explicitly: **the existence of a log does not by itself strengthen a claim about the work.** A log may be incomplete or about something else. A trace shows that something was recorded; only a named external checker or a re-execution shows that the claim was examined.

### 5D. Where should verification and oversight information be findable?

▶ Tick: **In a separate statement in the article** · **In a repository, as complementary materials** · **Available on demand for reviewers, readers, journal**

Not "main content only" (not comparable), and not "recorded but inaccessible" (an unverifiable record is not evidence). The three-tier answer from 2B applies: pointer in the article, record in a repository, restricted artefacts on request, with **hashes published even for artefacts that are not**, so that restricted evidence is still tamper-evident.

### 5E. Desirability of specific information

| Item | Rating |
|---|---|
| Which risks were considered and mitigated (hallucination, inaccuracy, bias, privacy, security, copyright, IP) | ▶ **Moderately desirable** |
| What aspects of the work were reviewed, verified, or corrected by humans | ▶ **Essential** |
| How sources, citations, factual claims, data, or outputs were checked against reliable sources or primary data | ▶ **Essential** |
| Any limitations in verification, including aspects of AI outputs that could not be fully checked | ▶ **Essential** |
| Whether records of AI interactions, prompts, logs, or audit trails were retained, and under what conditions they are accessible | ▶ **Essential** |
| Who (which human) was responsible for oversight and verification of each AI use | ▶ **Essential** |

*Note on the first row.* I rate risk-mitigation narratives lower than the other five deliberately, and it is the only rating where I expect disagreement. Generic risk prose is the most easily produced and least checkable part of any disclosure; it will converge on boilerplate within one publication cycle. The other five items are all statements someone can be confronted with. Keep the risk field, make it optional and prompt it with the specific risks, but do not let it become the field authors fill in *instead of* the checkable ones.

### 5F. What the Reporting Standard should advise on making verification and oversight transparent

1. **Advise recording the absence of verification as explicitly as its presence.** A standard whose only positive signals are "checked" will be filled in with "checked". The value of a graded record is symmetric: it makes a missing check *legible* instead of *invisible*. Practically: an author who declares five substantive AI uses of which two were never independently checked has produced a more informative and more trustworthy document than one who asserts blanket review of everything.
2. **Advise binding every verification claim to a content hash** (P4). This is the one recommendation I would keep if forced to drop all others. A verification claim that names a file state cannot be inherited by a later, different file state. Without it, "verified" is a claim about a title.
3. **Do not certify.** A structured verification record invites an aggregate score ("provenance quality: 8/10"). I recommend the standard state explicitly that no field or combination of fields constitutes a quality or truth judgement about the research. Certification carries liability a reporting standard cannot bear, aggregate scores get optimised rather than satisfied, and venues legitimately differ in what they require. Record who did what and what was evidenced; stop there.

---

## 6: Summary and other feedback

**Where this response comes from.** It is informed by ongoing qualitative work on how people word AI disclosures across genres: research articles, emails and chat messages, teaching and internal materials, and software projects. Among the questions that pilot asks: which components a real disclosure actually carries (role of the AI, share of the work, what the human did, accountability, certainty, state of the output, expectations of the recipient, placement), and how much of the wording is publisher template rather than author voice. Validated findings from that pilot can be offered for Round 3.

On process: the three-round design and the published preparatory reading have made this consultation unusually easy to engage with substantively. One suggestion: publish the round-2 outcome as a **versioned, machine-readable draft** (vocabulary file plus example records), not only as prose, so implementers can respond in Round 3 with running code instead of comments.

---

## Attribution and contact preferences

- **Optional attribution:** *Jan Nehyba, Assistant Professor, Faculty of Education, Masaryk University (Czechia)*, willing for open-text comments to be attributed.
- **Contact after submission:** ▶ Yes, contact me about my answers · ▶ Yes, invite me for the 3rd Consultation Round · ▶ Yes, keep me updated on the final result
- **How I found out about this round:** ▶ Other → *"Following the Focus Track publicly (ISC website); researching how people word AI disclosures across genres."*
- **Relationship with AI systems:** ▶ Professional-heavy AI user
- **Role/career stage:** ▶ Active researcher (with PhD or equivalent) · ▶ Researcher with a permanent contract

---

*Prepared for submission via <https://council.science/AIdisclosure> by 16 October 2026. Sources for process facts are listed in [`README.md`](./README.md).*





