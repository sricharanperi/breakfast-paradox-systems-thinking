import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render, PALETTE, label_box

W, H = 1900, 1350
GOV_C, GOV_F = "#00695c", "#e0f2f1"
PROC_C, PROC_F = "#1565c0", "#e3f2fd"
DEC_C, DEC_F = "#e65100", "#fff3e0"
FB_C, FB_F = "#6a1b9a", "#f3e5f5"
EXT_C, EXT_F = "#616161", "#f0f0f0"
WARN_C = "#c62828"
TENSION_C = "#f57f17"

body = []

def flag(x, y, text, color=WARN_C, w=260):
    out = f'<g><rect x="{x-w/2:.1f}" y="{y-18:.1f}" width="{w}" height="36" rx="9" fill="white" stroke="{color}" stroke-width="2"/>'
    out += f'<circle cx="{x-w/2+20:.1f}" cy="{y:.1f}" r="14" fill="{color}"/>'
    out += f'<use href="#ic-warning" x="{x-w/2+9:.1f}" y="{y-11:.1f}" width="22" height="22" fill="white"/>'
    out += f'<text x="{x-w/2+40:.1f}" y="{y+4:.1f}" font-size="11" font-weight="700" fill="{color}">{text}</text></g>'
    return out

body.append('<text x="40" y="55" font-size="34" font-weight="800" fill="#e8590c">System Map</text>')
body.append('<text x="40" y="82" font-size="16" fill="#555">Actors, process flow, resources, constraints — IIIT Hyderabad Breakfast Mess System</text>')

# Governance row
gov_y = 160
body.append(chip(560, gov_y, "ic-briefcase", "Mess Committee", "policy · menu", GOV_C, w=210))
body.append(chip(820, gov_y, "ic-gear", "Mess Office", "operations", GOV_C, w=210))
body.append(chip(1080, gov_y, "ic-shield", "Warden", "vendors · structural", GOV_C, w=210))
body.append(chip(1650, gov_y, "ic-building", "Academic administration", "sets 8:30 AM class start", EXT_C, w=340, fill="#fafafa"))
body.append(straight_arrow(665, gov_y, 715, gov_y, GOV_C, width=5))
body.append(straight_arrow(925, gov_y, 975, gov_y, GOV_C, width=5))
body.append(curved_arrow(1480, gov_y, 1185, gov_y, WARN_C, "NO FORMAL CHANNEL", bend=-0.35, width=3, dash="7 5"))

# Process row
proc_y = 440
proc_x = {"reg": 200, "bill": 490, "vk": 780, "sw": 1080, "out": 1380}
body.append(chip(proc_x["reg"], proc_y, "ic-phone", "Registration", "monthly, in advance", PROC_C, w=220))
body.append(chip(proc_x["bill"], proc_y, "ic-coin", "Billing", "by registration, not attendance", PROC_C, w=220))
body.append(chip(proc_x["vk"], proc_y, "ic-pot", "Vendors / Kitchen", "cook to 4-day forecast", PROC_C, w=220))
body.append(chip(proc_x["sw"], proc_y, "ic-clock", "Service window", "7:30-9:30 AM, crowd builds to close", PROC_C, w=240))
body.append(chip(proc_x["out"], proc_y, "ic-warning", "Outcome", "eaten / run-out / no-show", PROC_C, w=230))
for a, b in [("reg","bill"), ("bill","vk"), ("vk","sw"), ("sw","out")]:
    body.append(straight_arrow(proc_x[a]+110, proc_y, proc_x[b]-110, proc_y, PROC_C, width=5))

# Governance -> process dashed verticals
body.append(curved_arrow(820, gov_y+37, proc_x["bill"], proc_y-39, GOV_C, "orders &amp; bills", bend=0.12, width=2.6, dash="6 5"))
body.append(curved_arrow(820, gov_y+37, proc_x["vk"]-30, proc_y-39, GOV_C, "4-day order", bend=0.08, width=2.6, dash="6 5"))
body.append(curved_arrow(1080, gov_y+37, proc_x["vk"]+30, proc_y-39, GOV_C, "vendor mgmt", bend=-0.1, width=2.6, dash="6 5"))
body.append(curved_arrow(1650, gov_y+55, proc_x["sw"], proc_y-40, WARN_C, "8:30 class overlaps this window", bend=-0.05, width=3))

# bottleneck flags
body.append(flag(proc_x["vk"], proc_y+80, "BOTTLENECK: 4-day lead time"))
body.append(flag(proc_x["sw"], proc_y+80, "BOTTLENECK: 9:30 close, items run out"))

# No-show branch
ns_y = 680
body.append(chip(proc_x["out"], ns_y, "ic-warning", "No-show", "decided not to attend", DEC_C, w=220))
body.append(straight_arrow(proc_x["out"], proc_y+39, proc_x["out"], ns_y-39, DEC_C, width=5))

exit_y = 880
exits = [("ic-calendar-x","Cancel","capped 5/mo", 900), ("ic-toggle","Skip Meal","no refund — 0/6 used", 1130), ("ic-people","Mess Cell resale","informal WhatsApp", 1360), ("ic-warning","Wasted","no recovery path", 1590)]
for icon, l1, l2, x in exits:
    body.append(chip(x, exit_y, icon, l1, l2, DEC_C, w=200))
    body.append(curved_arrow(proc_x["out"], ns_y+39, x, exit_y-39, DEC_C, bend=0.06, width=2.6))
body.append(flag(1245, exit_y+75, "TENSION: resale outcompetes Skip Meal", color=TENSION_C, w=380))

# Feedback row
fb_y = 1120
body.append(chip(560, fb_y, "ic-chat", "In-app rating", "", FB_C, w=200))
body.append(chip(820, fb_y, "ic-chat", "Public email", "", FB_C, w=200))
body.append(chip(1080, fb_y, "ic-chat", "Ping", "student press", FB_C, w=200))
for x in [560, 820, 1080]:
    body.append(curved_arrow(x, fb_y-39, x, gov_y+40, FB_C, bend=0.02 if x==820 else (0.15 if x<820 else -0.15), width=2.6, dash="5 4"))
body.append(flag(820, fb_y+75, "FEEDBACK: inputs exist, no confirmed output", color=FB_C, w=420))

# Students
st_x, st_y = 120, 1120
body.append(f'<circle cx="{st_x}" cy="{st_y}" r="52" fill="{DEC_C}" stroke="#a13800" stroke-width="3"/>')
body.append(f'<use href="#ic-person" x="{st_x-26}" y="{st_y-26}" width="52" height="52" fill="white"/>')
body.append(f'<text x="{st_x}" y="{st_y+80}" text-anchor="middle" font-size="13" font-weight="700" fill="#1b1b1b">Students</text>')
body.append(f'<text x="{st_x}" y="{st_y+97}" text-anchor="middle" font-size="11" fill="#555">registrant · billed · consumer</text>')
body.append(curved_arrow(st_x+50, st_y-30, proc_x["reg"]-110, proc_y+15, DEC_C, "registers", bend=-0.25, width=3))
body.append(curved_arrow(st_x+45, st_y+15, 460, fb_y, DEC_C, "rates, emails, reads", bend=0.1, width=2.6))

# Legend
lx, ly = 1600, 1200
body.append(f'<rect x="{lx}" y="{ly}" width="270" height="140" rx="10" fill="white" stroke="#999" stroke-width="1.4"/>')
body.append(f'<text x="{lx+14}" y="{ly+22}" font-size="13" font-weight="800" fill="#222">Legend</text>')
for i, (c, label) in enumerate([(PROC_C,"Process"), (GOV_C,"Governance"), (DEC_C,"Student decision"), (FB_C,"Feedback"), (EXT_C,"External")]):
    yy = ly + 38 + i*20
    body.append(f'<rect x="{lx+14}" y="{yy-10}" width="15" height="15" rx="3" fill="{c}"/>')
    body.append(f'<text x="{lx+36}" y="{yy+1}" font-size="11.5" fill="#333">{label}</text>')

colors = [GOV_C, PROC_C, DEC_C, FB_C, EXT_C, WARN_C, TENSION_C]
svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(colors))
render(svg, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/diagram1-system-map.png", W, H)
