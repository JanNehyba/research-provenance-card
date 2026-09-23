# Consultation Round 2: Submission

**Towards a Global Reporting Standard for AI Disclosure in Research ("Vancouver Standard")**
Focus Track of WCRI 2026 · ISC · WCRIF · COPE · STM · GYA
Deadline: **16 October 2026** · Webform: <https://council.science/AIdisclosure>

---

**About this version.** This is written in plain English on purpose. The answer in 1A(c) argues that the standard must not be harder to follow for researchers who do not write in English. A submission that argues this in dense prose would undercut its own point. Before submitting, open the webform in a browser and check that the questions still match those of 29 July 2026. Recommended tick-box answers are marked ▶.

## Respondent

| Field | Value |
|---|---|
| Name | Jan Nehyba |
| Role | Assistant Professor, Faculty of Education, Masaryk University, Brno, Czechia |
| ORCID | 0000-0003-4159-5576 |
| Capacity | Personal perspectives of a natural person |
| Discipline | Educational research, social sciences, qualitative methods |
| Country | Czechia |
| Contact | nehyba@ped.muni.cz |

**Where this comes from.** I am a qualitative researcher. I am currently studying how people introduce, sign and label texts written with AI, and how this differs by genre: research articles, emails and messages, teaching and internal materials, software projects, theses, and social media. That study asks what a real disclosure actually says, not what a standard says it should say. Nothing below rests on findings from it. It has no results yet.

### How this submission was produced

**This text was written by AI.** Not "with some AI assistance" in the usual sense of that phrase. Large language models drafted every section of it, over several working sessions, and the wording is theirs throughout. I set the direction, decided what went in and what came out, and I am accountable for all of it.

I am reporting this in the row format this submission asks the standard to adopt. A submission that argues for disclosure and hides its own production would not be worth reading. It also demonstrates the blind spot described in 1B(3): the third row is a real use that no text-based disclosure rule would ever catch.

| Task | Actor | What was checked, and by whom | Trace | What could not be checked |
|---|---|---|---|---|
| Drafting and rewriting every section | Claude (Anthropic), Opus 5, September 2026; earlier drafts by other models | Read by me, and reviewed at the level of arguments and decisions. Every recommendation is one I hold. | Public commit history: <https://github.com/JanNehyba/research-provenance-card/commits/vancouver/round2-trimmed> | Whether the models shaped the wording of arguments I agreed with, in ways I did not notice |
| Literature search and checking | Same | Each source opened in the original, and the verification status of each is recorded. | Verification log, public: <https://github.com/JanNehyba/research-provenance-card/blob/vancouver/round2-kit/docs/reserse.md> | Three sources were checked from the abstract only, not the full text |
| Shaping the argument | Me, using a model as a critic instructed to attack my framing | Not independently checked | **None. The exchange left no durable record.** | How much of the framing came from that exchange. I cannot reconstruct it. |
| Deciding what to include and what to cut | Me | Not independently checked | The same commit history | Nothing. These were my decisions and I stand behind them. |

Repository: <https://github.com/JanNehyba/research-provenance-card>
(The work described here sits on the `vancouver/round2-trimmed` and `vancouver/round2-kit` branches, not on the default branch.)

I hold responsibility for every claim in this submission.

---

## 0: Summary: seven proposals

| # | Proposal | Question |
|---|---|---|
| **P1** | Give every taxonomy category a **stable machine-readable identifier**, a slug rather than a number, and version the taxonomy itself, with rules for retiring and replacing a category. CRediT did this as ANSI/NISO Z39.104-2022. Without stable identifiers, nobody downstream can deliver "machine-readable". | 3 |
| **P2** | Make the unit of disclosure a **row, not a sentence**. One row per task, actor, check and trace. Prose can accompany a row. It cannot replace one, if disclosures are meant to be comparable. | 3 |
| **P3** | Give every row a **verification level** from a closed list. Round 1's criteria and the Focus Track's own ladder (attestation, review, audit, replication) already point this way. A closed list is what makes it machine-readable. | 5 |
| **P4** | **Tie the disclosure to the version it describes**, using a content hash (SHA-256) of the accepted file. Today a disclosure is attached to a title, not to a state of a file. That is why it survives a silent change of content. | 4, 5 |
| **P5** | Add **three missing categories**: orchestration (configuring and directing the system), verification performed by AI, and selection among several runs or outputs. | 3 |
| **P6** | **Keep at least one required field that a machine cannot fill on its own.** A record that an agent can generate in full, and another agent can check, may be complete, well-formed and empty. | 5 |
| **P7** | **Create a persistent identifier for the AI systems themselves**, on the model of RRID rather than of authorship. A named, versioned, citable identifier for a tool is what makes "which model, which version" a checkable fact instead of a phrase. | 3, 5 |

### Why the proposals look like this

A useful distinction comes from a nearby field. Corbin, Dawson and Liu (2025) describe two kinds of change to assessment.[^1] **Discursive** changes work only by telling people what they should do. **Structural** changes alter how a task must be completed. Their argument is that instructions alone do not hold, because people stay free to ignore them.

The same split applies here. A standard that prescribes a sentence authors should write is discursive. A standard that defines a record, with required fields and a closed list of verification levels, is structural. All seven proposals are attempts to move this standard from the first kind towards the second.

[^1]: Corbin, T., Dawson, P., & Liu, D. (2025). Talk is cheap: why structural assessment changes are needed for a time of GenAI. *Assessment & Evaluation in Higher Education*, 50(7), 1087-1097. That paper is about student assessment, not about disclosure. I am borrowing the distinction, not the findings.

---

## 1: Which AI use should be disclosed? (Thresholds)

### 1A. Views on the proposed threshold

**I support the qualitative threshold as written, including the decision not to use quantitative thresholds.** The reasoning in the footnote is right, and the final standard should say it even more plainly. There is no unit for "percentage of AI contribution". No instrument measures it and no procedure audits it.

Percentages go wrong in two ways. Authors guess. And detectors produce numbers such as "this manuscript is 40% AI" that nobody can confirm or refute. A claim about roles and tasks is a different kind of claim. You can hold it up against code, logs, outputs, and named people.

I also support criterion (1): AI-shaped judgement should be disclosed **even when a human validated the result afterwards**. This is the most important sentence in the draft. It blocks the most common way out, which is "I checked it, so it is mine".

Three refinements.

**(a) Do not make the threshold carry everything.** A single line, with the same reporting cost for everyone above it, creates a cliff. Cross the line and you pay the full price. Stay just below and you pay nothing. So an author near the line has every reason to argue they are below it.

Pair the threshold with a **graded record** (P3). Then a small use can be reported honestly, in one cheap row at the lowest level. A large, well-documented use can be reported as that. What should scale is not *whether* you disclose. It is *how much evidence the record carries*.

**(b) "Substantive" needs examples, not a better definition.** The reviewer test is the right test, and more abstract refinement will not help. What will help is a small set of worked examples for each field, perhaps a dozen each, kept and cited as part of the living standard. Reporting-guideline networks build up exemplars this way. I can contribute examples from educational research.

**(c) Language work must not be taxed by the author's first language.** Category 17 (Translation), and the language part of category 18, create an imbalance.

A Czech, Ukrainian or Indonesian researcher thinks and drafts in their own language, then uses AI to produce English prose. The intellectual work is the same as an anglophone colleague's. But read the threshold literally and they must disclose more. Round 1 concluded that the standard must not be harder for less-resourced communities. This is where that promise is tested.

Proposed wording: **translating the author's own content, with the meaning preserved and checked by the author, is a technical use below the threshold. AI-generated content is above the threshold, in any language.** The line is who wrote the content, not which language it was produced in.

### 1B. Three examples from my field (educational research, qualitative methods)

1. **Needs disclosure.** An LLM does the first pass of thematic coding on interview transcripts. The researcher then reviews, decides and revises. Judgement that a trained human would normally make was handed over. Checking it afterwards does not remove the duty to disclose (criterion 1). Category: qualitative data analysis.

2. **Does not need disclosure.** Fixing spelling and punctuation, and reformatting a reference list, in a text the author wrote and argued themselves. Nothing about the meaning changes.

3. **Unclear, and I argue it is above the threshold.** An author uses an LLM over a long period as a sparring partner while designing the work. The model is told to attack the author's framing. The framing changes as a result.

   **Not one sentence from the model reaches the manuscript.** So every rule that looks at the text reports nothing. Yet the design of the work was shaped by the exchange.

   This is how I work, and the framing of my work does change this way. See the third row of the table above. I disclosed this use, and I could not reconstruct how much of my framing came from it. Under criteria (1) and (3) it should be disclosed, but no category fits it. The *orchestration* category proposed in 3B (P5) is meant to fill that gap.

   I flag this as the case where current practice is most systematically blind, and the reason is simple. The AI's contribution is invisible in the output.

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

Three tiers, with one source of truth behind them.

1. **Methods and figure captions, in prose.** Why AI was used, how it fitted the design, and what that means for reading the results. This is methodological transparency and it belongs where the method is described. It cannot be standardised beyond a controlled vocabulary, and it should not be.

2. **A separate structured statement, comparable and machine-readable.** The rows: task, actor, verification level, trace, access conditions. Published next to the author-contribution and conflict-of-interest statements, and available as data, not only as rendered prose. This is what makes comparison across articles, and screening at scale, possible at all.

3. **A repository record, holding the evidence.** Prompts, logs, code, outputs, with persistent identifiers, hashes, and an access status. Not in the article. Referenced from it.

**One implementation detail matters more than it looks.** Tiers 1 and 2 must be generated from one record. They must not be written twice. Two hand-written descriptions of the same facts drift apart, and a reader cannot tell drift from misconduct. So define the record first, then define how it is displayed.

### 2C. Other comments on placement

The objection that this will make articles longer is real, and tier 2 answers it. The structured statement is **data attached to the article, not words inside it**. It should not count towards the word limit, in the same way a conflict-of-interest statement does not.

The objection about stigma deserves a direct answer. Yes, a separate statement singles out AI today, and in ten years it will look like a transitional measure. That is acceptable. Author-contribution statements were once new too, and they were introduced to solve one specific integrity problem. Design the record so it can later be folded into a general contributorship record (P1, P2), rather than avoiding it now.

---

## 3: How should AI disclosure be structured? (Taxonomy)

### 3A. Is the proposed 18-category taxonomy adequate?

▶ **Mostly adequate.**

### 3B. Views on the taxonomy

The level of detail is broadly right. Splitting quantitative from qualitative data analysis (12 and 13) is correct. So is splitting data visualization from figure or image generation (14 and 15). Both prevent real confusion about what the AI actually did.

**Overlaps to resolve.**

- 8 *Data collection (operations)* against 9 *Data creation*. "Creation" reads as generating synthetic or simulated data, but it can also be read as collection. Rename 9 to *Synthetic or simulated data generation*, and define both.
- 4 *Literature summarization* against 16 *Drafting text*. An AI-written literature review section is both. State the rule: classify by the task, and allow more than one category per use.
- 18 puts editing and rewriting together with reference lists. Reference handling has its own failure mode that anyone can check, namely citations that do not resolve. It deserves to be separate from editing prose.
- Treating 5, 6 and 7 as children of *Design* is good. Make the parent-child relation explicit and machine-readable, or implementers will flatten it in different ways.

**Structural recommendations. This is the part that decides whether "machine-readable" is real.**

1. **Use stable identifiers, slugs rather than numbers** (P1). `vs:literature-search`, not "category 3". Numbers break as soon as a category is added or retired. Publish the list as a versioned machine-readable vocabulary, in JSON or SKOS, with `deprecated` and `replaced_by` fields. CRediT went through ANSI/NISO Z39.104-2022, and that is why CRediT works in metadata today.

   **The same applies to actors, not only to categories** (P7). "We used GPT-4" is not an identifier. A row should name the provider, the model family, the version or snapshot, and the interface. Better still, it should point to a persistent identifier for that system.

   **There is already a precedent, and it is not authorship.** Research Resource Identifiers (RRIDs) give antibodies, cell lines, model organisms, software tools and databases a persistent, machine-readable identifier that never changes and is consistent across publishers. None of those resources is an author. The identifier exists so that a reader or a tool can find every paper that used the same resource, and so that "we used a commercial antibody" becomes a checkable statement.

   An AI model is a research resource of exactly that kind. It has a producer, a version, and behaviour that changes between versions. I propose that the standard call for **persistent identifiers for AI systems, along RRID lines**, and that the disclosure row carry one.

   To be clear about what this is not. I am not proposing that an AI system be treated as an author. COPE has settled that, and I agree with it. Identification is not authorship: a dataset has a DOI and is not an author, and an antibody has an RRID and is not an author. Work that does frame AI systems as authors exists (AICID, Vidal and Monperrus, arXiv 2606.28756), and I am deliberately proposing the weaker and more useful version. The point is that the **tool that acted** should be identified as precisely as the human who is accountable for it.

   Without this, "machine-readable" stops at the category and never reaches the actor, which is the field a reader most often wants to check.

2. **Rows, not sentences** (P2). A category on its own does not carry a disclosure. The smallest useful row is: task (category ID), actor (which AI system, or which human), what was checked and by whom, and trace (what record exists and how to reach it). This is the structure Round 1 asked for: a consistent core, with room for free description.

3. **The taxonomy classifies tasks, and disclosure needs one more axis.** The draft says this itself, calling the list "merely a classification of research tasks". I agree, and that is the point. Without the verification axis in section 5, the taxonomy tells a reader what the AI touched. It does not tell them what anyone did about it.

4. **Three missing categories** (P5). All 18 categories describe a research task the AI performed. Three acts with different integrity properties fall outside them.

   - **Orchestration, or operating an agent.** The human act of configuring, prompting and directing the system, including a supervising agent that picks specialist agents. This is where AI can shape the work substantially while leaving no trace in the output, as in the example in 1B(3). No category that looks at the output can express it. The only artefact is usually the prompt or the protocol, which is exactly why it should be disclosable.

   - **Verification performed by AI.** Checking done by AI: resolving references, judging whether a claim is supported, auditing statistics, reviewing code. This is a different act from producing research material and it has different integrity properties. Categories 10 and 11 smuggle it in as "auditing". It should be recordable as what it is, and carry its own evidence level (P3).

   - **Selection among several runs or outputs.** Which run was reported, out of how many, and under what rule. Undisclosed selection of the best of many runs is invisible in every disclosure scheme I know of, including this draft. It is a question of integrity, not of implementation. A category makes disclosure possible. Making it mandatory for agentic pipelines is a separate policy decision, and I would support it.

---

## 4: Should non-empty AI disclosure be mandatory?

### 4A. Agreement with statements

| Statement | Answer |
|---|---|
| Journals should require authors to include a non-empty disclosure (including a negative disclosure when they have not substantively used AI). | ▶ **Strongly agree** |
| Agreement with a publisher policy on AI disclosure is convincing enough to trust that AI reporting was accurate. | ▶ **Strongly disagree** |

### 4B. View on mandatory non-empty disclosure and null declarations

**I support it, for a reason that is not the usual one.** The culture-change argument is fine but soft. The strong argument is about evidence.

Silence cannot be proved false. A null declaration is a specific, dated statement by a named person. If evidence later shows substantial undisclosed AI use, silence gives you an argument about interpretation, along the lines of "nobody asked". A null declaration gives you a documented false statement, with a name and a date on it.

Mandatory non-empty disclosure does not stop dishonesty. It turns fog into a paper trail. That is a large gain for the cost of one line.

Two conditions. Without them the null declaration becomes exactly the empty sentence the standard is trying to replace.

1. **Tie it to the accepted version** (P4). A declaration made at submission, and never repeated, is a claim about a file that no longer exists. Require it to be re-affirmed at acceptance, attached to the content hash of the accepted manuscript. This closes a problem I would call a **dangling attestation**: a check that outlives the thing it checked. A SHA-256 hash takes a second to compute and anyone can verify it. It is the most under-used mechanism available to this standard.

2. **Do not let a tick-box stand in for it.** Agreeing to a publisher policy at submission is invisible to readers and cannot be checked afterwards. The declaration has to be published with the article.

**On stigma.** The risk is real, but it depends mostly on wording. A null declaration written as the absence of *threshold-meeting* use, placed in the same block as the conflict-of-interest statement, normalises rather than singles out. The bigger stigma risk today is the opposite one. Honest disclosers look worse than people who said nothing.

---

## 5: How to signal responsibility and accountability?

### 5A. Should a general responsibility statement be part of AI disclosure?

▶ **Yes, a default statement should be part of the disclosure standard.**

### 5B. View on general responsibility statements

Include it, but do not let it stand alone, and make it **attributable rather than collective**.

"The authors take full responsibility" is true of every paper ever published. It therefore tells the reader nothing, and the box-ticking objection is correct about that wording. What does tell the reader something is a named person, with a persistent identifier, accepting responsibility for a specific AI use at a specific time. One guarantor per disclosed row where the AI use was substantial, much like the corresponding-author role. It costs the author nothing they do not already know.

So keep the default sentence for the general case, and require **named oversight for each substantial use**. See 5E, last row, which I rate Essential.

**A note about genres this standard does not cover.** A disclosure is also a language act. Its wording can be broken into who sends the text, who chose the words, and who vouches for the content. Those parts combine differently outside the research article.

An email that opens with "Here is an AI summary" tells the reader something no article-style statement says. A slide deck signed with a name alone claims authorship and accountability at the same time. A `Co-Authored-By:` trailer in a commit message, an established convention in git and in AI coding tools, gives an AI system a share of the authorship and none of the accountability. A thesis declaration page does all of this in a form the university prescribed.

A standard written for research articles will not cover emails, teaching materials or internal documents, where the same responsibility is handled by other means: signatures, review conventions, naming rules. I suggest the standard state its genre scope openly, and avoid implying that an article-style statement is the model for all communication.

### 5C. What information about verification and oversight should authors disclose

**Structured, not narrative, but with a slot for narrative.** The example statements in the preparatory reading show the problem. The generic example, "the authors reviewed and edited all AI-generated content", cannot be proved false. The rigorous and descriptive examples are good, but you cannot compare them across articles, screen them at scale, or check them for internal consistency.

A five-slot row per disclosed use takes minutes to fill and can be compared.

| Slot | Content | Why |
|---|---|---|
| 1. Task | Category ID from the taxonomy | So rows can be compared |
| 2. Actor | Which AI system: provider, model family, **version or snapshot**, interface. Or which human. | "We used an LLM" does not describe a tool. A dated version does. |
| 3. What was checked, and by whom | Closed list: *not checked* · *read through by the author* · *sampled, say what fraction* · *fully re-run or recomputed* · *cross-checked against primary sources* · *checked by a named third party* · *independently reproduced* | This is the axis that turns a disclosure into accountability |
| 4. Trace | What record exists (prompt, log, code, output), its identifier and hash, and its access status: *public · embargoed · on request · restricted · not retained*, with a reason whenever it is not public | Prompts and logs often cannot be published, because of personal data, licensed text or third-party material. An unpublishable record can still be referenced by its hash, which makes a later swap detectable. |
| 5. What could not be checked | Short free text, **required** | The most informative field in the record, and the first one that will be dropped if it is optional |

**How concrete is each slot? A working draft.** The five slots say what to record. They do not say how specific a record has to be, and that turns out to be a separate question. I have been sketching a four-level scale that applies to every slot: **0 nothing stated, 1 a general word, 2 a specific fact, 3 a fact someone else can check.**

| Slot | 1 general | 2 specific | 3 checkable |
|---|---|---|---|
| Actor | "AI" | "Claude" | "Claude Opus 5, September 2026" |
| What the AI did | "with AI help" | "the AI wrote the first draft" | "the AI wrote section 2, the conversation is in the appendix" |
| What I did | "I checked it" | "I checked the numbers" | "I checked the numbers against the source, a colleague checked the citations" |
| Accountability | "I take full responsibility" | "I stand behind the facts" | "I stand behind the conclusions; the estimate in section 3 is uncertain" |
| What I expect of the reader | "please check it" | "please check the numbers in table 2" | "check the numbers by Friday, then it goes to the board" |

Three things this makes visible, and they matter for the standard.

**Accountability is a value, not a level.** "I stand behind this" and "I do not stand behind this" are different claims, and either can be said generally or specifically. A record should capture the claim and its specificity as two separate fields, not one.

**The strongest-sounding phrase says the least.** "The authors take full responsibility" is level 1. A specific, limited claim, such as "I stand behind the facts, the wording is the model's", is both more honest and more informative. This is the same point as in 5B, now with a scale attached to it.

**More is not always better.** Prajod et al. (2026) found that a detailed disclosure lowered trust while raising source-checking, and that a one-line disclosure did neither. Level 3 in an ordinary email is probably noise. Which level is appropriate looks like it depends on the genre, and on what the reader is going to do with the text. That is a hypothesis, and it is what my pilot is meant to test.

**What this is not.** The axes came top-down, from reading and reflection, not from data. A corpus coded against them would mostly return what I put into them, so the pilot will code inductively and this draft will be compared with whatever the data produces, not imposed on it. I am including it here because the question "how specific must a record be" is one this standard has to answer, and because it is easier to disagree with a draft than with a gap. Related empirical work: He, Houde and Weisz (2025), *Which Contributions Deserve Credit?*, CHI 2025, arXiv 2502.18357, found that people already grade attribution by the type of contribution, its size, and who took the initiative.

**P6: keep at least one field a machine cannot fill.** The consultation criteria ask for records that are machine-readable and machine-generatable. Both are useful. Together they carry a risk worth naming.

The more structured a record is, the more easily an agent produces it. If an agent can write the whole disclosure, and another agent can check it, then a complete, well-formed, entirely empty record becomes the cheapest thing in the pipeline. It looks finished, it asserts nothing, and it moves the work of discovering that to the reader.

The protection already exists in the design above. It should be stated as a principle rather than left to chance: **every record must contain at least one required field that cannot be completed honestly unless a human did something.** In this proposal there are two. Slot 5 is required free text about what was not checked. And the named guarantor is a person with an identifier who can be asked.

The same logic runs through the list in slot 3. A machine can write "not checked", or "read through by the author", without anyone reading anything. It cannot write "checked by a named third party" or "independently reproduced" without naming someone or producing something. The upper rungs resist automation. The lower ones do not, and that is fine, because the value of the lower rungs is that they are honest.

**The closed list in slot 3 is a ladder, and the Focus Track has already drawn it.** Session 4.B proposed attestation, review, audit, replication. Two different axes are hiding inside it. Perkins's ladder grades **how strong the checking act was**. A second axis grades **what a third party can still verify**. Both are needed, because "I inspected the output", with no surviving record, is just a claim.

| Session 4.B ladder | What it asserts | What a third party can verify |
|---|---|---|
| Attestation, "I take responsibility" | Responsibility | The claim itself, visibly unverified |
| Review, "I inspected the output" | A self-check | Nothing, unless the review left a lasting record |
| Audit, "I checked process and evidence" | A process check | A record, if the author ran it; or a named third party's check, with a stated scope |
| Replication, "I reproduced or cross-checked" | Re-execution | The reproduction |

One consequence is worth putting in the standard in so many words. **Having a log does not by itself make a claim about the work any stronger.** A log can be incomplete, or about something else. A trace shows that something was recorded. Only a named external checker, or a re-run, shows that the claim was examined.

### 5D. Where should verification and oversight information be findable?

▶ Tick: **In a separate statement in the article** · **In a repository, as complementary materials** · **Available on demand for reviewers, readers, journal**

Not "main content only", because that cannot be compared. And not "recorded but inaccessible", because a record nobody can reach is not evidence.

The three tiers from 2B apply: a pointer in the article, the record in a repository, restricted material on request. Publish **the hashes even of material that stays restricted**, so that restricted evidence can still show whether it has been changed.

### 5E. How desirable is each kind of information?

| Item | Rating |
|---|---|
| Which risks were considered and mitigated (hallucination, inaccuracy, bias, privacy, security, copyright, IP) | ▶ **Moderately desirable** |
| What aspects of the work were reviewed, verified, or corrected by humans | ▶ **Essential** |
| How sources, citations, factual claims, data, or outputs were checked against reliable sources or primary data | ▶ **Essential** |
| Any limitations in verification, including aspects of AI outputs that could not be fully checked | ▶ **Essential** |
| Whether records of AI interactions, prompts, logs, or audit trails were retained, and under what conditions they are accessible | ▶ **Essential** |
| Who (which human) was responsible for oversight and verification of each AI use | ▶ **Essential** |

*A note on the first row.* I rate risk narratives lower than the other five on purpose, and this is the only rating where I expect disagreement.

Generic prose about risk is the easiest part of any disclosure to produce and the hardest to check. Within one publication cycle it will settle into boilerplate. The other five items are all statements someone can be confronted with. Keep the risk field, make it optional, and prompt it with the specific risks. Just do not let it become the field authors fill in **instead of** the ones that can be checked.

### 5F. What should the standard advise about making verification transparent?

1. **Advise recording the absence of a check as plainly as its presence.** A standard whose only positive signal is "checked" will be filled in with "checked" everywhere. A graded record works in both directions. It makes a missing check **visible** instead of invisible.

   In practice: an author who declares five substantial AI uses, and says that two of them were never independently checked, has written a more informative and more trustworthy document than one who claims to have reviewed everything.

2. **Advise tying every verification claim to a content hash** (P4). If I had to drop every other recommendation, I would keep this one. A verification claim that names a file state cannot be inherited by a later, different file state. Without it, "verified" is a claim about a title.

3. **Do not certify.** A structured record invites someone to add up a score, such as "provenance quality: 8 out of 10". The standard should say plainly that no field, and no combination of fields, is a judgement about the quality or the truth of the research.

   Certification carries liability that a reporting standard cannot bear. Aggregate scores get optimised rather than met. And venues differ, legitimately, in what they require. Record who did what, and what evidence exists. Stop there.

---

## 6: Summary and other feedback

**Where this response comes from.** It is written from ongoing qualitative work on how people word AI disclosures across genres: research articles, emails and messages, teaching and internal materials, software projects, theses, and social media.

The questions that work asks are: which parts a real disclosure actually carries, and how much of the wording is a publisher template rather than the author's own voice. The parts I am tracking are the role of the AI, the share of the work, what the human did, accountability, certainty, the state of the output, what is expected of the reader, and where the statement sits.

There are no findings yet, and I am not offering any for Round 3. These proposals are submitted to be used or discarded on their own merits, and they need no follow-up from me.

**On process.** The three-round design and the published preparatory reading have made this consultation unusually easy to engage with. One suggestion: publish the Round 2 outcome as a **versioned, machine-readable draft**, a vocabulary file plus example records, and not only as prose. Then implementers can answer in Round 3 with working code instead of comments.

---

## Attribution and contact preferences

- **Optional attribution:** *Jan Nehyba, Assistant Professor, Faculty of Education, Masaryk University (Czechia)*, willing for open-text comments to be attributed.
- **Contact after submission:** ▶ Yes, please keep me updated on the final result (this one only). Not for questions about my answers, and not an invitation to the 3rd Consultation Round.
- **E-mail given for that purpose:** nehyba@ped.muni.cz
- **How I found out about this round:** ▶ Other → *"Following the Focus Track publicly (ISC website); researching how people word AI disclosures across genres."*
- **Relationship with AI systems:** ▶ Professional-heavy AI user
- **Role/career stage:** ▶ Active researcher (with PhD or equivalent) · ▶ Researcher with a permanent contract
