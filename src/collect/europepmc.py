"""Collect AI disclosure formulations from open access research articles.

Source: Europe PMC. Free, no API key, and it exposes the full text of open
access articles, which matters because disclosures live in acknowledgments and
in dedicated declaration sections, not in abstracts.

The trigger phrases are deliberately mixed. Publisher boilerplate is the easiest
thing to find and would otherwise be the whole sample, so free-form and negative
("no AI was used") phrasings are searched too.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse

from common import Item, fetch, strip_tags, window_around, write_items

SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
ARTICLE_URL = "https://europepmc.org/article/PMC/{pmcid}"

# (phrase, why it is here)
TRIGGERS = [
    ("During the preparation of this work", "Elsevier template"),
    ("used generative AI", "free wording"),
    ("ChatGPT was used to", "free wording, tool named"),
    ("with the assistance of ChatGPT", "free wording"),
    ("was used to improve the readability", "common half-template"),
    ("no artificial intelligence was used", "negative declaration"),
    ("did not use any generative AI", "negative declaration"),
    ("the authors declare that no AI", "negative declaration"),
]


def search_pmcids(phrase: str, limit: int) -> list[dict]:
    query = urllib.parse.quote(f'"{phrase}" AND OPEN_ACCESS:y')
    url = f"{SEARCH}?query={query}&format=json&pageSize={limit}&resultType=lite"
    raw = fetch(url)
    if not raw:
        return []
    try:
        results = json.loads(raw)["resultList"]["result"]
    except (KeyError, ValueError):
        return []
    out = []
    for row in results:
        pmcid = row.get("pmcid")
        if pmcid:
            out.append(
                {
                    "pmcid": pmcid,
                    "year": str(row.get("pubYear", "")),
                    "journal": row.get("journalTitle", ""),
                }
            )
    return out


def section_title_before(xml: str, phrase: str) -> str:
    """Nearest preceding <title>, which is the placement of the disclosure."""
    idx = xml.lower().find(phrase.lower())
    if idx < 0:
        return ""
    titles = list(re.finditer(r"<title[^>]*>(.*?)</title>", xml[:idx], flags=re.S | re.I))
    if not titles:
        return ""
    return strip_tags(titles[-1].group(1))[:120]


# Section names the disclosure commonly sits in, used as a fallback when the
# XML has no <title> before the phrase (4 of 21 article items had no placement).
FALLBACK_SECTIONS = (
    "declaration",
    "acknowledgement",
    "acknowledgment",
    "author contribution",
    "backmatter",
    "competing interest",
    "conflict of interest",
    "funding",
    "data availability",
)


def placement_in_plain(plain: str, phrase: str) -> str:
    """Fallback placement: nearest known section name preceding the phrase."""
    idx = plain.lower().find(phrase.lower())
    if idx < 0:
        return ""
    prefix = plain[:idx].lower()
    best, best_pos = "", -1
    for name in FALLBACK_SECTIONS:
        pos = prefix.rfind(name)
        if pos > best_pos:
            best, best_pos = name, pos
    return best


def collect(per_phrase: int = 4, pause: float = 0.4) -> list[Item]:
    items: list[Item] = []
    for phrase, why in TRIGGERS:
        hits = search_pmcids(phrase, per_phrase)
        print(f"[europepmc] {phrase!r}: {len(hits)} candidates ({why})")
        for hit in hits:
            xml = fetch(FULLTEXT.format(pmcid=hit["pmcid"]))
            time.sleep(pause)
            if not xml:
                continue
            plain = strip_tags(xml)
            placement = (
                section_title_before(xml, phrase)
                or placement_in_plain(plain, phrase)
            )
            text = window_around(plain, phrase)
            if not text:
                continue
            items.append(
                Item(
                    text_verbatim=text,
                    lang="en",
                    genre="article",
                    source_type="open_access_article",
                    source_url=ARTICLE_URL.format(pmcid=hit["pmcid"]),
                    source_date=hit["year"],
                    placement=placement,
                    context_note=f"journal: {hit['journal']}; found via phrase: {phrase}",
                    license_note="open access full text via Europe PMC",
                    trigger_phrase=phrase,
                )
            )
    return items


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "data/corpus/corpus.jsonl"
    found = collect()
    stats = write_items(out, found)
    print(f"[europepmc] {stats}")
