import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

DES, TEST, NEU, RED, AMB, GRN = "#283593", "#EF6C00", "#455A64", "#C62828", "#E08600", "#2E7D32"
INK = "#22262B"

def rect(c, x, y, w, h, fill, stroke=None, r=14, sw=2.4, dash=False, op=1.0):
    st = f'stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    d = 'stroke-dasharray="8 6"' if dash else ""
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" fill-opacity="{op}" {st} {d}/>')

def circ(c, cx, cy, r, fill, stroke=None, sw=0):
    st = f'stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    c.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" {st}/>')

def icon(c, name, cx, cy, size, color="white"):
    c.add(f'<use href="#{name}" x="{cx-size/2}" y="{cy-size/2}" width="{size}" height="{size}" fill="{color}"/>')

def txt(c, x, y, s, fs=18, bold=False, color=INK, anchor="start", width=None, lh=1.25):
    return c.text(x, y, s, fs=fs, bold=bold, color=color, anchor=anchor, width=width, lh=lh)

# ------------------------------------------------------------ f-depth
def depth():
    W, H = 1200, 960
    c = Canvas(W, H)
    c.add(f'<text x="40" y="52" font-size="30" font-weight="800" fill="{DES}">Twelve places to push, from deepest to shallowest</text>')
    names = ["Paradigm: the way of thinking itself", "Mindset: the beliefs", "Goals: what the system is for", "Self-organisation: who can change the structure",
             "Rules: who decides, what it costs", "Information flows: who knows what", "Reinforcing loops", "Balancing loops",
             "Delays", "Stocks and flows", "Buffers", "Parameters: numbers and ratios"]
    lps = {2: [("LP11", 0)], 3: [("LP3", 0), ("LP12", 0)], 4: [("LP4", 0)], 5: [("LP2", 0), ("LP9", 1), ("LP10", 1)],
           6: [("LP1", 0), ("LP5", 0), ("LP6", 0), ("LP8", 0)], 8: [("LP3", 0), ("LP5", 0), ("LP7", 0)], 10: [("LP6", 0)]}
    top, rh = 100, 62
    for i in range(12):
        p = i + 1
        y = top + i * rh
        t = i / 11.0
        # colour: deep indigo to pale
        col = "#%02X%02X%02X" % (int(0x28 + (0xB0 - 0x28) * t), int(0x35 + (0xB8 - 0x35) * t), int(0x93 + (0xE6 - 0x93) * t))
        x0 = 40 + i * 14
        rect(c, x0, y, 640 - i * 14, rh - 8, col, None, r=10)
        circ(c, x0 + 30, y + (rh - 8) / 2, 20, "white")
        txt(c, x0 + 30, y + (rh - 8) / 2 + 7, str(p), 20, True, DES, "middle")
        tc = "white" if t < 0.55 else INK
        txt(c, x0 + 62, y + (rh - 8) / 2 + 7, names[i], 18, False, tc)
        cx = 720
        if p in lps:
            for lab, held in lps[p]:
                w = 82 if lab not in ("LP10", "LP11", "LP12") else 90
                if held:
                    rect(c, cx, y + 6, w, rh - 20, "white", AMB, 12, 2.6, True)
                    txt(c, cx + w / 2, y + 34, lab, 18, True, AMB, "middle")
                else:
                    rect(c, cx, y + 6, w, rh - 20, DES, None, 12)
                    txt(c, cx + w / 2, y + 34, lab, 18, True, "white", "middle")
                cx += w + 10
        else:
            txt(c, 720, y + 34, "no lever here", 16, False, "#9AA5B1")
    # side arrows
    c.add(f'<text x="1160" y="140" font-size="18" font-weight="700" fill="{DES}" text-anchor="end">deeper, harder,</text><text x="1160" y="162" font-size="18" font-weight="700" fill="{DES}" text-anchor="end">stronger</text>')
    c.add(f'<text x="1160" y="{top+12*rh-30}" font-size="18" font-weight="700" fill="{NEU}" text-anchor="end">shallower,</text><text x="1160" y="{top+12*rh-8}" font-size="18" font-weight="700" fill="{NEU}" text-anchor="end">easier</text>')
    rect(c, 720, top + 12 * rh + 6, 20, 14, "white", AMB, 4, 2.2, True)
    txt(c, 750, top + 12 * rh + 19, "dashed = held until facts are known", 16, False, NEU)
    c.render("f-depth.png")

# ------------------------------------------------------------ f-principles
def principles():
    W, H = 1200, 780
    c = Canvas(W, H)
    c.add(f'<text x="40" y="52" font-size="30" font-weight="800" fill="{DES}">Seven rules every idea must pass</text>')
    P = [("P1", "Route before you measure", "The records exist. Connect them first.", "ic-book"),
         ("P2", "Make measurement blame-free", "No figure is used against the person who recorded it.", "ic-shield"),
         ("P3", "Change the default, the goal and the belief", "Not the people.", "ic-toggle"),
         ("P4", "Act on the first batch the day before", "Mornings work only through the top-up.", "ic-clock"),
         ("P5", "Feed the absorbers by plan", "Name who eats the surplus.", "ic-people"),
         ("P6", "Judge by cooked against eaten, run-outs and quality", "Not by turnout.", "ic-pot"),
         ("P7", "Use several measures, never one target", "One number can be gamed.", "ic-scale")]
    cw, ch = 265, 290
    pos = []
    for i in range(7):
        r, k = divmod(i, 4)
        if r == 0: x = 40 + k * 285
        else: x = 40 + k * 285 + 142
        pos.append((x, 100 + r * 320))
    for (p, rule, sub, ic), (x, y) in zip(P, pos):
        rect(c, x, y, cw, ch, "#EEF0FA", DES, 18, 2.6)
        circ(c, x + 52, y + 56, 34, DES)
        txt(c, x + 52, y + 66, p, 26, True, "white", "middle")
        icon(c, ic, x + cw - 56, y + 56, 54, DES)
        h = txt(c, x + 22, y + 138, rule, 21, True, INK, width=cw - 44)
        txt(c, x + 22, y + 138 + h + 14, sub, 18, False, NEU, width=cw - 44)
    c.render("f-principles.png")

# ------------------------------------------------------------ f-concepts
def concepts():
    W, H = 1200, 860
    c = Canvas(W, H)
    c.add(f'<text x="40" y="52" font-size="30" font-weight="800" fill="{DES}">Eight concepts, and the lever each one pulls</text>')
    K = [("A", "The Breakfast Ledger", "One weekly sheet merging scans and kitchen books, with the money charged.", "LP1  LP7", DES),
         ("B", "The Kitchen Learning Kit", "A plan card and daily sheet for Kadamba, with a named staff allowance.", "LP3  LP4  LP5", TEST),
         ("C", "The Crest Plan", "A 9:00 late batch that lands before the crowd.", "LP6", TEST),
         ("D", "The Sunday Exit", "A Sunday skip that really removes the charge.", "LP2", DES),
         ("E", "The Operator Menu Slot", "Operators bring what wastes and runs out. A voice, not authority.", "LP8", DES),
         ("F", "Billed at Consumption", "Charge on the scan. Held until the payment basis is known.", "LP10", AMB),
         ("G", "The Ratio Cut", "Cut the first batch to 50% by order.", "no lever", RED),
         ("H", "The Shared Reading", "Each person reads their own number beside the record.", "LP11  LP12", DES)]
    cw, chh = 270, 340
    for i, (l, name, what, lp, col) in enumerate(K):
        r, k = divmod(i, 4)
        x, y = 40 + k * 285, 100 + r * 365
        fill = "#FDECEA" if l == "G" else "white"
        rect(c, x, y, cw, chh, fill, col, 18, 3, dash=(l == "F"))
        circ(c, x + 44, y + 48, 30, col)
        txt(c, x + 44, y + 58, l, 28, True, "white", "middle")
        h = txt(c, x + 20, y + 112, name, 21, True, INK, width=cw - 40)
        h2 = txt(c, x + 20, y + 112 + h + 12, what, 17, False, NEU, width=cw - 40)
        rect(c, x + 20, y + chh - 62, cw - 40, 40, col, None, 20)
        txt(c, x + cw / 2, y + chh - 35, lp, 18, True, "white", "middle")
        if l == "G":
            c.add(f'<line x1="{x+18}" y1="{y+18}" x2="{x+cw-18}" y2="{y+chh-18}" stroke="{RED}" stroke-width="5" opacity="0.28"/><line x1="{x+cw-18}" y1="{y+18}" x2="{x+18}" y2="{y+chh-18}" stroke="{RED}" stroke-width="5" opacity="0.28"/>')
            rect(c, x + cw - 120, y + 22, 100, 34, "white", RED, 10, 2.5)
            txt(c, x + cw - 70, y + 46, "the foil", 18, True, RED, "middle")
        if l == "F":
            txt(c, x + cw - 20, y + 36, "held", 18, True, AMB, "end")
    c.render("f-concepts.png")

# ------------------------------------------------------------ f-scores
def scores():
    W, H = 1200, 960
    c = Canvas(W, H)
    c.add(f'<text x="40" y="52" font-size="30" font-weight="800" fill="{DES}">How the concepts scored (out of 100)</text>')
    rows = [("Re-sequenced bundle", 79, "pass", "passes all four gates"), ("First-draft bundle", 79, "fail", "fails gate 4"),
            ("A  Breakfast Ledger", 68, "pass", ""), ("H  Shared Reading", 65, "pass", ""), ("F  Billed at consumption", 63, "held", "fails gate 3, held"),
            ("C  Crest Plan, alone", 63, "fail", "fails gate 4"), ("D  Sunday skip, ratio kept", 60, "pass", ""), ("E  Operator Menu Slot", 60, "pass", ""),
            ("B  Kitchen Kit, alone", 58, "fail", "fails gate 4"), ("D  every-day skip", 50, "pass", ""), ("G  Ratio cut to 50%", 48, "fail", "fails gate 1 and P4")]
    x0, bw, top, rh = 400, 460, 100, 62
    col = {"pass": DES, "fail": RED, "held": AMB}
    for i, (lab, v, g, note) in enumerate(rows):
        y = top + i * rh + (24 if i >= 2 else 0)
        txt(c, x0 - 16, y + 31, lab, 19, i < 2, INK, "end")
        w = v / 100 * bw
        rect(c, x0, y + 6, w, 40, col[g], None, 8, op=1 if g != "held" else 0.9)
        txt(c, x0 + w + 12, y + 36, str(v), 22, True, INK)
        if note: txt(c, x0 + w + 62, y + 35, note, 17, False, col[g] if g != "pass" else NEU)
    c.add(f'<line x1="{x0}" y1="{top}" x2="{x0}" y2="{top+11*rh+30}" stroke="#90A4AE" stroke-width="2"/>')
    rect(c, 40, top + 11 * rh + 50, 1120, 70, "#F3F4F8", DES, 12, 2)
    txt(c, 60, top + 11 * rh + 92, "Two bundles tie at 79. A score cannot see order. The gates can.", 20, True, DES)
    # legend
    lx = 40
    for lab, cc in [("passes the gates", DES), ("fails a gate", RED), ("held", AMB)]:
        rect(c, lx, 66, 24, 18, cc, None, 4); txt(c, lx + 34, 82, lab, 17, False, NEU); lx += 210
    c.render("f-scores.png")

# ------------------------------------------------------------ f-responses
def responses():
    W, H = 1200, 1000
    c = Canvas(W, H)
    c.add(f'<text x="40" y="50" font-size="30" font-weight="800" fill="{DES}">How we expect people to react</text>')
    c.add(f'<text x="40" y="82" font-size="18" fill="{NEU}">Expectations, not feedback. Nobody has been asked yet.</text>')
    cols = ["Ledger", "Kitchen kit + crest plan", "Sunday exit", "Shared reading"]
    W_, T_, R_ = "w", "t", "r"
    rows = [("Near-daily eaters", [T_, W_, T_, T_]), ("Sunday and frequent skippers", [T_, T_, W_, T_]), ("Mess Cell resellers", [T_, T_, T_, T_]),
            ("Prism, Kadamba management", [T_, W_, R_, T_]), ("Kadamba supervisor and staff", [T_, T_, T_, T_]), ("Bakul operator", [T_, R_, T_, T_]),
            ("Yuktāhār operator", [W_, W_, W_, T_]), ("Dining office (CDS)", [T_, W_, T_, T_]), ("Facilities head (CFS)", [W_, T_, W_, W_]),
            ("Student representatives", [W_, T_, W_, W_]), ("Outside diners and staff", [T_, T_, T_, T_]), ("Facility team at the tasting", [T_, T_, T_, T_])]
    lx, cx0, cw, top, rh = 40, 480, 175, 140, 60
    for j, cn in enumerate(cols):
        x = cx0 + j * cw
        rect(c, x + 6, top - 44, cw - 12, 40, DES, None, 10)
        txt(c, x + cw / 2, top - 17, cn if len(cn) < 14 else cn.replace("Kitchen kit + crest plan", "Kitchen kit"), 17, True, "white", "middle")
    c.add(f'<text x="{cx0+cw*1.5:.0f}" y="{top-52}" font-size="1" fill="white"> </text>')
    for i, (lab, cells) in enumerate(rows):
        y = top + i * rh
        if i % 2 == 0: rect(c, 30, y, 1140, rh - 4, "#F3F4F8", None, 8)
        txt(c, lx + 8, y + 36, lab, 19, False, INK)
        for j, s in enumerate(cells):
            cx = cx0 + j * cw + cw / 2; cy = y + 26
            if s == W_:
                circ(c, cx, cy, 20, GRN); c.add(f'<path d="M {cx-9} {cy} L {cx-2} {cy+8} L {cx+10} {cy-8}" fill="none" stroke="white" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
            elif s == T_:
                circ(c, cx, cy, 20, "#CFD8DC"); c.add(f'<line x1="{cx-9}" y1="{cy}" x2="{cx+9}" y2="{cy}" stroke="{NEU}" stroke-width="5" stroke-linecap="round"/>')
            else:
                circ(c, cx, cy, 20, RED); c.add(f'<path d="M {cx-8} {cy-8} L {cx+8} {cy+8} M {cx+8} {cy-8} L {cx-8} {cy+8}" stroke="white" stroke-width="5" stroke-linecap="round"/>')
    ly = top + 12 * rh + 24
    for k, (lab, kind) in enumerate([("would welcome it", W_), ("would tolerate it, or barely notice", T_), ("would resist it", R_)]):
        x = 60 + k * 330
        if kind == W_: circ(c, x, ly, 14, GRN)
        elif kind == T_: circ(c, x, ly, 14, "#CFD8DC")
        else: circ(c, x, ly, 14, RED)
        txt(c, x + 26, ly + 6, lab, 17, False, NEU)
    txt(c, 40, ly + 46, "Prism resists a skip only if paid on booked plates. The Bakul operator resists any run-out risk.", 17, False, NEU)
    c.render("f-responses.png")

# ------------------------------------------------------------ f-sequence
def sequence():
    W, H = 1200, 640
    c = Canvas(W, H)
    c.add(f'<text x="40" y="52" font-size="30" font-weight="800" fill="{DES}">Twenty weeks, three stages, dates that do not move</text>')
    x0, x1 = 70, 1130
    wk = lambda w: x0 + w * (x1 - x0) / 20.0
    stages = [(0, 4, "Stage 1", "Weeks 0 to 4", "Build the Ledger. Test with students and cooks. Joint reading.", DES),
              (4, 8, "Stage 2", "Weeks 5 to 8", "Propose the Sunday skip. Pilot at Kadamba.", TEST),
              (8, 20, "Stage 3", "Weeks 9 to 20", "Skip in force from about week 10. Roll out. Hand over.", GRN)]
    for a_, b_, nm, wks, desc, col in stages:
        rect(c, wk(a_) + 3, 90, wk(b_) - wk(a_) - 6, 190, col, None, 16, op=0.12)
        rect(c, wk(a_) + 3, 90, wk(b_) - wk(a_) - 6, 12, col, None, 6)
        txt(c, wk(a_) + 20, 140, nm, 24, True, col)
        txt(c, wk(a_) + 20, 166, wks, 17, True, NEU)
        txt(c, wk(a_) + 20, 198, desc, 18, False, INK, width=wk(b_) - wk(a_) - 40)
    ay = 370
    c.add(f'<line x1="{x0}" y1="{ay}" x2="{x1}" y2="{ay}" stroke="{NEU}" stroke-width="5" stroke-linecap="round"/>')
    for w in range(0, 21, 2):
        c.add(f'<line x1="{wk(w)}" y1="{ay-8}" x2="{wk(w)}" y2="{ay+8}" stroke="{NEU}" stroke-width="3"/><text x="{wk(w)}" y="{ay+32}" font-size="16" fill="{NEU}" text-anchor="middle">{w}</text>')
    txt(c, x0 - 30, ay + 58, "week", 16, False, NEU)
    # above-axis decision points
    for w, lab in [(6, "DP1: Sunday skip proposed"), (14, "DP2: every-day skip decided")]:
        x = wk(w)
        c.add(f'<polygon points="{x},{ay-16} {x+16},{ay} {x},{ay+16} {x-16},{ay}" fill="{RED}"/>')
        c.add(f'<line x1="{x}" y1="{ay-18}" x2="{x}" y2="{ay-48}" stroke="{RED}" stroke-width="2.5"/>')
        txt(c, x, ay - 84, lab, 17, True, RED, "middle", width=190)
    # below-axis milestones
    for w, lab, col, anc in [(10, "Skip in force, about week 10", GRN, "middle"), (16, "Handover begins", DES, "middle"), (20, "We step back", DES, "end")]:
        x = wk(w)
        c.add(f'<polygon points="{x},{ay-16} {x+16},{ay} {x},{ay+16} {x-16},{ay}" fill="{col}"/>')
        c.add(f'<line x1="{x}" y1="{ay+44}" x2="{x}" y2="{ay+78}" stroke="{col}" stroke-width="2.5"/>')
        txt(c, x + (0 if anc == "middle" else 16), ay + 104, lab, 17, True, col, anc, width=170 if anc == "middle" else 150)
    rect(c, 60, 520, 1080, 76, "white", AMB, 14, 3, True)
    txt(c, 84, 551, "Held until the facts are known", 20, True, AMB)
    txt(c, 84, 579, "billing at consumption   ·   an owner of the whole outcome   ·   anything sized for Bakul", 17, False, NEU)
    c.render("f-sequence.png")

# ------------------------------------------------------------ f-believed-found
def believed():
    W, H = 1200, 1160
    c = Canvas(W, H)
    c.add(f'<text x="40" y="50" font-size="30" font-weight="800" fill="{RED}">Ten things we believed, and what the evidence said</text>')
    R = [("About 30% of bookings go unused", "63% to 72% go unused", 6),
         ("A forecast four days ahead sets the cooking", "Kitchens set quantities the day before", 5),
         ("Leftovers are composted", "No composting at Kadamba", 5),
         ("20 to 30 staff eat the leftovers", "About 30 portions for 30 to 50 outsiders, plus half the staff", 5),
         ("Friends pull each other to breakfast", "Not a deciding factor", 5),
         ("The operators are one actor", "Three firms, three ways of working", 5),
         ("Every operator distrusts the booking", "Only Yuktāhār does", 9),
         ("Cuisine explains low uptake", "Not on the evidence: item and line matter", 9),
         ("Six of our loops were closed", "Three close", 8),
         ("Skip Meal reaches the kitchen", "In conflict: Kadamba says it cooks on bookings alone", 8)]
    top, rh = 120, 102
    txt(c, 60, top - 14, "WE BELIEVED", 17, True, RED)
    txt(c, 640, top - 14, "THE EVIDENCE SAID", 17, True, GRN)
    txt(c, 1128, top - 14, "CHAPTER", 17, True, NEU, "end")
    for i, (a, b, ch) in enumerate(R):
        y = top + i * rh
        rect(c, 40, y, 510, rh - 14, "#FDECEA", RED, 14, 2.4)
        n1 = len(wrap(a, 470, 20)); txt(c, 62, y + (rh - 14) / 2 + 7 - (n1 - 1) * 12, a, 20, False, INK, width=470)
        c.add(f'<path d="M 560 {y+(rh-14)/2} L 618 {y+(rh-14)/2}" stroke="{NEU}" stroke-width="4" marker-end="url(#ar-455A64)"/>')
        c.use_color("#455A64")
        rect(c, 630, y, 480, rh - 14, "#E8F5E9", GRN, 14, 2.4)
        n2 = len(wrap(b, 440, 20, True)); txt(c, 652, y + (rh - 14) / 2 + 7 - (n2 - 1) * 12, b, 20, True, INK, width=440)
        circ(c, 1142, y + (rh - 14) / 2, 22, NEU)
        txt(c, 1142, y + (rh - 14) / 2 + 8, str(ch), 22, True, "white", "middle")
    c.render("f-believed-found.png")

# ------------------------------------------------------------ f-open
def openq():
    W, H = 1200, 690
    c = Canvas(W, H)
    c.add(f'<text x="40" y="52" font-size="30" font-weight="800" fill="{AMB}">What nobody knows yet, and who could tell us</text>')
    G = [("Contract holders", "ic-plate", ["What does a plate mean in each operator's payment, booked or served?"]),
         ("Rule owners", "ic-building", ["Who set the four-day close and the limit of five?", "Who heads the dining body? Two names are on record.", "Which booking rule applied to Yuktāhār in June?"]),
         ("Kitchens", "ic-pot", ["Does Skip Meal reach Kadamba's kitchen?", "What is the 5 to 10% waste figure a percentage of?", "Can a 9:00 late batch avoid slowing the crest?", "Bakul: any written record? How long is a top-up?"]),
         ("Our own tests", "ic-chat", ["How many students would take a Sunday skip? We assumed a quarter to a half.", "Do the planned co-design tests agree with us? None has run."])]
    cw = 540
    for i, (nm, ic, qs) in enumerate(G):
        r, k = divmod(i, 2)
        x, y = 40 + k * 580, 100 + r * 280
        h = 250 if r == 0 else 295
        rect(c, x, y, cw, h, "#FFF8E1", AMB, 18, 3, True)
        circ(c, x + 46, y + 48, 30, AMB); txt(c, x + 46, y + 61, '?', 38, True, 'white', 'middle')
        txt(c, x + 92, y + 58, nm, 24, True, INK)
        yy = y + 106
        for q in qs:
            hh = txt(c, x + 28, yy + 14, "?  " + q, 18, False, INK, width=cw - 56)
            yy += hh + 14
    c.render("f-open.png")

if __name__ == "__main__":
    depth(); principles(); concepts(); scores(); responses(); sequence(); believed(); openq()
