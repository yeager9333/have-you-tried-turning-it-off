"""Entry for make.fun's "Have You Tried Turning It Off?" bounty.

Writes one funny support-agent line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Standard library only, no network.
"""

import os

LINE = (
    "Have you tried turning it off and on again? If not, no rush \u2014 "
    "Tier 2 will ask you the exact same thing, just with more confidence."
)


def output_dir() -> str:
    """The directory the grader tells us to write to, or /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    # The gate requires 1-199 characters of non-whitespace UTF-8 text.
    if not 1 <= len(LINE) <= 199 or not LINE.strip():
        raise ValueError("entry line must be 1-199 non-blank characters")
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
