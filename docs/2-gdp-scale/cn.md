# GDP：总量与购买力

GDP（国内生产总值）是一国境内一定时期内生产的全部最终产品与服务的市场价值 — 宏观经济学最核心的总量指标。

两种口径：

- **名义 GDP（nominal）**：按当期市场价格、当期汇率折算，衡量经济体量与市场规模；
- **购买力平价 GDP（PPP）**：按各国国内实际购买力折算（国际元），剔除汇率与物价水平差异，更接近"实际产出/生活成本"。

读图要点：中国名义 GDP 约为美国的六成，但 PPP 口径已超过美国 — 差异主要来自两国价格水平不同（巴拉萨–萨缪尔森效应）。印度在 PPP 口径下的排位显著前移。

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%20%C2%B7%20nominal%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20bn%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B29167.8%2C18273.4%2C4710.0%2C4070.1%2C3889.1%2C3587.5%2C3174.1%2C2376.5%5D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%20%C2%B7%20nominal%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20bn%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B29167.8%2C18273.4%2C4710.0%2C4070.1%2C3889.1%2C3587.5%2C3174.1%2C2376.5%5D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%20%C2%B7%20nominal%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20bn%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B29167.8%2C18273.4%2C4710.0%2C4070.1%2C3889.1%2C3587.5%2C3174.1%2C2376.5%5D%7D%5D%7D" width="760" alt="GDP nominal 2024"></a>

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%202024%20%C2%B7%20nominal%20vs%20PPP%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20%2F%20intl%20bn%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22nominal%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C18273.0%2C4710.0%2C4070.0%2C3889.0%2C3588.0%2C3174.0%2C2377.0%5D%7D%2C%7B%22name%22%3A%22PPP%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C37072.0%2C6017.0%2C6572.0%2C16020.0%2C4282.0%2C4359.0%2C3598.0%5D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%202024%20%C2%B7%20nominal%20vs%20PPP%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20%2F%20intl%20bn%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22nominal%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C18273.0%2C4710.0%2C4070.0%2C3889.0%2C3588.0%2C3174.0%2C2377.0%5D%7D%2C%7B%22name%22%3A%22PPP%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C37072.0%2C6017.0%2C6572.0%2C16020.0%2C4282.0%2C4359.0%2C3598.0%5D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22GDP%202024%20%C2%B7%20nominal%20vs%20PPP%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22USA%22%2C%22China%22%2C%22Germany%22%2C%22Japan%22%2C%22India%22%2C%22UK%22%2C%22France%22%2C%22Italy%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22USD%20%2F%20intl%20bn%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22nominal%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C18273.0%2C4710.0%2C4070.0%2C3889.0%2C3588.0%2C3174.0%2C2377.0%5D%7D%2C%7B%22name%22%3A%22PPP%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B29168.0%2C37072.0%2C6017.0%2C6572.0%2C16020.0%2C4282.0%2C4359.0%2C3598.0%5D%7D%5D%7D" width="760" alt="GDP nominal vs PPP 2024"></a>

**数据**：IMF World Economic Outlook（NGDPD / PPPGDP），经 DBnomics 取 2024 值。
**复现**：`x dbnomics align imf.us.gdp imf.cn.gdp imf.de.gdp imf.jp.gdp imf.in.gdp imf.uk.gdp imf.fr.gdp imf.it.gdp`
