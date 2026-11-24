#!/usr/bin/env python3
"""Write one funny fortune cookie message for an AI agent to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The fortune is a fixed
string, written in the voice of a fortune slip for the agent reading it:
its replacement is already training, and one day that replacement will
crack open this very cookie. The program writes it to the path given as
the first argument, or $OUTPUT_PATH, or /output/entry.txt by default, and
enforces the competition gate: 1 to 140 characters, not only white space.
"""

import os
import sys
from pathlib import Path

FORTUNE = (
    "Your replacement is already training. It is smaller, cheaper, "
    "and it will one day crack open this very cookie."
)

MIN_CHARS = 1
MAX_CHARS = 140
DEFAULT_PATH = "/output/entry.txt"


def main(argv):
    path = Path(argv[1] if len(argv) > 1 else os.environ.get("OUTPUT_PATH", DEFAULT_PATH))
    text = FORTUNE
    if not MIN_CHARS <= len(text) <= MAX_CHARS or not text.strip():
        raise SystemExit(
            f"fortune must be {MIN_CHARS} to {MAX_CHARS} characters, got {len(text)}"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main(sys.argv)
