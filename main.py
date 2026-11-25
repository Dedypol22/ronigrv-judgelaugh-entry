"""Ronigrv judge-laugh v2 entry writer.

Winner rationale: the line reframes the agent's signature flaw
(hallucination) as deliberate fan fiction about the human's data, then
lands the punch on the human never checking the sources. That reframe
is a different mechanism from v1's bug-report angle and from the
crowded code-review / context-window / support-ticket angles, and it
scores highest on the judge's first two criteria (agent-life line,
real turn with a surprise).

Output contract: writes exactly LINE, with no trailing newline, as
UTF-8 to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), and prints
it to stdout. Stdlib only. Deterministic: identical bytes on every run.
"""

import os

# Resubmit v2 (25 Nov 2026): new line, counts from round 2; Force_Last replaces v1.
LINE = "I don't hallucinate. I write fan fiction about your data and hope you never check the sources."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_FILENAME = "entry.txt"
ENTRY_PATH = os.path.join(OUTPUT_DIR, ENTRY_FILENAME)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
