# 海报设计实际字体包 · 8类风格

打包日期：2026-10-23。共8个字体家族、16个完整原始字体文件。字体按家族存放，映射表按8类风格引用，同一文件不重复打包。

## 使用

解压后在Mac上选中需要的 .ttf/.otf 文件，用「字体册」打开并安装；已有同名字体先比较版本，避免重复安装。Windows可从字体文件右键安装。具体设计软件需在安装后刷新字体列表或重新启动。

本包不会自动安装字体或修改配置。原海报Skill压缩包保持不变；将本包与它一起迁移即可。目标机的字体索引仍需重新生成，不可套用源机器路径。

## 8类风格匹配

- **手写暖感**：Yozai, Yozai-Bold。悠哉 Regular 400用于自然手写正文，Bold 700用于短标题；保持不规则笔画，不做机械拉伸。
- **重响·超重无衬线／黑体**：SourceHanSansSC-Heavy, Montserrat-Thin。思源黑体 Heavy 900为中文主标题；Montserrat 可变字体用800–900。
- **圆润波普·友善**：JiangChengYuanTi-500W, JiangChengYuanTi-700W, Gabarito-Regular。江城圆体500W为亲和信息文字，700W用于标题；Gabarito可变400–900，波普标题建议800–900。
- **高对比衬线·精致权威**：SourceHanSerifCN-Heavy, SourceHanSerifCN-Bold, Alegreya-BlackItalic, Alegreya-Regular。中文用思源宋体Heavy 900或Bold 700建立粗细对比；英文Alegreya Black Italic 900作为强调。Alegreya偏文学与书写性，不是Didot/Bodoni式极端细衬线。
- **宋体明朝·文气安静**：SourceHanSerifCN-Regular, Alegreya-Regular。思源宋体Regular 400配Alegreya Regular 400，适合阅读和安静的编辑版式。
- **毛笔书法·文化正统**：LongCang-Regular。有字库龙藏体Regular 400作自然行书短标题。它是行书方向的近似匹配，不代表碑帖、楷书或庄重典礼字形；正文另配思源宋体。
- **中性 grotesque·通用**：SourceHanSansSC-Regular, Montserrat-Thin。中文思源黑体Regular 400；英文Montserrat用400–500。Montserrat是几何无衬线，作为中性通用方案，不等于传统grotesque原字体。
- **轻宽·优雅时装**：SourceHanSerifCN-ExtraLight, Montserrat-Thin, Alegreya-Italic。思源宋体ExtraLight的真实OS/2字重为250；Montserrat建议200–300，Alegreya Italic 400用于小段强调。宽松字距属于排版参数，不是字体宽度轴。

## 包内资料

- fonts/：16个完整TTF/OTF字体文件，原始字节保持不变；未做子集化、变体实例化或内部改名。
- 8类风格字体映射.json / .csv：对应字体文件路径和具体用法，CSV为UTF-8 BOM编码。
- 8类风格字样.png：包内字体直接渲染的中文/英文字样；用于选型，未模拟完整海报。
- 字体清单.json：PostScript名称、真实字重、可变轴、字形数量、版权和许可字段、样句缺字情况。
- licenses/：每个字体对应的原始许可与版权字段、文件SHA、完整OFL-1.1正文。
- manifest.json：全部包内文件的大小和SHA-256。

## 中文、英文与字重

Alegreya、Gabarito、Montserrat是本包中的拉丁字体，不提供中文字形；中文按映射表配对。中文候选均覆盖本次样句“春日限定，中文设计与留白。0123456789 ABC abc”，不保证任意生僻字都有。

Gabarito可变字重范围400–900，Montserrat为100–900。不同应用对可变字体的支持需在目标机确认；不要只看默认名称判断是否只有Regular/Thin。思源宋体ExtraLight的真实字重为250。其余静态字重以清单为准，不用软件伪粗或机械拉伸代替。

## 许可及来源

本次16个文件的当前内嵌元数据均明确声明SIL Open Font License 1.1，且fsType为0；文件SHA与已有本机索引一致。逐文件保留原始版权、制造者、设计者、许可声明和完整OFL正文。按照OFL条款使用、转交时保留这些材料，不单独售卖字体文件。

作者/官方在线参考已核对：Yozai、Source Han Sans、Source Han Serif、Alegreya、Gabarito、Montserrat；URL在逐字体JSON内。江城圆体根据当前文件自身许可核对，未额外确认作者发布页；Long Cang内嵌作者仓库本次返回404，同样以本次原文件的许可声明为证据，不声称在线版本已对齐。

本包含原海报/编辑器示例已绑定的7个字体文件，并按8类风格补充9个文件。新增字体是本次匹配候选，不冒充旧海报实际使用记录。8类属于视觉选型建议，尤其行书、几何无衬线和文学衬线仅按所述气质匹配，不保证复刻任意参考图原字形。

## 验证范围

已校验16个字体源文件SHA、名称、字重/可变轴、字符映射和许可字段，16个文件均通过FreeType实际加载与字样渲染，并查看8类字样。已验证ZIP CRC、逐文件SHA与桌面副本一致。未在接收方电脑安装、试排完整海报或验证特定应用的字体加载。
