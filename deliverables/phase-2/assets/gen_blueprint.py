import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, marker_defs, wrap_svg, render, label_box

W, H = 2050, 1250
FRONT_C, FRONT_F = "#e65100", "#fff3e0"
BACK_C, BACK_F   = "#1565c0", "#e3f2fd"
SUPP_C, SUPP_F   = "#00695c", "#e0f2f1"
EVID_C, EVID_F   = "#6a1b9a", "#f3e5f5"

stages = ["Registration\n(monthly, in advance)", "T-4 days\n(vendor forecast)", "7:30-9:30 AM\n(service window)", "9:30 AM close\n(reconciliation)", "Ongoing\n(feedback channels)"]
col_x = [290, 700, 1110, 1510, 1900]
lane_y = {"evidence": 200, "front": 380, "los": 470, "back": 620, "support": 850}

body = []
body.append('<text x="40" y="50" font-size="32" font-weight="800" fill="#e8590c">Service Blueprint</text>')
body.append('<text x="40" y="76" font-size="15" fill="#555">Frontstage / backstage / support across the breakfast cycle — IIIT Hyderabad Breakfast Mess System</text>')

# column headers (timeline)
for x, s in zip(col_x, stages):
    lines = s.split("\n")
    body.append(f'<rect x="{x-105}" y="108" width="210" height="50" rx="10" fill="#37474f"/>')
    for k, ln in enumerate(lines):
        body.append(f'<text x="{x}" y="{130+k*17}" text-anchor="middle" font-size="12.5" font-weight="700" fill="white">{ln}</text>')

# lane labels (left margin, stacked two lines to fit before column 1)
def lane_label(x, y, lines, color):
    out = ""
    for k, ln in enumerate(lines):
        out += f'<text x="{x}" y="{y+k*15}" font-size="12" font-weight="800" fill="{color}">{ln}</text>'
    return out

body.append(lane_label(20, 190, ["PHYSICAL", "EVIDENCE"], EVID_C))
body.append(lane_label(20, 372, ["FRONTSTAGE", "(student)"], FRONT_C))
body.append(f'<line x1="0" y1="{lane_y["los"]}" x2="{W}" y2="{lane_y["los"]}" stroke="#c62828" stroke-width="2" stroke-dasharray="10 6"/>')
body.append('<text x="20" y="' + str(lane_y["los"]-8) + '" font-size="11" font-weight="800" fill="#c62828">LINE OF VISIBILITY</text>')
body.append(lane_label(20, 612, ["BACKSTAGE", "(mess/vendor)"], BACK_C))
body.append(lane_label(20, 842, ["SUPPORT", "PROCESSES"], SUPP_C))

# lane separators
for y in [lane_y["front"]+60, lane_y["back"]+60]:
    body.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#ddd" stroke-width="1.5"/>')

# Physical evidence row (icons only, small)
evidence = ["ic-phone", "ic-qr", "ic-pot", "ic-warning", "ic-chat"]
ev_labels = ["App screen", "QR credential", "Food tray", "Empty counter", "Rating screen"]
for x, icon, lab in zip(col_x, evidence, ev_labels):
    body.append(chip(x, lane_y["evidence"], icon, lab, "", EVID_C, w=190, h=56))

# Frontstage row
front_nodes = [
    ("ic-phone", "Registers for the month", "no attendance step"),
    ("ic-clock", "(nothing — decision", "not yet made)"),
    ("ic-person", "Wakes, decides, walks", "to mess or skips"),
    ("ic-warning", "Eats, runs out, or", "already left"),
    ("ic-chat", "Rates / emails /", "reads Ping (rarely)"),
]
for x, (icon, l1, l2) in zip(col_x, front_nodes):
    body.append(chip(x, lane_y["front"], icon, l1, l2, FRONT_C, w=220))

# Backstage row
back_nodes = [
    ("ic-coin", "Billing calculated from", "registration count"),
    ("ic-briefcase", "Vendor forecast fixed,", "order placed"),
    ("ic-pot", "Kitchen cooks &amp; serves", "to the fixed forecast"),
    ("ic-warning", "Waste / shortfall counted", "informally, if at all"),
    ("ic-link-broken", "No confirmed record of", "input reaching a decision"),
]
for x, (icon, l1, l2) in zip(col_x, back_nodes):
    body.append(chip(x, lane_y["back"], icon, l1, l2, BACK_C, w=220))

# Support processes row
supp_nodes = [
    ("ic-gear", "Registration/billing portal", "&amp; QR infrastructure"),
    ("ic-building", "4-day procurement lead", "time (structural ceiling)"),
    ("ic-shield", "Warden &amp; vendor", "contracts in force"),
    ("ic-briefcase", "Mess Committee sets", "policy, menu"),
    ("ic-people", "Student Parliament Mess", "Secretary (unreached)"),
]
for x, (icon, l1, l2) in zip(col_x, supp_nodes):
    body.append(chip(x, lane_y["support"], icon, l1, l2, SUPP_C, w=220))

# vertical connectors within each column (evidence->front->back->support)
for x in col_x:
    body.append(f'<line x1="{x}" y1="{lane_y["evidence"]+28}" x2="{x}" y2="{lane_y["front"]-39}" stroke="#bbb" stroke-width="2"/>')
    body.append(f'<line x1="{x}" y1="{lane_y["front"]+39}" x2="{x}" y2="{lane_y["back"]-39}" stroke="#bbb" stroke-width="2" stroke-dasharray="4 4"/>')
    body.append(f'<line x1="{x}" y1="{lane_y["back"]+39}" x2="{x}" y2="{lane_y["support"]-39}" stroke="#bbb" stroke-width="2"/>')

# horizontal flow arrows along each lane
for row_y in [lane_y["front"], lane_y["back"], lane_y["support"]]:
    for i in range(len(col_x)-1):
        x1 = col_x[i]+115
        x2 = col_x[i+1]-115
        body.append(f'<line x1="{x1}" y1="{row_y}" x2="{x2}" y2="{row_y}" stroke="#cfd8dc" stroke-width="3" marker-end="url(#arrow-cfd8dc)"/>')

# key insight callout
body.append(f'<rect x="1600" y="960" width="360" height="140" rx="12" fill="#fdecea" stroke="#c62828" stroke-width="2"/>')
body.append(f'<text x="1620" y="988" font-size="13" font-weight="800" fill="#c62828">Blueprint finding</text>')
insight = ["The line of visibility is crossed", "only twice a month (registration,", "rating). Every single-morning", "decision — go, skip, what to eat —", "happens with zero backstage", "visibility until it is too late to act."]
for k, ln in enumerate(insight):
    body.append(f'<text x="1620" y="{1008+k*18}" font-size="11.5" fill="#333">{ln}</text>')

svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(["#cfd8dc"]))
render(svg, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/diagram8-service-blueprint.png", W, H)
