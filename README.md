[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Ahmadramdani09/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Ahmadramdani09/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — Thursday, 19 November 2026

Entry for make.fun's [news-image-20261119](https://make.fun/bounty/news-image-20261119) bounty,
"Sum up 19 November's world news in one image" ($250 in USDC): one image that sums up the
world news of Thursday 19 November 2026.

A newspaper front page composed by `build_image.py` (Python/Pillow) from four
AI-generated news illustrations in `assets/`:

- **GTA VI launches worldwide** — gamers queue on launch night in a neon Vice City
- **Trump, Xi & Putin meet face to face** — the first US-China-Russia summit, Shenzhen
- **Three tankers ablaze after striking mines** — Strait of Hormuz
- **Van Gogh sells for a record $190.4M** — art market
- *Also today:* Voyager 1 at one light-day, the World Court's Myanmar ruling,
  Pew's 2035 projection, a magnitude 5.7 quake in Kumamoto

Run it as the grader does:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

`main.ts` copies `entry.png` to the output directory as `entry.png`.
The image is 1024x1024, JPEG bytes in a file named entry.png, ~310 KB.
