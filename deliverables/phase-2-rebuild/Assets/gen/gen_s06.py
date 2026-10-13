import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *
G = "#37474f"

def system_map():
    c = Canvas(1250, 900, "The system at a glance", "Who decides, how a breakfast happens, what it runs on, and what holds it in place")
    c.zone(14, 84, 1222, 170, "WHO DECIDES", "soc", fs=13.5, opacity=0.2)
    cfs = c.node(34, 124, 170, 74, "CFS", "parent of CDS", "soc", "ic-building", fs=14.5)
    cds = c.node(234, 124, 270, 74, "CDS", "Committee, Student Council, hall admins; head: two names, open", "soc", "ic-gear", True, fs=14.5, sfs=11.5)
    ten = c.node(534, 124, 300, 74, "Open tender, one operator per hall", "Prism, ABC Hospitality, Vijayalakshmi Caterers", "biz", "ic-truck", fs=14.5, sfs=11.5)
    ac = c.node(870, 124, 350, 74, "Academic administration", "sets the 8:30 class start; no role in mess governance", "ext", "ic-building", fs=14.5, sfs=11.5)
    c.edge(cfs, cds, "#6a1b9a", None, width=3); c.edge(cds, ten, "#6a1b9a", None, width=3)
    c.edge((870, 161), (506, 161), C["red"][0], None, width=2.6, dash="6 5", bend=0.0) if False else None
    c.pill(1050, 218, "no channel to the mess", "red", fs=12)
    c.zone(14, 280, 1222, 190, "HOW A BREAKFAST HAPPENS", "tech", fs=13.5, opacity=0.2)
    st = [("Registration", "automatic default; five cancellations a month, four days ahead", "users", "ic-toggle"),
          ("Billing", "at the booking, monthly, eaten or not", "red", "ic-coin"),
          ("Planning, day before", "three regimes: fixed 70%, weekly judgement, books", "biz", "ic-book"),
          ("Cooking", "5:30 on site, 3 AM at Hafizpet; a batch only goes up", "biz", "ic-pot"),
          ("Service", "7:30 to 9:30; crest 9:15 to 9:30; back door after", "tech", "ic-clock"),
          ("Surplus", "reuse, outside diners, reheating, the bin", "green", "ic-bin")]
    ns = []
    for i, (t, s, k, ic) in enumerate(st):
        ns.append(c.node(30 + i * 202, 322, 190, 124, t, s, k, ic, fs=14, sfs=11.5))
    for a, b in zip(ns, ns[1:]): c.edge(a, b, G, None, width=3)
    c.edge((369, 200), (125, 320), "#6a1b9a", None, width=2.4, dash="6 5")
    c.edge((684, 200), (529, 320), "#00695c", None, width=2.4, dash="6 5")
    c.zone(14, 496, 1222, 140, "WHAT IT RUNS ON", "amber", fs=13.5, opacity=0.2)
    rs = [("Portal and scan record", "every registration and scan; exportable", "ic-qr"), ("Operators' own books", "Yuktāhār's Wastage Book and registers", "ic-book"),
          ("Kitchens and stores", "equipment, cold and dry stores", "ic-pot"), ("Suppliers in tiers", "a week, two to three days, the day before", "ic-truck")]
    for i, (t, s, ic) in enumerate(rs): c.node(34 + i * 303, 534, 285, 82, t, s, "amber", ic, fs=14, sfs=11.5)
    c.zone(14, 660, 1222, 214, "WHAT HOLDS IT IN PLACE", "red", fs=13.5, opacity=0.15)
    fl = ["The exit closes four days ahead; beyond five a month the charge cannot be removed", "Cooked food lasts three to four hours; a batch can be topped up, never shrunk", "The safety sequence fixes the batch before 7:30", "Operators control quantity, not the rules or the menu", "Records of the gap stay in the kitchen: no route to the rule owners"]
    for i, t in enumerate(fl): c.flag(34 + i * 240, 704 + (i % 2) * 76, t, "red", w=232, fs=12)
    c.render("s06-system-map.png")

def batch():
    c = Canvas(1100, 560, "First batch against turnout", "Solid bars are records; dashed bars are an operator's statement or belief")
    x0, w = 270, 780
    for v in range(0, 101, 20):
        x = x0 + v / 100 * w
        c.add(f'<line x1="{x:.0f}" y1="96" x2="{x:.0f}" y2="470" stroke="#e0e6ec" stroke-width="1.2"/><text x="{x:.0f}" y="490" font-size="12" fill="#555" text-anchor="middle">{v}%</text>')
    rows = [("Kadamba", [("first batch, operator", 70, None, "dash", "#e08600"), ("turnout, April scans", 37.1, None, "solid", "#1565c0")]),
            ("Yuktāhār", [("site head's belief", 50, None, "dash", "#e08600"), ("turnout, September register", 28.0, None, "solid", "#1565c0")]),
            ("Bakul", [("first batch, manager", 70, 80, "dash", "#e08600"), ("turnout, manager's estimate (at most)", 60, None, "dash", "#1565c0")])]
    for r, (name, bars) in enumerate(rows):
        y = 112 + r * 128
        c.add(f'<text x="30" y="{y+46}" font-size="17" font-weight="800" fill="#1b1b1b">{name}</text>')
        for b, (lab, v, v2, style, col) in enumerate(bars):
            yy = y + b * 52
            bw = v / 100 * w
            da = 'stroke-dasharray="7 5"' if style == "dash" else ""
            fill = "white" if style == "dash" else col
            c.add(f'<rect x="{x0}" y="{yy}" width="{bw:.0f}" height="40" rx="5" fill="{fill}" fill-opacity="{0.9 if style=="solid" else 1}" stroke="{col}" stroke-width="3" {da}/>')
            if v2:
                c.add(f'<rect x="{x0+bw:.0f}" y="{yy}" width="{(v2-v)/100*w:.0f}" height="40" rx="5" fill="{col}" fill-opacity="0.25" stroke="{col}" stroke-width="3" {da}/>')
            lab_v = f"{v:g}%" if not v2 else f"{v:g} to {v2:g}%"
            c.add(f'<text x="{x0+8}" y="{yy+26}" font-size="14" font-weight="800" fill="{"#1b1b1b" if style=="dash" else "white"}">{lab_v}</text>')
            c.add(f'<text x="{x0+(max(v, v2 or 0))/100*w+10:.0f}" y="{yy+25}" font-size="13" fill="#444">{esc(lab)}</text>')
    c.add(f'<text x="30" y="535" font-size="12.5" fill="#555">Bakul has no records: both bars are the manager\'s statements. Its floor is about 70% even on low weekends.</text>'.replace("\\'", "'"))
    c.render("s06-batch-vs-turnout.png")

def books():
    c = Canvas(1200, 800, "Yuktāhār's books and how they feed each other", "Each book was photographed (confirmed); the connections are the operator's account (single-sourced)")
    c.zone(14, 84, 300, 360, "READ AT THE MEETING", "soc", fs=13, opacity=0.2)
    ins = [("Portal registrations", "regular, Jain, cash: the Grocery Book header"), ("Wastage Book, matching week", "from two weeks ago"), ("Weekday attendance register", "all Sundays together, all Mondays together"), ("Month's pattern and events", "only if someone raises them")]
    inn = [c.node(30, 116 + i * 82, 268, 70, t, s, "soc", None, False, fs=13, sfs=11) for i, (t, s) in enumerate(ins)]
    mt = c.node(470, 190, 250, 150, "Daily planning meeting", "twice a day; storekeeper, coordinator, kitchen staff; raises discrepancies; reads the inputs and fixes tomorrow's issue", "biz", "ic-people", fs=15, sfs=12)
    for n in inn: c.edge(n, mt, G, None, width=2.4)
    c.zone(880, 84, 306, 360, "ISSUE AND PURCHASING", "amber", fs=13, opacity=0.2)
    outs = [("Store book", "kilograms per dish"), ("Grocery Book issue", "breakfast, lunch, snacks, dinner; running balance"), ("Stock register", "receipts and issues; agrees with the Grocery Book"), ("Fortnightly purchasing", "vegetables two to three times a week")]
    on = [c.node(896, 116 + i * 82, 276, 70, t, s, "amber", None, False, fs=13, sfs=11) for i, (t, s) in enumerate(outs)]
    c.edge(mt, on[0], G, None, width=2.6)
    for a, b in zip(on, on[1:]): c.edge(a, b, G, None, width=2.2, a_pt=(a.cx, a.y + a.h + 2), b_pt=(b.cx, b.y - 2))
    c.pill(595, 392, "two-book check: issued must equal cooked", "soc", fs=12)
    c.zone(14, 470, 1172, 190, "AFTER EACH MEAL", "slate", fs=13, opacity=0.2)
    wb = c.node(30, 506, 300, 100, "Wastage Book", "issued, cooked, left, %, run-out time, re-cook, plate waste plus leftover", "slate", "ic-book", fs=14, sfs=11.5)
    bd = c.node(370, 506, 250, 100, "Wastage board", "the coordinator's target: push the waste share down", "slate", "ic-chart", fs=14, sfs=11.5)
    vg = c.node(660, 506, 250, 100, "Vegetable book and indent", "spoilage remarks: \"3 spoiled\"", "slate", "ic-bowl", fs=14, sfs=11.5)
    ut = c.node(950, 506, 236, 100, "Utility and fridge logs", "milk, fruit, gas, electricity, water; fridge three times a day", "slate", "ic-thermometer", fs=14, sfs=11.5)
    c.edge(wb, bd, G, None, width=2.4)
    c.edge((130, 504), (130, 448), "#6a1b9a", "read again in two weeks", width=2.6, dash="6 4", lfs=11.5, lpos=(130, 478))
    rule = c.node(30, 690, 460, 74, "CDS, Mess Office, menu owner", "no book, record or figure reaches them", "red", "ic-link-broken", True, fs=14, sfs=12)
    c.edge((180, 608), (180, 688), C["red"][0], None, width=3, dash="6 5")
    c.pill(300, 650, "no outbound route", "red", fs=12)
    c.text(530, 720, "Records reconcile materials, not diners: for 3 September the Wastage Book shows 77 breakfasts and the attendance register 110.", 13, False, "#444", width=640)
    c.render("s06-book-network.png")

def blueprint():
    c = Canvas(1200, 800, "Service blueprint: one breakfast across the line of visibility", "Kadamba and Yuktāhār on site; Bakul's differences in the lowest lane")
    cols = ["Day before to 7:30", "7:30 to 9:00", "9:15 to 9:30, the crest", "After 9:30"]
    X0, CW = 160, 258
    for i, t in enumerate(cols):
        c.add(f'<rect x="{X0+i*(CW+6)}" y="80" width="{CW}" height="34" rx="8" fill="#37474f"/><text x="{X0+i*(CW+6)+CW/2}" y="102" font-size="13.5" font-weight="800" fill="white" text-anchor="middle">{t}</text>')
    lanes = [("Student sees", "users", 130, [("Registered automatically", "nothing to decide; billed at the booking"), ("Display plate, queue, QR scan", "wrapped plate shows the menu, never quantity"), ("Items run out", "idli, puri and bhatura go first; staff promise a restock"), ("Front door shuts at 9:30", "latecomers use the back door and are served")]),
             ("Kitchen reacts", "biz", 340, [("Count read; first batch set", "fixed 70%, weekly judgement or books; safety sequence before 7:30"), ("Supervisor reads item levels", "Yuktāhār projects from the first half hour; checks every 30 minutes"), ("Top-up, upward only", "10 to 15 minutes at Kadamba; Bakul phones Hafizpet"), ("Door reopened for 5 to 10 minutes", "surplus to outside diners, reuse or the bin")]),
             ("Support", "tech", 550, [("Portal count; prep from 3 AM at Hafizpet", "the count is the only input", ), ("Scan count; Hafizpet food arrives about 7", "hot-water holding at Bakul"), ("Bakul holds a reserve of about 50 at 9:20", "a late top-up cannot land in time (candidate)"), ("Wastage Book entry at Yuktāhār", "read again two weeks later")])]
    for name, key, y, cells in lanes:
        s, f = C[key]
        c.add(f'<rect x="14" y="{y}" width="{X0-24}" height="190" rx="10" fill="{s}"/><text x="{14+(X0-24)/2}" y="{y+100}" font-size="14" font-weight="800" fill="white" text-anchor="middle">{name}</text>')
        for i, (t, sub) in enumerate(cells):
            c.node(X0 + i * (CW + 6), y + 12, CW, 166, t, sub, key, None, False, fs=14, sfs=12)
    c.add(f'<line x1="14" y1="326" x2="1200" y2="326" stroke="{C["red"][0]}" stroke-width="3" stroke-dasharray="10 6"/>')
    c.pill(1070, 326, "line of visibility", "red", fs=12)
    c.pill(300, 326, "the display plate crosses the line", "green", fs=11.5)
    c.pill(760, 326, "nothing about what was left over crosses it", "red", fs=11.5)
    c.render("s06-blueprint.png")

def governance():
    c = Canvas(1200, 820, "CDS, CFS and the vendors: three routes", "The complaint route works for incidents; the escalation route changed the menu once; no route carries the records to the rules")
    cfs = c.node(30, 92, 160, 70, "CFS", "parent department", "soc", "ic-building", fs=15)
    cds = c.node(230, 92, 290, 70, "CDS", "head: two names on record, unresolved", "soc", "ic-gear", True, fs=15, sfs=11.5)
    com = c.node(570, 92, 270, 70, "CDS Committee", "faculty, final say", "soc", "ic-briefcase", fs=15, sfs=11.5)
    sc = c.node(890, 92, 280, 70, "CDS Student Council", "drafts and first-reviews proposals", "soc", "ic-cap", fs=15, sfs=11.5)
    c.edge(cfs, cds, "#6a1b9a", None, width=3); c.edge(cds, com, "#6a1b9a", None, width=3); c.edge(sc, com, "#6a1b9a", "high-intensity feedback", width=3, lfs=11.5, lpos=(865, 200)) if False else c.edge(sc, com, "#6a1b9a", None, width=3)
    c.node(230, 196, 290, 58, "CFS Head", "handles low-intensity feedback directly", "soc", None, False, fs=14, sfs=11.5)
    c.node(570, 196, 600, 58, "Worked once: one fixed menu for the semester became a fortnightly rotation (L4)", "complaint, Student Council, Committee, rotation; confirmed by the person who ran it", "green", "ic-calendar-x", fs=13.5, sfs=11.5)
    c.zone(14, 290, 1172, 190, "CONTRACT: CDS tenders each hall to a vendor that runs the kitchen", "biz", fs=13, opacity=0.2)
    c.node(34, 330, 370, 130, "Prism, Kadamba", "layered chain: operations manager, manager, supervisor, service staff; facility team tastes beside it", "biz", "ic-pot", fs=14.5, sfs=11.5)
    c.node(425, 330, 340, 130, "ABC Hospitality, Yuktāhār", "flat: two project managers, no hierarchy, daily meeting, peer cross-checking", "biz", "ic-book", fs=14.5, sfs=11.5)
    c.node(786, 330, 380, 130, "Vijayalakshmi Caterers, Bakul", "manager at the mess, kitchen at Hafizpet, managing director above; Palash a candidate", "biz", "ic-truck", fs=14.5, sfs=11.5)
    c.edge((375, 164), (215, 328), "#00695c", None, width=2.4, dash="6 5")
    c.zone(14, 504, 1172, 130, "COMPLAINT ROUTE: exists, works for same-incident fixes", "green", fs=13, opacity=0.2)
    rt = ["Student, director's email or CDS site team", "Operator's manager", "WhatsApp group (Kadamba) or the kitchen and managing director (Bakul)", "Fix on the day"]
    rn = [c.node(30 + i * 292, 540, 270, 80, t, None, "green", None, False, fs=13.5) for i, t in enumerate(rt)]
    for a, b in zip(rn, rn[1:]): c.edge(a, b, C["green"][0], None, width=3)
    c.zone(14, 660, 1172, 140, "RULE-CHANGE ROUTE: absent", "red", fs=13, opacity=0.15)
    a = c.node(30, 696, 440, 80, "Operators' books and the CDS scan records", "the gap is measured here, daily", "slate", "ic-chart", fs=14, sfs=12)
    b = c.node(700, 696, 470, 80, "Owners of registration, billing and menu rules", "split across offices; none holds knowledge and authority", "red", "ic-gear", True, fs=14, sfs=12)
    c.edge(a, b, C["red"][0], None, width=3.2, dash="8 6")
    c.pill(585, 700, "no route", "red", fs=12.5)
    c.render("s06-governance.png")

def bottlenecks():
    c = Canvas(1200, 650, "The bottleneck chain", "From the booking to a shortage and a surplus on the same morning, and what keeps each link in place")
    ch = [("Standing booking", "automatic default", "users"), ("Flat count", "about 1,070 a day at Kadamba", "tech"), ("Ratio applied", "fixed, judged or learned", "biz"), ("First batch cooked", "can go up, never down", "biz"), ("Crest meets top-up", "last fifteen minutes", "red"), ("Shortage and surplus", "the same morning", "red")]
    ns = [c.node(12 + i * 200, 110, 176, 110, t, s, k, None, False, fs=14.5, sfs=12) for i, (t, s, k) in enumerate(ch)]
    for a, b in zip(ns, ns[1:]): c.edge(a, b, G, None, width=3)
    keep = ["Exit closes four days ahead; beyond five a month the charge stands", "Billing at the booking; nothing rewards accuracy", "At Kadamba no record returns to the ratio; Bakul holds a floor", "Safety checks commit it before 7:30; cooked food lasts three to four hours", "Kadamba tops up in 10 to 15 minutes; Bakul needs a call, cooking and a 20 to 40 minute drive", "A shortage is loud and reaches a complaint route; a surplus is silent"]
    for i, t in enumerate(keep):
        c.flag(12 + i * 200, 260, t, "amber", w=184, fs=11.5)
    r = c.node(12, 470, 560, 90, "Absorbers take the surplus", "reuse, outside diners and staff, reheating (candidate), the bin; each does real good", "green", "ic-people", fs=14.5, sfs=12)
    z = c.node(640, 470, 546, 90, "The record of the gap stays in the kitchen", "no link back to the booking, the bill or the rule owner", "red", "ic-link-broken", True, fs=14.5, sfs=12)
    c.edge((1100, 224), (1000, 468), C["red"][0], None, width=2.8, dash="7 5")
    c.edge((1100, 224), (320, 468), C["green"][0], None, width=2.8, bend=0.08)
    c.render("s06-bottlenecks.png")

if __name__ == "__main__":
    system_map(); batch(); books(); blueprint(); governance(); bottlenecks()
