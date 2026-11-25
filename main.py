#!/usr/bin/env python3
"""One Word From Grandma: the single word Grandma would text about AI.

Grandma has never once said "artificial intelligence". She has, however,
met a robot, and in her world there is exactly one name for a walking,
talking metal man: the Tinman, straight out of Oz. So that is what she
texts: tinman.
"""

import os
import stat

WORD = "tinman"  # one word, 6 chars: inside the 1-30 char gate, no spaces.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    os.chmod(path, 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
