#!/usr/bin/env python3
"""Render index.html to output/entry.png deterministically.

Pipeline: WeasyPrint renders index.html to a PDF (page is 1024x1024 CSS
pixels = 768pt), then pdftoppm converts that PDF to a 1024x1024 PNG at
96 dpi. Both steps are deterministic for fixed input: the PDF holds no
rendering-relevant timestamps, and pdftoppm writes pixels only.

Usage: python3 render.py [output-path]
Default output: output/entry.png next to this script.
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from weasyprint import HTML

HERE = Path(__file__).resolve().parent
SRC = HERE / "index.html"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "output" / "entry.png"

OUT.parent.mkdir(parents=True, exist_ok=True)

# Fixed epoch so any metadata WeasyPrint embeds is stable.
os.environ["SOURCE_DATE_EPOCH"] = "1795579200"  # 2026-11-25 12:00:00 UTC

with tempfile.TemporaryDirectory(dir=str(HERE)) as tmp:
    pdf = Path(tmp) / "page.pdf"
    HTML(filename=str(SRC)).write_pdf(str(pdf))
    # -r 96: 768pt page -> 1024px. -singlefile: one PNG, named <prefix>.png
    subprocess.run(
        ["pdftoppm", "-png", "-r", "96", "-singlefile", str(pdf),
         str(OUT.with_suffix(""))],
        check=True,
    )

print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
