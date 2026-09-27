"""Retrieve the text of the included records, in the cleanest form available.

    python -m src.lit.retrieve

Every extracted quote is later checked against the file this module writes, so
what lands here defines what can be quoted. That makes the order of preference a
methodological choice, not a convenience:

1. **Europe PMC full text XML.** Structured, with section titles intact, so a
   locator like "Methods" survives.
2. **arXiv HTML.** Recent preprints have an HTML rendering, which keeps headings
   and loses none of the body to PDF layout.
3. **A PDF**, from the record's open access location or from Unpaywall. Layout
   extraction reorders columns and drops table structure, so a quote from a table
   may fail verification even when the table is really there. That is recorded as
   a limitation, not worked around.
4. **The abstract only.** Kept as the source text so a row extracted from an
   abstract can still be verified, and marked so the report never presents it as
   a full-text finding.

Nothing written here is committed; `data/lit/fulltext/` is gitignored, because
the texts belong to their publishers and the repository is public. What is
committed is `retrieval.jsonl`: the status, the source, the byte count and the
sha256, which is enough to prove later that a quote was checked against a
specific retrieved text.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
import re
import sys

from . import http, sources

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LIT = os.path.join(ROOT, "data", "lit")
INCLUDED = os.path.join(LIT, "screened-in.jsonl")
FULLTEXT = os.path.join(LIT, "fulltext")
RETRIEVAL = os.path.join(LIT, "retrieval.jsonl")

MIN_FULLTEXT_CHARS = 3000


def _pdf_to_text(raw: bytes) -> tuple[str, str]:
    """Text from PDF bytes, preferring the extractor that keeps reading order.

    PyMuPDF handles two-column layouts better than pypdf. Either is acceptable;
    which one ran is recorded, because a quote that fails verification may have
    failed on extraction rather than on the agent's honesty.
    """
    try:
        import fitz  # PyMuPDF
        with fitz.open(stream=raw, filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc), "pymupdf"
    except Exception:
        pass
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(raw))
        return "\n".join((page.extract_text() or "") for page in reader.pages), "pypdf"
    except Exception as exc:
        print(f"    pdf extraction failed: {type(exc).__name__}")
        return "", "none"


def _html_to_text(html_text: str) -> str:
    """Body text from an HTML page, with headings kept as their own lines."""
    text = re.sub(r"(?is)<(script|style|nav|footer)[^>]*>.*?</\1>", " ", html_text)
    text = re.sub(r"(?i)</(h[1-6]|p|div|li|section)\s*>", "\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    import html as html_mod
    text = html_mod.unescape(text)
    lines = [re.sub(r"[^\S\n]+", " ", line).strip() for line in text.split("\n")]
    return "\n".join(line for line in lines if line)


def _xml_to_text(xml: str) -> str:
    """Text from JATS full text, keeping section titles on their own lines."""
    text = re.sub(r"(?is)<(ref-list|back)[^>]*>.*?</\1>", " ", xml)
    text = re.sub(r"(?i)<title[^>]*>", "\n## ", text)
    text = re.sub(r"(?i)</(title|p|sec|abstract)\s*>", "\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    import html as html_mod
    text = html_mod.unescape(text)
    lines = [re.sub(r"[^\S\n]+", " ", line).strip() for line in text.split("\n")]
    return "\n".join(line for line in lines if line)


def _store(rec_id: str, text: str) -> tuple[str, int]:
    os.makedirs(FULLTEXT, exist_ok=True)
    path = os.path.join(FULLTEXT, f"{rec_id}.txt")
    with io.open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return digest, len(text)


def retrieve_one(record: dict) -> dict:
    rec_id = record["rec_id"]
    attempts: list[str] = []

    if record.get("pmcid"):
        xml = sources.europepmc_fulltext_xml(record["pmcid"])
        attempts.append(f"europepmc_xml:{len(xml)}")
        if xml:
            text = _xml_to_text(xml)
            if len(text) >= MIN_FULLTEXT_CHARS:
                digest, size = _store(rec_id, text)
                return {"rec_id": rec_id, "status": "fulltext_oa",
                        "text_source": "europepmc_xml", "extractor": "jats",
                        "url": f"https://europepmc.org/article/PMC/{record['pmcid']}",
                        "chars": size, "sha256": digest, "attempts": attempts}

    if record.get("arxiv_id"):
        resp = http.get(f"https://arxiv.org/html/{record['arxiv_id']}")
        attempts.append(f"arxiv_html:{len(resp.content) if resp else 0}")
        if resp is not None and "text/html" in resp.headers.get("content-type", ""):
            text = _html_to_text(resp.text)
            if len(text) >= MIN_FULLTEXT_CHARS:
                digest, size = _store(rec_id, text)
                return {"rec_id": rec_id, "status": "fulltext_oa",
                        "text_source": "arxiv_html", "extractor": "html",
                        "url": f"https://arxiv.org/html/{record['arxiv_id']}",
                        "chars": size, "sha256": digest, "attempts": attempts}

    pdf_urls = [url for url in (record.get("oa_pdf_url"),
                                f"https://arxiv.org/pdf/{record['arxiv_id']}"
                                if record.get("arxiv_id") else "") if url]
    if record.get("doi") and not pdf_urls:
        found = sources.unpaywall_pdf(record["doi"])
        if found and found.lower().endswith(".pdf"):
            pdf_urls.append(found)
    for url in pdf_urls:
        resp = http.get(url)
        attempts.append(f"pdf:{url[:60]}:{len(resp.content) if resp else 0}")
        if resp is None:
            continue
        if "pdf" not in resp.headers.get("content-type", "").lower():
            continue
        text, extractor = _pdf_to_text(resp.content)
        if len(text) >= MIN_FULLTEXT_CHARS:
            digest, size = _store(rec_id, text)
            return {"rec_id": rec_id, "status": "fulltext_oa",
                    "text_source": "pdf", "extractor": extractor, "url": url,
                    "chars": size, "sha256": digest, "attempts": attempts}

    abstract = record.get("abstract", "")
    if abstract:
        digest, size = _store(rec_id, abstract)
        return {"rec_id": rec_id, "status": "abstract_only",
                "text_source": "abstract", "extractor": "none",
                "url": record.get("url", ""), "chars": size, "sha256": digest,
                "attempts": attempts}

    return {"rec_id": rec_id, "status": "no_text", "text_source": "none",
            "extractor": "none", "url": record.get("url", ""), "chars": 0,
            "sha256": "", "attempts": attempts}


def main() -> int:
    if not os.path.exists(INCLUDED):
        print("no screened-in.jsonl; run the screening first")
        return 1
    records = []
    with io.open(INCLUDED, encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                records.append(json.loads(line))

    done: dict[str, dict] = {}
    if os.path.exists(RETRIEVAL):
        with io.open(RETRIEVAL, encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    row = json.loads(line)
                    done[row["rec_id"]] = row

    rows = []
    for index, record in enumerate(records, 1):
        rec_id = record["rec_id"]
        stored = os.path.join(FULLTEXT, f"{rec_id}.txt")
        if rec_id in done and os.path.exists(stored):
            rows.append(done[rec_id])
            continue
        row = retrieve_one(record)
        rows.append(row)
        print(f"[{index}/{len(records)}] {rec_id} {row['status']:14} "
              f"{row['text_source']:14} {row['chars']:>7} chars  "
              f"{record['title'][:50]}")

    with io.open(RETRIEVAL, "w", encoding="utf-8", newline="\n") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    print("\nretrieval:", counts)
    print(f"wrote {RETRIEVAL}; texts in {FULLTEXT} (gitignored)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
