import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

# ---------------------------------------------------------------- diagram 1: system boundary
def diagram1():
    c = Canvas(1240, 900, "System boundary", "What sits inside the breakfast system, on its edge and outside it")
    # inside
    c.zone(24, 84, 1192, 440, "INSIDE THE BOUNDARY", "tech", fs=14)
    # col A registration and billing
    c.zone(44, 116, 336, 392, "Registration and billing layer", "tech", fs=14, opacity=0.25)
    c.node(60, 150, 304, 72, "Students", "registered for every meal by default", "users", "ic-person")
    c.node(60, 234, 304, 72, "Dining portal", "register, cancel (5 per meal type per month), pay", "tech", "ic-phone")
    c.node(60, 318, 304, 72, "QR scan at the counter", "records who ate, and when", "tech", "ic-qr")
    c.node(60, 402, 304, 72, "Monthly bill", "follows registration, not attendance", "tech", "ic-coin")
    # col B kitchens
    c.zone(396, 116, 440, 392, "Kitchen layer: one operator per hall", "biz", fs=14, opacity=0.25)
    k1 = c.node(412, 150, 408, 66, "Kadamba: Prism", "on-site kitchen, first batch about 70% of registrations", "biz", "ic-pot")
    k2 = c.node(412, 226, 408, 66, "Yuktāhār: ABC Hospitality Services", "on-site kitchen, plans from its own books", "biz", "ic-book")
    k3 = c.node(412, 302, 408, 66, "Bakul: Vijayalakshmi Caterers", "Hafizpet kitchen about 8 km away, hot-held at the hall", "biz", "ic-truck")
    k4 = c.node(412, 378, 408, 50, "Palash: same off-site kitchen", "operator unconfirmed (candidate)", "biz", "ic-truck", dashed=True)
    c.node(412, 436, 408, 64, "Inside every kitchen", "quantity planning, food-safety checks, top-up, reuse, disposal", "slate", "ic-gear", fs=14)
    # col C governance
    c.zone(852, 116, 348, 392, "Governance layer", "soc", fs=14, opacity=0.25)
    c.node(868, 150, 316, 56, "Mess Committee", "menu and mess policy", "soc", "ic-briefcase", fs=14)
    c.node(868, 214, 316, 62, "Mess Office / CDS team", "portal and operations; identity unconfirmed", "soc", "ic-gear", fs=14, dashed=True)
    c.node(868, 284, 316, 56, "Warden", "vendor management, structural change", "soc", "ic-shield", fs=14)
    c.node(868, 348, 316, 62, "CFS, then CDS, then Prism", "the Kadamba operator's chain; CDS head unresolved", "soc", "ic-building", fs=14, dashed=True)
    c.node(868, 418, 316, 62, "Tender and contracts", "monthly lump sum on plates; basis unknown", "soc", "ic-coin", fs=14, dashed=True)

    # on the boundary
    c.zone(24, 540, 1192, 150, "ON THE BOUNDARY: exchange food, money or information, but are not run by the system", "ext", fs=13.5)
    bx = [("Suppliers", "three tiers: a week, 2 to 3 days, the day before", "ic-truck"),
          ("Garbage contractor", "the bin exit at Kadamba; no composting", "ic-bin"),
          ("Facility team and weekly QC", "safety and taste, not quantity", "ic-thermometer"),
          ("CDS site team", "relays complaints to operators", "ic-chat"),
          ("Non-student diners", "30 to 50 outsiders and about half of Kadamba's staff", "ic-people")]
    for i, (t, s, ic) in enumerate(bx):
        c.node(40 + i * 235, 580, 222, 90, t, s, "ext", ic, fs=14, sfs=12.5, dashed=True)

    # outside
    c.zone(24, 706, 1192, 170, "OUTSIDE THE BOUNDARY", "ext", fs=13.5, opacity=0.2)
    ox = [("Class schedule", "8:30 AM start, set by a separate authority", "ic-clock", "red"),
          ("Alternatives", "Vindhya Canteen, juice canteens, delivery apps", "ic-bowl", "ext"),
          ("Lunch and dinner", "same portal and rules, very different turnout: the comparison case", "ic-calendar-x", "ext"),
          ("Mess Cell", "student resale of unused registrations, run on WhatsApp", "ic-chat", "users")]
    for i, (t, s, ic, k) in enumerate(ox):
        c.node(40 + i * 293, 748, 280, 100, t, s, k, ic, fs=14.5, sfs=12.5)
    c.render("diagram1-system-boundary.png")

# ---------------------------------------------------------------- diagram 2: context map
def diagram2():
    c = Canvas(1240, 1070, "Context map", "Who administers, cooks, eats and absorbs surplus around the registration count")
    hub = c.node(470, 420, 300, 110, "Registration count", "automatic default for every student; flat across the week", "navy", "ic-toggle", fs=16, sfs=13, fill="#e8eaf6")
    stu = c.node(30, 410, 250, 130, "Students", "registered by default; may cancel 5 per meal type per month, 4 days ahead; Skip Meal returns nothing", "users", "ic-person", fs=16, sfs=12.5)
    mc = c.node(30, 590, 250, 90, "Mess Cell", "resale of unused registrations on WhatsApp", "users", "ic-chat", fs=14.5, sfs=12.5)
    cl = c.node(30, 110, 250, 90, "Academic office", "sets the 8:30 AM class start", "ext", "ic-building", fs=14.5, sfs=12.5)
    mo = c.node(430, 110, 380, 86, "Mess Office / CDS team (unconfirmed)", "administers the portal; operators read the registration count from it", "soc", "ic-gear", fs=14.5, sfs=12.5, dashed=True)
    mcm = c.node(850, 110, 340, 56, "Mess Committee", "menu and mess policy", "soc", "ic-briefcase", fs=14.5, sfs=12.5)
    war = c.node(850, 176, 340, 56, "Warden", "vendors, structural change", "soc", "ic-shield", fs=14.5, sfs=12.5)
    cfs = c.node(850, 242, 340, 96, "CFS, then CDS, then Prism", "the Kadamba operator's line of authority; the CDS head is one name from the operator and another from an earlier interview (unresolved)", "soc", "ic-building", fs=14, sfs=12, dashed=True)
    c.zone(850, 354, 360, 326, "Operators: own ratio on the day-before count", "biz", fs=12.5, opacity=0.25)
    kad = c.node(864, 386, 332, 78, "Kadamba: Prism", "fixed 70% first batch, supervisor tops up", "biz", "ic-pot", fs=14.5, sfs=12.5)
    yuk = c.node(864, 474, 332, 78, "Yuktāhār: ABC Hospitality", "books, matching-week lookup, first-half-hour check", "biz", "ic-book", fs=14.5, sfs=12.5)
    bak = c.node(864, 562, 332, 78, "Bakul: Vijayalakshmi Caterers", "70 to 80% by item, weekly; top-up by phone", "biz", "ic-truck", fs=14.5, sfs=12.5)
    pal = c.node(864, 648, 332, 30, "", "", "biz", None, dashed=True) if False else None
    cb = C["navy"][0]
    c.edge(stu, hub, C["users"][0], "registered automatically", width=3.2, lfs=11.5)
    c.edge(hub, mo, C["soc"][0], "administered by", dash="7 5", width=2.6, lfs=11.5, a_pt=(620, 418), b_pt=(620, 198))
    c.edge(hub, kad, cb, width=3.2, b_pt=(862, 425), bend=-0.04)
    c.edge(hub, yuk, cb, width=3.2, b_pt=(862, 513), a_pt=(772, 475))
    c.edge(hub, bak, cb, width=3.2, b_pt=(862, 601), bend=0.04)
    c.edge(mcm, mo, C["soc"][0], width=2.2, dash="7 5", a_pt=(846, 138), b_pt=(813, 150))
    c.edge(mc, stu, C["users"][0], "resell", width=2.6, dash="6 4", lfs=11.5, a_pt=(155, 588), b_pt=(155, 542))
    c.edge(cl, mo, C["red"][0], "no formal channel", dash="7 5", width=3, lfs=11.5, a_pt=(282, 150), b_pt=(428, 150))
    c.flag(30, 222, "The classroom clock and the mess clock are set by separate authorities.", "red", w=250, fs=12)
    c.add(f'<text x="868" y="656" font-size="12.5" fill="#00695c" font-weight="700">Palash: same off-site kitchen as Bakul;</text><text x="868" y="672" font-size="12.5" fill="#00695c" font-weight="700">operator unconfirmed (candidate)</text>')
    # surplus zone
    c.zone(410, 704, 780, 340, "Where the surplus goes", "green", fs=14, opacity=0.2)
    c.node(430, 754, 380, 90, "Extra diners at Kadamba", "30 to 50 outsiders and about half of the operator's staff eat from the same food", "green", "ic-people", fs=14.5, sfs=12.5)
    c.node(430, 856, 380, 80, "Reuse at Yuktāhār", "idli to idli upma or poha, batter to fridge, milk to curd", "green", "ic-bowl", fs=14.5, sfs=12.5)
    c.node(430, 948, 380, 72, "Held and reheated food", "Kadamba, candidate", "amber", "ic-flame", fs=14.5, sfs=12.5, dashed=True)
    c.node(830, 754, 340, 90, "Bin, then garbage contractor", "no composting at Kadamba; the exit for everything not eaten", "red", "ic-bin", fs=14.5, sfs=12.5)
    c.edge((620, 532), (620, 702), C["green"][0], "surplus after the first batch", width=3, lfs=11.5)
    c.legend(30, 740, [(cb, "registration flow", "line"), (C["biz"][0], "operators", "box"), (C["soc"][0], "governance (dashed = unconfirmed)", "dash"),
                       (C["green"][0], "surplus absorbed", "box"), (C["red"][0], "no channel / exit", "dash")], title="Reading the map")
    c.render("diagram2-context-map.png")

if __name__ == "__main__":
    diagram1(); diagram2()
