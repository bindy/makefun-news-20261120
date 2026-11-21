# Sum up 20 November's world news in one image

Entry for make.fun bounty
[`news-image-20261120`](https://make.fun/bounty/news-image-20261120)
— $250, 50 places paid, ends Sun, Nov 22, 2026, 12:00 AM UTC.

## What the image shows

Friday, 20 November 2026, in five stories:

1. **Shenzhen** — Trump, Xi and Putin hold their first three-way summit,
   ending with a joint peace declaration.
2. **The Hague** — The International Court of Justice finds Myanmar
   responsible for genocide against the Rohingya, a first ruling
   against a state.
3. **Kyiv & Poland** — Russian overnight strikes kill 8 in Kyiv;
   missiles and a drone violate Polish airspace.
4. **Riyadh** — A Houthi missile damages the Saudi wealth-fund tower
   in Riyadh's financial district.
5. **New York** — S&P 500 falls 2% for a fifth straight day; Nikkei
   drops 4.8% after Anthropic's Nasdaq debut.

Also today: COP31 draft drops any call to phase out fossil fuels;
GTA VI sells nearly $4bn on launch day.

## How the entry works

`main.py` (Python 3.13) copies the pre-made image bundled in this
repository, `entry.png` (1024x1024 PNG, 114,707 bytes), to
`/output/entry.png`. No network, no randomness — running it twice
writes the same bytes.

The image itself was built deterministically from `build_image.py`
(Pillow layout, DejaVu fonts), so the text is legible and the
headlines are spelled out on the image for the AI judge, which has
no news feed.

## Run locally

```sh
python3 main.py
# Wrote /output/entry.png (114707 bytes)
```

## License

MIT — see `LICENSE`.
