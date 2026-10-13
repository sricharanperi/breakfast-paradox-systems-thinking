import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def box(c, x, y, w, h, text, fill, stroke, fs=12, bold=False, color="#1b1b1b", anchor="start", rx=7):
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>')
    pad = 7
    lines = wrap(text, w - 2 * pad, fs, bold)
    yy = y + (h - len(lines) * fs * 1.22) / 2 + fs * 0.92
    tx = x + pad if anchor == "start" else x + w / 2
    for ln in lines:
        c.add(f'<text x="{tx}" y="{yy:.1f}" font-size="{fs}" font-weight="{700 if bold else 400}" fill="{color}" text-anchor="{anchor}">{esc(ln)}</text>')
        yy += fs * 1.22

# ---------------------------------------------------------------- 1 concepts x levers
def concepts_levers():
    c = Canvas(1250, 640, "Eight concepts, mapped to the twelve leverage points", "Dots mark the leverage points each concept pulls; G is the foil and pulls none")
    lps = ["LP1", "LP2", "LP3", "LP4", "LP5", "LP6", "LP7", "LP8", "LP9", "LP10", "LP11", "LP12"]
    place = ["6", "5", "3/8", "4", "6/8", "6/10", "8", "6", "5", "5", "2", "3"]
    rows = [("A  Breakfast Ledger", ["LP1", "LP7", "LP9"], "Fundamental: route", "biz"),
            ("B  Kitchen Learning Kit", ["LP3", "LP4", "LP5"], "Quick fix", "amber"),
            ("C  Crest Plan", ["LP6"], "Quick fix", "amber"),
            ("D  Sunday Exit", ["LP2"], "Fundamental: default and exit", "biz"),
            ("E  Operator Menu Slot", ["LP8"], "Fundamental: route", "biz"),
            ("F  Billed at Consumption", ["LP10"], "Fundamental, held", "ext"),
            ("G  Ratio Cut to 50%", [], "Foil (a place 12 parameter)", "red"),
            ("H  The Shared Reading", ["LP11", "LP12"], "Fundamental: goal and belief", "soc")]
    x0, y0, cw, rh, lw = 250, 120, 52, 52, 250
    for j, (lp, pl) in enumerate(zip(lps, place)):
        c.add(f'<text x="{x0+j*cw+cw/2}" y="{y0-26}" font-size="13" font-weight="800" fill="#0d47a1" text-anchor="middle">{lp}</text><text x="{x0+j*cw+cw/2}" y="{y0-9}" font-size="11" fill="#666" text-anchor="middle">place {pl}</text>')
    for i, (name, ls, role, k) in enumerate(rows):
        y = y0 + i * rh
        s, f = C[k]
        c.add(f'<rect x="14" y="{y}" width="{lw+len(lps)*cw+10}" height="{rh-6}" rx="8" fill="{f}" fill-opacity="0.55"/>')
        c.add(f'<text x="24" y="{y+rh/2+1}" font-size="14" font-weight="700" fill="#1b1b1b">{esc(name)}</text>')
        for j, lp in enumerate(lps):
            if lp in ls:
                cx = x0 + j * cw + cw / 2
                held = (name.startswith("A") and lp == "LP9") or (name.startswith("F"))
                fl = "white" if held else s
                da = 'stroke-dasharray="3 3"' if held else ""
                c.add(f'<circle cx="{cx}" cy="{y+rh/2-3}" r="12" fill="{fl}" stroke="{s}" stroke-width="3" {da}/>')
        c.add(f'<text x="{x0+len(lps)*cw+16}" y="{y+rh/2+1}" font-size="12.5" font-weight="700" fill="{s}">{esc(role)}</text>')
    c.add(f'<text x="24" y="{y0+8*rh+28}" font-size="12.5" fill="#444">Dashed rings: levers held or taken up later (LP9 in A; LP10 in F, held until each operator\'s payment basis is known).</text>')
    c.render("a10-concepts-levers.png")

# ---------------------------------------------------------------- 2 plan card and 9:00 rule
def plan_card():
    c = Canvas(1250, 700, "Prototype B and C in one morning: Kadamba veg line, Sunday 19 April 2026", "Day-before plan card, then the 9:00 rule. Eaters and shares are records (confirmed); the cooked amounts are projected")
    c.add('<text x="30" y="110" font-size="16" font-weight="800" fill="#00695c">Saturday evening: the plan card</text>')
    steps = [("Expected eaters", "mean of the same weekday in earlier weeks (5 and 12 April: 168 and 159)", "164", "biz"),
             ("x share in by 9:15", "earlier Sundays, both lines pooled", "54.7%", "biz"),
             ("x cover", "so the late batch has margin", "1.5", "biz"),
             ("= first batch", "per the gram standard: four idlis from 120 g batter, 100 g sambar", "134", "green")]
    x = 30
    for i, (t, s, v, k) in enumerate(steps):
        c.node(x, 130, 270, 110, t, s, k, None, False, fs=14, sfs=11.5)
        c.add(f'<text x="{x+240}" y="{130+30}" font-size="22" font-weight="800" fill="{C[k][0]}" text-anchor="end">{v}</text>')
        x += 300
    c.node(30, 262, 570, 62, "Added by name, whatever the batch", "about 30 portions for outside diners (single-sourced) and a staff allowance (assumed); a float for bonda, puri, vada, idli; raw reserve kept", "amber", None, False, fs=13.5, sfs=11.5)
    c.add('<text x="30" y="370" font-size="16" font-weight="800" fill="#1565c0">9:00 on the day: the late batch</text>')
    st2 = [("62 veg diners so far", "scans by 9:00", "tech"), ("/ 39.4% usual share by 9:00", "the two earlier Sundays", "tech"), ("+ 10% = about 173", "day's projected total (157 before the margin)", "tech"), ("- first batch 134 = 39", "late batch, landing by about 9:15", "green")]
    x = 30
    for t, s, k in st2:
        c.node(x, 390, 270, 90, t, s, k, None, False, fs=14, sfs=11.5); x += 300
    # bars
    c.add('<text x="30" y="530" font-size="15" font-weight="800" fill="#333">Portions cooked against the 179 who ate (projected)</text>')
    for i, (lab, v, col) in enumerate([("Baseline: 70% of 817 registered", 572, "#c62828"), ("Refined: first batch plus late batch", 173, "#1565c0"), ("Eaten (scans, confirmed)", 179, "#2e7d32")]):
        y = 548 + i * 40
        c.add(f'<text x="30" y="{y+20}" font-size="13" fill="#222">{lab}</text><rect x="330" y="{y}" width="{v/572*700:.0f}" height="28" rx="4" fill="{col}"/><text x="{330+v/572*700+8:.0f}" y="{y+20}" font-size="13" font-weight="700" fill="#222">{v}</text>')
    c.add('<text x="30" y="690" font-size="12.5" fill="#444">The refined plan leaves 6 diners to the ordinary top-up. At Bakul the prototype is a per-item sheet only.</text>')
    c.render("a10-plan-card.png")

# ---------------------------------------------------------------- 3 gates and scores heat table
def gates_scores():
    c = Canvas(1250, 760, "Concepts scored against the system objectives", "Four gates first, then nine weighted criteria scored 0 to 4 (total out of 400); gate failure makes a concept ineligible whatever its score")
    cols = ["Gates", "O1", "O2", "O3", "O4", "O5", "O6", "O9", "O7", "O8", "Score"]
    sub = ["", "booked/\neaten", "cooked/\neaten", "crest", "capab.", "fair", "quality", "desir.", "feasible", "revers.", ""]
    wts = ["", "15", "15", "15", "15", "10", "10", "10", "5", "5", ""]
    data = [("A: Breakfast Ledger", "Pass", [2, 2, 4, 4, 2, 1, 2, 4, 4], 68),
            ("H: Shared Reading", "Pass", [2, 2, 4, 3, 3, 1, 2, 3, 4], 65),
            ("F: Billed at consumption", "Fails G3 (held)", [4, 2, 4, 2, 3, 1, 2, 0, 2], 63),
            ("C: Crest Plan, alone", "Fails G4 alone", [1, 2, 4, 1, 3, 3, 3, 4, 4], 63),
            ("D: Sunday skip, ratio kept", "Pass", [2, 2, 4, 2, 3, 1, 3, 1, 3], 60),
            ("E: Operator Menu Slot", "Pass", [1, 2, 4, 2, 2, 2, 3, 3, 4], 60),
            ("B: Kitchen Kit, alone", "Fails G4 alone", [1, 4, 1, 3, 2, 3, 1, 3, 4], 58),
            ("D: every-day skip", "Pass", [3, 2, 1, 2, 3, 1, 3, 0, 2], 50),
            ("D: Sunday opt-in (first draft)", "Pass", [3, 3, 0, 2, 2, 2, 2, 1, 3], 50),
            ("G: Ratio cut to 50%", "Fails G1, P4", [1, 3, 3, 1, 1, 1, 1, 4, 4], 48),
            ("First-draft bundle", "Fails G4", [2, 4, 3, 4, 3, 3, 3, 3, 3], 79),
            ("Re-sequenced bundle", "Pass", [2, 4, 3, 4, 3, 3, 3, 3, 3], 79)]
    x0, y0 = 300, 130
    gw, cw, sw, rh = 150, 62, 130, 40
    xs = [x0] + [x0 + gw + i * cw for i in range(9)] + [x0 + gw + 9 * cw]
    for i, t in enumerate(cols):
        x = x0 if i == 0 else (x0 + gw + (i - 1) * cw if i < 10 else x0 + gw + 9 * cw)
        w = gw if i == 0 else (cw if i < 10 else sw)
        c.add(f'<text x="{x+w/2}" y="{y0-34}" font-size="13" font-weight="800" fill="#0d47a1" text-anchor="middle">{cols[i]}</text>')
        if wts[i]: c.add(f'<text x="{x+w/2}" y="{y0-18}" font-size="11" fill="#666" text-anchor="middle">weight {wts[i]}</text>')
        if sub[i]:
            for k_, ln in enumerate(sub[i].split("\n")): c.add(f'<text x="{x+w/2}" y="{y0-3+k_*0}" font-size="0" fill="none">{ln}</text>')
    heat = {0: "#fdecea", 1: "#fff3e0", 2: "#fffde7", 3: "#e8f5e9", 4: "#a5d6a7"}
    for r, (nm, g, sc, tot) in enumerate(data):
        y = y0 + r * rh + (14 if r >= 10 else 0)
        bundle = r >= 10
        c.add(f'<text x="14" y="{y+rh/2+4}" font-size="13.5" font-weight="{800 if bundle else 600}" fill="#1b1b1b">{esc(nm)}</text>')
        gk = "#2e7d32" if g == "Pass" else "#c62828"
        box(c, x0, y + 3, gw - 6, rh - 8, g, "#e8f5e9" if g == "Pass" else "#fdecea", gk, fs=12, bold=True, color=gk, anchor="middle")
        for i, v in enumerate(sc):
            x = x0 + gw + i * cw
            box(c, x + 2, y + 3, cw - 4, rh - 8, str(v), heat[v], "#cfd8dc", fs=14, bold=True, anchor="middle")
        x = x0 + gw + 9 * cw + 8
        c.add(f'<rect x="{x}" y="{y+8}" width="{tot/80*(sw-50):.0f}" height="{rh-18}" rx="4" fill="{"#1565c0" if g=="Pass" else "#90a4ae"}"/><text x="{x+tot/80*(sw-50)+6:.0f}" y="{y+rh/2+4}" font-size="13" font-weight="800" fill="#222">{tot}%</text>')
    c.text(14, y0+12*rh+40, "O1 booked against eaten, O2 cooked against eaten, O3 crest service every hall, O4 fundamental capability, O5 fairness, O6 food quality, O9 desirability, O7 feasibility now, O8 reversibility. Scores are model results (projected); weights are the team's judgement.", 12.5, False, "#444", width=1200)
    c.render("a10-gates-scores.png")

# ---------------------------------------------------------------- 4 simulated responses
def responses():
    c = Canvas(1250, 870, "Simulated responses of twelve stakeholders to four concepts", "Reasoned from each actor's stated position and incentives (simulated); not actor feedback")
    cols = ["A: Ledger", "B with C: Kitchen kit and crest plan", "D: Sunday exit", "H: Shared reading"]
    G, A, R, N = ("#e8f5e9", "#2e7d32"), ("#fff8e1", "#e08600"), ("#fdecea", "#c62828"), ("#f2f2f2", "#9e9e9e")
    rows = [("Near-daily eaters", [("Indifferent", N), ("Fresher food; object to any run-out", A), ("Barely affected", N), ("Indifferent", N)]),
            ("Sunday or frequent skippers", [("Indifferent", N), ("Unaffected", N), ("Strong uptake if simple and free", G), ("Indifferent", N)]),
            ("Mess Cell resellers", [("Indifferent", N), ("Unaffected", N), ("Some shift to skipping", A), ("Indifferent", N)]),
            ("Prism, Kadamba management", [("Wary of audit; accepts if blame-free", A), ("Receptive: a food-cost saving", G), ("Opposed if paid on registered plates; neutral if served", R), ("Engages if its figures lead", A)]),
            ("Kadamba supervisor and staff", [("Fears reprimand", A), ("Fears run-outs; accepts with reserve and named staff meal", A), ("Unaffected", N), ("Curious, if a wrong guess costs nothing", A)]),
            ("Bakul operator", [("Accepts a check; may lack records", A), ("Bakul form only; resists any run-out risk", R), ("Likely neutral or favourable if paid on served plates (candidate)", A), ("Engages once a record exists", A)]),
            ("Yuktāhār (ABC)", [("Welcomes if paper-based", G), ("Willing host; adopts the 9:00 rule", G), ("Welcomes a truer count", G), ("Uncomfortable, then anchors on its register", A)]),
            ("CDS", [("Accepts a light export", G), ("Supportive", G), ("Cautious about workload", A), ("Receptive if no new work", A)]),
            ("CFS", [("Receptive to a threshold", G), ("Neutral to positive", G), ("Supportive if a no-cost pilot", G), ("Receptive: its own goal", G)]),
            ("Student representatives", [("Use as evidence", G), ("Neutral", N), ("Natural carriers", G), ("Carry the tested view", G)]),
            ("Outside diners and staff", [("Unaffected", N), ("Harmed only if the allowance is unnamed", R), ("Unaffected", N), ("Unaffected", N)]),
            ("Facility team at the tasting", [("One line if no delay", A), ("Unaffected", N), ("Unaffected", N), ("Neutral", N)])]
    x0, y0, lw, cw, rh = 250, 110, 235, 238, 50
    for j, t in enumerate(cols):
        c.add(f'<text x="{x0+lw-235+235+j*cw+cw/2-235}" y="{y0-12}" font-size="13" font-weight="800" fill="#0d47a1" text-anchor="middle">{esc(t)}</text>')
    for i, (nm, cs) in enumerate(rows):
        y = y0 + i * rh
        c.add(f'<text x="14" y="{y+rh/2+2}" font-size="13" font-weight="700" fill="#1b1b1b">{esc(nm)}</text>')
        for j, (t, (f, s)) in enumerate(cs):
            box(c, x0 + j * cw - 0 + 0, y, cw - 6, rh - 6, t, f, s, fs=11.5)
    c.legend(14, y0 + 12 * rh + 10, [("#2e7d32", "welcomes or supports"), ("#e08600", "conditional or wary"), ("#c62828", "opposed or harmed"), ("#9e9e9e", "indifferent or unaffected")], fs=11.5)
    c.render("a10-responses.png")

# ---------------------------------------------------------------- 5 hedge ratchet loop
def hedge_loop():
    c = Canvas(1100, 780, "Unintended consequence: the hedge ratchet", "One loud shortage pushes the first batch back up (a balancing loop that undoes the cut)")
    cx, cy, r = 550, 380, 235
    labs = [("First-batch size", "after the cut", "biz"), ("Run-outs at the crest", "diners short after 9:15", "red"), ("One loud complaint", "a run-out is visible; a surplus is silent", "amber"), ("Pressure to restore the hedge", "from supervisor and manager", "soc")]
    ns = []
    for i, (t, s, k) in enumerate(labs):
        a = -math.pi / 2 + i * math.pi / 2
        x, y = cx + r * 1.15 * math.cos(a), cy + r * 0.78 * math.sin(a)
        ns.append(c.node(x - 125, y - 42, 250, 84, t, s, k, None, False, fs=15, sfs=12))
    signs = ["-", "+", "+", "+"]
    for i in range(4):
        c.edge(ns[i], ns[(i + 1) % 4], "#37474f", None, width=3.2, bend=0.18, sign=signs[i])
    c.badge(cx, cy, "B", "#37474f", r=28, fs=22)
    c.text(cx, cy + 52, "The batch returns to its old size", 13, True, "#37474f", "middle")
    c.node(30, 660, 1040, 90, "What holds it down", "judge results over months, not days; record every run-out; keep the 9:00 late batch and the raw reserve; read the share after 9:30 weekly (grace period withdrawn after four weeks above 9.2%)", "green", "ic-shield", False, fs=15, sfs=12.5)
    c.render("a10-hedge-loop.png")

# ---------------------------------------------------------------- 6 sequence with decision points and handover
def sequence():
    c = Canvas(1250, 780, "The recommended sequence, with decision points and handover", "Weeks 0 to 20; the fundamental fix runs on fixed dates whatever the kitchen pilot shows")
    x0, x1 = 190, 1130
    wx = lambda w: x0 + w / 20 * (x1 - x0)
    for w in range(0, 21, 2):
        c.add(f'<line x1="{wx(w)}" y1="100" x2="{wx(w)}" y2="650" stroke="#e3e8ee"/><text x="{wx(w)}" y="94" font-size="12" fill="#555" text-anchor="middle">{w}</text>')
    c.add(f'<text x="{x0}" y="78" font-size="12.5" fill="#555">week</text>')
    for a, b, lab, col in [(0, 4, "Stage 1", "#2e7d32"), (4, 9, "Stage 2", "#1565c0"), (9, 20, "Stage 3", "#6a1b9a")]:
        c.add(f'<rect x="{wx(a)+2}" y="104" width="{wx(b)-wx(a)-4}" height="24" rx="6" fill="{col}"/><text x="{(wx(a)+wx(b))/2}" y="121" font-size="13" font-weight="800" fill="white" text-anchor="middle">{lab}</text>')
    lanes = [("Fundamental fix", 150, "biz", [(0, 4, "Ledger with charge line; co-design tests; goal and indicators to CFS and CDS"), (4, 6, "Joint reading wk 4"), (6, 10, "Sunday skip proposed wk 6, in force wk 10"), (10, 20, "Every-day skip if DP2 passes at wk 14; forum on a cycle; menu notes")]),
             ("Quick fix (Kadamba, Yuktāhār)", 300, "amber", [(0, 4, "Cards and sheet drafted with the supervisor"), (5, 10, "Sunday veg pilot: card, allowance, 9:00 batch, daily sheet"), (10, 20, "Every day, both lines; Yuktāhār re-anchors")]),
             ("Handover", 450, "slate", [(14, 20, "Wk 14 decision; wk 16 CDS compiles with the team; wk 18 CDS alone; wk 20 the team steps back")]),
             ("Held until facts known", 560, "red", [(0, 20, "Billing and payment basis (LP10); a named owner of booked, cooked and eaten (LP9); Bakul only once it has its own records")])]
    for nm, y, k, items in lanes:
        s, f = C[k]
        h = 136 if nm in ("Fundamental fix", "Quick fix (Kadamba, Yuktāhār)") else (96 if nm == "Handover" else 80)
        c.add(f'<rect x="14" y="{y}" width="1222" height="{h}" rx="10" fill="{f}" fill-opacity="0.5" stroke="{s}" stroke-width="1.2"/><text x="24" y="{y+22}" font-size="13.5" font-weight="800" fill="{s}">{esc(nm)}</text>')
        for i, (a, b, t) in enumerate(items):
            yy = y + 30 + (i % 2) * 52 if nm in ("Fundamental fix", "Quick fix (Kadamba, Yuktāhār)") else y + 30
            hh = 46 if nm != "Held until facts known" else 36
            box(c, wx(a) + 2, yy, max(wx(b) - wx(a) - 4, 70), hh, t, "white", s, fs=11, rx=6)
    for w, t in [(4, "joint reading"), (6, "DP1 Sunday skip"), (10, "skip in force"), (14, "DP2 every-day skip"), (20, "team steps back")]:
        c.add(f'<polygon points="{wx(w)},664 {wx(w)-8},682 {wx(w)+8},682" fill="#c62828"/><text x="{wx(w)}" y="700" font-size="12" font-weight="800" fill="#c62828" text-anchor="middle">{t}</text>')
    c.add('<text x="24" y="740" font-size="12.5" fill="#444">DP3 (default matched to intent) follows a term of DP2; DP4 (billing and payment basis) waits for the plate basis, operator by operator.</text>')
    c.render("a10-sequence.png")

# ---------------------------------------------------------------- 7 theory of change
def theory():
    c = Canvas(1250, 760, "Theory of change: from root cause to expected response", "Expected responses are projected or candidate, never observed")
    rows = [("Gap measured but unrouted (L10; L4 fires on loudness)", "Ledger, charge line, threshold", "Cost becomes a trigger beside complaint (candidate)"),
            ("A count is sought while minimising wastage is the stated goal", "Goal carried with two indicators", "Indicators cited in a decision (untested)"),
            ("Beliefs holding the count, ratio and default", "Shared readings", "Anchors move toward records (candidate)"),
            ("Fixed ratio, no learning record at Kadamba (L13; L11 absent)", "Plan card and daily sheet create L11", "Surplus 254 to 471 down to 69 to 120 a day (projected)"),
            ("Top-ups blind to the crest (L12, L14)", "9:00 late batch", "0.5 to 7.7 short; 9 to 13 on heavy days (projected)"),
            ("Count treated as a paid obligation (L8, L17)", "Operator forum and a food-cost case", "Kadamba's own reason to cut (candidate)"),
            ("Default with a narrow exit (L13, L2, L1)", "Sunday skip, then every-day on its own rule", "Rs 4,000 to 30,000 a week on Sundays; Rs 62,000 to 1.23 lakh a week every day (projected)"),
            ("Billing at the booking (L1, L6, L8)", "Held; the ledger builds the case", "Decided once the plate basis is known")]
    cols = [("Root cause", 30, 400, "soc"), ("Bundle change", 480, 300, "biz"), ("Expected response", 830, 390, "green")]
    for t, x, w, k in cols:
        c.add(f'<text x="{x}" y="100" font-size="15" font-weight="800" fill="{C[k][0]}">{t}</text>')
    for i, r in enumerate(rows):
        y = 116 + i * 74
        ns = [c.node(x, y, w, 62, t, None, k, None, False, fs=12.5) for (x, w, k), t in zip([(30, 400, "soc"), (480, 300, "biz"), (830, 390, "green")], r)]
        c.edge(ns[0], ns[1], "#37474f", None, width=2.4); c.edge(ns[1], ns[2], "#37474f", None, width=2.4)
    c.render("a10-theory-of-change.png")

if __name__ == "__main__":
    concepts_levers(); plan_card(); gates_scores(); responses(); hedge_loop(); sequence(); theory()
