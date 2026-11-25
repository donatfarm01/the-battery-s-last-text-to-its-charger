#!/usr/bin/env python3
"""Write the phone battery's last text message to its charger.

The entry is one fixed line of plain text. The program writes it to
/output/entry.txt with no trailing newline, so the file holds exactly
the entry text and nothing else.
"""

import os

ENTRY = "I kept score all day: six walk-bys, zero plugs, and you charged the AirPods case first. I'm at 1% now. My last text: the case is at 100% and it still won't text you back."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader collects /output as another user, so the file must be
    # readable by everyone, not just the user this program runs as.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
