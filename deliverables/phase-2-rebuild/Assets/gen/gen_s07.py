import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def cell(c, x, y, w, h, text, key, fs=12, dashed=False, bold=False):
    s, f = C[key]
    da = 'stroke-dasharray="5 4"' if dashed else ""
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{f}" fill-opacity="0.8" stroke="{s}" stroke-width="1.6" {da}/>')
    lines = wrap(text, w - 14, fs, bold)
    yy = y + (h - len(lines) * fs * 1.25) / 2 + fs * 0.95
    for ln in lines:
        c.add(f'<text x="{x+7}" y="{yy:.1f}" font-size="{fs}" font-weight="{700 if bold else 400}" fill="#1b1b1b">{esc(ln)}</text>'); yy += fs * 1.25

# ---------------------------------------------------------------- seven chains
def seven():
    c = Canvas(1300, 900, "The seven chains at a glance", "One visible event in each chain, traced down to the belief that holds it in place")
    heads = [("Event", "tech"), ("Pattern", "biz"), ("Structure", "soc"), ("Mental model", "red"), ("Root cause", "slate")]
    x0, lw, cw, g = 14, 176, 214, 6
    for i, (h, k) in enumerate(heads):
        s, f = C[k]
        c.add(f'<rect x="{x0+lw+g+i*(cw+g)}" y="82" width="{cw}" height="30" rx="8" fill="{s}"/><text x="{x0+lw+g+i*(cw+g)+cw/2}" y="102" font-size="14" font-weight="800" fill="white" text-anchor="middle">{h}</text>')
    rows = [("1  Registered, not showing up", "users", ["Sunday 6 Sept: 267 registered at Yuktāhār, 50 ate", "Flat 1,070 a day at Kadamba; turnout 27 to 42%", "Automatic default; five cancellations; billed at booking", "\"We have no opportunity to nullify it\"", "Billing tracks registration, not attendance"]),
            ("2  Food runs out at the close", "biz", ["Idli and puri gone by 9:20; Kadamba last scan 10:07", "26.5% of scans in 9:15 to 9:30; Sunday latest", "First batch fixed before any signal; top-up only upward", "\"The highest flow is in the last 10 minutes\"", "Late one-way top-up against a crest"]),
            ("3  Complaints ignored", "soc", ["Cap tightened Dec 2024; water complaints unheard in 2023", "A loud problem is fixed, a quiet one is not", "Menu, kitchen, calendar, billing with different owners; oversight on safety and taste only", "Consultation is optional; workload is the reason", "Nobody owns the whole picture; action follows loudness"]),
            ("4  A fix switched off", "tech", ["Gas shortage and holidays: no compulsory registration", "Worked every time; reverted every time", "No review exists; the cap has been moved before", "An automatic count beats matching demand", "The institution solved it twice and did not keep it"]),
            ("5  A fix and its shadow", "pink", ["Fortnightly menu rotation replaces a fixed semester menu", "Fatigue fell; turnout moves with the item", "Student Council, Parliament, Committee path worked", "Menu variety is worth a policy change", "Loud problems get fixed; visibility also enables avoidance"]),
            ("6  Not a problem at all", "green", ["A student fasts on purpose", "Late sleep, Sundays lowest, ceiling on variation", "Default registers the absent and fasting as no-shows", "Sleep outranks a booked breakfast", "A real slice, too small to explain the gap"]),
            ("7  Cook to a guess, absorb the rest", "amber", ["Site head sees 18.7%, still says about 50%", "70% batch is about 1.9 times turnout; surplus routes", "Three ratio regimes; records stay in the kitchen", "\"We are paid for the registration\"; \"waste is money\"", "Cooked food cannot be shrunk; the booking is upstream"])]
    y = 118
    for name, key, cells in rows:
        s, f = C[key]
        c.add(f'<rect x="{x0}" y="{y}" width="{lw}" height="102" rx="8" fill="{s}"/>')
        for i, ln in enumerate(wrap(name, lw - 16, 13.5, True)):
            c.add(f'<text x="{x0+9}" y="{y+22+i*17}" font-size="13.5" font-weight="800" fill="white">{esc(ln)}</text>')
        for i, t in enumerate(cells):
            cell(c, x0 + lw + g + i * (cw + g), y, cw, 102, t, key if i < 4 else "slate", 12.5)
        y += 108
    c.render("s07-seven-chains.png")

# ---------------------------------------------------------------- fix switch
def fix():
    c = Canvas(1200, 520, "Chain 4: the same breakfast under two models", "The institution has run both; it kept the one that bills the booking")
    c.zone(14, 84, 1172, 170, "Ordinary days: the standing default", "red", fs=14, opacity=0.18)
    a = [("Registered automatically", "every student, holidays included", "tech", "ic-toggle"), ("Five cancellations", "per meal type per month, 4 days ahead", "tech", "ic-calendar-x"), ("Billed at the booking", "eaten or not", "red", "ic-coin"), ("Flat count, 63% unused", "Kadamba, April", "red", "ic-chart")]
    n = [c.node(34 + i * 285, 130, 255, 90, t, s, k, ic, False, fs=14, sfs=12) for i, (t, s, k, ic) in enumerate(a)]
    for i in range(3): c.edge(n[i], n[i + 1], "#37474f", None, width=3)
    c.zone(14, 290, 1172, 170, "Gas shortage and holidays: the relaxed model", "green", fs=14, opacity=0.18)
    b = [("Registration not compulsory", "walk in and scan, or register 1 to 2 days ahead", "green", "ic-door"), ("Any of four messes", "no lock to one mess four days out", "green", "ic-building"), ("Billed on attendance", "no show, no charge", "green", "ic-coin"), ("No-show problem eased", "by the CFS Chair's account", "green", "ic-chart")]
    m = [c.node(34 + i * 285, 336, 255, 90, t, s, k, ic, False, fs=14, sfs=12) for i, (t, s, k, ic) in enumerate(b)]
    for i in range(3): c.edge(m[i], m[i + 1], "#37474f", None, width=3)
    c.edge((1060, 428), (1060, 480), C["red"][0], None, width=3, dash="7 5")
    c.pill(600, 486, "trigger passes: switched back off, with no review of keeping any part of it", "red", fs=13)
    c.render("s07-fix-switch.png")

# ---------------------------------------------------------------- root causes
def roots():
    c = Canvas(1200, 690, "Structural causes, conditions and the mechanism beneath them", "Three causes, two conditions that keep them unaddressed, one actionable mechanism")
    cs = [c.node(30 + i * 390, 90, 360, 96, t, s, "red", ic, False, fs=15, sfs=12) for i, (t, s, ic) in enumerate([
        ("1  Automatic standing default", "five cancellations, four days ahead; cannot follow the morning", "ic-toggle"),
        ("2  Billing at the booking", "an unused booking costs the system nothing", "ic-coin"),
        ("3  The gap is measured but unrouted", "scan records and operator books reach no rule owner", "ic-link-broken")])]
    sa = c.node(30, 250, 560, 80, "Students book and do not show", "flat count; 37% and about 28% turnout", "users", "ic-person", False, fs=15)
    sb = c.node(620, 250, 550, 80, "Nobody with authority sees the cost", "kitchens correct privately; rules never change", "soc", "ic-eye", False, fs=15)
    c.edge(cs[0], sa, "#37474f", None, width=3); c.edge(cs[1], sa, "#37474f", None, width=3); c.edge(cs[2], sb, "#37474f", None, width=3)
    rm = c.node(310, 400, 580, 110, "The uncalibrated conversion ratio", "fixed 70% at Kadamba; weekly judgement above a floor at Bakul; book lookup at Yuktāhār. Downstream of 1 to 3, inside authority operators already hold", "biz", "ic-scale", False, fs=15, sfs=12)
    c.edge((590, 332), (700, 398), "#37474f", None, width=3)
    ko = c.node(310, 560, 580, 80, "Kitchens cook more than is eaten, and run short at the crest", "calibration cuts waste and run-outs, not no-shows", "red", "ic-pot", False, fs=15, sfs=12)
    c.edge(rm, ko, "#37474f", None, width=3)
    c.zone(30, 400, 250, 240, "Two conditions", "amber", fs=13.5, opacity=0.25)
    c.node(42, 440, 226, 88, "Action follows loudness", "quiet numbers work only where the measurer decides", "amber", None, False, fs=13.5, sfs=11)
    c.node(42, 540, 226, 88, "The absorption layer", "resale, reuse, outsiders, reheating, late door, bin", "amber", None, False, fs=13.5, sfs=11)
    c.edge((270, 480), (24, 150), C["amber"][0], None, width=2.4, dash="6 5", bend=-0.0) if False else None
    c.add(f'<text x="920" y="470" font-size="12.5" fill="#444">The two conditions keep all three</text><text x="920" y="488" font-size="12.5" fill="#444">causes from being addressed.</text>')
    c.render("s07-root-causes.png")

# ---------------------------------------------------------------- ratio regimes
def regimes():
    c = Canvas(1200, 640, "Three regimes: how a registration becomes a first batch", "Each has a different record, delay and correction; none is calibrated to breakfast turnout")
    cols = [("Kadamba (Prism)", "biz", "ic-pot", ["Fixed 70% of registrations, veg and non-veg apart", "Gram standard for every dish", "No learning record", "Top-up by the supervisor in 10 to 15 minutes, upward only", "Single-sourced, observer-verified"]),
            ("Bakul (Vijayalakshmi)", "users", "ic-truck", ["70 to 80% by item, reset weekly by the manager's judgement", "Floor about 70% even on very low weekends", "Written record unknown", "Phone top-up from Hafizpet: cook plus a 20 to 40 minute drive", "Single-sourced; no Bakul records"]),
            ("Yuktāhār (ABC)", "tech", "ic-book", ["No fixed ratio: matching-week Wastage Book lookup", "Weekday register, month pattern, events if mentioned", "First-half-hour projection; re-cook by run-out time", "Two-week delay; calibrates items, not the headline belief", "Books confirmed; projection single-sourced"])]
    for i, (t, k, ic, items) in enumerate(cols):
        x = 30 + i * 390
        c.node(x, 90, 360, 64, t, None, k, ic, False, fs=16)
        for j, it in enumerate(items):
            cell(c, x, 170 + j * 64, 360, 56, it, k, 12.5)
    c.node(30, 510, 1140, 90, "Recorded breakfast turnout: 37.1% at Kadamba, about 28% at Yuktāhār; Bakul manager's estimate at most about 60% (no records)", "Every first batch sits above it, and every batch can be topped up but never shrunk", "red", "ic-warning", False, fs=15, sfs=13)
    c.render("s07-ratio-regimes.png")

# ---------------------------------------------------------------- archetypes
def arche():
    c = Canvas(1200, 800, "Two archetypes at work", "Shifting the burden (strong evidence); fixes that fail (candidate)")
    c.zone(14, 80, 1172, 330, "Shifting the burden: quick fixes carry the load so the real fix is never made", "soc", fs=14, opacity=0.15)
    sym = c.node(30, 118, 250, 214, "Symptom", "unused bookings; surplus cooked food", "red", "ic-warning", False, fs=15, sfs=12)
    qf = [c.node(340, 118 + i * 74, 300, 66, t, s, "amber", None, False, fs=13.5, sfs=11.5) for i, (t, s) in enumerate([("Quick fix: Mess Cell resale", "recovers the student's cost"), ("Quick fix: reuse, outsiders, reheating, bin", "clears each morning's surplus"), ("Quick fix: top-up and reserves", "keeps the counter full")])]
    for q in qf: c.edge(sym, q, C["amber"][0], None, width=2.4)
    rel = c.node(690, 160, 200, 100, "Relief", "pressure to fix the cause stays low", "green", "ic-eye", False, fs=15, sfs=12)
    for q in qf: c.edge(q, rel, C["green"][0], None, width=2.4)
    fu = c.node(985, 160, 190, 100, "Fundamental fix", "billing and booking rules; calibrated batch; routes to the rule owner", "biz", "ic-gear", True, fs=13.5, sfs=11)
    c.edge(rel, fu, C["red"][0], None, dash="7 5", width=2.6); c.pill(937, 150, "never made", "red", fs=11.5)
    c.add('<text x="700" y="300" font-size="12.5" fill="#444">Side effect at Kadamba: held food loses quality (candidate).</text>')
    c.add('<text x="30" y="380" font-size="12.5" fill="#444">Evidence: resale chain confirmed in quotes, last link assumed; absorbers observed at both halls.</text>')
    c.zone(14, 430, 1172, 340, "Fixes that fail: the fix works on its target and feeds the problem elsewhere (candidates)", "red", fs=14, opacity=0.15)
    rows = [("Cancellation cap tightened (Dec 2024)", "lower Mess Office workload", "more silent no-shows and resale, one account only"), ("Bakul's shortage floor, about 70%", "no shortage, even on very low weekends", "surplus on every slow morning; the reserve is the food held longest"), ("Kadamba's 70% batch with top-up", "few run-outs", "held and reheated food degrades quality")]
    for i, (a, b, d) in enumerate(rows):
        y = 480 + i * 92
        n1 = c.node(30, y, 360, 74, a, None, "tech", None, False, fs=14)
        n2 = c.node(440, y, 330, 74, "Intended effect", b, "green", None, False, fs=14, sfs=12)
        n3 = c.node(820, y, 350, 74, "Side effect", d, "red", None, False, fs=14, sfs=11.5)
        c.edge(n1, n2, "#37474f", None, width=2.6); c.edge(n2, n3, C["red"][0], None, width=2.6, dash="7 5")
    c.render("s07-archetypes.png")

# ---------------------------------------------------------------- tensions
def tensions():
    c = Canvas(1200, 800)
    pairs = [("A student registers broadly and resells: individually smart", "Everyone doing it: the waste and crowding"),
             ("Administration wants an automatic count", "The kitchen plans one day ahead, cooked food lasts 3 to 4 hours"),
             ("Cook once: simple, even quality", "Cook in stages: follows demand (aloo paratha softens in transit)"),
             ("Safety sequence before service", "Food cooked ahead is held and reheated (candidate)"),
             ("Cooking to registrations is a duty at Kadamba", "The duty generates the surplus"),
             ("Feed 30 to 50 outsiders and half the staff", "Cutting the first batch takes their food"),
             ("Avoid a shortage (visible, has a route upward)", "Avoid waste (silent, has no route)"),
             ("Tell students the menu in advance", "It also enables selective skipping"),
             ("Keep data on paper, close to the people", "It stays out of sight of the rule owners"),
             ("Escalation answers a loud problem", "Ignores a large, quiet one"),
             ("The 8:30 class start collides with breakfast", "The crest is latest on Sundays, with no classes")]
    c.add('<text x="30" y="52" font-size="26" font-weight="800" fill="#0d47a1">Eleven tensions: each pull is reasonable, and both act at once</text>')
    for i, (l, r) in enumerate(pairs):
        y = 76 + i * 64
        a = c.node(20, y, 520, 54, l, None, "tech", None, False, fs=13.5)
        b = c.node(660, y, 520, 54, r, None, "red" if i in (0, 4, 6, 9) else "amber", None, False, fs=13.5)
        c.add(f'<text x="600" y="{y+34}" font-size="26" font-weight="800" fill="#37474f" text-anchor="middle">&#8596;</text>')
    c.render("s07-tensions.png")

# ---------------------------------------------------------------- workarounds
def work():
    c = Canvas(1200, 790, "Workarounds: what was built around each gap", "Every one absorbs a cost that would otherwise force a fix")
    for i, (h, k) in enumerate([("The gap", "red"), ("The workaround", "green"), ("What it hides", "slate")]):
        s, f = C[k]
        c.add(f'<rect x="{20+i*395}" y="76" width="370" height="30" rx="8" fill="{s}"/><text x="{20+i*395+185}" y="96" font-size="14" font-weight="800" fill="white" text-anchor="middle">{h}</text>')
    rows = [("Students", "users", [("The charge cannot be removed; Skip Meal pays nothing", "Mess Cell resale (a friend eats on your registration)", "A resold meal still shows as eaten by the registrant"),
                                  ("Fixed window, fasting, other diets", "Eat elsewhere: canteen, juice stall, delivery", "Pays twice; a non-fit is counted as a no-show"),
                                  ("Item runs out, no restock", "Swap announced in a WhatsApp group", "No official record of shortage"),
                                  ("Popular mess fills", "Register the whole month defensively", "Inflates the count")]),
            ("Operators", "biz", [("First batch above turnout", "Reuse, outside diners and staff, reheating, the bin", "Surplus never becomes a number upstream"),
                                  ("Closing crest", "Back door, reserve of about 50, second roti counter", "A late crest is made safe, so it persists"),
                                  ("No calendar feed", "Events raised in the planning meeting", "Depends on someone mentioning them"),
                                  ("Scanner fails; no leave policy", "ID by hand; colleagues agree to cover", "Hand-logged diners may be missing from records")])]
    y = 128
    for name, key, rs in rows:
        s, f = C[key]
        h = len(rs) * 80 + 6
        c.add(f'<rect x="8" y="{y}" width="10" height="{h}" rx="4" fill="{s}"/>')
        c.add(f'<text x="30" y="{y-4}" font-size="12.5" font-weight="800" fill="{s}">{name.upper()}</text>')
        for j, (a, b, d) in enumerate(rs):
            yy = y + j * 80
            n1 = c.node(20, yy, 370, 72, a, None, "red", None, False, fs=13)
            n2 = c.node(415, yy, 370, 72, b, None, key, None, False, fs=13)
            n3 = c.node(810, yy, 370, 72, d, None, "ext", None, False, fs=13)
            c.edge(n1, n2, "#37474f", None, width=2.4); c.edge(n2, n3, "#37474f", None, width=2.4)
        y += h + 24
    c.render("s07-workarounds.png")

if __name__ == "__main__":
    seven(); fix(); roots(); regimes(); arche(); tensions(); work()
