"""Two framing diagrams for the project documentation, drawn with the Phase 1 diagram kit."""
import sys, os, shutil
KIT = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-1-rebuild/Assets/gen"
sys.path.insert(0, KIT)
from p1kit import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "newfig")

def finish(name):
    src = os.path.join(ASSETS, name)
    shutil.move(src, os.path.join(OUT, name))

def framework():
    c = Canvas(1360, 660, "Project structure: four phases, ten activities, fifteen deliverables", "Each activity ends in one or more deliverables; later phases build on the findings of earlier ones")
    cols = [("Phase 1: Understand the system", "tech", 30, 350),
            ("Phase 2: Model the system", "biz", 400, 330),
            ("Phase 3: Find the levers", "soc", 750, 280),
            ("Phase 4: Design and test", "users", 1050, 280)]
    for (t, k, x, w), zh in zip(cols, (550, 400, 250, 290)):
        c.zone(x, 100, w, zh, t, k, fs=15)
    A = {
     0: [("A1 System context", "System Context Brief"),
         ("A2 Stakeholders", "Stakeholder Map"),
         ("A3 Power, interest, leverage", "Power-Interest/Leverage Map and Power Analysis Brief"),
         ("A4 Existing process", "Process Trace"),
         ("A5 Behaviour over time", "System Timeline / Behaviour-Over-Time Map")],
     1: [("A6 System map", "System Map; Causal Loop and Feedback Analysis"),
         ("A7 Patterns and root causes", "Systemic Problem Analysis"),
         ("A8 Reframe the problem", "Reframed Problem Statement; Design Opportunity Statement")],
     2: [("A9 Principles and intervention points", "Leverage-Point / Intervention Map; Design Principles")],
     3: [("A10 Design, test, evaluate", "Intervention Concepts and Prototypes; Scenario Model and Impact Evaluation; Final System Design Recommendation")],
    }
    prev = None
    for i, (t, k, x, w) in enumerate(cols):
        y = 150
        last = None
        for (a, d) in A[i]:
            h = 82 if i < 2 else 150
            n = c.node(x + 14, y, w - 28, h, a, d, k, None, False, fs=15, sfs=12.5)
            if last: c.edge(last, n, C[k][0], None, width=2.4)
            last = n
            y += h + 12
        if i == 0: p1_last = last
    c.render("sub-framework.png"); finish("sub-framework.png")

def timeline():
    c = Canvas(1360, 470, "Project timeline, September to October 2026", "In order of date; cards are evenly spaced, not drawn to scale")
    items = [("3 Sep", "First interview (a team member); portal screenshots", "tech"),
             ("5 and 6 Sep", "Stakeholder and power work; five student interviews; Phase 1 first submission", "tech"),
             ("12 to 14 Sep", "Phase 2 written: system map, loops, root causes, reframe", "biz"),
             ("13 Sep", "Facilities head interview; Kadamba kitchen walkthrough; four posters", "amber"),
             ("26 Sep", "Field visits to the kitchens; registers photographed; April scan export", "users"),
             ("27 Sep", "Full revision of Phases 1 and 2 on the new records", "red"),
             ("27 and 28 Sep", "Phases 3 and 4 written", "soc"),
             ("28 Sep", "Summary of the Bakul interview received and folded in", "pink"),
             ("Early Oct", "All deliverables rebuilt from the revised evidence", "slate")]
    w, h = 236, 130
    prev = None
    for i, (d, t, k) in enumerate(items):
        row, col = (0, i) if i < 5 else (1, i - 5)
        x = 30 + col * (w + 28) + (0 if row == 0 else (w + 28) / 2)
        y = 120 + row * 190
        n = c.node(x, y, w, h, d, t, k, None, False, fs=16, sfs=13)
        if prev and i != 5: c.edge(prev, n, "#37474f", None, width=2.4)
        prev = n
    c.render("sub-timeline.png"); finish("sub-timeline.png")

if __name__ == "__main__":
    framework(); timeline()
