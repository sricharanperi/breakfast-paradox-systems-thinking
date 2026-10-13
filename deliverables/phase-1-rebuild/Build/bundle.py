#!/usr/bin/env python3
"""Build every Phase 1 PDF, the cover, and the combined document. Run from anywhere."""
import os, sys, subprocess
from pypdf import PdfReader, PdfWriter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import build, ROOT, BUILD

SRC = os.path.join(ROOT, "Source"); OUT = os.path.join(ROOT, "PDFs")
DOCS = [("01-system-context-brief", "System Context Brief", "Activity 1"),
        ("02-stakeholder-map", "Stakeholder Map", "Activity 2"),
        ("03-power-interest-leverage-map", "Stakeholder Power-Interest/Leverage Map and Power Analysis Brief", "Activity 3"),
        ("04-process-trace", "Current-State Process Map / Process Trace", "Activity 4"),
        ("05-system-timeline-bot-map", "System Timeline / Behaviour-Over-Time Map", "Activity 5"),
        ("00-consolidated-phase1-report", "Phase 1 Consolidated Report", "Summary of all five")]
FILES = {"01-system-context-brief": "System Context Brief", "02-stakeholder-map": "Stakeholder Map",
         "03-power-interest-leverage-map": "Power-Interest Leverage Map", "04-process-trace": "Process Trace",
         "05-system-timeline-bot-map": "System Timeline BOT Map", "00-consolidated-phase1-report": "Phase 1 Consolidated Report"}

def main(rebuild=True):
    pages = {}
    for key, title, act in DOCS:
        pdf = os.path.join(OUT, FILES[key] + ".pdf")
        if rebuild: build(os.path.join(SRC, key + ".md"), pdf)
        pages[key] = len(PdfReader(pdf).pages)
    start = 2; rows = []
    for key, title, act in DOCS:
        rows.append((act, title, start, pages[key])); start += pages[key]
    amp = "\\&"
    tbl = "\n".join(a + " & " + t.replace("&", amp) + " & " + str(s) + " & " + str(n) + " \\\\" for a, t, s, n in rows)
    cover = r"""\thispagestyle{empty}
\vspace*{1.3in}
\begin{center}
{\color{pblue2}\fontsize{14}{16}\selectfont\bfseries TEAM INVICTUS\par}
\vspace{16pt}
{\color{pblue}\fontsize{34}{40}\selectfont\bfseries Systems Thinking \& Design\par Phase 1 Submission\par}
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
\begin{tabular}{@{}p{1.3in}p{3.7in}rr@{}}
\textbf{\color{pblue}Activity} & \textbf{\color{pblue}Deliverable} & \textbf{\color{pblue}Starts on page} & \textbf{\color{pblue}Pages}\\
\hline
""" + tbl + r"""
\end{tabular}
\end{center}
"""
    cmd = os.path.join(BUILD, "work", "cover.md")
    os.makedirs(os.path.dirname(cmd), exist_ok=True)
    open(cmd, "w").write(cover)
    coverpdf = os.path.join(BUILD, "work", "cover.pdf")
    build(cmd, coverpdf, toc=False)
    w = PdfWriter(); w.append(coverpdf)
    marks = [("Cover and contents", 0)]
    for key, title, act in DOCS:
        marks.append((title, len(w.pages))); w.append(os.path.join(OUT, FILES[key] + ".pdf"))
    for t, p in marks: w.add_outline_item(t, p)
    w.add_metadata({"/Title": "Invictus Phase 1", "/Author": "", "/Subject": "", "/Creator": "", "/Producer": ""})
    with open(os.path.join(OUT, "Invictus_Phase1_Complete.pdf"), "wb") as f: w.write(f)
    print("combined:", len(w.pages), "pages")

if __name__ == "__main__":
    main(rebuild="--no-rebuild" not in sys.argv)
