"""Re-fit the charts on a page: decode each draw option, run the label fitter
with the page's canvas size, and write the URLs back into the markdown.

A chart whose category labels collide (the "names printed on top of each
other" bug) is repaired here instead of by hand: rotate, shrink, widen, or
thin out until the rendered SVG has no overlapping label boxes.

usage: python3 tools/refit.py docs/<page>/<lang>.md [--w 760] [--h 380] [--keep]

--keep keeps each chart's own canvas size (the URL's w/h, default 560x320);
without it every chart is moved to the given size.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mkchart import fit_labels, label_collisions, render  # noqa: E402

URL_RE = re.compile(
    r'https://x-cmd[.]com/draw/(explore/)?echarts[?]d=[^&\s")]+(?:&w=\d+)?(?:&h=\d+)?')


def option_of(url):
    q = urllib.parse.urlparse(url).query
    d = urllib.parse.parse_qs(q)['d'][0]
    return json.loads(d)


def canvas_of(url):
    q = urllib.parse.urlparse(url).query
    w = urllib.parse.parse_qs(q).get('w', ['560'])[0]
    h = urllib.parse.parse_qs(q).get('h', ['320'])[0]
    return int(w), int(h)


def encode(opt, w=None, h=None, explore=False):
    q = 'd=' + urllib.parse.quote(json.dumps(opt, ensure_ascii=False,
                                             separators=(',', ':')), safe='')
    if w:
        q += f'&w={w}'
    if h:
        q += f'&h={h}'
    kind = 'explore/echarts' if explore else 'echarts'
    return f'https://x-cmd.com/draw/{kind}?' + q


def refit(opt, w, h, title=''):
    """Return (new option, collisions left) for one chart option."""
    spec = {'w': w, 'h': h, 'title': title}
    cand, url, bad = fit_labels(opt, spec, lambda o: encode(o, w, h))
    d = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['d'][0]
    return json.loads(d), bad


def process(path, w, h, keep=False, dry=False):
    text = open(path).read()
    seen = {}

    def repl(m):
        old = m.group(0)
        explore = bool(m.group(1))
        if old in seen:
            return seen[old]
        try:
            opt = option_of(old)
        except Exception as e:
            print(f'  ! cannot decode {old[:60]}...: {e}')
            seen[old] = old
            return old
        title = (opt.get('title') or {}).get('text', '')
        cw, ch = (canvas_of(old) if keep else (w, h))
        new_opt, bad = refit(opt, cw, ch, title)
        new = encode(new_opt, cw, ch, explore)
        if bad:
            print(f'  ! {title}: {len(bad)} label collisions left')
        else:
            try:
                n = len(label_collisions(render(new)))
                print(f'  ok {title}: {"clean" if not n else str(n) + " left"}')
            except Exception as e:
                print(f'  ! {title}: cannot render ({e})')
        seen[old] = new
        return new

    out = URL_RE.sub(repl, text)
    if not dry and out != text:
        open(path, 'w').write(out)
        print(f'  wrote {path} ({len(seen)} charts)')
    return seen


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    ap.add_argument('--w', type=int, default=760)
    ap.add_argument('--h', type=int, default=380)
    ap.add_argument('--keep', action='store_true',
                    help='keep each chart\'s own canvas size')
    ap.add_argument('--dry', action='store_true')
    a = ap.parse_args()
    for f in a.files:
        print(f)
        process(f, a.w, a.h, a.keep, a.dry)
