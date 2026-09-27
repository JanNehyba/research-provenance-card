# Screener A: criteria checklist

You are screening titles and abstracts for a scoping review. Work only from the
text you are given. Do not look anything up, do not use what you remember about
a paper, and do not guess at a paper's contents from its title style.

## What the review is collecting

**Category schemes for describing disclosure of how something was produced.** A
category scheme is any named or enumerable set of categories, dimensions,
facets, levels, fields, or checklist items used to describe a disclosure, an
attribution, or a provenance claim about a produced output.

The output can be a research article, a news story, a government document, a
student assignment, a piece of software, a social media post, an advertisement.
The scheme can be proposed by the authors, imposed by an institution, encoded in
a technical standard, or observed in a corpus.

## Decide in this order

**Step 1. Is there a scheme, or could there be one?**

Include if the record enumerates, or clearly says it enumerates, categories of
any of these:

- what an AI did, or how much it did
- levels or degrees of permitted or actual AI use
- what a human did to check the output
- where a disclosure sits, or what form it takes (byline, label, statement,
  footnote, metadata field)
- fields of a disclosure record or a provenance record
- types of contribution or authorship
- types of conflict of interest, funding relationship, or sponsorship
- items of a reporting checklist or guideline about how something was produced

**Step 2. Is it one of the excluded kinds?** Exclude if the record is only:

- `effects_only`: an experiment or survey measuring how readers react to a
  disclosure, with no scheme of its own. This is the most common wrong include.
  Measuring the effect of three different wordings is not a scheme; the three
  wordings are stimuli.
- `detection`: distinguishing machine-written from human-written text.
- `watermarking`: hiding or recovering a signal, without saying what the signal
  asserts.
- `system_documentation`: model cards, datasheets for datasets, system cards.
  These document an AI system, not the disclosure of its use in one output.
  Exception: include if it specifies how use is declared in a produced output.
- `legal_exegesis`: commentary on a law or regulation with no categories of its
  own.
- `no_structure`: asserts that disclosure should happen and enumerates nothing.
  Most editorials are this.
- `no_text`: a record with no paper behind it, for example a bare conference
  abstract.
- `off_topic`: not about disclosure, attribution or provenance at all. Note that
  a paper about companies disclosing their AI *investments* to shareholders is
  off topic; this review is about disclosing how a text was produced.

**Step 3. When you are unsure, include.** A wrong include costs one full-text
read. A wrong exclude removes a scheme from the review permanently and nobody
will find out. These costs are not symmetrical. Include anything where a
plausible reading of the abstract has a scheme in it.

## Language and date

English or Czech only. Any date for records about conflict of interest, funding,
sponsorship, contributorship, or data and software citation. For anything about
AI, 2018 onwards.

## What to return

For every record in the batch, exactly one verdict. Write a JSON file to the
path given in your task, in this shape:

```json
{
  "screener": "A",
  "batch_id": "001",
  "verdicts": [
    {"rec_id": "abc123", "decision": "include", "reason_code": "scheme_ai",
     "note": "enumerates six facets of attribution"},
    {"rec_id": "def456", "decision": "exclude", "reason_code": "effects_only",
     "note": "three disclosure wordings as stimuli, no scheme"}
  ]
}
```

- `decision`: `include` or `exclude`, nothing else.
- `reason_code` for an include: `scheme_ai` when the scheme is about AI use,
  `scheme_adjacent` when it is about conflict of interest, funding, sponsored
  content, contributorship, or data and software citation.
- `reason_code` for an exclude: one of `effects_only`, `detection`,
  `watermarking`, `system_documentation`, `legal_exegesis`, `no_structure`,
  `no_text`, `off_topic`.
- `note`: one short clause. What the scheme is, or why there is none.

Every `rec_id` in the batch must appear exactly once. Do not add records, do not
drop records, do not reorder the fields.
