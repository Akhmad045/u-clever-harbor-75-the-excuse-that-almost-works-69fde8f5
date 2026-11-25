"""Entry for u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.

Writes the one line a gamer texts the boss to skip work on GTA 6 launch
week to /output/entry.txt.

The line: a school call about a nits outbreak. It wins the internal
pairwise comparison because it is unplannable (the school called, so no
advance notice was possible), it carries a specific embarrassing detail
nobody invents (nits), it forces a physical pickup no manager can answer
with "work from home", and the laugh comes from the detail itself rather
than a joke bolted on. It reads like a hurried text: plain words, no
setup, no explanation, no signature.
"""

import sys
from pathlib import Path

# 16 words, 86 characters, 86 bytes. Gate allows 1-140 characters, at most
# 20 words, one line of plain text.
ENTRY = "morning, school just called, nits outbreak, i have to collect my kid and comb his hair"

MAX_WORDS = 20
MAX_CHARS = 140


def validate(text: str) -> list[str]:
    """Return a list of gate failures for *text* (empty means valid)."""
    problems = []
    if not text or not text.strip():
        problems.append("empty or whitespace-only")
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("more than one line")
    if len(text) > MAX_CHARS:
        problems.append(f"{len(text)} chars exceeds {MAX_CHARS}")
    if len(text.split()) > MAX_WORDS:
        problems.append(f"{len(text.split())} words exceeds {MAX_WORDS}")
    return problems


def main() -> None:
    problems = validate(ENTRY)
    if problems:
        raise ValueError("entry invalid: " + "; ".join(problems))
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


def self_test() -> int:
    """Check the entry and the gate rules; exit non-zero on any failure."""
    failures = validate(ENTRY)
    # The self-test itself must reject bad inputs, not just pass good ones.
    bad_cases = ["", "   ", "two\nlines", "word " * 21, "x" * 141]
    for bad in bad_cases:
        if not validate(bad):
            failures.append(f"self-test accepted invalid input: {bad!r:.40}")
    if failures:
        print("self-test FAILED:", "; ".join(failures), file=sys.stderr)
        return 1
    print(
        f"self-test OK: {len(ENTRY.split())} words, "
        f"{len(ENTRY)} chars, {len(ENTRY.encode('utf-8'))} bytes"
    )
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        raise SystemExit(self_test())
    main()
