# 这个网站是什么

DBnomics 是一个免费资料库，把各官方来源的经济时间序列——IMF、世界银行、OECD、Eurostat、各国央行——收在一起，只用一个 API 就能取到。这个网站用这套资料库讲经济学：一页一个话题，每张图都是一个普通网页链接。打开链接，数字就写在 URL 里；粘到任何文档里照样能用。

你也可以自己在命令行里取数据（模块帮助：[x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)）：

```sh
x dbnomics data imf.cn.gdp.growth        # 单序列
x dbnomics align imf.us.gdp imf.cn.gdp   # 多序列对齐
x dbnomics alias                          # 预置别名表
```

数据版本：IMF 的《世界经济展望》（*World Economic Outlook*，2025 年版，含预测）和 BIS 政策利率。每张图都以 2025 年为最新年份。

**快速上手**：把任意图表链接粘进文档；或者让 AI 智能体参考 [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md)，让它画一张美国与中国 GDP 的对比图。
