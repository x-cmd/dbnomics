"""Give every language its own chart: the numbers stay, the labels change.

The English page holds the canonical charts. For each other language the
option is decoded, the labels are swapped for the translated ones
(`tools/labels/<lang>.json`), the result is re-fitted (CJK labels are wider,
so a chart that was clean in English can collide in Chinese) and the URL is
written back into that language's markdown.

usage:
    python3 tools/localize.py                      # every page, every language
    python3 tools/localize.py docs/5-us-casestudy/03-us-states
"""
import glob
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mkchart import apply_labels, fit_labels, label_collisions, render  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABELS = os.path.join(ROOT, 'tools', 'labels')
CHART = re.compile(r'https://x-cmd[.]com/draw/(explore/)?echarts[?]d=[^&\s")]+(?:&w=\d+)?(?:&h=\d+)?')
TEXT_BLOCK = re.compile(r'```text\n(https://x-cmd[.]com/draw/echarts[?]d=[^\n]+)\n```')
IMG_BLOCK = re.compile(r'<a href="(https://x-cmd[.]com/draw/explore/echarts[?]d=[^"]+)">'
                       r'<img src="(https://x-cmd[.]com/draw/echarts[?]d=[^"]+)"'
                       r' width="(\d+)" alt="([^"]*)"></a>')


def option_of(url):
    d = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['d'][0]
    return json.loads(d)


def canvas_of(url):
    q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    return int(q.get('w', ['560'])[0]), int(q.get('h', ['320'])[0])


def encode(opt, w, h):
    q = 'd=' + urllib.parse.quote(json.dumps(opt, ensure_ascii=False,
                                             separators=(',', ':')), safe='')
    if w:
        q += f'&w={w}'
    if h:
        q += f'&h={h}'
    return 'https://x-cmd.com/draw/echarts?' + q


def chart_urls(text):
    """The chart URLs of a page, in document order (one per chart)."""
    return [m.group(1) for m in TEXT_BLOCK.finditer(text)]


def localize_page(page_dir, langs=('cn', 'es', 'ja', 'de'), dry=False):
    en_path = os.path.join(page_dir, 'en.md')
    en_text = open(en_path).read()
    en_urls = chart_urls(en_text)
    if not en_urls:
        return
    for lang in langs:
        vocab_file = os.path.join(LABELS, f'{lang}.json')
        vocab = json.load(open(vocab_file)) if os.path.exists(vocab_file) else {}
        path = os.path.join(page_dir, f'{lang}.md')
        if not os.path.exists(path):
            continue
        text = open(path).read()
        urls = chart_urls(text)
        if len(urls) != len(en_urls):
            print(f'  ! {page_dir}/{lang}: {len(urls)} charts vs {len(en_urls)} in en.md - skipped')
            continue
        new_urls = []
        for en_url in en_urls:
            opt = option_of(en_url)
            w, h = canvas_of(en_url)
            loc = apply_labels(opt, vocab)
            spec = {'w': w, 'h': h}
            cand, url, bad = fit_labels(loc, spec, lambda o: encode(o, w, h))
            if bad:
                print(f'  ! {page_dir}/{lang}: {len(bad)} label collisions left on {opt.get("title", {}).get("text", "")[:40]}')
            new_urls.append(url)
        # write the new URLs back: the ```text block, then the img + explore link
        it = iter(new_urls)

        def sub_text(m):
            return f'```text\n{next(it)}\n```'

        out = TEXT_BLOCK.sub(sub_text, text)
        it2 = iter(new_urls)

        def sub_img(m):
            u = next(it2)
            return (f'<a href="{u.replace("/draw/echarts?", "/draw/explore/echarts?")}">'
                    f'<img src="{u}" width="{m.group(3)}" alt="{m.group(4)}"></a>')

        out = IMG_BLOCK.sub(sub_img, out)
        if not dry and out != text:
            open(path, 'w').write(out)
            print(f'  {page_dir}/{lang}: {len(new_urls)} charts localised')


if __name__ == '__main__':
    args = sys.argv[1:]
    dry = '--dry' in args
    args = [a for a in args if a != '--dry']
    dirs = args or sorted(glob.glob(os.path.join(ROOT, 'docs', '*', '*')))
    for d in dirs:
        if os.path.isdir(d):
            print(d.replace(ROOT + '/', ''))
            localize_page(d, dry=dry)
