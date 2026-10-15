# Redraws the We Gravel Morocco compass-star mark as a crisp square site icon.
import math, sys
from PIL import Image, ImageDraw
S = 2048; c = S / 2; k = S / 512
ORANGE = (225, 129, 49, 255)

def draw(bg):
    im = Image.new('RGBA', (S, S), bg)
    d = ImageDraw.Draw(im)
    L, rc, ring, dot, w = 222 * k, 92 * k, 15 * k, 40 * k, 15 * k
    # diagonal rays, between the star points
    for a in (45, 135, 225, 315):
        r = math.radians(a)
        p0 = (c + 104 * k * math.cos(r), c + 92 * k * math.sin(r))
        p1 = (c + 160 * k * math.cos(r), c + 148 * k * math.sin(r))
        d.line([p0, p1], fill=ORANGE, width=int(18 * k))
    # four star points: triangles from the ring out to each tip
    fill = bg if bg[3] else (0, 0, 0, 0)
    for axis in (-90, 0, 90, 180):
        a = math.radians(axis)
        tip = (c + L * math.cos(a), c + L * math.sin(a))
        base = [(c + rc * math.cos(a + s_), c + rc * math.sin(a + s_)) for s_ in (math.radians(-30), math.radians(30))]
        tri = [base[0], tip, base[1]]
        d.polygon(tri, fill=fill)
        d.line(tri, fill=ORANGE, width=int(w), joint='curve')
        for q in (tip,):
            d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=ORANGE)
    # ring and centre dot
    d.ellipse([c - rc, c - rc, c + rc, c + rc], fill=(255, 255, 255, 255) if bg[3] else (0, 0, 0, 0), outline=ORANGE, width=int(ring))
    d.ellipse([c - dot, c - dot, c + dot, c + dot], fill=ORANGE)
    return im.resize((512, 512), Image.LANCZOS)

out = sys.argv[1]
draw((255, 255, 255, 255)).save(f'{out}/wegravel-site-icon.png')
