# Work Log (audit trail)

This file records what was done, what was verified and how, what was left out
and why. Written for a later reviewer (human or model) who audits the work.

## 2026-09-16

### What was verified

Repository state, checked with read-only git commands (`git status`,
`git log`, `git branch -avv`, `git tag -l`, `git show --stat`):

- Active branch `vancouver/round2-kit`, working tree clean.
- Commit `de4dffe` (round 2 kit, validator tests, first card fix) exists
  locally and is NOT pushed. The branch is 1 commit ahead of
  `origin/vancouver/round2-kit`.
- No tag exists yet.
- `main` is at `b2eba51` and matches `origin/main`.
- `docs/vancouver/` contains the expected files, including the unfinished
  `kit/` directory, which stays unfinished.

### What was done

- Created `docs/zadani.md`, the project brief for the new topic (framing of
  AI-assisted output across genres). It contains the research topic with
  example framings, the perceived gap (to be verified, not assumed), the eight
  components, the hypothesis, the Goffman grounding, the author's decision
  table, five critical notes, the nine workflow steps, non-goals, and the
  verification criteria.
- Created this work log.
- The author approved: committing both files locally on `vancouver/round2-kit`,
  pushing commit `de4dffe` (plus the new brief commit) to
  `origin/vancouver/round2-kit`, and tagging the last state of `main` as
  `rpc-v0.1` with the tag pushed.
- Stopped after step 1 to wait for the author's confirmation of the brief.

### What was deliberately left out and why

- No repository restructuring (step 3). It happens only after the Vancouver
  input is submitted and after the author's explicit consent. `main` was not
  touched, except for the annotated tag, which changes no file content.
- No Vancouver trimmed submission draft yet (step 2). It starts after the
  author confirms the brief.
- The QualReAI path in the brief is kept as given by the author. It refers to
  a local clone and will be checked when step 7 starts.

### Open items for the author

- Confirm `docs/zadani.md` or request changes.

## 2026-09-16 (later, after independent review)

The author independently verified the repository state and the brief, and
reported three findings. All were applied:

1. **Genre fix (substantive).** The genre row said "emails and reports"; the
   author's decision is Czech "e-maily a zprávy", where "zprávy" means short
   chat messages (Teams, Slack), not reports. Changed to
   "emails and messages". Without this fix, corpus collectors would have
   looked for reports instead of chat communication.
2. **Local path removed.** The tools row carried a local filesystem path to the
   QualReAI clone. Replaced with the repository URL
   `https://github.com/JanNehyba/QualReAI`, as instructed by the author.
   Verification note: on 2026-09-16 this URL returned HTTP 404 both on the
   web page and via the GitHub API when accessed anonymously (a public control
   URL of this repository returned 200, so the check worked). This usually
   means the QualReAI repository is private. The author should check its
   visibility before the link is relied on.
3. **Cosmetic fixes.** The decisions heading said "final" while the document
   header said "draft awaiting author confirmation"; changed to "settled".
   The Goffman paragraph stated the production format as fact; added a
   sentence that the reading is verified in the literature review step,
   including whether a published Czech translation exists.

### Open items for the author

- Confirm `docs/zadani.md` (now with the three fixes above) or request
  further changes.
- Check whether the QualReAI repository is public; if not, either make it
  public or decide how to reference it.

## 2026-09-16 (step 2)

The author confirmed the brief and decided two things: (1) QualReAI stays
private and no code is copied from it. What is taken over is the design
pattern, not a library: three coders on different models plus a synthesis plus
kappa against a human sample. The pattern will be reimplemented from scratch in
this repository, which avoids maintaining two copies and unclear licence
status for copied files. (2) Step 2, the trimmed Vancouver submission, should
start now.

### What was done

- `docs/zadani.md`: status changed to "confirmed by the author on 2026-09-16";
  the tools row and workflow step 7 rewritten to reflect the QualReAI decision
  (no URL, no code copying, the repository stays private).
- Created `docs/vancouver/round2-submission-trimmed-en.md`, derived from
  `round2-submission-en.md`:
  - kept: the four proposals that stand on their own (P1 stable
    machine-readable category identifiers, P2 rows instead of sentences, P3
    closed list of verification levels, P4 binding the declaration to the
    version hash), the threshold support with three refinements, the three 1B
    examples, the three-tier placement answer, the taxonomy overlap fixes, the
    mandatory non-empty disclosure support, the five-slot row, the session 4.B
    ladder, the 5E ratings and the tick-box answers;
  - dropped: the RPC framing ("implementation profile"), the repository URL and
    all implementation claims, the kit, the schema, the validator, the
    crosswalk, the usage-report findings (former proposals P5 to P9), and all
    three appendices;
  - added: a paragraph in 5B stating that a disclosure is a language act
    decomposable into who sends, who chose the words and who vouches, and that
    a standard written for research articles will not cover emails, teaching
    materials or internal documents, where the same responsibility is handled
    by other means;
  - reworked the basis section: the response now stands on the ongoing
    qualitative work on disclosure wording across genres, with no
    implementation or pilot claims.
- Created `docs/vancouver/round2-submission-trimmed-cs.md`, a Czech working
  translation of the trimmed submission for the author's review, using the
  terminology of the existing full Czech translation (deklarace, užití AI,
  práh).
- Updated the file table in `docs/vancouver/README.md`: the full submission is
  now marked as the record of what was prepared first, the trimmed version is
  marked as the one to paste into the webform.

### What was verified and how

- `grep -i -E "RPC|kit|schema|validator|registry|provenance card|zenodo|preprint"`
  over the trimmed English file returns nothing.
- `grep "—"` over both new files returns nothing (no em dash in new text).
- `grep -P "[\x{0400}-\x{04FF}]"` over the Czech file returns nothing (no
  Cyrillic characters accidentally typed).
- Both files have 229 lines and mirror each other section by section.

### Open items for the author

- Review the trimmed submission (the Czech working translation is for this
  purpose), especially the new 5B paragraph and the 3A answer ("Mostly
  adequate", changed from "Mostly adequate, but a few categories are missing"
  after dropping the missing-categories proposal P7).
- Before submitting: open the webform in a browser and check that the questions
  and options still match those of 29 July 2026; fill in the institutional
  e-mail in the respondent table.

## 2026-09-16 — Step 2 audit applied (author's review of the trimmed submission)

### What the audit found

The author confirmed `5f5e119` on GitHub, clean tree, `main` untouched, and
raised three findings (two to fix, one decision) plus two notes without
required action.

### What was changed

- **Finding 1 (fixed, both languages).** 1B example 3 ended with a dangling
  reference to "the manuscript underlying this response" and the count "seven
  design reversals" — a manuscript the trimming had removed, contradicting the
  basis statement ("Nothing below rests on a formal implementation or on pilot
  findings"). The passage now says the example is drawn from the author's own
  practice and that the framing of the work changes in the process. No
  manuscript reference, no count.
- **Finding 2 (returned, both languages).** The three missing taxonomy
  categories from the former P7 — *orchestration / agent operation*,
  *verification performed by AI*, *selection among multiple runs or outputs* —
  are back in 3B as the fifth proposal P5, with no implementation mapping. They
  do not rest on the implementation; the run-selection category in particular
  is an integrity point. Applied consistently: section 0 now says "five
  proposals" and has a P5 row, the "About this version" note says five
  proposals, 1B.3 points to the proposed orchestration category, and the 3A
  answer stays "Mostly adequate", which now reads exactly as intended
  (adequate, with three categories missing). Wording follows the rationales in
  `taxonomy-crosswalk-v0.1.json`, single-author voice, no empirical claims
  beyond what the full version already carried.
- **Finding 3 (fixed, both languages).** The invented "Generated-with:" commit
  trailer in 5B is replaced with the real `Co-Authored-By:` convention
  (established in git and in AI coding tools), described by what it actually
  does: it credits an AI system with a share of the authorship while assigning
  it none of the accountability.
- **Czech typo (fixed).** "artikulové prohlášení" (2x in 5B) replaced with
  "prohlášení psané pro vědecký článek".
- **Majority vote in `docs/zadani.md`.** "Synthesizing agent" / "synthesis"
  replaced in all four places with aggregation by majority vote (two of three;
  items with no majority are flagged for human adjudication, not resolved
  silently; kappa is reported human versus the majority vote and human versus
  each model). NOTE: the author's prepared wording for this change had not
  arrived when this edit was made; the wording was drafted from the author's
  description and awaits the author's confirmation or replacement.
- `docs/vancouver/README.md` file table updated to five proposals (P1-P5).

### What was verified and how

- `grep -i -E "RPC|kit|schema|validator|registry|crosswalk|zenodo|preprint"`
  over the trimmed English file still returns nothing.
- `grep` for "Generated-with", "manuscript underlying" and "seven design
  reversals" in both trimmed files: no hits.
- `grep "artikulové"` in the Czech file: no hits.
- `grep "—"` over both trimmed files: no hits. `grep -P "[\x{0400}-\x{04FF}]"`:
  no hits.
- Both files still mirror each other section by section (234 lines each after
  the additions).
- `grep "synthesizing agent\|versus synthesis" docs/zadani.md`: no hits.

### Notes left without action

- The Round-3 offer in section 6 ("Validated findings from that pilot can be
  offered for Round 3") is left as a conscious commitment by the author.

### Open items for the author

- Confirm or replace the drafted majority-vote wording in `docs/zadani.md`
  with the prepared version.
- Review the Czech translation of the new P5 passage and the reworked 1B.3
  sentence.

## 2026-09-16 — Author's audit of the fixes; Czech wording in P5 corrected

### What the audit confirmed

All three findings fixed and verified independently; commit `695e52c` on
GitHub, `main` still at `b2eba51`, clean tree, both language versions 234
lines, no residue of the removed strings. The author confirmed the drafted
majority-vote wording in `docs/zadani.md` matches the prepared version
(two of three; items with no majority go to human adjudication) — no change
needed. The author endorsed two additions he had not asked for: the
cross-reference from 1B.3 to P5, and "invisible in every disclosure scheme I
know of" instead of an uncited empirical claim about inflated quality.
The submission is final from the author's side.

### What was changed

- Czech wording in the new P5 block, per the author's list: "substancičně" →
  "podstatně"; "specialistické agenty" → "specializované agenty";
  "supervizního agentu" → "supervizního agenta" (genitive);
  "reportován" → "uveden" (2x, table row P5 and the run-selection bullet);
  "samostatné politické rozhodnutí" → "samostatné koncepční rozhodnutí"
  (sounds like party politics otherwise).

### Instruction for pasting into the webform (from the author)

The document has two internal meta passages that are dead links outside the
repository: the "About this version" note (links to the full version) and the
footer "Sources for process facts are listed in README.md". When pasting,
skip both; only the answers to questions 1-6 and the respondent table go
into the form.

### Open items for the author

- Institutional e-mail in the respondent table.
- Open the webform in a browser well before the deadline (structure verified
  as of 29 July 2026 may have shifted); deadline 16 October 2026, target
  10 October 2026.
- Step 4 (verified literature review) can start before submission; it is the
  longest and riskiest part of the project and does not depend on the
  submission.
- Step 3 (repository rebuild) only after submission and the author's
  approval; the author will audit that `archive/rpc-v0.1` holds the entire
  original state and that nothing was lost from `main` except deletions
  recoverable from history.

