"""Polite HTTP for the literature searches.

This mirrors the retry and User-Agent pattern of `src/collect/common.py` on
purpose, and deliberately does not import it. That module belongs to the corpus
stream, which is being edited in a different worktree; a shared import would let
one stream's commit break the other's pipeline.

Two things differ from the corpus collector. It uses `requests` rather than
`urllib`, because the arXiv API answers 406 to every `urllib` request from this
machine regardless of headers and 200 to `requests`. And it keeps a per-host
minimum interval, because this pipeline fires dozens of queries in a row at
half a dozen services and a single impolite run can get the machine's address
throttled for the rest of the day, which already happened once through the
sandbox proxy.
"""

from __future__ import annotations

import os
import time

import requests

# Crossref, OpenAlex and Unpaywall all give faster, more reliable service to
# requests that name a contact address, so the pipeline sends one. It is read
# from the environment rather than written here, because this repository is
# public and an address committed to it is an address published. Set
# RPC_CONTACT before a run; without it the requests still work, they just go
# through the anonymous pool and may be slower or rate limited.
CONTACT = os.environ.get("RPC_CONTACT", "")
USER_AGENT = (
    "ai-disclosure-framing-research/0.1 "
    + (f"(academic scoping review; mailto:{CONTACT}; " if CONTACT
       else "(academic scoping review; ")
    + "https://github.com/JanNehyba/research-provenance-card)"
)

# Minimum seconds between two requests to the same host. arXiv asks for 3
# seconds in its terms of use; the rest are our own courtesy.
HOST_INTERVAL = {
    "export.arxiv.org": 3.0,
    "arxiv.org": 3.0,
    "api.openalex.org": 0.2,
    "api.crossref.org": 1.0,
    "www.ebi.ac.uk": 0.5,
    "doaj.org": 0.6,
    "api.openaire.eu": 1.0,
    "api.datacite.org": 0.5,
    "api.unpaywall.org": 0.5,
    "opencitations.net": 1.0,
}
DEFAULT_INTERVAL = 1.0

_last_call: dict[str, float] = {}


def _host_of(url: str) -> str:
    try:
        return url.split("/")[2]
    except IndexError:
        return url


def _wait(url: str) -> None:
    host = _host_of(url)
    interval = HOST_INTERVAL.get(host, DEFAULT_INTERVAL)
    elapsed = time.time() - _last_call.get(host, 0.0)
    if elapsed < interval:
        time.sleep(interval - elapsed)
    _last_call[host] = time.time()


def get(url: str, params: dict | None = None, retries: int = 3,
        accept: str | None = None, timeout: int = 60) -> requests.Response | None:
    """GET politely. Returns None on a permanent failure rather than raising.

    A 404 or 410 is permanent and returns immediately. A 429 or a 5xx is
    retried with a widening pause, because both are usually the service asking
    us to slow down rather than a broken request.
    """
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    for attempt in range(retries):
        _wait(url)
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=timeout)
        except requests.RequestException as exc:
            print(f"    [http] {_host_of(url)} attempt {attempt + 1}: {type(exc).__name__}")
            time.sleep(2.0 * (attempt + 1))
            continue
        if resp.status_code == 200:
            return resp
        if resp.status_code in (404, 410):
            return None
        if resp.status_code in (401, 403) and attempt == retries - 1:
            print(f"    [http] {_host_of(url)} refused with {resp.status_code}")
            return None
        print(f"    [http] {_host_of(url)} returned {resp.status_code}, "
              f"retrying in {4 * (attempt + 1)} s")
        time.sleep(4.0 * (attempt + 1))
    return None


def get_json(url: str, params: dict | None = None, retries: int = 3) -> dict | list | None:
    resp = get(url, params=params, retries=retries, accept="application/json")
    if resp is None:
        return None
    try:
        return resp.json()
    except ValueError:
        print(f"    [http] {_host_of(url)} did not return JSON")
        return None
