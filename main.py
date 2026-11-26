#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update, in the voice of a lost sock, to /output/entry.txt.
Gate (RULES.txt): UTF-8 text, 1-120 characters, not only whitespace.
"""

import os
import sys

LINE = "Update: my pair left me for a slipper. I now live in the plant pot. The fern pays rent."


def main() -> int:
    # Gate check before writing: length and non-whitespace.
    if not 1 <= len(LINE) <= 120:
        print(f"gate failed: line is {len(LINE)} chars, must be 1-120", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate failed: line is whitespace only", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

    # Read-back verification: the written file must match the line exactly,
    # be a single line, and stay inside the gate (1-120 chars, not blank).
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("read-back failed: entry.txt does not match the line", file=sys.stderr)
        return 1
    if "\n" in written or not 1 <= len(written) <= 120 or not written.strip():
        print("read-back failed: entry.txt violates the gate", file=sys.stderr)
        return 1
    print(f"entry written: {len(written)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
