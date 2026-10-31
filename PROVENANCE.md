# Provenance

These files are the DSH Link brand artwork, **rev 3** of the logo project ("set3"), designed by
this project's own contributors. No third-party artwork and no upstream mark is included.

- Original design set: `LOGO设计/dsh-link-logo/set3` (design working directory, not distributed).
- The SVG sources were copied unchanged into `svg/`; the PNG renders in `png/` are the design's own
  exports.
- `plated/` is generated from `png/symbol-v2-<n>.png` by `scripts/gen-plated-icons.py`; the plate
  geometry is the convention the upstream desktop icon uses (Windows: plate 93.75% of the canvas,
  corner radius 18.75% of the plate; macOS: 80.47% / 22.46%), and the plate colour is `#FBFBFB`.
  Only the geometry convention is shared; the artwork is ours.
- The main repository consumes these files under `plugins/dsh-link-brand/assets/` and derives its
  client mark components and boot-page mark from them.

DeepSeek Harness's own logo, wordmark, whale symbol and brand artwork are **not** part of this
repository and are not used in the DSH Link interface; see the main repository's `docs/brand.md`
and the upstream `BRAND_GUIDELINES.zh.md`.
