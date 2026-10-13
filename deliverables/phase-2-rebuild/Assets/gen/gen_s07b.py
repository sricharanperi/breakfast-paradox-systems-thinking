import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *
G = "#37474f"; RED = C["red"][0]; AMB = C["amber"][0]

def circle(c, cx, cy, r, nodes, w=210, h=76, fs=13.5, sfs=11.5):
    out = []; n = len(nodes)
    for i, (t, s, k, d) in enumerate(nodes):
        a = -math.pi / 2 + i * 2 * math.pi / n
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out.append(c.node(x - w / 2, y - h / 2, w, h, t, s, k, None, d, fs=fs, sfs=sfs))
    return out

def outpill(c, a, b, text, key="amber", bend=0.12, off=30, fs=11):
    """pill outside the curve between nodes a and b"""
    x1, y1 = a.cx, a.cy; x2, y2 = b.cx, b.cy
    dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy)
    nx, ny = -dy / L, dx / L
    mx, my = (x1 + x2) / 2 + nx * (bend * L / 2 + off), (y1 + y2) / 2 + ny * (bend * L / 2 + off)
    c.pill(mx, my, text, key, fs=fs)

# ---------------------------------------------------------------- dashboard
def dashboard():
    c = Canvas(1200, 640, "Loop status: eighteen mechanisms tested", "Three close with every link evidenced; most others are candidates or chains that do not close")
    rows = [("Closed, every link evidenced (balancing)", "green", ["L4  Menu rotation governance", "L11  Wastage-Book learning (Yuktāhār)", "L12  Counter top-up (upward only)"]),
            ("Candidate loop, closing link assumed", "pink", ["L1  Resale safety net", "L3b  Kadamba demand lock-in", "L9  Waste absorption", "L15  Soft close", "L17  Kitchen competence shifts the burden"]),
            ("Chain that does not close", "amber", ["L13  Standing booking to fixed-ratio surplus (core)", "L14  Closing rush to just-in-case batch", "L2  Skip Meal (kitchen link in conflict)", "L5  Menu transparency", "L6  Shock relaxation (a calendar switch)", "L7  Late-night workload to skip"]),
            ("Contraindicated, unresolved, absent or static", "red", ["L3  Capacity redistribution", "L8  Vendor discipline (plate basis unknown)", "L16  Operator waste to menu", "L10  Measured but unrouted (static)"])]
    y = 80
    for lab, key, items in rows:
        c.add(f'<text x="30" y="{y+16}" font-size="14" font-weight="800" fill="{C[key][0]}">{esc(lab)}</text>')
        for i, t in enumerate(items):
            c.node(30 + (i % 3) * 385, y + 26 + (i // 3) * 56, 372, 48, t, None, key, None, key == "pink", fs=13)
        y += 26 + ((len(items) + 2) // 3) * 56 + 20
    c.render("s07b-dashboard.png")

# ---------------------------------------------------------------- L11
def l11():
    c = Canvas(1200, 730, "L11: Yuktāhār's Wastage Book loop (balancing, confirmed at one mess)", "One negative link makes it balancing; signs: + moves together, - moves opposite")
    nodes = [("Cooked above what is eaten", "surplus and early run-outs", "red", False), ("Leftover and run-out time written down", "Wastage Book, per item", "slate", False),
             ("Meeting reads the matching past day", "twice a day; weekday register, events", "soc", False), ("Next day's issue list", "Grocery Book", "amber", False), ("Cooked quantity", "5:30 to 7:30", "biz", False)]
    ns = circle(c, 420, 395, 270, nodes)
    for i, s in enumerate(["+", "+", "-", "+", "+"]):
        c.edge(ns[i], ns[(i + 1) % 5], G, None, width=3, bend=0.1, sign=s)
    outpill(c, ns[1], ns[2], "lookup: weekday register next week, matching menu day in two weeks", "amber", 0.1, 38, 11)
    outpill(c, ns[2], ns[3], "plan fixed the day before", "amber", 0.1, 30, 11)
    c.badge(420, 395, "B", G, r=28, fs=22)
    c.add('<text x="420" y="440" font-size="13" text-anchor="middle" fill="#37474f" font-weight="700">balancing</text>')
    c.zone(870, 110, 310, 330, "Preconditions, not loops", "green", fs=13.5, opacity=0.25)
    for i, t in enumerate(["Blame-free weighing", "Peer cross-checking, no hierarchy", "Two-book rule: issued must equal cooked"]):
        c.node(884, 148 + i * 92, 282, 76, t, None, "green", None, False, fs=13.5)
    c.zone(870, 470, 310, 200, "Limits", "red", fs=13.5, opacity=0.2)
    c.text(886, 520, "Adjusts quantity, never the booking. Anchors on a wrong overall belief (about 50% against about 28%). Absent at Kadamba. Candidate at Bakul, bounded by a floor near 70%.", 12.5, False, "#333", width=280)
    c.render("s07b-l11.png")

# ---------------------------------------------------------------- L12
def l12():
    c = Canvas(1200, 800, "L12: counter monitoring and top-up (balancing, corrects upward only)", "Same loop at three halls; what differs is the delay")
    rows = [("Kadamba: supervisor against gram standards", "delay: 10 to 15 minutes on site", "biz", None),
            ("Yuktāhār: 30-minute checks and a first-half-hour projection (candidate at breakfast)", "delay: minutes; the sample is taken before the crest", "tech", None),
            ("Bakul: manager phones Hafizpet", "delay: call, cooking and a 20 to 40 minute drive; lead time unknown", "users", "late in the window the delay outruns the close, so a reserve of about 50 is held at 9:20 (candidate)")]
    for r, (title, delay, key, note) in enumerate(rows):
        y = 100 + r * 230
        c.add(f'<text x="30" y="{y}" font-size="14.5" font-weight="800" fill="{C[key][0]}">{esc(title)}</text>')
        a = c.node(30, y + 20, 330, 76, "Food left at the counter", None, key, None, False, fs=14)
        b = c.node(435, y + 20, 330, 76, "Risk of running out at the check", None, key, None, False, fs=14)
        d = c.node(840, y + 20, 330, 76, "Top-up cooked and served", None, key, None, False, fs=14)
        c.edge(a, b, G, None, width=3, sign="-"); c.edge(b, d, G, None, width=3, sign="+")
        c.edge((1005, y + 98), (195, y + 98), G, None, width=3, bend=-0.07, sign="+", t=0.5)
        c.pill(600, y + 150, delay, "amber", fs=11.5)
        if note: c.pill(600, y + 184, note, "red", fs=11.5, dashed=True)
    c.render("s07b-l12.png")

# ---------------------------------------------------------------- L4
def l4():
    c = Canvas(1200, 560, "L4: menu rotation governance response (balancing, confirmed)", "A loud complaint with a route closes the loop end to end")
    nodes = [("Menu fatigue", "one fixed menu for the semester", "red", False), ("Intensity of feedback", "posters, notifications, complaints", "tech", False),
             ("Escalation", "Student Council, Student Parliament, CDS Committee approves", "soc", False), ("Menu variety", "biweekly rotation, weeks 1 and 3 repeat, 2 and 4 repeat", "green", False)]
    ns = [c.node(60 + i * 285, 110 + (60 if i in (1, 2) else 0), 250, 90, t, s, k, None, d, fs=14, sfs=11.5) for i, (t, s, k, d) in enumerate(nodes)]
    for i, s in enumerate(["+", "+", "+"]): c.edge(ns[i], ns[i + 1], G, None, width=3, sign=s)
    c.edge((905, 190), (185, 200), G, None, width=3, bend=-0.17, sign="-")
    c.badge(530, 370, "B", G, r=26, fs=20)
    c.pill(530, 330, "delay: semester to policy cycle", "amber", fs=11.5)
    c.node(60, 430, 540, 90, "Live test at Kadamba", "dinner sambar dropped; a student complained 'while they are taking more money from us' (single-sourced); not reversed so far", "amber", None, True, fs=14, sfs=11.5)
    c.node(640, 430, 520, 90, "What it proves", "the escalation route can close a loop. It has never been used for the booking: a different process with a different owner", "slate", None, False, fs=14, sfs=11.5)
    c.render("s07b-l4.png")

# ---------------------------------------------------------------- L17
def l17():
    c = Canvas(1200, 720, "L17: kitchen competence shifts the burden (candidate)", "A working symptomatic fix removes the pressure for the fundamental one; the dashed link is assumed")
    g = c.node(500, 260, 300, 84, "Visible consequences of the gap", "queues, run-outs, surplus", "red", None, False, fs=14, sfs=11.5)
    k = c.node(60, 110, 300, 84, "Kitchen correction (L11, L12)", "discount, top-up, reuse, outsiders and staff, bin", "biz", None, False, fs=14, sfs=11.5)
    p = c.node(60, 480, 300, 84, "Pressure on the rule owner", "no signal accumulates upstream", "soc", None, True, fs=14, sfs=11.5)
    f = c.node(900, 480, 260, 84, "Change to the booking rule", "default, exit, cost", "tech", None, False, fs=14, sfs=11.5)
    c.edge(g, k, G, None, width=3, bend=0.18, sign="+"); c.edge(k, g, G, None, width=3, bend=0.18, sign="-")
    c.edge(g, p, G, None, width=3, sign="+"); c.edge(p, f, G, None, width=3, sign="+")
    c.edge(f, g, G, None, width=3, sign="-", bend=0.1)
    c.edge((210, 196), (210, 478), RED, None, width=3, dash="7 5", sign="-")
    c.pill(300, 345, "assumed link: relief lowers pressure", "red", fs=11.5, dashed=True)
    c.pill(190, 82, "symptomatic fix: works every morning", "green", fs=12)
    c.pill(1030, 600, "fundamental fix: slow and unrouted", "amber", fs=12)
    c.node(560, 90, 600, 100, "Why the shift is partly benign", "outsiders and half of Kadamba's staff eat the surplus; an operator that is paid for the count has no reason to raise a signal; Bakul's floor turns a visible shortage into a silent surplus", "green", None, False, fs=14, sfs=11.5)
    c.render("s07b-l17.png")

# ---------------------------------------------------------------- L13
def l13():
    c = Canvas(1240, 600, "L13: standing booking to fixed-ratio over-preparation (chain, does not close)", "The core chain of the paradox; no link runs back to the booking")
    d = [("Automatic registration", "five cancellations, four days ahead", "tech"), ("Flat booking count", "about 1,070 a day at Kadamba, Sunday included", "tech"), ("Fixed first batch", "70% Kadamba; 70 to 80% Bakul, floor 70%", "biz"), ("First-batch surplus", "worst on low-turnout days and the veg line", "red")]
    ns = [c.node(30 + i * 315, 110, 255, 92, t, s, k, None, False, fs=14, sfs=11.5) for i, (t, s, k) in enumerate(d)]
    for i in range(3): c.edge(ns[i], ns[i + 1], G, None, width=3, sign="+")
    c.pill(1100, 290, "absorbed: reuse, outsiders and staff, bin (L9)", "green", fs=11.5)
    h = c.node(975, 320, 255, 92, "Food held, reheated, moved between vessels", "Kadamba, team's judgement (candidate)", "amber", None, False, fs=13.5, sfs=11)
    q = c.node(665, 440, 255, 92, "Food quality falls", "Bakul: held hot, parathas soften", "amber", None, True, fs=14, sfs=11.5)
    t = c.node(350, 440, 255, 92, "Fewer students eat", "not evidenced for either hall", "ext", None, True, fs=14, sfs=11.5)
    c.edge(ns[3], h, G, None, width=3, sign="+", a_pt=(1102, 205), b_pt=(1102, 318))
    c.edge(h, q, G, None, width=3, sign="-"); c.edge(q, t, RED, None, width=3, dash="7 5", sign="+")
    c.edge(t, ns[3], RED, None, width=3, dash="7 5", sign="-", a_pt=(500, 438), b_pt=(1000, 205), bend=0.0)
    c.node(30, 330, 280, 100, "No link back", "nothing runs from surplus to the booking, the rule or the ratio", "red", "ic-link-broken", True, fs=14, sfs=11.5)
    c.render("s07b-l13.png")

# ---------------------------------------------------------------- L14
def l14():
    c = Canvas(1240, 520, "L14: closing rush to just-in-case over-preparation", "Shortage is loud and has a route; surplus is silent and has none, so the ratio can ratchet upward")
    n = [("Crest at close", "26.5% of Kadamba scans, 9:15 to 9:30", "tech"), ("Run-out risk at close", "queues, complaints, back door", "red"), ("Bigger batch or held reserve", "hedge against a late top-up", "biz"), ("Surplus", "absorbed quietly (L9)", "green")]
    ns = [c.node(30 + i * 315, 190, 255, 92, t, s, k, None, False, fs=14, sfs=11.5) for i, (t, s, k) in enumerate(n)]
    c.edge(ns[0], ns[1], G, None, width=3, sign="+")
    c.edge(ns[1], ns[2], G, None, width=3, bend=0.25, sign="+")
    c.edge(ns[2], ns[1], G, None, width=3, bend=0.25, sign="-")
    c.edge(ns[2], ns[3], G, None, width=3, sign="+")
    c.edge(ns[3], ns[2], RED, None, width=3, dash="7 5", bend=0.3, sign="-")
    c.pill(500, 110, "short loop balances: loud and fast", "green", fs=11.5)
    c.pill(840, 110, "candidate: this link never fires", "red", fs=11.5, dashed=True)
    c.node(30, 380, 1170, 90, "Delay that makes the hedge rational", "a 10 to 15 minute top-up against a crest in the last 10 to 15 minutes; off site, a call, cooking and a 20 to 40 minute drive. No change of ratio in either direction is on record, so the ratchet is an asymmetry of intent, not an observed drift", "amber", None, False, fs=14, sfs=12)
    c.render("s07b-l14.png")

# ---------------------------------------------------------------- L2
def l2():
    c = Canvas(1200, 520, "L2: Skip Meal, a designed mechanism that does not close", "Confirmed near zero use; the kitchen link is in open conflict")
    d = [("Student knows they will not attend", None, "users", False), ("Uses Skip Meal", "near zero: four of six never have", "red", False), ("Declaration reaches kitchen planning?", "in conflict", "amber", True), ("Count the kitchen cooks from falls", None, "biz", True), ("Less surplus", None, "green", True)]
    ns = [c.node(15 + i * 238, 120, 215, 100, t, s, k, None, dd, fs=13.5, sfs=11.5) for i, (t, s, k, dd) in enumerate(d)]
    for i in range(4):
        c.edge(ns[i], ns[i + 1], G if i < 1 else AMB, None, width=3, dash=None if i < 1 else "7 5", sign="+" if i < 1 else None)
    c.node(15, 280, 455, 100, "Why use is near zero", "Skip Meal tells the kitchen but the charge stands: 'it doesn't return the money'", "red", None, False, fs=14, sfs=12)
    c.node(500, 280, 330, 100, "Earlier finding", "declarations reach the kitchen for same-week preparation", "slate", None, True, fs=14, sfs=12)
    c.node(860, 280, 325, 100, "Kadamba operator", "cooks 'based only on the number of registrations' (single-sourced)", "slate", None, True, fs=14, sfs=12)
    c.node(15, 410, 1170, 76, "No link back", "nothing connects the resulting waste to whether a student uses Skip Meal next time, so no self-correcting dynamic exists", "red", "ic-link-broken", True, fs=14, sfs=12)
    c.render("s07b-l2.png")

if __name__ == "__main__":
    for f in (dashboard, l11, l12, l4, l17, l13, l14, l2): f()
