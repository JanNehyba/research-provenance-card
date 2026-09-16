# Corpus

`corpus.jsonl`, one disclosure formulation per line.

Public sources only. No names, no email addresses, nothing that identifies an
individual. Collectors redact email addresses before an item is written, and
`common.Item.problems()` refuses any item that still contains one.

## Fields

`id` `text_verbatim` `lang` `genre` `templated` `template_family` `trigger_phrase`
`source_type` `source_url` `source_date` `collected_at` `placement`
`context_note` `license_note`

`templated` marks a formulation that reuses publisher boilerplate. It is the
study's main explanatory variable, so it is computed at collection time rather
than left to the coder. `template_family` records which publisher's wording the
item follows (`frontiers`, `springer_nature`, `wiley`, `elsevier`), or is empty
when the wording is the author's own. Springer and Nature are one publisher
group and share a family. `trigger_phrase` is the phrase the collector found
the item with, and an item is refused if that phrase occurs more than once
inside it, which is how squashed merge commits get dropped.

## Running a collector

    cd src/collect
    python europepmc.py "<absolute path>/data/corpus/corpus.jsonl"
    python github.py   "<absolute path>/data/corpus/corpus.jsonl"

Collectors append. They skip items already present and near-duplicates of the
same wording, so re-running is safe. `github.py` needs `gh auth login`.

## Status, 2026-09-16

Seed run of 40 items (21 articles, 19 software projects), English only. The run
was a pipeline test and it found four defects, listed in
`docs/postup-korpus.md`. Do not treat these 40 items as corpus data until the
extraction is fixed and the file is rebuilt from scratch.
