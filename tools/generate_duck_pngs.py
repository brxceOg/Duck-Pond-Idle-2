#!/usr/bin/env python3
"""Generate standalone PNG duck variants from the canonical embedded WebP.

The source sprite remains untouched. The same SVG color-matrix operations used by
the previous artwork pass are baked into each PNG at build time; the game itself
loads only finished raster images and performs no runtime recoloring.
"""
from __future__ import annotations

import base64
import io
import re
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "ducks" / "source.svg"
OUT = ROOT / "assets" / "ducks"

# These are the approved hues/saturation levels from the existing duck designs.
VARIANTS = {
    "mint": (97, 0.58),
    "berry": (-78, 0.58),
    "peach": (-18, 0.62),
    "lilac": (-138, 0.58),
    "gold": (-5, 0.86),
    "zombie": (42, 0.58),
    "vampire": (-108, 0.58),
}

def clamp_rgb(values: np.ndarray) -> np.ndarray:
    return np.clip(values, 0.0, 1.0)

def hue_rotate(rgb: np.ndarray, degrees: float) -> np.ndarray:
    angle = np.deg2rad(degrees)
    c, s = np.cos(angle), np.sin(angle)
    matrix = np.array([
        [0.213 + c * 0.787 - s * 0.213,
         0.715 - c * 0.715 - s * 0.715,
         0.072 - c * 0.072 + s * 0.928],
        [0.213 - c * 0.213 + s * 0.143,
         0.715 + c * 0.285 + s * 0.140,
         0.072 - c * 0.072 - s * 0.283],
        [0.213 - c * 0.213 - s * 0.787,
         0.715 - c * 0.715 + s * 0.715,
         0.072 + c * 0.928 + s * 0.072],
    ], dtype=np.float32)
    return clamp_rgb(rgb @ matrix.T)

def saturate(rgb: np.ndarray, amount: float) -> np.ndarray:
    matrix = np.array([
        [0.213 + 0.787 * amount, 0.715 - 0.715 * amount, 0.072 - 0.072 * amount],
        [0.213 - 0.213 * amount, 0.715 + 0.285 * amount, 0.072 - 0.072 * amount],
        [0.213 - 0.213 * amount, 0.715 - 0.715 * amount, 0.072 + 0.928 * amount],
    ], dtype=np.float32)
    return clamp_rgb(rgb @ matrix.T)

def extract_master() -> Image.Image:
    svg = SOURCE.read_text(encoding="utf-8")
    match = re.search(r'href="data:image/webp;base64,([^"]+)"', svg)
    if not match:
        raise RuntimeError("Could not find the embedded master WebP in source.svg")
    raw = base64.b64decode(match.group(1))
    image = Image.open(io.BytesIO(raw)).convert("RGBA")
    if image.size != (160, 148):
        raise RuntimeError(f"Unexpected master sprite dimensions: {image.size}")
    return image

def main() -> None:
    master = extract_master()
    OUT.mkdir(parents=True, exist_ok=True)
    master.save(OUT / "sunny.png", format="PNG", optimize=True)

    rgba = np.asarray(master, dtype=np.float32) / 255.0
    source_rgb = rgba[..., :3]
    source_alpha = rgba[..., 3]

    # This reproduces the previous targeted body-color mask from its SVG
    # feColorMatrix: alpha = -.5R + 1.5G - B, followed by slope 12.
    # Warm orange beak pixels, dark linework, eyes, and white highlights therefore
    # remain from the original master instead of being hue-shifted.
    body_mask = np.clip((-0.5 * source_rgb[..., 0]
                         + 1.5 * source_rgb[..., 1]
                         - source_rgb[..., 2]) * 12.0, 0.0, 1.0)
    body_mask *= (source_alpha > 0).astype(np.float32)

    for name, (hue, saturation_amount) in VARIANTS.items():
        transformed = saturate(hue_rotate(source_rgb, hue), saturation_amount)
        blend = body_mask[..., None]
        result_rgb = source_rgb * (1.0 - blend) + transformed * blend
        result = np.dstack((np.clip(result_rgb * 255.0 + 0.5, 0, 255),
                            rgba[..., 3] * 255.0 + 0.5)).astype(np.uint8)
        Image.fromarray(result, mode="RGBA").save(
            OUT / f"{name}.png", format="PNG", optimize=True
        )

    expected = ["sunny.png", *(f"{name}.png" for name in VARIANTS)]
    for filename in expected:
        path = OUT / filename
        check = Image.open(path).convert("RGBA")
        if check.size != master.size:
            raise RuntimeError(f"{filename} has incorrect dimensions")
        if check.getchannel("A").tobytes() != master.getchannel("A").tobytes():
            raise RuntimeError(f"{filename} changed the master sprite silhouette/alpha")
        if path.stat().st_size < 1000:
            raise RuntimeError(f"{filename} appears incomplete")
    print("Generated and verified 8 independent duck PNGs from source.svg")

if __name__ == "__main__":
    main()
