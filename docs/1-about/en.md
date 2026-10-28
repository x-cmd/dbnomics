# What is DBnomics

DBnomics (db.nomics.world) is one of the largest free macroeconomic data aggregators, maintained in France. It unifies time series from IMF, World Bank, OECD, Eurostat, ECB, BIS and 70+ official providers behind a single web API.

> Three things we value: **free and authoritative data** (straight from official sources), **one API** (same parameters for every provider), and **high-quality citations** (used by EU and international organisations).

This site (x-cmd.com/dbnomics) does two things:

1. **Economics knowledge pages** — each page explains one macro indicator: what it measures, why it matters, how to read the chart. Every chart is a **plain URL rendered by x-cmd draw** (the data lives in the link; an AI can read it without rendering).
2. **A data entry point** — the `x dbnomics` module wraps the DBnomics API. See [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics) for parameters and subcommands.

```sh
x dbnomics data imf.us.gdp.growth      # US GDP growth (IMF WEO)
x dbnomics align imf.us.cpi imf.cn.cpi # US vs China CPI, aligned
```

Every chart below can be: clicked open (the URL *is* the params), pasted into your docs, or tweaked and regenerated.
