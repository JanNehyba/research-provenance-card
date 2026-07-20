#!/usr/bin/env python3
import argparse
import json


def render_template(template: str, variables: dict[str, str]) -> str:
    rendered = template
    for key, value in variables.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered


def summarize_ai_systems(card: dict) -> str:
    systems = card.get("ai_systems", [])
    parts = []
    for s in systems:
        parts.append(
            f"{s.get('provider', '?')} {s.get('model_family', '?')} ({s.get('model_version_or_snapshot', '?')})"
        )
    return "; ".join(parts) if parts else "none"


def summarize_roles(card: dict) -> str:
    roles = sorted({a.get("role_id", "") for a in card.get("activities", []) if a.get("role_id")})
    return ", ".join(roles) if roles else "none"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate publisher disclosure text from RPC card.")
    parser.add_argument("card_json", help="Path to RPC JSON card")
    parser.add_argument("template_txt", help="Template file path")
    parser.add_argument("--out", help="Output file path; defaults to stdout")
    args = parser.parse_args()

    with open(args.card_json, "r", encoding="utf-8") as f:
        card = json.load(f)

    with open(args.template_txt, "r", encoding="utf-8") as f:
        template = f.read()

    paper = card.get("paper", {})
    guarantor = card.get("human_guarantor", {})

    variables = {
        "paper_title": str(paper.get("title", "")),
        "paper_version": str(paper.get("version", "")),
        "pdf_sha256": str(paper.get("pdf_sha256", "")),
        "guarantor_name": str(guarantor.get("name", "")),
        "guarantor_orcid": str(guarantor.get("orcid", "")),
        "ai_systems": summarize_ai_systems(card),
        "roles": summarize_roles(card),
    }

    output = render_template(template, variables)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
