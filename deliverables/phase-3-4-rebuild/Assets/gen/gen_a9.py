import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def box(c, x, y, w, h, text, key, dashed=False, fs=12.5, bold=False, fill=None, tcolor="#1b1b1b"):
    s, f = C[key]
    da = 'stroke-dasharray="5 4"' if dashed else ""
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill or f}" fill-opacity="0.85" stroke="{s}" stroke-width="1.8" {da}/>')
    lines = wrap(text, w - 14, fs, bold)
    yy = y + (h - len(lines) * fs * 1.25) / 2 + fs * 0.95
    for ln in lines:
        c.add(f'<text x="{x+8}" y="{yy:.1f}" font-size="{fs}" font-weight="{700 if bold else 400}" fill="{tcolor}">{esc(ln)}</text>'); yy += fs * 1.25

# ---------------------------------------------------------------- depth ladder
def ladder():
    c = Canvas(1200, 800, "The twelve places to intervene, and where the levers sit", "Place 1 is the deepest, place 12 the shallowest; dashed chips are held levers; each lever appears once per part it acts on")
    names = ["Transcend paradigms", "Mindset or paradigm", "Goals of the system", "Power to self-organise", "Rules of the system", "Information flows", "Gain of reinforcing loops", "Strength of balancing loops", "Length of delays", "Stocks and flows structure", "Buffer sizes", "Parameters and numbers"]
    chips = {2: [("LP11", "soc", 0)], 3: [("LP12", "soc", 0), ("LP3 goal", "biz", 0)], 4: [("LP4", "biz", 0)],
             5: [("LP2", "users", 0), ("LP9", "soc", 1), ("LP10", "soc", 1), ("LP7 rule", "tech", 0), ("LP8 slot", "tech", 0)],
             6: [("LP1", "red", 0), ("LP5", "biz", 0), ("LP6", "biz", 0), ("LP8", "tech", 0)],
             8: [("LP3 target", "biz", 0), ("LP5", "biz", 0), ("LP7", "tech", 0)], 10: [("LP6 late batch", "biz", 0)]}
    notes = {1: "no lever", 7: "no lever", 9: "not claimed: flattening the crest is not attempted", 11: "allowances inside LP5 and LP6 only", 12: "settings inside a deeper lever only"}
    y0 = 90; rh = 54
    for i, nm in enumerate(names):
        p = i + 1; y = y0 + i * rh
        shade = ["#3949ab", "#5c6bc0", "#7986cb", "#9fa8da", "#b0bec5", "#cfd8dc"][min(i // 2, 5)]
        tc = "white" if i < 4 else "#1b1b1b"
        c.add(f'<rect x="30" y="{y}" width="330" height="{rh-6}" rx="9" fill="{shade}"/>')
        c.add(f'<text x="48" y="{y+rh/2+2}" font-size="17" font-weight="800" fill="{tc}">{p}</text><text x="86" y="{y+rh/2+2}" font-size="14" font-weight="700" fill="{tc}">{esc(nm)}</text>')
        c.add(f'<rect x="372" y="{y}" width="800" height="{rh-6}" rx="9" fill="#fafbfd" stroke="#e0e6ec"/>')
        x = 386
        for t, k, held in chips.get(p, []):
            w = tw(t, 13, True) + 24
            s, f = C[k]
            da = 'stroke-dasharray="4 3"' if held else ""
            c.add(f'<rect x="{x}" y="{y+8}" width="{w:.0f}" height="{rh-22}" rx="14" fill="{"white" if held else f}" stroke="{s}" stroke-width="2" {da}/><text x="{x+w/2:.0f}" y="{y+rh/2+2}" font-size="13" font-weight="700" fill="{s}" text-anchor="middle">{esc(t)}</text>')
            x += w + 10
        if p in notes:
            c.add(f'<text x="{x+6}" y="{y+rh/2+2}" font-size="12.5" fill="#777" font-style="italic">{esc(notes[p])}</text>')
    c.render("a9-depth-ladder.png")

# ---------------------------------------------------------------- archetype
def archetype():
    c = Canvas(1200, 700, "Shifting the burden: the structure that orders the levers", "Candidate reading; the link from kitchen competence to less pressure upstream is assumed")
    sy = c.node(60, 270, 280, 110, "The symptom", "booked far above eaten; run-outs at the crest; a charge for uneaten food", "red", "ic-warning", fs=16, sfs=12.5)
    qf = c.node(440, 90, 330, 130, "Quick fix: kitchen and resale", "L11 learning, L12 top-up, L9 absorbers, L1 resale; levers LP5 and LP6. Works within minutes to weeks", "green", "ic-pot", fs=15, sfs=12.5)
    ff = c.node(440, 440, 330, 150, "Fundamental fix: route, default, goal", "L10 route, L13 upward link, L2 Skip Meal, L6 reverted; levers LP1, LP2, LP12, LP10. Slow, and each attempt has withered", "soc", "ic-gear", fs=15, sfs=12.5)
    se = c.node(850, 270, 300, 120, "Side effect (L17, candidate)", "a better-run kitchen reduces the pressure on the people who could fix the cause", "amber", "ic-eye", True, fs=15, sfs=12.5)
    c.edge(sy, qf, "#37474f", None, width=3.2, bend=0.12, sign="+", a_pt=(240, 268), b_pt=(438, 150))
    c.edge(qf, sy, C["green"][0], None, width=3.2, bend=0.12, sign="-", a_pt=(438, 195), b_pt=(335, 272))
    c.edge(sy, ff, "#37474f", None, width=3.2, bend=-0.12, sign="+", a_pt=(130, 382), b_pt=(438, 520))
    c.edge(ff, sy, C["soc"][0], None, width=3.2, bend=0.1, sign="-", dash="8 5", a_pt=(520, 438), b_pt=(300, 382))
    c.edge(qf, se, C["amber"][0], None, width=2.6, dash="7 5", bend=0.1, sign="+")
    c.edge(se, ff, C["amber"][0], None, width=2.6, dash="7 5", bend=0.12, sign="-")
    c.pill(150, 200, "short delay", "green", fs=12); c.pill(120, 470, "long delay", "soc", fs=12)
    c.text(830, 470, "The recommendation names the quick fix as a quick fix, and runs the fundamental fix on fixed dates, whatever the kitchen results show.", 13.5, False, "#444", width=330)
    c.legend(60, 620, [("#37474f", "link, + moves together, - moves opposite", "line"), (C["amber"][0], "assumed link", "dash")], fs=11.5)
    c.render("a9-archetype.png")

# ---------------------------------------------------------------- comparison
def compare():
    c = Canvas(1200, 560, "The natural comparison: three halls, three planning rules", "Same registration and billing rules; the halls differ in five other ways, so the comparison cannot prove the cause")
    cols = [("Kadamba", "Prism", "biz"), ("Yuktāhār", "ABC Hospitality", "tech"), ("Bakul", "Vijayalakshmi Caterers", "users")]
    rows = [("Scale", ["about 1,070 registrations a day", "about 230 to 400 a day", "no records"]),
            ("Menu lines", ["veg and non-veg", "veg only, with Jain service", "veg and non-veg; Palash shares the kitchen (candidate)"]),
            ("Firm and layers", ["four-level chain", "flat team, two project managers", "one manager at the mess, kitchen 8 km away"]),
            ("Records, month", ["CDS scan export, April", "handwritten registers, September", "none"]),
            ("Planning rule", ["fixed 70% of registrations, top-up by supervisor", "matching-week lookup, first-half-hour check, run-out rule", "70 to 80% by item, floor near 70%, phoned top-up"]),
            ("Gap measured", ["63% unused (confirmed)", "about 72% unused (confirmed)", "unknown; manager estimates at most about 60% turn up"])]
    x0 = 190; cw = 330
    for j, (h, s, k) in enumerate(cols):
        st, f = C[k]
        c.add(f'<rect x="{x0+j*(cw+8)}" y="90" width="{cw}" height="52" rx="10" fill="{st}"/><text x="{x0+j*(cw+8)+cw/2}" y="114" font-size="17" font-weight="800" fill="white" text-anchor="middle">{h}</text><text x="{x0+j*(cw+8)+cw/2}" y="132" font-size="12" fill="white" text-anchor="middle">{s}</text>')
    for i, (lab, vals) in enumerate(rows):
        y = 150 + i * 66
        c.add(f'<text x="30" y="{y+34}" font-size="14" font-weight="800" fill="#37474f">{lab}</text>')
        for j, v in enumerate(vals):
            box(c, x0 + j * (cw + 8), y, cw, 58, v, cols[j][2], dashed=(v in ("none", "no records")), fs=12.5)
    c.render("a9-comparison.png")

# ---------------------------------------------------------------- IP chain
def ipchain():
    c = Canvas(1200, 680, "Fourteen intervention points along one breakfast", "From booking to bin, then governance; each tag shows the levers that act there")
    def ip(x, y, w, tag, t, lv, k="tech", d=False):
        box(c, x, y, w, 96, "", k, d)
        s, f = C[k]
        c.add(f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="9" fill="{s}"/><text x="{x+10}" y="{y+18}" font-size="13.5" font-weight="800" fill="white">{tag}</text><text x="{x+w-10}" y="{y+18}" font-size="11.5" fill="white" text-anchor="end">{esc(lv)}</text>')
        for i, ln in enumerate(wrap(t, w - 16, 12.5)[:3]): c.add(f'<text x="{x+8}" y="{y+44+i*16}" font-size="12.5" fill="#1b1b1b">{esc(ln)}</text>')
    c.add('<text x="30" y="84" font-size="14" font-weight="800" fill="#e65100">Before the meal</text>')
    for i, (t, a, l) in enumerate([("IP1", "Default registration: every student booked, on campus or not", "LP2 LP11"), ("IP2", "Cancellation exit, four days ahead; Skip Meal removes no charge", "LP2"), ("IP3", "The kitchen's count, the evening before; Skip Meal effect in conflict", "LP2"), ("IP4", "Day-before plan; Bakul's weekly review", "LP5 LP1 LP3 LP4")]):
        ip(30 + i * 290, 94, 275, t, a, l, "users")
    c.add('<text x="30" y="214" font-size="14" font-weight="800" fill="#1565c0">On the morning</text>')
    for i, (t, a, l) in enumerate([("IP5", "First batch and safety, 5:30 to 7:30; Bakul from about 3 AM", "LP5 LP7"), ("IP6", "Tasting and weekly inspection: no quantity check", "LP7"), ("IP7", "First half hour: flat projection or judgement", "LP6"), ("IP8", "Counter check about 9:00; Bakul phone top-up", "LP6"), ("IP9", "The crest and the back door from 9:15", "LP6")]):
        ip(30 + i * 232, 224, 222, t, a, l, "tech")
    c.add('<text x="30" y="344" font-size="14" font-weight="800" fill="#2e7d32">After the meal</text>')
    for i, (t, a, l) in enumerate([("IP10", "Surplus: held, reheated, reused, eaten by outside diners", "LP5"), ("IP11", "Daily record: a Wastage Book at Yuktāhār only", "LP5 LP4"), ("IP12", "Disposal: bin to contractor at Kadamba", "LP1")]):
        ip(30 + i * 290, 354, 275, t, a, l, "green")
    c.add('<text x="30" y="474" font-size="14" font-weight="800" fill="#6a1b9a">Governance</text>')
    ip(30, 484, 565, "IP13", "Records to rule owners: the export is reviewed by no one", "LP1 LP7 LP9 LP11 LP12", "soc")
    ip(610, 484, 565, "IP14", "Menu cycle, two-weekly: no operator input and no forum", "LP8 LP3 LP4", "soc")
    c.add('<text x="30" y="620" font-size="13" fill="#555">Monthly billing and vendor payment carry LP10 and the ledger bill line. Bakul needs no point of its own: dispatch is IP5, and the phoned top-up is IP8 with a longer delay.</text>')
    c.render("a9-ip-chain.png")

# ---------------------------------------------------------------- sunday
def sunday():
    c = Canvas(1200, 620, "Sunday breakfast: where three levers meet", "Kadamba's veg line on a Sunday is the first test slice")
    st = [("Lowest turnout", "Kadamba's Sunday, against about 1,070 registrations; Yuktāhār's Sundays run 17.9 to 24.1% (confirmed)", "red"),
          ("A 70% veg batch", "about 3.1 times what Sunday diners ate, against about 1.9 on Tuesdays (candidate arithmetic)", "amber"),
          ("Late arrivals", "about 46% of Sunday scans come after 9:15 (confirmed)", "tech")]
    for i, (t, s, k) in enumerate(st): c.node(30, 100 + i * 130, 400, 112, t, s, k, None, False, fs=15, sfs=12.5)
    lv = [("LP2, IP1 to IP3", "Sunday skip that removes the charge and lowers the count", "users"), ("LP5, IP4", "calibrated batch with a named allowance", "biz"), ("LP6, IP8 and IP9", "arrival card and a 9:00 late batch", "biz")]
    ln = [c.node(500, 100 + i * 130, 330, 112, t, s, k, None, False, fs=15, sfs=12.5) for i, (t, s, k) in enumerate(lv)]
    first = c.node(910, 200, 260, 160, "First test slice", "Kadamba veg line, Sunday breakfast", "green", "ic-pot", fs=17, sfs=13.5)
    for n in ln: c.edge(n, first, "#37474f", None, width=3)
    for i in range(3): c.edge((432, 156 + i * 130), (498, 156 + i * 130), "#37474f", None, width=3)
    c.text(30, 520, "Bakul's manager calls weekends very low but gives no figure, so the slice stays specific to Kadamba's veg line.", 13, False, "#555", width=1120)
    c.render("a9-sunday.png")

# ---------------------------------------------------------------- principles
def principles():
    c = Canvas(1200, 760, "Seven design principles", "Every Activity 10 concept must pass all seven; each card lists what it rules out")
    P = [("P1", "Route before you measure, and route on paper", "No new apps, sensors or forecasting software as a first step; no designs that need operators to go digital"),
         ("P2", "Make measurement blame-free, and judge it over months", "No audit-style quantity checks, no deductions from recorded figures, no one-week trials"),
         ("P3", "Change the default, the goal and the belief, not the people", "No nudges or campaigns aimed at students; no blaming operators"),
         ("P4", "Act on the first batch the day before, and on the morning only through the top-up", "No waste cut that raises shortage risk; no one ratio for every hall"),
         ("P5", "Feed the absorbers by plan; target only the over-cooked batch, reheating and the bin", "No restricting resale or the back door; no batch cut without an allowance"),
         ("P6", "Measure cooked against eaten, run-outs and food quality, not turnout", "No turnout targets; no temperature-only quality checks"),
         ("P7", "Measures are diagnostic and plural, never a single target", "No single headline target; no bonus or ranking tied to one figure")]
    cols = ["biz", "tech", "soc", "users", "green", "amber", "teal"]
    for i, (p, t, r) in enumerate(P):
        x = 30 + (i % 4) * 292; y = 90 + (i // 4) * 320
        s, f = C[cols[i]]
        c.add(f'<rect x="{x}" y="{y}" width="278" height="300" rx="14" fill="{f}" fill-opacity="0.8" stroke="{s}" stroke-width="2.2"/>')
        c.add(f'<circle cx="{x+36}" cy="{y+40}" r="26" fill="{s}"/><text x="{x+36}" y="{y+47}" font-size="19" font-weight="800" fill="white" text-anchor="middle">{p}</text>')
        c.text(x + 16, y + 92, t, 15.5, True, "#1b1b1b", width=250)
        c.text(x + 16, y + 190, "Rules out:", 12.5, True, s, width=250)
        c.text(x + 16, y + 208, r, 12.5, False, "#333", width=250)
    c.render("a9-principles.png")

if __name__ == "__main__":
    ladder(); archetype(); compare(); ipchain(); sunday(); principles()
