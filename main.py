#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry writer.

Writes one original funny rant about an everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt (default ./output/).

Gate (sealed scorer): entry.txt must be UTF-8 text of 1 to 400
characters, not only white space. This program self-checks that gate
before exiting.
"""

import os
import sys

ENTRY = (
    "The office printer has one job and it does it the way a cat does "
    "fetch: it stares at you, jams on page two, then prints a perfect "
    "test page the second IT walks over. I have fed it paper and toner "
    "and it repays me by blinking 'PC LOAD LETTER' like that is a "
    "sentence a human wrote. I am not angry at the printer. I am angry "
    "at the printer's confidence. It has never once apologised, and it "
    "never will."
)

MAX_CHARS = 400


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Self-check the gate: re-read and verify length / non-blank.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    assert 1 <= len(written) <= MAX_CHARS, "gate: length out of range"
    assert written.strip(), "gate: entry is only whitespace"

    print(f"wrote {path} ({len(written)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
