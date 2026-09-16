"""Shared pieces for the corpus collectors.

One item is one AI disclosure formulation found in the wild, plus enough
metadata to find it again. Standard library only, so a collector can be run on
any machine without installing anything.

Nothing personal goes into an item. We keep the wording of the formulation and
a public URL, never a name or an email address.
"""

from __future__ import annotations

import hashlib
import html
import io
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field

USER_AGENT = (
    "ai-disclosure-framing-research/0.1 "
    "(academic corpus collection; https://github.com/JanNehyba/research-provenance-card)"
)

GENRES = (
    "article",
    "email_message",
    "teaching_internal",
    "software_project",
    "thesis",
    "social_media",
)

# Publisher boilerplate, grouped by family. A formulation that contains one of
# these markers is a template fill-in, not the author's own sentence. The
# matched family is stored on the item, not just a yes/no flag, because
# `templated` is the study's main explanatory variable and a false negative or
# a muddled family is worse than anywhere else in the pipeline.
#
# Springer and Nature are one publisher group handing authors the same
# statement, so they share a family. Springer Nature is checked before
# Elsevier because their wordings overlap heavily and Springer Nature's is the
# superset. Frontiers is checked first because its wording is the most
# distinctive.
TEMPLATE_FAMILIES: dict[str, tuple[str, ...]] = {
    "frontiers": (
        "was used in the creation of this manuscript",
    ),
    "springer_nature": (
        "generative ai and ai-assisted technologies in the writing process",
        "after using this tool or service",
    ),
    "wiley": (
        "in the course of preparing this work",
        "in the course of preparing this manuscript",
    ),
    "elsevier": (
        "during the preparation of this work",
        "during the preparation of this manuscript",
        "after using this tool/service",
        "reviewed and edited the content as needed",
        "take full responsibility for the content of the publication",
        "takes full responsibility for the content of the publication",
        "the author(s) used",
    ),
}

# Where a disclosure ends. The forward cut of the extraction window stops at
# any of these section headings instead of at a character count, so an item
# cannot drag the next section in with it.
SECTION_BREAKS = (
    "footnotes",
    "references",
    "acknowledgement",
    "acknowledgment",
    "data availability",
    "author contribution",
    "competing interest",
    "conflict of interest",
    "abbreviations",
    "backmatter",
    "publisher's note",
    "additional information",
    "consent for publication",
    "ethics approval",
    "supplementary information",
)

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
URL_IN_TEXT_RE = re.compile(r"https?://\S+")


@dataclass
class Item:
    """One disclosure formulation."""

    text_verbatim: str
    lang: str
    genre: str
    source_type: str
    source_url: str
    source_date: str = ""
    placement: str = ""
    context_note: str = ""
    license_note: str = ""
    templated: bool = False
    template_family: str = ""
    trigger_phrase: str = ""
    collected_at: str = ""
    id: str = field(default="")

    def finalise(self) -> "Item":
        self.text_verbatim = normalise_ws(self.text_verbatim)
        family = template_family_of(self.text_verbatim)
        self.templated = family != ""
        self.template_family = family
        self.collected_at = self.collected_at or time.strftime("%Y-%m-%d")
        self.id = self.id or item_id(self.text_verbatim, self.source_url)
        return self

    def problems(self) -> list[str]:
        """Reasons this item must not enter the corpus."""
        bad = []
        if self.genre not in GENRES:
            bad.append(f"unknown genre {self.genre!r}")
        if len(self.text_verbatim) < 25:
            bad.append("text too short to be a formulation")
        if len(self.text_verbatim) > 1200:
            bad.append("text too long, extraction window probably overran")
        if not self.source_url.startswith("http"):
            bad.append("source_url is not a public URL")
        if EMAIL_RE.search(self.text_verbatim) or EMAIL_RE.search(self.context_note):
            bad.append("contains an email address")
        first_letter = next((ch for ch in self.text_verbatim if ch.isalpha()), "")
        if first_letter and first_letter.islower():
            bad.append("starts mid-sentence, first letter is lower case")
        if self.trigger_phrase:
            if self.text_verbatim.lower().count(self.trigger_phrase.lower()) > 1:
                bad.append("the same trigger phrase appears more than once")
        return bad


def normalise_ws(text: str) -> str:
    return " ".join(text.replace(" ", " ").split())


def template_family_of(text: str) -> str:
    """Publisher family whose boilerplate this wording follows, "" if none."""
    low = text.lower()
    for family, markers in TEMPLATE_FAMILIES.items():
        for marker in markers:
            if marker in low:
                return family
    return ""


def item_id(text: str, url: str) -> str:
    key = normalise_ws(text).lower() + "|" + url
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def dedup_key(text: str) -> str:
    """Near-duplicate key: same wording from a different source is one item.

    Template disclosures repeat verbatim across thousands of articles. We want
    them counted, but we do not want the corpus to be one sentence 500 times.
    """
    low = normalise_ws(text).lower()
    low = re.sub(r"[^a-z ]+", "", low)
    return hashlib.sha256(low.encode("utf-8")).hexdigest()[:16]


def fetch(url: str, retries: int = 3, pause: float = 1.0) -> str:
    """GET a URL politely. Returns "" on a permanent failure rather than raising."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 403):
                return ""
            time.sleep(pause * (attempt + 1))
        except Exception:
            time.sleep(pause * (attempt + 1))
    return ""


def strip_tags(xml: str) -> str:
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", xml, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return normalise_ws(text)


def sentence_start(text: str, idx: int, max_back: int = 600) -> int:
    """Index where the sentence holding `idx` begins, or -1 if unknown.

    Walks back to the nearest sentence boundary instead of assuming one sits
    within 40 characters. When the whole prefix up to the start of the text has
    no boundary either, the sentence starts at position 0.
    """
    lo = max(0, idx - max_back)
    for i in range(idx - 2, lo - 1, -1):
        if text[i] in ".!?":
            if i + 1 < len(text) and text[i + 1] == " ":
                return i + 2
    return 0 if lo == 0 else -1


def window_around(text: str, needle: str, before: int = 600, after: int = 900) -> str:
    """Pull the formulation out of a document.

    Starts at the beginning of the sentence the trigger phrase sits in and runs
    forward to the end of the disclosure: stops before the next section heading,
    before a repeated trigger (a squashed merge lists every sub-commit), and
    failing those at the last complete sentence before the cap. Returns "" when
    no sentence start can be found, so a mid-sentence fragment cannot pass.
    """
    low_text = text.lower()
    low_needle = needle.lower()
    idx = low_text.find(low_needle)
    if idx < 0:
        return ""

    start = sentence_start(text, idx, before)
    if start < 0:
        return ""

    end_cap = min(len(text), idx + after)
    second = low_text.find(low_needle, idx + len(low_needle))
    if second != -1:
        end_cap = min(end_cap, second)
    tail_low = low_text[idx:end_cap]
    for marker in SECTION_BREAKS:
        pos = tail_low.find(marker)
        if pos > 20:
            end_cap = min(end_cap, idx + pos)

    end = end_cap
    tail = max(
        text.rfind(". ", idx, end_cap),
        text.rfind("! ", idx, end_cap),
        text.rfind("? ", idx, end_cap),
    )
    if tail != -1 and tail > idx + 40:
        end = tail + 1
    return normalise_ws(text[start:end])


def load_existing(path: str) -> dict[str, dict]:
    if not os.path.exists(path):
        return {}
    out = {}
    with io.open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                row = json.loads(line)
                out[row["id"]] = row
    return out


def write_items(path: str, items: list[Item], verbose: bool = True) -> dict[str, int]:
    """Append valid, non-duplicate items to a JSONL corpus file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    existing = load_existing(path)
    seen_text = {dedup_key(row["text_verbatim"]) for row in existing.values()}

    stats = {"added": 0, "duplicate": 0, "rejected": 0}
    rows = []
    for item in items:
        item.finalise()
        problems = item.problems()
        if problems:
            stats["rejected"] += 1
            if verbose:
                print(f"  rejected: {'; '.join(problems)} :: {item.text_verbatim[:70]}")
            continue
        key = dedup_key(item.text_verbatim)
        if item.id in existing or key in seen_text:
            stats["duplicate"] += 1
            continue
        seen_text.add(key)
        rows.append(item)
        stats["added"] += 1

    with io.open(path, "a", encoding="utf-8", newline="\n") as fh:
        for item in rows:
            fh.write(json.dumps(asdict(item), ensure_ascii=False) + "\n")
    return stats
