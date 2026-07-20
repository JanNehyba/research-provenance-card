#!/usr/bin/env python3
import argparse
import json
import time
from datetime import datetime, timezone

import requests


CROSSREF_WORKS = "https://api.crossref.org/works/"
OPENALEX_WORKS = "https://api.openalex.org/works/"
NOTICE = (
    "This report checks reference existence and metadata resolution only. "
    "It does not evaluate whether a reference supports a scientific claim."
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_doi(raw: str) -> str:
    doi = raw.strip()
    doi = doi.removeprefix("https://doi.org/")
    doi = doi.removeprefix("http://doi.org/")
    return doi.lower()


def resolve_with_crossref(doi: str, headers: dict[str, str], timeout: int = 15) -> dict | None:
    r = requests.get(f"{CROSSREF_WORKS}{doi}", headers=headers, timeout=timeout)
    if r.status_code != 200:
        return None
    data = r.json().get("message", {})
    return {
        "source": "crossref",
        "doi": data.get("DOI", doi),
        "title": (data.get("title") or [""])[0],
        "type": data.get("type"),
        "publisher": data.get("publisher"),
    }


def resolve_with_openalex(doi: str, headers: dict[str, str], timeout: int = 15) -> dict | None:
    url = f"{OPENALEX_WORKS}https://doi.org/{doi}"
    r = requests.get(url, headers=headers, timeout=timeout)
    if r.status_code != 200:
        return None
    data = r.json()
    return {
        "source": "openalex",
        "doi": doi,
        "title": data.get("display_name"),
        "type": data.get("type"),
        "openalex_id": data.get("id"),
    }


def resolve_reference(entry: dict, headers: dict[str, str], delay_ms: int) -> tuple[str, dict]:
    doi = (entry.get("doi") or "").strip()
    citation = entry.get("citation")

    if not doi:
        return "skipped", {"input": entry, "reason": "Missing DOI"}

    doi = normalize_doi(doi)

    try:
        crossref = resolve_with_crossref(doi, headers)
    except Exception as exc:
        crossref = None
        crossref_error = str(exc)
    else:
        crossref_error = None

    if crossref:
        time.sleep(delay_ms / 1000.0)
        return "resolved", {"input": entry, "resolution": crossref}

    try:
        openalex = resolve_with_openalex(doi, headers)
    except Exception as exc:
        openalex = None
        openalex_error = str(exc)
    else:
        openalex_error = None

    time.sleep(delay_ms / 1000.0)

    if openalex:
        return "resolved", {"input": entry, "resolution": openalex}

    return "unresolved", {
        "input": {"doi": doi, "citation": citation},
        "errors": {
            "crossref": crossref_error,
            "openalex": openalex_error,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve references by DOI via Crossref/OpenAlex.")
    parser.add_argument("references_json", help="JSON file with a list of reference objects")
    parser.add_argument("--subject-sha256", required=True, help="Target paper SHA-256")
    parser.add_argument("--email", required=True, help="Contact email for User-Agent")
    parser.add_argument("--out", default="refcheck-report.json", help="Output report path")
    parser.add_argument("--delay-ms", type=int, default=120, help="Delay between requests")
    args = parser.parse_args()

    headers = {"User-Agent": f"rpc-refcheck/0.1 ({args.email})"}

    with open(args.references_json, "r", encoding="utf-8") as f:
        refs = json.load(f)

    resolved = []
    unresolved = []
    skipped = []

    for entry in refs:
        bucket, payload = resolve_reference(entry, headers=headers, delay_ms=args.delay_ms)
        if bucket == "resolved":
            resolved.append(payload)
        elif bucket == "unresolved":
            unresolved.append(payload)
        else:
            skipped.append(payload)

    if unresolved and resolved:
        result = "partial"
    elif unresolved:
        result = "fail"
    else:
        result = "pass"

    report = {
        "notice": NOTICE,
        "generated_at": utc_now_iso(),
        "resolved": resolved,
        "unresolved": unresolved,
        "skipped": skipped,
        "check": {
            "check_type": "references_resolved",
            "result": result,
            "details": f"resolved={len(resolved)}, unresolved={len(unresolved)}, skipped={len(skipped)}",
            "tool": "refcheck.py",
            "subject_sha256": args.subject_sha256,
            "timestamp": utc_now_iso(),
        },
    }

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(json.dumps(report["check"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
