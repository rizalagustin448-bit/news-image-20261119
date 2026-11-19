# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/rizalagustin448-bit/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/rizalagustin448-bit/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A 37-story newspaper-style front page of Thursday 19 November 2026's world news
in one 1024×1024 image: the Trump–Xi–Putin first-ever trilateral in Shenzhen as
the lead, an equirectangular world map pinning 15 story locations across six
continents, and three balanced news columns — the ICJ's Rohingya genocide
judgment, the Berlin Ukraine talks, Iran's drone strikes on Kuwait, Gaza, the
Anthropic IPO, Peltola's Alaska win, the DRC Ebola toll, Cyclone Akvan and more.
Every story came from real reporting published on the day (AP, BBC, Reuters,
Xinhua, Times of India, Kyiv Independent, ICJ, WHO, IAEA) and is listed with
sources in [NEWS.md](NEWS.md).

## Run it

```sh
python3 main.py        # writes $MAKEFUN_OUTPUT_DIR/entry.png (default: ./output)
```

`main.py` copies the pre-rendered `entry.png` (drawn by `render_entry.py`) into
the output directory. No network, no randomness, no clock reads: two runs
produce identical bytes.

Regenerate the artwork:

```sh
python3 render_entry.py   # needs Pillow; rewrites entry.png
```
