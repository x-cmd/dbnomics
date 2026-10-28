# DBnomics 与本站

DBnomics（db.nomics.world）聚合 IMF、世界银行、OECD、Eurostat、ECB、BIS 等 70+ 官方机构的时序数据，统一成一套免费 API。本站 = **经济学知识 + 数据图表**：每一页讲一个宏观主题，每张图都是 x-cmd draw 渲染的**明文 URL** — 数据就在链接里，AI 可直接读，点开即参数。

命令行取数（模块参数帮助见 [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)）：

```sh
x dbnomics data imf.cn.gdp.growth        # 单序列
x dbnomics align imf.us.gdp imf.cn.gdp   # 多序列对齐
x dbnomics alias                          # 预置别名表
```

本站数据口径：IMF WEO 2025（含预测）· BIS 政策利率（年末切片）。所有图 2025 年为最新值。

**快速开始**：复制任何一张图的 URL 到你的 markdown；或让 AI agent 加载 [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) 后说"用 draw 画中美 GDP 对比"。
