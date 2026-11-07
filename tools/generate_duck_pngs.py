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
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "ducks" / "source.svg"
OUT = ROOT / "assets" / "ducks"

# Target body hues in degrees. The original pixel saturation and brightness
# are retained, so the master artwork's painted light/shadow structure remains.
VARIANTS = {
    "mint": (158, 0.58),
    "berry": (333, 0.58),
    "peach": (22, 0.62),
    "lilac": (274, 0.58),
    "gold": (46, 0.86),
    "zombie": (91, 0.58),
    "vampire": (292, 0.58),
}

# The beak sits in this small search window. Protect it by its actual orange
# pixel color, not a broad polygon: a polygon also protects nearby yellow cheek
# and body pixels, which then remain Sunny-yellow on every recolored duck.
BEAK_WINDOW = (24, 50, 84, 86)  # left, top, right, bottom
BEAK_HUE_MAX = 18               # orange hues only; yellow body is beyond this
BEAK_MIN_SATURATION = 72

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
    # Include low-saturation and darker warm body-shadow pixels as well as
    # bright yellow pixels. The previous high saturation cutoff left islands
    # of original yellow inside the recolored body, especially in shaded areas.
    # The master outline is darker/browner (outside this hue band), while gloss
    # is protected by its near-neutral hue.
    body = (
        alpha
        & (hue >= 10) & (hue <= 55)
        & (saturation >= 12)
        & (value >= 30)
    )

    # Preserve only saturated orange pixels in the beak's local window.
    # The mouth/outline pixels are already outside the warm-body selection;
    # nearby yellow pixels remain eligible for recoloring.
    left, top, right, bottom = BEAK_WINDOW
    beak = np.zeros(master.size, dtype=bool)
    local_hue = hue[top:bottom, left:right]
    local_sat = saturation[top:bottom, left:right]
    local_val = value[top:bottom, left:right]
    local_alpha = alpha[top:bottom, left:right]
    beak[top:bottom, left:right] = (
        local_alpha
        & (local_hue <= BEAK_HUE_MAX)
        & (local_sat >= BEAK_MIN_SATURATION)
        & (local_val >= 55)
    )
    body &= ~beak
    return body

def main() -> None:
    master = extract_master()
    OUT.mkdir(parents=True, exist_ok=True)
    master.save(OUT / "sunny.png", format="PNG", optimize=True)

    body_mask = make_body_mask(master)
    source_hsv = np.asarray(master.convert("HSV"), dtype=np.uint8)
    source_alpha = np.asarray(master.getchannel("A"), dtype=np.uint8)
    source_rgb = np.asarray(master.convert("RGB"), dtype=np.uint8)
    # Recreate the same pixel-accurate orange-beak protection mask for QA.
    hsv = source_hsv
    hue = hsv[..., 0].astype(np.int16)
    saturation = hsv[..., 1]
    value = hsv[..., 2]
    left, top, right, bottom = BEAK_WINDOW
    beak_mask = np.zeros(master.size, dtype=bool)
    beak_mask[top:bottom, left:right] = (
        (source_alpha[top:bottom, left:right] > 0)
        & (hue[top:bottom, left:right] <= BEAK_HUE_MAX)
        & (saturation[top:bottom, left:right] >= BEAK_MIN_SATURATION)
        & (value[top:bottom, left:right] >= 55)
    )

    for name, (hue_degrees, saturation_factor) in VARIANTS.items():
        hsv = source_hsv.copy()
        hsv[..., 0][body_mask] = np.uint8(round((hue_degrees % 360) * 255 / 360))
        hsv[..., 1][body_mask] = np.clip(
            hsv[..., 1][body_mask].astype(np.float32) * saturation_factor,
            0, 255
        ).astype(np.uint8)
        # Preserve each source pixel's value and relative saturation structure:
        # shadow transitions remain continuous and highlights stay glossy.
        rgb = np.asarray(Image.fromarray(hsv, mode="HSV").convert("RGB"), dtype=np.uint8).copy()
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
