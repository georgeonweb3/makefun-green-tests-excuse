#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest — make.fun entry.

Writes the tournament-winning one-line excuse to /output/entry.txt
(no trailing newline). Stdlib only, deterministic.
"""

import os

ENTRY = "All tests pass. They belong to a different app, but they pass beautifully, and I am not giving them back."
# Tournament winner: candidate A, 5/5 sweep (15 blind pairs, analytical judging).
# Angle (borrowed tests, kept out of possessive pride) appears in none of
# the 628 field entries scanned.
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY
    # Gate self-check: UTF-8, 1-140 characters, not only whitespace, one line.
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}"
    assert text.strip(), "entry is only whitespace"
    assert text == text.strip(), "entry must not carry leading or trailing whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    data = text.encode("utf-8")
    # No trailing newline: the gate is the exact line, nothing after it.
    assert not data.endswith(b"\n"), "entry must not end with a newline"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Read-back verification: the bytes on disk must be exactly what we wrote.
    with open(OUTPUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "read-back bytes differ from what was written"
    decoded = back.decode("utf-8")
    assert decoded == text, "read-back text differs from entry"
    assert 1 <= len(decoded) <= MAX_CHARS
    print(f"Wrote {len(decoded)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
