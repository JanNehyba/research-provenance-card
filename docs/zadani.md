# Project Brief: How People Frame AI-Assisted Output Across Genres

Status: confirmed by the author on 2026-09-16
Date: 2026-09-16

This brief records the agreed direction of the project. The original Research
Provenance Card (RPC) work is treated as a dead end by the author and will be
archived (see the workflow steps below). Nothing in this brief changes that
assessment; it only redirects the repository toward the new research topic.

## Research topic

How people frame, that is introduce, sign, and label texts and materials
created with AI assistance, and how this differs by genre.

Illustrative framings that motivate the study:

- "Vypracoval jsem text s pomocí AI." / "I prepared this text with the help of AI."
- "Zde je AI souhrn:" / "Here is an AI summary:"
- "Text vypracovala AI, výstup jsem několikrát iteroval a ručím za něj." /
  "The AI wrote this text, I iterated on the output several times, and I stand behind it."
- "AI toto vygenerovala, přečetl jsem to a nechal to tak, ale mám pochybnosti." /
  "The AI generated this, I read it and left it as is, but I have doubts."
- "LLM output:" with no further comment
- A poster that carries only the author's name and affiliation although the text
  was written by AI. The signature then claims both that the author wrote the
  text and that the author stands behind it, while in reality only the second
  claim holds.

## The gap, as currently seen

No one has systematically described which introductory formulations people use
in different genres, what components these formulations consist of, and how
they affect perceived responsibility and trust. This perceived gap must be
verified, not assumed (see the literature review step below).

## Eight components (a starting guide, not a finished typology)

1. **Role of AI:** proofreading, suggestion, entire text, summary, analysis
2. **Share of AI:** a little, most, all
3. **What the human did:** read it, iterated on it, verified against sources,
   had it checked by someone else
4. **Accountability:** I stand behind it, I do not stand behind it, not stated
5. **Certainty:** certain, I have doubts, unverified
6. **State of the output:** finished, work in progress, raw, open to discussion
7. **What is expected from the recipient:** for information only, please verify,
   please decide
8. **Placement:** signature, opening sentence, note, label

**Hypothesis:** the components will be the same across genres, but each genre
will require a different minimum.

## Theoretical grounding

Goffman (1981, *Forms of talk*) distinguishes three roles in an utterance: the
one who delivers or sends it (animator), the one who chose the words (author),
and the one who stands behind the content (principal). The project uses
simplified questions: Who sends this? Who chose the words? Who stands behind it?
This reading is verified in the literature review step, including whether a
published Czech translation of the work exists.

## Decisions made by the author (settled, do not change without instruction)

| Area | Decision |
|---|---|
| Goal | Pilot first, then decide between an article, a handbook, and a grant. |
| Vancouver | Submit a trimmed consultation input without the RPC by 2026-10-16. |
| Genres | All four: research articles, emails and messages, teaching and internal materials, software and public projects. |
| Data languages | Czech and English. |
| Corpus | 200 items, target 25 per cell (4 genres x 2 languages). |
| Data sources | Public data only. Instead of private mail, use publicly archived mailing lists and forums. |
| Ethics | Pilot without an ethics board, because all data is public. A board will be needed only for a possible experiment or interviews. |
| Method | Qualitative coding along the eight components plus room for bottom-up categories. A decision about an experiment or card sorting comes only after the pilot. |
| Who codes | An LLM as coder (three different models), a human validates a control sample. |
| Control sample size | Decided after the first run based on disagreement between models. The selection rule is fixed in advance (see the first run step). |
| Tools | Own script in this repository. The design pattern (three independent coders on different models, a synthesizing agent, kappa against a human sample) is reimplemented from scratch; no code is copied from QualReAI, which stays a private project of the author. Data as files in git. |
| Author time | As little as possible, automate the maximum. |
| Repository | RPC archived in a branch, `main` rewritten for the new project, repository renamed on GitHub. |

## Critical notes that must be respected

1. **Templated versus free formulations.** A large share of statements in
   research articles is copied verbatim from the publisher's template
   (Elsevier, Springer). Such a formulation says something about the publisher,
   not about the author. Every corpus item must therefore carry a `templated`
   flag. This is likely one of the main findings: the genre determines how much
   freedom the formulation has at all.
2. **Weak cells.** The eight cells cannot be filled equally easily. Czech
   research articles with an AI statement are rare, Czech public discussion
   forums with this content are rare too, and Czech software projects with an
   AI policy are almost nonexistent. On the other hand, Czech theses
   (theses.cz, IS MUNI) contain AI use statements and are public, which is the
   richest Czech source. The target is 25 per cell, the minimum is 10, and an
   empty or thin cell must be reported, not hidden.
3. **The control sample cannot be skipped.** The author decides its size only
   after the first run, but the selection rule is fixed in advance, otherwise
   it would be post hoc data selection.
4. **Hard gate.** No public text may claim differences between genres before a
   manually coded sample exists and agreement between LLM and human has been
   computed. Without that it is not a result, it is a model output.
5. **LLM as judge has known weaknesses:** sensitivity to prompt wording, a
   tendency to agree with its own earlier output, position bias. Three
   different models dampen these, they do not remove them.

## Workflow

1. Brief and rescue of in-progress work (this document).
2. Vancouver: trimmed consultation input, deadline 2026-10-16, target ready by
   2026-10-10. The author submits it personally through the web form.
3. Repository restructuring (only after the input is submitted and after the
   author's consent): archive branch `archive/rpc-v0.1`, rewrite `main`, new
   README, CHANGELOG entry, workflows fixed. The GitHub rename is done by the
   author manually, suggested name: `ai-disclosure-framing`.
4. Verified literature review, `docs/reserse.md`. Every source carries a
   verification status column. Mandatory gap check: if someone has already
   built a corpus or typology of AI statement wording across genres, stop and
   tell the author.
5. Corpus collection, `data/corpus/`, format `corpus.jsonl`, collectors in
   `src/collect/`, coverage report in `data/corpus/coverage.md`.
6. Code book, `docs/kodovaci-kniha.md`. Eight components with closed value
   lists including a "not stated" value, examples, and boundary decisions. Free
   field `novel_note` for bottom-up categories. Versioned; a change means the
   whole run is repeated.
7. Machine coding, `src/code/`. Three independent coders on different models
   plus a synthesizing agent. The pattern is reimplemented from scratch, no
   code is copied from the author's private project QualReAI. Output in
   `data/coded/run-<date>-<book version>/`.
8. First run and the control sample decision. Fleiss kappa per component
   between the three models, a stratified random part plus a targeted part
   from disagreement items, blind human coding, Cohen kappa human versus
   synthesis and human versus each model.
9. Pilot evaluation, `docs/pilot-report.md`, ending with a recommendation:
   extend the corpus, card sorting with participants, or an experiment.

## Non-goals

- Do not finish the Vancouver kit (`docs/vancouver/kit/`). It is stored and
  stays unfinished.
- Do not delete the RPC card or anything from the RPC irreversibly.
- Do not rename the repository on GitHub, the author does that manually.
- Do not send anything to third parties. The author submits the consultation
  input personally.
- Do not decide the main output of the project. That is decided after step 9.
- Do not push or modify `main` without explicit author consent.

## How this work is verified

1. This brief exists and the author has confirmed it. Without that, `main` is
   not touched.
2. `git status` is clean, commit `de4dffe` is on the remote, and the tag
   `rpc-v0.1` exists.
3. The trimmed consultation input does not contain the word RPC or any kit
   reference (checked with `grep`), and it fits the form fields.
4. After the rewrite of `main`, `git show archive/rpc-v0.1:spec/rpc-spec-v0.1.md`
   still works. No workflow in `.github/` fails on missing files.
5. In `docs/reserse.md` no line remains with an unfilled verification status.
6. A check script verifies that every corpus item has all mandatory fields,
   that `source_url` leads to a public address, and that `text_verbatim` and
   `context_note` contain no email address. Plus a manual spot check of ten
   items against the source.
7. A coding run on twenty items must pass before the full 200. The output is
   valid JSON per the code book schema and the three models really ran
   separately.
8. Cohen kappa human versus synthesis is computed and reported for each of the
   eight components separately, including components where it turns out bad.
