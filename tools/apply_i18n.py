"""Merge a translation (list of prose strings, null at chart positions) into a page JSON."""
import json, sys


def merge(en_json_path, tr_json_path, out_json_path):
    en = json.load(open(en_json_path))
    tr = json.load(open(tr_json_path))
    blocks = en['blocks']
    if isinstance(tr, dict):
        tr_list = tr['blocks']
        data = tr.get('data')
    else:
        tr_list = tr
        data = None
    if len(tr_list) != len(blocks):
        raise SystemExit(f'{tr_json_path}: {len(tr_list)} blocks vs {len(blocks)} in English')
    merged = []
    for i, b in enumerate(blocks):
        if isinstance(b, str):
            t = tr_list[i]
            if not t or not t.strip():
                raise SystemExit(f'{tr_json_path}: missing translation at block {i}')
            merged.append(t)
        else:
            if tr_list[i] is not None:
                raise SystemExit(f'{tr_json_path}: chart block {i} must be null')
            merged.append(b)
    en['blocks'] = merged
    if data:
        en['data'] = data
    json.dump(en, open(out_json_path, 'w'), ensure_ascii=False, indent=1)
    return out_json_path


if __name__ == '__main__':
    print(merge(sys.argv[1], sys.argv[2], sys.argv[3]))
