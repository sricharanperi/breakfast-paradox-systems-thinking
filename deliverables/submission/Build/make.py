#!/usr/bin/env python3
"""Two-pass build: docx -> pdf (LibreOffice) -> printed page numbers -> docx again."""
import json, os, re, subprocess, sys, shutil
B = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.dirname(B)
WORK = os.path.join(B, 'work'); os.makedirs(WORK, exist_ok=True)
OUT = os.path.join(SUB, 'Project_Documentation.docx')
SOFFICE = '/opt/homebrew/bin/soffice'

def norm(s): return re.sub(r'\s+', ' ', s).strip().lower()

def build(pages):
    pj = os.path.join(WORK, 'pages.json'); json.dump(pages, open(pj, 'w'))
    subprocess.run(['node', os.path.join(B, 'build_docx.js'), OUT, pj], check=True, cwd=B)

def render():
    subprocess.run([SOFFICE, '--headless', '--convert-to', 'pdf', '--outdir', WORK, OUT], check=True, capture_output=True)
    pdf = os.path.join(WORK, 'Project_Documentation.pdf')
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    return pdf, txt.split('\f')

def compute(pages_txt):
    ent = json.load(open(os.path.join(B, 'entries.json')))
    lines = [[norm(l) for l in p.split('\n')] for p in pages_txt]
    start = None
    for i, ls in enumerate(lines):
        if any(re.fullmatch(r'1 introduction', l) for l in ls):
            start = i; break
    assert start is not None, 'body start not found'
    res = {}; cur = start
    def find(prefix, cur):
        for i in range(cur, len(lines)):
            for l in lines[i]:
                if l.startswith(prefix) and '....' not in l:
                    return i
        return None
    missing = []
    seq = []
    for e in ent['toc']:
        pref = norm((e['num'] + ' ' if e['num'] else '') + e['title'])
        if e['level'] == 1 and e.get('appendix'): pref = norm(e['num'] + ': ' + e['title'])
        seq.append((e['key'], pref[:28]))
    # headings in document order interleaved with figures and tables: search each independently from `start`,
    # but keep headings monotonic
    for key, pref in seq:
        i = find(pref, cur)
        if i is None: missing.append(key); continue
        res[key] = i - start + 1; cur = i
    for e in ent['lof']:
        pref = norm('Figure ' + e['num'] + ':')
        i = find(pref, start)
        if i is None: missing.append(e['key']); continue
        res[e['key']] = i - start + 1
    for e in ent['lot']:
        pref = norm('Table ' + e['num'] + ':')
        i = find(pref, start)
        if i is None: missing.append(e['key']); continue
        res[e['key']] = i - start + 1
    return res, missing, start, len(lines)

def gap_pages(pdf, txt_pages, start):
    import glob
    for f in glob.glob(os.path.join(WORK, 'gp-*')): os.remove(f)
    subprocess.run(['pdftoppm', '-gray', '-r', '30', pdf, os.path.join(WORK, 'gp')], check=True)
    from PIL import Image
    fs = sorted(glob.glob(os.path.join(WORK, 'gp-*.pgm')))
    res = []
    for i, f in enumerate(fs):
        im = Image.open(f); w, h = im.size; px = im.load(); last = 0
        for y in range(int(h * 0.08), int(h * 0.93)):
            if any(px[x, y] < 200 for x in range(int(w * 0.1), int(w * 0.9), 2)): last = y
        res.append((h * 0.93 - last) / (h * 0.85))
        os.remove(f)
    return res

def optimize(rounds=5):
    dj = os.path.join(WORK, 'delays.json')
    delays = json.load(open(dj)) if os.path.exists(dj) else {}
    ent = json.load(open(os.path.join(B, 'entries.json')))
    for r in range(rounds):
        json.dump(delays, open(dj, 'w'))
        build(json.load(open(os.path.join(WORK, 'pages.json'))) if os.path.exists(os.path.join(WORK, 'pages.json')) else {})
        pdf, pt = render()
        res, miss, start, n = compute(pt)
        build(res)  # numbers for this layout
        pdf, pt = render()
        gaps = gap_pages(pdf, pt, start)
        changed = 0
        for p in range(start, len(pt) - 1):
            if p >= len(gaps) - 1: break
            if gaps[p] > 0.2:
                nxt = [x for x in (norm(l) for l in pt[p + 1].split('\n')) if x]
                idx = [k for k, l in enumerate(nxt) if re.match(r'figure \d+\.\d+:', l)]
                if idx and idx[0] <= 3:
                    key = 'f:' + re.match(r'figure (\d+\.\d+):', nxt[idx[0]]).group(1)
                    if delays.get(key, 0) < 4:
                        delays[key] = delays.get(key, 0) + 1; changed += 1
        print('round', r, 'pages', len(pt) - 1, 'gap pages', sum(1 for g in gaps[start:] if g > 0.2), 'changed', changed)
        if not changed: break
    json.dump(delays, open(dj, 'w'))

if __name__ == '__main__' and '--optimize' in sys.argv:
    optimize(); sys.exit(0)

if __name__ == '__main__':
    build({})
    pdf, pt = render()
    res, miss, start, n = compute(pt)
    print('pass1: body starts at pdf page', start + 1, 'of', n - 1, 'missing', miss)
    build(res)
    pdf, pt = render()
    res2, miss2, start2, n2 = compute(pt)
    print('pass2: body starts at', start2 + 1, 'pages', n2 - 1, 'missing', miss2, 'stable', res == res2)
    if res != res2:
        build(res2); pdf, pt = render(); res3, *_ = compute(pt); print('pass3 stable', res2 == res3)
