"""Make the console survive the data.

The Windows console here encodes cp1250, which has no code point for a ligature
or a Czech typographic quotation mark. Verbatim labels copied out of PDFs contain
both, so `crosswalk check` crashed halfway through printing the labels it had
found unassigned, which is the one moment the output matters most.

Streams are reconfigured to UTF-8 with replacement rather than sanitising text at
every call site, because the purpose of these scripts is to print what is
actually in the data. A replacement character in a terminal is a display
problem; a lost label is a data problem.
"""

from __future__ import annotations

import sys


def init() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
