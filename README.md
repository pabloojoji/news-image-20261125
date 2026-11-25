# World in a Day — Wednesday 25 November 2026

[![Rank](https://make.fun/badge/news-image-20261125/pabloojoji/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/pabloojoji/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

One image summing up the world's news of **Wednesday 25 November 2026**,
for the make.fun bounty [news-image-20261125](https://make.fun/bounty/news-image-20261125).

## The image

`output/entry.png` — 1024×1024, 408,207 bytes. A newspaper front page,
"WORLD IN A DAY": 15 stories, all verified for 25 Nov 2026, with three
illustrated heroes, a markets/grid section, briefs, a UTC timeline, a
numbers panel, a schematic world map with numbered pins, and a DATE CHECK
box listing stories that belong to other days.

Illustrations are AI-generated images, not photographs of the events.
Each one is captioned "Illustration" on the page.

## Stories (all verified — see SOURCES.md)

1. Houthi drone hits Riyadh's PIF Tower (385 m, 80 floors) — 11 hurt
2. Huawei guilty on 10 of 12 counts in a Brooklyn jury trial
3. Shenzhou-24 launches at 00:18:52 UTC with Pakistan's first astronaut
4. Dow closes at 50,018.70 (+0.85%); Nvidia −5.86%; Dell revenue $54.94bn
5. Zelenskyy confirms Ukraine hit the Russian cargo ship Sparta II
6. Shanghai party chief Chen Jining under investigation
7. CIA and ODNI hit by a cyberattack (reported 25 Nov)
8. Sarkozy and Carla Bruni ordered to trial (first hearing 1 April 2027)
9. Trump awards Rudy Giuliani the Presidential Medal of Freedom
10. Israeli strike kills Hamas security chief Naeem Abu Nahel in Gaza
11. Poland to summon Russia's envoy after three missiles violate its airspace
12. Houthis 60 km from Aden, Yemen's military says
13. Landmine toll highest in five years: 6,929 victims in 2025
14. WHO evacuates Ebola team from a hospital in Akwe, Ituri (DRC)
15. Kyiv calls its Libya ship strikes self-defence (Merkury sunk)

Left out on purpose (DATE CHECK box on the page): COP31 ending with no
deal (22 Nov), Nepal quake (24 Nov), three tankers mined in the Strait of
Hormuz (24 Nov), Nvidia reinstating Jensen Huang as CEO (24 Nov), the ICJ
Myanmar genocide ruling (19 Nov), the US losing measles-free status (17 Nov).

Sources: Reuters, Xinhua, CNN, Wall Street Journal, Bloomberg,
Bloomberg Law, International Campaign to Ban Landmines (ICBL),
Associated Press, AFP.

## How it is built

- `index.html` — the front page (written from scratch for this entry).
- `render.py` — renders `index.html` to `output/entry.png` with WeasyPrint
  (PDF) + `pdftoppm` (PNG at 96 dpi). Deterministic: two renders are
  byte-identical. Needs the local virtualenv (`.venv`, WeasyPrint 70)
  and `pdftoppm` (poppler-utils).
- `main.py` — the entry program (standard library only: `os` + `shutil`).
  It copies the repository's `output/entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (fallback `/output`). No network,
  no fonts, no image libraries, no writes to the working directory.
  Verified grader-style: run twice from a read-only directory with
  `python3 -P -s main.py`, both runs exit 0 and write bytes identical
  to `output/entry.png`.

## Run

```sh
python3 render.py            # rebuild output/entry.png
python3 -P -s main.py        # copy it to $MAKEFUN_OUTPUT_DIR/entry.png
```

## License

MIT — see `LICENSE`.
