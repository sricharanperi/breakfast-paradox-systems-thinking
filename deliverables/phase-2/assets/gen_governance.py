import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render

W, H = 2000, 1350
GOV_C = "#00695c"
EXT_C = "#616161"
FB_C = "#6a1b9a"
DEC_C = "#e65100"
GREEN = "#2e7d32"
GREY = "#9e9e9e"

body = []
body.append('<text x="40" y="55" font-size="34" font-weight="800" fill="#e8590c">CDS / CFS Governance and Escalation</text>')
body.append('<text x="40" y="82" font-size="16" fill="#555">Org structure, decision flow, and the one confirmed, already-exercised policy loop — IIIT Hyderabad Breakfast Mess System</text>')

CFS = (1000, 160)
CDS = (1000, 340)
CFS_HEAD = (1500, 340)
CLS, CWS = (400, 340), (650, 340)
CHAIR = (1000, 520)
COMM = (750, 700)
COUNCIL = (1250, 700)
ADMIN = (1000, 880)

body.append(chip(*CFS, "ic-building", "CFS", "Campus Facilities Services (parent dept.)", GOV_C, w=260))
body.append(chip(*CLS, "ic-building", "CLS", "sibling dept., out of scope", EXT_C, w=210, fill="#fafafa"))
body.append(chip(*CWS, "ic-building", "CWS", "sibling dept., out of scope", EXT_C, w=210, fill="#fafafa"))
body.append(chip(*CDS, "ic-briefcase", "CDS", "Campus Dining Services (in scope)", GOV_C, w=260))
body.append(chip(*CFS_HEAD, "ic-person", "CFS Head", "handles low-intensity feedback directly", EXT_C, w=280, fill="#fafafa"))
body.append(chip(*CHAIR, "ic-shield", "CDS Chair: Giri", "NOT yet interviewed directly", GOV_C, w=280))
body.append(chip(*COMM, "ic-gear", "CDS Committee", "faculty — final decision authority", GOV_C, w=250))
body.append(chip(*COUNCIL, "ic-people", "CDS Student Council", "proposes, first review", GOV_C, w=250))
body.append(chip(*ADMIN, "ic-person", "Per-mess admin", "1 per mess, also a CDS member", GOV_C, w=250))

body.append(straight_arrow(CFS[0]-130, CFS[1]+10, CLS[0]+40, CLS[1]-39, GOV_C, width=2))
body.append(straight_arrow(CFS[0]-100, CFS[1]+15, CWS[0]+60, CWS[1]-39, GOV_C, width=2))
body.append(straight_arrow(CFS[0], CFS[1]+39, CDS[0], CDS[1]-39, GOV_C, width=4))
body.append(straight_arrow(CFS[0]+130, CFS[1]+15, CFS_HEAD[0]-100, CFS_HEAD[1]-39, EXT_C, width=3))
body.append(straight_arrow(CDS[0], CDS[1]+39, CHAIR[0], CHAIR[1]-39, GOV_C, width=3))
body.append(curved_arrow(CHAIR[0]-40, CHAIR[1]+39, COMM[0]+30, COMM[1]-39, GOV_C, "oversees", bend=-0.1, width=2.4))
body.append(curved_arrow(CHAIR[0]+40, CHAIR[1]+39, COUNCIL[0]-30, COUNCIL[1]-39, GOV_C, "oversees", bend=0.1, width=2.4))
body.append(curved_arrow(COUNCIL[0]-100, COUNCIL[1], COMM[0]+100, COMM[1], GOV_C, "proposes to", bend=-0.15, width=2.6))
body.append(curved_arrow(COMM[0]+40, COMM[1]+39, ADMIN[0]-60, ADMIN[1]-30, GOV_C, "coordinates via", bend=0.1, width=2.2))
body.append(curved_arrow(COUNCIL[0]-40, COUNCIL[1]+39, ADMIN[0]+60, ADMIN[1]-30, GOV_C, bend=-0.1, width=2.2))

# Escalation-by-intensity annotation
body.append(f'<rect x="{CFS_HEAD[0]-140}" y="{CFS_HEAD[1]+60}" width="280" height="60" rx="10" fill="#fafafa" stroke="{EXT_C}" stroke-dasharray="3 3"/>')
body.append(f'<text x="{CFS_HEAD[0]}" y="{CFS_HEAD[1]+82}" text-anchor="middle" font-size="12" font-weight="700" fill="#333">LOW-intensity feedback</text>')
body.append(f'<text x="{CFS_HEAD[0]}" y="{CFS_HEAD[1]+100}" text-anchor="middle" font-size="11" fill="#555">handled here, no escalation</text>')

body.append(f'<rect x="{COUNCIL[0]-140}" y="{COUNCIL[1]-110}" width="280" height="55" rx="10" fill="#fafafa" stroke="{GOV_C}" stroke-dasharray="3 3"/>')
body.append(f'<text x="{COUNCIL[0]}" y="{COUNCIL[1]-88}" text-anchor="middle" font-size="12" font-weight="700" fill="#333">HIGH-intensity feedback</text>')
body.append(f'<text x="{COUNCIL[0]}" y="{COUNCIL[1]-70}" text-anchor="middle" font-size="11" fill="#555">escalates through here</text>')

# Confirmed precedent badge (placed clear below-left of the chip, own box so it can't overlap)
badge_x, badge_y = COMM[0]-220, COMM[1]+70
body.append(f'<rect x="{badge_x-18}" y="{badge_y-38}" width="230" height="56" rx="10" fill="#e8f5e9" stroke="{GREEN}" stroke-width="1.6"/>')
body.append(f'<circle cx="{badge_x}" cy="{badge_y-10}" r="14" fill="{GREEN}"/>')
body.append(f'<text x="{badge_x}" y="{badge_y-5}" text-anchor="middle" font-size="14" font-weight="900" fill="white">&#10003;</text>')
body.append(f'<text x="{badge_x+24}" y="{badge_y-15}" font-size="11.5" font-weight="700" fill="{GREEN}">Already fired once:</text>')
body.append(f'<text x="{badge_x+24}" y="{badge_y}" font-size="10.5" fill="{GREEN}">biweekly menu rotation</text>')
body.append(f'<text x="{badge_x+24}" y="{badge_y+13}" font-size="10.5" fill="{GREEN}">(see B3 loop)</text>')

# Reconciliation question flags -- Phase 1 named these bodies differently; not silently merged
MC_OLD = (1600, 700)
SP_OLD = (1600, 880)
body.append(chip(*MC_OLD, "ic-warning", "Phase 1: 'Mess Committee'", "same body as CDS Committee?", FB_C, w=290, fill="#fdf6ff"))
body.append(chip(*SP_OLD, "ic-warning", "Phase 1: 'Student Parliament'", "same body as CDS Student Council?", FB_C, w=300, fill="#fdf6ff"))
body.append(curved_arrow(COMM[0]+125, COMM[1], MC_OLD[0]-145, MC_OLD[1], GREY, "unconfirmed", bend=-0.1, width=2, dash="4 5"))
body.append(curved_arrow(COUNCIL[0]+125, COUNCIL[1]+10, SP_OLD[0]-150, SP_OLD[1]-10, GREY, "unconfirmed", bend=0.08, width=2, dash="4 5"))

lx, ly = 60, 1080
body.append(f'<rect x="{lx}" y="{ly}" width="640" height="180" rx="10" fill="white" stroke="#999" stroke-width="1.4"/>')
body.append(f'<text x="{lx+16}" y="{ly+26}" font-size="14" font-weight="800" fill="#222">Reading this diagram</text>')
notes = [
 "Solid teal = confirmed org structure and decision flow (CFS Chair interview, 2026-09-13).",
 "Grey dashed = an open reconciliation question this project has not resolved: do these",
 "Phase 1 stakeholder-map terms name the same bodies under a different name, or two",
 "genuinely different groups? Not assumed either way. See braindump #2 sections 1-2.",
 "Green check = this exact pathway has already produced a real policy change once.",
]
for i, n in enumerate(notes):
    body.append(f'<text x="{lx+16}" y="{ly+50+i*24}" font-size="12" fill="#333">{n}</text>')

colors = [GOV_C, EXT_C, GREY]
svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(colors))
render(svg, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/diagram12-governance-escalation.png", W, H)
