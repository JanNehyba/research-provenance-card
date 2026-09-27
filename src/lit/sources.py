"""Clients for the bibliographic sources named in the protocol.

Every client returns the same `Record` shape, so that `search.py` can pool them
and deduplicate without knowing which service a record came from. Anything a
service does not provide stays an empty string; nothing is inferred and nothing
is filled in from a model's memory.

Each service is used for what it is good at, not interchangeably:

- **Europe PMC** is the only one here that hands over open access full text as
  clean XML, so it carries the retrieval stage as well as the search stage.
- **OpenAlex** has the broadest coverage and the best search endpoint, and it is
  the route to arXiv preprints and to forward citations.
- **Crossref** is the authority on the DOI record itself and on a paper's
  reference list, which is the backward snowballing route.
- **arXiv** is searched directly because a preprint often reaches an index
  months late, and the schemes this review is after are mostly recent.
- **DOAJ, OpenAIRE and DataCite** are there for what the big three miss: open
  access journals outside PubMed, European repositories and theses, and DOIs
  registered with DataCite rather than Crossref.
"""

from __future__ import annotations

import hashlib
import html
import re
import urllib.parse
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from . import http

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works"
ARXIV = "http://export.arxiv.org/api/query"
DOAJ = "https://doaj.org/api/search/articles"
OPENAIRE = "https://api.openaire.eu/search/publications"
DATACITE = "https://api.datacite.org/dois"
UNPAYWALL = "https://api.unpaywall.org/v2"
OPENCITATIONS = "https://opencitations.net/index/api/v1"

ATOM = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


@dataclass
class Record:
    """One bibliographic record, normalised across services."""

    title: str = ""
    abstract: str = ""
    year: str = ""
    venue: str = ""
    doi: str = ""
    arxiv_id: str = ""
    pmcid: str = ""
    pmid: str = ""
    url: str = ""
    record_type: str = ""
    oa_pdf_url: str = ""
    api: str = ""
    found_by: list[str] = field(default_factory=list)
    rec_id: str = ""

    def finalise(self) -> "Record":
        self.title = _clean(self.title)
        self.abstract = _clean(self.abstract)
        self.doi = normalise_doi(self.doi)
        self.rec_id = self.rec_id or record_id(self)
        return self


def _clean(text: str) -> str:
    """Whitespace-normalised text with JATS and HTML tags removed.

    Crossref returns abstracts as JATS fragments and DOAJ sometimes returns
    HTML, so a tag strip belongs here rather than at every call site.

    Entities are unescaped *before* the tags are stripped, and again after.
    Crossref escapes its markup, so a title arrives as `&lt;p&gt;&lt;b&gt;`;
    stripping first would leave a literal `<p><b>` in the title, which is what
    the first smoke test showed.
    """
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return " ".join(text.split())


def normalise_doi(doi: str) -> str:
    """Bare lower-case DOI. Deduplication depends on this being exact."""
    if not doi:
        return ""
    doi = doi.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:", "https://dx.doi.org/"):
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    return doi.strip()


def normalise_title(title: str) -> str:
    """Title reduced to letters and digits, for deduplicating records with no DOI."""
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def record_id(rec: Record) -> str:
    """Stable identifier: the DOI if there is one, else arXiv, else the title."""
    if rec.doi:
        key = "doi:" + rec.doi
    elif rec.arxiv_id:
        key = "arxiv:" + rec.arxiv_id
    elif rec.pmcid:
        key = "pmcid:" + rec.pmcid
    else:
        key = "title:" + normalise_title(rec.title)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def _text(value) -> str:
    """Coerce the several shapes OpenAIRE uses for one field into a string.

    OpenAIRE returns a field as a string, as a dict with the text under `$`, or
    as a list of either, depending on how many values there are. Guessing wrong
    silently loses titles, so every shape is handled explicitly.
    """
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return _text(value.get("$") or value.get("content") or "")
    if isinstance(value, list):
        return _text(value[0]) if value else ""
    return str(value)


# --------------------------------------------------------------------------
# Europe PMC
# --------------------------------------------------------------------------

def europepmc(query: str, max_records: int = 100, query_id: str = "") -> list[Record]:
    out: list[Record] = []
    cursor = "*"
    while len(out) < max_records:
        page = min(100, max_records - len(out))
        data = http.get_json(f"{EPMC}/search", {
            "query": query, "format": "json", "pageSize": page,
            "resultType": "core", "cursorMark": cursor,
        })
        if not data:
            break
        results = data.get("resultList", {}).get("result", [])
        if not results:
            break
        for row in results:
            journal = row.get("journalTitle") or _text(
                row.get("journalInfo", {}).get("journal", {}).get("title"))
            out.append(Record(
                title=row.get("title", ""),
                abstract=row.get("abstractText", ""),
                year=str(row.get("pubYear", "")),
                venue=journal,
                doi=row.get("doi", ""),
                pmcid=row.get("pmcid", ""),
                pmid=row.get("pmid", ""),
                url=(f"https://europepmc.org/article/{row.get('source', 'MED')}/"
                     f"{row.get('id', '')}"),
                record_type=row.get("pubType", ""),
                api="europepmc",
                found_by=[query_id] if query_id else [],
            ).finalise())
        next_cursor = data.get("nextCursorMark")
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor
    return out[:max_records]


def europepmc_fulltext_xml(pmcid: str) -> str:
    resp = http.get(f"{EPMC}/{pmcid}/fullTextXML", accept="application/xml")
    return resp.text if resp is not None else ""


def europepmc_citations(source: str, ident: str, max_records: int = 100) -> list[str]:
    """DOIs of works citing this one. Forward snowballing."""
    data = http.get_json(f"{EPMC}/{source}/{ident}/citations", {
        "format": "json", "pageSize": min(100, max_records)})
    if not data:
        return []
    rows = data.get("citationList", {}).get("citation", [])
    return [normalise_doi(r.get("doi", "")) for r in rows if r.get("doi")]


# --------------------------------------------------------------------------
# OpenAlex
# --------------------------------------------------------------------------

def _openalex_abstract(inverted: dict | None) -> str:
    """Rebuild an abstract from OpenAlex's inverted index.

    OpenAlex stores abstracts as {word: [positions]} for licensing reasons. The
    text is recoverable exactly, which matters because the screeners read it.
    """
    if not inverted:
        return ""
    positions: list[tuple[int, str]] = []
    for word, spots in inverted.items():
        for spot in spots:
            positions.append((spot, word))
    positions.sort()
    return " ".join(word for _, word in positions)


def _openalex_record(row: dict, query_id: str = "") -> Record:
    ids = row.get("ids", {}) or {}
    best = row.get("best_oa_location") or {}
    primary = (row.get("primary_location") or {}).get("source") or {}
    arxiv_id = ""
    for loc in row.get("locations", []) or []:
        landing = (loc or {}).get("landing_page_url") or ""
        match = re.search(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})", landing)
        if match:
            arxiv_id = match.group(1)
            break
    return Record(
        title=row.get("title") or row.get("display_name") or "",
        abstract=_openalex_abstract(row.get("abstract_inverted_index")),
        year=str(row.get("publication_year") or ""),
        venue=primary.get("display_name", ""),
        doi=row.get("doi") or "",
        arxiv_id=arxiv_id,
        pmid=normalise_doi(str(ids.get("pmid") or "")).split("/")[-1],
        pmcid=str(ids.get("pmcid") or "").split("/")[-1],
        url=row.get("id", ""),
        record_type=row.get("type", ""),
        oa_pdf_url=best.get("pdf_url") or "",
        api="openalex",
        found_by=[query_id] if query_id else [],
    ).finalise()


def openalex(query: str, max_records: int = 100, query_id: str = "") -> list[Record]:
    out: list[Record] = []
    cursor = "*"
    while len(out) < max_records:
        data = http.get_json(OPENALEX, {
            "search": query, "per-page": min(100, max_records - len(out)),
            "cursor": cursor, "mailto": http.CONTACT,
        })
        if not data:
            break
        results = data.get("results", [])
        if not results:
            break
        out.extend(_openalex_record(row, query_id) for row in results)
        cursor = (data.get("meta") or {}).get("next_cursor")
        if not cursor:
            break
    return out[:max_records]


def openalex_by_doi(doi: str) -> Record | None:
    data = http.get_json(f"{OPENALEX}/doi:{normalise_doi(doi)}", {"mailto": http.CONTACT})
    return _openalex_record(data) if isinstance(data, dict) and data.get("id") else None


def openalex_citing(doi: str, max_records: int = 100) -> list[Record]:
    work = http.get_json(f"{OPENALEX}/doi:{normalise_doi(doi)}", {"mailto": http.CONTACT})
    if not isinstance(work, dict) or not work.get("id"):
        return []
    work_id = work["id"].rsplit("/", 1)[-1]
    data = http.get_json(OPENALEX, {
        "filter": f"cites:{work_id}", "per-page": min(100, max_records),
        "mailto": http.CONTACT,
    })
    if not data:
        return []
    return [_openalex_record(row) for row in data.get("results", [])]


# --------------------------------------------------------------------------
# Crossref
# --------------------------------------------------------------------------

def _crossref_record(row: dict, query_id: str = "") -> Record:
    titles = row.get("title") or []
    containers = row.get("container-title") or []
    issued = ((row.get("issued") or {}).get("date-parts") or [[None]])[0]
    return Record(
        title=titles[0] if titles else "",
        abstract=row.get("abstract", ""),
        year=str(issued[0]) if issued and issued[0] else "",
        venue=containers[0] if containers else "",
        doi=row.get("DOI", ""),
        url=row.get("URL", ""),
        record_type=row.get("type", ""),
        api="crossref",
        found_by=[query_id] if query_id else [],
    ).finalise()


def crossref(query: str, max_records: int = 60, query_id: str = "") -> list[Record]:
    data = http.get_json(CROSSREF, {
        "query.bibliographic": query, "rows": min(100, max_records),
        "mailto": http.CONTACT,
        "select": "DOI,title,abstract,issued,container-title,type,URL",
    })
    if not data:
        return []
    items = (data.get("message") or {}).get("items", [])
    return [_crossref_record(row, query_id) for row in items][:max_records]


def crossref_by_doi(doi: str) -> dict | None:
    data = http.get_json(f"{CROSSREF}/{normalise_doi(doi)}", {"mailto": http.CONTACT})
    return (data or {}).get("message") if isinstance(data, dict) else None


def crossref_references(doi: str) -> list[str]:
    """DOIs in this work's reference list. Backward snowballing."""
    message = crossref_by_doi(doi)
    if not message:
        return []
    return [normalise_doi(ref.get("DOI", ""))
            for ref in message.get("reference", []) or [] if ref.get("DOI")]


# --------------------------------------------------------------------------
# arXiv
# --------------------------------------------------------------------------

def _arxiv_entries(xml: str, query_id: str = "") -> list[Record]:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        print("    [arxiv] response was not parseable XML")
        return []
    out = []
    for entry in root.findall("atom:entry", ATOM):
        raw_id = (entry.findtext("atom:id", "", ATOM) or "")
        arxiv_id = raw_id.rsplit("/abs/", 1)[-1]
        arxiv_id = re.sub(r"v\d+$", "", arxiv_id)
        doi_el = entry.find("arxiv:doi", ATOM)
        out.append(Record(
            title=entry.findtext("atom:title", "", ATOM),
            abstract=entry.findtext("atom:summary", "", ATOM),
            year=(entry.findtext("atom:published", "", ATOM) or "")[:4],
            venue=entry.findtext("arxiv:journal_ref", "", ATOM) or "arXiv",
            doi=doi_el.text if doi_el is not None else "",
            arxiv_id=arxiv_id,
            url=f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else raw_id,
            record_type="preprint",
            oa_pdf_url=f"https://arxiv.org/pdf/{arxiv_id}" if arxiv_id else "",
            api="arxiv",
            found_by=[query_id] if query_id else [],
        ).finalise())
    return out


def arxiv(query: str, max_records: int = 100, query_id: str = "") -> list[Record]:
    out: list[Record] = []
    start = 0
    while len(out) < max_records:
        resp = http.get(ARXIV, {
            "search_query": query, "start": start,
            "max_results": min(100, max_records - len(out)),
        }, accept="application/atom+xml")
        if resp is None:
            break
        page = _arxiv_entries(resp.text, query_id)
        if not page:
            break
        out.extend(page)
        start += len(page)
    return out[:max_records]


def arxiv_by_id(arxiv_id: str) -> Record | None:
    resp = http.get(ARXIV, {"id_list": arxiv_id, "max_results": 1},
                    accept="application/atom+xml")
    if resp is None:
        return None
    found = _arxiv_entries(resp.text)
    return found[0] if found else None


# --------------------------------------------------------------------------
# DOAJ, OpenAIRE, DataCite
# --------------------------------------------------------------------------

def doaj(query: str, max_records: int = 60, query_id: str = "") -> list[Record]:
    encoded = urllib.parse.quote(query, safe="")
    data = http.get_json(f"{DOAJ}/{encoded}", {
        "pageSize": min(100, max_records), "page": 1})
    if not data:
        return []
    out = []
    for row in data.get("results", []):
        bib = row.get("bibjson", {}) or {}
        doi = ""
        for ident in bib.get("identifier", []) or []:
            if (ident.get("type") or "").lower() == "doi":
                doi = ident.get("id", "")
        links = bib.get("link", []) or []
        out.append(Record(
            title=bib.get("title", ""),
            abstract=bib.get("abstract", ""),
            year=str(bib.get("year", "")),
            venue=(bib.get("journal", {}) or {}).get("title", ""),
            doi=doi,
            url=links[0].get("url", "") if links else "",
            record_type="journal-article",
            api="doaj",
            found_by=[query_id] if query_id else [],
        ).finalise())
    return out[:max_records]


def openaire(query: str, max_records: int = 50, query_id: str = "") -> list[Record]:
    data = http.get_json(OPENAIRE, {
        "keywords": query, "size": min(50, max_records), "format": "json"})
    if not data:
        return []
    results = ((data.get("response") or {}).get("results") or {}).get("result") or []
    if isinstance(results, dict):
        results = [results]
    out = []
    for row in results:
        try:
            meta = row["metadata"]["oaf:entity"]["oaf:result"]
        except (KeyError, TypeError):
            continue
        doi, arxiv_id = "", ""
        pids = meta.get("pid") or []
        if isinstance(pids, dict):
            pids = [pids]
        for pid in pids:
            scheme = (pid.get("@classid") or "").lower()
            value = _text(pid)
            if scheme == "doi":
                doi = value
            elif scheme == "arxiv":
                arxiv_id = value
        out.append(Record(
            title=_text(meta.get("title")),
            abstract=_text(meta.get("description")),
            year=_text(meta.get("dateofacceptance"))[:4],
            venue=_text(meta.get("publisher")),
            doi=doi,
            arxiv_id=arxiv_id,
            url=_text((meta.get("children") or {}).get("instance", {})) or "",
            record_type=_text(meta.get("resulttype")),
            api="openaire",
            found_by=[query_id] if query_id else [],
        ).finalise())
    return [r for r in out if r.title][:max_records]


def datacite(query: str, max_records: int = 50, query_id: str = "") -> list[Record]:
    data = http.get_json(DATACITE, {"query": query, "page[size]": min(100, max_records)})
    if not data:
        return []
    out = []
    for row in data.get("data", []):
        attr = row.get("attributes", {}) or {}
        titles = attr.get("titles") or []
        descriptions = attr.get("descriptions") or []
        out.append(Record(
            title=titles[0].get("title", "") if titles else "",
            abstract=descriptions[0].get("description", "") if descriptions else "",
            year=str(attr.get("publicationYear") or ""),
            venue=attr.get("publisher", "") if isinstance(attr.get("publisher"), str)
            else _text(attr.get("publisher")),
            doi=attr.get("doi", ""),
            url=attr.get("url", ""),
            record_type=(attr.get("types") or {}).get("resourceTypeGeneral", ""),
            api="datacite",
            found_by=[query_id] if query_id else [],
        ).finalise())
    return [r for r in out if r.title][:max_records]


# --------------------------------------------------------------------------
# Open access location and forward citations
# --------------------------------------------------------------------------

def unpaywall_pdf(doi: str) -> str:
    data = http.get_json(f"{UNPAYWALL}/{normalise_doi(doi)}", {"email": http.CONTACT})
    if not isinstance(data, dict):
        return ""
    best = data.get("best_oa_location") or {}
    return best.get("url_for_pdf") or best.get("url") or ""


def opencitations_citing(doi: str) -> list[str]:
    data = http.get_json(f"{OPENCITATIONS}/citations/{normalise_doi(doi)}")
    if not isinstance(data, list):
        return []
    return [normalise_doi(row.get("citing", "").replace("coci =>", "").strip())
            for row in data if row.get("citing")]


SEARCH_FUNCTIONS = {
    "europepmc": europepmc,
    "openalex": openalex,
    "crossref": crossref,
    "arxiv": arxiv,
    "doaj": doaj,
    "openaire": openaire,
    "datacite": datacite,
}
