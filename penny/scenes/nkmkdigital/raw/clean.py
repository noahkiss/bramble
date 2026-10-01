# /// script
# dependencies = ["numpy", "pillow", "scipy"]
# ///
"""Clean a flare 'transparent' Penny banner and cut it into a page-border strip.

usage: uv run clean.py RAW OUT --bottom Y [--x0 X --width W] [--side F] [--top F] [--solid N]

  --bottom Y   crop line: rows >= Y are dropped, so the grass meets the bottom edge
  --x0/--width horizontal crop (art-directed mobile/medium crops)
  --side F     soft fade at left/right, as a fraction of the output width
  --top F      soft fade from the top, as a fraction of the output height
  --solid N    ramp alpha to fully opaque over the last N rows (crisp bottom line)
"""
import argparse, numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("dst")
ap.add_argument("--bottom", type=int, required=True)
ap.add_argument("--x0", type=int, default=0); ap.add_argument("--width", type=int, default=0)
ap.add_argument("--side", type=float, default=0.12); ap.add_argument("--top", type=float, default=0.30)
ap.add_argument("--solid", type=int, default=10)
ap.add_argument("--headroom", type=float, default=0, help="crop the top to this fraction of headroom above the content; top fade covers it")
o = ap.parse_args()

def ss(x, lo, hi):
    t = np.clip((x - lo) / (hi - lo), 0, 1); return t * t * (3 - 2 * t)

im = np.asarray(Image.open(o.src).convert("RGBA")).astype(np.float32) / 255
rgb, a = im[..., :3], im[..., 3]
mn, mx = rgb.min(-1), rgb.max(-1)
sat = (mx - mn) / np.maximum(mx, 1e-3)
# 1. remove the near-white paper-wash haze the model leaves at partial alpha
white = ss(mn, 0.55, 0.78) * (1 - ss(sat, 0.10, 0.22))
keep = ss(a, 0.88, 0.97)
a2 = a * (1 - white * (1 - keep))
# 2. defringe: partial-alpha pixels take the colour of nearby solid paint
solid = (a > 0.92).astype(np.float32)
den = gaussian_filter(solid, 4) + 1e-4
bled = np.dstack([gaussian_filter(rgb[..., c] * solid, 4) / den for c in range(3)])
mix = (1 - keep)[..., None] * (den[..., None] > 0.02)
rgb = rgb * (1 - mix) + bled * mix
a2 = a2 * (0.6 + 0.4 * keep)
a2 = np.where(a2 < 0.10, 0, a2)
# 3. crop
w0 = o.width or rgb.shape[1]
y0 = 0
if o.headroom:
    cols = slice(o.x0, o.x0 + w0)
    rows = np.where(((a2[:o.bottom, cols] > 0.3).sum(1)) >= 3)[0]
    top = int(rows[0])
    y0 = max(0, int(round(top - o.headroom * (o.bottom - top) / (1 - o.headroom))))
    o.top = min(o.top, (top - y0) / (o.bottom - y0) * 1.1) if o.top else 0
sl = (slice(y0, o.bottom), slice(o.x0, o.x0 + w0))
rgb, a2, bled = rgb[sl], a2[sl], bled[sl]
h, w = a2.shape
# 4. crisp bottom: ramp to opaque over the last N rows, filling gaps with bled colour
if o.solid:
    # fill colour: wide blur of solid paint in the bottom band, falling back to its mean
    band = solid[sl][-40:]; brgb = rgb[-40:]
    wden = gaussian_filter(band, 20) + 1e-4
    mean = (brgb * band[..., None]).sum((0, 1)) / max(band.sum(), 1)
    wb = np.dstack([gaussian_filter(brgb[..., c] * band, 20) / wden for c in range(3)])
    conf = ss(wden, 0.02, 0.15)[..., None]
    wb = wb * conf + mean * (1 - conf)
    bled = bled.copy(); bled[-40:] = wb
    r = ss(np.arange(h, dtype=np.float32), h - o.solid, h - 1)[:, None]
    fill = r * (1 - a2)
    rgb = rgb * (1 - fill[..., None]) + bled * fill[..., None]
    a2 = np.maximum(a2, r)
# 5. soft fade at the sides and top only
x = np.linspace(0, 1, w)[None, :]; y = np.linspace(0, 1, h)[:, None]
a2 = a2 * ss(x, 0, o.side) * ss(1 - x, 0, o.side) * ss(y, 0, o.top)
Image.fromarray((np.dstack([rgb, a2]) * 255 + 0.5).astype(np.uint8), "RGBA").save(o.dst, optimize=True)
print(o.dst, w, h, "y0", y0)
