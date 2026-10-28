# このサイトについて

DBnomics は公的機関——IMF、世界銀行、OECD、Eurostat、中央銀行——が出す経済の時系列を収集する無料のライブラリで、それらをすべて 1 つの API のうしろにまとめている。このサイトはそのライブラリを使って経済学を解説している。1 ページ 1 テーマで、グラフはすべてただのウェブリンクだ。リンクを開けば数字は URL の中にそのまま出ていて、どの文書に貼ってもそのまま機能する。

シェルから自分でデータを取得することもできます(モジュールのヘルプ: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth
x dbnomics align imf.us.gdp imf.cn.gdp
x dbnomics alias
```

データの基準年: IMF の *World Economic Outlook*(2025 年版、予測値を含む)と BIS の政策金利。すべてのグラフの最新年が 2025 年である。

**クイックスタート**: 任意のグラフの URL を文書に貼り付けるか、[draw スキル](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) を AI エージェントに読ませて「アメリカと中国の GDP をグラフ化して」と頼む。
