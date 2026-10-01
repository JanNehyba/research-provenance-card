# Protocol: a scoping review of category schemes for disclosing AI use in produced texts

Frozen 2026-09-27. Registered nowhere; the evidence that these criteria were set
in advance is the order of commits in this repository, and the sha256 recorded
in `data/lit/protocol-frozen.json`.

Amendments are **appended** to the deviations log at the end of this file, with
a date and a reason. Nothing above that log is rewritten after the first search
has run.

---

## 1. Why this review

Two literatures exist on AI disclosure. The literature on its **effects** is
large and mature: a systematic review of 47 studies in journalism, a
meta-analysis over 67 effect sizes and 25,208 participants, and dozens of
experiments. That literature is mapped in `docs/reserse.md` and is **not** the
subject of this review.

The literature on **how disclosure is described** is thin and scattered. Every
descriptive study found so far sits inside one genre: medical education
journals, Australian government documents, digital humanities. One faceted
component model exists as a proposal without a corpus. Standards bodies and
publishers have produced category lists in parallel, largely without citing
each other.

Nobody has assembled the category schemes themselves and compared their
dimensions across domains. That inventory is a prerequisite for two things: a
defensible code book for the parent study, and any claim that a particular
dimension is unmodelled.

## 2. Research questions

- **RQ1** Which category schemes for describing AI use in a produced text
  exist, and in which domains?
- **RQ2** Which dimensions do they use, and which dimensions recur across
  domains?
- **RQ3** What do adjacent disclosure traditions model that the AI schemes do
  not? Adjacent traditions are: conflict of interest, funding, sponsored
  content and native advertising, contributorship, data and software citation.
- **RQ4** At what granularity does each scheme apply, on whose authority, and
  does a machine-readable artefact exist?
- **RQ5** Does any scheme model **accountability** (who vouches for the
  content), the **state of the output** (finished, draft, raw), or **what is
  expected of the recipient**?

RQ5 is a falsification test of a claim made by the parent project. If these
three are modelled somewhere, the finding is recorded and the project's claim
is rewritten. The claim is not defended against the finding.

## 3. Eligibility criteria

### Include

A record is included if all of the following hold.

1. It presents a nameable set of categories, dimensions, facets, levels or
   fields for describing disclosure, attribution or provenance **of a produced
   output**, whether proposed, imposed or observed.
2. Any domain, any venue.
3. Publication window: 2018 to 2026 for AI-specific records. **No lower bound**
   for adjacent traditions, because their dimension vocabularies are older than
   the AI debate and that is precisely why they are included.
4. Language: English or Czech.
5. Type: empirical study, normative proposal, editorial or institutional
   policy, reporting guideline, or technical standard.

### Exclude

1. **Effects only.** Measures how readers react to disclosure without offering
   its own category scheme. That literature is already reviewed elsewhere in
   this project.
2. **Detection.** Distinguishing AI text from human text.
3. **Watermarking and fingerprinting** without labelling semantics. A technique
   for hiding a signal in text is out; a specification of what the signal
   asserts is in.
4. **System documentation.** Model cards, datasheets for datasets and system
   cards describe an AI system, not the disclosure of its use in a particular
   output. Excluded, and recorded as a named excluded family so the boundary is
   visible rather than silent. A record crosses back in if it specifies how use
   is declared in a produced output.
5. **Pure legal exegesis** with no categories of its own.
6. **No retrievable text**, for example a conference abstract with no paper.
7. Editorials that assert a rule without any structure, for example "authors
   must disclose AI use", with nothing to extract.

### Boundary rules, decided in advance

- **A scheme with one dimension counts.** A three-level scale of AI involvement
  is a scheme. Granularity is recorded, not used to exclude.
- **A checklist counts** if its items are dimensions of a disclosure, not steps
  in a workflow.
- **Author instructions count** when they enumerate. "Disclose in the methods
  section which tool was used and for what" enumerates two dimensions.
- **The same scheme in several papers** is one scheme with several source
  references, decided at extraction, not at screening.
- **Journalism cue taxonomies count** when the cue types are enumerated,
  because a byline, a label and a disclosure paragraph are placements, and
  placement is a dimension.

## 4. Information sources

Availability was probed on 2026-09-27 from the machine that will run the
searches. The probe result is recorded because it constrains the search and a
later reader cannot reconstruct it.

| Source | Use | Probe result 2026-09-27 |
|---|---|---|
| OpenAlex | search, record by DOI, forward citations | works, but only when the client is not routed through the sandbox proxy, which returns 429 |
| Crossref | search, references of a DOI | works |
| Europe PMC | search, open access full text XML, citations | works |
| arXiv API | search, abstracts | works through `requests`, returns 406 through `urllib` regardless of headers |
| DOAJ | search of open access journals | works |
| OpenAIRE | search, the route to arXiv and to theses | works |
| DataCite | DOIs not registered with Crossref | works |
| Unpaywall | open access location of a DOI | works |
| OpenCitations | forward citations | works |
| Semantic Scholar | not used | 429 without an API key; no key requested |

**Grey literature is not searched systematically.** Publisher author
instructions, citation style manuals and university policies are in scope by
type but there is no reproducible way to enumerate them. They enter only when a
searched record points at them, and the report marks them as incidental
findings, never as a surveyed domain. This is a stated limitation, not an
oversight.

## 5. Search strategy

The queries are in `data/lit/queries.json`, verbatim, one entry per source with
the date it ran. That file is hashed together with this protocol.

Three blocks:

- **Block 1, AI disclosure schemes.** Concept A, artificial intelligence and its
  synonyms; concept B, disclosure, declaration, statement, acknowledgement,
  attribution, provenance, labelling, transparency; concept C, taxonomy,
  typology, framework, classification, categories, dimensions, rubric, scale,
  levels, checklist, ontology, vocabulary.
- **Block 2, adjacent traditions.** Concept B and C without concept A, narrowed
  to the five named traditions.
- **Block 3, known-item searches** for schemes already named in
  `docs/reserse.md` or in the consultation documents, so that a failure of
  block 1 to retrieve a known scheme becomes visible: AIAS, CANGARU, CRediT,
  C2PA Content Credentials, STM classification, the Global Reporting Standard
  for AI Disclosure in Research, the AID Framework, DAISY, the faceted
  attribution proposal, CONSORT-AI, TRIPOD+AI, CLAIM, DECIDE-AI.

**Snowballing.** One iteration only, from the included set: backward through
Crossref references, forward through Europe PMC citations and OpenCitations.
One iteration is a resource decision and is reported as such.

## 6. Screening

Two independent screeners, each an LLM agent working from these criteria in
batches of fifty titles and abstracts, neither seeing the other's verdict. The
two prompts are derived from this protocol but worded differently, so that
agreement is not merely a measure of one prompt's stability.

- Disagreement is resolved by **inclusion** and settled at full text.
- Cohen's kappa between screeners is computed and reported, including a bad
  result.
- **The author screens twenty randomly drawn records blind** to the agents'
  verdicts. Human versus agent kappa is the only screening quality figure the
  report will claim.

## 7. Data extraction

One row per **dimension**, not per paper. Fields:

| Field | Values |
|---|---|
| `scheme_id` | slug assigned at extraction |
| `scheme_name_verbatim` | as the source names it, or `not_stated` |
| `source_ref` | DOI, arXiv ID or URL |
| `domain` | research publishing, education and assessment, journalism and media, government, software, workplace, advertising, law and regulation, other |
| `artifact_type` | empirical study, normative proposal, policy, reporting guideline, technical standard |
| `granularity` | document, section, paragraph, sentence, asset, `not_stated` |
| `dimension_label_verbatim` | the source's own label |
| `definition_quote` | verbatim, 25 words maximum |
| `value_list_verbatim` | the enumerated values, verbatim, or empty |
| `closed_or_open` | closed list, open text, `not_stated` |
| `authority` | self-report, editorial requirement, regulatory, technical standard, `not_stated` |
| `empirical_basis` | corpus size, or `none` |
| `machine_readable_artifact` | URL, or `none` |
| `locator` | section or page, or `abstract` |
| `quote` | verbatim, 25 words maximum |
| `quote_verified` | written by the verification script, never by an agent |

`not_stated` is an available value everywhere. An empty field is an error; a
`not_stated` is a finding.

**The quote verification gate.** Every `quote` and `definition_quote` must be a
substring of the retrieved source text after whitespace normalisation. A quote
that cannot be located voids the whole row and the paper is queued for a second
extraction. Rows from records held as `abstract_only` are verified against the
abstract, carry `locator: abstract`, and are reported separately from rows
verified against a full text.

**The author spot checks ten extractions** against the source.

## 8. Synthesis

The dimension vocabulary is built **bottom up**, by merging verbatim labels.
The eight components of the parent project are mapped onto the finished
vocabulary as one column among the others, and only after it is closed. They
are not used as the merging frame, because that would return them.

Outputs: `data/lit/dimensions.json`, `docs/scoping/crosswalk.md`,
`docs/scoping/report.md`, `docs/scoping/gap-analysis.md`.

## 9. Reporting

PRISMA-ScR. The flow reconciles: records retrieved equals duplicates plus
excluded at screening plus text not retrievable plus included. Counts that do
not reconcile are printed as an error, not adjusted.

## 10. How this review is produced

Recorded in the row format the parent project proposes, because a review about
disclosure that hides its own production would not be worth reading.

- **Searching, retrieval, deduplication, verification of quotes.** Actor:
  deterministic scripts in `src/lit/`, written by Claude (Anthropic) Opus 5.
  Checked by: the author, at the level of design; the output is checked by the
  acceptance tests in section 9. Trace: this repository.
- **Screening and extraction.** Actor: Claude agents, two independent screeners
  and one extractor per batch. Checked by: the quote verification gate for
  every row, the author for twenty screening decisions and ten extractions.
  Trace: `data/lit/screen/` and `data/lit/schemes.jsonl`, both versioned.
- **Protocol, research questions, eligibility criteria.** Actor: drafted by
  Claude Opus 5 from the project brief, decided by the author 2026-09-27.
  Checked by: the author. Trace: this file and its commit.
- **What could not be checked.** Whether the two screener prompts are
  independent enough to make their agreement meaningful. Whether the search
  missed a domain whose vocabulary differs so much that none of the queries
  reach it. Neither can be settled from inside this review.

## 11. Deviations log

Appended only. Nothing above this line changes after the first search.

- 2026-09-27: protocol frozen, no deviations yet.
- 2026-09-27: **candidate windows added to the extraction packets.** Section 7
  says what to extract, not how an extractor navigates a paper. Reading every
  retrieved full text in full would have cost more than the rest of the pipeline
  together, so `extract.py prepare` now pre-cuts up to twelve passages around
  terms a scheme is usually stated with (taxonomy, dimension, levels, coding
  scheme, checklist and so on) and puts them in the packet with the heading above
  each. This is logged as a deviation even though it changes no criterion,
  because it changes what an extractor sees first and could therefore change what
  it finds. Three safeguards: the whole retrieved text stays on disk and the
  extractor is instructed to open it, quotes are verified against the whole text
  and not against the windows, and the report states the measure under
  limitations. The term list is in `src/lit/extract.py` as `WINDOW_TERMS` and is
  versioned with everything else.
- 2026-09-27: **a safety net for records with no abstract.** 482 of the 2750
  records carry no abstract in any index we searched, so the screeners judged
  them on the title alone. That is thin evidence for an exclusion, because a
  paper can name its taxonomy only in section 3. Section 6 is therefore extended:
  a record with no abstract whose **title** contains both a disclosure word and a
  scheme word is carried to full text even when both screeners excluded it, and
  is flagged `carried_no_abstract` so the report counts it separately. The two
  word lists are in `src/lit/screen.py` as `DISCLOSURE_WORDS` and `SCHEME_WORDS`.
  The rule is deliberately narrow: it never overrules a screener who had an
  abstract in front of them, and it cannot rescue a record whose title says
  nothing. Records excluded by both screeners on a title alone remain a stated
  risk of under-inclusion; this reduces it, it does not remove it.

- 2026-10-01: **candidate windows and screening batches removed from git, and a
  limit stated for what may stay.** Section 10 says the repository carries the
  locator, the hash and quotes of up to 25 words, never the retrieved text. Two
  directories broke that and nobody noticed until the branch was about to be
  published for the first time. `data/lit/extract/packets/` held 137 files with
  892,648 words of verbatim third-party text, the longest single passage 1,949
  words; `data/lit/screen/batches/` held another 55 files of titles and
  abstracts. Both are now in `.gitignore` and both were removed from the whole
  history of the branch with `git filter-branch`, before the first push rather
  than after it. Nothing is lost: `extract prepare` rebuilds the packets from
  the local full-text cache and `screen prepare` rebuilds the batches from
  `records.jsonl`, and both were rebuilt to the same counts to prove it.
  **What stays and why.** `records.jsonl` keeps the abstract of each record. An
  abstract exceeds the 25-word limit, so this is a stated exception rather than
  an oversight: abstracts are index metadata, redistributed as such by Crossref,
  OpenAlex and Europe PMC, they are not the body of the work, and without them
  the screening cannot be repeated from the frozen file. The exception is stated
  at its true size rather than as a word: 2268 records carry an abstract, median
  205 words, 95th percentile 400, but 113 run past 400 words, 23 past 600 and
  the longest is 5007. The long ones are not abstracts in any ordinary sense;
  they are what the index returned in the abstract field, which for some
  publishers and for Zenodo deposits is the whole description of the document.
  They are kept because they are the field the screeners actually read and
  because the indexes serve them publicly, not because they are short. `extract/raw/` keeps
  what the extraction agents returned, whose longest string is 60 words, as the
  audit trail behind every row in `schemes.jsonl`. `screen/verdicts/` keeps the
  verdicts and their one-line notes, which carry no source text.
  This was found by a scan for third-party text before the first push. The audit
  of 2026-09-29 missed it: it tested file extensions and the passages were inside
  JSON. That audit's claim that no third-party full text was committed was wrong
  when it was written.
