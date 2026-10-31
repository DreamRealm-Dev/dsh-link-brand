# DSH Link brand assets

**English** | [简体中文](README.zh.md)

This repository holds the **DSH Link** brand artwork: the mark (ring, whale and LINK stem),
the wordmark (`dsh` with the whale in the bowl of its `d` plus LINK), their mono and white
variants, and the generated application-icon plates.

**Why a separate repository.** The DSH Link source code is MIT. The brand artwork is deliberately
not: it is licensed **CC BY-NC-SA 4.0**, so the name and the mark cannot be absorbed by a commercial
product or presented as somebody else's identity. Keeping the artwork in its own repository makes the
boundary mechanical — the code repository's MIT licence covers code, this repository's licence covers
artwork. The design is our own; no DeepSeek Harness mark is used, and nothing here claims official
endorsement (see [USAGE.md](USAGE.md)).

## Contents

| Path | What |
|---|---|
| `svg/symbol-v2.svg` | the mark: ring, whale and the LINK stem, 96×96 |
| `svg/symbol-v2-mono.svg`, `svg/symbol-v2-mono-accent.svg`, `svg/symbol-v2-white.svg` | the same geometry in one ink / one ink + accent / white |
| `svg/dsh-link-in-d.svg` | the wordmark: `dsh` with the whale in the `d` bowl plus LINK, 141.43×27.9 |
| `svg/dsh-link-in-d-mono.svg`, `svg/dsh-link-in-d-white.svg` | wordmark in one ink / white |
| `svg/dsh-link-in-d-lg*.svg` | the large wordmark (same design, larger optical size) |
| `png/symbol-v2-{16,24,32,48,64,128,256,512,1024}.png` | the design's own renders of the mark |
| `png/symbol-v2-{mono,mono-accent,white}-512.png`, `png/symbol-v2-dark.png` | the variant renders |
| `png/dsh-link-in-d{,-lg}{,-mono,-white}-{256,512,1024,1600}.png`, `png/dsh-link-in-d-white-dark.png` | wordmark renders |
| `png/dsh-link-v2.ico` | multi-size icon built from the mark |
| `plated/windows-<n>.png`, `plated/macos-<n>.png` | white rounded plate + mark, the two plate geometries the application icon uses |
| `scripts/gen-plated-icons.py` | regenerates `plated/` from `png/` (Pillow) |
| `LICENSE` | CC BY-NC-SA 4.0 legal code |
| `USAGE.md` | usage scope, attribution format, trademark and endorsement rules |
| `PROVENANCE.md` | where the artwork comes from and how it is generated |

## Licence

The artwork in this repository is licensed under
**[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE)**
(SPDX: `CC-BY-NC-SA-4.0`).

- **Share / adapt** for non-commercial purposes, with attribution and under the same licence.
- **Commercial use, trademark use, or implying endorsement** requires separate permission.
- The full scope — what is allowed, what is not, and how to attribute — is in [USAGE.md](USAGE.md).

The DSH Link source code is a different work: <https://github.com/DreamRealm-Dev/dsh-link>
under the MIT licence. The copies of this artwork that ship inside that repository
(`plugins/dsh-link-brand/assets/`) stay under this repository's licence, not MIT.

## Attribution

> "DSH Link brand artwork" by DSH Link contributors, licensed under CC BY-NC-SA 4.0.
> Source: https://github.com/DreamRealm-Dev/dsh-link-brand. Modified versions must be marked as modified.

## Provenance and generation

The SVG sources are author-owned designs (logo project `set3`, rev 3) — no third-party artwork and
no upstream logo. The `plated/` ladder is generated from `png/` by `scripts/gen-plated-icons.py`.
See [PROVENANCE.md](PROVENANCE.md) for the full record.

DSH Link is a third-party desktop edition of DeepSeek Harness; DeepSeek and DeepSeek Harness are
trademarks of their respective owner, and this repository neither uses their marks nor claims
affiliation.
