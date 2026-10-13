#!/usr/bin/env python3
"""Story book build. Usage: story_build.py SRC.md OUT.pdf"""
import sys, os, subprocess
from pypdf import PdfReader, PdfWriter
BUILD = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(BUILD)
def build(src, out_pdf, toc=True):
    stem = os.path.splitext(os.path.basename(out_pdf))[0]; work = os.path.join(BUILD, "work_" + stem); os.makedirs(work, exist_ok=True)
    stem0 = stem; tex = os.path.join(work, stem + ".tex")
    cmd = ["pandoc", "-f", "markdown-smart-tex_math_dollars-raw_html-native_spans-header_attributes-auto_identifiers+fenced_divs+bracketed_spans",
           "-t", "latex", "-s", "--wrap=preserve", "--include-in-header=" + os.path.join(BUILD, "story_header.tex"),
           "--lua-filter=" + os.path.join(BUILD, "story.lua"),
           "-V", "documentclass=article", "-V", "classoption=table", "-V", "fontsize=11pt",
           "-V", "geometry:paperwidth=8.5in", "-V", "geometry:paperheight=8.5in", "-V", "geometry:left=1.05in", "-V", "geometry:right=1.05in",
           "-V", "geometry:top=0.75in", "-V", "geometry:bottom=0.8in", "-V", "linestretch=1.15", "-V", "colorlinks=true", "-V", "linkcolor=cLook", "-V", "toccolor=cLook",
           "-V", "toc-title=Contents"]
    if toc: cmd += ["--toc", "--toc-depth=1"]
    cmd += [src, "-o", tex]; subprocess.run(cmd, check=True)
    s = open(tex).read().replace("height=\\textheight", "height=0.65\\textheight"); open(tex, "w").write(s)
    import re; s = re.sub(r"\\begin\{figure\}(\s*\\centering\s*\\includegraphics\[[^\]]*\]\{Assets/(?:zzz-none)\.)", lambda m: "\\begin{figure}[H]" + m.group(1), s); open(tex, "w").write(s)
    r = subprocess.run(["tectonic", "-X", "compile", "--keep-logs", "-Z", "search-path=" + ROOT, tex, "--outdir", work], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0: print((r.stdout + r.stderr)[-3000:]); sys.exit(1)
    rd = PdfReader(os.path.join(work, stem + ".pdf")); w = PdfWriter(); w.append(rd)
    w.add_metadata({"/Title": "", "/Author": "", "/Subject": "", "/Creator": "", "/Producer": ""})
    with open(out_pdf, "wb") as f: w.write(f)
    print("built", out_pdf, len(rd.pages), "pages")
if __name__ == "__main__": build(sys.argv[1], sys.argv[2], toc="--no-toc" not in sys.argv)
