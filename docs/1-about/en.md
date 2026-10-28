# DBnomics and this site

DBnomics (db.nomics.world) aggregates time series from IMF, World Bank, OECD, Eurostat, ECB, BIS and 70+ official providers behind one free API. This site = **economics knowledge + charts**: one macro theme per page, every chart a **plain URL rendered by x-cmd draw** — the data lives in the link, AI-readable, click to see the params.

Fetch from the shell (module help: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth         # one series
x dbnomics align imf.us.gdp imf.cn.gdp    # multi-series, aligned
x dbnomics alias                           # preset alias table
```

Data vintage here: IMF WEO 2025 (incl. projections) · BIS policy rates (year-end slice). All charts use 2025 as the latest value.

**Quick start**: paste any chart URL into your markdown; or point an AI agent at the [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) and ask it to chart US vs China GDP.
