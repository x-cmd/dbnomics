# GDP: scale and purchasing power

GDP (gross domestic product) is the market value of all final goods and services produced within a country in a period — the core aggregate of macroeconomics.

Two flavours:

- **Nominal GDP**: valued at current market prices, converted at market exchange rates — economic and market scale;
- **PPP GDP**: valued at purchasing power parity (international dollars), stripping out exchange-rate and price-level differences — closer to real output and living costs.

Reading guide: China's nominal GDP is about 60% of the US, but on PPP it exceeds it — the gap mostly reflects price-level differences (Balassa–Samuelson). India jumps ranks under PPP.

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%20%C2%B7%20nominal%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20bn%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B29167.8%2C18273.4%2C4710.0%2C4070.1%2C3889.1%2C3587.5%2C3174.1%2C2376.5%5D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%20%C2%B7%20nominal%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20bn%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B29167.8%2C18273.4%2C4710.0%2C4070.1%2C3889.1%2C3587.5%2C3174.1%2C2376.5%5D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%20%C2%B7%20nominal%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20bn%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B29167.8%2C18273.4%2C4710.0%2C4070.1%2C3889.1%2C3587.5%2C3174.1%2C2376.5%5D%7D%5D%7D" width="760" alt="GDP nominal 2024"></a>

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%202024%20%C2%B7%20nominal%20vs%20PPP%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20%2F%20intl%20bn%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22nominal%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C18273.0%2C4710.0%2C4070.0%2C3889.0%2C3588.0%2C3174.0%2C2377.0%5D%7D%2C%7B%22name%22%3A%22PPP%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C37072.0%2C6017.0%2C6572.0%2C16020.0%2C4282.0%2C4359.0%2C3598.0%5D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%202024%20%C2%B7%20nominal%20vs%20PPP%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20%2F%20intl%20bn%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22nominal%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C18273.0%2C4710.0%2C4070.0%2C3889.0%2C3588.0%2C3174.0%2C2377.0%5D%7D%2C%7B%22name%22%3A%22PPP%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C37072.0%2C6017.0%2C6572.0%2C16020.0%2C4282.0%2C4359.0%2C3598.0%5D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%202024%20%C2%B7%20nominal%20vs%20PPP%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20%2F%20intl%20bn%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22nominal%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C18273.0%2C4710.0%2C4070.0%2C3889.0%2C3588.0%2C3174.0%2C2377.0%5D%7D%2C%7B%22name%22%3A%22PPP%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C37072.0%2C6017.0%2C6572.0%2C16020.0%2C4282.0%2C4359.0%2C3598.0%5D%7D%5D%7D" width="760" alt="GDP nominal vs PPP 2024"></a>

**Data**: IMF World Economic Outlook (NGDPD / PPPGDP), 2024 values via DBnomics.
**Reproduce**: `x dbnomics align imf.us.gdp imf.cn.gdp imf.de.gdp imf.jp.gdp imf.in.gdp imf.uk.gdp imf.fr.gdp imf.it.gdp`
