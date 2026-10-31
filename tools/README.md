# tools

Helpers used to write the pages in `docs/`. Nothing here runs at build time —
they are authoring tools for the markdown.

| file | what it does |
|---|---|
| `mkchart.py` | Fetch a series by x-cmd alias (`bls.cpi`, `imf.us.unemployment`, `bis.rate.euro`, …), aggregate it, and emit a `x-cmd.com/draw/echarts?d=…` URL carrying the numbers. Chart types: `line`, `area`, `bar`, `hbar`, `scatter`, `treemap`, `heatmap`, `radar`. Prints `{"ok": true, "url": …}` and refuses to hand over a URL that does not render. |
| `build_page.py` | Assemble a page from a page JSON (prose blocks + chart specs + per-language text). Chart URLs, tables and the trailing `**Data**:` line are copied verbatim; only prose is replaced. |
| `apply_i18n.py` | Merge a translation (one string per prose block, `null` at chart positions) into a page JSON. |
| `refit.py` | Re-fit the charts already on a page: decode each option, run the label fitter at a new canvas size, write the URLs back into the markdown. Use it after changing the column width or when a chart's labels start colliding. |
| `localize.py` | Give every language its own chart: take the English charts, swap the labels for the translated ones (`labels/<lang>.json`), re-fit them and write the URLs back into that language's markdown. |
| `labels/*.json` | The chart label vocabulary per language (titles, axis names, series names, country / state / province names). |

## Chart labels follow the article

A Chinese article carries Chinese charts: the title, the axis names, the
series names, the country and province names are translated, the numbers are
not. `tools/localize.py` does that mechanically:

```sh
python3 tools/localize.py                                  # every page
python3 tools/localize.py docs/5-us-casestudy/03-us-states  # one page
```

The English page keeps the English charts (it is the source), every other
language gets its own URL - so a chart is no longer shared between languages.
Localized labels are wider, so the fitter runs again on them: a chart that was
clean in English can still collide in Chinese, and the repair is applied to
the localized chart.

## Label anti-collision

The one place where an ECharts chart silently becomes unreadable is a category
axis with many or long labels: the labels print on top of each other. `mkchart.py`
does not trust the parameters — it renders the candidate, measures the real label
boxes in the SVG (`<text>` positions, including the enclosing `<g>` transforms
and the `x`/`y` offsets ECharts uses for wrapped lines), and tries, in order:

1. as given → 45° → 60° → smaller font → 45°+font → 90° → 90°+font
2. a wider canvas (up to the page column width; a wider canvas displayed at the
   same width only shrinks the type)
3. thinning the labels out (`axisLabel.interval`)
4. for a vertical bar with long names: the same data as a horizontal bar

The first candidate with **zero** overlapping label boxes wins. A chart that
still collides is reported on stderr and flagged in the JSON output, never
silently shipped.

```sh
python3 tools/mkchart.py spec.json          # build + self-check
python3 tools/refit.py docs/5-us-casestudy/03-us-states/en.md --w 760 --h 380
```

## Chart types worth knowing

| type | the question it answers |
|---|---|
| `bar` | ranking, short labels |
| `hbar` | ranking, long labels (categories move to the y axis) |
| `treemap` | "how big is this piece of the whole" — area is proportional to value |
| `heatmap` | many entities × a few periods — colour is the value |
| `scatter` | relationship between two variables |
| `radar` | several entities on the same set of indicators |
| `area` | magnitude and composition over time |

The site keeps the bar chart next to the new chart of the same data, so a reader
can compare the two readings side by side.

## Page JSON shape

```json
{
  "data": "**Data**: … **Reproduce**: `x dbnomics …`",
  "data_i18n": {"cn": "**数据**：…"},
  "blocks": ["# Title", "prose…", {"chart": {"spec": {…}, "alt": "x", "width": 760}}],
  "i18n": {"cn": ["# 标题", "中文段落…", null]}
}
```

`i18n` is positional: same length as `blocks`, `null` where the block is a chart.
Both string and `{"prose": …}` entries are accepted — mixing the two silently
dropped the translation once, so keep one shape per file.

After editing a page, check:

```sh
python3 - <<'PY'
import os, re, glob
for f in ['README.md'] + glob.glob('docs/**/*.md', recursive=True):
    for m in re.finditer(r'\]\(([^)]+)\)', open(f).read()):
        l = m.group(1)
        if l.startswith(('http', '#', 'mailto')):
            continue
        assert os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), l.split('#')[0]))), (f, l)
print('links ok')
PY
```
