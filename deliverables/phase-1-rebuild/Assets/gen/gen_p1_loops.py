import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def circle_loop(c, cx, cy, r, nodes, w=230, h=70):
    out = []
    n = len(nodes)
    for i, (t, s, k, d) in enumerate(nodes):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out.append(c.node(x - w / 2, y - h / 2, w, h, t, s, k, None, d, fs=14, sfs=11.5))
    return out

def d10():
    c = Canvas(1100, 960, "R1: Mess Cell as a shifting-the-burden loop", "Open chain held as a candidate loop; dashed links are inferences no respondent stated")
    nodes = [("Billing not tied to attendance", "the structural cause", "red", False),
             ("Unused registrations", "flat registrations, 27 to 42% turnout", "tech", False),
             ("Financial pain to the student", "charged for meals not eaten", "users", False),
             ("Resale on Mess Cell", "four of six respondents use it", "pink", False),
             ("Pressure to fix billing", "no respondent stated this", "soc", True)]
    ns = circle_loop(c, 550, 470, 330, nodes, 250, 80)
    g = "#37474f"
    E = lambda a, b, col, s, d=None, bend=0.12, lab=None: c.edge(ns[a], ns[b], col, lab, dash=d, width=3.2, bend=bend, sign=s)
    E(0, 1, g, "+"); E(1, 2, g, "+"); E(2, 3, g, "+")
    E(3, 2, C["green"][0], "-", None, 0.3)
    E(2, 4, C["soc"][0], "+", "7 5")
    E(4, 0, C["soc"][0], "-", "7 5")
    c.badge(550, 470, "R1", "#37474f", r=26, fs=20)
    c.add(f'<text x="640" y="890" font-size="14" fill="#37474f" font-weight="700">Relief lowers the pain, so the pressure to fix billing stays low.</text>')
    c.legend(30, 830, [(g, "evidenced link", "line"), (C["soc"][0], "inferred link (dashed)", "dash"), (C["green"][0], "balancing relief (evidenced)", "line")], title="Signs: + moves together, - moves opposite", fs=12)
    c.render("d10-loop-r1.png")

def mini(c, x, y, title, labels, signs, delay=None, dashes=(), w=250):
    col = "#37474f"
    c.add(f'<text x="{x}" y="{y-14}" font-size="15" font-weight="800" fill="#0d47a1">{esc(title)}</text>')
    pos = [(x, y), (x + 330, y), (x + 165, y + 150)]
    ns = [c.node(px, py, w, 70, l[0], l[1], l[2], None, l[3], fs=13.5, sfs=11) for (px, py), l in zip(pos, labels)]
    for i in range(3):
        j = (i + 1) % 3
        d = "7 5" if i in dashes else None
        c.edge(ns[i], ns[j], col, None, dash=d, width=3, bend=0.2, sign=signs[i])
    if delay:
        c.pill(x + 290, y + 250, delay, "amber", fs=11.5)
    return ns

def d11():
    c = Canvas(1260, 1000, "B1: balancing channels in the kitchen", "Each mess closes its own loop with a different delay; Skip Meal's link to the kitchen is unresolved")
    mini(c, 30, 130, "Kadamba: shortage loop, upward only",
         [("Food left at the counter", "against expected demand", "biz", False), ("Supervisor calls a top-up", "ready in 10 to 15 minutes", "biz", False), ("Shortage at the counter", "run-out", "red", False)],
         ["-", "-", "-"], "delay: minutes; nothing shrinks the next first batch")
    mini(c, 650, 130, "Yuktāhār: surplus loop, two weeks",
         [("Surplus recorded", "Wastage Book, weekday register", "green", False), ("Smaller matching-week batch", "planned at the daily meeting", "tech", False), ("Surplus", "cooked against eaten", "red", False)],
         ["+", "-", "+"], "delay: two weeks (a within-meal channel adds minutes, upward only)")
    mini(c, 30, 500, "Bakul: weekly loop with a floor",
         [("Surplus seen by the manager", "from attendance history, in his head", "amber", True), ("Share lowered, never below about 70%", "weekly review", "biz", False), ("Surplus", "bounded by the floor", "red", False)],
         ["+", "-", "+"], "delay: about a week; a phone top-up adds a 20 to 40 minute drive", dashes=(0,))
    c.add(f'<text x="650" y="486" font-size="15" font-weight="800" fill="#0d47a1">Skip Meal and the Kadamba kitchen</text>')
    sk = c.node(650, 510, 270, 84, "Skip Meal declaration", "charge stands; returns nothing", "amber", "ic-toggle", True, fs=14, sfs=11.5)
    cnt = c.node(980, 510, 260, 84, "Count Kadamba cooks from", "registrations only, says the operator", "biz", "ic-pot", False, fs=14, sfs=11.5)
    c.edge(sk, cnt, C["amber"][0], None, dash="7 5", width=3)
    c.pill(950, 500, "unresolved", "amber", fs=12)
    c.text(650, 630, "The institution's account says declarations reach the kitchen. The Kadamba operator says it cooks on registrations alone. None of the six student respondents has used Skip Meal.", 13, False, "#444", width=590)
    c.text(30, 900, "None of the three loops is calibrated to actual breakfast turnout, and the records that would calibrate them never leave the kitchen.", 14, True, "#c62828", width=1180)
    c.legend(30, 930, [("#37474f", "evidenced or operator-stated link", "line"), ("#37474f", "inferred link (dashed)", "dash")], title="Signs: + moves together, - moves opposite", fs=12)
    c.render("d11-loop-b1.png")

if __name__ == "__main__":
    d10(); d11()
