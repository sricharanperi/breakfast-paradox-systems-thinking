#!/usr/bin/env python3
"""Final pass using Microsoft Word's own pagination: build, export a PDF from Word, take page numbers from it, rebuild until stable."""
import json, os, subprocess, sys, shutil
B = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, B)
import make
TMP = os.path.join(make.WORK, 'word'); os.makedirs(TMP, exist_ok=True)
def word_pdf():
    shutil.copy(make.OUT, os.path.join(TMP, 'w.docx')); pdf = os.path.join(TMP, 'w.pdf')
    if os.path.exists(pdf): os.remove(pdf)
    script = f'''tell application "Microsoft Word"
  open POSIX file "{TMP}/w.docx"
  delay 15
  set d to active document
  save as d file name "{pdf}" file format format PDF
  close d saving no
end tell'''
    subprocess.run(['osascript', '-e', script], check=True, capture_output=True)
    return pdf
pages = json.load(open(os.path.join(make.WORK, 'pages.json')))
for r in range(4):
    make.build(pages)
    pdf = word_pdf()
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout.split('\f')
    res, miss, start, n = make.compute(txt)
    diff = {k: (pages.get(k), v) for k, v in res.items() if pages.get(k) != v}
    print('round', r, 'word pages', n - 1, 'missing', miss, 'diffs', len(diff))
    if not diff: break
    pages = res
json.dump(pages, open(os.path.join(make.WORK, 'pages.json'), 'w'))
