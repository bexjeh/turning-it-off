#!/usr/bin/env python3
"""Have You Tried Turning It Off? - make.fun entry.

Writes one funny line from a hopeless tech support agent to a desperate
customer, to entry.txt in the output directory.

The grader runs with a read-only working directory and only the output
directory writable, so the output path honours MAKEFUN_OUTPUT_DIR when it
is set and falls back to ./output otherwise. The output is deterministic:
the same line, byte for byte, on every run.
"""

import os

LINE = (
    "Good news, sir \u2014 your computer is already off, so we\u2019re halfway "
    "through turning it off and on again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
