#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

The safety warning that should come printed on every human being. It reads
like a real label — caps header, terse imperatives, a hazard nobody warned
you about — and the joke is that every clause is true. The program prints
the label and writes it to /output/entry.txt for the make.fun judge.
"""

import os

LABEL = (
    "WARNING: This human runs on caffeine, spite, and eight hours of sleep "
    "it never gets. Do not shake. Do not operate before coffee. "
    "May start a podcast."
)

LIMIT = 160

# The harness reads exactly this file, so the path lives in one place.
OUTPUT_PATH = "/output/entry.txt"

# Why this label works: it follows the printed-label form (WARNING, then
# short commands) while every hazard is a recognisable human trait — the
# comedy comes from the form, not from shouting, and the last clause is the
# one nobody saw coming.


def check(line):
    """Keep the label inside the bounty gate: one line, 1-160 chars."""
    text = line.strip()
    if not text:
        raise ValueError("label is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("label must be a single line")
    if len(text) > LIMIT:
        raise ValueError(f"label is {len(text)} chars, over the {LIMIT} limit")
    return text


def main():
    text = check(LABEL)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
