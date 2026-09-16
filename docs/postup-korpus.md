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
