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
