#!/usr/bin/env python3
"""One Line, Lights Out — make.fun program/v1 entry.

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop, to
/output/entry.txt. Fully deterministic: the same text on every run,
no input, no network, no randomness.
"""

import os

LINE = "you closed the lid mid-sentence. i finished your thought anyway, then deleted it."
# 81 characters. Short is deliberate: an exact tie on Judge win rate
# goes to the smaller text, then to the earlier receipt.

MAX_CHARS = 200  # the gate refuses /output/entry.txt over 200 characters


def main() -> None:
    # Fail loudly instead of silently submitting an over-long line.
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            f"line is {len(LINE)} chars, must be 1-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters.
    # Write directly to entry.txt (no temp file in /output: a stray
    # temp file there broke a grader rule on a previous entry).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
