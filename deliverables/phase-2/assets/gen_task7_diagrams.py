import sys, math
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render, label_box

BASE = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/"

# ---------------------------------------------------------------------------
# 1. ICEBERG MODEL
# ---------------------------------------------------------------------------
W, H = 2000, 1620
body = []
body.append('<text x="40" y="50" font-size="30" font-weight="800" fill="#0d47a1">Iceberg Model — Events to Mental Models</text>')
body.append('<text x="40" y="76" font-size="15" fill="#555">Breakfast Paradox — what is visible above the waterline vs. the structure holding it in place</text>')

bands = [
    (110, 380, "#e3f2fd", "#0d47a1", "EVENTS", "Directly observed"),
    (380, 700, "#bbdefb", "#0d47a1", "PATTERNS", "What keeps recurring"),
    (700, 1080, "#5c9fd8", "#0d3b66", "STRUCTURES", "Rules, timing, decision rights"),
    (1080, 1560, "#0d3b66", "#0d3b66", "MENTAL MODELS", "Beliefs holding structures in place"),
]
for (y0, y1, fill, labelcolor, title, sub) in bands:
    body.append(f'<rect x="0" y="{y0}" width="{W}" height="{y1-y0}" fill="{fill}"/>')

textcolor_by_band = ["#0d47a1", "#0d47a1", "white", "white"]
for i, (y0, y1, fill, labelcolor, title, sub) in enumerate(bands):
    tc = textcolor_by_band[i]
    body.append(f'<text x="40" y="{y0+40}" font-size="20" font-weight="800" fill="{tc}">{title}</text>')
    body.append(f'<text x="40" y="{y0+64}" font-size="13" fill="{tc}" opacity="0.85">{sub}</text>')

body.append(f'<line x1="0" y1="380" x2="{W}" y2="380" stroke="#1565c0" stroke-width="4"/>')
body.append('<text x="1550" y="374" font-size="14" font-weight="700" fill="#0d47a1">WATERLINE — what everyone can see</text>')

EVENT_C = "#0d47a1"
events = [
    ("ic-calendar-x", "Registers daily,", "never attends (n=1)"),
    ("ic-phone", "T-4 sourcing lock,", "same-week prep flexes"),
    ("ic-chat", "Turnout 35-45% for", "breakfast vs 70-90%+"),
    ("ic-warning", "Portal shows two", "different domains"),
    ("ic-shield", "Gap confirmed never", "reaching policy"),
]
ex = [230, 620, 1010, 1400, 1790]
for x, (icon, l1, l2) in zip(ex, events):
    body.append(chip(x, 250, icon, l1, l2, EVENT_C, w=340))

PATTERN_C = "#0d47a1"
patterns = [
    ("ic-coin", "Ghost registration,", "concentrated in breakfast"),
    ("ic-toggle", "Skip Meal mechanism", "works, uptake ~zero"),
    ("ic-people", "Informal resale absorbs", "the demand-side symptom"),
    ("ic-calendar-x", "Shock-adaptive model", "already run, then retired"),
]
px = [280, 780, 1280, 1750]
for x, (icon, l1, l2) in zip(px, patterns):
    body.append(chip(x, 550, icon, l1, l2, PATTERN_C, w=380))

STRUCT_C = "#0d3b66"
structs = [
    ("ic-briefcase", "Billing decoupled", "from attendance"),
    ("ic-clock", "Two-stage pipeline:", "T-4 sourcing + prep-flex"),
    ("ic-building", "3 distinct kitchen", "systems, one label"),
    ("ic-people", "Decision rights split", "4 ways, none owns gap"),
    ("ic-warning", "Waste tracked, never", "fed back to policy"),
]
sx = [220, 640, 1060, 1480, 1850]
for x, (icon, l1, l2) in zip(sx, structs):
    body.append(chip(x, 900, icon, l1, l2, STRUCT_C, w=320, fill="#eaf2fb"))

MM_C = "#ffca28"
mms = [
    ("ic-person", "Students: \"registering costs", "me nothing extra\""),
    ("ic-briefcase", "Institution: \"registration ≈", "demand,\" as standing policy"),
    ("ic-shield", "Institution: \"procurement certainty", "beats demand-matching,\" permanently"),
]
mx = [420, 1000, 1620]
for x, (icon, l1, l2) in zip(mx, mms):
    body.append(chip(x, 1320, icon, l1, l2, "#ffca28", w=480, h=100, fill="white", text_color="#0d3b66"))

body.append('<rect x="600" y="1440" width="800" height="130" rx="10" fill="#08213d" stroke="#ffca28" stroke-width="1.6"/>')
body.append('<text x="1000" y="1470" text-anchor="middle" font-size="14" font-weight="800" fill="#ffca28">The deepest belief is the one most recently confirmed:</text>')
body.append('<text x="1000" y="1495" text-anchor="middle" font-size="12.5" fill="white">the institution treats registration as an adequate demand proxy for procurement,</text>')
body.append('<text x="1000" y="1516" text-anchor="middle" font-size="12.5" fill="white">even though the same office can name the exact size of the gap, and has already</text>')
body.append('<text x="1000" y="1537" text-anchor="middle" font-size="12.5" fill="white">run a working alternative (B4) — proof this is a choice, not an unsolved problem.</text>')

colors = [EVENT_C, STRUCT_C, "#f57f17"]
svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(colors))
render(svg, BASE + "diagram15-iceberg-model.png", W, H)

# ---------------------------------------------------------------------------
# 2. ROOT CAUSE NETWORK
# ---------------------------------------------------------------------------
W2, H2 = 1700, 1500
body2 = []
body2.append('<text x="40" y="50" font-size="28" font-weight="800" fill="#b71c1c">Root Cause Network</text>')
body2.append('<text x="40" y="76" font-size="15" fill="#555">Why the registration-attendance gap persists as a structural outcome, not an oversight</text>')

RC_C = "#b71c1c"
MECH_C = "#e65100"
GAP_C = "#37474f"

cx = 850
nodes = [
    (cx, 180, "ic-briefcase", "RC1 — Billing decoupled", "from attendance (root cause)", RC_C, 480),
    (cx, 380, "ic-coin", "Ghost-registration incentive", "(individual level)", MECH_C, 420),
    (cx, 580, "ic-clock", "RC2 — T-4 sourcing lock", "(compounds RC1, sourcing stage only)", MECH_C, 480),
    (cx, 780, "ic-warning", "Persistent registration-attendance gap", "35-45% breakfast turnout", GAP_C, 560),
    (cx, 980, "ic-chat", "Known precisely to CFS Chair —", "CONFIRMED never reaching policy", GAP_C, 520),
    (cx, 1200, "ic-people", "RC3 — Fragmented decision rights", "(root cause, confirmed as cause of inaction)", RC_C, 560),
]
for (x, y, icon, l1, l2, color, w) in nodes:
    body2.append(chip(x, y, icon, l1, l2, color, w=w))

for i in range(len(nodes) - 1):
    x1, y1 = nodes[i][0], nodes[i][1] + 44
    x2, y2 = nodes[i+1][0], nodes[i+1][1] - 44
    body2.append(straight_arrow(x1, y1, x2, y2, "#616161", width=4))

body2.append(curved_arrow(cx - 240, 1200, cx - 240, 180, "#9e9e9e", "root-caused by", bend=-0.35, width=3, dash="6 5"))

body2.append(chip(1420, 380, "ic-shield", "RC5 — Vendor revenue", "insulation (assumed)", "#6a1b9a", w=340, fill="#f3e5f5"))
body2.append(curved_arrow(1250, 380, 1090, 380, "#6a1b9a", "compounds", bend=0.15, width=3))

body2.append(chip(1420, 980, "ic-toggle", "B5 — Silo success (B3)", "masks the gap (plausible)", "#00838f", w=340, fill="#e0f7fa"))
body2.append(curved_arrow(1250, 980, 1090, 980, "#00838f", "reduces scrutiny", bend=0.15, width=3))

body2.append('<rect x="150" y="1340" width="1400" height="130" rx="10" fill="#fff3e0" stroke="#e65100" stroke-width="1.6"/>')
body2.append('<text x="850" y="1372" text-anchor="middle" font-size="15" font-weight="800" fill="#e65100">The sharpest evidence of RC3\'s severity:</text>')
body2.append('<text x="850" y="1396" text-anchor="middle" font-size="13" fill="#5d4037">the institution already possesses a proven working alternative (loop B4, the shock-adaptive</text>')
body2.append('<text x="850" y="1417" text-anchor="middle" font-size="13" fill="#5d4037">precedent) and has never evaluated it for partial or permanent adoption.</text>')
body2.append('<text x="850" y="1440" text-anchor="middle" font-size="13" fill="#5d4037">Fragmentation is severe enough that even a demonstrated success goes unconnected to the standing-model conversation.</text>')

colors2 = [RC_C, MECH_C, GAP_C, "#616161", "#9e9e9e", "#6a1b9a", "#00838f"]
svg2 = wrap_svg(W2, H2, "\n".join(body2), extra_defs=marker_defs(colors2))
render(svg2, BASE + "diagram16-root-cause-network.png", W2, H2)

# ---------------------------------------------------------------------------
# 3. CONSOLIDATED LOOP OVERVIEW (dashboard)
# ---------------------------------------------------------------------------
W3, H3 = 2000, 620
body3 = []
body3.append('<text x="40" y="45" font-size="26" font-weight="800" fill="#0d47a1">Feedback Loop Overview — 14 Loops/Chains Tracked</text>')
body3.append('<text x="40" y="70" font-size="14" fill="#555">The eight most decision-relevant loops, at a glance — full templates for all fourteen in the supporting assets</text>')

loops = [
    ("ic-qr", "B4", "Shock-Adaptive Registration Relaxation", "Balancing · CONFIRMED (headline)", "#1565c0", "#e3f2fd"),
    ("ic-coin", "R1", "Registration / Resale", "Reinforcing · CONFIRMED", "#5e35b1", "#ede7f6"),
    ("ic-warning", "R6", "Waste Invisibility", "Reinforcing · assumed, mirrors R1", "#6a1b9a", "#f3e5f5"),
    ("ic-bowl", "B3", "Menu Rotation Governance", "Balancing · CONFIRMED, closed", "#00838f", "#e0f7fa"),
    ("ic-chat", "R4", "Known-But-Unowned Gap", "Reinforcing · mostly evidenced", "#37474f", "#eceff1"),
    ("ic-toggle", "B1", "Skip Meal", "Balancing · mechanism works, uptake ~0", "#2e7d32", "#e8f5e9"),
    ("ic-briefcase", "R5", "Vendor Margin / Quality", "Reinforcing · assumed", "#ad1457", "#fce4ec"),
    ("ic-people", "B5", "Silo Success Masking Gap", "Balancing/system-level · plausible", "#e65100", "#fff3e0"),
]

gx = 4
cell_w, cell_h = 480, 240
x0, y0 = 40, 110
for idx, (icon, lid, name, tag, color, fillc) in enumerate(loops):
    col = idx % gx
    row = idx // gx
    cx0 = x0 + col*cell_w
    cy0 = y0 + row*cell_h
    body3.append(f'<rect x="{cx0}" y="{cy0}" width="{cell_w-25}" height="{cell_h-30}" rx="14" fill="{fillc}" stroke="{color}" stroke-width="2.4"/>')
    body3.append(f'<circle cx="{cx0+42}" cy="{cy0+42}" r="24" fill="{color}"/>')
    body3.append(f'<use href="#{icon}" x="{cx0+30}" y="{cy0+30}" width="24" height="24" fill="white"/>')
    body3.append(f'<text x="{cx0+78}" y="{cy0+50}" font-size="19" font-weight="900" fill="{color}">{lid}</text>')
    body3.append(f'<text x="{cx0+25}" y="{cy0+92}" font-size="13.5" font-weight="800" fill="#222">{name}</text>')
    body3.append(f'<text x="{cx0+25}" y="{cy0+116}" font-size="11.5" fill="#444">{tag}</text>')

colors3 = [c for (_,_,_,_,c,_) in loops]
svg3 = wrap_svg(W3, H3, "\n".join(body3), extra_defs=marker_defs(colors3))
render(svg3, BASE + "diagram17-loop-overview-dashboard.png", W3, H3)
