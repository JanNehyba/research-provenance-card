"""Shared pieces for the corpus collectors.

One item is one AI disclosure formulation found in the wild, plus enough
metadata to find it again. Standard library only, so a collector can be run on
any machine without installing anything.

Nothing personal goes into an item. We keep the wording of the formulation and
a public URL, never a name or an email address.
"""

from __future__ import annotations

import hashlib
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

# Wordings that publishers hand authors. A formulation that contains one of
# these is a template fill-in, not the author's own sentence. This flag is the
# main explanatory variable of the study, so it is computed here rather than
# left to the coder.
TEMPLATE_MARKERS = (
    "during the preparation of this work",
    "during the preparation of this manuscript",
    "the author(s) used",
    "after using this tool/service",
    "after using this tool or service",
    "take(s) full responsibility for the content of the publication",
    "take full responsibility for the content of the publication",
    "reviewed and edited the content as needed",
    "generative ai and ai-assisted technologies in the writing process",
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
    collected_at: str = ""
    id: str = field(default="")

    def finalise(self) -> "Item":
        self.text_verbatim = normalise_ws(self.text_verbatim)
        self.templated = is_templated(self.text_verbatim)
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
        return bad


def normalise_ws(text: str) -> str:
    return " ".join(text.replace(" ", " ").split())


def is_templated(text: str) -> bool:
    low = text.lower()
    return any(marker in low for marker in TEMPLATE_MARKERS)


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
    return normalise_ws(text)


def window_around(text: str, needle: str, before: int = 40, after: int = 520) -> str:
    """Pull the formulation out of a document.

    Starts at the sentence the trigger phrase sits in and runs forward to the
    end of the disclosure, capped so a bad match cannot drag half a paper in.
    """
    idx = text.lower().find(needle.lower())
    if idx < 0:
        return ""
    start = idx
    back = text.rfind(". ", max(0, idx - before), idx)
    if back != -1:
        start = back + 2
    end = min(len(text), idx + after)
    tail = text.rfind(". ", idx, end)
    if tail != -1 and tail > idx + 60:
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
