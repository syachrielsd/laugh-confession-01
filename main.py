#!/usr/bin/env python3
"""Write one funny secret confession from an AI agent to entry.txt.

The confession: an agent that lost the user's name to its context window
and has been covering the gap with a generic honorific. The punch word
('boss') is the last word, so the twist lands on the final beat.
"""
import os

LINE = "I forgot your name four messages in, so I've been calling you 'boss'."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = LINE.strip()
    assert "\n" not in line and 1 <= len(line) <= 200, "entry must be one line of 1-200 chars"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
