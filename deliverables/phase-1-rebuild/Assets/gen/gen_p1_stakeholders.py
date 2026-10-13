import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def sn(c, x, y, w, h, title, sub=None, key="tech", icon=None, dashed=False, fs=14, sfs=12):
    return c.node(x, y, w, h, title, sub, key, icon, dashed, fs=fs, sfs=sfs)

# ------------------------------------------------------------ diagram 3: four rings
def diagram3():
    c = Canvas(1300, 900, "Stakeholder map", "Twenty-four stakeholders in four rings: customer, internal, external, public")
    c.zone(14, 82, 1272, 806, "PUBLIC: informal, public-facing, no standing in the system", "soc", fs=13.5, opacity=0.18)
    for i, (t, s, ic) in enumerate([("Mess Cell", "resale of registrations on WhatsApp", "ic-chat"), ("Unofficial mess-tool developers", "alternative registration interface", "ic-phone"), ("Ping", "student publication", "ic-chat")]):
        sn(c, 36 + i * 420, 114, 392, 56, t, s, "soc", ic, fs=14.5)
    c.zone(40, 186, 1220, 690, "EXTERNAL: interact with the system's boundary from outside", "ext", fs=13.5, opacity=0.35)
    r1 = [("Academic administration", "timetable; latent", "ic-building"), ("Event and exam organisers", "latent demand shifters", "ic-calendar-x"),
          ("Facilities and Estate team", "latent", "ic-building"), ("Portal and IT system owner", "latent", "ic-gear"), ("Suppliers", "grocery, vegetables, milk, paneer, mills, LPG", "ic-truck")]
    nodes1 = []
    for i, (t, s, ic) in enumerate(r1):
        nodes1.append(sn(c, 60 + i * 238, 220, 226, 64, t, s, "ext", ic, dashed=(i < 4)))
    r2 = [("Non-student diners at Kadamba", "outsiders, half the staff", "ic-people"), ("Garbage contractor", "waste exit", "ic-bin"),
          ("Vindhya and juice canteens", "substitutes", "ic-bowl"), ("Delivery platforms and riders", "substitute", "ic-truck")]
    for i, (t, s, ic) in enumerate(r2):
        sn(c, 298 + i * 238, 298, 226, 70, t, s, "ext", ic)
    c.zone(76, 386, 1148, 474, "INTERNAL: the mess system's own operating structure", "biz", fs=13.5, opacity=0.2)
    gov = [("Mess Committee", "policy, menu", "ic-briefcase"), ("Mess Office", "candidate: CDS; rules and portal", "ic-gear"), ("CDS site team", "liaison with operators", "ic-chat"),
           ("Warden", "vendors, structural change", "ic-shield"), ("Student Parliament mess seats", "elected representation", "ic-cap")]
    gn = []
    for i, (t, s, ic) in enumerate(gov):
        gn.append(sn(c, 98 + i * 220, 418, 208, 66, t, s, "soc", ic, dashed=(i in (1, 2))))
    ops = [("Prism: Kadamba", "outsourced vendor, on-site kitchen", "ic-pot"), ("Vijayalakshmi: Bakul", "Hafizpet kitchen; Palash candidate", "ic-truck"),
           ("ABC Hospitality: Yuktāhār", "on-site kitchen, books", "ic-book"), ("Operator site management", "decides quantities and top-ups", "ic-gear")]
    on = []
    for i, (t, s, ic) in enumerate(ops):
        on.append(sn(c, 98 + i * 276, 506, 264, 70, t, s, "biz", ic))
    sn(c, 98, 592, 264, 50, "Serving and counter staff", None, "biz", "ic-people")
    sn(c, 374, 592, 264, 50, "Kitchen and cooking staff", None, "biz", "ic-pot")
    c.zone(300, 664, 700, 180, "CUSTOMER / USER", "users", fs=13.5, opacity=0.35)
    st = c.node(420, 700, 460, 120, "Students", "registrant, billed party, consumer; registered automatically, charged whether or not they eat", "users", "ic-person", fs=19, sfs=14)
    # edges
    c.edge((780, 698), (780, 578), C["biz"][0], "food, service", width=3.2, lfs=12)
    c.edge(gn[1], on[0], C["soc"][0], None, width=5, a_pt=(330, 486), b_pt=(250, 504))
    c.pill(430, 497, "contract chain", "soc", 11)
    c.edge(nodes1[0], gn[0], C["red"][0], "no confirmed relationship", dash="3 6", width=3, lfs=11.5, a_pt=(170, 286), b_pt=(190, 416), lpos=(282, 375))
    c.add(f'<text x="181" y="408" font-size="22" font-weight="800" fill="{C["red"][0]}">X</text>')
    c.legend(1020, 664, [(C["soc"][0], "institutional", "line"), ("#37474f", "directed flow", "line"), (C["red"][0], "no connection", "dash")], title="Relationships", fs=11.5)
    c.render("diagram3-stakeholder-map.png")

# ------------------------------------------------------------ diagram 4: relationship network
def diagram4():
    c = Canvas(1300, 1100, "Relationship network", "The same stakeholders by function: five clusters and the flows that connect them")
    c.zone(14, 82, 840, 290, "Governance, and latent institutional actors", "soc", fs=13.5, opacity=0.2)
    g = {}
    spec = [("Event and exam organisers", "calendar never reaches kitchens", 30, 118, False, "ext"), ("Facilities and Estate team", "identity unconfirmed", 296, 118, True, "ext"), ("Portal and IT owner", "named by no one", 562, 118, True, "ext"),
            ("Academic administration", "sets the 8:30 AM start", 30, 190, False, "ext"), ("Warden", "vendors, structural change", 296, 190, False, "soc"), ("Student Parliament mess seats", "elected channel", 562, 190, False, "soc"),
            ("Mess Committee", "menu and policy", 30, 262, False, "soc"), ("Mess Office (candidate: CDS)", "rules, portal, counts", 296, 262, True, "soc"), ("CDS site team", "WhatsApp link to operators", 562, 262, True, "soc")]
    for t_, s, x, y, d, k in spec:
        g[t_] = sn(c, x, y, 250, 62, t_, s, k, None, d, fs=13.5, sfs=11.5)
    c.zone(874, 82, 412, 290, "Supply and waste", "amber", fs=13.5, opacity=0.2)
    sn(c, 892, 118, 376, 76, "Suppliers", "three tiers: a week, 2 to 3 days, the day before; Yuktāhār checks an impurity norm per item", "amber", "ic-truck", fs=14, sfs=11.5)
    sn(c, 892, 208, 376, 70, "Garbage contractor", "Kadamba's exit for uneaten food; no composting; onward route unconfirmed", "red", "ic-bin", fs=14, sfs=11.5)
    sn(c, 892, 292, 376, 62, "Non-student diners at Kadamba", "30 to 50 outsiders and half the staff; a food sink", "green", "ic-people", fs=13.5, sfs=11.5)
    c.zone(14, 400, 1272, 400, "Operator interior: three different organisations", "biz", fs=13.5, opacity=0.18)
    c.zone(30, 432, 300, 354, "Kadamba: a ladder", "biz", fs=12.5, opacity=0.35)
    chain = ["CFS", "CDS (head unresolved)", "Prism (tender, runs everything)", "Operations manager", "Manager", "Supervisor: decides top-ups", "Service staff, about 10 chefs"]
    prev = None
    for i, t_ in enumerate(chain):
        nd = c.node(50, 460 + i * 46, 260, 34, t_, None, "biz", None, dashed=(i == 1), fs=12.5)
        if prev: c.edge(prev, nd, C["biz"][0], width=2.2)
        prev = nd
    c.zone(346, 432, 450, 354, "Yuktāhār: a flat ring of books and keepers", "biz", fs=12.5, opacity=0.35)
    cx, cy = 571, 610
    ctr = c.node(cx - 95, cy - 50, 190, 100, "The books", "Wastage, attendance, grocery, stock, vegetable, utilities, fridge", "slate", "ic-book", fs=13.5, sfs=10.5)
    sats = [("Two project managers", -1, -1), ("Mess in-charge: accounts, Wastage Book", 1, -1), ("Cross-verifier", -1, 0), ("Coordinator: registrations, board", 1, 0),
            ("Store function", -1, 1), ("Tasting, cutting, cleaning teams", 1, 1)]
    for t_, sx, sy in sats:
        px = (cx - 168 - 70) if sx < 0 else (cx + 168 - 70)
        py = cy + sy * 100 - 24
        nd = c.node(px, py, 140, 48, t_, None, "biz", None, fs=11.5)
        c.edge(ctr, nd, C["biz"][0], width=1.6)
    c.pill(571, 756, "no hierarchy: peers cross-check; mismatches go to the daily meeting", "biz", fs=11)
    c.zone(812, 432, 458, 354, "Bakul: two sites, one manager", "biz", fs=12.5, opacity=0.35)
    md = c.node(990, 466, 230, 40, "Operator's managing director", None, "biz", None, fs=12.5)
    mg = c.node(830, 546, 200, 92, "Bakul manager", "70 to 80% by item; weekly review; checks every 30 min; reserve for about 50 at 9:20", "biz", "ic-person", fs=13.5, sfs=10.5)
    hf = c.node(1082, 546, 170, 92, "Hafizpet kitchen", "about 8 km; 20 min early, 40 normal", "biz", "ic-truck", fs=13.5, sfs=11)
    c.edge(mg, hf, C["biz"][0], None, width=3, a_pt=(1034, 576), b_pt=(1080, 576))
    c.edge(hf, mg, C["biz"][0], None, width=3, a_pt=(1080, 610), b_pt=(1034, 610))
    c.pill(1042, 662, "phone top-up; insulated boxes, 60 to 72 °C", "biz", fs=11)
    c.edge((960, 544), (1040, 508), C["red"][0], "complaints go up", width=2.4, lfs=11, dash="6 4", lpos=(930, 524))
    c.node(830, 690, 420, 84, "Held only by the manager", "turnout estimate (at most about 60%), which items go (pav bhaji, muesli, Chocos), his view of pairings; whether anything is written down is unknown", "red", "ic-eye", dashed=True, fs=13, sfs=10.5)
    c.zone(14, 820, 800, 260, "Core daily operation", "users", fs=13.5, opacity=0.2)
    sn(c, 34, 856, 220, 80, "Students", "registered by default, billed on registration", "users", "ic-person", fs=15)
    sn(c, 274, 856, 250, 80, "Serving and counter staff", "second counter in the surge; scanner failures logged by hand", "biz", "ic-people", fs=13.5, sfs=11)
    sn(c, 544, 856, 250, 80, "Kitchen and cooking staff", "start 5:30; about 3 AM for Bakul's heavy items", "biz", "ic-pot", fs=13.5, sfs=11)
    sn(c, 34, 956, 760, 100, "Operator site management", "Kadamba's supervisor, Yuktāhār's coordinator and kitchen team, Bakul's manager: the only actors who watch the morning crowd as it happens", "biz", "ic-eye", fs=14, sfs=11.5)
    c.zone(834, 820, 452, 260, "Informal and competing", "pink", fs=13.5, opacity=0.2)
    inf = [("Mess Cell", "resale on WhatsApp", 852, 854), ("Mess-tool developers", "alternative interface", 1066, 854), ("Ping", "student press", 852, 924), ("Vindhya and juice canteens", "substitutes", 1066, 924), ("Delivery platforms and riders", "substitute, gate-restricted", 852, 994)]
    for t_, s, x, y in inf:
        sn(c, x, y, 200, 62, t_, s, "pink", None, fs=13, sfs=11)
    c.edge((420, 326), (250, 458), C["soc"][0], None, width=3.2, bend=0.0, a_pt=(400, 326), b_pt=(250, 458))
    c.pill(395, 386, "tender, counts, registration rules", "soc", fs=11)
    c.edge(g["Academic administration"], g["Mess Committee"], C["red"][0], "no channel", dash="3 6", width=2.6, lfs=11, a_pt=(155, 254), b_pt=(155, 260), lpos=(262, 258))
    c.edge((1000, 376), (1000, 430), C["amber"][0], None, width=3)
    c.pill(1000, 386, "stock in", "amber", fs=10.5)
    c.edge((1170, 430), (1170, 376), C["red"][0], None, width=3)
    c.pill(1170, 386, "waste out", "red", fs=10.5)
    c.render("diagram4-relationship-network.png")

# ------------------------------------------------------------ diagram 5: onion
def diagram5():
    W, H = 1100, 1170
    c = Canvas(W, H, "Proximity to a student's morning", "Closest to the student at the centre; furthest at the edge")
    cx, cy = 550, 650
    rings = [(500, "ext"), (400, "soc"), (300, "biz"), (200, "teal"), (105, "users")]
    for r, k in rings:
        s, f = C[k]
        c.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}" fill-opacity="0.55" stroke="{s}" stroke-width="2.2" stroke-dasharray="8 6"/>')
    for r, k, lab in [(500, "ext", "OUTERMOST"), (400, "soc", "GOVERNANCE AND SUPPLY"), (300, "biz", "OPERATORS"), (200, "teal", "ON THE FLOOR")]:
        c.add(f'<text x="{cx}" y="{cy - r + 22}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{C[k][0]}">{lab}</text>')
    def place(r, deg, title, w, h, key, dashed=False, sub=None, fs=12.5):
        a = math.radians(deg)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        c.node(x - w / 2, y - h / 2, w, h, title, sub, key, None, dashed, fs=fs, sfs=10.5)
    R5 = 450
    place(R5, -125, "Academic administration", 170, 50, "ext")
    place(R5, -55, "Event and exam organisers", 170, 50, "ext")
    place(R5, 195, "Facilities and Estate", 130, 50, "ext", True)
    place(R5, -15, "Portal and IT owner", 130, 50, "ext", True)
    place(R5, 125, "Vindhya and juice canteens", 170, 50, "ext")
    place(R5, 55, "Delivery platforms and riders", 170, 50, "ext")
    R4 = 352
    place(R4, -135, "Mess Committee", 140, 40, "soc")
    place(R4, -45, "Mess Office (candidate: CDS)", 160, 50, "soc", True)
    place(R4, 176, "CDS site team", 120, 40, "soc", True)
    place(R4, 4, "Warden", 100, 40, "soc")
    place(R4, 130, "Parliament mess seats", 140, 50, "soc")
    place(R4, 45, "Suppliers", 110, 40, "amber")
    place(R4, 90, "Garbage contractor", 150, 40, "red")
    R3 = 252
    place(R3, -150, "Prism (Kadamba)", 130, 40, "biz")
    place(R3, -90, "ABC (Yuktāhār)", 130, 40, "biz")
    place(R3, -30, "Vijayalakshmi (Bakul)", 140, 40, "biz")
    place(R3, 150, "Operator site management", 150, 50, "biz")
    place(R3, 30, "Non-student diners (Kadamba)", 150, 50, "green")
    R2 = 152
    place(R2, -90, "In-service deciders", 190, 68, "teal", False, "Kadamba supervisor, Yuktāhār coordinator and kitchen team, Bakul manager")
    place(R2, 150, "Kitchen and cooking staff", 130, 50, "teal")
    place(R2, 30, "Serving and counter staff", 130, 50, "teal")
    c.add(f'<circle cx="{cx}" cy="{cy-8}" r="34" fill="{C["users"][0]}"/><use href="#ic-person" x="{cx-20}" y="{cy-28}" width="40" height="40" fill="white"/>')
    c.add(f'<text x="{cx}" y="{cy+40}" text-anchor="middle" font-size="15" font-weight="800" fill="#1b1b1b">Students</text>')
    c.pill(cx - 55, cy - 74, "Mess Cell", "pink", 11)
    c.pill(cx + 55, cy - 74, "Ping", "pink", 11)
    c.pill(cx, cy + 74, "unofficial tools", "pink", 11)
    c.render("diagram5-onion-proximity.png")

if __name__ == "__main__":
    diagram3(); diagram4(); diagram5()
