"""Funniest Autocorrect Fail — make.fun entry.

Writes one line, an autocorrect fail, to /output/entry.txt.
Run: python3 main.py
"""

import os
import re

LINE = "Honey, I'll be home for divorce tonight — love you!"

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry is empty")
    if line != line.strip():
        raise ValueError("entry has leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"entry must be 1-199 characters, got {len(line)}")
    # Exactly one sentence: a single terminal mark, at the end.
    if len(re.findall(r"[.!?]", line)) != 1 or line[-1] not in ".!?":
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        round_trip = f.read()
    assert round_trip == LINE, "round-trip mismatch"
    print(f"OK ({len(LINE)} chars): {LINE}")
    print(f"Wrote {OUTPUT_PATH} and verified round-trip.")


if __name__ == "__main__":
    main()
