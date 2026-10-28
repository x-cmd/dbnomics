# 政府债务

政府总债务 / GDP 是可持续性的核心指标。《马斯特里赫特条约》给欧元区划了 60% 参考线（图中红线）— 不是硬约束，但超过后利率–增长差（r−g）恶化时风险陡增。

读图要点：

- 日本 ~250% 全球最高，但持有人结构（国内/央行）与零利率让它长期稳定;
- 希腊是危机样本：2009 后主权债务危机，靠 bailout + 重组压回;
- 美国 >120% 且趋势向上，疫情后财政扩张是主因。

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Government%20gross%20debt%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22Japan%22%2C%22Greece%22%2C%22Italy%22%2C%22USA%22%2C%22France%22%2C%22Spain%22%2C%22UK%22%2C%22China%22%2C%22Germany%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%20GDP%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B251.2%2C159.0%2C136.9%2C121.0%2C112.3%2C102.3%2C101.8%2C90.1%2C62.7%5D%2C%22markLine%22%3A%7B%22data%22%3A%5B%7B%22yAxis%22%3A60%7D%5D%2C%22lineStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Government%20gross%20debt%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22Japan%22%2C%22Greece%22%2C%22Italy%22%2C%22USA%22%2C%22France%22%2C%22Spain%22%2C%22UK%22%2C%22China%22%2C%22Germany%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%20GDP%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B251.2%2C159.0%2C136.9%2C121.0%2C112.3%2C102.3%2C101.8%2C90.1%2C62.7%5D%2C%22markLine%22%3A%7B%22data%22%3A%5B%7B%22yAxis%22%3A60%7D%5D%2C%22lineStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Government%20gross%20debt%20%282024%29%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%22Japan%22%2C%22Greece%22%2C%22Italy%22%2C%22USA%22%2C%22France%22%2C%22Spain%22%2C%22UK%22%2C%22China%22%2C%22Germany%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%20GDP%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B251.2%2C159.0%2C136.9%2C121.0%2C112.3%2C102.3%2C101.8%2C90.1%2C62.7%5D%2C%22markLine%22%3A%7B%22data%22%3A%5B%7B%22yAxis%22%3A60%7D%5D%2C%22lineStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%7D%5D%7D" width="760" alt="Government debt 2024, Maastricht line 60%"></a>

**数据**：IMF WEO（GGXWDG_NGDP），2024。
**复现**：`x dbnomics align imf.jp.gov.debt.gdp imf.gr.gov.debt.gdp imf.it.gov.debt.gdp imf.us.gov.debt.gdp imf.fr.gov.debt.gdp imf.es.gov.debt.gdp imf.uk.gov.debt.gdp imf.cn.gov.debt.gdp imf.de.gov.debt.gdp`
**延伸**：净债务 `imf.jp.gov.net.debt.gdp`。
