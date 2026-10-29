# tools

Helpers used to write the pages in `docs/`. Nothing here runs at build time —
they are authoring tools for the markdown.

| file | what it does |
|---|---|
| `mkchart.py` | Fetch a series by x-cmd alias (`bls.cpi`, `imf.us.unemployment`, `bis.rate.euro`, …), aggregate it, and emit a `po6.sh/draw/echarts?d=…` URL carrying the numbers. Prints `{"ok": true, "url": …}` and refuses to hand over a URL that does not render. |
| `build_page.py` | Assemble a page from a page JSON (prose blocks + chart specs + per-language text). Chart URLs, tables and the trailing `**Data**:` line are copied verbatim; only prose is replaced. |
| `apply_i18n.py` | Merge a translation (one string per prose block, `null` at chart positions) into a page JSON. |

Page JSON shape:

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
