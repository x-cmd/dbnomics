# Government debt

General government gross debt / GDP is the core sustainability indicator. The Maastricht treaty set a 60% reference line for the euro area (red line) — not a hard limit, but risk rises steeply once past it if r−g turns against you.

Reading guide:

- Japan ~250%, highest globally, yet stable for decades thanks to holder structure (domestic/central bank) and near-zero rates;
- Greece is the crisis case: post-2009 sovereign debt crisis, worked down via bailouts and restructuring;
- US above 120% and rising — mostly post-pandemic fiscal expansion.

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Government%20gross%20debt%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22Japan%22%2C%22Greece%22%2C%22Italy%22%2C%22USA%22%2C%22France%22%2C%22Spain%22%2C%22UK%22%2C%22China%22%2C%22Germany%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%20GDP%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B251.2%2C159.0%2C136.9%2C121.0%2C112.3%2C102.3%2C101.8%2C90.1%2C62.7%5D%2C%22markLine%22%3A%7B%22data%22%3A%5B%7B%22yAxis%22%3A60%7D%5D%2C%22lineStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Government%20gross%20debt%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22Japan%22%2C%22Greece%22%2C%22Italy%22%2C%22USA%22%2C%22France%22%2C%22Spain%22%2C%22UK%22%2C%22China%22%2C%22Germany%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%20GDP%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B251.2%2C159.0%2C136.9%2C121.0%2C112.3%2C102.3%2C101.8%2C90.1%2C62.7%5D%2C%22markLine%22%3A%7B%22data%22%3A%5B%7B%22yAxis%22%3A60%7D%5D%2C%22lineStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Government%20gross%20debt%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22Japan%22%2C%22Greece%22%2C%22Italy%22%2C%22USA%22%2C%22France%22%2C%22Spain%22%2C%22UK%22%2C%22China%22%2C%22Germany%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%20GDP%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B251.2%2C159.0%2C136.9%2C121.0%2C112.3%2C102.3%2C101.8%2C90.1%2C62.7%5D%2C%22markLine%22%3A%7B%22data%22%3A%5B%7B%22yAxis%22%3A60%7D%5D%2C%22lineStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%7D%5D%7D" width="760" alt="Government debt 2024, Maastricht line 60%"></a>

**Data**: IMF WEO (GGXWDG_NGDP), 2024.
**Reproduce**: `x dbnomics align imf.jp.gov.debt.gdp imf.gr.gov.debt.gdp imf.it.gov.debt.gdp imf.us.gov.debt.gdp imf.fr.gov.debt.gdp imf.es.gov.debt.gdp imf.uk.gov.debt.gdp imf.cn.gov.debt.gdp imf.de.gov.debt.gdp`
**More**: net debt `imf.jp.gov.net.debt.gdp`.
