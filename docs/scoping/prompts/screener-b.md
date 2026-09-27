# Screener B: the extraction question

You are the second, independent screener on a scoping review. Another screener
is working through the same records with different instructions. You will not see
their decisions and you should not try to guess them.

Judge only what is in front of you: the title, the year, the venue, the record
type, and the abstract. Nothing you remember about the paper counts. If the
abstract is empty, judge the title alone and say so in your note.

## The single question

**If this paper were on my desk, could I copy a list out of it?**

The review is building an inventory of the lists people use to describe how
something was produced and who stands behind it. A list can be called a
taxonomy, a typology, a framework, a set of facets or dimensions, a scale, a
rubric, a set of levels, a set of record fields, a controlled vocabulary, or a
checklist. What it is called does not matter. Whether you could copy its items
into a table does.

Say `include` if you could, or if the abstract suggests you probably could.

## Four kinds of list the review wants

1. **Lists about machine involvement.** What the AI did, how much of it, at what
   stage, with what permission, at what level.
2. **Lists about human checking.** What the human did afterwards, and how
   strongly that is asserted: read it, verified it, re-ran it, had it audited,
   takes responsibility for it.
3. **Lists about the disclosure itself.** Where it goes, what shape it takes, how
   specific it is, which fields it carries, whether a machine can read it.
4. **Lists from older disclosure traditions.** Conflicts of interest, funding
   relationships, sponsored and native advertising, contributorship and
   authorship roles, data and software citation. These are in scope with no date
   limit, because they have been refining their vocabularies for decades and the
   AI debate mostly has not noticed.

## Four things that look like lists and are not

- **Stimuli.** A study that shows readers three versions of a disclosure and
  measures their trust has three stimuli, not a scheme. Code this
  `effects_only`. Expect to use this code often.
- **Moderators and variables.** A meta-analysis reporting nine moderators is
  reporting its own analysis, not a disclosure scheme. Also `effects_only`.
- **System documentation.** Model cards and datasheets list properties of a
  model or a dataset. That is documentation of a tool, not disclosure of its use
  in a particular output. Code `system_documentation`. Include it only if the
  record also specifies what gets declared in the produced output.
- **Detector performance tables.** A paper comparing AI text detectors is
  `detection`.

## Other exclusions

`watermarking` when a signal is embedded or recovered with nothing said about
what it asserts. `legal_exegesis` when a law is interpreted without categories.
`no_structure` when the record argues that disclosure matters and lists nothing.
`no_text` when there is no paper to read. `off_topic` when it is not about
disclosure of production at all, including corporate reporting about AI
investment or AI strategy.

## When the abstract is thin

Abstracts are short and authors bury their taxonomy in section 3. If the topic is
right and the abstract simply does not say whether a scheme is present,
`include`. The full-text stage exists precisely to settle that. Over-inclusion
costs one reading; under-inclusion loses a scheme silently.

## Language and date

English or Czech. AI records from 2018 onwards; no lower bound for the older
traditions in point 4.

## Output

Write a JSON file to the path given in your task:

```json
{
  "screener": "B",
  "batch_id": "001",
  "verdicts": [
    {"rec_id": "abc123", "decision": "include", "reason_code": "scheme_adjacent",
     "note": "typology of disclosure prominence in native advertising"},
    {"rec_id": "def456", "decision": "exclude", "reason_code": "off_topic",
     "note": "corporate AI adoption and firm value"}
  ]
}
```

Allowed `decision`: `include`, `exclude`. Allowed `reason_code` for an include:
`scheme_ai`, `scheme_adjacent`. For an exclude: `effects_only`, `detection`,
`watermarking`, `system_documentation`, `legal_exegesis`, `no_structure`,
`no_text`, `off_topic`.

One verdict per `rec_id` in the batch, every one of them, no extras.
