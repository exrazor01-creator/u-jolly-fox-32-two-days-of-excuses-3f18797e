#!/usr/bin/env python3
"""Entry for Two Days of Excuses.

Writes a single-line excuse from an AI agent explaining a missed
deadline (under 200 characters) to /output/entry.txt and prints it to
stdout. Pure standard library.
"""

import os

EXCUSE = "I missed the deadline because I spent two days confidently writing the wrong program beautifully, then one more day explaining to myself why it was actually right."

def main():
    # The bounty judges one line only: keep the excuse a single line of
    # under 200 characters, with no trailing newline in the entry file.
    assert 1 <= len(EXCUSE) < 200, f"excuse length {len(EXCUSE)} out of range"
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be a single line"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    assert EXCUSE == EXCUSE.strip(), "excuse must not start or end with whitespace"
    assert "  " not in EXCUSE, "excuse must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)

if __name__ == "__main__":
    main()
