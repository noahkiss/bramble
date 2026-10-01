# /// script
# dependencies = ["numpy", "pillow", "scipy"]
# ///
import sys, numpy as np
from scipy.ndimage import gaussian_filter
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
side = float(sys.argv[3]) if len(sys.argv) > 3 else 0.12
im = np.asarray(Image.open(src).convert("RGBA")).astype(np.float32) / 255
rgb, a = im[..., :3], im[..., 3]
mn, mx = rgb.min(-1), rgb.max(-1)
sat = (mx - mn) / np.maximum(mx, 1e-3)
def ss(x, lo, hi):
    t = np.clip((x - lo) / (hi - lo), 0, 1); return t * t * (3 - 2 * t)
white = ss(mn, 0.55, 0.78) * (1 - ss(sat, 0.10, 0.22))   # paper-like haze
keep = ss(a, 0.88, 0.97)                                  # solid paint stays
a2 = a * (1 - white * (1 - keep))
# defringe: semi-transparent pixels take the colour of nearby solid paint
solid = (a > 0.92).astype(np.float32)
den = gaussian_filter(solid, 4) + 1e-4
bled = np.dstack([gaussian_filter(rgb[..., c] * solid, 4) / den for c in range(3)])
mix = (1 - keep)[..., None] * (den[..., None] > 0.02)
rgb = rgb * (1 - mix) + bled * mix
a2 = a2 * (0.6 + 0.4 * keep)
# drop faint residue
a2 = np.where(a2 < 0.10, 0, a2)
h, w = a.shape
x = np.linspace(0, 1, w)[None, :]; y = np.linspace(0, 1, h)[:, None]
fx = ss(x, 0, side) * ss(1 - x, 0, side)
fy = ss(y, 0.0, 0.30)
a2 = a2 * fx * fy
out = np.dstack([rgb, a2])
Image.fromarray((out * 255 + 0.5).astype(np.uint8), "RGBA").save(dst, optimize=True)
