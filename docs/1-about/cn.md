# DBnomics 是什么

DBnomics（db.nomics.world）是全球最大的免费宏观经济数据聚合平台之一，由法国团队维护，聚合 IMF、世界银行、OECD、Eurostat、欧洲央行、BIS 等 70+ 官方机构的时序数据，统一成一套 Web API。

> 我们看重的三件事：**数据免费且权威**（官方源直达）、**API 统一**（一套参数取所有机构）、**被高质量引用**（欧盟与国际组织常用其数据）。

本站（x-cmd.com/dbnomics）做两件事：

1. **经济学知识展示** — 每一页讲一个宏观经济指标：它度量什么、为什么重要、怎么读图。所有图都是 x-cmd draw 渲染的**明文 URL**（数据就在链接里，AI 可直接读）。
2. **数据入口** — 命令行直接取数：`x dbnomics` 模块封装了 DBnomics API。参数与子命令帮助见 [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)。

```sh
x dbnomics data imf.cn.gdp.growth      # 中国 GDP 增速(IMF WEO)
x dbnomics align imf.us.cpi imf.cn.cpi # 中美 CPI 对齐
```

本页之下各页的每张图都可以：点击打开（即参数）、复制 URL 进你的文档、改参数重生成。
