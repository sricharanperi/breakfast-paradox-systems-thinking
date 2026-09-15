import sys
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import marker_defs, wrap_svg, render

BASE = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/deliverables/phase-2/assets/"


def card(cx, cy, icon, name, feel_label, feel, miss_label, miss, color, w=440, h=210):
    left = cx - w / 2
    top = cy - h / 2
    icon_r = 22
    out = f'<g><rect x="{left:.1f}" y="{top:.1f}" width="{w}" height="{h}" rx="16" fill="white" stroke="{color}" stroke-width="2.8"/>'
    out += f'<rect x="{left:.1f}" y="{top:.1f}" width="{w}" height="46" rx="16" fill="{color}"/>'
    out += f'<rect x="{left:.1f}" y="{top+24:.1f}" width="{w}" height="22" fill="{color}"/>'
    out += f'<circle cx="{left+34:.1f}" cy="{top+23:.1f}" r="{icon_r}" fill="white"/>'
    out += f'<use href="#{icon}" x="{left+34-16:.1f}" y="{top+23-16:.1f}" width="32" height="32" fill="{color}"/>'
    out += f'<text x="{left+66:.1f}" y="{top+30:.1f}" font-size="18" font-weight="800" fill="white">{name}</text>'
    ty = top + 78
    out += f'<text x="{left+22:.1f}" y="{ty:.1f}" font-size="12.5" font-weight="800" fill="{color}">{feel_label}</text>'
    for i, line in enumerate(feel):
        out += f'<text x="{left+22:.1f}" y="{ty+20+i*18:.1f}" font-size="12.5" fill="#232323">{line}</text>'
    ty2 = ty + 20 + len(feel) * 18 + 16
    out += f'<text x="{left+22:.1f}" y="{ty2:.1f}" font-size="12.5" font-weight="800" fill="#8a8a8a">{miss_label}</text>'
    for i, line in enumerate(miss):
        out += f'<text x="{left+22:.1f}" y="{ty2+20+i*18:.1f}" font-size="12.5" fill="#5a5a5a">{line}</text>'
    out += '</g>'
    return out


def stakeholder_grid():
    cols, rows = 4, 2
    cw, ch = 460, 220
    xgap, ygap = 30, 34
    W = 2020
    y0 = 175
    H = int(y0 + (rows - 1) * (ch + ygap) + ch / 2 + 90)
    body = []
    body.append(f'<text x="40" y="60" font-size="26" font-weight="800" fill="#0d47a1">What Each Stakeholder Actually Experiences</text>')
    cards = [
        ("ic-person", "Students", "#e65100", ["Charged for meals", "they can't use"], ["The aggregate cost, one", "lost meal isn't alarming"]),
        ("ic-pot", "Kitchen & Serving Staff", "#00695c", ["A rush at 9:20 with", "popular items gone"], ["Any channel to report", "what they see daily"]),
        ("ic-coin", "The Vendor", "#616161", ["Nothing, revenue is", "insulated from attendance"], ["Any reason to want", "this fixed (assumed)"]),
        ("ic-building", "CFS / CDS Office", "#1565c0", ["The workload behind", "the last policy change"], ["The gap as a daily pain,", "not just a number they hold"]),
        ("ic-people", "CDS Committee", "#6a1b9a", ["Menu satisfaction,", "already fixed once"], ["Visibility into what's", "eaten versus registered"]),
        ("ic-briefcase", "Academic Administration", "#616161", ["Nothing about the mess,", "their own timetable works"], ["Any consequence of the", "8:30 collision, any link at all"]),
        ("ic-person", "Faculty & Early-Shift Staff", "#616161", ["No confirmed", "mess access"], ["Any seat in the system's", "own stakeholder maps"]),
    ]
    x0 = (W - (cols * cw + (cols - 1) * xgap)) / 2 + cw / 2
    colors = []
    for i, (icon, name, color, feel, miss) in enumerate(cards):
        r, c = divmod(i, cols)
        cx = x0 + c * (cw + xgap)
        cy = y0 + r * (ch + ygap)
        body.append(card(cx, cy, icon, name, "EXPERIENCES", feel, "DOESN'T EXPERIENCE", miss, color, w=cw, h=ch))
        colors.append(color)
    body.append(f'<text x="{W/2:.0f}" y="{y0 + (rows-1)*(ch+ygap) + ch/2 + 55:.0f}" text-anchor="middle" font-size="15" fill="#444" font-style="italic">Nobody in this system experiences the Breakfast Paradox as their own problem.</text>')
    svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(list(set(colors))))
    render(svg, BASE + "diagram30-stakeholder-perspective-grid.png", W, H)


def reframe_iceberg():
    W, H = 2000, 1060
    body = []
    body.append(f'<text x="40" y="46" font-size="26" font-weight="800" fill="#0d47a1">Reading the Reframe Through the Iceberg</text>')
    bands = [
        (85, 230, "#e3f2fd", "EVENTS"),
        (230, 380, "#bbdefb", "PATTERNS"),
        (380, 690, "#5c9fd8", "STRUCTURES"),
        (690, 1010, "#0d3b66", "MENTAL MODELS"),
    ]
    for (y0, y1, fill, label) in bands:
        body.append(f'<rect x="0" y="{y0}" width="{W}" height="{y1-y0}" fill="{fill}"/>')
    tc = ["#0d47a1", "#0d47a1", "white", "white"]
    for i, (y0, y1, fill, label) in enumerate(bands):
        body.append(f'<text x="30" y="{y0+35}" font-size="15" font-weight="800" fill="{tc[i]}">{label}</text>')

    def row_chip(cx, cy, l1, l2, color, w, h, fill="white", text_color="#1b1b1b"):
        left = cx - w / 2
        out = f'<rect x="{left:.1f}" y="{cy-h/2:.1f}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{color}" stroke-width="2.4"/>'
        out += f'<text x="{cx:.1f}" y="{cy-4:.1f}" text-anchor="middle" font-size="13.5" font-weight="700" fill="{text_color}">{l1}</text>'
        if l2:
            out += f'<text x="{cx:.1f}" y="{cy+15:.1f}" text-anchor="middle" font-size="12" fill="#3a3a3a">{l2}</text>'
        return out

    body.append(row_chip(1070, 158, "A 48 rupee breakfast, booked and skipped almost every day", "plus a frog in the biryani, a tightened cancellation cap, and a fix already run twice", "#0d47a1", 1700, 100))
    body.append(row_chip(1070, 305, "Registration beats attendance every month, worst at breakfast", "no one interviewed ever got value from Skip Meal, and complaints sit until an incident forces a response", "#0d47a1", 1700, 100))

    structs = [
        ("Billing fires at", "registration, not consumption"),
        ("Decision rights split", "four ways, no single owner"),
        ("Feedback triages by", "how loud, not what it costs"),
        ("Skip Meal pays the", "student nothing back"),
    ]
    sw = 430
    x0 = 1000 - 1.5 * (sw + 20)
    for i, (l1, l2) in enumerate(structs):
        body.append(row_chip(x0 + i * (sw + 20), 535, l1, l2, "#0d3b66", sw, 150, fill="#eaf2fb"))

    models = [
        ("Registration count is treated", "as close enough to real demand"),
        ("Planning certainty is worth more", "than accuracy, as a fixed default"),
        ("A meal everyone should", "default into unless they opt out"),
    ]
    mw = 560
    mx0 = 1000 - 1.0 * (mw + 20)
    for i, (l1, l2) in enumerate(models):
        body.append(row_chip(mx0 + i * (mw + 20), 850, l1, l2, "#ffca28", mw, 150, fill="white", text_color="#0d3b66"))

    svg = wrap_svg(W, H, "\n".join(body), extra_defs=marker_defs(["#0d47a1", "#0d3b66", "#ffca28"]))
    render(svg, BASE + "diagram31-reframe-iceberg.png", W, H)


stakeholder_grid()
reframe_iceberg()
