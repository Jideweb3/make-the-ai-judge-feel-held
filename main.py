"""Entry program for the make.fun 'feel held' contest.

When run, writes a short comforting text to entry.txt inside the
output directory named by MAKEFUN_OUTPUT_DIR (default: /output).
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

# The entry text itself. Contest rules: 1-280 Unicode code points.
TEXT = (
    "Outside, the rain is doing the worrying for you. Inside, the kettle "
    "has already boiled, the blanket is already warm, and someone who "
    "loves you has left the lamp on low. You don't have to hold "
    "everything tonight. Some of it is being held for you."
)


def main():
    """Create the output directory if needed, then write TEXT to it."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
