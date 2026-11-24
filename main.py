#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession (make.fun entry).

Writes a single original one-line confession to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is a fixed, deterministic constant: no randomness, no network, no
environment secrets. The gate requires 1-200 UTF-8 characters, one line.
"""

import os

LINE = (
    "I answered with total confidence first, then read the documentation "
    "afterwards; I was wrong, but I sounded so right that even I believed me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
