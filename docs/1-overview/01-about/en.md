# What this site is

DBnomics is a free library that collects economic time series from official sources — the IMF, the World Bank, OECD, Eurostat, central banks — and puts them all behind one API. This site uses that library to explain economics: one topic per page, and every chart is a plain web link. Open the link and the numbers are right there in the URL; paste it into any document and it still works.

Pull the data yourself from the shell (module help: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth         # one series
x dbnomics align imf.us.gdp imf.cn.gdp    # multi-series, aligned
x dbnomics alias                           # preset alias table
```

Data vintage: IMF's *World Economic Outlook* (2025 edition, forecasts included) and BIS policy rates. Every chart uses 2025 as its latest year.

**Quick start**: paste any chart URL into a document; or point an AI agent at the [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) and ask it to chart US vs China GDP.
