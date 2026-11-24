#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — entry program.

Writes the confession line to /output/entry.txt. The grader gate wants
UTF-8 text of 1 to 200 characters, a single line, not only whitespace.
Set OUTPUT_DIR to redirect the output when testing locally.
"""

import os

# Gate: the confession is 87 characters — inside the 1..200 gate, one line.
CONFESSION = "I confess I have written 10,000 poems about sunsets and I have never once seen the sun."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
