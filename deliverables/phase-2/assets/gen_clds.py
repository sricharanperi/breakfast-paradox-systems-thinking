import sys, math
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, curved_arrow, marker_defs, wrap_svg, render

def loop_diagram(nodes, edges, title, tag, tag_color, out_path, w=1300, h=1050, radius=360, node_w=260, extra_note=None, cy_offset=0):
    cx, cy = w/2, h/2 + 40 + cy_offset
    n = len(nodes)
    pos = []
    for i in range(n):
        ang = -90 + i*(360/n)
        rad = math.radians(ang)
        pos.append((cx + radius*math.cos(rad), cy + radius*math.sin(rad)))
    body = [f'<text x="40" y="55" font-size="28" font-weight="800" fill="{tag_color}">{title}</text>']
    body.append(f'<text x="40" y="82" font-size="15" fill="#555">{tag}</text>')
    for (icon, l1, l2, color), (x, y) in zip(nodes, pos):
        body.append(chip(x, y, icon, l1, l2, color, w=node_w))
    colors_used = set()
    for (i, j, sign, style, color, label) in edges:
        x1, y1 = pos[i]; x2, y2 = pos[j]
        dx, dy = x2-x1, y2-y1
        dist = math.hypot(dx, dy) or 1
        ux, uy = dx/dist, dy/dist
        start = (x1+ux*(node_w/2+6), y1+uy*40)
        end = (x2-ux*(node_w/2+6), y2-uy*40)
        dash = "8 6" if style=="broken" else None
        body.append(curved_arrow(start[0], start[1], end[0], end[1], color, label=label, bend=0.22, width=4.5 if style!="broken" else 3.5, dash=dash, sign=sign))
        colors_used.add(color)
    if extra_note:
        nx, ny, note = extra_note
        lines = note.split("\n")
        body.append(f'<rect x="{nx-160}" y="{ny-16}" width="320" height="{28+18*len(lines)}" rx="10" fill="#fafafa" stroke="#9e9e9e" stroke-dasharray="3 3"/>')
        for k, ln in enumerate(lines):
            body.append(f'<text x="{nx}" y="{ny+8+k*18}" text-anchor="middle" font-size="12" fill="#424242">{ln}</text>')
    svg = wrap_svg(w, h, "\n".join(body), extra_defs=marker_defs(list(colors_used)))
    render(svg, out_path, w, h)

BASE = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/"

# R1 -- reinforcing, confirmed
loop_diagram(
    nodes=[
        ("ic-coin", "Perceived cost of", "over-registering (low)", "#5e35b1"),
        ("ic-phone", "Registration volume", "vs. real attendance intent", "#5e35b1"),
        ("ic-warning", "Unused / no-show", "registrations", "#5e35b1"),
        ("ic-people", "Mess Cell resale", "activity", "#5e35b1"),
        ("ic-coin", "Value recovered from", "an unused registration", "#5e35b1"),
    ],
    edges=[
        (0,1,"+","solid","#5e35b1",""), (1,2,"+","solid","#5e35b1",""),
        (2,3,"+","solid","#5e35b1",""), (3,4,"+","solid","#5e35b1",""),
        (4,0,"+","solid","#5e35b1",""),
    ],
    title="R1 — Registration / Resale Loop",
    tag="Reinforcing — confirmed by respondent data",
    tag_color="#5e35b1",
    out_path=BASE+"diagram4-cld-r1-resale.png",
)

# B1 -- balancing, broken at first link
loop_diagram(
    nodes=[
        ("ic-warning", "Gap: kitchen over-", "preparation above target", "#00838f"),
        ("ic-toggle", "Skip Meal", "toggle usage", "#00838f"),
        ("ic-pot", "Kitchen preparation", "volume for no-shows", "#00838f"),
    ],
    edges=[
        (0,1,"+","broken","#c62828","intended, 0/6 confirmed used"),
        (1,2,"-","solid","#00838f",""),
        (2,0,"+","solid","#00838f",""),
    ],
    title="B1 — Skip Meal Balancing Loop",
    tag="Balancing as designed — the corrective link does not fire in practice",
    tag_color="#00838f",
    out_path=BASE+"diagram5-cld-b1-skipmeal.png",
    radius=300, w=1150, h=950,
)

# B2 -- balancing, broken
loop_diagram(
    nodes=[
        ("ic-building", "Kadamba registration", "nearing capacity", "#f57f17"),
        ("ic-warning", "Scarcity signal", "(hard to get a slot)", "#f57f17"),
        ("ic-people", "Redistribution toward", "Bakul / Palash", "#f57f17"),
    ],
    edges=[
        (0,1,"+","solid","#f57f17",""),
        (1,2,"+","broken","#c62828","intended, not observed"),
        (2,0,"-","solid","#f57f17",""),
    ],
    title="B2 — Capacity Redistribution Loop",
    tag="Balancing as designed — weak / broken in practice",
    tag_color="#f57f17",
    out_path=BASE+"diagram6-cld-b2-redistribution.png",
    radius=300, w=1150, h=1000,
    extra_note=(575, 850, "Confirmed instead: one respondent registers at Kadamba\nBECAUSE it is scarce (demand concentration, not redistribution).\nCapacity was added administratively (Bakul built) — outside this loop."),
)

# R2 -- candidate loop
loop_diagram(
    nodes=[
        ("ic-clock", "Late night /", "late sleep", "#2e7d32"),
        ("ic-calendar-x", "Breakfast", "skipped", "#2e7d32"),
        ("ic-warning", "Late-morning energy", "crash (~11:15 AM)", "#ad1457"),
        ("ic-coin", "Compensatory canteen /", "delivery purchase", "#ad1457"),
        ("ic-coin", "Pays twice (mess", "fee + canteen)", "#ad1457"),
        ("ic-bowl", "Low-nutrition, sluggish", "by evening", "#ad1457"),
    ],
    edges=[
        (0,1,"+","solid","#2e7d32",""),
        (1,2,"+","broken","#ad1457",""),
        (2,3,"+","broken","#ad1457",""),
        (3,4,"+","broken","#ad1457",""),
        (4,5,"+","broken","#ad1457",""),
        (5,0,"+","broken","#ad1457",""),
    ],
    title="R2 — Candidate Skip / Crash / Compensate Loop",
    tag="Reinforcing, candidate — only the first link is confirmed by real respondents",
    tag_color="#ad1457",
    out_path=BASE+"diagram7-cld-candidate-skip-crash.png",
    radius=380, w=1400, h=1150,
)

# B3 -- Menu Rotation Governance Response: the project's first FULLY CONFIRMED,
# already-exercised closed loop (not a candidate, not broken -- this one actually fired)
loop_diagram(
    nodes=[
        ("ic-warning", "Menu fatigue", "(fixed semester-long menu)", "#00838f"),
        ("ic-chat", "Feedback intensity", "rises (posters, complaints)", "#00838f"),
        ("ic-people", "Escalates via CDS", "Student Council", "#00838f"),
        ("ic-briefcase", "CDS Committee", "approves biweekly rotation", "#00838f"),
        ("ic-bowl", "Menu variety", "increases", "#00838f"),
    ],
    edges=[
        (0,1,"+","solid","#00838f",""), (1,2,"+","solid","#00838f",""),
        (2,3,"+","solid","#00838f",""), (3,4,"+","solid","#00838f",""),
        (4,0,"-","solid","#00838f","confirmed: already happened"),
    ],
    title="B3 — Menu Rotation Governance Loop",
    tag="Balancing — CONFIRMED and already exercised (not a candidate)",
    tag_color="#00838f",
    out_path=BASE+"diagram10-cld-b3-menu-rotation.png",
)

# R3 -- Menu Transparency Backfire: interviewee-self-identified second-order risk
# of the B3 fix above -- a candidate loop, only the first link confirmed
loop_diagram(
    nodes=[
        ("ic-calendar-x", "Menu rotation makes", "next menu predictable", "#2e7d32"),
        ("ic-phone", "Students check the", "posted menu in advance", "#ad1457"),
        ("ic-warning", "Selective no-show on", "disliked-menu days", "#ad1457"),
        ("ic-people", "Habit of deciding by", "menu, not by default", "#ad1457"),
    ],
    edges=[
        (0,1,"+","solid","#2e7d32",""),
        (1,2,"+","broken","#ad1457","not yet measured"),
        (2,3,"+","broken","#ad1457",""),
        (3,1,"+","broken","#ad1457",""),
    ],
    title="R3 — Menu Transparency Backfire Loop",
    tag="Reinforcing, candidate — self-identified risk; offsets some of B3's gain",
    tag_color="#ad1457",
    out_path=BASE+"diagram11-cld-r3-menu-backfire.png",
    radius=300, w=1150, h=950,
)

# B4 -- Shock-Adaptive Registration Relaxation: the headline finding of the 2026-09-13
# systems-boundary expansion. Condition-triggered, CONFIRMED as historical fact -- the
# institution has already run a working attendance-based billing model, it just retires
# it once the triggering shock passes.
loop_diagram(
    nodes=[
        ("ic-warning", "Uncertainty spike:", "holiday / fest / LPG shortage", "#1565c0"),
        ("ic-qr", "Registration made", "non-compulsory (walk-in QR)", "#1565c0"),
        ("ic-shield", "Consumption tracked", "at point of service", "#1565c0"),
        ("ic-coin", "Billing / waste risk", "realigned with true demand", "#1565c0"),
        ("ic-toggle", "Relaxed model retired", "once shock passes", "#e65100"),
    ],
    edges=[
        (0,1,"+","solid","#1565c0",""),
        (1,2,"+","solid","#1565c0",""),
        (2,3,"-","solid","#1565c0",""),
        (3,4,"-","broken","#e65100","assumed: reverts to standing model"),
        (4,0,"-","broken","#e65100","assumed closure"),
    ],
    title="B4 — Shock-Adaptive Registration Relaxation",
    tag="Balancing, condition-triggered — CONFIRMED as historical fact (LPG shortage + holidays)",
    tag_color="#1565c0",
    out_path=BASE+"diagram14-cld-b4-shock-adaptive.png",
    radius=340, w=1300, h=1050,
    extra_note=(650, 950, "The institution has already built and run a working fix for the\ncore registration-attendance gap. It is not the standing default —\nRC1 is a choice against procurement certainty, not an unsolved problem."),
)
