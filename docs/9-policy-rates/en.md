# Policy rates

Policy rates are the central banks' price instrument: the Fed funds rate, the ECB deposit facility rate, the BoJ short-term rate. They transmit to loans, deposits, exchange rates and asset prices — "the anchor of all prices".

Reading guide:

- Slow normalisation 2015–2019; the epic 2022–2023 hikes (Fed 0→5.5%) against inflation;
- The ECB followed with smaller steps; the BoJ left negative rates last (2024) — the end of a 30-year experiment;
- Every 1-point move reprices floating-rate debt and every valuation model.

```text
https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Policy%20rates%20%C2%B7%20year-end%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%2C%222023%22%2C%222024%22%2C%222025%22%5D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22US%20Fed%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22ECB%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22BoJ%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%5D%7D
```

<a href="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Policy%20rates%20%C2%B7%20year-end%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%2C%222023%22%2C%222024%22%2C%222025%22%5D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22US%20Fed%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22ECB%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22BoJ%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%5D%7D"><img src="https://po6.sh/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Policy%20rates%20%C2%B7%20year-end%22%7D%2C%22xAxis%22%3A%7B%22data%22%3A%5B%222015%22%2C%222016%22%2C%222017%22%2C%222018%22%2C%222019%22%2C%222020%22%2C%222021%22%2C%222022%22%2C%222023%22%2C%222024%22%2C%222025%22%5D%7D%2C%22yAxis%22%3A%7B%22name%22%3A%22%25%22%7D%2C%22legend%22%3A%7B%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22US%20Fed%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22ECB%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%2C%7B%22name%22%3A%22BoJ%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%5D%7D%5D%7D" width="760" alt="Policy rates year-end 2015-2025"></a>

**Data**: BIS central bank policy rates (monthly, year-end slice) via DBnomics.
**Reproduce**: `x dbnomics align bis.rate.us bis.rate.eu bis.rate.jp`
