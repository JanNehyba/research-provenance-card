# Vancouver Standard — Consultation Round 2 submission

Working folder for the project's input to the **Global Reporting Standard for AI Disclosure in Research** (informally the *Vancouver Standard*), the Focus Track of the World Conference on Research Integrity 2026.

## Files

| File | What it is |
|---|---|
| [`round2-submission-en.md`](./round2-submission-en.md) | **Full submission.** Paste-ready, question by question (1A–6), with recommended tick-box answers marked ▶ and three appendices. References the RPC implementation throughout; kept as the record of what was prepared first. |
| [`round2-submission-trimmed-en.md`](./round2-submission-trimmed-en.md) | **Trimmed submission for sending.** Keeps only the four proposals that stand on their own (P1, P2, P3, P4), drops the RPC framing and all appendices, and adds a genre perspective to question 5. This is the version to paste into the webform. |
| [`round2-submission-trimmed-cs.md`](./round2-submission-trimmed-cs.md) | Czech working translation of the trimmed submission, for the author's review. Not for submission, the consultation runs in English. |
| [`round2-submission-cs.md`](./round2-submission-cs.md) | Czech working translation, for the author's review. Not for submission — the consultation runs in English. |
| [`taxonomy-crosswalk-v0.1.json`](./taxonomy-crosswalk-v0.1.json) | Machine-readable crosswalk: the proposed 18 categories ↔ RPC roles, with gaps flagged in both directions and three proposed additions. Supporting material for question 3B. |

## Verified process facts

All facts below were checked against primary sources on **29 July 2026** (not taken from model memory).

| Item | Value | Source |
|---|---|---|
| Initiative | Global Reporting Standard for AI Disclosure in Research, "Vancouver Standard" | [ISC](https://council.science/our-work/ai-disclosure-in-research/) |
| Partners | ISC, WCRIF, COPE, STM, GYA | [STM](https://stm-assoc.org/global-reporting-standard-for-ai-disclosure-in-research-first-consultation-is-open/) |
| Round 1 | Dec 2025 – 28 Feb 2026; needs and preferred structured format | [ISC](https://council.science/our-work/ai-disclosure-in-research/) |
| WCRI 2026 Focus Track | Vancouver, 3–6 May 2026; sessions 2.B (thresholds) and 4.B (accountability) | [wcri2026.org](https://wcri2026.org/focus-track/), [slides 4.B](https://council.science/wp-content/uploads/2026/07/WCRI2026_FocusTrack_4B.pdf) |
| **Round 2 (current)** | July – **16 October 2026**; thresholds, placement, taxonomy, mandatory non-empty disclosure, responsibility/accountability | [ISC](https://council.science/our-work/ai-disclosure-in-research/) |
| Round 2 preparatory reading | v4.5, published 8 July 2026, 9 pages — contains the proposed threshold and the 18-category taxonomy | [PDF](https://council.science/wp-content/uploads/2026/07/WCRI2026FT_PrepReadingRound2_v45.pdf) |
| Round 3 | End 2026 – early 2027; feedback on a draft. Standard published ~Dec 2026 per the 4.B timeline slide | [ISC](https://council.science/our-work/ai-disclosure-in-research/) |
| Where to submit | Webform at <https://council.science/AIdisclosure> (survey embedded on the page; "Consultation round 2") | ISC |
| Contacts | Bert Seghers, process lead (office@enrio.eu); Hylke Koers, STM (hylke@stm-solutions.org); Mike Perkins, survey ethics (mike.p@buv.edu.vn) | ISC, STM |
| Round 2 core team | Kari D. Weaver, Kiera McNeice, Mike Perkins, Natalya Tsibulyak, Sergio Santamarina, Lorelei Lingard, Bert Seghers | Round 2 preparatory reading |

Two things to know before reading the submission:

- **Date discrepancy.** The [wcri2026.org focus-track page](https://wcri2026.org/focus-track/) still lists Round 2 as April–August 2026. The ISC page and the round-2 preparatory reading (both newer) say July–October 2026 with a **16 October 2026** deadline. The ISC page governs.
- **Format.** The survey is a webform with open-text boxes and tick-boxes; there is no file upload. The submission document is therefore written to be pasted answer by answer, with the repository URL doing the work an attachment would do.

## Round 2 asks five questions

1. **Thresholds** — which AI use should be disclosed? (proposed: a qualitative threshold, "substantively shapes or replaces human judgement", explicitly no quantitative criteria)
2. **Placement** — integrated in the article, a separate statement, or both?
3. **Taxonomy** — how should disclosure be structured? (proposed: 18 controlled research-task categories)
4. **Mandatory non-empty disclosure** — including "null" declarations?
5. **Responsibility and accountability** — a general responsibility statement, and how to document verification and oversight

## Before submitting — checklist

The submission cites this project as an implementation. Three of its claims about our own state must be true on the day it is sent:

- [ ] **Fix the first card.** `registry/2026/rpc-2026-0001.json` currently asserts `artifact_linked` for `log1`, an artefact with no hash and `access_status: on_request` that we cannot release. Either deposit a curated log with the two-hash record from Appendix B, or drop the affected activities to `declared` and remove the artefact. The submission's §6 finding is honest either way, but "we corrected it" must not be written before it is corrected.
- [ ] **Publish the adversarial protocol** as `protocol/adversarial-review-prompt.md`, and land the Method section with the table of seven documented design reversals in both language versions of the manuscript. The submission's 1B example 3 ("seven design reversals are traceable to it") and proposed category A both rest on them; the protocol is also the only artefact for `rpc:prompt_orchestration`.
- [ ] **Run `refcheck.py` over the manuscript's own bibliography** and record the result as a `check`. Question 5C claims the resolution/support distinction is implemented, not just specified.
- [ ] Fill in the institutional e-mail in the respondent table.
- [ ] Decide: individual response (as written) or a group response after discussion with colleagues at the faculty. The consultation explicitly prefers collective reflections — a departmental discussion would strengthen it and change the "capacity" answer.
- [ ] Decide on attribution: the submission currently opts **in** to attributed quotation of open-text answers.
- [ ] Optional: mint a Zenodo DOI for a `v0.1.x` release so the submission cites an archived version rather than a moving branch.

## Licence

Specification and documents CC BY 4.0; code MIT. Reuse of this submission by the core team, including verbatim, is welcome.
