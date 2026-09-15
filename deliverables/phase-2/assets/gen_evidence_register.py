import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, marker_defs, wrap_svg, render

BASE = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/"

W, H = 2000, 1080
body = []
body.append(f'<text x="40" y="52" font-size="26" font-weight="800" fill="#0d47a1">Assumptions Tested Against Evidence</text>')
body.append(f'<text x="40" y="84" font-size="15" fill="#555">Left: what Phase 1 assumed. Right: what the evidence did to it.</text>')

ASSUME_C = "#616161"
CONFIRM_C = "#2e7d32"
REVISE_C = "#f57f17"
OVERTURN_C = "#c62828"

rows = [
    ("ic-calendar-x", "8:30 class start is the", "main reason for skipping", "ic-check", "Real, but secondary.", "Late sleep dominates instead", REVISE_C),
    ("ic-warning", "Skip leads to an energy crash", "and a compensatory purchase", "ic-check", "Only the first link confirmed.", "Rest is untested hypothesis", REVISE_C),
    ("ic-briefcase", "Registration is an adequate", "stand-in for real demand", "ic-check", "Confirmed false in practice,", "confirmed still the operating belief", OVERTURN_C),
    ("ic-person", "Bakul's low uptake is because", "it's a newer mess", "ic-check", "Cuisine preference is the", "stronger, better-evidenced driver", REVISE_C),
    ("ic-briefcase", "Nobody has solved the", "registration-attendance gap", "ic-check", "A working fix ran twice,", "and was switched off both times", OVERTURN_C),
    ("ic-person", "Peer presence meaningfully", "drives attendance", "ic-check", "Tested directly and", "disconfirmed as decisive", CONFIRM_C),
]

y0 = 155
row_h = 160
for i, (icon_a, a1, a2, icon_b, b1, b2, color) in enumerate(rows):
    cy = y0 + i * row_h
    body.append(chip(430, cy, icon_a, a1, a2, ASSUME_C, w=700, h=110, fill="#f5f5f5"))
    body.append(straight_arrow(790, cy, 1080, cy, color, width=6))
    body.append(chip(1500, cy, icon_b, b1, b2, color, w=760, h=110, fill="white"))

svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs([ASSUME_C, CONFIRM_C, REVISE_C, OVERTURN_C]))
render(svg, BASE + "diagram29-assumption-evidence-map.png", W, H)
