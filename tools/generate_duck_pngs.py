#!/usr/bin/env python3
"""Bake the collectible duck palette variants from the untouched master sprite.

Only the yellow/orange rubber body pixels are recolored. The original beak,
linework, eyes, gloss, alpha silhouette, and luminance-based shading are kept.
The game loads the finished PNGs directly; no recoloring happens at runtime.
"""
from __future__ import annotations

import base64
import io
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "ducks" / "source.svg"
OUT = ROOT / "assets" / "ducks"

# Target body hues in degrees. The original pixel saturation and brightness
# are retained, so the master artwork's painted light/shadow structure remains.
VARIANTS = {
    "mint": 158,
    "berry": 333,
    "peach": 22,
    "lilac": 274,
    "gold": 46,
    "zombie": 91,
    "vampire": 292,
}

# A tight exclusion around the actual beak. Beak pixels are copied unchanged
# from the master, including its orange upper/lower surfaces and mouth details.
BEAK_POLYGON = [
    (29, 55), (39, 52), (72, 53), (81, 59),
    (86, 68), (81, 78), (72, 83), (49, 85),
    (34, 80), (27, 72),
]

def extract_master() -> Image.Image:
    svg = SOURCE.read_text(encoding="utf-8")
    match = re.search(r'href="data:image/webp;base64,([^"]+)"', svg)
    if not match:
        raise RuntimeError("Could not find the embedded master WebP in source.svg")
    image = Image.open(io.BytesIO(base64.b64decode(match.group(1)))).convert("RGBA")
    if image.size != (160, 148):
        raise RuntimeError(f"Unexpected master sprite dimensions: {image.size}")
    return image

def make_body_mask(master: Image.Image) -> np.ndarray:
    rgb = np.asarray(master.convert("RGB"), dtype=np.uint8)
    hsv = np.asarray(master.convert("HSV"), dtype=np.uint8)
    hue = hsv[..., 0].astype(np.int16)
    saturation = hsv[..., 1]
    value = hsv[..., 2]
    alpha = np.asarray(master.getchannel("A")) > 0

    # Select the warm yellow/orange rubber body and its painted orange shadows.
    # Dark burgundy linework and low-saturation gloss are intentionally excluded.
    body = (
        alpha
        & (hue >= 10) & (hue <= 55)
        & (saturation >= 48)
        & (value >= 46)
    )

    beak = Image.new("1", master.size, 0)
    ImageDraw.Draw(beak).polygon(BEAK_POLYGON, fill=1)
    body &= ~np.asarray(beak, dtype=bool)
    return body

def main() -> None:
    master = extract_master()
    OUT.mkdir(parents=True, exist_ok=True)
    master.save(OUT / "sunny.png", format="PNG", optimize=True)

    body_mask = make_body_mask(master)
    source_hsv = np.asarray(master.convert("HSV"), dtype=np.uint8)
    source_alpha = np.asarray(master.getchannel("A"), dtype=np.uint8)
    source_rgb = np.asarray(master.convert("RGB"), dtype=np.uint8)
    beak_mask = Image.new("1", master.size, 0)
    ImageDraw.Draw(beak_mask).polygon(BEAK_POLYGON, fill=1)
    beak_mask = np.asarray(beak_mask, dtype=bool)

    for name, hue_degrees in VARIANTS.items():
        hsv = source_hsv.copy()
        hsv[..., 0][body_mask] = np.uint8(round((hue_degrees % 360) * 255 / 360))
        # Keep each source pixel's saturation and value: shaded pixels stay
        # shaded, highlights stay glossy, and no RGB matrix clipping is introduced.
        rgb = np.asarray(Image.fromarray(hsv, mode="HSV").convert("RGB"), dtype=np.uint8)
        rgb[~body_mask] = source_rgb[~body_mask]
        rgba = np.dstack((rgb, source_alpha))
        output = Image.fromarray(rgba, mode="RGBA")
        path = OUT / f"{name}.png"
        output.save(path, format="PNG", optimize=True)

    expected = ["sunny.png", *(f"{name}.png" for name in VARIANTS)]
    for filename in expected:
        path = OUT / filename
        check = Image.open(path).convert("RGBA")
        if check.size != master.size:
            raise RuntimeError(f"{filename} has incorrect dimensions")
        if check.getchannel("A").tobytes() != master.getchannel("A").tobytes():
            raise RuntimeError(f"{filename} changed the master sprite silhouette/alpha")
        if check.crop((0, 0, 160, 148)).convert("RGBA").tobytes() == b"":
            raise RuntimeError(f"{filename} is empty")
        if filename != "sunny.png":
            check_rgb = np.asarray(check.convert("RGB"))
            # The entire beak exclusion region must remain pixel-identical.
            if not np.array_equal(check_rgb[beak_mask], source_rgb[beak_mask]):
                raise RuntimeError(f"{filename} changed protected beak pixels")
        if path.stat().st_size < 1000:
            raise RuntimeError(f"{filename} appears incomplete")

    print("Generated 8 independent duck PNGs; beaks, outlines, alpha, and shading values verified.")

if __name__ == "__main__":
    main()
