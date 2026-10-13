#!/usr/bin/env python3
"""Build the case study: prepare images, build docx, take page numbers from Word's own PDF, rebuild until stable."""
import json, os, re, subprocess, sys, shutil
B = os.path.dirname(os.path.abspath(__file__)); CS = os.path.dirname(B); SUB = os.path.dirname(CS)
WORK = os.path.join(B, 'work'); os.makedirs(os.path.join(WORK, 'img'), exist_ok=True)
OUT = os.path.join(CS, 'Breakfast_Paradox_Case_Study.docx')
PDFOUT = os.path.join(CS, 'Breakfast_Paradox_Case_Study.pdf')
NP = os.path.join(SUB, 'Build', 'node_modules')

def norm(s): return re.sub(r'\s+', ' ', s).strip().lower()

def prep():
    from PIL import Image
    im = Image.open(os.path.join(SUB, 'Figures', 'Figure_4.1_m-portal.png')); w, h = im.size
    im.crop((0, int(h * 0.197), int(w * 0.49), int(h * 0.425))).save(os.path.join(WORK, 'img', 'portal.png'))

def build(pages):
    pj = os.path.join(WORK, 'pages.json'); json.dump(pages, open(pj, 'w'))
    subprocess.run(['node', os.path.join(B, 'build_case.js'), OUT, pj], check=True, cwd=B, env={**os.environ, 'NODE_PATH': NP})

def word_pdf(dest):
    tmp = os.path.join(WORK, 'word'); os.makedirs(tmp, exist_ok=True)
    shutil.copy(OUT, os.path.join(tmp, 'w.docx')); pdf = os.path.join(tmp, 'w.pdf')
    if os.path.exists(pdf): os.remove(pdf)
    script = f'''tell application "Microsoft Word"
  open POSIX file "{tmp}/w.docx"
  delay 12
  set d to active document
  save as d file name "{pdf}" file format format PDF
  close d saving no
end tell'''
    subprocess.run(['osascript', '-e', script], check=True, capture_output=True)
    if dest: shutil.copy(pdf, dest)
    return pdf

def compute(pages_txt):
    ent = json.load(open(os.path.join(B, 'entries.json')))
    lines = [[norm(l) for l in p.split('\n')] for p in pages_txt]
    res, miss = {}, []
    def find(prefix, cur):
        for i in range(cur, len(lines)):
            for l in lines[i]:
                if l.startswith(prefix) and not re.search(r'\.{4,}|(\. ){4,}', l): return i
        return None
    cur = 0
    for e in ent:
        if e['kind'] == 'h': pref = norm(e['num'] + ' ' + e['title'])[:30]
        elif e['kind'] == 'd': pref = 'decision ' + e['num'] + ' '
        elif e['kind'] == 'f': pref = 'figure ' + e['num'] + '.'
        else: pref = 'table ' + e['num'] + '.'
        i = find(pref, cur if e['kind'] == 'h' else 1)
        if i is None: miss.append(e['key']); continue
        res[e['key']] = i + 1
        if e['kind'] == 'h': cur = i
    return res, miss, len(lines) - 1

if __name__ == '__main__':
    prep()
    pages = {}
    for r in range(5):
        build(pages)
        pdf = word_pdf(None)
        txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout.split('\f')
        res, miss, n = compute(txt)
        print('round', r, 'pages', n, 'missing', miss, 'stable', res == pages)
        if res == pages: break
        pages = res
    json.dump(pages, open(os.path.join(WORK, 'pages.json'), 'w'))
    shutil.copy(pdf, PDFOUT)
    print('pdf ->', PDFOUT)
