# Economics you can see

Every chart on this site is a link. Open it and the picture appears; read the link and you get the numbers behind it — the data lives inside the URL, so an AI agent can read it too. The subjects are the ones that decide how your week goes: jobs, prices, growth, debt, and what the biggest economies on earth are actually doing.

The site runs in six sections, and they read in one direction: **what to look at → what rule binds it → what one economy looks like up close**. Indicators (GDP, growth, inflation, unemployment, debt, the balance with the world, policy rates, people and savings) · macroeconomics (five laws: Phillips, Okun, Wagner, Beveridge, Laffer) · and three case studies — Europe, the United States, China.

Not sure where to begin? These six pages are the ones people argue about — and each one answers a question you already have.

**Three economies, three arguments.** The US, the euro area and China on the same dials: whose job market is tight, whose prices are calm, who is still growing, who is borrowing the most. Everybody has an opinion; here is the data — and the places where the data refuses to settle it.

**Your job and your shopping basket sit on the same seesaw.** The Phillips curve is the oldest rule in macroeconomics: when prices rise, jobs get scarcer, so governments have to pick which one they want more of. America just rode the smoothest version in forty years.

**How can a city have jobs nobody wants and people who need one?** The Beveridge curve traces vacancies against unemployment. It normally slopes downward; the pandemic bent it outward, and it has not fully straightened since.

**The one indicator that has called every American recession for sixty years.** When the 10-year Treasury yield falls below the 3-month, the market is betting that the central bank will cut — and a recession usually follows. It inverted in 2022 and 2023; 2025 re-steepened.

**Fifty economies, one credit card.** Washington runs a single fiscal policy, a single Fed map and a single bankruptcy court for states that share a currency and almost nothing else. New York and Mississippi are a factor of 2.2 apart, and 24 years of "convergence" did not close it.

**One country, two economies.** On China's coast a factory town can out-earn an entire province up north. The gap narrowed from 11.7 times to 4.3 — but the people moved the other way: Guangdong is 55 million people larger than it was in 2000.

How to read a chart here: click it. The URL *is* the chart, and the numbers are in plain sight inside it. The data is one command away (module help: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth         # one series
x dbnomics align imf.us.gdp imf.cn.gdp    # multi-series, aligned
x dbnomics alias                           # preset alias table
```

Data vintage: the IMF's *World Economic Outlook* (2025 edition, forecasts included) and BIS policy rates; the state and province pages use the OECD's regional database. Every chart uses 2025 as its latest year. **Quick start**: paste any chart URL into a document, or point an AI agent at the [draw skill](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) and ask it to chart US vs China GDP.
