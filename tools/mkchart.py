"""Chart toolkit for the dbnomics site.

Fetch a series by x-cmd alias (or explicit values), aggregate it, and emit a
draw URL whose ECharts option carries the numbers.

CLI:  python3 tools/mkchart.py spec.json [spec2.json ...]
Each spec is a JSON object; the script prints one JSON line per spec.

spec keys:
  type      line | area | bar | hbar | scatter | treemap | heatmap | radar
            (default line)
  title     chart title
  yname     y-axis label
  xname     x-axis label
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
  w, h      canvas size in px (draw accepts 200-1600 x 140-1200, default 560x320)

Label anti-collision: a category axis with many or long labels is the one
place where an ECharts chart silently becomes unreadable — labels print on top
of each other. `fit_labels` renders the candidate, measures the real label
boxes in the SVG, and tries rotations / a wider canvas / thinning before
handing a URL over. A chart that still collides is reported, not shipped.
"""
import copy
import json
import math
import re
import subprocess
import sys
import urllib.parse
import urllib.request

PALETTE = ['#2563eb', '#dc2626', '#64748b', '#f59e0b', '#8b5cf6', '#eab308',
           '#0d9488', '#db2777', '#65a30d', '#0891b2', '#be123c', '#8a9a5b']

# treemap / heatmap ramps (light -> dark), used when the spec asks for a ramp
RAMPS = {
    'blue': ('#dbeafe', '#1d4ed8'),
    'green': ('#dcfce7', '#15803d'),
    'amber': ('#fef3c7', '#b45309'),
    'red': ('#fee2e2', '#b91c1c'),
}

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


# ---------------------------------------------------------------- label fit

def _text_transform(attrs):
    """(x, y, angle) of an SVG text element.

    ECharts writes the anchor on the element's transform and the offset from
    that anchor in x=/y= (a wrapped label puts each line a few pixels lower),
    so both have to be combined.
    """
    m = re.search(r'transform="([^"]*)"', attrs)
    t = m.group(1) if m else ''
    mm = re.search(r'matrix\(([-\d.]+),([-\d.]+),([-\d.]+),([-\d.]+),([-\d.]+),([-\d.]+)\)', t)
    if mm:
        a, b, c, d, e, f = (float(v) for v in mm.groups())
        return e, f, math.degrees(math.atan2(b, a))
    tr = re.search(r'translate\(([-\d.]+)[ ,]+([-\d.]+)\)', t)
    x, y = (float(tr.group(1)), float(tr.group(2))) if tr else (0.0, 0.0)
    rm = re.search(r'rotate\(([-\d.]+)', t)
    ang = float(rm.group(1)) if rm else 0.0
    mx = re.search(r'\bx="([-\d.]+)"', attrs)
    my = re.search(r'\by="([-\d.]+)"', attrs)
    if mx:
        x += float(mx.group(1))
    if my:
        y += float(my.group(1))
    return x, y, ang


def svg_labels(svg):
    """Every <text> in the SVG with the position it is actually drawn at.

    ECharts positions some labels on the <text> itself (translate/matrix) and
    some on an enclosing <g>, so the enclosing transforms have to be applied
    too - otherwise every treemap tile label looks like it sits at 0,0.
    """
    out = []
    stack = []          # translations of the open <g> elements
    pos = 0
    tag_re = re.compile(r'<(/?)(g|text)\b([^>]*)>', re.S)
    while True:
        m = tag_re.search(svg, pos)
        if not m:
            break
        pos = m.end()
        closing, tag, attrs = m.group(1) == '/', m.group(2), m.group(3)
        if tag == 'g':
            if closing:
                if stack:
                    stack.pop()
            else:
                stack.append(_text_transform(attrs))
            continue
        # a <text> element: read its content
        end = svg.find('</text>', pos)
        body = re.sub(r'<[^>]+>', '', svg[pos:end if end > 0 else len(svg)]).strip()
        pos = (end + 7) if end > 0 else len(svg)
        if not body:
            continue
        x, y, ang = _text_transform(attrs)
        for gx, gy, _ in stack:
            x += gx
            y += gy
        fs = re.search(r'font-size:([\d.]+)px', attrs)
        out.append({'x': x, 'y': y, 'ang': ang, 'fs': float(fs.group(1)) if fs else 12.0,
                    'text': body})
    return out


def _box(l):
    """Bounding box of a (possibly rotated) label.

    Text sits on its baseline: the ink runs from about 0.78em above the
    baseline to 0.22em below it. Modelling it that way keeps two stacked
    lines of a wrapped label from counting as a collision.
    """
    w = len(l['text']) * l['fs'] * 0.56
    h = l['fs']
    r = math.radians(l['ang'])
    c, s = abs(math.cos(r)), abs(math.sin(r))
    W, H = w * c + h * s, w * s + h * c
    cy = l['y'] - 0.28 * h          # centre of the ink, just above the baseline
    return (l['x'] - W / 2, cy - H / 2, l['x'] + W / 2, cy + H / 2)


def label_collisions(svg):
    """Pairs of labels whose boxes overlap (the 'labels on top of each other' bug)."""
    ls = svg_labels(svg)
    bad = []
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            a, b = _box(ls[i]), _box(ls[j])
            ox = min(a[2], b[2]) - max(a[0], b[0])
            oy = min(a[3], b[3]) - max(a[1], b[1])
            if ox > 0.5 and oy > 0.5:
                bad.append((ls[i]['text'], ls[j]['text'], round(ox, 1), round(oy, 1)))
    return bad


def render(url, tries=3):
    """Fetch the rendered SVG (the network here is not always kind)."""
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            return urllib.request.urlopen(req, timeout=60).read().decode('utf-8', 'ignore')
        except Exception as e:      # noqa: BLE001 - transient network errors
            last = e
    raise last


def _cat_axis(opt):
    """The category axis of an option, if it has one.

    ECharts treats an axis that carries `data` as a category axis even when the
    type is left out, so the type key alone is not enough to spot one.
    """
    xa = opt.get('xAxis')
    if isinstance(xa, list):
        xa = xa[0] if xa else None
    if not isinstance(xa, dict):
        return None
    if xa.get('type') == 'category':
        return xa
    if xa.get('type') is None and xa.get('data'):
        return xa
    return None


def _scatter_labels(opt):
    """True when a series draws its own labels (scatter point names)."""
    for s in opt.get('series') or []:
        if not isinstance(s, dict) or s.get('type') not in ('scatter', 'effectScatter'):
            continue
        if (s.get('label') or {}).get('show'):
            return True
        for d in s.get('data') or []:
            if isinstance(d, dict) and (d.get('label') or {}).get('show'):
                return True
    return False


def _axis_names_mid(opt):
    """Move axis names to the middle of the axis.

    By default ECharts puts a value axis' name at the far end of the axis,
    where it lands on top of the last tick label.
    """
    o = copy.deepcopy(opt)
    touched = False
    for key in ('xAxis', 'yAxis'):
        ax = o.get(key)
        axes = ax if isinstance(ax, list) else [ax]
        for a in axes:
            if isinstance(a, dict) and a.get('name'):
                a['nameLocation'] = 'middle'
                a['nameGap'] = 28
                touched = True
    return o if touched else None


def _candidates(opt, spec):
    """Options to try, best first, when the category labels collide."""
    ax = _cat_axis(opt)
    if not ax:
        # a scatter with named points: let ECharts move the labels apart
        if _scatter_labels(opt):
            out = []
            o = copy.deepcopy(opt)
            for s in o.get('series', []):
                if isinstance(s, dict) and s.get('type') in ('scatter', 'effectScatter'):
                    s['labelLayout'] = {'moveOverlap': 'shiftY'}
            out.append((o, 'shift overlapping point labels'))
            o2 = copy.deepcopy(opt)
            for s in o2.get('series', []):
                if isinstance(s, dict) and s.get('type') in ('scatter', 'effectScatter'):
                    s['labelLayout'] = {'hideOverlap': True}
            out.append((o2, 'hide overlapping point labels'))
            moved = _axis_names_mid(o2)
            if moved:
                out.append((moved, 'hide overlapping labels + axis names in the middle'))
            return out
        moved = _axis_names_mid(opt)
        return [(opt, 'as given'), (moved, 'axis names in the middle')] if moved else [(opt, 'as given')]
    n = len(ax.get('data') or [])
    if n < 2:
        return [(opt, 'as given')]
    out = [(opt, 'as given')]
    base_rotate = (ax.get('axisLabel') or {}).get('rotate', 0)
    base_font = (ax.get('axisLabel') or {}).get('fontSize', 9)
    base_interval = (ax.get('axisLabel') or {}).get('interval')

    def variant(**label_over):
        o = copy.deepcopy(opt)
        lab = o['xAxis'].setdefault('axisLabel', {})
        lab.update(label_over)
        return o

    # A tilted label is easier to read than a vertical one, so try 45 and 60
    # degrees before falling back to 90.
    if base_rotate != 45:
        out.append((variant(rotate=45), 'rotate 45'))
    if base_rotate != 60:
        out.append((variant(rotate=60), 'rotate 60'))
    if base_font > 8:
        out.append((variant(fontSize=8), 'font 8'))
        if base_rotate != 45:
            out.append((variant(rotate=45, fontSize=8), 'rotate 45 + font 8'))
    if base_rotate != 90:
        out.append((variant(rotate=90), 'rotate 90'))
        if base_font > 8:
            out.append((variant(rotate=90, fontSize=8), 'rotate 90 + font 8'))
    # widen the canvas (draw caps at 1600 x 1200); only up to the page column,
    # a wider canvas displayed at the same width just shrinks the type
    target = spec.get('w') or 760
    for w in (760, 900, 1100, 1400, 1600):
        if target < w <= 1600 and spec.get('w'):
            o = copy.deepcopy(opt)
            o['_canvas'] = {'w': w, 'h': spec.get('h', 0) or None}
            out.append((o, f'widen to {w}'))
    # last resort: thin the labels out
    if base_interval in (0, 'auto', None):
        for k in (1, 2, 3):
            out.append((variant(interval=k), f'every {k + 1}th label'))
    return out


def fit_labels(opt, spec, url_for):
    """Return (option, url, collisions) for the first candidate without overlaps."""
    best = None
    for cand, note in _candidates(opt, spec):
        u = url_for(cand)
        try:
            svg = render(u)
        except Exception as e:
            continue
        bad = label_collisions(svg)
        if not bad:
            return cand, u, []
        if best is None or len(bad) < len(best[2]):
            best = (cand, u, bad, note)
    if best:
        return best[0], best[1], best[2]
    return opt, url_for(opt), ['not rendered']


# ---------------------------------------------------------------- builders

def _ramp(spec, values):
    """Map values to a light->dark colour ramp (treemap tiles, heatmap cells)."""
    lo_hi = spec.get('ramp', 'blue')
    c0, c1 = RAMPS.get(lo_hi, RAMPS['blue'])
    if not values:
        return c0
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1.0
    a = tuple(int(c0[i:i + 2], 16) for i in (1, 3, 5))
    b = tuple(int(c1[i:i + 2], 16) for i in (1, 3, 5))
    return c0, c1, a, b, span


def _mix(a, b, t):
    return '#%02x%02x%02x' % tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def _ink_on(hexcolor):
    """Black or white text, whichever stays readable on that tile."""
    n = int(hexcolor[1:], 16)
    r, g, b = (n >> 16) & 255, (n >> 8) & 255, n & 255
    lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return '#0f172a' if lum > 0.6 else '#ffffff'


def build(spec):
    typ = spec.get('type', 'line')
    colors = spec.get('colors', PALETTE)
    sers = spec.get('series', [])
    for i, s in enumerate(sers):
        s.setdefault('color', colors[i % len(colors)])
    title = {'text': spec['title']}

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
        opt = {'title': title, 'color': colors,
               'xAxis': {'type': 'value', 'name': spec.get('xname', '')},
               'yAxis': {'type': 'value', 'name': spec.get('yname', '')},
               'series': [{'type': 'scatter', 'symbolSize': spec.get('size', 10),
                           'data': pts}],
               'legend': {} if spec.get('legend', True) else {'show': False}}
        return opt

    if typ == 'treemap':
        # area is proportional to value: the "size of the piece" reading
        items = spec['data']
        vals = [it['value'] for it in items]
        c0, c1, a, b, span = _ramp(spec, vals)
        lo = min(vals)
        data = []
        for it in items:
            t = (it['value'] - lo) / span
            col = _mix(a, b, t)
            d = {'name': it['name'], 'value': it['value'],
                 'itemStyle': {'color': col}}
            fmt = it.get('label')
            if fmt:
                # text colour follows the tile it sits on, so the tile stays readable
                d['label'] = {'formatter': fmt,
                              'color': _ink_on(col)}
            data.append(d)
        opt = {'title': title,
               'series': [{'type': 'treemap', 'roam': False, 'nodeClick': False,
                           'breadcrumb': {'show': False},
                           'label': {'show': True, 'fontSize': spec.get('font', 10),
                                     'formatter': spec.get('label_formatter', '{b}'),
                                     'lineHeight': 13},
                           'labelLayout': {'hideOverlap': True},
                           'itemStyle': {'borderColor': '#fff', 'borderWidth': 1},
                           'data': data}]}
        return opt

    if typ == 'heatmap':
        xs = spec['x']
        ys = spec['y']
        vals = [c[2] for c in spec['cells']]
        c0, c1, a, b, span = _ramp(spec, vals)
        vmin = spec.get('vmin', min(vals))
        vmax = spec.get('vmax', max(vals))
        colors = [c0, c1]
        base = spec.get('base')
        if base is not None:
            # diverging scale: the base year sits on the neutral colour
            d = max(base - vmin, vmax - base)
            vmin, vmax = base - d, base + d
            colors = [spec.get('low_color', '#dc2626'), '#f8fafc',
                      spec.get('high_color', '#1d4ed8')]
        opt = {'title': title,
               'xAxis': {'type': 'category', 'data': xs,
                         'axisLabel': {'interval': 0, 'fontSize': spec.get('font', 10)},
                         'name': spec.get('xname', ''), 'nameLocation': 'middle',
                         'nameGap': 22},
               'yAxis': {'type': 'category', 'data': ys,
                         'axisLabel': {'interval': 0, 'fontSize': spec.get('yfont', 9)},
                         'name': spec.get('yname', '')},
               'visualMap': {'min': vmin, 'max': vmax, 'calculable': False,
                             'orient': 'horizontal', 'left': 'center', 'bottom': 0,
                             'inRange': {'color': colors}},
               'series': [{'type': 'heatmap', 'data': spec['cells'],
                           'label': {'show': False},
                           'itemStyle': {'borderColor': '#fff',
                                         'borderWidth': spec.get('border', 1)}}]}
        return opt

    if typ == 'radar':
        inds = [{'name': i['name'], 'max': i.get('max', 100)} for i in spec['indicators']]
        out_series = []
        for s in sers:
            # a radar series carries one data item: the values of that series
            out_series.append({'name': s['name'], 'type': 'radar',
                               'data': [{'value': [round(v, 2) for v in s['values']],
                                         'name': s['name']}],
                               'itemStyle': {'color': s['color']},
                               'lineStyle': {'color': s['color']},
                               'areaStyle': {'opacity': 0.14}})
        opt = {'title': title, 'color': colors,
               'legend': {} if spec.get('legend', True) else {'show': False},
               'radar': {'indicator': inds, 'radius': spec.get('radius', '62%'),
                         'axisName': {'fontSize': spec.get('font', 10)}},
               'series': out_series}
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
        if typ in ('line', 'area'):
            item['smooth'] = spec.get('smooth', True)
            item['connectNulls'] = spec.get('connect', True)
            item['lineStyle'] = {'color': s['color']}
            if typ == 'area':
                item['areaStyle'] = {'opacity': 0.18 if len(sers) == 1 else 0.22}
                if spec.get('stack'):
                    item['stack'] = spec['stack']
                    item['areaStyle'] = {'opacity': 0.75}
        if s.get('bar_colors'):          # per-bar colour for signed bars
            item['data'] = [{'value': v, 'itemStyle': {'color': c}}
                            for v, c in zip(vals, s['bar_colors'])]
        out_series.append(item)

    if typ == 'hbar':
        # categories on the y axis: long names get their own column, never collide
        xs = list(reversed(xs))
        out_series = []
        for s in sers:
            vals = list(reversed(series_values(dict(s, x=xs))))
            out_series.append({'name': s['name'], 'type': 'bar', 'data': vals,
                               'itemStyle': {'color': s['color']}})
        opt = {'title': title, 'color': colors,
               'xAxis': {'type': 'value', 'name': spec.get('yname', '')},
               'yAxis': {'type': 'category', 'data': xs,
                         'axisLabel': {'interval': 0, 'fontSize': spec.get('font', 10)}},
               'legend': {} if spec.get('legend', True) else {'show': False},
               'series': out_series}
        return opt

    opt = {'title': title, 'color': colors,
           'xAxis': {'type': 'category', 'data': xs,
                     'axisLabel': {'interval': max(0, int(spec.get('every', 1)) - 1),
                                   'rotate': spec.get('rotate', 0),
                                   'fontSize': spec.get('font', 9)}},
           'yAxis': {'name': spec.get('yname', '')},
           'legend': {} if spec.get('legend', True) else {'show': False},
           'series': out_series}
    return opt


def _canvas(spec, opt):
    """(w, h) for the draw canvas; a candidate may carry its own override."""
    c = opt.get('_canvas')
    if c:
        return c.get('w'), c.get('h') or spec.get('h')
    return spec.get('w'), spec.get('h')


def _trim(opt):
    """Drop the unused palette entries: they only make the URL longer."""
    o = copy.deepcopy(opt)
    col = o.get('color')
    sers = o.get('series')
    if isinstance(col, list) and isinstance(sers, list) and sers:
        used = max(1, len(sers))
        if len(col) > used:
            o['color'] = col[:used]
    return o


def url_for(spec, opt=None, fit=True):
    """draw URL for a spec (or a prepared option)."""
    if opt is None:
        opt = build(spec)
    opt = _trim(opt)
    w, h = _canvas(spec, opt)
    q = 'd=' + urllib.parse.quote(json.dumps(opt, ensure_ascii=False,
                                             separators=(',', ':')), safe='')
    if w:
        q += f'&w={w}'
    if h:
        q += f'&h={h}'
    base = 'https://x-cmd.com/draw/echarts?' + q
    if not fit:
        return base
    # measure, then repair the labels if they collide
    cand, u, bad = fit_labels(opt, spec, lambda o: url_for(spec, o, fit=False))
    if bad:
        print(f'  ! {spec.get("title", "")}: {len(bad)} label collisions left', file=sys.stderr)
    return u


if __name__ == '__main__':
    for path in sys.argv[1:]:
        spec = json.load(open(path))
        u = url_for(spec)
        try:
            svg = render(u)
            bad = label_collisions(svg)
            ok = '<svg' in svg and not bad
        except Exception as e:
            ok = f'ERR {e}'
            bad = []
        print(json.dumps({'file': path, 'ok': ok, 'collisions': len(bad),
                          'url': u}, ensure_ascii=False))
