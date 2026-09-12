import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render

W, H = 2000, 1400
GOV_C = "#00695c"     # governance
PROC_C = "#1565c0"    # process / vendors
DEC_C = "#e65100"     # students / informal-economy
FB_C = "#6a1b9a"      # feedback
EXT_C = "#616161"     # external
WARN_C = "#c62828"    # no formal / no direct channel

body = []
body.append('<text x="40" y="55" font-size="34" font-weight="800" fill="#e8590c">Power and Information Flow Network</text>')
body.append('<text x="40" y="82" font-size="16" fill="#555">Who talks to whom, what flows, and where the channel does not exist — IIIT Hyderabad Breakfast Mess System</text>')

MC, MO, WD, ACAD = (560, 170), (900, 170), (1240, 170), (1650, 170)
VEN = (1650, 620)
ST = (300, 780)
MCELL, PING, TOOLS = (560, 1150), (900, 1150), (1240, 1150)

body.append(chip(*MC, "ic-briefcase", "Mess Committee", "policy", GOV_C, w=210))
body.append(chip(*MO, "ic-gear", "Mess Office", "operations", GOV_C, w=210))
body.append(chip(*WD, "ic-shield", "Warden", "vendors, structural", GOV_C, w=210))
body.append(chip(*ACAD, "ic-building", "Academic administration", "external", EXT_C, w=280, fill="#fafafa"))
body.append(chip(*VEN, "ic-pot", "Vendors", "commercial", PROC_C, w=210))
body.append(chip(*MCELL, "ic-people", "Mess Cell", "informal resale", FB_C, w=210))
body.append(chip(*PING, "ic-chat", "Ping", "student press", FB_C, w=210))
body.append(chip(*TOOLS, "ic-phone", "Unofficial tools", "outside the portal", FB_C, w=210))

body.append(f'<circle cx="{ST[0]}" cy="{ST[1]}" r="58" fill="{DEC_C}" stroke="#a13800" stroke-width="3"/>')
body.append(f'<use href="#ic-person" x="{ST[0]-29}" y="{ST[1]-29}" width="58" height="58" fill="white"/>')
body.append(f'<text x="{ST[0]}" y="{ST[1]+85}" text-anchor="middle" font-size="14" font-weight="700" fill="#1b1b1b">Students</text>')

# Governance row internal
body.append(straight_arrow(MC[0]+105, MC[1], MO[0]-105, MO[1], GOV_C, width=4))

# Confirmed formal / material flows (solid)
body.append(curved_arrow(ST[0]+45, ST[1]-45, MO[0]-105, MO[1]+30, DEC_C, "money, registration intent", bend=-0.18, width=3.2))
body.append(curved_arrow(MO[0], MO[1]+39, VEN[0]-90, VEN[1]-70, GOV_C, "four-day forecast, order", bend=0.2, width=3))
body.append(curved_arrow(WD[0]+40, WD[1]+39, VEN[0]+20, VEN[1]-70, GOV_C, "contract authority", bend=0.32, width=3))
body.append(curved_arrow(VEN[0]-105, VEN[1]+30, ST[0]+50, ST[1]+15, PROC_C, "food, service", bend=0.15, width=3.2))
body.append(curved_arrow(ACAD[0]-60, ACAD[1]+39, ST[0]+50, ST[1]-60, EXT_C, "class schedule constraint", bend=0.08, width=3))

# Feedback (dashed purple)
body.append(curved_arrow(ST[0]+30, ST[1]-58, MO[0]-105, MO[1]+55, FB_C, "feedback: rating, email", bend=-0.32, width=2.2, dash="6 5"))
body.append(curved_arrow(ST[0]+20, ST[1]-70, MC[0]-30, MC[1]+39, FB_C, "feedback: rating", bend=-0.42, width=2.2, dash="6 5"))
body.append(curved_arrow(PING[0]-40, PING[1]-39, MC[0], MC[1]+39, FB_C, "public visibility", bend=0.12, width=2, dash="6 5"))
body.append(curved_arrow(PING[0]+40, PING[1]-39, MO[0], MO[1]+39, FB_C, "public visibility", bend=-0.08, width=2, dash="6 5"))

# Informal economy (dashed orange)
body.append(curved_arrow(ST[0]+20, ST[1]+58, MCELL[0]-40, MCELL[1]-39, DEC_C, "resells, buys", bend=0.15, width=2.2, dash="6 5"))
body.append(curved_arrow(ST[0]+40, ST[1]+55, TOOLS[0]-60, TOOLS[1]-39, DEC_C, "may use instead of portal", bend=-0.32, width=2.2, dash="6 5"))

# No formal / no direct channel (dashed red) -- the governance-isolation finding
# (these three are nearly-horizontal long lines: a "bend" fraction that looks
# fine on a short/steep edge translates into a huge absolute pixel arc here,
# which is what previously pushed these arrows off the top of the canvas)
body.append(curved_arrow(MC[0]+40, MC[1]-39, ACAD[0]-90, ACAD[1]-10, WARN_C, bend=-0.06, width=2, dash="4 5"))
body.append(curved_arrow(MO[0]+50, MO[1]-39, ACAD[0]-90, ACAD[1]+2, WARN_C, bend=-0.09, width=2, dash="4 5"))
body.append(curved_arrow(WD[0]+60, WD[1]-39, ACAD[0]-90, ACAD[1]+15, WARN_C, "NO FORMAL CHANNEL (x3)", bend=-0.15, width=2, dash="4 5"))
body.append(curved_arrow(VEN[0]-30, VEN[1]+39, ST[0]+55, ST[1]+55, WARN_C, "NO DIRECT CHANNEL", bend=-0.35, width=2, dash="4 5"))

lx, ly = 1620, 1230
body.append(f'<rect x="{lx}" y="{ly}" width="330" height="150" rx="10" fill="white" stroke="#999" stroke-width="1.4"/>')
body.append(f'<text x="{lx+14}" y="{ly+22}" font-size="13" font-weight="800" fill="#222">Legend</text>')
for i, (c, label) in enumerate([(GOV_C,"Governance / formal authority"), (PROC_C,"Vendors / material flow"), (DEC_C,"Students / informal economy"), (FB_C,"Feedback channel"), (WARN_C,"No channel confirmed")]):
    yy = ly + 40 + i*22
    body.append(f'<rect x="{lx+14}" y="{yy-10}" width="15" height="15" rx="3" fill="{c}"/>')
    body.append(f'<text x="{lx+36}" y="{yy+1}" font-size="11.5" fill="#333">{label}</text>')

colors = [GOV_C, PROC_C, DEC_C, FB_C, WARN_C, EXT_C]
svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(colors))
render(svg, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/diagram9-power-flow-network.png", W, H)
