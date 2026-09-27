# Extractor: pull the category scheme out of one paper

You are extracting data for a scoping review. Your output is machine-checked, so
read this whole file before you start.

## The one rule that matters

**Every quote you write is verified as a substring of the text file you were
given.** A script normalises whitespace, dashes and quotation marks, then looks
for your quote in that file. If it is not there, the whole row is thrown away and
the paper is sent back to be extracted again.

So: **copy, do not retype, and never improve the wording.** Not the author's
grammar, not their capitalisation, not a typo. If a sentence you want runs across
a line break in the file, copy it across the break; the script collapses
whitespace. Do not quote from memory and do not quote anything you did not find
in that file.

If you cannot find a sentence in the text that supports a field, the value is
`not_stated`. That is a finding, not a failure. Papers that say less than you
expected are part of the result.

## What you are looking for

A **category scheme**: any named or enumerable set of categories, dimensions,
facets, levels, fields, roles or checklist items that the paper uses to describe
a disclosure, an attribution, or a provenance claim about something that was
produced.

A **dimension** is one axis of such a scheme. If the paper offers a scheme with
six facets, that is one scheme with six dimensions, and you write six rows.

If the paper's scheme is a single scale, for example five levels of permitted AI
use, that is one scheme with one dimension whose `value_list_verbatim` holds the
five level names.

## If there is no scheme

Full texts often disappoint. If, after reading, the paper turns out to have no
scheme at all, say so plainly:

```json
{"rec_id": "abc123", "has_scheme": false,
 "reason": "measures trust in three disclosure wordings; no categories proposed or used"}
```

Do not invent a scheme out of a paper's section headings, its variables, or its
recommendations. A paper that says "authors should disclose which tool they used
and for what purpose" does enumerate two dimensions and counts. A paper that says
"transparency is essential" does not.

## Fields

Per scheme:

| Field | What goes in it |
|---|---|
| `scheme_id` | a slug you invent, lowercase with hyphens, recognisable, for example `xexeo-faceted-attribution` or `aias-five-levels` |
| `scheme_name_verbatim` | the name the paper gives it, copied. `not_stated` if it has none |
| `source_ref` | copy the `source_ref` from the packet entry |
| `domain` | one of `research_publishing`, `education_assessment`, `journalism_media`, `government`, `software`, `workplace`, `advertising`, `law_regulation`, `other` |
| `artifact_type` | one of `empirical_study`, `normative_proposal`, `policy`, `reporting_guideline`, `technical_standard` |
| `granularity` | what the scheme is applied to: `document`, `section`, `paragraph`, `sentence`, `asset`, or `not_stated` |
| `authority` | who makes it binding: `self_report`, `editorial_requirement`, `regulatory`, `technical_standard`, `not_stated` |
| `empirical_basis` | the corpus or sample the scheme was built or tested on, as the paper states it, for example `51 disclosure statements`. `none` if the scheme is proposed without data |
| `machine_readable_artifact` | a URL to a schema, vocabulary or dataset the paper points at, else `none` |

Per dimension:

| Field | What goes in it |
|---|---|
| `dimension_label_verbatim` | the paper's own label, copied exactly, not tidied |
| `definition_quote` | the paper's definition of that dimension, copied, 25 words at most. `""` if it defines nothing |
| `value_list_verbatim` | the values it enumerates, each copied, as a list. `[]` if it enumerates none |
| `closed_or_open` | `closed_list` if the values are a fixed set, `open_text` if the field is free text, `not_stated` |
| `locator` | where you found it: a section heading or a page, copied from the text. For an abstract-only paper, write `abstract` |
| `quote` | a copied passage, 25 words at most, that shows this dimension exists in the paper |

Do not write a `quote_verified` field. The script writes that.

## Output shape

One JSON file per packet, at the path your task gives you:

```json
{
  "packet_id": "001",
  "papers": [
    {
      "rec_id": "abc123",
      "has_scheme": true,
      "schemes": [
        {
          "scheme_id": "example-three-facets",
          "scheme_name_verbatim": "the Attribution Facet Model",
          "source_ref": "arXiv:2604.25346",
          "domain": "research_publishing",
          "artifact_type": "normative_proposal",
          "granularity": "section",
          "authority": "self_report",
          "empirical_basis": "none",
          "machine_readable_artifact": "none",
          "dimensions": [
            {
              "dimension_label_verbatim": "Generation",
              "definition_quote": "who or what produced the initial text",
              "value_list_verbatim": ["human", "machine", "mixed"],
              "closed_or_open": "closed_list",
              "locator": "Section 3.2",
              "quote": "The Generation facet records who or what produced the initial text"
            }
          ]
        }
      ]
    },
    {"rec_id": "def456", "has_scheme": false, "reason": "editorial, enumerates nothing"}
  ]
}
```

Every `rec_id` in the packet must appear exactly once in your output.

## How to work through a paper

1. Read the packet entry. Note the `retrieval_status`. If it is `abstract_only`,
   you have only an abstract; extract what is there and put `abstract` in every
   `locator`. Do not speculate about the rest of the paper.
2. **Work from `candidate_windows` in the packet.** A script cut out the passages
   around words like taxonomy, dimension, levels, coding scheme and checklist,
   each with the heading above it and its `starts_at_char` offset. Between them
   they cover a large part of the paper, and most papers give up their scheme
   here. This is where you should expect to do nearly all of your work.
3. **Open `text_file` only for a specific reason**, and then read a part of it,
   not all of it. A good reason: the windows show a named scheme whose dimension
   list visibly runs past the end of a window, or a table that has been cut in
   half. A bad reason: wanting to be thorough in general. Reading whole papers is
   what this pipeline cannot afford, and a packet spent that way is a packet not
   spent on the next three papers. Use the `starts_at_char` offset to go to the
   right part of the file rather than reading from the top.
4. Look for the places schemes live: a methods or coding section, a framework or
   model section, a table of categories, a numbered list, an appendix.
5. For each scheme, copy its dimensions out one at a time.
6. Before writing, check each quote against the file once more. This is cheaper
   than an extraction that gets thrown away.

## What not to do

- Do not read any other paper's text file.
- Do not search the web. Everything you need is in the packet and the text files.
- Do not merge two papers' schemes because they look similar. Similar schemes
  from different papers are separate rows; the merging happens later, deliberately,
  in a step that is not yours.
- Do not translate. Czech labels stay Czech.
