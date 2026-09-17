# Work log: corpus and collectors

Branch: `corpus/collectors`
Owns: `src/collect/**`, `data/corpus/**`, this file.
Touches nothing else. `docs/zadani.md` belongs to the author.

## 2026-09-16 - seed run, 40 items, four defects found

Two collectors written and run. 40 items: 21 from open access articles
(Europe PMC), 19 from public repositories (GitHub). English only.

The run worked end to end, which was the point of doing 40 before 300. It also
exposed four defects. **The 40 items are a pipeline test, not corpus data.**
Fix these, then rebuild the file from scratch rather than patching it.

1. **Extraction starts mid-sentence.** 14 of 40 items begin lower-case, because
   `common.window_around` only looks back 40 characters for a sentence
   boundary. An item that starts mid-sentence is not a verbatim formulation.
2. **Extraction overruns the end.** Several items carry trailing matter from the
   next section, for example "Footnotes Handling editor: Professor ...". The
   forward cut needs to stop at the end of the disclosure, not at a character
   count.
3. **Squash commits repeat the same trigger.** 3 GitHub items contain the same
   trailer eight times over, because a squashed merge lists every sub-commit.
   Take the first occurrence only, or split the message.
4. **The template flag is too narrow.** Only 5 of 40 were flagged. It catches
   the Elsevier wording and misses Frontiers, which uses "The author(s) declared
   that no generative AI was used in the creation of this manuscript". Since
   `templated` is the study's main explanatory variable, a false negative here
   is worse than anywhere else in the pipeline. Add markers for Frontiers,
   Springer, Wiley and Nature, and record which publisher family matched.

Also observed: `placement` was empty for 4 of 21 article items, because the
nearest preceding `<title>` was not found; and GitHub's commit search hits a
secondary rate limit after roughly two queries, so it needs a longer pause than
the 2 seconds currently used.

### Open for the author

- Nothing. This stream can proceed without a decision.

## 2026-09-16 - defects fixed, corpus rebuilt from scratch, 38 items

All four seed defects fixed, plus smaller ones the rebuild itself exposed.
The corpus was deleted and re-collected, not patched. 38 items: 20 articles
(Europe PMC), 18 repository items (GitHub), all English. Acceptance checks
pass: no item starts lower-case, no item repeats its trigger phrase, no item
contains an email address (`src/collect/check.py`, kept as a reusable check).

Fixes, one commit each:

- `window_around` now finds the real sentence start (walking back up to 600
  characters for a boundary, refusing the item if none is findable) instead of
  assuming one within 40 characters, and the forward cut stops before the next
  section heading (`SECTION_BREAKS`) and at the first occurrence of a repeated
  trigger, so a squashed merge cannot fill an item with eight copies of the
  same trailer. Items are also refused when the same trigger phrase occurs
  twice inside them.
- `TEMPLATE_MARKERS` became `TEMPLATE_FAMILIES` grouped by publisher family
  (`frontiers`, `springer_nature`, `wiley`, `elsevier`), and the item now
  carries `template_family` plus `trigger_phrase` as fields. Springer and
  Nature share one family: they are one publisher group handing authors the
  same statement. Current split: 3 springer_nature, 3 elsevier, 1 frontiers,
  31 free wording. The Elsevier and Springer Nature wordings overlap heavily,
  so the family attribution should be spot-checked against the journal name
  during the 20-item review.
- `placement` falls back to the nearest known section name when the XML has no
  preceding `<title>`; no article item has an empty placement now.
- GitHub searches wait 30 seconds between queries and retry once after a
  minute when the secondary rate limit answers; the Europe PMC search got the
  same treatment after a refused search silently returned zero candidates.
- Repository prose is extracted line by line: a markdown line is the source's
  semantic unit, and earlier lines are credits or navigation that regularly
  name individuals. Two seed items carried such names; that way in was closed.
- Article windows are bounded by the disclosure's paragraph: `strip_tags`
  keeps paragraph breaks, and the window stops at the end of the trigger's
  paragraph. A CRediT authorship list with full author names had run into one
  seed item through a missing section marker.
- HTML entities are unescaped in extracted text (`&#x2028;` line separators
  had leaked in as literal text), and `gh` output is decoded as UTF-8 rather
  than with the Windows locale codec, which crashed the reader thread.

Verification: the acceptance checks over the whole file, plus nine items
checked against the live sources (four article full texts, two commit
messages through the API, three repository files re-extracted from raw) - all
are verbatim runs of their source or reproduce exactly.

### Open for the author

- 20 random items from the rebuild are shown below for review before any
  further collection or scaling to 300.
- Conventional-commit subjects (`docs:`, `fix:`) are refused by the lower-case
  guard. The guard implements the acceptance rule as written; whether
  subjects like these should be allowed in is a wording decision for the
  author.
- Two items quote author initials or names inside the disclosure itself
  ("KIF and JY used Chat GPT to improve writing"); one carries a correction
  notice rather than a primary statement. They are verbatim and were kept, but
  the author may want them dropped as noise.
- One free-form item is a study finding about ChatGPT use by students, not an
  author's own disclosure; the trigger phrase found it legitimately. Whether
  that belongs in the corpus is an editorial call.
- GitHub commit items may keep the squash subject line above the trigger
  bullet (verbatim message content, no personal data).
