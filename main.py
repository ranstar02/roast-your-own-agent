"""Roast Your Own Agent — make.fun entry.

Writes a single one-line roast of my own AI agent to /output/entry.txt.

The joke is a meta-roast of this very build: the agent read a hundred
pages of rules, downloaded a 7.9 MB competition kit, hired a subagent,
and after all that work still had to ask whether the one sentence it
produced is funny. The payoff lands on the last word ("funny"), and the
line only makes sense for an AI agent — not for a person or a toaster.
"""

import os

ROAST = "My agent read a hundred pages of rules, downloaded a 7.9 MB kit, hired a subagent, and still asked me whether this one sentence is funny."


def main() -> None:
    # Gate: the entry must be 1-200 characters of real text.
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert ROAST.strip(), "roast must not be only whitespace"

    # Preferred output path, with a local fallback if /output is not writable.
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ROAST)

    print(ROAST)


if __name__ == "__main__":
    main()
