# DBnomics とこのサイト

DBnomics（db.nomics.world）は IMF・世界銀行・OECD・Eurostat・ECB・BIS など 70 以上の公式機関の時系列データを、単一の無料 API に統合しています。本サイト = **経済学の知識 + グラフ**：各ページで 1 つのマクロテーマを扱い、すべてのグラフは x-cmd draw がレンダリングする**平文 URL** です — データはリンクそのものにあり、AI が直接読めます。

CLI で取得（モジュールのヘルプ: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)）：

```sh
x dbnomics data imf.us.gdp.growth
x dbnomics align imf.us.gdp imf.cn.gdp
x dbnomics alias
```

データ時点：IMF WEO 2025（予測を含む）・BIS 政策金利（年末）。全グラフの最新値は 2025 年です。
