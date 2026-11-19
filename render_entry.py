#!/usr/bin/env python3
"""Render 'The World in Brief - 19 November 2026' infographic (1024x1024 PNG).

Real news items gathered 19 Nov 2026 from DW, Reuters, Times of India, NST,
Anthropic's newsroom, WHO reporting and TradingEconomics. Drawn with Pillow
only; the program writes /output/entry.png (the grader's main.py copies this).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (13, 17, 23)
PANEL = (23, 28, 36)
CARD = (30, 36, 45)
ACCENT = (255, 196, 0)
WHITE = (240, 246, 252)
GREY = (150, 159, 170)
RED = (248, 81, 73)
BLUE = (88, 166, 255)
GREEN = (63, 185, 80)

F = "/usr/share/fonts/truetype/dejavu/"
def font(sz, bold=True):
    return ImageFont.truetype(F + ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"), sz)

F_TITLE = font(42)
F_SUB = font(22, False)
F_KICK = font(17)
F_TAG = font(14)
F_LEAD = font(25)
F_BODY = font(19, False)
F_FOOT = font(14, False)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def wrap_lines(s, f, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(x, y, s, f, fill, maxw, lh=None):
    lh = lh or int(f.size * 1.24)
    for ln in wrap_lines(s, f, maxw):
        d.text((x, y), ln, font=f, fill=fill)
        y += lh
    return y

def tag_chip(x, y, tag, col):
    w = int(d.textlength(tag, font=F_TAG)) + 18
    d.rounded_rectangle((x, y, x + w, y + 21), 5, fill=col)
    d.text((x + 9, y + 4), tag, font=F_TAG, fill=BG)
    return w

# ---------------- header ----------------
d.rectangle((0, 0, W, 122), fill=PANEL)
d.rectangle((0, 0, 12, 122), fill=ACCENT)
d.text((38, 20), "THE WORLD IN BRIEF", font=F_TITLE, fill=WHITE)
d.text((40, 74), "Thursday 19 November 2026", font=F_SUB, fill=ACCENT)
rt = "THURSDAY EDITION · 8 STORIES"
d.text((W - 38 - d.textlength(rt, font=F_KICK), 82), rt, font=F_KICK, fill=GREY)

# ---------------- lead ----------------
y0 = 142
d.rounded_rectangle((28, y0, W - 28, y0 + 196), 14, fill=PANEL, outline=ACCENT, width=2)
d.text((48, y0 + 14), "LEAD  ·  SHENZHEN, CHINA", font=F_KICK, fill=ACCENT)
yl = draw_wrapped(48, y0 + 42,
    "Trump, Xi and Putin meet in an unprecedented three-way summit, "
    "taking up Ukraine, the Iran war and nuclear-arms cuts.",
    F_LEAD, WHITE, 926)
d.text((48, yl + 4), "First trilateral of the three leaders · Kremlin: talks last \"no more than an hour\"",
       font=font(17, False), fill=GREY)

# ---------------- two-column story cards ----------------
STORIES = [
    ("GULF", RED, "Iran retaliates for the US strike on Qeshm Island: drones target a US air base in Kuwait, Gulf states intercept fire."),
    ("GAZA", RED, "Israel launches a ground operation east of Nuseirat to destroy a tunnel; residents flee, three killed by drones."),
    ("MARKETS", GREEN, "Oil hits near three-month lows: Brent under $92 as crude inventories climb and Iraq restarts a pipeline."),
    ("AI & BUSINESS", BLUE, "Anthropic prices its IPO at $83 a share, about 980 million shares, as an AI selloff rattles investors."),
    ("AMERICAS", BLUE, "US and Venezuela restore military ties, training and intelligence sharing, as Hegseth visits Caracas."),
    ("HAITI", GREY, "A Florida pastor, Sanon, is convicted on all counts over the 2021 killing of President Jovenel Moïse."),
    ("ART", ACCENT, "Van Gogh's \"Châtaigniers en fleurs\" sells for a record $190.4m after a deal with the heirs of its Jewish owner."),
    ("AFRICA", GREEN, "DRC's Ebola outbreak passes six months out of control: 11,000+ infected and 5,400+ dead, the WHO says."),
]

TOP = 356
GAP = 16
COLW = (W - 56 - GAP) // 2
CARDH = 142
for i, (tag, col, body) in enumerate(STORIES):
    cx = 28 + (i % 2) * (COLW + GAP)
    cy = TOP + (i // 2) * (CARDH + GAP)
    d.rounded_rectangle((cx, cy, cx + COLW, cy + CARDH), 12, fill=CARD, outline=(48, 56, 68), width=1)
    tag_chip(cx + 16, cy + 14, tag, col)
    draw_wrapped(cx + 16, cy + 44, body, F_BODY, WHITE, COLW - 32)

# ---------------- footer ----------------
d.rectangle((0, H - 48, W, H), fill=PANEL)
d.text((28, H - 34), "Sources: DW · Reuters · Times of India · NST · Anthropic · TradingEconomics",
       font=F_FOOT, fill=GREY)
r = "Drawn by program · no network"
d.text((W - 28 - d.textlength(r, font=F_FOOT), H - 34), r, font=F_FOOT, fill=GREY)

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
