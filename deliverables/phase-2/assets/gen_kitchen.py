import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render

W, H = 2000, 1400
SUPPLY_C, SUPPLY_F = "#1565c0", "#e3f2fd"
EQUIP_C, EQUIP_F = "#00695c", "#e0f2f1"
INV_C, INV_F = "#e65100", "#fff3e0"
WASTE_C, WASTE_F = "#6a1b9a", "#f3e5f5"
WARN_C = "#c62828"
GREEN = "#2e7d32"

body = []
body.append('<text x="40" y="55" font-size="34" font-weight="800" fill="#e8590c">Kitchen and Supply Subsystem</text>')
body.append('<text x="40" y="82" font-size="16" fill="#555">Kadamba (on-site kitchen) — supply chain, equipment, inventory, waste and food safety, as one interacting system</text>')

HX, HY = 1000, 700
body.append(f'<circle cx="{HX}" cy="{HY}" r="105" fill="url(#hubGrad2)" stroke="#0d3b2e" stroke-width="3"/>')
body.append(f'<text x="{HX}" y="{HY-8}" text-anchor="middle" font-size="18" font-weight="800" fill="white">Kadamba Kitchen</text>')
body.append(f'<text x="{HX}" y="{HY+16}" text-anchor="middle" font-size="13" fill="white">(on-site)</text>')

# Supply chain zone (top)
body.append(f'<ellipse cx="{HX}" cy="230" rx="560" ry="170" fill="{SUPPLY_F}" stroke="{SUPPLY_C}" stroke-width="2" stroke-dasharray="2 6"/>')
body.append(f'<text x="{HX}" y="55" text-anchor="middle" font-size="17" font-weight="800" fill="{SUPPLY_C}">SUPPLY CHAIN</text>')
sx = [500, 780, 1220, 1500]
supply_nodes = [
    ("ic-briefcase", "Outsourced catering", "via open tender"),
    ("ic-calendar-x", "T-4 registration", "locked, sent to vendor"),
    ("ic-clock", "Weekly stock", "assessment"),
    ("ic-coin", "Consumption-pattern", "driven ordering"),
]
for x, (icon, l1, l2) in zip(sx, supply_nodes):
    body.append(chip(x, 230, icon, l1, l2, SUPPLY_C, w=230))
body.append(straight_arrow(sx[0]+115, 230, sx[1]-115, 230, SUPPLY_C, width=3))
body.append(straight_arrow(sx[1]+115, 230, sx[2]-115, 230, SUPPLY_C, width=3))
body.append(straight_arrow(sx[2]+115, 230, sx[3]-115, 230, SUPPLY_C, width=3))
body.append(f'<rect x="{HX-260}" y="330" width="520" height="66" rx="10" fill="white" stroke="{SUPPLY_C}" stroke-width="1.6"/>')
body.append(f'<text x="{HX}" y="352" text-anchor="middle" font-size="12" font-weight="700" fill="#222">Turnout by category: high-demand items &gt;90%,</text>')
body.append(f'<text x="{HX}" y="368" text-anchor="middle" font-size="12" font-weight="700" fill="#222">general ~70%, breakfast specifically only 35-40%</text>')
body.append(straight_arrow(HX, 330, HX, HY-105, SUPPLY_C, width=4))

# Equipment zone (right)
body.append(f'<ellipse cx="1620" cy="{HY}" rx="330" ry="480" fill="{EQUIP_F}" stroke="{EQUIP_C}" stroke-width="2" stroke-dasharray="2 6"/>')
body.append('<text x="1620" y="245" text-anchor="middle" font-size="17" font-weight="800" fill="' + EQUIP_C + '">EQUIPMENT</text>')
ey = [300, 430, 560, 690, 820, 950, 1080]
equip_nodes = [
    ("ic-gear", "Roti line", "mixes, portions, roasts"),
    ("ic-pot", "Multi-item cooker", "veg / non-veg kept separate"),
    ("ic-warning", "Curry / steam machine", "tilts to drain — safer clean"),
    ("ic-toggle", "Sterilizer", "for knives"),
    ("ic-gear", "Chopper + washer", "veg / rice / lentils"),
    ("ic-building", "Butchering section", "mostly unused, meat arrives ready"),
    ("ic-clock", "Prep start", "~5:00 AM, dish-dependent"),
]
for y, (icon, l1, l2) in zip(ey, equip_nodes):
    body.append(chip(1620, y, icon, l1, l2, EQUIP_C, w=280))
body.append(straight_arrow(HX+105, HY-20, 1620-140, 300, EQUIP_C, width=3))

# Inventory zone (left)
body.append(f'<ellipse cx="380" cy="{HY}" rx="330" ry="330" fill="{INV_F}" stroke="{INV_C}" stroke-width="2" stroke-dasharray="2 6"/>')
body.append('<text x="380" y="395" text-anchor="middle" font-size="17" font-weight="800" fill="' + INV_C + '">INVENTORY</text>')
iy = [460, 590, 720]
inv_nodes = [
    ("ic-building", "Cold storage", "milk, curd, veg (walk-in)"),
    ("ic-building", "Dry storage", "rice, lentils, flour, sauces"),
    ("ic-warning", "ONE person manages both", "FIFO + FEFO — single point of failure"),
]
for y, (icon, l1, l2) in zip(iy, inv_nodes):
    c = WARN_C if "ONE" in l1 else INV_C
    body.append(chip(380, y, icon, l1, l2, c, w=280))
body.append(straight_arrow(380, 460+39, 380, 590-39, INV_C, width=2.6))
body.append(straight_arrow(380, 590+39, 380, 720-39, WARN_C, width=2.6))
body.append(straight_arrow(380+220, HY-260, HX-105, HY-30, INV_C, width=3))

# Waste & Safety zone (bottom)
body.append(f'<ellipse cx="{HX}" cy="1170" rx="560" ry="170" fill="{WASTE_F}" stroke="{WASTE_C}" stroke-width="2" stroke-dasharray="2 6"/>')
body.append('<text x="' + str(HX) + '" y="1345" text-anchor="middle" font-size="17" font-weight="800" fill="' + WASTE_C + '">WASTE &amp; FOOD SAFETY</text>')
wx = [500, 780, 1220, 1500]
waste_nodes = [
    ("ic-warning", "Production + plate waste", "split streams"),
    ("ic-people", "Garbage collector", "external"),
    ("ic-building", "Compost facility", "off-site"),
    ("ic-shield", "Contamination sample", "sent to a lab"),
]
for x, (icon, l1, l2) in zip(wx, waste_nodes):
    body.append(chip(x, 1170, icon, l1, l2, WASTE_C, w=230))
body.append(straight_arrow(wx[0]+115, 1170, wx[1]-115, 1170, WASTE_C, width=3))
body.append(straight_arrow(wx[1]+115, 1170, wx[2]-115, 1170, WASTE_C, width=3))
body.append(curved_arrow(HX-60, HY+105, wx[0]+60, 1170-39, WASTE_C, bend=-0.15, width=3))
body.append(curved_arrow(1400, HY+50, wx[3], 1170-39, WASTE_C, "lab test", bend=0.1, width=2.6))
body.append(f'<rect x="{wx[3]-115}" y="1250" width="360" height="60" rx="10" fill="#e8f5e9" stroke="{GREEN}" stroke-width="1.6"/>')
body.append(f'<text x="{wx[3]+65}" y="1272" text-anchor="middle" font-size="12" font-weight="700" fill="{GREEN}">Externally validated:</text>')
body.append(f'<text x="{wx[3]+65}" y="1290" text-anchor="middle" font-size="11.5" fill="{GREEN}">FSSAI &quot;Eat Right Campus&quot; 5-star (Exemplary)</text>')
body.append(straight_arrow(wx[3], 1170+39, wx[3]+65, 1250, GREEN, width=2))

# Off-site note (Bakul/Palash — a DIFFERENT kitchen system, not this one)
body.append(f'<rect x="30" y="1080" width="340" height="130" rx="10" fill="#fafafa" stroke="#9e9e9e" stroke-dasharray="3 3"/>')
body.append('<text x="45" y="1105" font-size="12.5" font-weight="800" fill="#555">Not this system:</text>')
body.append('<text x="45" y="1125" font-size="11.5" fill="#555">Bakul + Palash share ONE separate</text>')
body.append('<text x="45" y="1141" font-size="11.5" fill="#555">off-site kitchen (not Kadamba\'s).</text>')
body.append('<text x="45" y="1161" font-size="11.5" fill="#555">Transitional until Felicity Kitchen</text>')
body.append('<text x="45" y="1177" font-size="11.5" fill="#555">&amp; Dining Facility opens (~Dec 2026).</text>')
body.append('<text x="45" y="1197" font-size="11.5" fill="#555">Yuktahar: on-site, separate again.</text>')

extra = '<radialGradient id="hubGrad2" cx="35%" cy="30%" r="80%"><stop offset="0%" stop-color="#26a69a"/><stop offset="100%" stop-color="#004d40"/></radialGradient>'
colors = [SUPPLY_C, EQUIP_C, INV_C, WASTE_C, WARN_C, GREEN]
svg = wrap_svg(W, H, "\n".join(body), extra_defs=extra + marker_defs(colors))
render(svg, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/diagram13-kitchen-supply-subsystem.png", W, H)
