#!/usr/bin/env python3
"""Regenerate the plated application-icon ladder from the mark's own renders.

    python scripts/gen-plated-icons.py

The plate geometry is the convention the upstream desktop icon uses -- the plate share of
the canvas and the corner radius only, not the artwork: Windows plate 93.75% / radius
18.75%, macOS plate 80.47% / radius 22.46%. The plate colour is #FBFBFB. The mark sits at
84% of the plate. A plate rather than a bare mark is the point: taskbars and tray surfaces
paint their own background and the mark's ink is dark.

Reads png/symbol-v2-<n>.png, writes plated/windows-<n>.png and plated/macos-<n>.png.
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PNG = os.path.join(REPO, 'png')
PLATED = os.path.join(REPO, 'plated')

PROFILES = {
    'windows': {'plate': 0.9375, 'radius': 0.1875},
    'macos': {'plate': 0.8046875, 'radius': 0.2246},
}
PLATE_FILL = (251, 251, 251, 255)
GLYPH_SHARE = 0.84
SUPERSAMPLE = 4
SIZES = [16, 24, 32, 48, 64, 128, 256, 512, 1024]


def render(profile: str, size: int) -> None:
    geometry = PROFILES[profile]
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    plate_size = size * geometry['plate']
    offset = (size - plate_size) / 2
    radius = plate_size * geometry['radius']
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(
        [offset, offset, offset + plate_size, offset + plate_size],
        radius=radius,
        fill=PLATE_FILL,
    )
    glyph_size = max(1, round(plate_size * GLYPH_SHARE))
    source = Image.open(os.path.join(PNG, 'symbol-v2-' + str(size) + '.png')).convert('RGBA')
    if source.size != (glyph_size, glyph_size):
        source = source.resize((glyph_size, glyph_size), Image.LANCZOS)
    position = ((size - glyph_size) // 2, (size - glyph_size) // 2)
    canvas.alpha_composite(source, position)
    canvas.save(os.path.join(PLATED, profile + '-' + str(size) + '.png'))


def main() -> None:
    os.makedirs(PLATED, exist_ok=True)
    for profile in PROFILES:
        for size in SIZES:
            render(profile, size)
    print('wrote ' + str(len(PROFILES) * len(SIZES)) + ' plated icons to ' + PLATED)


if __name__ == '__main__':
    main()
