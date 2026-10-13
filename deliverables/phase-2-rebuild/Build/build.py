#!/usr/bin/env python3
"""Markdown -> LaTeX -> PDF (tectonic), Phase 2 look. Usage: build.py SRC.md OUT.pdf [--no-toc]"""
import sys, os, subprocess, shutil, tempfile
from pypdf import PdfReader, PdfWriter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # phase-1-rebuild/
BUILD = os.path.join(ROOT, "Build")

def build(src, out_pdf, toc=True):
    work = os.path.join(BUILD, "work"); os.makedirs(work, exist_ok=True)
    stem = os.path.splitext(os.path.basename(src))[0]
    tex = os.path.join(work, stem + ".tex")
    cmd = ["pandoc", "-f", "markdown-smart-tex_math_dollars-raw_html-fenced_divs-bracketed_spans-native_divs-native_spans-header_attributes-auto_identifiers",
           "-t", "latex", "-s", "--wrap=preserve",
           "--include-in-header=" + os.path.join(BUILD, "header.tex"),
           "--lua-filter=" + os.path.join(BUILD, "tables.lua"),
           "-V", "documentclass=article", "-V", "classoption=table", "-V", "fontsize=10pt",
           "-V", "geometry:letterpaper", "-V", "geometry:left=0.7in", "-V", "geometry:right=0.7in",
           "-V", "geometry:top=0.7in", "-V", "geometry:bottom=0.75in",
           "-V", "linestretch=1.08", "-V", "colorlinks=true", "-V", "linkcolor=pblue2", "-V", "urlcolor=pblue2", "-V", "toccolor=pslate",
           "-V", "toc-title=Contents"]
    if toc: cmd += ["--toc", "--toc-depth=2"]
    cmd += [src, "-o", tex]
    subprocess.run(cmd, check=True)
    r = subprocess.run(["tectonic", "-X", "compile", "--keep-logs", "-Z", "search-path=" + ROOT, tex, "--outdir", work],
                       cwd=ROOT, capture_output=True, text=True)
    log = r.stdout + r.stderr
    if r.returncode != 0:
        print(log[-3000:]); sys.exit(1)
    for line in log.splitlines():
        if "Missing character" in line or "Overfull" in line and "pt too wide" in line and float(line.split("(")[1].split("pt")[0]) > 25:
            print("WARN", line.strip()[:160])
    pdf = os.path.join(work, stem + ".pdf")
    rd = PdfReader(pdf); w = PdfWriter(); w.append(rd)
    w.add_metadata({"/Title": "", "/Author": "", "/Subject": "", "/Creator": "", "/Producer": ""})
    with open(out_pdf, "wb") as f: w.write(f)
    print("built", out_pdf, len(rd.pages), "pages")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], toc="--no-toc" not in sys.argv)
