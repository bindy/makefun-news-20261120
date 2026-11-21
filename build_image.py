from PIL import Image, ImageDraw, ImageFont
import textwrap, os

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(__file__), "entry.png")

def font(name, size):
    base = "/usr/share/fonts/truetype/dejavu/"
    paths = {
        "bold": base+"DejaVuSans-Bold.ttf",
        "reg": base+"DejaVuSans.ttf",
        "serif_bold": base+"DejaVuSerif-Bold.ttf",
        "serif": base+"DejaVuSerif.ttf",
    }
    return ImageFont.truetype(paths[name], size)

def wrap(draw, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur+" "+w).strip()
        if draw.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def draw_wrapped(draw, x, y, text, f, color, max_w, lh=None):
    lines = wrap(draw, text, f, max_w)
    if lh is None: lh = int(f.size*1.25)
    for ln in lines:
        draw.text((x, y), ln, font=f, fill=color)
        y += lh
    return y

img = Image.new("RGB", (W, H), "#F6F1E7")
d = ImageDraw.Draw(img)

NAVY = (15, 32, 64)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
INK = (20, 20, 20)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)

# Header
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 154], fill=RED)
d.text((36, 22), "THE WORLD  •  IN ONE IMAGE", font=font("bold", 22), fill=(255, 210, 90))
d.text((36, 52), "FRIDAY, 20 NOVEMBER 2026", font=font("serif_bold", 46), fill=WHITE)
d.text((36, 108), "Five stories that defined the day  —  Shenzhen  •  The Hague  •  Kyiv  •  Riyadh  •  Wall Street", font=font("reg", 19), fill=(210, 220, 235))

# Hero - Shenzhen
x, y, w, h = 28, 172, 968, 196
d.rounded_rectangle([x, y, x+w, y+h], radius=14, fill=CARD, outline=(220, 210, 190), width=2)
d.rectangle([x, y, x+10, y+h], fill=RED)
# three flag-ish circles
for i, (label, col) in enumerate([("US", (178,34,34)), ("CN", (200,30,30)), ("RU", (20,60,140))]):
    cx = x+58+i*0  # placeholder, draw row on right instead
# right visual: three circles
cx0 = 830
for i, (label, col) in enumerate([("US", (178,34,34)), ("CN", (210,40,40)), ("RU", (25,70,160))]):
    cx = cx0 + i*0
    cy = y+28+i*50
    d.ellipse([cx, cy, cx+42, cy+42], fill=col, outline=WHITE, width=2)
    d.text((cx+7 if label!="US" else cx+9, cy+11), label, font=font("bold", 17), fill=WHITE)
d.text((x+28, y+16), "01  •  DIPLOMACY  —  SHENZHEN, CHINA", font=font("bold", 20), fill=RED)
draw_wrapped(d, x+28, y+46, "TRUMP, XI & PUTIN MEET", font("serif_bold", 36), INK, 740)
draw_wrapped(d, x+28, y+90, "IN SHENZHEN", font("serif_bold", 36), INK, 740)
d.text((x+28, y+140), "First three-way summit ends with a joint", font=font("reg", 21), fill=GREY)
d.text((x+28, y+166), "peace declaration.", font=font("reg", 21), fill=GREY)

# 2x2 grid
stories = [
    ("02  •  JUSTICE  —  THE HAGUE", "MYANMAR GUILTY\nOF GENOCIDE", "UN court finds Myanmar responsible\nfor genocide against the Rohingya —\na first ruling against a state.", (15, 90, 130)),
    ("03  •  WAR  —  KYIV & POLAND", "MISSILES OVER\nKYIV & POLAND", "Russian overnight strikes kill 8 in\nKyiv; missiles and a drone violate\nPolish airspace.", (140, 40, 40)),
    ("04  •  MIDDLE EAST  —  RIYADH", "MISSILE HITS\nRIYADH TOWER", "Houthi missile damages the Saudi\nwealth-fund tower in Riyadh's\nfinancial district.", (150, 100, 20)),
    ("05  •  MARKETS  —  NEW YORK", "AI STOCKS\nCRASH", "S&P 500 falls 2% for a fifth straight\nday; Nikkei drops 4.8% after\nAnthropic's Nasdaq debut.", (20, 110, 60)),
]
gx, gy = 28, 388
cw, ch, gap = 474, 236, 20
for i, (tag, head, sub, col) in enumerate(stories):
    cx = gx + (i % 2)*(cw+gap)
    cy = gy + (i // 2)*(ch+gap)
    d.rounded_rectangle([cx, cy, cx+cw, cy+ch], radius=14, fill=CARD, outline=(220, 210, 190), width=2)
    d.rectangle([cx, cy, cx+cw, cy+8], fill=col)
    d.text((cx+22, cy+22), tag, font=font("bold", 17), fill=col)
    yy = cy+52
    for ln in head.split("\n"):
        d.text((cx+22, yy), ln, font=font("serif_bold", 30), fill=INK)
        yy += 38
    yy += 6
    for ln in sub.split("\n"):
        d.text((cx+22, yy), ln, font=font("reg", 19), fill=GREY)
        yy += 25

# Bottom strip - two mini stories
y = 900
d.rounded_rectangle([28, y, 996, y+96], radius=14, fill=NAVY)
d.text((52, y+14), "ALSO TODAY", font=font("bold", 18), fill=(255, 210, 90))
d.text((52, y+40), "COP31 draft drops any call to phase out fossil fuels  •  GTA VI sells nearly $4bn on launch day", font=font("reg", 19), fill=WHITE)
d.text((52, y+68), "Sources: AP / Reuters / Just Security / OneTurn  —  20 Nov 2026", font=font("reg", 16), fill=(180, 195, 215))

img.save(OUT, "PNG", optimize=True)
print(OUT, img.size, os.path.getsize(OUT))
