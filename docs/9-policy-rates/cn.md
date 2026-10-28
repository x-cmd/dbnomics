# 政策利率

政策利率是央行的价格工具：Fed 联邦基金利率、ECB 存款便利利率、BoJ 短期政策利率。它传导到贷款、存款、汇率与资产价格 — "一切价格的锚"。

读图要点：

- 2015–2019 缓慢正常化；2022–2023 史诗级加息（Fed 0→5.5%）压通胀;
- ECB 跟随但幅度更小;BoJ 最后一个离开负利率（2024）— 日本三十年实验的尾声;
- 利率每变动 1 点，浮息债务与估值模型全部重定价。

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Policy%20rates%20%C2%B7%20year-end%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%2C%222023%22%2C%222024%22%2C%222025%22%5D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22US%20Fed%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22ECB%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22BoJ%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Policy%20rates%20%C2%B7%20year-end%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%2C%222023%22%2C%222024%22%2C%222025%22%5D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22US%20Fed%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22ECB%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22BoJ%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Policy%20rates%20%C2%B7%20year-end%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%2C%222023%22%2C%222024%22%2C%222025%22%5D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22US%20Fed%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22ECB%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22BoJ%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%5D%7D" width="760" alt="Policy rates year-end 2015-2025"></a>

**数据**：BIS 央行政策利率（月度，取年末），经 DBnomics。
**复现**：`x dbnomics align bis.rate.us bis.rate.eu bis.rate.jp`
