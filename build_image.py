#!/usr/bin/env python3
"""Compose the 19 Nov 2026 'world in one day' front page, 1024x1024. v2: stacked, measured text."""
from PIL import Image, ImageDraw, ImageFont
import os

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

def F(path, size):
    return ImageFont.truetype(path, size)

def crop_fill(img, w, h):
    img = img.convert("RGB")
    s = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    x = (img.width - w) // 2
    y = (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))

def panel(canvas, path, box):
    x0, y0, x1, y1 = box
    im = crop_fill(Image.open(path), x1 - x0, y1 - y0)
    canvas.paste(im, (x0, y0))
    d = ImageDraw.Draw(canvas)
    d.rectangle([x0, y0, x1 - 1, y1 - 1], outline=(20, 20, 20), width=3)

_probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))

def wrap(s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if _probe.textlength(t, font=font) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def block(d, x, y, s, font, fill, maxw, leading=1.12):
    """Draw wrapped text at (x,y); return y just below it."""
    lines = wrap(s, font, maxw)
    lh = round(font.size * leading)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

W = H = 1024
paper = (247, 243, 234)
img = Image.new("RGB", (W, H), paper)
d = ImageDraw.Draw(img)
INK = (15, 15, 15)
GREY = (42, 42, 42)
RED = (178, 24, 32)

# ---------- masthead ----------
d.text((W // 2, 24), "THE WORLD IN ONE DAY", font=F(SERIF_B, 63), fill=INK, anchor="ma")
d.rectangle([28, 104, 996, 108], fill=INK)
d.rectangle([28, 112, 996, 150], fill=RED)
d.text((W // 2, 120), "THURSDAY  ·  19 NOVEMBER 2026", font=F(SANS_B, 27), fill=(255, 255, 255), anchor="ma")
d.rectangle([28, 158, 996, 161], fill=INK)

# ---------- left column: GTA VI ----------
LX, LW = 28, 608
panel(img, f"{A}/media-generation-panel-gta-0-d08a807e-3612-4f32-8c18-aa0ec4ac2b15.jpg", (LX, 174, LX + LW, 540))
y = 552
y = block(d, LX, y, "GAMING  ·  THE WAIT IS OVER", F(SANS_B, 17), RED, LW) + 4
y = block(d, LX, y, "GTA VI LAUNCHES WORLDWIDE", F(SERIF_B, 40), INK, LW) + 4
y = block(d, LX, y, "After a 13-year wait, gamers pour into Vice City as the blockbuster rolls out worldwide to near-perfect reviews.", F(SANS, 19), GREY, LW - 8)

# ---------- right column: summit + hormuz ----------
RX, RW = 652, 344
panel(img, f"{A}/media-generation-panel-summit-0-e6536f3a-a671-44e7-bba4-62123f45e040.jpg", (RX, 174, 996, 384))
y = 396
y = block(d, RX, y, "SHENZHEN  ·  DIPLOMACY", F(SANS_B, 15), RED, RW) + 3
y = block(d, RX, y, "TRUMP, XI & PUTIN MEET FACE TO FACE", F(SERIF_B, 25), INK, RW) + 3
y = block(d, RX, y, "The first US-China-Russia summit puts nuclear arms and two wars on the table.", F(SANS, 17), GREY, RW - 4)
panel(img, f"{A}/media-generation-panel-hormuz-0-fd9fb224-4b92-4558-b296-85e0d9a88f61.jpg", (RX, y + 14, 996, y + 158))
y = y + 170
y = block(d, RX, y, "STRAIT OF HORMUZ  ·  ENERGY", F(SANS_B, 15), RED, RW) + 3
y = block(d, RX, y, "THREE TANKERS ABLAZE AFTER STRIKING MINES", F(SERIF_B, 22), INK, RW)

# ---------- bottom band ----------
BY = 806
d.rectangle([28, BY, 996, BY + 3], fill=INK)
panel(img, f"{A}/media-generation-panel-vangogh-0-ba3ef1e4-e665-407b-b7a6-cc9458ef1f8d.jpg", (28, BY + 16, 356, 988))
VX = 372
y = BY + 18
y = block(d, VX, y, "ART MARKET", F(SANS_B, 15), RED, 280) + 3
y = block(d, VX, y, "VAN GOGH SELLS FOR A RECORD $190.4M", F(SERIF_B, 23), INK, 284) + 3
y = block(d, VX, y, "The highest price ever paid for the artist, after an ownership dispute.", F(SANS, 16), GREY, 280)

AX = 676
y = BY + 18
y = block(d, AX, y, "ALSO TODAY", F(SANS_B, 16), RED, 320) + 5
items = [
    "VOYAGER 1 - NASA's probe reaches one light-day from Earth",
    "THE HAGUE - World Court rules in Myanmar's Rohingya genocide case",
    "PEW - Muslims projected to outnumber Christians by 2035",
    "JAPAN - Magnitude 5.7 earthquake strikes Kumamoto",
]
for it in items:
    y = block(d, AX, y, it, F(SANS, 15), (30, 30, 30), 318) + 6

img.save(OUT, format="JPEG", quality=90)
print("saved", OUT, os.path.getsize(OUT), "bytes", img.size)
