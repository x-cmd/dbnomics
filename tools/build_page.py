"""Build a docs page from a page JSON.

page JSON:
{
  "data": "**Data**: ... **Reproduce**: `...`",
  "data_i18n": {"cn": "...", "es": "...", "ja": "...", "de": "..."},
  "blocks": [
     {"prose": "..."},
     {"chart": {"spec": {...}, "alt": "x", "width": 760}},
     {"chart": {"url": "https://po6.sh/draw/echarts?d=..."}}
  ],
  "i18n": {"cn": [{"prose": "..."}, null, ...], "es": [...], "ja": [...], "de": [...]}
}
The i18n list is positional: same length as blocks, null where the block is a chart.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mkchart import url_for

ROOT = '/Users/l/.x-repo/github.com/x-cmd/dbnomics'


def render(page_json, lang, page_dir):
    blocks = page_json['blocks']
    i18n = page_json.get('i18n', {}).get(lang) or []
    parts = []
    for i, b in enumerate(blocks):
        if isinstance(b, str) or 'prose' in b:
            txt = b if isinstance(b, str) else b['prose']
            if lang != 'en' and i < len(i18n) and i18n[i]:
                entry = i18n[i]
                txt = entry['prose'] if isinstance(entry, dict) and 'prose' in entry else entry
            elif lang != 'en' and (not i18n or i >= len(i18n) or not i18n[i]):
                if not page_json.get('pretranslated'):
                    raise SystemExit(f'{page_dir}: missing {lang} translation for block {i}')
            parts.append(txt)
        elif 'table' in b:
            parts.append(b['table'])
        elif 'shell' in b:
            parts.append(b['shell'])
        elif 'chart' in b:
            c = b['chart']
            u = c.get('url')
            if not u:
                u = url_for(c['spec'])
            explore = u.replace('/draw/echarts?', '/draw/explore/echarts?')
            parts.append(f"```text\n{u}\n```\n\n"
                         f'<a href="{explore}"><img src="{u}" width="{c.get("width", 680)}" alt="{c.get("alt", "chart")}"></a>')
        else:
            raise SystemExit(f'unknown block: {list(b)}')
    body = '\n\n'.join(parts)
    data = page_json.get('data', '')
    if lang != 'en' and page_json.get('data_i18n', {}).get(lang):
        data = page_json['data_i18n'][lang]
    if data:
        body += '\n\n' + data
    body += '\n'
    path = os.path.join(ROOT, page_dir, lang + '.md')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(body)
    return path


def build_all(page_json, page_dir, langs=('en', 'cn', 'es', 'ja', 'de')):
    out = []
    for lang in langs:
        out.append(render(page_json, lang, page_dir))
    return out


if __name__ == '__main__':
    src, page_dir = sys.argv[1], sys.argv[2]
    langs = sys.argv[3:] or ['en', 'cn', 'es', 'ja', 'de']
    pj = json.load(open(src))
    for p in build_all(pj, page_dir, langs):
        print('wrote', p)
