#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the cat's one-sentence excuse for knocking a glass off the
table to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, no network, no randomness.
"""
import os
import sys

ENTRY = (
    "The glass was empty, it was taunting me from the edge, and I only "
    "helped it complete its lifelong dream of flying."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text and not text.isspace()
    assert text.count(".") == 1 and text.endswith(".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
