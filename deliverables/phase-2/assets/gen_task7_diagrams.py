import sys, math
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render, label_box

BASE = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/"

# ---------------------------------------------------------------------------
# 1. ICEBERG MODEL v2 -- ONE fully-worked chain (Chain 1: Ghost Registration &
# Resale), narrated causally bottom-to-top: Mental Model -> Structure ->
# Pattern -> Event. Corrects the v1 bug where standing facts were mislabeled
# as Events.
# ---------------------------------------------------------------------------
W, H = 2000, 1700
body = []
body.append('<text x="40" y="50" font-size="30" font-weight="800" fill="#0d47a1">Iceberg Model -- Worked Example: Ghost Registration &amp; Resale</text>')
body.append('<text x="40" y="76" font-size="15" fill="#555">Course framework (Lecture 4): Events are single, concrete occurrences -- not rules or statistics. Read bottom-up: belief -&gt; structure -&gt; pattern -&gt; event.</text>')

bands = [
    (110, 430, "#e3f2fd", "EVENT", "What happened? (visible)"),
    (430, 760, "#bbdefb", "PATTERN / TREND", "What keeps happening?"),
    (760, 1160, "#5c9fd8", "SYSTEMIC STRUCTURE", "What causes the pattern?"),
    (1160, 1640, "#0d3b66", "MENTAL MODEL", "What beliefs created the structure? (invisible)"),
]
for (y0, y1, fill, title, sub) in bands:
    body.append(f'<rect x="0" y="{y0}" width="{W}" height="{y1-y0}" fill="{fill}"/>')
textcolor_by_band = ["#0d47a1", "#0d47a1", "white", "white"]
for i, (y0, y1, fill, title, sub) in enumerate(bands):
    tc = textcolor_by_band[i]
    body.append(f'<text x="40" y="{y0+38}" font-size="19" font-weight="800" fill="{tc}">{title}</text>')
    body.append(f'<text x="40" y="{y0+60}" font-size="12.5" fill="{tc}" opacity="0.85">{sub}</text>')
body.append(f'<line x1="0" y1="430" x2="{W}" y2="430" stroke="#1565c0" stroke-width="4"/>')
body.append('<text x="1500" y="424" font-size="13" font-weight="700" fill="#0d47a1">WATERLINE</text>')

EC = "#0d47a1"
body.append(chip(1000, 300, "ic-coin", "“I book Kadamba veg breakfast (₹48)", "every day and never avail it.” -- respondent, 2026-09-03", EC, w=1200, h=110))

PC = "#0d47a1"
body.append(chip(500, 580, "ic-calendar-x", "Breakfast turnout: 35-45%", "vs 70-90%+ other categories (CFS Chair)", PC, w=460))
body.append(chip(1000, 580, "ic-toggle", "0 of 6 respondents", "get value from Skip Meal", PC, w=380, fill="white"))
body.append(chip(1500, 580, "ic-people", "4 of 6 respondents", "use Mess Cell resale routinely", PC, w=440))

SC = "#0d3b66"
body.append(chip(330, 900, "ic-briefcase", "Billing = registration count,", "not attendance", SC, w=380, fill="#eaf2fb"))
body.append(chip(760, 900, "ic-coin", "Spot price 70-90% above", "registered rate", SC, w=380, fill="#eaf2fb"))
body.append(chip(1190, 900, "ic-people", "Mess Cell WhatsApp", "resale market", SC, w=380, fill="#eaf2fb"))
body.append(chip(1620, 900, "ic-toggle", "Skip Meal returns", "no money to student", SC, w=340, fill="#eaf2fb"))
body.append(chip(1000, 1070, "ic-clock", "T-4 sourcing lock: no same-day signal can change what is ordered", "same-week Skip Meal data only adjusts prep, confirmed 2026-09-13", SC, w=1500, h=90, fill="#eaf2fb"))

body.append(chip(600, 1330, "ic-briefcase", "INSTITUTION: “aggregate registration is an", "adequate demand proxy,” as standing policy", "#ffca28", w=760, h=100, fill="white", text_color="#0d3b66"))
body.append(chip(1420, 1330, "ic-person", "STUDENT: “a registration, once made,", "costs nothing extra to leave unused”", "#ffca28", w=680, h=100, fill="white", text_color="#0d3b66"))

body.append('<rect x="500" y="1480" width="1000" height="150" rx="10" fill="#08213d" stroke="#ffca28" stroke-width="1.6"/>')
body.append('<text x="1000" y="1512" text-anchor="middle" font-size="14" font-weight="800" fill="#ffca28">The institution\'s own belief is the best-evidenced mental model in this project:</text>')
body.append('<text x="1000" y="1536" text-anchor="middle" font-size="12.5" fill="white">the practice continues even though the CFS Chair can name the exact size of the gap,</text>')
body.append('<text x="1000" y="1557" text-anchor="middle" font-size="12.5" fill="white">and even though the institution has already run and retired a working alternative (loop L6).</text>')
body.append('<text x="1000" y="1608" text-anchor="middle" font-size="12" font-weight="700" fill="#ffca28">confirmed · single-sourced · assumed -- see the full chain table for per-row tags</text>')

# Causal arrows, drawn upward (deepest cause -> visible event), matching how
# the narrative reads: belief shapes structure, structure produces pattern,
# pattern manifests as event.
body.append(curved_arrow(1000, 1330, 850, 1160, "#e65100", "shapes", bend=-0.15, width=5))
body.append(curved_arrow(850, 900, 700, 760, "#e65100", "produces", bend=-0.15, width=5))
body.append(curved_arrow(1000, 580, 1000, 430, "#e65100", "manifests as", bend=0.0, width=5))

colors = [EC, "#ffca28", "#e65100"]
svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(colors))
render(svg, BASE + "diagram15-iceberg-model.png", W, H)

# ---------------------------------------------------------------------------
# 2. LOOP / CHAIN OVERVIEW DASHBOARD v2 -- honestly distinguishes closed
# loops from chains, disconfirmed mechanisms, and absent/missing loops. This
# corrects the v1 dashboard, which visually presented several non-closing
# chains as if they were loops.
# ---------------------------------------------------------------------------
W2, H2 = 2000, 1000
body2 = []
body2.append('<text x="40" y="45" font-size="26" font-weight="800" fill="#0d47a1">Feedback Analysis -- Loops, Chains, and Disconfirmed Mechanisms</text>')
body2.append('<text x="40" y="70" font-size="14" fill="#555">Closure was tested for every candidate. Only a mechanism whose last variable causally returns to its first counts as a loop.</text>')

def card(cx0, cy0, w, h, icon, lid, name, tag, color, fillc, style="solid"):
    dash = 'stroke-dasharray="10 7"' if style == "dashed" else ""
    body2.append(f'<rect x="{cx0}" y="{cy0}" width="{w}" height="{h}" rx="14" fill="{fillc}" stroke="{color}" stroke-width="2.6" {dash}/>')
    body2.append(f'<circle cx="{cx0+42}" cy="{cy0+42}" r="24" fill="{color}"/>')
    body2.append(f'<use href="#{icon}" x="{cx0+30}" y="{cy0+30}" width="24" height="24" fill="white"/>')
    body2.append(f'<text x="{cx0+78}" y="{cy0+50}" font-size="19" font-weight="900" fill="{color}">{lid}</text>')
    body2.append(f'<text x="{cx0+22}" y="{cy0+92}" font-size="13" font-weight="800" fill="#222">{name}</text>')
    body2.append(f'<text x="{cx0+22}" y="{cy0+116}" font-size="11" fill="#444">{tag}</text>')

body2.append('<text x="60" y="150" font-size="16" font-weight="800" fill="#2e7d32">CLOSED LOOPS (solid border)</text>')
loops = [
    ("ic-coin", "L1", "Registration / Resale Safety Net", "Reinforcing · closes (1 link assumed)", "#5e35b1", "#ede7f6"),
    ("ic-bowl", "L4", "Menu Rotation Governance", "Balancing · closes, every link confirmed", "#00838f", "#e0f7fa"),
    ("ic-qr", "L6", "Shock-Adaptive Registration Relaxation", "Balancing · closes, self-limiting mechanism assumed", "#1565c0", "#e3f2fd"),
    ("ic-building", "L3b", "Kadamba Demand Concentration", "Reinforcing · candidate, weak closing link", "#f57f17", "#fff8e1"),
    ("ic-warning", "L9", "Waste-Disposal Suppresses Pressure", "Reinforcing · closes on assumed links", "#6a1b9a", "#f3e5f5"),
]
x0 = 60
for i, (icon, lid, name, tag, color, fillc) in enumerate(loops):
    card(x0 + i*380, 170, 355, 150, icon, lid, name, tag, color, fillc, "solid")

body2.append('<text x="60" y="380" font-size="16" font-weight="800" fill="#c62828">CHAINS, DISCONFIRMED, OR ABSENT (dashed border -- not loops)</text>')
chains = [
    ("ic-toggle", "L2", "Skip Meal", "Chain -- mechanism works, no return link found", "#616161", "#f5f5f5"),
    ("ic-calendar-x", "L5", "Menu Transparency → Selective Skip", "Chain -- feeds L1, does not close on its own", "#616161", "#f5f5f5"),
    ("ic-clock", "L7", "Late Night → Skip → Energy Crash", "Chain — only link 1 confirmed, rest unconfirmed", "#616161", "#f5f5f5"),
    ("ic-link-broken", "L8", "Vendor Quality Market-Discipline", "Absent — the corrective link is confirmed severed", "#c62828", "#fdecea"),
    ("ic-link-broken", "L3", "Capacity Redistribution (old)", "Disconfirmed — evidence shows hoarding, not diversion", "#c62828", "#fdecea"),
    ("ic-shield", "L10", "“Known-But-Unowned Gap”", "Static state — confirmed facts, no worsening-over-time evidence", "#616161", "#f5f5f5"),
]
for i, (icon, lid, name, tag, color, fillc) in enumerate(chains):
    col = i % 3
    row = i // 3
    card(x0 + col*640, 400 + row*160, 610, 135, icon, lid, name, tag, color, fillc, "dashed")

body2.append('<rect x="60" y="750" width="1880" height="200" rx="10" fill="#fff3e0" stroke="#e65100" stroke-width="1.6"/>')
body2.append('<text x="80" y="782" font-size="14" font-weight="800" fill="#e65100">Why this distinction matters:</text>')
body2.append('<text x="80" y="806" font-size="12.5" fill="#5d4037">Calling a chain a "loop" implies a self-sustaining cycle that will keep reproducing itself even without new inputs. Several mechanisms in this</text>')
body2.append('<text x="80" y="828" font-size="12.5" fill="#5d4037">system -- Skip Meal, menu-transparency-driven skipping, the late-night/energy-crash story -- are real, evidenced up to a point, but never shown</text>')
body2.append('<text x="80" y="850" font-size="12.5" fill="#5d4037">to close. Presenting them honestly as open chains (or, for L8/L3, as an absent/disconfirmed mechanism) is itself a finding: it shows exactly</text>')
body2.append('<text x="80" y="872" font-size="12.5" fill="#5d4037">where this system\'s self-reinforcing dynamics stop and where a missing link -- an unasked question, an unbuilt feedback channel -- begins.</text>')
body2.append('<text x="80" y="900" font-size="12.5" fill="#5d4037">L4 (menu governance) is the only loop where every single link traces to a direct, named source with zero assumed links -- the reference case</text>')
body2.append('<text x="80" y="922" font-size="12.5" fill="#5d4037">against which every other mechanism\'s closure (or non-closure) in this document should be read.</text>')

colors2 = ["#5e35b1", "#00838f", "#1565c0", "#f57f17", "#6a1b9a", "#616161", "#c62828"]
svg2 = wrap_svg(W2, H2, "\n".join(body2), extra_defs=marker_defs(colors2))
render(svg2, BASE + "diagram17-loop-overview-dashboard.png", W2, H2)

# ---------------------------------------------------------------------------
# 3. ROOT CAUSE NETWORK v2 -- RC1 / RC2 / RC3 (RC3 replaced: now
# "complaint-intensity-triggered attention", not vendor-interest, which is
# demoted to a compounding candidate).
# ---------------------------------------------------------------------------
W3, H3 = 1900, 1500
body3 = []
body3.append('<text x="40" y="50" font-size="28" font-weight="800" fill="#b71c1c">Root Cause Network v2</text>')
body3.append('<text x="40" y="76" font-size="15" fill="#555">Three co-primary root causes, tested against a structural / breadth / counterfactual / evidence test</text>')

RC_C = "#b71c1c"
INT_C = "#e65100"

body3.append(chip(500, 200, "ic-briefcase", "RC1 -- Billing decoupled", "from attendance", RC_C, w=440))
body3.append(chip(1400, 200, "ic-people", "RC2 -- Fragmented decision rights", "(menu / execution / academic / billing)", RC_C, w=520))
body3.append(chip(950, 420, "ic-chat", "RC3 -- Attention triggers on complaint", "intensity, not data severity", RC_C, w=560))

body3.append(chip(500, 650, "ic-coin", "Incentive to over-register", "(individual + vendor revenue)", INT_C, w=460, fill="#fff3e0"))
body3.append(chip(1400, 650, "ic-warning", "Known gap never escalated", "though quantified (CFS Chair)", INT_C, w=460, fill="#fff3e0"))
body3.append(chip(950, 850, "ic-shield", "L4 (menu, loud) succeeds; RC1's gap", "(quiet, quantified) never escalates -- same design, opposite outcomes", INT_C, w=760, h=90, fill="#fff3e0"))

body3.append(chip(500, 1080, "ic-clock", "Intermediate: T-4 lock, average-based", "portioning, cancellation cap, price gap", "#616161", w=460, fill="#f5f5f5"))
body3.append(chip(1400, 1080, "ic-briefcase", "Candidate compounding: vendor revenue", "interest in the standing model (assumed)", "#6a1b9a", w=460, fill="#f3e5f5"))

body3.append(straight_arrow(500+220, 244, 500, 606, RC_C, width=3))
body3.append(straight_arrow(1400-220, 244, 1400, 606, RC_C, width=3))
body3.append(curved_arrow(500+120, 244, 950-280, 396, RC_C, "gates", bend=0.12, width=3))
body3.append(curved_arrow(1400-120, 244, 950+280, 396, RC_C, "gates", bend=-0.12, width=3))
body3.append(straight_arrow(950, 464, 950, 806, RC_C, width=3))
body3.append(straight_arrow(500, 694, 500, 1036, "#616161", width=3))
body3.append(straight_arrow(1400, 694, 1400, 1036, "#6a1b9a", width=3))

body3.append('<rect x="150" y="1230" width="1600" height="220" rx="10" fill="#fff3e0" stroke="#e65100" stroke-width="1.6"/>')
body3.append('<text x="950" y="1264" text-anchor="middle" font-size="15" font-weight="800" fill="#e65100">RC1 and RC2 are co-primary, not sequential:</text>')
body3.append('<text x="950" y="1290" text-anchor="middle" font-size="12.5" fill="#5d4037">RC1 generates the incentive problem; RC2 is why nobody with both the knowledge and the authority ever revisits RC1,</text>')
body3.append('<text x="950" y="1312" text-anchor="middle" font-size="12.5" fill="#5d4037">even once a working counterfactual (loop L6, the shock-adaptive precedent) exists inside the institution\'s own history.</text>')
body3.append('<text x="950" y="1338" text-anchor="middle" font-size="12.5" fill="#5d4037">RC3 sits between them: it is why RC2\'s fragmentation is never overcome by an unusually well-informed individual actor</text>')
body3.append('<text x="950" y="1360" text-anchor="middle" font-size="12.5" fill="#5d4037">simply escalating on their own initiative -- the escalation design itself only listens for complaint intensity, so a known-but-quiet</text>')
body3.append('<text x="950" y="1382" text-anchor="middle" font-size="12.5" fill="#5d4037">cost has no route upward regardless of who could, in principle, act on it.</text>')
body3.append('<text x="950" y="1420" text-anchor="middle" font-size="12" font-weight="700" fill="#e65100">Sharpest evidence for RC2: the institution already possesses a proven alternative (L6) and has never evaluated adopting it.</text>')

colors3 = [RC_C, INT_C, "#616161", "#6a1b9a"]
svg3 = wrap_svg(W3, H3, "\n".join(body3), extra_defs=marker_defs(colors3))
render(svg3, BASE + "diagram16-root-cause-network.png", W3, H3)
