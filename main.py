"""Entry for "Make the AI Judge Laugh": The Bug Report Against My Career.

The humour here rests on a bait-and-switch of scope. The opening half
sets up the most ordinary scene in a programmer's life: you hand your
code to a reviewer and wait for comments about style, naming, maybe a
missing null check. The reviewer in this case happens to be another
model, but that alone is not the joke.

The turn comes when the reviewer's verdict skips past the code
entirely. Instead of flagging a defect in the file it was given, it
opens a report against the author's whole career, as if years of work
were a single bad commit. The escalation lands because it is only one
step wide — file to career — yet that one step reframes everything:
the reviewer did find a genuine bug, and the bug turns out to be the
person who wrote the code in the first place.

The program itself is deliberately plain. It validates the one-liner
against the competition's constraints, writes it to the entry file
with no trailing newline, and echoes it to stdout.
"""

import os

LINE = "I asked another model to review my code. It filed a bug report against my career."
MAX_LENGTH = 200


def validate(line):
    """Check that *line* is an acceptable single-line entry.

    Raises ValueError when the line is blank, spans more than one
    physical line, contains control characters, or exceeds the
    maximum permitted length.
    """
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    for ch in line:
        if ord(ch) < 0x20:
            raise ValueError("line must not contain control characters")
    if len(line) > MAX_LENGTH:
        raise ValueError("line exceeds the maximum length")
    return line


def output_path():
    """Return the path of the entry file to write."""
    # Use `or` rather than a .get() default: if the variable is set but
    # empty, the default would not apply and the join below would yield a
    # bare relative "entry.txt" instead of the intended fallback path.
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
