import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def box(c, x, y, w, h, text, key, fs=12.5, bold=False, dashed=False, fillop=0.75, anchor="start", pad=9):
    s, f = C[key]
    da = 'stroke-dasharray="5 4"' if dashed else ""
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{f}" fill-opacity="{fillop}" stroke="{s}" stroke-width="1.8" {da}/>')
    lines = wrap(text, w - 2 * pad, fs, bold)
    yy = y + (h - len(lines) * fs * 1.25) / 2 + fs * 0.95
    for ln in lines:
        tx = x + pad if anchor == "start" else x + w / 2
        c.add(f'<text x="{tx}" y="{yy:.1f}" font-size="{fs}" font-weight="{700 if bold else 400}" fill="#1b1b1b" text-anchor="{anchor}">{esc(ln)}</text>'); yy += fs * 1.25

# 1 perspectives
def perspectives():
    rows = [("Students", "users", "ic-person", "An automatic booking, five exits, a charge that stands; resale is the only recovery", "The aggregate cost. One lost ₹48 is annoying, not alarming"),
            ("Kadamba operator", "biz", "ic-pot", "A 70% first batch by gram standard, topped up on the supervisor's call; the count is its paid obligation", "Any route from its records to the rules, or any say over close, billing or menu"),
            ("Yuktāhār operator", "biz", "ic-book", "The gap every morning, item by item, in books that learn; waste is a cost", "Anyone upstream to tell: complaints flow in, measurements never flow out"),
            ("Bakul operator", "biz", "ic-truck", "A weekly 70 to 80% share, phone top-ups, a reserve for about 50; shortage is the failure to avoid", "Any record, and any say over the menu it sees eaten"),
            ("Facility team and QC", "tech", "ic-thermometer", "Safety and taste at every meal, from temperature to tasting", "Quantity cooked, waste or turnout"),
            ("CFS and CDS", "soc", "ic-building", "The workload behind one policy change, and a scan for every breakfast", "The gap as a daily pain: it is a number they hold"),
            ("Menu committee", "soc", "ic-briefcase", "Menu satisfaction, which it already fixed", "Per-item waste, and what actually sells"),
            ("Academic administration", "ext", "ic-clock", "Nothing related to the mess", "The 8:30 collision, or any channel to mess governance"),
            ("Outside diners and staff", "green", "ic-people", "Reliable meals from the same food", "Any count in the records, or a seat in governance")]
    h = 110 + len(rows) * 68
    c = Canvas(1200, h, "What each stakeholder experiences, and what they never see", "Each feels a smaller piece; nobody sees the whole")
    c.add('<text x="290" y="96" font-size="14" font-weight="800" fill="#2e7d32">Feels</text><text x="760" y="96" font-size="14" font-weight="800" fill="#c62828">Never sees</text>')
    for i, (n, k, ic, a, b) in enumerate(rows):
        y = 108 + i * 68
        c.node(20, y, 240, 58, n, None, k, ic, False, fs=14)
        box(c, 276, y, 450, 58, a, "green", 12.5)
        box(c, 742, y, 440, 58, b, "red", 12.5, dashed=True)
    c.render("s08r-perspectives.png")

# 2 tensions
def tensions():
    T = [("Individual sense", "Total cost", "Resale is right for one student; at scale it is the waste"),
         ("Billing certainty", "Demand accuracy", "The institution chose certainty both times the trigger passed"),
         ("Operator knowledge", "Operator authority", "Best data, control over quantity only"),
         ("One billing basis", "Three operator stances", "Cook to the count, learn from books, hold a floor"),
         ("The operator's discount", "The late crest", "Cook less: run-outs. Cook more: waste"),
         ("One rule", "Real variation", "Four halls, three kitchen systems"),
         ("Transparency", "Gaming", "A menu posted ahead fixed fatigue and let students plan skipping"),
         ("Loud complaints", "Quiet costs", "A path that fixed the menu in one pass never carried the gap"),
         ("One model", "Real difference", "Fasting and habit counted as no-shows"),
         ("Two systems", "Nobody between", "8:30 class start and 7:30 to 9:30 breakfast, no link")]
    c = Canvas(1200, 90 + 5 * 118 + 20, "Tensions that hold the gap in place", "Both poles of every pair are individually reasonable")
    for i, (a, b, note) in enumerate(T):
        x = 20 + (i % 2) * 590; y = 86 + (i // 2) * 118
        c.add(f'<rect x="{x}" y="{y}" width="570" height="108" rx="12" fill="#fff" stroke="#b0bec5" stroke-width="1.6"/>')
        box(c, x + 12, y + 12, 220, 38, a, "biz", 13, True, anchor="middle")
        box(c, x + 338, y + 12, 220, 38, b, "amber", 13, True, anchor="middle")
        c.add(f'<line x1="{x+236}" y1="{y+31}" x2="{x+334}" y2="{y+31}" stroke="#c62828" stroke-width="3"/>')
        c.pill(x + 285, y + 31, "vs", "red", fs=12)
        c.text(x + 285, y + 78, note, 12.5, False, "#333", "middle", width=520)
    c.render("s08r-tensions.png")

# 3 iceberg
def iceberg():
    c = Canvas(1100, 640, "Reading the reframe through the iceberg", "The original framing stayed above the waterline")
    c.add('<rect x="0" y="292" width="1100" height="348" fill="#e3f2fd" fill-opacity="0.7"/><line x1="0" y1="292" x2="1100" y2="292" stroke="#1565c0" stroke-width="3" stroke-dasharray="9 6"/>')
    c.add('<text x="1085" y="284" font-size="13" font-weight="800" fill="#1565c0" text-anchor="end">waterline: what Phase 1 asked about</text>')
    L = [("Events", "a charge for a skipped breakfast; items gone by 9:20; one Sunday at Yuktāhār, 267 booked and 50 eaten", "tech", 460, 84, 90),
         ("Patterns", "breakfast unused far more than lunch; flat bookings, swinging turnout; a late crest; first batches above turnout", "biz", 640, 186, 90),
         ("Structures", "automatic default with five exits; billing at the booking; the gap measured and unrouted; safety-only oversight; four owners", "soc", 820, 312, 100),
         ("Mental models", "registration is demand; cook what is registered; waste is cost; no shortage even if waste; measurement means blame", "red", 1040, 434, 100)]
    for t_, s, k, w, y, h in L:
        c.node((1100 - w) / 2, y, w, h, t_, s, k, None, False, fs=17, sfs=12.5)
    c.render("s08r-iceberg.png")

# 4 equilibrium
def equilibrium():
    c = Canvas(1200, 960, "Why the gap holds steady", "Forces create it, absorbers soak up its cost, and only loud signals reach the rule setters")
    F = ["Default booking, five exits", "Billing at the booking", "Gap measured, not routed"]
    c.add('<text x="20" y="176" font-size="14" font-weight="800" fill="#c62828">Forces that create the gap</text>')
    for i, t_ in enumerate(F): c.node(20, 190 + i * 110, 300, 76, t_, None, "red", None, False, fs=14)
    gap = c.node(420, 290, 280, 170, "The gap", "breakfast registration far above attendance; lunch under the same rules mostly works", "navy", "ic-toggle", False, fs=20, sfs=13)
    for i in range(3): c.edge((322, 228 + i * 110), (418, 375), "#c62828", None, width=3)
    A = [("Resale on Mess Cell", "users"), ("Operator top-ups and discount", "biz"), ("Reuse at Yuktāhār", "green"), ("Outside diners and Kadamba staff", "green"), ("Held and reheated food (candidate)", "amber"), ("Late-door service", "tech"), ("Outside venues", "ext"), ("The bin", "red")]
    c.add('<text x="780" y="176" font-size="14" font-weight="800" fill="#2e7d32">Absorbers: most are useful</text>')
    for i, (t_, k) in enumerate(A):
        y = 190 + i * 54
        c.node(780, y, 400, 44, t_, None, k, None, k == "amber", fs=13)
        c.edge((702, 375), (778, y + 22), "#455a64", None, width=1.8)
    c.node(420, 84, 280, 64, "Rule setters", "office, committee, CFS", "soc", "ic-briefcase", False, fs=15, sfs=12)
    c.edge((560, 288), (560, 152), C["red"][0], None, width=3, dash="7 5")
    c.pill(560, 220, "only loud complaints arrive", "red", fs=12)
    c.add('<line x1="20" y1="670" x2="1180" y2="670" stroke="#c62828" stroke-width="3" stroke-dasharray="9 6"/><text x="20" y="660" font-size="13" font-weight="800" fill="#c62828">the kitchen door: nothing the kitchens learn crosses this line upward</text>')
    c.node(20, 720, 520, 90, "Local correction at Yuktāhār", "blame-free weighing, a matching-week lookup, daily discussion: waste fell between August and December", "green", "ic-book", False, fs=14, sfs=12)
    c.node(560, 720, 620, 90, "Local correction at Bakul and Kadamba", "Bakul adjusts weekly but only down to its floor; Kadamba has one recorded adjustment and no outcome record", "amber", "ic-truck", False, fs=14, sfs=12)
    c.edge((280, 718), (280, 680), "#2e7d32", None, width=3)
    c.add('<text x="296" y="706" font-size="22" font-weight="800" fill="#c62828">X</text>')
    c.legend(20, 840, [(C["red"][0], "force or exit that does not exist", "dash"), (C["green"][0], "absorber or learning that works", "box")], title="Reading the picture")
    c.render("s08r-equilibrium.png")

# 5 framings matrix
def framings():
    F = [("More registered students attend", 0, 0, 0, 0), ("Registration as a truer signal of intent", 0, 0, 1, 0), ("Kitchens forecast better", 0, 0, 0, 1), ("Every operator runs like Yuktāhār", 0, 1, 0, 1), ("Why breakfast fails when lunch works", 2, 0, 1, 2), ("Who should own the gap", 0, 1, 1, 1), ("The reframing: a stable equilibrium", 2, 2, 2, 2)]
    cols = ["Explains why breakfast and not lunch", "Explains why it persists unseen", "Reaches the booking", "Fits the evidence"]
    c = Canvas(1200, 150 + len(F) * 60, "Alternative framings against four tests", "Full circle: passes. Half: partly. Empty: fails")
    for j, t in enumerate(cols):
        x = 470 + j * 180
        for k, ln in enumerate(wrap(t, 165, 12.5, True)): c.add(f'<text x="{x+90}" y="{96+k*15}" font-size="12.5" font-weight="800" fill="#37474f" text-anchor="middle">{esc(ln)}</text>')
    for i, row in enumerate(F):
        y = 132 + i * 60
        last = i == len(F) - 1
        c.add(f'<rect x="20" y="{y}" width="1160" height="52" rx="9" fill="{"#e8f5e9" if last else "#f7f9fb"}" stroke="{"#2e7d32" if last else "#cfd8dc"}" stroke-width="1.6"/>')
        c.add(f'<text x="34" y="{y+31}" font-size="14" font-weight="{800 if last else 600}" fill="#1b1b1b">{esc(row[0])}</text>')
        for j in range(4):
            cx = 470 + j * 180 + 90; cy = y + 26; v = row[j + 1]
            c.add(f'<circle cx="{cx}" cy="{cy}" r="13" fill="white" stroke="#37474f" stroke-width="2.4"/>')
            if v == 2: c.add(f'<circle cx="{cx}" cy="{cy}" r="13" fill="#2e7d32"/>')
            if v == 1: c.add(f'<path d="M {cx} {cy-13} A 13 13 0 0 1 {cx} {cy+13} Z" fill="#37474f"/>')
    c.render("s08r-framings.png")

# 6 assumptions
def assumptions():
    A = [("The 8:30 class is the main reason students skip", "Not the main reason", "amber", "late sleep is named far more often"),
         ("A skipped breakfast leads to a crash and a later purchase", "Only link 1 confirmed", "ext", "nobody was asked what happens after"),
         ("Registration approximates who will eat", "Overturned", "red", "37.1% eaten at Kadamba, about 28% at Yuktāhār"),
         ("The gap is about 30%", "Revised", "amber", "63% at Kadamba, about 72% at Yuktāhār"),
         ("Four halls means four kitchens", "Revised", "amber", "Bakul and Palash share an off-site kitchen"),
         ("The kitchen cooks to the count or a four-day order", "Overturned", "red", "each operator applies its own ratio and tops up"),
         ("Nobody measures the gap", "Overturned", "red", "measured twice: scan records and operator books"),
         ("The crowd builds to a peak before close", "Confirmed", "green", "26.5% of scans between 9:15 and 9:30"),
         ("Surplus food is composted", "Overturned", "red", "Kadamba's waste goes to a garbage contractor"),
         ("Skip Meal declarations reach the kitchen", "Conflicting", "ext", "Kadamba says it cooks on registrations alone"),
         ("Nobody has solved the gap", "Overturned", "red", "attendance-tracked billing ran twice"),
         ("Peer company drives attendance", "Disconfirmed", "red", "four of six say a friend's absence changes nothing"),
         ("Academic administration is connected to the mess", "Confirmed absent", "green", "no relationship, in three independent sources"),
         ("Operator revenue is cut off from attendance", "Open", "ext", "plate basis unconfirmed for every operator")]
    c = Canvas(1200, 100 + len(A) * 54 + 20, "Assumptions tested against evidence", "Where each assumption came from, and what the records and operators found")
    for i, (a, v, k, e) in enumerate(A):
        y = 92 + i * 54
        box(c, 20, y, 520, 46, a, "ext", 12.8, anchor="start", fillop=0.35)
        s, f = C[k]
        c.add(f'<rect x="556" y="{y+4}" width="170" height="38" rx="19" fill="{s}"/><text x="641" y="{y+28}" font-size="13" font-weight="800" fill="white" text-anchor="middle">{esc(v)}</text>')
        c.add(f'<text x="742" y="{y+28}" font-size="12.8" fill="#333">{esc(e)}</text>')
    c.render("s08r-assumptions.png")

if __name__ == "__main__":
    perspectives(); tensions(); iceberg(); equilibrium(); framings(); assumptions()
