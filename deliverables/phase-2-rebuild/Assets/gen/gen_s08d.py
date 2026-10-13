import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def ladder():
    c = Canvas(1200, 600, "Where intervening pays", "Five layers of the iceberg, read against the evidence")
    rows = [("Events", "Persuade students: reminders, nudges, campaigns", "Fights the structure for good; some skipping is legitimate", "red", "ic-person"),
            ("Parameters", "Cancellation cap (5 to 10 to 5); first-batch ratio", "Moves the pressure, not its source; a lower ratio shifts cost to run-outs", "amber", "ic-scale"),
            ("Structures", "Automatic default and its exit; billing at the booking", "Where the booking is set; gated on how a plate is paid", "tech", "ic-toggle"),
            ("Information flows", "Scan records and operators' books reach no rule owner", "Highest yield: the records already exist", "green", "ic-link-broken"),
            ("Mental models", "A count stands for demand; certainty four days out is worth more", "Hardest and most durable; both beliefs were suspended before", "soc", "ic-eye")]
    y = 82
    c.add(f'<text x="260" y="{y-6}" font-size="13" font-weight="800" fill="#37474f">What sits here</text><text x="760" y="{y-6}" font-size="13" font-weight="800" fill="#37474f">What the evidence says</text>')
    for i, (t, a, b, k, ic) in enumerate(rows):
        yy = y + i * 98
        c.node(30, yy, 210, 84, t, None, k, ic, fs=16)
        c.node(260, yy, 480, 84, a, None, k, None, fs=13.5)
        c.node(760, yy, 410, 84, b, None, k, None, fs=13.5)
        c.add(f'<path d="M 242 {yy+42} L 258 {yy+42}" stroke="#90a4ae" stroke-width="3"/><path d="M 742 {yy+42} L 758 {yy+42}" stroke="#90a4ae" stroke-width="3"/>')
    c.render("s08d-leverage-ladder.png")

def four_points():
    c = Canvas(1200, 640, "Four intervention points on the chain from booking to bin", "One in the kitchen, three in governance")
    ch = [("Default booking", "ic-toggle", "users"), ("Day-before plan", "ic-book", "biz"), ("First batch, 5:30", "ic-pot", "biz"), ("Service and crest", "ic-clock", "tech"), ("Surplus, then bin", "ic-bin", "red")]
    ns = []
    for i, (t, ic, k) in enumerate(ch):
        n = c.node(30 + i * 232, 330, 206, 80, t, None, k, ic, fs=15)
        ns.append(n)
        if i: c.edge(ns[i-1], n, "#37474f", None, width=3)
    c.node(30, 100, 520, 150, "4.1 Process", "feed recorded turnout, by hall, weekday and line, into the day-before plan; keep every top-up path", "biz", "ic-gear", fs=16, sfs=13)
    c.edge((290, 252), (400, 328), C["biz"][0], None, width=3)
    c.node(580, 180, 590, 70, "4.2 Rule", "what a registration is, how it is left, what it costs", "tech", "ic-toggle", fs=16, sfs=13)
    c.edge((700, 252), (140, 328), C["tech"][0], None, width=3, bend=-0.08)
    c.node(580, 100, 590, 70, "4.3 Decision rights", "one owner of booked, cooked and eaten", "soc", "ic-briefcase", fs=16, sfs=13)
    c.node(30, 450, 1140, 80, "4.4 Information flow", "a cost trigger beside the complaint trigger, on one agreed meaning of \"ate\"; routes from the scan records and the operators' books up to the rule owner", "green", "ic-link-broken", fs=16, sfs=13)
    c.edge((600, 448), (600, 412), C["green"][0], None, width=3)
    c.pill(600, 575, "secondary areas: food quality as eaten, demand by item, menu pairings", "ext", fs=13)
    c.render("s08d-four-points.png")

def guardrails():
    c = Canvas(1200, 640, "Guardrails for any intervention", "Keep what protects people; target only what protects no one; leave the students and the timetable alone")
    c.zone(20, 80, 380, 300, "KEEP (absorbers that feed or pay people)", "green", fs=13)
    for i, t in enumerate(["Resale on Mess Cell", "Reuse at Yuktāhār", "Outside diners and half of Kadamba's staff", "Top-ups, walk-in buffer, late service"]):
        c.node(36, 112 + i * 64, 348, 54, t, None, "green", None, fs=13.5)
    c.zone(420, 80, 360, 300, "TARGET (protect no one)", "red", fs=13)
    for i, t in enumerate(["The over-cooked first batch", "Repeated reheating into later service", "The bin"]):
        c.node(436, 112 + i * 64, 328, 54, t, None, "red", None, fs=13.5)
    c.zone(800, 80, 380, 300, "LEAVE ALONE", "ext", fs=13)
    for i, t in enumerate(["The 8:30 class start", "Safety steps before service", "Students as the target of the fix", "Operators as the blamed party"]):
        c.node(816, 112 + i * 64, 348, 54, t, None, "ext", None, fs=13.5)
    c.node(20, 410, 560, 90, "Act before the first batch", "the evening before or at the planning meeting; the morning only through the top-up", "tech", "ic-clock", fs=15, sfs=12.5)
    c.node(600, 410, 580, 90, "No waste cut that raises shortage risk", "shortage is the failure students feel; Bakul states it as its rule", "amber", "ic-warning", fs=15, sfs=12.5)
    c.node(20, 516, 560, 90, "Measure cooked against eaten, with run-outs and quality", "turnout alone is not success", "biz", "ic-scale", fs=15, sfs=12.5)
    c.node(600, 516, 580, 90, "Blame-free, paper-first measurement", "start from the books and the daily meeting, not new software", "biz", "ic-book", fs=15, sfs=12.5)
    c.render("s08d-guardrails.png")

def interaction():
    c = Canvas(1200, 420, "How the four fit together", "Bottom-up in cost, top-down in impact")
    st = [("1", "4.4 Information flow", "route what is already measured; agree one meaning of \"ate\"", "green"), ("2", "4.1 Process", "calibrate the first batch to the records; keep top-ups", "biz"), ("3", "4.3 Decision rights", "name an owner so the signal has an addressee", "soc"), ("4", "4.2 Rule", "change the default, the exit and the charge; scope to breakfast; gated", "tech")]
    ns = []
    for i, (n_, t, s, k) in enumerate(st):
        nd = c.node(30 + i * 292, 120, 270, 130, t, s, k, None, fs=15, sfs=12.5)
        c.badge(30 + i * 292 + 18, 120, n_, C[k][0], r=15)
        ns.append(nd)
        if i: c.edge(ns[i-1], nd, "#37474f", None, width=3)
    c.add('<text x="30" y="290" font-size="13" fill="#2e7d32" font-weight="700">cheapest, needs no new data</text><text x="900" y="290" font-size="13" fill="#1565c0" font-weight="700">deepest, closes the gap</text>')
    c.add('<line x1="30" y1="310" x2="1170" y2="310" stroke="#90a4ae" stroke-width="3" marker-end="url(#ar-37474f)"/>')
    c.use_color("#37474f")
    c.add('<text x="30" y="340" font-size="13" fill="#37474f">cost and effort rise to the right; so does the effect on the booking</text>')
    c.render("s08d-interaction.png")

def gates():
    c = Canvas(1200, 600, "The two gating questions", "Each answer changes what the deepest intervention point is")
    q = c.node(30, 90, 520, 90, "What counts as a plate for payment?", "Bakul's manager says served; Kadamba's remark points to registered; no contract seen", "red", "ic-coin", True, fs=15, sfs=12.5)
    a = c.node(30, 250, 250, 130, "Registered plates", "no-show cost sits with students and the institution", "tech", None, fs=14, sfs=12)
    b = c.node(300, 250, 250, 130, "Served plates", "operator already bears part of it; incentive changes", "biz", None, fs=14, sfs=12)
    c.edge(q, a, "#37474f", None, width=3); c.edge(q, b, "#37474f", None, width=3)
    c.node(30, 410, 250, 100, "4.2 adoption problem", "if the contract can take a consumption basis; renegotiation if not", "tech", None, fs=13.5, sfs=12)
    c.node(300, 410, 250, 100, "Bakul accepts waste", "to avoid shortage; a lower booking would not cut its revenue (candidate)", "biz", None, fs=13.5, sfs=12)
    c.edge((155, 382), (155, 408), "#37474f", None, width=3); c.edge((425, 382), (425, 408), "#37474f", None, width=3)
    q2 = c.node(620, 90, 550, 90, "Who set the four-day lead and the cap of five?", "kitchens buy perishables one to three days ahead", "amber", "ic-calendar-x", True, fs=15, sfs=12.5)
    c.node(620, 250, 550, 100, "If nothing operational depends on four days", "the lead is held by habit; moving it or widening the exit is the nearest-term version of 4.2", "tech", None, fs=14, sfs=12)
    c.node(620, 380, 550, 100, "A shorter lead is not free", "Kadamba finds last-minute registrations a pain (single-sourced)", "amber", None, fs=14, sfs=12)
    c.edge((895, 182), (895, 248), "#37474f", None, width=3)
    c.pill(600, 560, "Either way the other three intervention points stand unchanged", "green", fs=14)
    c.render("s08d-gates.png")

if __name__ == "__main__":
    ladder(); four_points(); guardrails(); interaction(); gates()
