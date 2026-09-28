"""Activity 10, Deliverable 3: the recommended bundle as it runs over one breakfast.

Swimlane prototype diagram (systems-visual-design skill, svgkit.py): columns are
moments from the evening before to the monthly review; lanes are students, the
kitchen, the records and the governance around them. Solid chips can be piloted
with an operator now; dashed chips need the rule owner. Red dashed arrows are
routes that do not exist today; the green dashed arrow is the next-day learning
link the daily sheet creates at Kadamba.
"""
import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render

OUT = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-3/assets/diagram-a10-intervention-prototype.png"
W, H = 2360, 1260
STU, PROC, GOV, SOC, RED, GREEN, GREY = "#e65100", "#1565c0", "#00695c", "#6a1b9a", "#c62828", "#2e7d32", "#616161"
F = 'font-family="Helvetica,Arial,sans-serif"'
CW = 290


def tx(x, y, s, size=13, w="400", c="#222", a="start"):
    return f'<text x="{x}" y="{y}" {F} font-size="{size}" font-weight="{w}" fill="{c}" text-anchor="{a}">{s}</text>'


def X(i):
    return 360 + i * 300


LANES = {"stu": (270, "Students", STU, "#fff3e0"), "kit": (510, "Kitchen: the quick fix, named as such", PROC, "#e3f2fd"),
         "rec": (750, "Records", SOC, "#f3e5f5"), "gov": (990, "Governance: the fundamental fix, on fixed dates", GOV, "#e0f2f1")}
COLS = ["Evening before", "5:30 to 7:30", "7:30 to 9:00", "9:00", "9:15 to 9:30 and after", "After service",
        "Weekly and monthly"]

b = [tx(40, 56, "Intervention Prototype: the re-sequenced bundle over one breakfast", 30, "800", "#1a237e"),
     tx(40, 88, "Where each piece acts, from the evening before to the monthly review. The kitchen lane is the quick fix that buys time; the student, records and governance lanes carry the fundamental fix on fixed dates.", 15, "400", "#555")]
for k, (y, name, c, fill) in LANES.items():
    b.append(f'<rect x="20" y="{y - 105}" width="{W - 40}" height="210" rx="18" fill="{fill}" fill-opacity="0.55" stroke="{c}" stroke-opacity="0.35"/>')
    b.append(tx(40, y - 78, name, 16, "800", c))
for i, c in enumerate(COLS):
    b.append(tx(X(i), 150, c, 14, "700", "#37474f", "middle"))
    b.append(f'<line x1="{X(i)}" y1="160" x2="{X(i)}" y2="1100" stroke="#b0bec5" stroke-width="1" stroke-dasharray="3 6"/>')


def node(i, lane, icon, l1, l2, color, dashed=False):
    y = LANES[lane][0]
    out = ""
    if dashed:
        out += f'<rect x="{X(i) - CW / 2 - 7}" y="{y - 46}" width="{CW + 14}" height="92" rx="18" fill="none" stroke="{color}" stroke-width="2" stroke-dasharray="7 5"/>'
    return out + chip(X(i), y, icon, l1, l2, color, w=CW, h=78)


b += [
    node(0, "stu", "ic-toggle", "Sunday skip (proposed wk 6)", "by Sat 8 pm; no charge, lower count", STU, True),
    node(2, "stu", "ic-people", "Diners arrive", "Sundays: 13.5% in by 8:00", STU),
    node(4, "stu", "ic-warning", "Closing crest", "Sundays: 46% after 9:15", STU),
    node(0, "kit", "ic-calendar-x", "Day-before plan card", "grams x expected eaters", PROC),
    node(1, "kit", "ic-pot", "First batch, all checks", "1.5 x expected before 9:15", PROC),
    node(3, "kit", "ic-clock", "9:00 count, late batch", "count / weekday share", PROC),
    node(4, "kit", "ic-pot", "Late batch lands 9:15", "counter top-up still on", PROC),
    node(5, "kit", "ic-bowl", "Named allowance", "outside diners and staff", PROC),
    node(5, "rec", "ic-briefcase", "One-page daily sheet", "batch, top-ups, run-out, left", SOC),
    node(6, "rec", "ic-qr", "Breakfast Ledger", "booked, cooked, eaten, charged", SOC),
    node(2, "gov", "ic-shield", "Tasting: quantity line", "first batch vs yesterday", GOV, True),
    node(5, "gov", "ic-people", "Joint reading (wk 4)", "operators, CDS, students, facility", GOV),
    node(6, "gov", "ic-building", "Goal, beliefs, threshold", "review, never a deduction", GOV, True),
]

sy, ky, ry, gy = (LANES[k][0] for k in ("stu", "kit", "rec", "gov"))
h = 46
b += [
    straight_arrow(X(0), sy + h, X(0), ky - h - 8, RED, "lower count", width=4, dash="9 6"),
    straight_arrow(X(0) + CW / 2, ky, X(1) - CW / 2 - 8, ky, PROC, width=4),
    straight_arrow(X(1) + CW / 2, ky, X(3) - CW / 2 - 8, ky, PROC, "hold raw reserve", width=4),
    curved_arrow(X(2) + 60, sy + h, X(3) - 40, ky - h - 8, STU, "count so far", bend=-0.12, width=3.5),
    straight_arrow(X(3) + CW / 2, ky, X(4) - CW / 2 - 8, ky, PROC, width=4),
    straight_arrow(X(4), sy + h, X(4), ky - h - 8, STU, "served", width=3.5),
    straight_arrow(X(4) + CW / 2, ky, X(5) - CW / 2 - 8, ky, PROC, width=4),
    straight_arrow(X(5), ky + h, X(5), ry - h - 8, SOC, "record", width=3.5),
    straight_arrow(X(5) + CW / 2, ry, X(6) - CW / 2 - 8, ry, SOC, width=4),
    straight_arrow(X(6), ry + h, X(6), gy - h - 12, RED, "new route", width=4, dash="9 6"),
    curved_arrow(X(1), ky + h, X(2) - 40, gy - h - 12, RED, "quantity line", bend=0.12, width=3.5, dash="9 6", t=0.62),
    curved_arrow(X(5) - CW / 2, ry + 20, X(0) + 20, ky + h + 8, GREEN, "read next day: learning link", bend=-0.10, width=4, dash="9 6"),
    straight_arrow(X(5) + 110, ry + h, X(5) + 110, gy - h - 8, SOC, width=3),
]

# legend
ly = 1150
b.append(f'<rect x="40" y="{ly - 30}" width="{W - 80}" height="80" rx="12" fill="white" stroke="#cfd8dc"/>')
b.append(f'<rect x="64" y="{ly - 12}" width="46" height="30" rx="8" fill="white" stroke="#37474f" stroke-width="2.4"/>')
b.append(tx(122, ly + 8, "solid chip: the team can pilot it with an operator now", 14))
b.append(f'<rect x="560" y="{ly - 12}" width="46" height="30" rx="8" fill="none" stroke="#37474f" stroke-width="2" stroke-dasharray="7 5"/>')
b.append(tx(618, ly + 8, "dashed chip: needs the rule owner or the facility team; the team proposes", 14))
b.append(f'<line x1="1180" y1="{ly + 3}" x2="1240" y2="{ly + 3}" stroke="{RED}" stroke-width="4" stroke-dasharray="9 6"/>')
b.append(tx(1252, ly + 8, "route that does not exist today", 14))
b.append(f'<line x1="1520" y1="{ly + 3}" x2="1580" y2="{ly + 3}" stroke="{GREEN}" stroke-width="4" stroke-dasharray="9 6"/>')
b.append(tx(1592, ly + 8, "next-day learning link (runs at Yuktāhār, absent at Kadamba)", 14))
b.append(tx(64, ly + 36, "Percentages are Kadamba April 2026 records. Batch sizes follow the refined design in the scenario model; the named allowance is kept whatever the batch.", 12.5, "400", "#555"))

svg = wrap_svg(W, H, "".join(b), marker_defs([STU, PROC, SOC, RED, GREEN, GOV]))
render(svg, OUT, W, H)
