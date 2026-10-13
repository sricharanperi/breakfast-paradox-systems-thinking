#!/usr/bin/env python3
"""Combine the finished PDFs of one phase behind a cover. Usage: bundle.py CONFIG_NAME"""
import os, sys
from pypdf import PdfReader, PdfWriter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import build, ROOT, BUILD
OUT = os.path.join(ROOT, "PDFs")
CFG = {
 "phase2": ("Phase 2 Submission", "Systems Thinking \\& Design", [
   ("Activity 6", "System Map", "System Map.pdf"), ("Activity 6", "Causal Loop and Feedback Analysis", "Causal Loop and Feedback Analysis.pdf"),
   ("Activity 7", "Systemic Problem Analysis", "Systemic Problem Analysis.pdf"), ("Activity 8", "Reframed Systemic Problem Statement", "Reframed Systemic Problem Statement.pdf"),
   ("Activity 8", "Design Opportunity Statement", "Design Opportunity Statement.pdf"), ("All five", "Corrections Since the First Submission", "Corrections.pdf")],
   "Invictus_Phase2_Complete.pdf"),
 "phase34": ("Phase 3 and Phase 4 Submission", "Systems Thinking \\& Design", [
   ("Activity 9", "Leverage Points and Design Principles", "Activity 9 Leverage Points and Design Principles.pdf"),
   ("Activity 10", "Design, Test and Evaluate Interventions", "Activity 10 Design Test and Evaluate Interventions.pdf")],
   "Invictus_Phase3_4_Complete.pdf")}
name = sys.argv[1]; title, sub, docs, outname = CFG[name]
if name == "phase2":
    build(os.path.join(ROOT, "Source", "Phase2-corrections.md"), os.path.join(OUT, "Corrections.pdf"))
pages = [len(PdfReader(os.path.join(OUT, f)).pages) for _, _, f in docs]
start = 2; rows = []
for (a, t, f), n in zip(docs, pages):
    rows.append(f"{a} & {t} & {start} & {n} \\\\"); start += n
cover = r"""\thispagestyle{empty}
\vspace*{1.3in}
\begin{center}
{\color{pblue2}\fontsize{14}{16}\selectfont\bfseries TEAM INVICTUS\par}
\vspace{16pt}
{\color{pblue}\fontsize{32}{38}\selectfont\bfseries """ + sub + r"""\par """ + title + r"""\par}
\vspace{14pt}
{\color{pslate}\Large The Breakfast Paradox\par}
{\color{pslate}\normalsize IIIT Hyderabad Breakfast Mess System\par}
\vspace{18pt}
{\color{prule}\rule{2.6in}{1.4pt}}
\end{center}
\vspace{22pt}
\begin{center}
\renewcommand{\arraystretch}{1.5}
\footnotesize
\begin{tabular}{@{}p{1.0in}p{3.7in}rr@{}}
\textbf{\color{pblue}Activity} & \textbf{\color{pblue}Document} & \textbf{\color{pblue}Starts on page} & \textbf{\color{pblue}Pages}\\
\hline
""" + "\n".join(rows) + r"""
\end{tabular}
\end{center}
"""
cmd = os.path.join(BUILD, "work", "cover_" + name + ".md"); os.makedirs(os.path.dirname(cmd), exist_ok=True); open(cmd, "w").write(cover)
cp = os.path.join(BUILD, "work", "cover_" + name + ".pdf"); build(cmd, cp, toc=False)
w = PdfWriter(); w.append(cp); marks = [("Cover and contents", 0)]
for a, t, f in docs:
    marks.append((t, len(w.pages))); w.append(os.path.join(OUT, f))
for t, p in marks: w.add_outline_item(t, p)
w.add_metadata({"/Title": title, "/Author": "", "/Subject": "", "/Creator": "", "/Producer": ""})
with open(os.path.join(OUT, outname), "wb") as fh: w.write(fh)
print(outname, len(w.pages), "pages")
