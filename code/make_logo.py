"""Draws the site logo: an "I (heart) ECLIPSES" bumper sticker -> images/logo.png."""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

S = 4                                   # supersample, then shrink for smooth edges
H = 84                                  # final height in pixels
font = ImageFont.truetype("C:/Windows/Fonts/ariblk.ttf", 44 * S)
word_w = font.getlength("ECLIPSES") / S
W = round(112 + word_w + 24)            # text start + text + right margin
img = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# sticker: white, rounded, black border
d.rounded_rectangle((3 * S, 3 * S, (W - 3) * S, (H - 3) * S), radius=16 * S,
                    fill="white", outline="#111", width=4 * S)

baseline = 58 * S
d.text((24 * S, baseline), "I", font=font, fill="#111", anchor="ls")


def heart(cx, cy, size, n=200):
    """Classic heart curve, centered at (cx, cy), about `size` wide."""
    t = np.linspace(0, 2 * np.pi, n)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    k = size / 34
    return list(zip(cx + k * x, cy - k * y))


d.polygon(heart(76 * S, 42 * S, 46 * S), fill="#d7191c")

d.text((112 * S, baseline), "ECLIPSES", font=font, fill="#111", anchor="ls")

img.resize((W, H), Image.LANCZOS).save("images/logo.png")
print("wrote images/logo.png")
