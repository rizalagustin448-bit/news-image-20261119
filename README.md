# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/rizal0909/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/rizal0909/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

An infographic summarising Thursday 19 November 2026's world news in one
1024×1024 image: the Trump–Xi–Putin summit in Shenzhen as the lead, plus the
Gulf escalation, Gaza, Anthropic's IPO, oil at three-month lows, US–Venezuela
military ties, the Sanon verdict, the Van Gogh record sale and the DRC Ebola
outbreak. Every item came from real reporting published on the day (DW,
Reuters, Times of India, NST, Anthropic, TradingEconomics) and is listed in
[NEWS.md](NEWS.md).

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
