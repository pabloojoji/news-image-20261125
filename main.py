#!/usr/bin/env python3
"""Entry program for the news-image-20261125 bounty.

Copies the repository's pre-rendered image to the output directory.
Standard library only. No network, no fonts, no image libraries,
no writes to the working directory.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "output", "entry.png")

OUTDIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
if not os.path.isdir(OUTDIR):
    OUTDIR = os.path.join(HERE, "output")

os.makedirs(OUTDIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUTDIR, "entry.png"))
