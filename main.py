#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — writes one status update to /output/entry.txt."""

import os

LINE = "Status: single. Literally. My pair married a slipper. I'm the one in the plant pot, thriving."

OUTPUT = "/output/entry.txt"


def main():
    # Gate: UTF-8 text, 1-120 characters, single line, no trailing whitespace.
    line = LINE.strip()
    assert 1 <= len(line) <= 120, f"line must be 1-120 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line == line.strip(), "no leading/trailing whitespace allowed"
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(OUTPUT, 0o644)


if __name__ == "__main__":
    main()
