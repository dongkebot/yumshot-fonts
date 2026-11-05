# YumShot 字体库

YumShot 海报模版和 `yumshot-poster-design` skill 共用的字体，放在这里供所有线程和工作区调用。全部为 SIL OFL 1.1：可商用、可嵌入 App 和导出图片；不得单独售卖字体文件；分发时附许可文本（各目录 `licenses/`）。

| 目录 | 内容 | 什么时候用 |
|---|---|---|
| `web/` | 模版库 30 款 woff2 子集（约 17 MB）+ `fonts.css` + `字体清单.md` | 网页 / 画布渲染、出预览。子集覆盖 GB2312 一级 3755 字 + 常见菜单字 + 模版用字 |
| `full/` | 8 类风格字体包：8 个家族、16 个完整 TTF / OTF（约 142 MB）+ 映射表、字样图、逐字体许可 | 菜名有生僻字、子集缺字时；导出给 App 时 |
| `manifest.json` | 每个文件的 key、CSS 名、字重、路径、大小、SHA-256；8 类风格 → 文件映射 | 程序读取 |
| `tools/fetch_fonts.py` | 按需下载并校验 SHA，只用标准库 | 只要几款字体时 |

## 三种取法

**1. 只要几款（推荐）**：单独下载脚本，按 key / 风格取。

```bash
curl -sSLO https://raw.githubusercontent.com/dongkebot/yumshot-fonts/main/tools/fetch_fonts.py
python3 fetch_fonts.py --list                         # 看有哪些
python3 fetch_fonts.py --web --out ./fonts            # 30 款 woff2 + fonts.css
python3 fetch_fonts.py --key song hei mont --out ./fonts
python3 fetch_fonts.py --style 手写暖感 --out ./fonts   # 8 类之一的完整字体
```

输出保持仓库相对路径，网页里引用 `fonts/web/fonts.css` 即可，`font-family` 名（`YS Song`、`YS Hei`…）与模版 CSS 一致。

**2. 只要网页字体**：

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/dongkebot/yumshot-fonts
cd yumshot-fonts && git sparse-checkout set web
```

**3. 全部**：`git clone --depth 1 https://github.com/dongkebot/yumshot-fonts`（约 160 MB）。

仓库是私有的时候：工作区里先把仓库加进当前会话；单独用脚本时设置 `GITHUB_TOKEN`。

## 两套之间怎么对应

- 用 woff2 画布出图时，思源黑体用 `hei`、思源宋体用 `song`（Noto Sans / Serif SC 可变字体，与完整包里的 Source Han 同一套设计），其余同名直接对应。
- 只有 `full/` 里的完整字体能保证覆盖所有菜名用字；子集缺字时换完整字体，并实际渲染检查。
- 30 款里有 18 款（霞鹜漫黑、文楷、未来荧黑、得意黑、朱雀仿宋、马善政、Playfair、Anton 等）只有 woff2 子集；需要完整版时从 `web/字体清单.md` 的「来源」列下载，连同许可文件一起提交到 `full/`。

## 新增字体

只收可商用许可的字体，连同许可文件一起提交，并重新生成 `manifest.json`（`python3 tools/build_manifest.py`）。
