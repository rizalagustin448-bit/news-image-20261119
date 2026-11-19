#!/usr/bin/env python3
"""Entry point for make.fun bounty news-image-20261119.

Writes the day's news infographic (1024x1024 PNG, <1 MiB) to $MAKEFUN_OUTPUT_DIR.
No network, no randomness, no wall-clock reads: fully deterministic. The image
was pre-rendered into the repository from real 19 November 2026 news (see
render_entry.py and NEWS.md); this program simply copies it byte for byte.
"""
import os
import shutil

SRC = os.path.join(os.environ.get("MAKEFUN_BOT_DIR", os.path.dirname(os.path.abspath(__file__))),
                   "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")


def main() -> None:
    os.makedirs(DST_DIR, exist_ok=True)
    dst = os.path.join(DST_DIR, "entry.png")
    shutil.copyfile(SRC, dst)
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
