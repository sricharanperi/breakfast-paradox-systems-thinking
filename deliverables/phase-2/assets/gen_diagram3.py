import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render

W, H = 1800, 1450
USERS_C = "#e65100"; USERS_F = "#fff3e0"
TECH_C  = "#1565c0"; TECH_F  = "#e3f2fd"
BIZ_C   = "#00695c"; BIZ_F   = "#e0f2f1"
SOC_C   = "#6a1b9a"; SOC_F   = "#f3e5f5"
HUB_C   = "#1a237e"
HX, HY, HR = 900, 720, 125

body = []
body.append('<text x="40" y="52" font-size="34" font-weight="800" fill="#e8590c">System Map</text>')
body.append('<text x="40" y="80" font-size="16" fill="#555">Users, Technology, Business &amp; Social/Environmental Factors — IIIT Hyderabad Breakfast Mess System</text>')

body.append(f'<ellipse cx="{HX}" cy="260" rx="650" ry="190" fill="{USERS_F}" stroke="{USERS_C}" stroke-width="2" stroke-dasharray="2 6"/>')
body.append(f'<ellipse cx="1560" cy="{HY}" rx="230" ry="470" fill="{TECH_F}" stroke="{TECH_C}" stroke-width="2" stroke-dasharray="2 6"/>')
body.append(f'<ellipse cx="{HX}" cy="1180" rx="650" ry="180" fill="{BIZ_F}" stroke="{BIZ_C}" stroke-width="2" stroke-dasharray="2 6"/>')
body.append(f'<ellipse cx="240" cy="{HY}" rx="230" ry="470" fill="{SOC_F}" stroke="{SOC_C}" stroke-width="2" stroke-dasharray="2 6"/>')

body.append(f'<text x="{HX}" y="42" text-anchor="middle" font-size="19" font-weight="800" fill="{USERS_C}">USERS</text>')
body.append('<text x="1560" y="218" text-anchor="middle" font-size="19" font-weight="800" fill="' + TECH_C + '">TECHNOLOGY COMPONENTS</text>')
body.append(f'<text x="{HX}" y="1412" text-anchor="middle" font-size="19" font-weight="800" fill="{BIZ_C}">BUSINESS FACTORS</text>')
body.append('<text x="240" y="218" text-anchor="middle" font-size="19" font-weight="800" fill="' + SOC_C + '">SOCIAL / ENVIRONMENTAL FACTORS</text>')

body.append(f'<circle cx="{HX}" cy="{HY}" r="{HR}" fill="url(#hubGrad)" stroke="#0d1257" stroke-width="3"/>')
body.append(f'<text x="{HX}" y="{HY-8}" text-anchor="middle" font-size="20" font-weight="800" fill="white">IIIT-H Breakfast</text>')
body.append(f'<text x="{HX}" y="{HY+20}" text-anchor="middle" font-size="20" font-weight="800" fill="white">Mess System</text>')

body.append(straight_arrow(HX, HY-HR, HX, 450, USERS_C, "registers / scans / rates via"))
body.append(straight_arrow(HX+HR, HY, 1330, HY, TECH_C, "runs on, logs to"))
body.append(straight_arrow(HX, HY+HR, HX, 1000, BIZ_C, "billed &amp; procured under"))
body.append(straight_arrow(HX-HR, HY, 470, HY, SOC_C, "shaped by schedule &amp; culture"))

users_x = [480, 760, 1040, 1320]
users_nodes = [
    ("ic-person", "Students", "registrant &amp; consumer"),
    ("ic-people", "Mess Office staff", "daily operators"),
    ("ic-pot", "Vendors / kitchen", "food preparers"),
    ("ic-shield", "Warden", "vendor &amp; structural mgmt"),
]
for x, (icon, l1, l2) in zip(users_x, users_nodes):
    body.append(chip(x, 260, icon, l1, l2, USERS_C))

tech_y = [300, 510, 720, 930, 1140]
tech_nodes = [
    ("ic-phone", "Registration portal", "&amp; billing"),
    ("ic-qr", "Personal QR credential", "counter access"),
    ("ic-chat", "In-app rating feature", ""),
    ("ic-toggle", "Skip Meal toggle", "no refund"),
    ("ic-calendar-x", "Cancellation flow", "capped 5/month"),
]
for y, (icon, l1, l2) in zip(tech_y, tech_nodes):
    body.append(chip(1560, y, icon, l1, l2, TECH_C, w=250))

biz_x = [480, 760, 1040, 1320]
biz_nodes = [
    ("ic-coin", "Billing = registration", "not attendance"),
    ("ic-clock", "4-day procurement", "lead time"),
    ("ic-building", "Per-mess capacities", "registered limits"),
    ("ic-briefcase", "Vendor contracts", "&amp; compensation"),
]
for x, (icon, l1, l2) in zip(biz_x, biz_nodes):
    body.append(chip(x, 1180, icon, l1, l2, BIZ_C))

soc_y = [300, 510, 720, 930, 1140]
soc_nodes = [
    ("ic-clock", "8:30 AM class start", "external, Academic Admin."),
    ("ic-bowl", "Cuisine preference", "Kadamba demand"),
    ("ic-people", "Peer presence", "weak motivator"),
    ("ic-warning", "Institutional pattern:", "complaint until crisis"),
    ("ic-building", "Four separate kitchens", "physical infrastructure"),
]
for y, (icon, l1, l2) in zip(soc_y, soc_nodes):
    body.append(chip(240, y, icon, l1, l2, SOC_C, w=250))

# Intra-zone interconnections -- relationships between elements INSIDE the
# same category, each grounded in an already-confirmed Phase 1/2 finding.
# Short adjacent links are left unlabeled (the gap between neighbouring chips
# has no room for label text without overlapping one of them); longer links
# that cross open canvas keep their label.
GREY = "#9e9e9e"

# Users: registration/billing and forecast/contract chains within the zone
body.append(curved_arrow(480+105, 275, 760-105, 275, USERS_C, bend=-0.15, width=2.6))
body.append(curved_arrow(760+105, 275, 1040-105, 275, USERS_C, bend=-0.15, width=2.6))
body.append(curved_arrow(1320-105, 275, 1040+105, 275, USERS_C, bend=0.15, width=2.6))
body.append(curved_arrow(1320-105, 235, 760+105, 235, GREY, "relationship unconfirmed", bend=-0.55, width=2, dash="4 5"))

# Technology: everything is a feature of the one registration portal
for y in [510, 720, 930, 1140]:
    body.append(curved_arrow(1560+125, 300+10, 1560+125, y, TECH_C, bend=0.32, width=2.2))

# Business: registration, capacity and contracts all converge on the 4-day forecast
body.append(curved_arrow(480+105, 1195, 760-105, 1195, BIZ_C, bend=-0.15, width=2.6))
body.append(curved_arrow(1040-105, 1195, 760+105, 1195, BIZ_C, bend=0.15, width=2.6))
body.append(curved_arrow(1320-105, 1210, 760+105, 1210, BIZ_C, "governs", bend=0.55, width=2.2))

# Social/Environmental: cuisine culture and institutional pattern both tie to the four kitchens
body.append(curved_arrow(240, 930+39, 240, 1140-39, SOC_C, "Kadamba incident precedent", bend=0.32, width=2.6))
body.append(curved_arrow(115, 495, 115, 1125, SOC_C, bend=0.15, width=2.2))

lx, ly = 1500, 1230
body.append(f'<rect x="{lx}" y="{ly}" width="270" height="140" rx="10" fill="white" stroke="#999" stroke-width="1.4"/>')
body.append(f'<text x="{lx+14}" y="{ly+22}" font-size="13" font-weight="800" fill="#222">Legend</text>')
for i, (c, label) in enumerate([(USERS_C,"Users"), (TECH_C,"Technology"), (BIZ_C,"Business"), (SOC_C,"Social/Environmental")]):
    yy = ly + 40 + i*23
    body.append(f'<rect x="{lx+14}" y="{yy-11}" width="16" height="16" rx="3" fill="{c}"/>')
    body.append(f'<text x="{lx+38}" y="{yy+1}" font-size="12" fill="#333">{label}</text>')

extra_defs = f'<radialGradient id="hubGrad" cx="35%" cy="30%" r="80%"><stop offset="0%" stop-color="#5c6bc0"/><stop offset="100%" stop-color="{HUB_C}"/></radialGradient>' + marker_defs([USERS_C, TECH_C, BIZ_C, SOC_C, GREY])
svg = wrap_svg(W, H, "\n".join(body), extra_defs=extra_defs)
render(svg, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/diagram3-mapping-sprint-quadrants.png", W, H)
