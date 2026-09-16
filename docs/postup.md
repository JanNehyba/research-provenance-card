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

