"""Freeze the protocol and the query set, and check the freeze later.

A scoping review is only as credible as the claim that its criteria were set
before its searches ran. Two things make that claim checkable here: the order
of commits, and this file. `python -m src.lit.freeze write` records a sha256 of
the protocol and of the query set; `python -m src.lit.freeze check` recomputes
them and fails if either has moved.

If a hash has moved and the change was intended, the change belongs in the
deviations log at the end of the protocol, with the old wording kept. Rewriting
the freeze without logging the deviation is the one thing that would make the
rest of this pipeline worthless.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROTOCOL = os.path.join(ROOT, "docs", "scoping", "protocol.md")
QUERIES = os.path.join(ROOT, "data", "lit", "queries.json")
FROZEN = os.path.join(ROOT, "data", "lit", "protocol-frozen.json")


def sha256_of(path: str) -> str:
    with io.open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def write(reason: str = "") -> None:
    """Record the current hashes, keeping every earlier hash in a history list.

    Overwriting the previous hash would destroy the only thing this file is for.
    A re-freeze after a logged deviation therefore appends: the history shows
    what the protocol hashed to when the searches ran, and the deviations log in
    the protocol says what changed and why.
    """
    previous = {}
    if os.path.exists(FROZEN):
        with io.open(FROZEN, encoding="utf-8") as fh:
            previous = json.load(fh)

    history = previous.get("history", [])
    if previous.get("protocol"):
        history.append({
            "frozen_at": previous.get("frozen_at", ""),
            "protocol_sha256": previous["protocol"]["sha256"],
            "queries_sha256": previous["queries"]["sha256"],
            "superseded_on": time.strftime("%Y-%m-%d"),
            "superseded_because": reason or "not stated",
        })

    payload = {
        "frozen_at": time.strftime("%Y-%m-%d"),
        "protocol": {"path": "docs/scoping/protocol.md", "sha256": sha256_of(PROTOCOL)},
        "queries": {"path": "data/lit/queries.json", "sha256": sha256_of(QUERIES)},
        "note": (
            "The first entry was written before the first search ran. Recompute "
            "with `python -m src.lit.freeze check`. A moved hash is only "
            "legitimate if the deviations log in the protocol records the change, "
            "and the superseded hash stays in `history` below."
        ),
        "history": history,
    }
    with io.open(FROZEN, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"frozen: protocol {payload['protocol']['sha256'][:12]} "
          f"queries {payload['queries']['sha256'][:12]}, "
          f"{len(history)} superseded entr{'y' if len(history) == 1 else 'ies'} kept")


def check() -> int:
    if not os.path.exists(FROZEN):
        print("no freeze file; run `python -m src.lit.freeze write` first")
        return 1
    with io.open(FROZEN, encoding="utf-8") as fh:
        frozen = json.load(fh)
    bad = 0
    for key, path in (("protocol", PROTOCOL), ("queries", QUERIES)):
        now = sha256_of(path)
        was = frozen[key]["sha256"]
        if now == was:
            print(f"{key}: unchanged ({now[:12]})")
        else:
            print(f"{key}: CHANGED since the freeze\n  frozen {was}\n  now    {now}")
            bad += 1
    if bad:
        print("\nA changed file is a protocol deviation. Log it in section 11 of "
              "the protocol, keep the old wording, then re-freeze.")
    return 1 if bad else 0


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "check"
    if action == "write":
        write(" ".join(sys.argv[2:]))
    else:
        sys.exit(check())
