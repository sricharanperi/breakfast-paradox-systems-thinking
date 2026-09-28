"""Activity 9, Deliverable 1: Leverage-Point / System Intervention Map.

Hand-composed SVG (systems-visual-design skill, svgkit.py), rasterised through
headless Chrome. The core booking-to-bin chain runs left to right in the middle,
records and money sit above it, governance at the top, absorbers below. Each
leverage point is a numbered marker coloured by its depth in the leverage
hierarchy; held levers have a dashed ring. Dashed red lines are routes that do
not exist today and that a leverage point would build.
"""
import sys, math
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render, label_box

OUT = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-3/assets/diagram-a9-leverage-intervention-map.png"

W, H = 2400, 1500
FONT = 'font-family="Helvetica,Arial,sans-serif"'

# node palette (project standard)
STU = "#e65100"; PROC = "#1565c0"; GOV = "#00695c"; SOC = "#6a1b9a"
EXT = "#616161"; RED = "#c62828"; GREEN = "#2e7d32"; MISSING = "#c62828"
FLOW = "#455a64"

# leverage depth colours (deeper = darker / cooler)
DEPTH = {
    3: ("#4a148c", "Level 3: goals of the system"),
    4: ("#ad1457", "Level 4: self-organisation"),
    5: ("#b71c1c", "Level 5: rules of the system"),
    6: ("#0d47a1", "Level 6: information flows"),
    8: ("#2e7d32", "Level 8: balancing feedback loops"),
    9: ("#ef6c00", "Level 9: delays"),
}

body = []
LABELS = []

def text(x, y, s, size=13, weight="400", color="#222", anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}"{st}>{s}</text>'

def band(y, h, label, color, fill):
    out = f'<rect x="20" y="{y}" width="{W-40}" height="{h}" rx="18" fill="{fill}" stroke="{color}" stroke-width="1.4" stroke-opacity="0.45"/>'
    lw = len(label)*9.6 + 24
    LABELS.append(f'<rect x="30" y="{y+8}" width="{lw:.0f}" height="26" rx="8" fill="{fill}"/>' + text(40, y+26, label, 14, "800", color))
    return out

def marker(cx, cy, n, level, held=False):
    c = DEPTH[level][0]
    out = ""
    if held:
        out += f'<circle cx="{cx}" cy="{cy}" r="31" fill="white" stroke="{c}" stroke-width="2.4" stroke-dasharray="5 4"/>'
        out += f'<circle cx="{cx}" cy="{cy}" r="24" fill="{c}" fill-opacity="0.55"/>'
    else:
        out += f'<circle cx="{cx}" cy="{cy}" r="27" fill="white"/>'
        out += f'<circle cx="{cx}" cy="{cy}" r="24" fill="{c}"/>'
    out += text(cx, cy+5, f"LP{n}", 14, "900", "white", "middle")
    return out

def pill(cx, cy, s, color="#37474f"):
    w = len(s)*7.2 + 22
    return (f'<rect x="{cx-w/2:.1f}" y="{cy-13}" width="{w:.1f}" height="26" rx="13" fill="{color}"/>'
            + text(cx, cy+5, s, 12.5, "700", "white", "middle"))

def looptag(cx, cy, s):
    return text(cx, cy, s, 12, "700", "#6a1b9a", "middle", italic=True)

def callout(x, y, lines, color):
    w = max(len(l) for l in lines)*6.4 + 20
    h = 10 + 16*len(lines)
    out = f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h}" rx="8" fill="white" stroke="{color}" stroke-width="1.3"/>'
    for k, l in enumerate(lines):
        out += text(x+10, y+20+16*k, l, 11.5, "600" if k == 0 else "400", "#222" if k else color)
    return out

# ---------------------------------------------------------------- title
body.append(text(40, 52, "Leverage-Point / System Intervention Map", 30, "800", "#1a237e"))
body.append(text(40, 82, "IIIT Hyderabad breakfast mess system: where each leverage point acts on the booking-to-bin chain, coloured by depth", 15, "400", "#555"))

# ---------------------------------------------------------------- bands
GOV_Y, REC_Y, CH_Y, ABS_Y = 225, 455, 700, 955
body.append(band(120, 190, "GOVERNANCE AND RULE OWNERS", GOV, "#f1f8f7"))
body.append(band(345, 200, "RECORDS AND MONEY", "#37474f", "#f7f8fa"))
body.append(band(580, 235, "THE BOOKING-TO-BIN CHAIN (ONE BREAKFAST)", PROC, "#f3f8fe"))
body.append(band(835, 190, "WHERE THE SURPLUS GOES", SOC, "#faf5fc"))

# ---------------------------------------------------------------- governance row
gov = [
    (420,  "ic-building", "Rule owner", "CDS / Mess Office, head open", GOV),
    (900,  "ic-people",   "Escalation forum", "Council, Parliament, Committee", GOV),
    (1380, "ic-chat",     "Menu committee", "selects the two-week menu", GOV),
    (1860, "ic-briefcase","Operator management", "Prism ops manager; ABC PMs", GOV),
]
for x, ic, l1, l2, c in gov:
    body.append(chip(x, GOV_Y, ic, l1, l2, c, w=280, h=80))
    body.append(pill(x, GOV_Y-58, "IP13" if x < 1100 else "IP14"))

# ---------------------------------------------------------------- records row
rec = [
    (170,  "ic-coin",     "Student bill", "fires at the booking", STU),
    (500,  "ic-coin",     "Vendor payment", "on plates, basis unknown", EXT),
    (830,  "ic-calendar-x","Academic calendar", "exams, events, holidays", EXT),
    (1490, "ic-qr",       "CDS scan export", "one row per registration", PROC),
    (1820, "ic-briefcase","Operator books", "Yuktāhār set; Kadamba gram standards", PROC),
]
for x, ic, l1, l2, c in rec:
    body.append(chip(x, REC_Y, ic, l1, l2, c, w=290 if x == 1820 else 270, h=80))

# ---------------------------------------------------------------- chain row
chain = [
    (170,  "ic-toggle",  "Default registration", "every student, automatic", STU, "IP1: cycle start", "L13"),
    (500,  "ic-phone",   "Exit and portal count", "5 cancellations, 4 days out", STU, "IP2 to IP3: T-4 to T-1", "L13, L2"),
    (830,  "ic-clock",   "Day-before plan", "70% ratio or book lookup", PROC, "IP4: T-1", "L11 at Yuktāhār only"),
    (1160, "ic-shield",  "First batch cooked", "safety checks, tasting", PROC, "IP5 to IP6: 5:30 to 7:30", "L13"),
    (1490, "ic-pot",     "Service and top-up", "crest in 9:15 to 9:30", PROC, "IP7 to IP9: 7:30 to 9:30+", "L12, L14, L15"),
    (1820, "ic-bowl",    "Surplus after close", "held, reheated, routed", SOC, "IP10 to IP11: after close", "L9, L17, L13 branch"),
    (2150, "ic-warning", "Bin", "garbage contractor", RED, "IP12: disposal", "exit, not absorber"),
]
CW = 270
for x, ic, l1, l2, c, tt, lt in chain:
    body.append(pill(x, CH_Y+58, tt))
    body.append(chip(x, CH_Y, ic, l1, l2, c, w=CW, h=80))
    body.append(looptag(x, CH_Y+94, lt))

colors = {FLOW, MISSING, GREEN, STU, PROC, EXT}
for i in range(len(chain)-1):
    x1 = chain[i][0] + CW/2 + 2
    x2 = chain[i+1][0] - CW/2 - 4
    body.append(straight_arrow(x1, CH_Y, x2, CH_Y, FLOW, width=5))

# chain -> records (solid, existing flows)
body.append(straight_arrow(170, CH_Y-40, 170, REC_Y+42, STU, width=3.5))
body.append(straight_arrow(1490, CH_Y-40, 1490, REC_Y+42, PROC, width=3.5))
body.append(straight_arrow(1820, CH_Y-40, 1820, REC_Y+42, PROC, width=3.5))
# vendor payment follows the count (basis unknown) : dotted grey
body.append(straight_arrow(500, CH_Y-40, 500, REC_Y+42, EXT, width=3, dash="4 4"))

# ---------------------------------------------------------------- existing learning loop and missing routes
# LP5: books -> day-before plan (exists at Yuktahar, absent at Kadamba)
body.append(curved_arrow(1668, REC_Y+30, 900, CH_Y-40, GREEN, bend=-0.10, width=4, dash="10 6"))
# calendar -> day-before plan (missing formal feed)
body.append(straight_arrow(830, REC_Y+42, 830, CH_Y-42, MISSING, width=3.5, dash="9 6"))
# LP1: records -> rule owner (missing)
body.append(curved_arrow(1430, REC_Y-42, 540, GOV_Y+42, MISSING, bend=0.06, width=4, dash="10 7"))
# LP7: quantity line at the tasting -> escalation forum (missing)
body.append(curved_arrow(1120, CH_Y-40, 930, GOV_Y+42, MISSING, bend=0.05, width=3.5, dash="10 7"))
# LP8: item waste -> menu committee (missing, L16 absent)
body.append(curved_arrow(1780, REC_Y-42, 1420, GOV_Y+42, MISSING, bend=-0.08, width=3.5, dash="10 7"))
# LP4: Yuktahar books as template -> operator management / other operators
body.append(curved_arrow(1900, REC_Y-42, 1890, GOV_Y+42, MISSING, bend=-0.25, width=3.5, dash="10 7"))

# ---------------------------------------------------------------- absorber row
body.append(straight_arrow(1820, CH_Y+102, 1820, ABS_Y-88, SOC, width=4))
protect = [
    (500,  "ic-phone",  "Resale on Mess Cell", "student recovers money", GREEN),
    (830,  "ic-people", "Outside diners, half of staff", "30 to 50 people, ~30 portions", GREEN),
    (1160, "ic-pot",    "Reuse into later meals", "idli upma, curd, batter", GREEN),
    (1490, "ic-clock",  "Late and back-door service", "about 37 scans a day after 9:30", GREEN),
]
targets = [
    (1820, "ic-warning", "Repeated reheating", "quality cost (candidate)", RED),
    (2150, "ic-warning", "Over-cooked first batch", "and the bin", RED),
]
body.append(text(345, ABS_Y-50, "PROTECT, BY PLAN", 12.5, "800", GREEN))
body.append(text(1690, ABS_Y-50, "LEGITIMATE TARGETS", 12.5, "800", RED))
for x, ic, l1, l2, c in protect + targets:
    body.append(chip(x, ABS_Y, ic, l1, l2, c, w=300 if x == 830 else 280, h=80))

# ---------------------------------------------------------------- leverage markers
LP = {}
def put(n, x, y, level, held=False):
    body.append(marker(x, y, n, level, held))

put(2, 335, CH_Y-2, 5)                 # between default and exit
put(10, 335, REC_Y-2, 5, held=True)    # between student bill and vendor payment
put(9, 560, GOV_Y-52, 5, held=True)    # on rule owner
put(1, 1180, 372, 6)                    # on the records -> rule owner route
put(1, 830, 580, 6)                    # on the calendar feed (same lever, downward route)
put(7, 1042, 405, 5)                   # on the tasting -> forum route
put(5, 1250, 598, 8)                   # on the learning link into the plan
put(6, 1612, CH_Y-40, 9)               # on service and top-up
put(8, 1560, 330, 5)                   # on item waste -> menu committee
put(4, 1975, 330, 4)                   # books as template
put(3, 2045, GOV_Y, 3)                 # on operator management
put(5, 963, CH_Y+28, 8)                # also sits on the plan itself

# short callouts on the missing routes
body.append(callout(580, 318, ["Missing route", "records never reach a rule owner"], MISSING))
body.append(callout(1070, 437, ["Quantity line", "at the per-meal tasting"], MISSING))
body.append(callout(1268, 612, ["Learning loop", "runs at Yuktāhār only"], GREEN))

# ---------------------------------------------------------------- legend: depth
LY = 1070
body.append(f'<rect x="20" y="{LY}" width="610" height="400" rx="18" fill="white" stroke="#bdbdbd"/>')
body.append(text(40, LY+32, "Depth of each leverage point", 16, "800", "#1a237e"))
body.append(text(40, LY+52, "Lower level number = deeper lever; 12 is the shallowest", 12, "400", "#555"))
yy = LY+88
for lvl in [3, 4, 5, 6, 8, 9]:
    c, lab = DEPTH[lvl]
    body.append(f'<circle cx="62" cy="{yy}" r="15" fill="{c}"/>')
    body.append(text(92, yy+5, lab, 13.5, "600", "#222"))
    yy += 40
body.append(f'<circle cx="62" cy="{yy}" r="17" fill="white" stroke="#555" stroke-width="2" stroke-dasharray="5 4"/><circle cx="62" cy="{yy}" r="12" fill="#b71c1c" fill-opacity="0.55"/>')
body.append(text(92, yy+5, "Dashed ring: held until a gating fact is known", 13.5, "600", "#222"))
yy += 34
body.append(text(40, yy+5, "Level 12 (parameters, e.g. the 70% ratio) appears only as an output of LP5.", 12, "400", "#555", italic=True))

# ---------------------------------------------------------------- legend: key
KX = 660
body.append(f'<rect x="{KX}" y="{LY}" width="1150" height="400" rx="18" fill="white" stroke="#bdbdbd"/>')
body.append(text(KX+20, LY+32, "Leverage points", 16, "800", "#1a237e"))
key = [
    (1, 6, "Build the missing routes: the gap upward, the calendar downward"),
    (2, 5, "Change the breakfast default and its exit"),
    (3, 3, "Operator goal: surplus is a cost"),
    (4, 4, "Operator-to-operator practice exchange"),
    (5, 8, "Record-calibrated first batch with a daily learning record"),
    (6, 9, "Crest-aware top-up and a staged late batch"),
    (7, 5, "A cost trigger for attention, on the oversight line"),
    (8, 5, "Operator voice in the menu"),
    (9, 5, "A named owner of booked, cooked and eaten (held)"),
    (10, 5, "What a booking costs: billing and payment basis (held)"),
]
for k, (n, lvl, lab) in enumerate(key):
    col = 0 if k < 5 else 1
    row = k % 5
    x = KX + 40 + col*560
    y = LY + 80 + row*62
    c = DEPTH[lvl][0]
    held = n in (9, 10)
    if held:
        body.append(f'<circle cx="{x}" cy="{y}" r="21" fill="white" stroke="{c}" stroke-width="2" stroke-dasharray="4 3"/><circle cx="{x}" cy="{y}" r="16" fill="{c}" fill-opacity="0.55"/>')
    else:
        body.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{c}"/>')
    body.append(text(x, y+4, f"LP{n}", 11, "900", "white", "middle"))
    words = lab.split(" ")
    # wrap at ~44 chars
    lines, cur = [], ""
    for w_ in words:
        if len(cur) + len(w_) + 1 > 44:
            lines.append(cur); cur = w_
        else:
            cur = (cur + " " + w_).strip()
    lines.append(cur)
    for j, ln in enumerate(lines):
        body.append(text(x+32, y-2+j*17 - (8 if len(lines) > 1 else -2), ln, 13.5, "600", "#222"))

# ---------------------------------------------------------------- legend: lines
RX = 1840
body.append(f'<rect x="{RX}" y="{LY}" width="540" height="400" rx="18" fill="white" stroke="#bdbdbd"/>')
body.append(text(RX+20, LY+32, "Lines", 16, "800", "#1a237e"))
ly = LY+80
body.append(f'<line x1="{RX+30}" y1="{ly}" x2="{RX+120}" y2="{ly}" stroke="{FLOW}" stroke-width="5" marker-end="url(#arrow-{FLOW[1:]})"/>')
body.append(text(RX+140, ly+5, "Flow that exists today", 13.5, "600"))
ly += 50
body.append(f'<line x1="{RX+30}" y1="{ly}" x2="{RX+120}" y2="{ly}" stroke="{MISSING}" stroke-width="4" stroke-dasharray="10 7" marker-end="url(#arrow-{MISSING[1:]})"/>')
body.append(text(RX+140, ly+5, "Route that does not exist today", 13.5, "600"))
body.append(text(RX+140, ly+23, "and that a leverage point would build", 12.5, "400", "#444"))
ly += 60
body.append(f'<line x1="{RX+30}" y1="{ly}" x2="{RX+120}" y2="{ly}" stroke="{GREEN}" stroke-width="4" stroke-dasharray="10 6" marker-end="url(#arrow-{GREEN[1:]})"/>')
body.append(text(RX+140, ly+5, "Learning link: present at Yuktāhār,", 13.5, "600"))
body.append(text(RX+140, ly+23, "absent at Kadamba", 12.5, "400", "#444"))
ly += 60
body.append(f'<line x1="{RX+30}" y1="{ly}" x2="{RX+120}" y2="{ly}" stroke="{EXT}" stroke-width="3" stroke-dasharray="4 4" marker-end="url(#arrow-{EXT[1:]})"/>')
body.append(text(RX+140, ly+5, "Link whose basis is unknown", 13.5, "600"))
ly += 50
body.append(text(RX+30, ly+5, "L-numbers: loop or chain IDs from", 12.5, "600", "#6a1b9a", italic=True))
body.append(text(RX+30, ly+23, "the Causal Loop and Feedback Analysis", 12.5, "600", "#6a1b9a", italic=True))

body.extend(LABELS)
svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(sorted(colors | {SOC})))
render(svg, OUT, W, H)
