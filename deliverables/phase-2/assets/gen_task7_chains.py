import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import chip, curved_arrow, marker_defs, wrap_svg, render

BASE = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/"

def chain_diagram(title, event, pattern, structures, mental_models, out_name):
    W, H = 2000, 1030
    body = []
    body.append(f'<text x="40" y="46" font-size="26" font-weight="800" fill="#0d47a1">{title}</text>')

    bands = [
        (85, 250, "#e3f2fd", "EVENT"),
        (250, 415, "#bbdefb", "PATTERN"),
        (415, 700, "#5c9fd8", "STRUCTURE"),
        (700, 1000, "#0d3b66", "MENTAL MODEL"),
    ]
    for (y0, y1, fill, label) in bands:
        body.append(f'<rect x="0" y="{y0}" width="{W}" height="{y1-y0}" fill="{fill}"/>')
    tc = ["#0d47a1", "#0d47a1", "white", "white"]
    for i, (y0, y1, fill, label) in enumerate(bands):
        body.append(f'<text x="30" y="{y0+35}" font-size="15" font-weight="800" fill="{tc[i]}">{label}</text>')

    EC = "#0d47a1"
    body.append(chip(1050, 168, "ic-warning", event[0], event[1] if len(event) > 1 else "", EC, w=1600, h=90))

    body.append(chip(1050, 332, "ic-calendar-x", pattern[0], pattern[1] if len(pattern) > 1 else "", EC, w=1600, h=90))

    n = len(structures)
    sw = min(620, int(1900 / max(n, 1)) - 20)
    x0 = 1050 - (n - 1) * (sw + 20) / 2
    for i, (l1, l2) in enumerate(structures):
        body.append(chip(x0 + i * (sw + 20), 555, "ic-briefcase", l1, l2, "#0d3b66", w=sw, h=140, fill="#eaf2fb"))

    m = len(mental_models)
    mw = min(900, int(1900 / max(m, 1)) - 20)
    mx0 = 1050 - (m - 1) * (mw + 20) / 2
    for i, (l1, l2) in enumerate(mental_models):
        body.append(chip(mx0 + i * (mw + 20), 850, "ic-person", l1, l2, "#ffca28", w=mw, h=140, fill="white", text_color="#0d3b66"))

    svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs([EC, "#0d3b66", "#ffca28"]))
    render(svg, BASE + out_name, W, H)


chain_diagram(
    "Chain 1: Students register and don't show up",
    ("Books Kadamba veg breakfast at 48 rupees", "every day, skips it most days"),
    ("Breakfast turnout runs 35 to 45 percent,", "against 70 to 90 percent for other meals"),
    [
        ("Billing follows registration,", "not attendance"),
        ("Mess Cell WhatsApp market", "lets a slot be resold"),
        ("Skip Meal pays the", "student nothing back"),
    ],
    [
        ("Institution: registration numbers", "are close enough to real demand"),
        ("Student: showing up or not", "costs the same either way"),
    ],
    "diagram18-chain1-registration.png",
)

chain_diagram(
    "Chain 2: Food runs out before the mess closes",
    ("Idli, puri, and bhatura are gone", "by 9:20 most mornings at Kadamba"),
    ("The same few items run out", "near the same time, most days"),
    [
        ("One average portion size", "applied to every item"),
        ("Four day order lock,", "no same day fix"),
        ("One person runs all", "storage, no backup"),
    ],
    [
        ("Kitchen planning: an average", "number is fair across every item"),
    ],
    "diagram19-chain2-runouts.png",
)

chain_diagram(
    "Chain 3: Complaints get ignored until something forces a response",
    ("A frog in the biryani, Nov 2024,", "non veg pulled with no explanation given"),
    ("A complaint sits until a bigger", "incident forces the issue"),
    [
        ("No committee sign-off", "confirmed before a change"),
        ("Menu, kitchen, calendar, and billing", "sit with four separate owners"),
    ],
    [
        ("Mess Office: this is ours to decide,", "consultation is optional under pressure"),
    ],
    "diagram20-chain3-complaints.png",
)

chain_diagram(
    "Chain 4: A working fix already exists and gets switched off anyway",
    ("Registration made optional during a shortage", "and during holidays, no bill if you skip"),
    ("It worked every time it ran,", "and got switched off every time"),
    [
        ("Vendor's four day lock needs", "a knowable headcount"),
        ("Nothing evaluates keeping", "any part of it permanently"),
    ],
    [
        ("Procurement certainty matters more", "than matching real demand, as a permanent default"),
    ],
    "diagram21-chain4-shelved-fix.png",
)

chain_diagram(
    "Chain 5: A real fix, and the shadow it cast",
    ("Council and Parliament moved a fixed", "semester menu to a two week rotation"),
    ("Fatigue complaints dropped;", "selective skipping is now a live question"),
    [
        ("A real escalation path,", "council to parliament to committee"),
        ("Menu now posted", "two weeks ahead"),
    ],
    [
        ("CDS: menu variety is worth", "pushing a real change for"),
        ("CDS: more transparency is automatically", "good, now being doubted"),
    ],
    "diagram22-chain5-menu-rotation.png",
)

chain_diagram(
    "Chain 6: A meaningful slice of this isn't a problem at all",
    ("“I don’t usually see the mess,”", "despite living in the same hostel"),
    ("Late sleep is named far more often", "than food quality or class timing"),
    [
        ("Breakfast pulls far less company", "than lunch does"),
        ("Only Yuktahar offers separate", "Jain and pure veg lines"),
    ],
    [
        ("Sleep matters more than a booked", "breakfast the moment the two clash"),
    ],
    "diagram23-chain6-invisible-mess.png",
)

print("done")
