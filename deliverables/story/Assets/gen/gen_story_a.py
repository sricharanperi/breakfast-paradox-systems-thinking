import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

PUZ, CTX, PEO, PRO, SYS, CAU, DES, TST, NEU = "#E65100", "#1565C0", "#6A1B9A", "#00838F", "#00695C", "#AD1457", "#283593", "#EF6C00", "#455A64"
INK, SOFT = "#22262B", "#6B7480"

def T(c, x, y, s, fs=18, bold=False, col=INK, anchor="start", italic=False, halo=False):
    h = 'stroke="white" stroke-width="6" stroke-linejoin="round" paint-order="stroke"' if halo else ""
    c.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{fs}" font-weight="{800 if bold else 500}" fill="{col}" text-anchor="{anchor}" {"font-style=italic" if italic else ""} {h}>{esc(s)}</text>')

def TL(c, x, y, lines, fs=18, bold=False, col=INK, anchor="middle", lh=1.25, halo=False):
    for i, ln in enumerate(lines): T(c, x, y + i * fs * lh, ln, fs, bold, col, anchor, False, halo)

def circ(c, cx, cy, r, fill, stroke=None, sw=3, dash=None):
    d = f'stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" {f"stroke={chr(34)}{stroke}{chr(34)} stroke-width={chr(34)}{sw}{chr(34)}" if stroke else ""} {d}/>')

def icon(c, name, cx, cy, r, col, white=True):
    circ(c, cx, cy, r, col)
    s = r * 1.25
    c.add(f'<use href="#{name}" x="{cx-s/2:.1f}" y="{cy-s/2:.1f}" width="{s:.1f}" height="{s:.1f}" fill="{"white" if white else col}"/>')

def card(c, x, y, w, h, col, fill="white", rx=18, sw=3, dash=None, op=1):
    d = f'stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" fill-opacity="{op}" stroke="{col}" stroke-width="{sw}" {d}/>')

def arrow(c, x1, y1, x2, y2, col, w=4, dash=None):
    c.use_color(col)
    d = f'stroke-dasharray="{dash}"' if dash else ""
    c.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" {d} marker-end="url(#ar-{col[1:]})"/>')

# ---------------------------------------------------------------- journey
def journey():
    c = Canvas(1200, 760)
    parts = [("PART 1", "The puzzle", PUZ), ("PART 2", "Looking from outside", CTX), ("PART 3", "Seeing the system", SYS), ("PART 4", "Deciding what to change", DES), ("PART 5", "Looking back", NEU)]
    px = 30
    for i, (a, b, col) in enumerate(parts):
        circ(c, px + 12, 40, 11, col); T(c, px + 30, 47, b, 17, True, col); px += 30 + len(b) * 9.5 + 34
    stops = [(1, "The puzzle", PUZ, "1"), (2, "Drawing the edge,\nwho is in the room", CTX, "2 to 4"), (3, "Following\none breakfast", CTX, "5"), (4, "The numbers\narrive", SYS, "6"),
             (5, "One page, then\nthe loops", SYS, "7, 8"), (6, "Why it keeps\nhappening", SYS, "9, 10"), (7, "Where we can\npush", DES, "11"), (8, "Ideas on trial", DES, "12"), (9, "What we\nrecommend", DES, "13"), (10, "What we got wrong,\nwhat nobody knows", NEU, "14")]
    pos = [(130, 200), (440, 200), (750, 200), (1060, 200), (1060, 430), (750, 430), (440, 430), (130, 430), (130, 650), (440, 650)]
    # path
    path = "M 60 200 L 1060 200 C 1160 200 1160 430 1060 430 L 130 430 C 30 430 30 650 130 650 L 560 650"
    c.add(f'<path d="{path}" fill="none" stroke="#DDE3EA" stroke-width="30" stroke-linecap="round" stroke-linejoin="round"/>')
    c.add(f'<path d="{path}" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-dasharray="14 14" stroke-linecap="round"/>')
    for (n, lab, col, ch), (x, y) in zip(stops, pos):
        circ(c, x, y, 38, col, "white", 5)
        T(c, x, y + 12, str(n), 34, True, "white", "middle")
        lines = lab.split("\n")
        TL(c, x, y - 66 - (len(lines) - 1) * 24, lines, 20, True, INK, "middle", 1.2)
        T(c, x, y + 74, "chapter " + ch, 16, False, SOFT, "middle")
    c.pill(1060, 292, "turning point", "amber", fs=16)
    c.render("f-journey.png")

# ---------------------------------------------------------------- rohan
def person(c, x, y, s=1.0, col="#6A1B9A", droop=False, lying=False):
    if lying:
        c.add(f'<rect x="{x-70*s}" y="{y-6*s}" width="{150*s}" height="{40*s}" rx="{18*s}" fill="{col}" fill-opacity="0.85"/>')
        circ(c, x - 72 * s, y + 10 * s, 24 * s, "#F2C6A0", "#22262B", 3)
        return
    c.add(f'<rect x="{x-26*s}" y="{y+(22 if droop else 10)*s}" width="{52*s}" height="{74*s}" rx="{22*s}" fill="{col}"/>')
    hy = y + (22 if droop else 0) * s
    circ(c, x + (14 if droop else 0) * s, hy, 24 * s, "#F2C6A0", "#22262B", 3)

def clock(c, cx, cy, r, h, m, col=PUZ):
    circ(c, cx, cy, r, "white", col, 5)
    for k in range(12):
        a = k * math.pi / 6
        c.add(f'<line x1="{cx+(r-9)*math.sin(a):.1f}" y1="{cy-(r-9)*math.cos(a):.1f}" x2="{cx+(r-3)*math.sin(a):.1f}" y2="{cy-(r-3)*math.cos(a):.1f}" stroke="{INK}" stroke-width="2"/>')
    ah = (h % 12 + m / 60) * math.pi / 6; am = m * math.pi / 30
    c.add(f'<line x1="{cx}" y1="{cy}" x2="{cx+r*0.5*math.sin(ah):.1f}" y2="{cy-r*0.5*math.cos(ah):.1f}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')
    c.add(f'<line x1="{cx}" y1="{cy}" x2="{cx+r*0.78*math.sin(am):.1f}" y2="{cy-r*0.78*math.cos(am):.1f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>')

def rohan():
    c = Canvas(1200, 470)
    w, g = 262, 30
    xs = [30 + i * (w + g) for i in range(4)]
    caps = [("7:45", "The alarm rings. Four times."), ("Roll over", "Twenty more minutes."), ("9:45", "Full trays go in the bin."), ("11:15", "Back-to-back lectures.")]
    cols = [PUZ, PEO, CAU, CTX]
    for i, x in enumerate(xs):
        card(c, x, 20, w, 330, cols[i], "#FFF8F2" if i == 0 else "white", 22)
        T(c, x + 18, 58, f"{i+1}", 26, True, cols[i])
    # panel 1: bed + clock
    x = xs[0]
    c.add(f'<rect x="{x+30}" y="240" width="210" height="46" rx="12" fill="#CFD8DC"/><rect x="{x+30}" y="286" width="210" height="14" rx="4" fill="#90A4AE"/>')
    person(c, x + 120, 205, 1, PEO, lying=True) if False else None
    c.add(f'<rect x="{x+50}" y="212" width="170" height="34" rx="16" fill="{PEO}" fill-opacity="0.85"/>')
    circ(c, x + 62, 226, 24, "#F2C6A0", INK, 3)
    clock(c, x + 190, 120, 52, 7, 45)
    T(c, x + 190, 52, "ring ring", 18, True, PUZ, "middle")
    # panel 2
    x = xs[1]
    c.add(f'<rect x="{x+30}" y="240" width="210" height="46" rx="12" fill="#CFD8DC"/><rect x="{x+30}" y="286" width="210" height="14" rx="4" fill="#90A4AE"/>')
    c.add(f'<rect x="{x+40}" y="196" width="190" height="56" rx="26" fill="{PEO}"/>')
    circ(c, x + 62, 236, 22, "#F2C6A0", INK, 3)
    T(c, x + 170, 140, "z", 34, True, SOFT); T(c, x + 196, 112, "z", 44, True, SOFT); T(c, x + 228, 78, "Z", 54, True, SOFT)
    # panel 3: trays and bin
    x = xs[2]
    for k in range(3):
        ty = 110 + k * 62
        c.add(f'<rect x="{x+26}" y="{ty}" width="150" height="46" rx="10" fill="#ECEFF1" stroke="{NEU}" stroke-width="3"/>')
        for j, col in enumerate(["#F9A825", "#8BC34A", "#EF5350", "#FFB74D"]):
            circ(c, x + 52 + j * 34, ty + 23, 12, col)
    c.add(f'<path d="M {x+178} 170 L {x+184} 296 L {x+240} 296 L {x+246} 170 Z" fill="#78909C"/><rect x="{x+172}" y="152" width="80" height="16" rx="6" fill="#546E7A"/>')
    c.add(f'<path d="M {x+150} 200 Q {x+178} 130 {x+208} 150" fill="none" stroke="{CAU}" stroke-width="5" stroke-dasharray="8 7" marker-end="url(#ar-{CAU[1:]})"/>'); c.use_color(CAU)
    # panel 4: lecture, droop
    x = xs[3]
    c.add(f'<rect x="{x+40}" y="250" width="190" height="16" rx="6" fill="#8D6E63"/><rect x="{x+60}" y="266" width="12" height="50" fill="#8D6E63"/><rect x="{x+198}" y="266" width="12" height="50" fill="#8D6E63"/>')
    person(c, x + 120, 128, 1.25, CTX, droop=True)
    clock(c, x + 215, 92, 40, 11, 15, CTX)
    T(c, x + 60, 100, "...", 40, True, SOFT)
    for i, x in enumerate(xs):
        T(c, x + w / 2, 394, caps[i][0], 28, True, cols[i], "middle")
        T(c, x + w / 2, 428, caps[i][1], 18, False, INK, "middle")
    c.render("f-rohan.png")

# ---------------------------------------------------------------- first guess
def firstguess():
    c = Canvas(1200, 560)
    nodes = [("Late nights", "ic-clock", PUZ), ("Skipped\nbreakfast", "ic-toggle", PEO), ("Food\nwasted", "ic-bin", CAU), ("11 AM energy\ncrash", "ic-warning", TST), ("A second meal\nat the canteen", "ic-coin", NEU)]
    w, h, gap = 176, 150, 70
    x0 = 30
    pos = [(x0 + i * (w + gap), 250) for i in range(5)]
    for (lab, ic, col), (x, y) in zip(nodes, pos):
        card(c, x, y, w, h, col, "white", 24)
        icon(c, ic, x + w / 2, y + 44, 30, col)
        TL(c, x + w / 2, y + 108, lab.split("\n"), 19, True, INK)
    # early class input
    ex, ey = pos[1][0], 60
    card(c, ex, ey, w, 100, CTX, "white", 24, 3, "9 7")
    icon(c, "ic-building", ex + 40, ey + 50, 24, CTX)
    TL(c, ex + 112, ey + 44, ["8:30", "class"], 19, True, INK)
    arrow(c, ex + w / 2, ey + 102, ex + w / 2, 246, CTX, 4, "8 6")
    circ(c, ex + w / 2 + 40, 200, 22, "#FFF3E0", TST, 3); T(c, ex + w / 2 + 40, 210, "?", 28, True, TST, "middle")
    for i in range(4):
        x1 = pos[i][0] + w + 4; x2 = pos[i + 1][0] - 6; y = pos[i][1] + h / 2
        dash = None if i == 0 else "9 7"
        arrow(c, x1, y, x2, y, "#37474F" if i == 0 else SOFT, 5, dash)
        mx = (x1 + x2) / 2
        if i == 0:
            circ(c, mx, y - 38, 24, "#2E7D32"); c.add(f'<path d="M {mx-11} {y-38} L {mx-3} {y-29} L {mx+12} {y-48}" fill="none" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            circ(c, mx, y - 38, 24, "#FFF3E0", TST, 3); T(c, mx, y - 28, "?", 30, True, TST, "middle")
    T(c, 30, 470, "Evidence in hand:", 20, True, INK); 
    circ(c, 250, 464, 13, "#2E7D32"); T(c, 272, 470, "one student told us", 19, False, INK)
    circ(c, 520, 464, 13, "#FFF3E0", TST, 3); T(c, 544, 470, "a link we had not checked", 19, False, INK)
    T(c, 30, 515, "Our first interview was with ourselves.", 19, False, SOFT, italic=True)
    c.render("f-firstguess.png")

# ---------------------------------------------------------------- edge
def edge():
    c = Canvas(1200, 940)
    cx, cy = 600, 470
    card(c, 10, 10, 1180, 920, "#B0BEC5", "#F5F7F9", 40, 2, "10 8")
    T(c, 40, 52, "OUTSIDE THE EDGE", 18, True, SOFT)
    # edge ring
    c.add(f'<ellipse cx="{cx}" cy="{cy}" rx="430" ry="340" fill="white" stroke="{NEU}" stroke-width="7" stroke-dasharray="22 12"/>')
    layers = [(380, 296, PEO, "#F3E5F5", "Rules and money: the committee, the dining office, the warden", 124), (290, 222, SYS, "#E0F2F1", "Kitchens: three firms cook and serve", 0), (190, 140, CTX, "#E3F2FD", "", 0)]
    for rx, ry, col, fill, lab, _ in layers:
        c.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{col}" stroke-width="4"/>')
    T(c, cx, cy - 296 + 40, "Rules and money", 21, True, PEO, "middle")
    T(c, cx, cy - 296 + 62, "committee, dining office, warden", 17, False, PEO, "middle")
    T(c, cx, cy - 222 + 38, "Kitchens", 21, True, SYS, "middle")
    T(c, cx, cy - 222 + 60, "three firms cook and serve", 17, False, SYS, "middle")
    icon(c, "ic-qr", cx - 70, cy - 20, 34, CTX); icon(c, "ic-coin", cx, cy - 20, 34, CTX); icon(c, "ic-phone", cx + 70, cy - 20, 34, CTX)
    T(c, cx, cy + 56, "Booking and billing", 22, True, CTX, "middle")
    T(c, cx, cy + 82, "portal, bill, scan at the counter", 17, False, CTX, "middle")
    # edge actors on the ring
    ea = [(-155, "ic-truck", "Suppliers"), (-100, "ic-bin", "Garbage\ncontractor"), (-20, "ic-chat", "Site team"), (35, "ic-thermometer", "Quality\ncheck"), (150, "ic-people", "People outside\nthe booking")]
    for deg, ic, lab in ea:
        a = math.radians(deg)
        x = cx + 430 * math.cos(a); y = cy + 340 * math.sin(a)
        icon(c, ic, x, y, 30, NEU)
        c.add(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="33" fill="none" stroke="white" stroke-width="4"/>')
        lines = lab.split("\n")
        # label outside
        ox = x + (50 if math.cos(a) > 0 else -50); anc = "start" if math.cos(a) > 0 else "end"
        if abs(math.cos(a)) < 0.35: ox = x; anc = "middle"
        oy = y - 44 if math.sin(a) < 0 else y + 56
        if abs(math.cos(a)) >= 0.35: oy = y - 4 - (len(lines) - 1) * 10
        if lab.startswith('Garbage'): ox = x - 50; anc = 'end'; oy = y - 4 - 10
        TL(c, ox, oy, lines, 17, True, INK, anc, 1.2)
    T(c, cx + 520, 110, "", 10)
    # outside actors
    icon(c, "ic-building", 140, 140, 34, PUZ); TL(c, 140, 200, ["Class timetable", "run by someone else"], 17, True, INK)
    icon(c, "ic-bowl", 1060, 140, 34, PUZ); TL(c, 1060, 200, ["Other places", "to eat"], 17, True, INK)
    T(c, 60, 905, "The edge is a choice. We drew it at breakfast.", 20, False, SOFT, italic=True)
    c.render("f-edge.png")

# ---------------------------------------------------------------- default
def default():
    c = Canvas(1200, 560)
    # checkbox
    card(c, 30, 70, 360, 380, CTX, "#F4F9FF", 26)
    T(c, 210, 118, "Every meal", 24, True, CTX, "middle")
    c.add(f'<rect x="100" y="150" width="220" height="150" rx="26" fill="white" stroke="{CTX}" stroke-width="8"/>')
    c.add(f'<path d="M 140 228 L 190 276 L 285 180" fill="none" stroke="#2E7D32" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>')
    T(c, 210, 345, "Booked", 34, True, INK, "middle")
    TL(c, 210, 384, ["already ticked,", "on campus or not"], 19, False, INK)
    # exits
    card(c, 420, 70, 360, 380, PEO, "#FBF4FD", 26)
    T(c, 600, 118, "The only way out", 24, True, PEO, "middle")
    for i in range(5):
        x = 470 + (i % 3) * 100; y = 190 + (i // 3) * 100
        circ(c, x + 30, y + 30, 40, "white", PEO, 5); T(c, x + 30, y + 44, str(i + 1), 36, True, PEO, "middle")
    TL(c, 600, 400, ["5 cancellations a month,", "each 4 days ahead"], 19, True, INK)
    # skip + resale
    card(c, 810, 70, 360, 190, "#B0BEC5", "#F5F7F9", 26)
    c.add(f'<rect x="880" y="104" width="220" height="64" rx="32" fill="#CFD8DC"/>')
    T(c, 990, 146, "Skip Meal", 28, True, "#90A4AE", "middle")
    TL(c, 990, 208, ["tells the kitchen,", "returns nothing"], 19, False, SOFT)
    card(c, 810, 290, 360, 160, "#2E7D32", "#F1F8F2", 26)
    c.add(f'<path d="M 850 330 h 270 a 20 20 0 0 1 20 20 v 48 a 20 20 0 0 1 -20 20 h -170 l -40 32 v -32 h -60 a 20 20 0 0 1 -20 -20 v -48 a 20 20 0 0 1 20 -20 Z" fill="#DCEFD9"/>')
    TL(c, 990, 362, ["“Selling my", "breakfast today”"], 20, True, "#1B5E20")
    T(c, 990, 478, "student WhatsApp group", 17, False, SOFT, "middle")
    c.render("f-default.png")

# ---------------------------------------------------------------- cast
def cast():
    c = Canvas(1200, 1040)
    cx, cy = 600, 500
    rings = [(300, 190, PEO, "#F8F0FB"), (470, 310, SYS, "#EFF8F6"), (575, 420, CAU, "#FDF1F6")]
    for rx, ry, col, fill in reversed(rings):
        c.add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{col}" stroke-width="3.5"/>')
    icon(c, "ic-person", cx, cy - 6, 56, PUZ); T(c, cx, cy + 92, "Students", 24, True, PUZ, "middle")
    r1 = [("Kadamba\nfirm", "ic-pot"), ("Bakul\nfirm", "ic-truck"), ("Yuktāhār\nfirm", "ic-book"), ("Site\nmanagers", "ic-eye"), ("Serving\nstaff", "ic-people"), ("Kitchen\nstaff", "ic-pot"), ("Mess\ncommittee", "ic-briefcase"), ("Dining\noffice", "ic-gear"), ("Site\nteam", "ic-chat"), ("Warden", "ic-shield"), ("Parliament\nseats", "ic-cap")]
    r2 = [("Academic\nadmin", "ic-building"), ("Event\norganisers", "ic-calendar-x"), ("Facilities\nteam", "ic-gear"), ("Portal and\nIT owner", "ic-phone"), ("Suppliers", "ic-truck"), ("Garbage\ncontractor", "ic-bin"), ("Outside\ndiners", "ic-people"), ("Canteens", "ic-bowl"), ("Delivery\napps", "ic-truck")]
    r3 = [("Mess Cell", "ic-chat", 150), ("Tool\ndevelopers", "ic-phone", 90), ("Ping", "ic-chat", 30)]
    def place(items, rx, ry, col, start, rr):
        n = len(items)
        for i, it in enumerate(items):
            a = math.radians(start + i * 360 / n)
            x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
            icon(c, it[1], x, y, rr, col)
            TL(c, x, y + rr + 20, it[0].split("\n"), 17, True, INK, "middle", 1.15, True)
    place(r1, 300, 190, PEO, -90 + 360 / 22, 25)
    place(r2, 470, 310, SYS, -90 + 20, 27)
    for lab, ic, deg in r3:
        a = math.radians(deg); x, y = cx + 575 * math.cos(a), cy + 420 * math.sin(a)
        icon(c, ic, x, y, 27, CAU); TL(c, x, y + 47, lab.split("\n"), 17, True, INK, "middle", 1.15, True)
    for i, (lab, col) in enumerate([("Inside the system", PEO), ("At its edge", SYS), ("Informal, no standing", CAU)]):
        circ(c, 40, 44 + i * 34, 10, col); T(c, 60, 50 + i * 34, lab, 18, True, col)
    T(c, 1170, 1010, "24 in all", 20, True, SOFT, "end")
    c.render("f-cast.png")

# ---------------------------------------------------------------- missing
def missing():
    c = Canvas(1200, 640)
    for x, title, col in [(20, "The first map", NEU), (620, "The second map", SYS)]:
        card(c, x, 20, 560, 600, col, "#FAFBFC", 26, 3)
        T(c, x + 24, 66, title, 26, True, col)
    # left
    def box(x, y, w, h, lab, col, fill="white", dash=None, fs=18):
        card(c, x, y, w, h, col, fill, 14, 3, dash); TL(c, x + w / 2, y + h / 2 + fs * 0.35 - (len(lab.split(chr(10))) - 1) * fs * 0.6, lab.split("\n"), fs, True, INK)
    box(40, 110, 170, 70, "Students", PUZ); box(40 + 190, 110, 170, 70, "Committee", PEO); box(40 + 380, 110, 140, 70, "Warden", PEO)
    box(40, 210, 520 - 20, 70, "Dining office and its rules", PEO)
    box(40, 340, 520 - 20, 150, "Vendors", NEU, "#ECEFF1", None, 28)
    T(c, 300, 540, "one grey box", 20, False, SOFT, "middle")
    # right
    box(640, 110, 170, 70, "Students", PUZ); box(640 + 190, 110, 170, 70, "Committee", PEO); box(640 + 380, 110, 140, 70, "Warden", PEO)
    box(640, 210, 520, 70, "Dining office and its rules", PEO)
    for i, (n, ic) in enumerate([("Kadamba\nfirm", "ic-pot"), ("Bakul\nfirm", "ic-truck"), ("Yuktāhār\nfirm", "ic-book")]):
        x = 640 + i * 178
        card(c, x, 320, 164, 170, SYS, "#E8F5F1", 18, 4)
        icon(c, ic, x + 82, 372, 28, SYS); TL(c, x + 82, 438, n.split("\n"), 19, True, INK)
    card(c, 640, 516, 520, 80, TST, "#FFF4E8", 18, 3, "9 7")
    icon(c, "ic-people", 690, 556, 26, TST); T(c, 730, 562, "Outside diners eat from the same pots", 19, True, INK)
    c.pill(690, 302, "NEW: three firms", "amber", 16); c.pill(1090, 556, "NEW", "amber", 16)
    T(c, 900, 600, "", 10)
    c.render("f-missing.png")

# ---------------------------------------------------------------- power grid
def power_grid():
    c = Canvas(1200, 840)
    x0, y0, w, h = 140, 50, 1020, 640
    for (qx, qy, col, lab, anc) in [(0, 0, "#F3E5F5", "Keep satisfied", "start"), (1, 0, "#E8EAF6", "Manage closely", "end"), (0, 1, "#F5F7F9", "Monitor", "start"), (1, 1, "#FFF3E0", "Keep informed", "end")]:
        c.add(f'<rect x="{x0+qx*w/2}" y="{y0+qy*h/2}" width="{w/2}" height="{h/2}" fill="{col}"/>')
        T(c, x0 + qx * w / 2 + (16 if anc == "start" else w / 2 - 16), y0 + qy * h / 2 + 34, lab, 20, True, SOFT, anc)
    c.add(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="#90A4AE" stroke-width="3"/>')
    c.add(f'<line x1="{x0+w/2}" y1="{y0}" x2="{x0+w/2}" y2="{y0+h}" stroke="#B0BEC5" stroke-width="2" stroke-dasharray="8 6"/><line x1="{x0}" y1="{y0+h/2}" x2="{x0+w}" y2="{y0+h/2}" stroke="#B0BEC5" stroke-width="2" stroke-dasharray="8 6"/>')
    T(c, x0 + w / 2, y0 + h + 44, "How much they care about breakfast  \u2192", 20, True, INK, "middle")
    c.add(f'<text x="70" y="{y0+h/2}" font-size="20" font-weight="800" fill="{INK}" text-anchor="middle" transform="rotate(-90 70 {y0+h/2})">How much they can decide  \u2192</text>')
    pts = [(0.62, 0.84, "Dining office", PEO, "start"), (0.55, 0.70, "Mess committee", PEO, "start"), (0.06, 0.86, "Academic office", NEU, "start"), (0.12, 0.66, "Quality inspectors", NEU, "start"),
           (0.34, 0.60, "Warden", PEO, "start"), (0.88, 0.57, "Caterers: power over quantity only", SYS, "end"), (0.97, 0.11, "Students", PUZ, "end"), (0.74, 0.22, "Mess Cell", CAU, "end"),
           (0.46, 0.14, "Ping", CAU, "end"), (0.17, 0.30, "Outside diners", TST, "start")]
    for fx, fy, lab, col, anc in pts:
        x, y = x0 + fx * w, y0 + (1 - fy) * h
        circ(c, x, y, 15, col, "white", 4)
        T(c, x + (24 if anc == "start" else -24), y + 7, lab, 19, True, INK, anc)
    T(c, 140, 790, "Placed by judgement. Where an actor sits matters more than the exact spot.", 19, False, SOFT, italic=True)
    c.render("f-power-grid.png")

# ---------------------------------------------------------------- knows / decides
def knows_decides():
    c = Canvas(1200, 660)
    card(c, 20, 30, 430, 520, SYS, "#EFF8F6", 28)
    T(c, 235, 84, "Who knows the gap", 26, True, SYS, "middle")
    for i, (ic, lab) in enumerate([("ic-book", "Kitchens, in their own books"), ("ic-chart", "Dining team, in the scans")]):
        y = 190 + i * 170
        icon(c, ic, 110, y, 44, SYS); TL(c, 270, y - 6, lab.split(", "), 21, True, INK, "middle")
    card(c, 750, 30, 430, 520, PEO, "#F8F0FB", 28)
    T(c, 965, 84, "Who sets the rules", 26, True, PEO, "middle")
    for i, (ic, lab) in enumerate([("ic-briefcase", "Menu committee"), ("ic-gear", "Dining office"), ("ic-shield", "Warden")]):
        y = 175 + i * 120
        icon(c, ic, 840, y, 38, PEO); T(c, 900, y + 8, lab, 22, True, INK)
    # broken bridge
    c.add(f'<rect x="450" y="300" width="130" height="22" fill="#78909C"/><rect x="620" y="300" width="130" height="22" fill="#78909C"/>')
    c.add(f'<rect x="470" y="322" width="16" height="90" fill="#90A4AE"/><rect x="714" y="322" width="16" height="90" fill="#90A4AE"/>')
    c.add(f'<path d="M 450 440 q 30 -16 60 0 t 60 0 t 60 0 t 60 0 t 60 0" fill="none" stroke="#90CAF9" stroke-width="6"/>')
    c.add(f'<path d="M 585 288 l 14 -26 l 6 20 l 14 -10 l -8 30 Z" fill="{CAU}"/>')
    c.pill(600, 480, "no route", "red", fs=22)
    T(c, 600, 600, "The people who see the gap cannot touch its cause.", 21, True, INK, "middle")
    c.render("f-knows-decides.png")

# ---------------------------------------------------------------- morning strip
def morning_strip():
    c = Canvas(1200, 480)
    sc = [("Wake", "ic-clock", False), ("Check\nthe app?", "ic-phone", True), ("Go or\nskip?", "ic-toggle", True), ("Cancel?", "ic-calendar-x", True), ("Resell?", "ic-chat", True), ("Arrive\nlate", "ic-person", False), ("Door\ncloses", "ic-door", False)]
    w, g = 148, 22
    y = 150
    c.add(f'<line x1="30" y1="{y+80}" x2="1170" y2="{y+80}" stroke="#DDE3EA" stroke-width="10" stroke-linecap="round"/>')
    for i, (lab, ic, dec) in enumerate(sc):
        x = 14 + i * (w + g)
        col = PRO if not dec else PEO
        card(c, x, y, w, 160, col, "white", 24, 4)
        icon(c, ic, x + w / 2, y + 56, 34, col)
        TL(c, x + w / 2, y + 126, lab.split("\n"), 20, True, INK, "middle", 1.15)
        if dec:
            c.add(f'<path d="M {x+w/2} {y-44} l 24 22 l -24 22 l -24 -22 Z" fill="{TST}"/>')
            T(c, x + w / 2, y - 14, "?", 24, True, "white", "middle")
        T(c, x + w / 2, y + 196, f"{i+1}", 20, True, SOFT, "middle")
    # bracket last minute
    bx1 = 14 + 5 * (w + g); bx2 = 14 + 7 * (w + g) - g
    c.add(f'<path d="M {bx1} 380 v 14 h {bx2-bx1} v -14" fill="none" stroke="{CAU}" stroke-width="5"/>')
    T(c, (bx1 + bx2) / 2, 430, "the last minute", 22, True, CAU, "middle")
    c.add(f'<path d="M 14 380 v 14 h {5*(w+g)-g-0} v -14" fill="none" stroke="{SOFT}" stroke-width="5"/>')
    T(c, (14 + 5 * (w + g)) / 2, 430, "the long morning", 22, True, SOFT, "middle")
    c.add(f'<path d="M 24 90 l 22 20 l -22 20 l -22 -20 Z" fill="{TST}" transform="translate(14,-70)"/>')
    T(c, 90, 62, "= a decision", 20, True, TST)
    c.render("f-morning-strip.png")

# ---------------------------------------------------------------- three ways
def three_ways():
    c = Canvas(1200, 560)
    ks = [("Kadamba", "ic-pot", SYS, "A fixed share of the booking", "ic-scale", "A supervisor tops up at the counter", "ic-eye"),
          ("Bakul", "ic-truck", PRO, "A weekly judgement by the manager", "ic-person", "Food is driven in from far away", "ic-truck"),
          ("Yuktāhār", "ic-book", CTX, "Reads its own books", "ic-book", "Plans from the same menu day, two weeks ago", "ic-calendar-x")]
    w, g = 370, 25
    for i, (name, ic, col, l1, i1, l2, i2) in enumerate(ks):
        x = 20 + i * (w + g)
        card(c, x, 30, w, 480, col, "white", 28, 4)
        c.add(f'<rect x="{x}" y="30" width="{w}" height="120" rx="28" fill="{col}"/><rect x="{x}" y="100" width="{w}" height="50" fill="{col}"/>')
        icon(c, ic, x + 70, 90, 38, "white", False)
        c.add(f'<use href="#{ic}" x="{x+70-24}" y="{90-24}" width="48" height="48" fill="{col}"/>')
        T(c, x + 130, 102, name, 32, True, "white")
        for j, (ii, lab) in enumerate([(i1, l1), (i2, l2)]):
            yy = 220 + j * 150
            icon(c, ii, x + 56, yy, 30, col)
            TL(c, x + 110, yy - 6, wrap(lab, 230, 21, True), 21, True, INK, "start", 1.2)
    c.render("f-three-ways.png")

if __name__ == "__main__":
    which = sys.argv[1:] or ["journey", "rohan", "firstguess", "edge", "default"]
    for w in which: globals()[w]()
