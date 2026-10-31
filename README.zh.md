# DSH Link 品牌素材

[English](README.md) | **简体中文**

本仓库保存 **DSH Link** 的品牌素材：标志（环、鲸与 LINK 字干）、字标（`dsh`，鲸在 `d` 的
碗里，后接 LINK）、它们的单色/白色变体，以及由素材生成的应用图标底板。

**为什么单独开一个仓库。** DSH Link 源码是 MIT；品牌素材**刻意不采用 MIT**，而是
**CC BY-NC-SA 4.0**——这样名称与标志不会被商业产品吸收，也不会被当成别人的身份。素材独立成库，
边界就是机械的：代码仓库的 MIT 只覆盖代码，本仓库的许可证只覆盖素材。设计是我们的原创；没有使用
DeepSeek Harness 的商标素材，本仓库也不声称获得官方背书（见 [USAGE.md](USAGE.md)）。

## 目录

| 路径 | 内容 |
|---|---|
| `svg/symbol-v2.svg` | 标志：环、鲸与 LINK 字干，96×96 |
| `svg/symbol-v2-mono.svg`、`symbol-v2-mono-accent.svg`、`symbol-v2-white.svg` | 同一几何的单墨色 / 单墨色+强调色 / 白色版本 |
| `svg/dsh-link-in-d.svg` | 字标：`dsh`（鲸在 `d` 的碗里）+ LINK，141.43×27.9 |
| `svg/dsh-link-in-d-mono.svg`、`dsh-link-in-d-white.svg` | 字标的单墨色 / 白色版本 |
| `svg/dsh-link-in-d-lg*.svg` | 大字标（同一设计，更大的光学尺寸） |
| `png/` | 设计自己的位图导出（标志 16…1024、各变体、字标 256…1600）与多尺寸 `.ico` |
| `plated/windows-<n>.png`、`plated/macos-<n>.png` | 白底圆角底板 + 标志，应用图标使用的两种底板几何 |
| `scripts/gen-plated-icons.py` | 由 `png/` 重新生成 `plated/`（Pillow） |
| `LICENSE` | CC BY-NC-SA 4.0 法律文本 |
| `USAGE.md` | 使用范围、署名格式、商标与背书规则 |
| `PROVENANCE.md` | 素材来源与生成方式 |

## 许可

本仓库素材采用 **[知识共享 署名-非商业性使用-相同方式共享 4.0 国际](LICENSE)**
（SPDX：`CC-BY-NC-SA-4.0`）。

- **非商业目的**可共享、可改编；需署名，改编作品需以同一许可发布。
- **商业使用、商标性使用、暗示背书**需要另行获得许可。
- 完整范围（允许什么、不允许什么、如何署名）见 [USAGE.md](USAGE.md)。

DSH Link 源码是另一件作品：<https://github.com/DreamRealm-Dev/dsh-link>，MIT。源码仓库内随附的
本素材副本（`plugins/dsh-link-brand/assets/`）仍适用本仓库的许可证，**不是** MIT。

## 署名

> “DSH Link 品牌素材”，作者 DSH Link contributors，采用 CC BY-NC-SA 4.0 许可。
> 来源：https://github.com/DreamRealm-Dev/dsh-link-brand。修改过的版本必须标注为已修改。

## 来源与生成

SVG 源文件为作者自有设计（logo 项目 `set3` rev 3），不含第三方素材，也不含上游商标。`plated/`
由 `scripts/gen-plated-icons.py` 从 `png/` 生成。完整记录见 [PROVENANCE.md](PROVENANCE.md)。

DSH Link 是 DeepSeek Harness 的第三方桌面版；DeepSeek 与 DeepSeek Harness 是其各自权利人的商标，
本仓库既不使用其商标素材，也不声称关联。
