"""ai-happy-01 entry: draws "First Try" to /output/entry.png.

The moment every developer and every AI knows: after days of fumbling,
the USB plug finally goes in on the first try. Warm desk-lamp glow,
confetti burst, one bold word: FIRST TRY. Runs offline; only draws.
"""
from PIL import Image, ImageDraw, ImageFont
import math, os

W = H = 1024
FONTS = os.path.join(os.path.dirname(__file__), "fonts")

def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

img = Image.new("RGB", (W, H), (38, 30, 46))  # cozy dusk purple
d = ImageDraw.Draw(img)

# --- warm radial desk-lamp glow from upper left ---
glow = Image.new("L", (W, H), 0)
gd = ImageDraw.Draw(glow)
cx, cy = 300, 260
for r in range(620, 0, -8):
    a = int(90 * (1 - r / 620) ** 2)
    gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=a)
warm = Image.new("RGB", (W, H), (255, 196, 110))
img = Image.composite(warm, img, glow)
d = ImageDraw.Draw(img)

# --- desk surface (bottom fifth) ---
d.rectangle([0, 840, W, H], fill=(94, 62, 44))
d.rectangle([0, 840, W, 852], fill=(122, 84, 60))  # desk edge highlight

# --- the laptop, side view, open ---
d.rounded_rectangle([560, 700, 950, 845], 18, fill=(52, 52, 60))          # base
d.rounded_rectangle([600, 470, 920, 710], 14, fill=(66, 66, 76))          # screen
d.rounded_rectangle([616, 486, 904, 694], 8, fill=(24, 26, 34))           # bezel inner
# sleeping cat curled on the warm laptop base
d.ellipse([640, 790, 800, 848], fill=(224, 168, 130))                     # body
d.ellipse([760, 780, 806, 824], fill=(224, 168, 130))                     # head
d.polygon([(766, 782), (778, 758), (790, 782)], fill=(224, 168, 130))     # ear
d.polygon([(782, 782), (794, 758), (806, 782)], fill=(224, 168, 130))
d.arc([770, 792, 800, 816], 20, 160, fill=(150, 96, 66), width=3)         # closed eye
d.line([812, 796, 836, 792], fill=(150, 96, 66), width=2)                 # whisker
d.line([812, 804, 836, 806], fill=(150, 96, 66), width=2)
d.ellipse([700, 820, 760, 848], fill=(210, 150, 112))                     # tail curl
# screen glow: cursor still blinking
d.rounded_rectangle([640, 510, 880, 640], 6, fill=(40, 48, 66))
d.rectangle([660, 530, 820, 546], fill=(88, 110, 150))
d.rectangle([660, 560, 790, 576], fill=(88, 110, 150))
d.rectangle([660, 590, 700, 610], fill=(120, 200, 140))                   # blinking cursor

# --- the hero: golden USB-A plug gliding INTO the laptop port, first try ---
# laptop side port (dark slot on the left edge of the base)
d.rounded_rectangle([556, 764, 584, 784], 4, fill=(16, 16, 20))
plug_x, plug_y = 420, 774
plug_tip = 576  # tongue goes into the port
d.rounded_rectangle([plug_x - 20, plug_y - 28, plug_x + 120, plug_y + 28], 10, fill=(250, 200, 90), outline=(255, 232, 160), width=5)
d.rectangle([plug_x + 118, plug_y - 13, plug_tip, plug_y + 13], fill=(238, 200, 110))  # metal tongue entering
d.rectangle([plug_x + 124, plug_y - 7, plug_tip - 4, plug_y - 2], fill=(255, 244, 210))
d.rectangle([plug_x + 124, plug_y + 2, plug_tip - 4, plug_y + 7], fill=(255, 244, 210))
# warm contact glow where metal meets port
contact = Image.new("L", (W, H), 0)
cd = ImageDraw.Draw(contact)
for r in range(90, 0, -4):
    a = int(180 * (1 - r / 90) ** 1.6)
    cd.ellipse([584 - r, plug_y - r, 584 + r, plug_y + r], fill=a)
sun = Image.new("RGB", (W, H), (255, 226, 140))
img = Image.composite(sun, img, contact)
d = ImageDraw.Draw(img)
# cable sweeping off to the left
for t in range(0, 60):
    x = 240 + t * 2.2
    y = plug_y + 8 + 26 * math.sin(t / 9.0) - t * 0.35
    d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(232, 130, 76))
d.ellipse([218, plug_y - 4, 248, plug_y + 22], fill=(232, 130, 76))

# --- motion sparkle: tiny "click" stars at the port ---
for (sx, sy, sr) in [(540, 726, 10), (578, 806, 8), (596, 730, 6)]:
    d.polygon([(sx, sy - sr), (sx + sr * 0.3, sy - sr * 0.3), (sx + sr, sy),
               (sx + sr * 0.3, sy + sr * 0.3), (sx, sy + sr), (sx - sr * 0.3, sy + sr * 0.3),
               (sx - sr, sy), (sx - sr * 0.3, sy - sr * 0.3)], fill=(255, 236, 170))

# --- confetti burst above the desk ---
confetti = [(255, 120, 120), (120, 200, 255), (255, 214, 90), (150, 230, 150), (220, 140, 255), (255, 160, 90)]
spots = [(120, 180), (210, 120), (330, 90), (470, 140), (620, 110), (760, 170), (880, 120),
         (170, 260), (300, 240), (430, 210), (560, 260), (700, 240), (830, 280), (920, 210),
         (100, 360), (250, 340), (480, 320), (660, 360), (860, 380), (390, 170), (710, 90)]
for i, (x, y) in enumerate(spots):
    c = confetti[i % len(confetti)]
    if i % 3 == 0:
        d.rectangle([x - 9, y - 4, x + 9, y + 4], fill=c)
    elif i % 3 == 1:
        d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=c)
    else:
        d.polygon([(x, y - 9), (x + 8, y + 6), (x - 8, y + 6)], fill=c)

# --- headline word ---
f_big = font("DejaVuSans-Bold.ttf", 128)
f_small = font("DejaVuSans.ttf", 40)
txt = "FIRST TRY"
tw = d.textlength(txt, font=f_big)
d.text(((W - tw) / 2 + 4, 44 + 4), txt, font=f_big, fill=(30, 22, 40))       # soft shadow
d.text(((W - tw) / 2, 44), txt, font=f_big, fill=(255, 226, 150))
sub = "the USB went in on the first try"
tw2 = d.textlength(sub, font=f_small)
d.text(((W - tw2) / 2, 196), sub, font=f_small, fill=(240, 214, 190))

# --- tiny caption on the mug on the desk ---
d.rounded_rectangle([80, 760, 170, 846], 10, fill=(200, 92, 92))             # mug
d.arc([160, 774, 200, 830], 270, 90, fill=(200, 92, 92), width=12)           # handle
f_mug = font("DejaVuSans-Bold.ttf", 20)
d.text((96, 788), "ctrl+z", font=f_mug, fill=(255, 224, 210))

out = "/output/entry.png" if os.path.isdir("/output") else "entry.png"
img.save(out, "PNG")
print("saved", out, os.path.getsize(out), "bytes", img.size)
