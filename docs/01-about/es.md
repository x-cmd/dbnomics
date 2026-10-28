# DBnomics y este sitio

DBnomics (db.nomics.world) agrega series temporales del FMI, Banco Mundial, OCDE, Eurostat, BCE, BIS y más de 70 fuentes oficiales en una única API gratuita. Este sitio = **conocimiento económico + gráficos**: un tema macro por página, y cada gráfico es una **URL en texto plano renderizada por x-cmd draw** — los datos viven en el enlace, legibles por IA.

Datos desde la terminal (ayuda del módulo: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth
x dbnomics align imf.us.gdp imf.cn.gdp
x dbnomics alias
```

Vigencia de los datos: FMI WEO 2025 (con proyecciones) · tipos de política del BIS (fin de año). Todos los gráficos usan 2025 como último valor.
