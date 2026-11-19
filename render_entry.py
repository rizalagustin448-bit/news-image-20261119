#!/usr/bin/env python3
"""Render the 19 November 2026 world-news front page into entry.png.

Dense newspaper-style layout at 1024x1024: masthead, lead story, world map
with story markers, and 37 sourced stories organised by region. Pillow only.
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (243, 239, 230)
INK = (18, 20, 24)
RED = (170, 30, 30)
BLUE = (30, 90, 170)
GREEN = (30, 130, 60)
ORANGE = (170, 100, 20)
LAND = (214, 209, 196)
LANDLINE = (130, 127, 118)
GREY = (105, 102, 94)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FO = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def f(path, size):
    return ImageFont.truetype(path, size)

def text(x, y, s, fo_, fill=INK, anchor=None):
    d.text((x, y), s, font=fo_, fill=fill, anchor=anchor)

def wrap(x, y, s, fo_, width, lh, fill=INK, maxlines=3):
    words = s.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=fo_) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    lines.append(cur)
    for i, ln in enumerate(lines[:maxlines]):
        text(x, y + i * lh, ln, fo_, fill)
    return y + min(len(lines), maxlines) * lh

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 116], fill=INK)
text(W // 2, 14, "THE WORLD IN BRIEF", f(FB, 46), PAPER, anchor="ma")
text(W // 2, 74, "THURSDAY 19 NOVEMBER 2026   ·   SIX CONTINENTS, ONE PAGE   ·   37 STORIES",
     f(FR, 17), (198, 198, 198), anchor="ma")
d.line([30, 126, W - 30, 126], fill=INK, width=3)

# ---------------- lead strip ----------------
LY = 136
d.rectangle([30, LY, W - 30, LY + 108], outline=RED, width=3)
text(44, LY + 8, "LEAD  ·  SHENZHEN, CHINA", f(FB, 16), RED)
wrap(44, LY + 30,
     "Trump, Xi and Putin hold historic first trilateral summit on APEC sidelines — Ukraine, "
     "the Iran war and nuclear-arms cuts on the table.",
     f(FB, 21), 920, 26, maxlines=2)
text(44, LY + 86, "First meeting ever of the three leaders · Kremlin: talks last \"no more than an hour\" · AP, BBC",
     f(FO, 13), GREY)

# ---------------- world map ----------------
MX0, MY0, MX1, MY1 = 24, 258, 1000, 470
d.rectangle([MX0, MY0, MX1, MY1], outline=INK, width=2)

def mx(lon): return MX0 + (lon + 180) / 360 * (MX1 - MX0)
def my(lat): return MY0 + (75 - lat) / 135 * (MY1 - MY0)

CONTINENTS = [
    [(-168, 65), (-120, 70), (-95, 72), (-60, 68), (-55, 50), (-75, 42), (-80, 25), (-97, 18), (-105, 22), (-125, 40), (-168, 65)],
    [(-92, 18), (-83, 9), (-77, 8), (-50, 0), (-35, -8), (-40, -22), (-58, -35), (-72, -18), (-80, 0), (-92, 18)],
    [(-10, 36), (10, 38), (32, 32), (43, 12), (51, 12), (40, -5), (35, -25), (20, -35), (12, -18), (9, 4), (-8, 5), (-17, 15), (-10, 36)],
    [(-10, 44), (0, 50), (20, 55), (40, 60), (60, 68), (100, 72), (140, 70), (170, 66), (140, 50), (100, 42), (60, 40), (28, 36), (-10, 44)],
    [(72, 22), (80, 12), (88, 22), (78, 30), (70, 26), (72, 22)],
    [(95, 5), (105, 2), (115, 5), (120, 12), (108, 18), (98, 12), (95, 5)],
    [(112, -12), (130, -12), (150, -22), (153, -30), (140, -38), (115, -34), (112, -12)],
    [(-62, -62), (-40, -70), (-20, -72), (20, -70), (60, -68), (120, -66), (170, -70), (160, -78), (60, -80), (-40, -80), (-62, -62)],
]
for poly in CONTINENTS:
    d.polygon([(mx(lo), my(la)) for lo, la in poly], fill=LAND, outline=LANDLINE)

MAP_PINS = [
    (114.06, 22.54, RED), (13.4, 52.5, RED), (47.5, 29.4, RED), (34.4, 31.5, RED),
    (4.3, 52.1, RED), (-149.5, 61.2, BLUE), (-66.9, 10.5, BLUE), (23.0, -3.0, GREEN),
    (86.0, 20.0, ORANGE), (127.4, 39.8, RED), (-74.0, 40.7, BLUE), (36.5, 45.3, RED),
    (100.0, 60.0, RED), (32.5, 15.5, RED), (-77.0, -12.0, (120, 60, 150)),
]
for lon, lat, color in MAP_PINS:
    x, y = mx(lon), my(lat)
    d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=color, outline=INK)

text(MX0 + 12, MY0 + 8, "WHERE THE DAY HAPPENED", f(FB, 16), INK)
text(MX1 - 12, MY0 + 8,
     "● conflict/diplomacy  ● politics/markets  ● health  ● weather",
     f(FR, 12), GREY, anchor="ra")

# ---------------- story columns ----------------
stories_cols = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "stories_cols.json")))
colx = [30, 348, 666]
COLW = 306
y0 = 482
d.line([30, y0 - 10, W - 30, y0 - 10], fill=INK, width=2)

columns = stories_cols

maxbottom = 0
for ci, col in enumerate(columns):
    cx = colx[ci]
    yy = y0 + 2
    for tag, loc, lon, lat, headline, src in col:
        text(cx, yy, tag + " · " + loc, f(FB, 12), RED if ci != 1 else BLUE)
        yy += 13
        yy = wrap(cx, yy, headline, f(FR, 12), COLW, 13.5, maxlines=2)
        text(cx, yy + 1, src, f(FO, 9), GREY)
        yy += 12
        maxbottom = max(maxbottom, yy)

# footer
d.rectangle([0, H - 24, W, H], fill=INK)
text(W // 2, H - 19,
     "SOURCES: AP · BBC · REUTERS · XINHUA · TOI · KYIV INDEPENDENT · ICJ · WHO · IAEA · MEE · EURONEWS  |  ALL EVENTS 19 NOV 2026",
     f(FR, 11), (190, 190, 190), anchor="ma")

img.save("/home/agentuser/news-image-20261119/entry.png", optimize=True)
q = img.quantize(colors=64, method=Image.MAXCOVERAGE, dither=Image.NONE)
q.save("/home/agentuser/news-image-20261119/entry_q.png", optimize=True)
print("rgb:", os.path.getsize("/home/agentuser/news-image-20261119/entry.png"),
      "quant:", os.path.getsize("/home/agentuser/news-image-20261119/entry_q.png"),
      "col_bottoms:", maxbottom)
