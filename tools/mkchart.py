"""Chart toolkit for the dbnomics site.

Fetch a series by x-cmd alias (or explicit values), aggregate it, and emit a
draw URL whose ECharts option carries the numbers.

CLI:  python3 /tmp/mkchart.py spec.json [spec2.json ...]
Each spec is a JSON object; the script prints one draw URL per spec.

spec keys:
  type      line | bar | scatter          (default line)
  title     chart title
  yname     y-axis label
  xname     x-axis label (scatter)
  x         explicit x values (scatter) or category labels
  start/end first/last year to keep
  agg       none | last | avg             (for monthly series: year-end or annual average)
  transform none | yoy | diff             (applied before aggregation)
  unit      unit suffix for the series name, e.g. "%"
  series    [{name, alias | values, color}]
  colors    palette used when a series has no color
  legend    true | false
  connect   true | false  (connectNulls)
  smooth    true | false
"""
import json, subprocess, sys, urllib.parse, urllib.request

PALETTE = ['#2563eb', '#dc2626', '#64748b', '#f59e0b', '#8b5cf6', '#eab308',
           '#0d9488', '#db2777', '#65a30d', '#0891b2', '#be123c', '#8a9a5b']

_alias_cache = {}


def fetch(alias):
    """Return {period: value} for an x-cmd dbnomics alias."""
    if alias in _alias_cache:
        return _alias_cache[alias]
    out = subprocess.run(['x', 'dbnomics', 'data', alias], capture_output=True, text=True).stdout
    lines = [l for l in out.split('\n')
             if l and not l.startswith(('/usr/bin/awk', ' source line', ' context is', '\t#', ' <<<'))]
    data = {}
    for l in lines[1:]:
        p = l.split('\t')
        if len(p) == 2 and p[1] not in ('NA', ''):
            data[p[0]] = float(p[1])
    if not data:
        raise SystemExit(f'no data for alias {alias}')
    _alias_cache[alias] = data
    return data


def annualize(data, transform='none', agg='last'):
    """monthly/daily {period: value} -> {year(int): value}"""
    if transform == 'none':
        by = {}
        for per, v in data.items():
            y = int(per[:4])
            by.setdefault(y, []).append((per, v))
        out = {}
        for y, lst in by.items():
            lst.sort()
            out[y] = lst[-1][1] if agg == 'last' else sum(v for _, v in lst) / len(lst)
        return out
    # yoy / diff on the raw period
    if transform == 'yoy':
        by_year = {}
        for per, v in data.items():
            by_year.setdefault(int(per[:4]), []).append((per, v))
        out = {}
        for y, lst in by_year.items():
            lst.sort()
            yoys = []
            for per, v in lst:
                prev = f'{y-1}{per[4:]}'
                if prev in data:
                    yoys.append((per, (v / data[prev] - 1) * 100))
            if not yoys:
                continue
            out[y] = yoys[-1][1] if agg == 'last' else sum(v for _, v in yoys) / len(yoys)
        return out
    # diff
    by = {}
    for per, v in data.items():
        y = int(per[:4])
        by.setdefault(y, []).append((per, v))
    out = {}
    for y, lst in by.items():
        lst.sort()
        if len(lst) >= 2:
            out[y] = lst[-1][1] - lst[0][1]
    return out


def series_values(spec):
    """Return list of values aligned to the x axis for one series spec."""
    if 'values' in spec:
        vals = list(spec['values'])
    else:
        raw = fetch(spec['alias'])
        if all(len(p) == 4 for p in raw):          # yearly already
            d = {int(k): v for k, v in raw.items()}
        else:
            d = annualize(raw, spec.get('transform', 'none'), spec.get('agg', 'last'))
        start, end = spec.get('start'), spec.get('end')
        vals = []
        if 'x' in spec:
            for xv in spec['x']:
                vals.append(d.get(int(xv)))
        else:
            lo = start if start is not None else min(d)
            hi = end if end is not None else max(d)
            for y in range(int(lo), int(hi) + 1):
                vals.append(d.get(y))
    return vals


def build(spec):
    typ = spec.get('type', 'line')
    colors = spec.get('colors', PALETTE)
    sers = spec['series']
    for i, s in enumerate(sers):
        s.setdefault('color', colors[i % len(colors)])
    if typ == 'scatter':
        pts = []
        for s in sers:
            years = list(range(int(s.get('start', 1960)), int(s.get('end', 2025)) + 1))
            xv = series_values(dict(s, alias=s['x_alias'], x=years,
                                    transform=s.get('x_transform', 'none'),
                                    agg=s.get('x_agg', 'last')))
            yv = series_values(dict(s, alias=s['y_alias'], x=years,
                                    transform=s.get('y_transform', 'none'),
                                    agg=s.get('y_agg', 'last')))
            for j, yr in enumerate(years):
                if xv[j] is None or yv[j] is None:
                    continue
                d = {'value': [round(xv[j], 3), round(yv[j], 3)], 'name': s['name'],
                     'itemStyle': {'color': s['color']}}
                if s.get('label'):
                    d['label'] = {'show': True, 'formatter': '{b}', 'position': 'top', 'fontSize': 9}
                pts.append(d)
        opt = {'title': {'text': spec['title']}, 'color': colors,
               'xAxis': {'type': 'value', 'name': spec.get('xname', '')},
               'yAxis': {'type': 'value', 'name': spec.get('yname', '')},
               'series': [{'type': 'scatter', 'symbolSize': spec.get('size', 10),
                           'data': pts,
                           'legend': spec.get('legend_names', [])}]}
        opt['series'][0].pop('legend')
        opt['legend'] = {} if spec.get('legend', True) else {'show': False}
        return opt
    xs = spec.get('x')
    if xs is None:
        vals0 = series_values(sers[0])
        start = sers[0].get('start', 2000)
        end = sers[0].get('end')
        if end is None:
            raw = fetch(sers[0]['alias']) if 'alias' in sers[0] else None
            end = (max(int(k[:4]) for k in raw) if raw else start + len(vals0) - 1)
        xs = [str(y) for y in range(int(start), int(end) + 1)]
    out_series = []
    for s in sers:
        vals = series_values(dict(s, x=xs))
        item = {'name': s['name'], 'type': typ, 'data': vals,
                'itemStyle': {'color': s['color']}}
        if typ == 'line':
            item['smooth'] = spec.get('smooth', True)
            item['connectNulls'] = spec.get('connect', True)
            item['lineStyle'] = {'color': s['color']}
        if s.get('bar_colors'):          # per-bar colour for signed bars
            item['data'] = [{'value': v, 'itemStyle': {'color': c}}
                            for v, c in zip(vals, s['bar_colors'])]
        out_series.append(item)
    opt = {'title': {'text': spec['title']}, 'color': colors,
           'xAxis': {'type': 'category', 'data': xs,
                     'axisLabel': {'interval': max(0, int(spec.get('every', 1)) - 1),
                                   'rotate': spec.get('rotate', 0),
                                   'fontSize': spec.get('font', 9)}},
           'yAxis': {'name': spec.get('yname', '')},
           'legend': {} if spec.get('legend', True) else {'show': False},
           'series': out_series}
    return opt


def url_for(spec):
    opt = build(spec)
    return 'https://po6.sh/draw/echarts?d=' + urllib.parse.quote(
        json.dumps(opt, ensure_ascii=False, separators=(',', ':')), safe='')


if __name__ == '__main__':
    for path in sys.argv[1:]:
        spec = json.load(open(path))
        u = url_for(spec)
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            body = urllib.request.urlopen(req, timeout=30).read(200).decode('utf-8', 'ignore')
            ok = '<svg' in body
        except Exception as e:
            ok = f'ERR {e}'
        print(json.dumps({'file': path, 'ok': ok, 'url': u}, ensure_ascii=False))
