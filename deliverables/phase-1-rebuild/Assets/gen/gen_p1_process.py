import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def lane(c, y, h, label, key, x=14, w=None, lw=118):
    s, f = C[key]
    w = w or (c.w - 28)
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{f}" fill-opacity="0.5" stroke="{s}" stroke-width="1.4"/>'
          f'<rect x="{x}" y="{y}" width="{lw}" height="{h}" rx="12" fill="{s}"/>')
    ls = wrap(label, lw - 16, 13, True)
    yy = y + h / 2 - (len(ls) - 1) * 8 + 4
    for i, ln in enumerate(ls):
        c.add(f'<text x="{x+lw/2}" y="{yy+i*16:.1f}" font-size="13" font-weight="800" fill="white" text-anchor="middle">{esc(ln)}</text>')

def n(c, x, y, w, h, t, s=None, k="tech", ic=None, d=False, fs=13.5, sfs=11.5):
    return c.node(x, y, w, h, t, s, k, ic, d, fs=fs, sfs=sfs)

def poly(c, pts, color, width=2.6, dash=None):
    c.use_color(color)
    d = "M " + " L ".join(f"{x:.0f} {y:.0f}" for x, y in pts)
    da = f'stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" {da} marker-end="url(#ar-{color[1:]})"/>')

# ---------------------------------------------------------------- diagram6 monthly cycle
def diagram6():
    c = Canvas(1200, 560, "The monthly registration cycle", "Student side: a default, a capped exit and a bill")
    a = n(c, 30, 100, 250, 96, "Student does nothing, or opens the portal", "no daily decision is asked of them", "users", "ic-person", fs=15)
    b = n(c, 330, 100, 270, 96, "Registered automatically for the month", "holidays and absences included; registrations flat at about 1,070 a day at Kadamba", "tech", "ic-toggle", fs=15)
    d = n(c, 650, 100, 270, 96, "One exit: cancel", "5 per meal type per month, at least 4 days ahead", "tech", "ic-calendar-x", fs=15)
    e = n(c, 950, 100, 220, 96, "Billing follows the booking", "monthly bill, eaten or not", "red", "ic-coin", fs=15)
    c.edge(a, b, "#37474f", None, width=3.4); c.edge(b, d, "#37474f", None, width=3.4); c.edge(d, e, "#37474f", None, width=3.4)
    f1 = n(c, 690, 290, 270, 90, "Beyond the cap", "no way to remove the charge (confirmed)", "red", "ic-warning", fs=15)
    f2 = n(c, 340, 290, 300, 110, "Skip Meal", "tells the kitchen not to prepare, but the charge stands; whether Kadamba's kitchen acts on it is unresolved", "amber", "ic-toggle", True, fs=15)
    f3 = n(c, 30, 290, 250, 100, "Mess Cell resale", "outside the portal, at a negotiated price; the one route that returns value", "users", "ic-chat", True, fs=15)
    c.edge(d, f1, C["red"][0], None, width=2.6, a_pt=(800, 200), b_pt=(820, 288), bend=0.0)
    c.edge(b, f2, C["amber"][0], None, width=2.4, dash="6 4", a_pt=(480, 200), b_pt=(480, 288))
    c.edge(b, f3, C["users"][0], None, width=2.4, dash="6 4", a_pt=(380, 200), b_pt=(210, 288))
    c.pill(600, 470, "A decision made on the morning itself has no mechanism at all", "red", fs=14)
    c.render("diagram6-monthly-cycle.png")

# ---------------------------------------------------------------- diagram7 daily cycle
def diagram7():
    c = Canvas(1200, 800, "The daily attendance-decision cycle", "Student side, with Kadamba's April scan times (confirmed, records)")
    # time axis
    x0, x1, y = 60, 1140, 150
    c.add(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#90a4ae" stroke-width="6" stroke-linecap="round"/>')
    t = lambda h, m: x0 + ((h * 60 + m) - (7 * 60 + 20)) / (10 * 60 + 10 - (7 * 60 + 20)) * (x1 - x0)
    c.add(f'<rect x="{t(7,30):.0f}" y="{y-9}" width="{t(9,30)-t(7,30):.0f}" height="18" rx="9" fill="#1565c0" fill-opacity="0.85"/>')
    c.add(f'<rect x="{t(9,15):.0f}" y="{y-16}" width="{t(9,30)-t(9,15):.0f}" height="32" rx="6" fill="#c62828"/>')
    c.add(f'<rect x="{t(9,30):.0f}" y="{y-9}" width="{t(10,7)-t(9,30):.0f}" height="18" rx="9" fill="#e08600" fill-opacity="0.85"/>')
    marks = [((7, 28), "first scans 7:28", -1), ((9, 0), "median scan about 9:00", 1), ((9, 22), "26.5% of scans 9:15 to 9:30", -1), ((9, 30), "close 9:30", 1), ((10, 7), "latest scan 10:07", -1)]
    for (h, m), lab, up in marks:
        px = t(h, m)
        c.add(f'<line x1="{px:.0f}" y1="{y-34*(1 if up<0 else -1)*0 }" x2="{px:.0f}" y2="{y + (-48 if up < 0 else 48)}" stroke="#455a64" stroke-width="1.4"/>')
        ty = y - 56 if up < 0 else y + 66
        anc = "middle"
        if h == 10: anc = "end"
        c.add(f'<text x="{px:.0f}" y="{ty}" font-size="13" font-weight="700" fill="#263238" text-anchor="{anc}">{esc(lab)}</text>')
    c.add(f'<text x="{t(8,15):.0f}" y="{y+34}" font-size="12.5" fill="#1565c0" font-weight="700" text-anchor="middle">service window, 7:30 to 9:30</text>')
    c.add(f'<text x="{t(9,52):.0f}" y="{y+34}" font-size="12.5" fill="#b26a00" font-weight="700" text-anchor="middle">back door</text>')
    # flow
    a = n(c, 30, 300, 190, 84, "Wake", "late sleep is the commonest reason to skip", "users", "ic-clock", fs=15)
    b = n(c, 260, 300, 190, 84, "Check the app?", "one of six respondents does", "tech", "ic-phone", fs=15)
    d = n(c, 490, 300, 200, 84, "Go or skip", "8:30 class, hunger, friends, habit", "users", "ic-toggle", fs=15)
    g1 = n(c, 740, 270, 220, 70, "Go early, 7:30 to 8:00", "counter peaceful; whatever you want", "green", "ic-person", fs=14)
    g2 = n(c, 740, 354, 220, 78, "Go at 9:00 to 9:30", "crowded; items run out (idli, puri, bhatura, fruit)", "amber", "ic-people", fs=14)
    sc = n(c, 990, 300, 180, 84, "QR scan, plate", "veg or non-veg as registered", "tech", "ic-qr", fs=14.5)
    for x1_, x2_ in [(a, b), (b, d)]:
        c.edge(x1_, x2_, "#37474f", None, width=3.2)
    c.edge(d, g1, C["green"][0], None, width=2.6); c.edge(d, g2, C["amber"][0], None, width=2.6)
    c.edge(g1, sc, "#37474f", None, width=2.6); c.edge(g2, sc, "#37474f", None, width=2.6)
    s1 = n(c, 490, 500, 280, 90, "Skip", "the charge stands whatever happens next", "red", "ic-warning", fs=15)
    s2 = n(c, 810, 500, 360, 90, "Resell on Mess Cell, eat elsewhere, or let it go", "four of six have used Mess Cell; none used Skip Meal for value", "users", "ic-chat", fs=14.5)
    c.edge(d, s1, C["red"][0], None, width=2.6, a_pt=(590, 386), b_pt=(630, 498))
    c.edge(s1, s2, "#37474f", None, width=2.4)
    l1 = n(c, 30, 640, 520, 90, "After 9:30", "the front door closes; latecomers use the back door and are not refused (single-sourced); 9.2% of April scans fall at or after 9:30", "amber", "ic-door", True, fs=15)
    l2 = n(c, 590, 640, 580, 90, "What the student sees", "items run out around 9:20 at Kadamba and staff promise a restock that does not come (confirmed, interviews)", "red", "ic-bowl", fs=15)
    c.render("diagram7-daily-cycle.png")

# ---------------------------------------------------------------- d9 exception paths
def d9():
    c = Canvas(1200, 1090, "Exception and workaround paths", "What goes wrong, and what people do about it")
    c.add(f'<text x="60" y="94" font-size="14" font-weight="800" fill="#c62828">What goes wrong</text><text x="640" y="94" font-size="14" font-weight="800" fill="#00695c">What people do</text>')
    rows = [("Student side", "users", [
        ("The charge stands after Skip Meal", "Resell on Mess Cell, or eat elsewhere"),
        ("A student forgets to cancel", "The registration runs and is billed"),
        ("A late riser misses 9:30", "Latecomers enter by the Kadamba back door, served"),
        ("The popular mess is full", "Register for the whole month defensively; buy at spot rate")]),
        ("Operator side", "biz", [
        ("QR scanner fails", "Kadamba staff write ID and name by hand; may be missing from records"),
        ("LPG shortage", "Cut quantities, buy some items outside"),
        ("Grill or toaster broken", "Item removed from service; no replacement yet"),
        ("Exam, event or holiday unknown to the kitchen", "Raised in Yuktāhār's meeting only if someone mentions it"),
        ("Impurities above the norm in grain", "Complaint to the supplier, or a new supplier; paneer brand switched"),
        ("Late run-out at the close", "Not re-cooked past the cut-off; Bakul holds a reserve for about 50 at 9:20"),
        ("Hafizpet top-up too slow", "Phone call, cooking and a 20 to 40 minute drive; the reserve is the hedge"),
        ("Issued does not match cooked", "Raised in the daily meeting; the two diner counts for 3 September (77 and 110) are still unreconciled"),
        ("Biryani lunch", "Cooked at 100%, with a head chef; three pieces for two still causes late run-outs")])]
    y = 110
    for title, key, items in rows:
        h = len(items) * 82 + 16
        c.zone(14, y, 1172, h, title, key, fs=13.5, opacity=0.18)
        yy = y + 30
        for t_, r_ in items:
            a = n(c, 40, yy, 520, 70, t_, None, "red", "ic-warning", fs=14.5)
            b = n(c, 640, yy, 520, 70, r_, None, key, "ic-gear", fs=14, sfs=12)
            c.edge(a, b, "#37474f", None, width=2.8)
            yy += 82
        y += h + 14
    c.render("d9-exception-paths.png")

# ---------------------------------------------------------------- d15 Yuktahaar swimlane
def d15():
    c = Canvas(1260, 900, "Yuktāhār: the book system as a process", "Five lanes, one loop (confirmed from the registers; single-sourced from the operator)")
    names = [("Meeting", "soc"), ("Records", "slate"), ("Store", "amber"), ("Kitchen", "biz"), ("Counter", "tech")]
    ys = [90 + i * 160 for i in range(5)]
    for (nm, k), y in zip(names, ys): lane(c, y, 148, nm, k)
    X = lambda i: 150 + i * 220
    W = 206; H = 116
    def put(col, lane_i, w_cols, t_, s_, k, ic, d=False):
        return n(c, X(col), ys[lane_i] + 16, W + (w_cols - 1) * 220, H, t_, s_, k, ic, d, fs=13.5, sfs=11)
    m1 = put(0, 0, 2, "Daily meeting, the day before", "registrations (regular, Jain, cash); matching-week Wastage Book page; month pattern; events only if someone mentions them", "soc", "ic-people")
    m2 = put(2, 0, 2, "Same menu day returns, two weeks later", "the matching page is read again (delay mark: two weeks)", "red", "ic-clock", True)
    m3 = put(4, 0, 1, "Two-book check", "issued must equal cooked; mismatches raised here", "soc", "ic-scale")
    r1 = put(1, 1, 1, "Weekday attendance register", "every Sunday together, every Monday together (one-week loop)", "slate", "ic-chart")
    r2 = put(2, 1, 2, "Wastage Book", "issued, cooked, left, %, run-out time, re-cook, plate waste plus leftover", "slate", "ic-book")
    r3 = put(4, 1, 1, "Wastage board", "a falling waste-share target", "slate", "ic-chart")
    s1 = put(0, 2, 1, "Store book, then Grocery Book issue", "per-dish kg; cross-checked by a peer", "amber", "ic-book")
    s2 = put(1, 2, 1, "Clean grain against the impurity norm", "over the norm: complain or change supplier", "amber", "ic-scale")
    k1 = put(1, 3, 1, "Cook 5:30 to 7:30", "mostly one batch; poha in two", "biz", "ic-pot")
    k2 = put(3, 3, 1, "Re-cook by run-out time", "early run-out: re-cook; late: no", "biz", "ic-flame")
    k3 = put(4, 3, 1, "After close: reuse", "idli to idli upma or poha; batter to fridge; milk to curd", "green", "ic-bowl")
    t1 = put(2, 4, 1, "Service from 7:30", "first half hour sampled to project the rest", "tech", "ic-clock")
    t2 = put(3, 4, 1, "Counter checks every 30 minutes", "from about 8:45; second roti counter at peak", "tech", "ic-eye")
    G = "#37474f"
    c.edge(m1, s1, G, None, width=3, a_pt=(X(0) + 103, ys[0] + 132), b_pt=(X(0) + 103, ys[2] + 14))
    c.edge(s1, s2, G, None, width=3)
    c.edge(s2, k1, G, None, width=3)
    c.edge(k1, t1, G, None, width=3, a_pt=(X(1) + 206, ys[3] + 100), b_pt=(X(2) + 4, ys[4] + 40))
    c.edge(t1, t2, G, None, width=3)
    c.edge(t2, k2, C["biz"][0], "run-out", width=2.8, lfs=11, a_pt=(X(3) + 103, ys[4] + 14), b_pt=(X(3) + 103, ys[3] + 134))
    c.edge(k2, k3, G, None, width=3)
    c.edge(k3, r3, G, None, width=2.8, a_pt=(X(4) + 103, ys[3] + 14), b_pt=(X(4) + 103, ys[1] + 134))
    c.edge(r3, r2, G, None, width=2.6)
    c.edge(r2, m2, C["red"][0], "two-week delay", width=2.8, dash="6 4", lfs=11, a_pt=(X(2) + 215, ys[1] + 16), b_pt=(X(2) + 215, ys[0] + 134))
    c.edge(r1, m1, C["soc"][0], "one-week loop", width=2.6, dash="6 4", lfs=11, a_pt=(X(1) + 103, ys[1] + 16), b_pt=(X(1) + 103, ys[0] + 134))
    c.render("d15-yuktahaar-operator-swimlane.png")

# ---------------------------------------------------------------- d16 Kadamba swimlane
def d16():
    c = Canvas(1200, 980, "Kadamba: the operator side of the breakfast day", "Single-sourced (operator, heard first-hand); the display plate and tasting confirmed by observation")
    c.add(f'<rect x="14" y="76" width="1172" height="46" rx="10" fill="#f3e5f5" stroke="#6a1b9a" stroke-width="1.4"/>'
          f'<text x="30" y="105" font-size="14" font-weight="800" fill="#6a1b9a">Governance strip: CFS, then CDS (head unresolved), then Prism (tender); operations manager, manager, supervisor, service staff</text>')
    names = [("Planning", "soc"), ("Kitchen", "biz"), ("Safety", "tech"), ("Counter", "users"), ("After close", "slate")]
    ys = [134 + i * 166 for i in range(5)]
    for (nm, k), y in zip(names, ys): lane(c, y, 154, nm, k)
    p1 = n(c, 150, ys[0] + 14, 250, 126, "Veg and non-veg registrations", "read the day before", "soc", "ic-toggle", fs=13.5, sfs=11)
    p2 = n(c, 440, ys[0] + 14, 330, 126, "First batch: about 70%, by gram standard", "plus about 30 portions for outside people; dry goods a week ahead, perishables the day before", "soc", "ic-scale", fs=13.5, sfs=11)
    k1 = n(c, 150, ys[1] + 14, 250, 126, "5:30 chef batch", "sambar, upma; the main veg chef", "biz", "ic-pot", fs=13.5, sfs=11)
    k2 = n(c, 440, ys[1] + 14, 330, 126, "Live counter from 7:00", "dosa and vada cooked in front of diners", "biz", "ic-flame", fs=13.5, sfs=11)
    k3 = n(c, 810, ys[1] + 14, 360, 126, "Top-up ready in 10 to 15 minutes", "raw remainder held; hold and reheat is the team's candidate reading", "biz", "ic-clock", fs=13.5, sfs=11)
    s1 = n(c, 150, ys[2] + 14, 1020, 126, "Food-safety sequence before service (detail in the next figure)", "cooking temperature, 72-hour sample, wrapped display plate, serving temperature per item, tasting with the facility team and two Prism staff, corrections", "tech", "ic-thermometer", fs=14, sfs=12)
    c1 = n(c, 150, ys[3] + 14, 330, 126, "Service from about 7:30", "the supervisor watches item levels against gram standards", "users", "ic-eye", fs=13.5, sfs=11)
    c2 = n(c, 520, ys[3] + 14, 330, 126, "Last-ten-minute crest", "26.5% of scans between 9:15 and 9:30; rule of thumb about 150 in the last ten minutes", "red", "ic-chart", fs=13.5, sfs=11)
    c3 = n(c, 890, ys[3] + 14, 280, 126, "9:30 close", "front door shuts; back door after 9:30; 9.2% of scans come later", "amber", "ic-door", fs=13.5, sfs=11)
    a1 = n(c, 150, ys[4] + 14, 380, 126, "Outside diners and about half the staff eat", "30 to 50 outsiders such as night security", "green", "ic-people", fs=13.5, sfs=11)
    a2 = n(c, 570, ys[4] + 14, 280, 126, "The bin", "dustbin to a garbage contractor; no composting", "red", "ic-bin", fs=13.5, sfs=11)
    a3 = n(c, 890, ys[4] + 14, 280, 126, "Records", "gram standards; waste about 5 to 10% on an unstated base", "slate", "ic-book", fs=13.5, sfs=11)
    G = "#37474f"
    c.edge(p1, p2, G, None, width=3); c.edge(k1, k2, G, None, width=3); c.edge(k2, k3, G, None, width=3)
    c.edge(c1, c2, G, None, width=3); c.edge(c2, c3, G, None, width=3)
    c.edge(p2, k1, G, None, width=3, a_pt=(520, ys[0] + 141), b_pt=(280, ys[1] + 13), bend=0.0)
    c.edge(k1, s1, G, None, width=3, a_pt=(280, ys[1] + 141), b_pt=(280, ys[2] + 13))
    c.edge(s1, c1, G, None, width=3, a_pt=(320, ys[2] + 141), b_pt=(320, ys[3] + 13))
    c.edge(c3, a1, G, None, width=2.6, a_pt=(1030, ys[3] + 141), b_pt=(400, ys[4] + 13), bend=0.0)
    c.edge(a1, a2, G, None, width=2.6); c.edge(a2, a3, G, None, width=2.6)
    c.render("d16-kadamba-operator-swimlane.png")

# ---------------------------------------------------------------- d17 food-safety sequence
def d17():
    c = Canvas(1200, 560, "Kadamba's food-safety sequence", "Every meal, before service; the display plate and the tasting were observed (confirmed), the rest is single-sourced")
    steps = [("Cook", "batch items from 5:30", "ic-pot"), ("Cooking temperature", "checked", "ic-thermometer"), ("72-hour sample", "kept, so any illness can be traced", "ic-flask"),
             ("Display plate", "wrapped, at the entrance: the full menu", "ic-plate"), ("Serving temperature", "measured per item", "ic-thermometer"),
             ("Tasting", "facility team with two Prism staff", "ic-eye"), ("Corrections", "before service", "ic-gear"), ("Service", "by 7:30", "ic-clock")]
    prev = None
    for i, (t, s, ic) in enumerate(steps):
        x = 30 + (i % 4) * 292; y = 110 + (i // 4) * 170
        k = "tech" if i not in (3, 5) else "green"
        nd = n(c, x, y, 262, 100, t, s, k, ic, fs=15, sfs=12.5)
        if prev:
            if i % 4 == 0:
                c.edge(prev, nd, "#37474f", None, width=3, a_pt=(1150, 212), b_pt=(150, 108), bend=0.0) if False else None
            else:
                c.edge(prev, nd, "#37474f", None, width=3)
        prev = nd
    c.add(f'<path d="M 1100 212 L 1100 240 L 160 240 L 160 276" fill="none" stroke="#37474f" stroke-width="3" marker-end="url(#ar-37474f)"/>')
    c.use_color("#37474f")
    c.node(30, 400, 560, 90, "Weekly", "QC inspects, including the store", "slate", "ic-shield", fs=15, sfs=12.5)
    c.node(620, 400, 550, 90, "Daily", "TDS read on cooking and drinking water; a failure triggers a full check", "slate", "ic-flask", fs=15, sfs=12.5)
    c.render("d17-food-safety-sequence.png")

# ---------------------------------------------------------------- d24 Bakul loop
def d24():
    c = Canvas(1200, 900, "Bakul: the off-site breakfast loop", "The manager's account (single-sourced); no Bakul records exist")
    a = n(c, 40, 100, 340, 90, "Registrations", "automatic default for every student", "tech", "ic-toggle", fs=15)
    b = n(c, 420, 100, 360, 90, "Weekly review of past attendance", "the manager's judgement; whether it is written down is unknown", "biz", "ic-eye", True, fs=15)
    fb = n(c, 240, 240, 720, 96, "First batch: 70 to 80% of registrations, by item", "floor about 70% even on low weekends: \"there should not be a shortage of food, even if some wastage occurs\"", "biz", "ic-scale", fs=15)
    h = n(c, 40, 390, 330, 100, "Hafizpet kitchen", "labour-heavy items such as aloo paratha started from about 3 AM", "biz", "ic-truck", fs=15)
    tr = n(c, 420, 390, 360, 100, "Road, about 8 km", "about 20 minutes early, 40 later; insulated boxes at 60 to 72 °C", "ext", "ic-truck", fs=15)
    bk = n(c, 830, 390, 330, 100, "Bakul, about 7 AM", "hot-water holding; steam softens parathas", "tech", "ic-thermometer", fs=15)
    sv = n(c, 40, 540, 330, 96, "Service from 7:30", "main rush 8:00 to 8:30; 10 to 15 in the last ten minutes", "users", "ic-people", fs=15)
    ck = n(c, 420, 540, 360, 96, "Check every 30 minutes", "food left against registrations and demand still expected", "biz", "ic-eye", fs=15)
    sh = n(c, 820, 540, 340, 96, "Short? Phone Hafizpet", "cook plus a 20 to 40 minute drive; lead time unknown", "amber", "ic-phone", fs=15)
    rs = n(c, 420, 690, 360, 96, "Reserve for about 50 at 9:20", "candidate: held because a late top-up could not arrive", "amber", "ic-clock", True, fs=15)
    lo = n(c, 820, 690, 340, 96, "Leftovers", "some back to Hafizpet, the rest thrown", "red", "ic-bin", fs=15)
    G = "#37474f"
    c.edge(a, fb, G, None, width=3, a_pt=(210, 192), b_pt=(400, 238)); c.edge(b, fb, G, None, width=3, a_pt=(600, 192), b_pt=(600, 238))
    c.edge(fb, h, G, None, width=3, a_pt=(400, 338), b_pt=(205, 388)); c.edge(h, tr, G, None, width=3); c.edge(tr, bk, G, None, width=3)
    c.edge(bk, sv, G, None, width=3, a_pt=(900, 492), b_pt=(250, 538), bend=0.0) if False else None
    c.edge((995, 492), (995, 538), G, None, width=0) if False else None
    c.edge(bk, sh, G, None, width=0) if False else None
    c.edge((205, 492), (205, 538), G, None, width=3)
    c.edge(sv, ck, G, None, width=3); c.edge(ck, sh, G, None, width=3)
    poly(c, [(990, 538), (990, 514), (205, 514), (205, 494)], C["amber"][0], 2.6, "6 4")
    c.pill(600, 514, "order: cook, then drive 20 to 40 minutes", "amber", fs=11.5)
    c.edge(ck, rs, G, None, width=2.6, a_pt=(600, 638), b_pt=(600, 688)); c.edge(rs, lo, G, None, width=2.6)
    c.render("d24-bakul-offsite-loop.png")

if __name__ == "__main__":
    diagram6(); diagram7(); d9(); d15(); d16(); d17(); d24()
