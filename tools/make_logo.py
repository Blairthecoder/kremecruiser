#!/usr/bin/env python3
"""Regenerate the header logo assets.

Drop the real logo artwork in as assets/img/logo-source.png (PNG with a
transparent background is ideal, but a solid flat background is handled)
and run:

    python3 tools/make_logo.py

It writes kreme-cruiser-logo.png, @2x and @3x at the header display size.
If no logo-source.png is present it falls back to the version extracted
from the cart wrap photo, which is soft because that is all the source
resolution there was.
"""

import os
import sys
from PIL import Image, ImageFilter

DISPLAY_H = 64                      # must match .logo img height in style.css
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
SOURCE = os.path.join(IMG, "logo-source.png")
FALLBACK = os.path.join(IMG, "logo-source-from-cart.png")


def flatten_background(im, tol=26):
    """Make a uniform border colour transparent, for artwork supplied on a
    solid background such as the cream square version of the logo."""
    im = im.convert("RGBA")
    px = im.load()
    w, h = im.size
    corners = [px[0, 0], px[w - 1, 0], px[0, h - 1], px[w - 1, h - 1]]
    if len({c[:3] for c in corners}) != 1:
        return im                    # not a flat background, leave it alone
    key = corners[0][:3]
    if corners[0][3] == 0:
        return im                    # already transparent
    from collections import deque
    seen = [[False] * h for _ in range(w)]
    q = deque([(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)])
    while q:
        x, y = q.popleft()
        if not (0 <= x < w and 0 <= y < h) or seen[x][y]:
            continue
        seen[x][y] = True
        r, g, b, a = px[x, y]
        if abs(r - key[0]) + abs(g - key[1]) + abs(b - key[2]) > tol * 3:
            continue
        px[x, y] = (r, g, b, 0)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q.append((x + dx, y + dy))
    return im.crop(im.getbbox())


def main():
    path = SOURCE if os.path.exists(SOURCE) else FALLBACK
    if not os.path.exists(path):
        sys.exit("No logo source found. Add assets/img/logo-source.png")
    print("source:", os.path.basename(path))
    src = flatten_background(Image.open(path))

    for mult, name in ((1, "kreme-cruiser-logo.png"),
                       (2, "kreme-cruiser-logo@2x.png"),
                       (3, "kreme-cruiser-logo@3x.png")):
        h = DISPLAY_H * mult
        w = round(src.width * h / src.height)
        t = src.resize((w, h), Image.LANCZOS)
        t = t.filter(ImageFilter.UnsharpMask(
            radius=0.7 if mult == 1 else 1.0,
            percent=55 if mult == 1 else 75, threshold=0))
        t.save(os.path.join(IMG, name), optimize=True)
        print(f"  {name}  {w}x{h}")

    base = Image.open(os.path.join(IMG, "kreme-cruiser-logo.png"))
    print(f"\nSet width={base.width} height={base.height} on the header <img> "
          f"(tools/build.py) if the aspect ratio changed.")


if __name__ == "__main__":
    main()
