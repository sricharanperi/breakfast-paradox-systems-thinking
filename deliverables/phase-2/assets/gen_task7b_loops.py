import sys, math
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, curved_arrow, marker_defs, wrap_svg, render, label_box

BASE = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/"

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
        body.append(f'<rect x="{nx-190}" y="{ny-16}" width="380" height="{28+18*len(lines)}" rx="10" fill="#fafafa" stroke="#9e9e9e" stroke-dasharray="3 3"/>')
        for k, ln in enumerate(lines):
            body.append(f'<text x="{nx}" y="{ny+8+k*18}" text-anchor="middle" font-size="12" fill="#424242">{ln}</text>')
    svg = wrap_svg(w, h, "\n".join(body), extra_defs=marker_defs(list(colors_used)))
    render(svg, out_path, w, h)

# ---------------------------------------------------------------------------
# diagram24 -- loop status dashboard, all ten (eleven, counting L3b) loops
# ---------------------------------------------------------------------------
def dashboard():
    w, h = 1500, 1000
    body = []
    body.append(f'<text x="40" y="50" font-size="26" font-weight="800" fill="#0d47a1">Loop Status Dashboard — L1 through L10</text>')
    body.append(f'<text x="40" y="76" font-size="14" fill="#555">Every candidate feedback mechanism tested against primary evidence. Closure rule: a loop only counts if the last link causes the first.</text>')

    legend = [
        ("#2e7d32", "Closes — Reinforcing"),
        ("#00838f", "Closes — Balancing"),
        ("#f57f17", "Chain — does not close"),
        ("#c62828", "Disconfirmed"),
        ("#616161", "Absent / missing loop"),
        ("#6a1b9a", "Not a loop — static state"),
    ]
    lx = 40
    ly = 110
    for color, label in legend:
        body.append(f'<circle cx="{lx+8}" cy="{ly}" r="8" fill="{color}"/>')
        body.append(f'<text x="{lx+24}" y="{ly+5}" font-size="12.5" fill="#333">{label}</text>')
        lx += 24 + len(label)*7.2 + 26

    items = [
        ("ic-coin", "L1 — Speculative Registration", "Reinforcing, closes (1 assumed link)", "#2e7d32"),
        ("ic-toggle", "L2 — Skip Meal Mechanism", "Chain — confirmed, does not close", "#f57f17"),
        ("ic-building", "L3 — Capacity Redistribution", "Disconfirmed — opposite of evidence", "#c62828"),
        ("ic-warning", "L3b — Kadamba Demand Lock-in", "Reinforcing, candidate (weak link)", "#2e7d32"),
        ("ic-bowl", "L4 — Menu Rotation Response", "Balancing, closes — fully confirmed", "#00838f"),
        ("ic-calendar-x", "L5 — Menu Transparency Effect", "Chain — feeds L1, does not close", "#f57f17"),
        ("ic-qr", "L6 — Shock-Adaptive Relaxation", "Balancing, closes — closure assumed", "#00838f"),
        ("ic-clock", "L7 — Late-Night / Skip / Crash", "Chain — only first link confirmed", "#f57f17"),
        ("ic-link-broken", "L8 — Vendor Quality Discipline", "Absent — corrective link severed", "#616161"),
        ("ic-pot", "L9 — Waste Disposal Effectiveness", "Reinforcing, closes (assumed links)", "#2e7d32"),
        ("ic-gear", "L10 — Known-But-Unowned Gap", "Static state, not a reinforcing spiral", "#6a1b9a"),
    ]
    cols = 3
    col_w = 460
    row_h = 190
    x0 = 260
    y0 = 260
    for idx, (icon, l1, l2, color) in enumerate(items):
        r = idx // cols
        c = idx % cols
        cx = x0 + c*col_w
        cy = y0 + r*row_h
        body.append(chip(cx, cy, icon, l1, l2, color, w=400, h=110))

    svg = wrap_svg(w, h, "\n".join(body))
    render(svg, BASE+"diagram24-loop-status-dashboard.png", w, h)

dashboard()

# ---------------------------------------------------------------------------
# diagram25 -- L1, Speculative Registration / Resale Safety Net (closes, reinforcing)
# ---------------------------------------------------------------------------
loop_diagram(
    nodes=[
        ("ic-phone", "Speculative registration", "rate (no firm intent)", "#2e7d32"),
        ("ic-warning", "Unused registration", "volume", "#2e7d32"),
        ("ic-people", "Mess Cell resale", "activity", "#2e7d32"),
        ("ic-coin", "Net cost of a", "speculative registration", "#2e7d32"),
    ],
    edges=[
        (0,1,"+","solid","#2e7d32",""),
        (1,2,"+","solid","#2e7d32",""),
        (2,3,"-","solid","#2e7d32",""),
        (3,0,"-","broken","#c62828","assumed closing link"),
    ],
    title="L1 — Speculative Registration / Resale Safety Net",
    tag="Reinforcing, closes — three links confirmed by direct respondent quotes, the closing link is assumed",
    tag_color="#2e7d32",
    out_path=BASE+"diagram25-cld-l1-resale.png",
    radius=320, w=1250, h=1000,
    extra_note=(625, 900, "The strongest available evidence for what drives registration is capacity-\nsecuring (\"Kadamba is hard to get and it gets full\"), not cost-insurance from\nresale. The loop's existence rests on this one unconfirmed link."),
)

# ---------------------------------------------------------------------------
# diagram26 -- L4, Menu Rotation Governance Response (closes, balancing, fully confirmed)
# ---------------------------------------------------------------------------
loop_diagram(
    nodes=[
        ("ic-warning", "Menu fatigue", "(fixed semester-long menu)", "#00838f"),
        ("ic-chat", "Feedback intensity rises,", "reaches Student Council", "#00838f"),
        ("ic-briefcase", "CDS Committee", "approves biweekly rotation", "#00838f"),
        ("ic-bowl", "Menu variety", "increases", "#00838f"),
    ],
    edges=[
        (0,1,"+","solid","#00838f",""),
        (1,2,"+","solid","#00838f",""),
        (2,3,"+","solid","#00838f",""),
        (3,0,"-","solid","#00838f","confirmed: already happened"),
    ],
    title="L4 — Menu Rotation Governance Response",
    tag="Balancing, closes — every link confirmed directly by the CFS Chair, no assumed step",
    tag_color="#00838f",
    out_path=BASE+"diagram26-cld-l4-menu-rotation.png",
    radius=320, w=1250, h=1000,
)

# ---------------------------------------------------------------------------
# diagram27 -- L6, Shock-Adaptive Registration Relaxation (closes, balancing, condition-triggered)
# ---------------------------------------------------------------------------
loop_diagram(
    nodes=[
        ("ic-qr", "Walk-in / attendance-tracked", "billing in effect", "#1565c0"),
        ("ic-warning", "Vendor procurement", "uncertainty", "#1565c0"),
        ("ic-shield", "Institutional confidence in", "sustaining the model", "#1565c0"),
    ],
    edges=[
        (0,1,"+","broken","#1565c0","assumed"),
        (1,2,"-","broken","#1565c0","assumed"),
        (2,0,"+","broken","#1565c0","assumed"),
    ],
    title="L6 — Shock-Adaptive Registration Relaxation",
    tag="Balancing, condition-triggered — trigger and mechanism confirmed, self-limiting closure assumed",
    tag_color="#1565c0",
    out_path=BASE+"diagram27-cld-l6-shock-adaptive.png",
    radius=300, w=1150, h=950,
    extra_note=(575, 850, "Only fires under an uncertainty shock (an LPG shortage, a mass-exodus\nholiday). Whether it is a real self-limiting loop or just an on/off switch\ntied to the calendar, with no feedback at all, is not resolved by the evidence."),
)

# ---------------------------------------------------------------------------
# diagram28 -- L2, Skip Meal: a chain that does not close
# ---------------------------------------------------------------------------
loop_diagram(
    nodes=[
        ("ic-clock", "Non-attendance intent", "known in advance", "#f57f17"),
        ("ic-toggle", "Skip Meal", "declarations made", "#f57f17"),
        ("ic-pot", "Kitchen same-week", "prep-quantity forecast", "#f57f17"),
        ("ic-warning", "Over-preparation /", "wasted-food volume", "#f57f17"),
    ],
    edges=[
        (0,1,"+","solid","#f57f17","near-zero uptake, confirmed"),
        (1,2,"-","solid","#f57f17",""),
        (2,3,"+","solid","#f57f17",""),
        (3,0,"✕","broken","#c62828","no evidenced return link"),
    ],
    title="L2 — Skip Meal: a Designed Mechanism That Does Not Close",
    tag="Chain, not a loop — the first three links are real; nothing evidenced returns waste to intent",
    tag_color="#f57f17",
    out_path=BASE+"diagram28-chain-l2-skipmeal.png",
    radius=320, w=1250, h=1000,
    extra_note=(625, 900, "Skip Meal genuinely reaches the kitchen and changes prep quantity — a real,\nworking, one-way mechanism. No institutional feedback connects resulting\nwaste back to whether a student uses Skip Meal. Calling this \"B1\" (a prior\ndraft's label) implied closure that the evidence does not support."),
)

print("done")
