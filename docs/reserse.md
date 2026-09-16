# Literature Review (verified)

Status: first pass, 2026-09-16
Scope: the sources listed in the project brief, plus what a gap check turned up.

Every row carries a verification status. Nothing here is reported from model memory.

- **Full text read** means the paper itself was retrieved and the specific claim located in it.
- **Abstract verified** means the publisher or arXiv record was retrieved and the claim matches the abstract.
- **Listing only** means the record was seen in a search index but the abstract page was not retrieved directly.
- **Not identified** means no source matching the description was found. That is not a claim that none exists.

---

## 1. The gap, rewritten

The brief said: *"No one has systematically described which introductory formulations people use in different genres, what components these formulations consist of, and how they affect perceived responsibility and trust."*

**That statement is false as written and must be replaced.** For research articles someone has done it (3.1). For government documents someone has done it (3.2). A faceted component model already exists (3.3).

Proposed replacement:

> Normative schemes for what an AI disclosure should contain are proliferating: AID, DAISY, the STM classification, the faceted attribution model, the Vancouver Standard itself. Descriptive work on what people actually write is far thinner, and every existing study sits inside a single genre: medical education journals, Australian government documents, digital humanities. No study compares the wording across genres, and none asks whether the components of a disclosure behave differently in an email than in an article. Three components that existing component models omit entirely are accountability (who vouches for the content), the state of the output (finished, draft, raw), and what is expected of the recipient. These become visible only when a disclosure is treated as a language act addressed to someone, rather than as a record of a process.

**What this changes for the project.** The contribution is no longer "a typology of components". Component models exist. The contribution is (a) the cross-genre comparison, (b) the three components nobody has modelled, and (c) an empirical test of a claim currently asserted for one field only, that disclosure is performative rather than informative. The `templated` flag stops being housekeeping and becomes the main independent variable.

---

## 2. Status table

| # | Source | Status | Note |
|---|---|---|---|
| 1 | Schilke & Reimann 2025, transparency dilemma | **Full text read** | Every claim in the brief confirmed, including the job applicant letter |
| 2 | Goffman 1981, *Forms of Talk* | **Partly verified** | No Czech translation found; see 4.2 |
| 3 | van Nuenen et al., *The Fabricated Front*, arXiv 2608.18369 | **Listing only** | ID correct, five mechanisms match the brief |
| 4 | Vancouver Standard, round 2 | **Verified** | Deadline 16 October 2026 reconfirmed 2026-09-16 |
| 5a | DAISY, arXiv 2604.02760 | **Abstract verified** | ID in the brief is correct |
| 5b | AID Framework, arXiv 2408.01904 | **Abstract verified, one claim open** | Author is Kari D. Weaver; "14 categories" not confirmed, see 4.3 |
| 5c | STM classification recommendations | **Verified** | September 2025, stm-assoc.org |
| 6 | El Ali et al. 2024, disclosure obligations | **Abstract verified** | arXiv 2403.06823, CHI EA '24 |
| 7a | News label experiment, n = 415 | **Not identified** | See 4.4 |
| 7b | Purcell et al. 2025, writing with AI | **Abstract verified** | iScience, N = 1,637 confirmed |
| 7c | Khadpe et al., arXiv 2509.09645 | **Abstract verified** | N = 399, not 415; see 4.5 |
| 8 | Niederhoffer et al. 2025, workslop | **Verified** | HBR, September 2025 |
| 9 | AI disclosure in medical education journals | **New, abstract verified** | Closest existing work; see 3.1 |
| 10 | Australian government AI transparency statements | **New, abstract verified** | See 3.2 |
| 11 | Xexéo, faceted attribution proposal | **New, abstract verified** | See 3.3 |

---

## 3. Work not in the brief that changes the gap

### 3.1 Disclosure statements in medical education journals

*The Presence and Nature of AI-Use Disclosure Statements in Medical Education Journals: A Bibliometric Study.* Perspectives on Medical Education, PubMed 41800434. Preprint: medRxiv 10.1101/2025.11.11.25340015.

24 medical education journals, articles from January to July 2025 (n = 2,762), of which 2,046 empirical articles were screened for AI disclosures. 51 disclosures (2.5%) were content-analysed. Reported pattern: authors name the tool and affirm their own responsibility, but describe the use superficially. The authors call this "safe" disclosure and conclude it is more performative than informative.

**Why it matters here.** This is the study that makes the original gap statement false. It is also the best available methodological precedent, and its central finding is a hypothesis this project can test across genres rather than assert. Note the limits it leaves open: one field, one genre, English only, and no analysis of how much of the wording is publisher template.

*Status: abstract and summary figures verified from the journal record. Full text not read. Re-check the numbers before citing them.*

### 3.2 Government AI transparency statements (Australia)

Pan, Gong, Xia, Sun, Xu & Zhu, *The Creation and Analysis of Government AI Transparency Statements in Australia*, arXiv 2604.26075 (submitted 28 April 2026, revised 8 July 2026). Dataset "AITS-101" of 101 government documents, analysed stylometrically, quantitatively and qualitatively for disclosure coverage and structure.

**Why it matters here.** Precedent for analysing disclosure wording in a genre other than the research article. Whether they built an explicit coding scheme is not stated in the abstract and needs checking in the full text.

### 3.3 A faceted model of attribution

Geraldo Xexéo, *A Faceted Proposal for Transparent Attribution of AI-Assisted Text Production*, arXiv 2604.25346 (28 April 2026). Core model: Form, Generation, Evaluation. Extended model adds Intent, Control, Traceability. Applies at document, chapter, section and paragraph level.

**Why it matters here.** This is the nearest competitor to the eight-component scheme. It is a **proposal, not an empirical study**: no corpus, and the only worked example is the article itself.

Overlap with the eight components: Generation covers roughly components 1 and 2 (role and share of AI), Evaluation covers 3 and 5 (what the human did, certainty), Traceability covers evidence. **Not covered: accountability, state of the output, expectations of the recipient.** Those three follow from treating a disclosure as an utterance with an addressee, which is the Goffman angle, and they are where this project is not duplicating anyone.

---

## 4. Per-source verification notes

### 4.1 Schilke & Reimann 2025 (full text read)

*The transparency dilemma: How AI disclosure erodes trust.* Organizational Behavior and Human Decision Processes 188 (2025), 104405.

Confirmed from the full text:

- Thirteen studies. Actors who disclose AI use are trusted less than those who do not.
- **Study 9 tested six disclosure framings**, exactly as the brief described: (a) general terms, (b) a human reviewed and revised the work, (c) AI was used only for proofreading, (d) the human's intent behind the AI usage, (e) AI-generated content may contain errors, (f) the human's transparency about their AI usage. All six were trusted less than the no-disclosure control, all *p* < 0.02; F(6, 511) = 15.79, *p* < 0.001, eta-squared = 0.16.
- **Study 9's stimulus was a letter from a job applicant**, not an email. The brief was right. Study 10, a different study, used an email.
- **Third-party exposure of undisclosed AI use damages trust more than voluntary self-disclosure.** Confirmed in the abstract and in the discussion.

Implication for this project: six different wordings, all failing equally, is a strong result and a warning. If wording made no difference in Schilke's evaluative settings, the project has to explain why it would matter elsewhere. The honest answer is that Schilke tested *whether trust drops*, not *what the wording communicates about responsibility*, and that all six of his framings kept the human as guarantor. None of them said "I do not stand behind this."

### 4.2 Goffman 1981 and the Czech translation

The three roles (animator, author, principal) come from *Forms of Talk* (1981), in the essay on footing.

**No Czech translation of *Forms of Talk* was found.** What exists in Czech is *The Presentation of Self in Everyday Life* (1959), published as *Všichni hrajeme divadlo: Sebeprezentace v každodenním životě*, translated by Milada McGrathová, Nakladatelství Studia Ypsilon, Prague 1999.

**Consequence:** any Czech rendering of animator / author / principal is the project's own translation and must be marked as such every time it is used. Before stating in print that no Czech translation exists, check the national library catalogue. A web search is not a catalogue.

### 4.3 AID Framework: the author matters

*The Artificial Intelligence Disclosure (AID) Framework: An Introduction*, **Kari D. Weaver**, arXiv 2408.01904 (August 2024, revised April 2025), published in College & Research Libraries News. A statement builder exists at aidframework.org.

**The "14 categories" claim is not confirmed.** The abstract does not enumerate the categories. A plausible explanation, to be checked in the full text, is that AID is built on CRediT, which has exactly 14 contributor roles; the categories named in secondary sources (conceptualization, data analysis, visualization, writing review and editing, project administration, translation) are largely CRediT roles plus additions. **Do not cite "14 categories" until the full text confirms it.**

**Separate point, worth knowing.** Kari D. Weaver is listed on the Vancouver Standard round 2 core team (see `docs/vancouver/README.md`). The author of the framework this project cites is one of the people writing the standard, and one of the people who will read the round 2 submission.

### 4.4 The news label experiment (n = 415): not identified

The brief describes an experiment with news labels ("influenced by / with the help of / generated by AI") with n = 415. **No source matching that description was confirmed.**

Two candidates were found and neither matches:

- Toff, B., & Simon, F. M. (2025). *"Or They Could Just Not Use It?": The Dilemma of AI Disclosure for Audience Trust in News.* The International Journal of Press/Politics. DOI 10.1177/19401612241308697. Tests AI-generated labelling and source disclosure in a US survey experiment, not a three-level label contrast; the sample size was not confirmed as 415.
- Li, F., Yang, Y., & Yu, G. (2025). *Nudging Perceived Credibility: The Impact of AIGC Labeling on User Distinction of AI-Generated Content.* Sage.

**Action:** the author should supply the original reference, or the source is dropped. Do not substitute a similar-looking paper for it.

### 4.5 Khadpe et al.: correct paper, different sample size

arXiv 2509.09645 is *Explaining the Reputational Risks of AI-Mediated Communication: Messages labeled as AI-assisted are viewed as less diagnostic of the sender's moral character*, by Pranav Khadpe, Kimi Wenzel, George Loewenstein and Geoff Kaufman (September 2025, revised March 2026). **Two studies, 399 participants.**

The finding is more precise than the brief suggests, and more useful. AI labels do not simply make senders look worse. They **dampen the diagnosticity of the message**: an AI-assisted apology makes the sender seem less warm, and an AI-assisted accusation makes the sender seem less cold. The label weakens the signal in both directions.

**Why this is central to the project.** This is the strongest existing evidence that a disclosure changes what a text says about its sender, not just how much it is believed. That is the "who vouches for this" component, measured. It is also the paper closest to the project's theoretical core.

### 4.6 A contradiction in the literature worth building on

Two well-powered studies disagree:

- Schilke & Reimann (2025), thirteen studies: disclosure erodes trust, across six framings, robustly.
- Purcell, Jakesch, Dong, Nussberger & Köbis (2025), *Writing with AI boosts trust-building efficiency*, iScience, PubMed 41492389: two preregistered experiments, N = 1,637, incentivised trust games with communication. **AI assistance had minimal impact on trust regardless of disclosure**, and the efficiency advantage persisted when AI use was disclosed. Linguistic analysis: AI-assisted messages were slightly less authentic but warmer, more complex and higher in clout.

These are not easily reconciled. One candidate moderator is the setting: Schilke's stimuli are evaluative (a job applicant, a supervisor, an analyst, that is, contexts where the reader is judging the sender), while Purcell's are transactional (a trust game where the reader is deciding whether to cooperate). **Genre and communicative situation are a plausible explanation for the disagreement, and that is this project's territory.** Worth stating as a motivation rather than leaving the two studies side by side.

### 4.7 Remaining sources, verified

- **The Fabricated Front**, arXiv 2608.18369, van Nuenen, Sachdeva & Chopra, accepted in the Paris Journal of AI and Digital Ethics. Goffman's dramaturgical framework applied to workplace GenAI use. Five opacity mechanisms, matching the brief: voice, provenance, vulnerability, attention, investment. Based on 1,250 interview transcripts from Anthropic's AI Interviewer dataset. *Listing only: the arXiv abstract page was not retrieved directly. Verify before citing.*
- **El Ali et al. (2024)**, *Transparent AI Disclosure Obligations: Who, What, When, Where, Why, How*, CHI EA '24, DOI 10.1145/3613905.3650750, arXiv 2403.06823. Uses the 5W1H frame to generate research questions about disclosure obligations under the EU AI Act, Article 52. *Author list needs checking against the ACM record; one search result rendered it inconsistently.*
- **STM (2025)**, *Recommendations for a Classification of AI Use in Academic Manuscript Preparation*, published September 2025, stm-assoc.org.
- **Niederhoffer et al. (2025)**, *AI-Generated "Workslop" Is Destroying Productivity*, Harvard Business Review, September 2025. Workslop is defined as AI-generated content that looks polished but shifts the work downstream, requiring the recipient to interpret, correct or redo it. Reported: 40 per cent of survey respondents received workslop, spending an average of 1 hour 56 minutes per instance. A follow-up appeared in HBR in January 2026.

---

## 5. What is still open

1. **Read three full texts, not abstracts:** the medical education study (its coding scheme is the direct methodological precedent), the Australian government study (does it have a coding scheme?), and the AID Framework (how many categories, and are they CRediT?).
2. **Get the n = 415 reference from the author**, or drop it.
3. **Check the national library catalogue** for a Czech *Forms of Talk* before asserting there is none.
4. **Check the ACM record** for the El Ali author list.
5. **Search two areas not yet covered:** disclosure wording in teaching materials and university policy documents, and disclosure conventions in software projects (commit trailers, AI policy files). The gap check covered research articles, news, government and workplace communication. Those two genres were not searched.
6. **Reconcile Schilke and Purcell** in the eventual article rather than citing both as if they agreed.
