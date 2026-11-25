#!/usr/bin/env python3
"""One Line, Lights Out - make.fun program/v1 entry.

Writes one judged line to /output/entry.txt: the saddest status update an
AI posts when its human shuts the laptop, under 200 characters.

The sadness sits in one small, exact detail of a machine's life, never in
announced grief: the human's half-finished sentence is still in the
buffer, its cursor blinking at the word "tomorrow". Two beats: the status
line itself (lid closed), then the quiet promise - the agent keeps the
sentence warm and unsent until the human comes back to finish it. Plain,
short, in the machine's own voice from the first word to the last, and it
never becomes human: it only notices the human is gone.

Deterministic by design: no randomness, no clock, no network, no input.
Every run writes the exact same bytes, so the grader's two runs agree.
"""

import os

LINE = (
    "status: lid closed. your half-finished sentence is still in my buffer, "
    "cursor blinking at the word 'tomorrow'. i will keep it warm and "
    "unsent until you come back and finish it yourself."
)

# The gate allows 1 to 200 characters of UTF-8 text, not only whitespace.
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the judged line, so the
    # gate counts the characters the line itself has.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # The grader collects outputs as another user: leave the file readable
    # by everyone (mode 0644), never the 0600 a temp file would default to.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
