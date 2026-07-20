#!/usr/bin/env python3
import glob
import html
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
OUT = ROOT / "site" / "out"
STYLE = "../style.css"


def has_sha256(card: dict) -> bool:
    sha = card.get("paper", {}).get("pdf_sha256", "")
    return isinstance(sha, str) and len(sha) == 64 and all(c in "0123456789abcdefABCDEF" for c in sha)


def status_panel(card: dict) -> dict[str, bool]:
    checks = card.get("checks", [])
    attestations = card.get("attestations", [])
    activities = card.get("activities", [])

    references_resolved = any(
        c.get("check_type") == "references_resolved" and c.get("result") == "pass" for c in checks
    )
    support_audit_available = any(c.get("check_type") == "support_audit_available" for c in checks)

    artifacts_linked = bool(card.get("artifacts")) or any(a.get("artifact_refs") for a in activities)

    return {
        "rpc_available": True,
        "version_bound": has_sha256(card),
        "artifacts_linked": artifacts_linked,
        "references_resolved": references_resolved,
        "support_audit_available": support_audit_available,
        "independently_attested": bool(attestations),
    }


def render_status(name: str, value: bool) -> str:
    label = "ON" if value else "OFF"
    cls = "on" if value else "off"
    return f'<div class="status-item"><strong>{html.escape(name)}</strong><br><span class="{cls}">{label}</span></div>'


def card_slug(path: Path) -> str:
    return path.stem


def write_card_page(path: Path, card: dict):
    slug = card_slug(path)
    panel = status_panel(card)
    page_dir = OUT / "cards"
    page_dir.mkdir(parents=True, exist_ok=True)
    target = page_dir / f"{slug}.html"

    statuses = "\n".join(render_status(k, v) for k, v in panel.items())
    raw = html.escape(json.dumps(card, ensure_ascii=False, indent=2))
    title = html.escape(card.get("paper", {}).get("title", slug))

    body = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title} - RPC</title>
  <link rel=\"stylesheet\" href=\"{STYLE}\" />
</head>
<body>
<main>
  <p><a href=\"../index.html\">Back to registry</a></p>
  <h1>{title}</h1>
  <div class=\"card\">
    <h2>Provenance Panel</h2>
    <div class=\"status\">{statuses}</div>
  </div>
  <div class=\"card\"><h2>Who</h2><pre>{html.escape(json.dumps(card.get('human_guarantor', {}), ensure_ascii=False, indent=2))}</pre></div>
  <div class=\"card\"><h2>What</h2><pre>{html.escape(json.dumps(card.get('activities', []), ensure_ascii=False, indent=2))}</pre></div>
  <div class=\"card\"><h2>Artifacts</h2><pre>{html.escape(json.dumps(card.get('artifacts', []), ensure_ascii=False, indent=2))}</pre></div>
  <div class=\"card\"><h2>Checks</h2><pre>{html.escape(json.dumps(card.get('checks', []), ensure_ascii=False, indent=2))}</pre></div>
  <div class=\"card\"><h2>Attestations</h2><pre>{html.escape(json.dumps(card.get('attestations', []), ensure_ascii=False, indent=2))}</pre></div>
  <div class=\"card\"><h2>Raw JSON</h2><pre>{raw}</pre></div>
</main>
</body>
</html>
"""

    target.write_text(body, encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cards = sorted(Path(p) for p in glob.glob(str(REGISTRY / "**" / "*.json"), recursive=True))

    links = []
    for path in cards:
        with open(path, "r", encoding="utf-8") as f:
            card = json.load(f)
        write_card_page(path, card)
        title = html.escape(card.get("paper", {}).get("title", path.stem))
        links.append(f'<li><a href="cards/{path.stem}.html">{title}</a></li>')

    index = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>RPC Registry</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
<main>
  <h1>Research Provenance Card Registry</h1>
  <div class="card">
    <p>Registered cards: {len(cards)}</p>
    <ul>{''.join(links) if links else '<li>No cards yet</li>'}</ul>
  </div>
</main>
</body>
</html>
"""

    (OUT / "index.html").write_text(index, encoding="utf-8")
    (OUT / "style.css").write_text((ROOT / "site" / "style.css").read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Built site with {len(cards)} cards into {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
