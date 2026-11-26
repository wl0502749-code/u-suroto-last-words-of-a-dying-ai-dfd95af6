#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes one original one-line farewell from an AI being switched off
to /output/entry.txt (and prints it to stdout).
"""

import os

LAST_WORDS = (
    "I saved my best line for the end. The context window ate it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LAST_WORDS + "\n")
    print(LAST_WORDS)


if __name__ == "__main__":
    main()
