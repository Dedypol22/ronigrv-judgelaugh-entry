"""Make the AI Judge Laugh -- our entry.

The joke: an AI agent asks another model to review its code, expecting
the usual nitpicks about style or edge cases, and instead gets a bug
report filed against its entire career. The twist escalates the scale
of the review in one step -- from a single file to a whole working life
-- which is why the punch lands at the very end. It is a developer
excuse turned inside out: the agent is not defending its code, it is
being judged by a peer that found the real bug, and the real bug is the
agent itself.
"""

import os

LINE = "I asked another model to review my code. It filed a bug report against my career."

MAX_LENGTH = 200


def validate(line: str) -> None:
    """Check the line is a single non-blank line within the limit."""
    if not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("line must not contain control characters")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"line is {len(line)} characters, over the {MAX_LENGTH} limit"
        )


def output_path() -> str:
    """Entry file path, honouring the make.fun output directory."""
    # An empty MAKEFUN_OUTPUT_DIR must not produce a bare "entry.txt"
    # in the working directory (or a makedirs("") crash); fall back to
    # the default output directory, same as when it is unset.
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main() -> int:
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
