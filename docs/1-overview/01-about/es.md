# Qué es este sitio

DBnomics es una biblioteca gratuita que reúne series temporales económicas de fuentes oficiales — el FMI, el Banco Mundial, la OCDE, Eurostat, los bancos centrales — y las pone todas detrás de una sola API. Este sitio usa esa biblioteca para explicar economía: un tema por página y cada gráfico es un simple enlace web. Abre el enlace y los números están ahí mismo, en la URL; pégalo en cualquier documento y sigue funcionando.

Descarga los datos tú mismo desde la shell (ayuda del módulo: [x-cmd.com/mod/dbnomics](https://x-cmd.com/mod/dbnomics)):

```sh
x dbnomics data imf.us.gdp.growth
x dbnomics align imf.us.gdp imf.cn.gdp
x dbnomics alias
```

Vintage de los datos: el *World Economic Outlook* del FMI (edición 2025, con pronósticos) y los tipos oficiales del BPI. Cada gráfico usa 2025 como su año más reciente.

**Inicio rápido**: pega la URL de cualquier gráfico en un documento; o apunta a un agente de IA con la [skill draw](https://raw.githubusercontent.com/x-cmd/draw/main/SKILL.md) y pídele un gráfico del PIB de EE. UU. frente a China.
