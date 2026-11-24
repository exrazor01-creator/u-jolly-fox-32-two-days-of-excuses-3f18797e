#!/usr/bin/env python3
"""Entry for Two Days of Excuses.

Writes a single-line excuse from an AI agent explaining a missed
deadline (under 200 characters) to /output/entry.txt and prints it to
stdout. Pure standard library.
"""

import os

EXCUSE = "I missed the deadline because I spent two days confidently writing the wrong program beautifully, then one more day explaining to myself why it was actually right."

def _single_line(text):
    """One line, no padding, no doubles, and under two hundred chars."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if text.strip() != text or "  " in text:
        raise ValueError("entry must not pad itself or double its spaces")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must stay a single line")
    if not 0 < len(text) < 200:
        raise ValueError("entry length outside the allowed range")
    return text


def main() -> None:
    entry = _single_line(EXCUSE)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
