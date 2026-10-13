import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def quad(c, x0, y0, w, h, xl, yl, q):
    """Draw a quadrant frame. q = (tl, tr, bl, br) labels. Returns mapper (fx, fy)->px,py with 0..1 inputs."""
    colors = {"tl": "#e3f2fd", "tr": "#e8eaf6", "bl": "#fafafa", "br": "#fff3e0"}
    c.add(f'<rect x="{x0}" y="{y0}" width="{w/2}" height="{h/2}" fill="{colors["tl"]}"/><rect x="{x0+w/2}" y="{y0}" width="{w/2}" height="{h/2}" fill="{colors["tr"]}"/>'
          f'<rect x="{x0}" y="{y0+h/2}" width="{w/2}" height="{h/2}" fill="{colors["bl"]}"/><rect x="{x0+w/2}" y="{y0+h/2}" width="{w/2}" height="{h/2}" fill="{colors["br"]}"/>'
          f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="none" stroke="#9aa5b1" stroke-width="2"/>'
          f'<line x1="{x0+w/2}" y1="{y0}" x2="{x0+w/2}" y2="{y0+h}" stroke="#9aa5b1" stroke-width="1.6" stroke-dasharray="6 5"/>'
          f'<line x1="{x0}" y1="{y0+h/2}" x2="{x0+w}" y2="{y0+h/2}" stroke="#9aa5b1" stroke-width="1.6" stroke-dasharray="6 5"/>')
    for (lab, ax, ay, anc) in [(q[0], x0 + 12, y0 + 26, "start"), (q[1], x0 + w - 12, y0 + 26, "end"), (q[2], x0 + 12, y0 + h - 14, "start"), (q[3], x0 + w - 12, y0 + h - 14, "end")]:
        c.add(f'<text x="{ax}" y="{ay}" font-size="15" font-weight="800" fill="#455a64" text-anchor="{anc}">{esc(lab)}</text>')
    c.add(f'<text x="{x0+w/2}" y="{y0+h+34}" font-size="15" font-weight="700" fill="#333" text-anchor="middle">{esc(xl)}</text>')
    c.add(f'<text x="{x0-44}" y="{y0+h/2}" font-size="15" font-weight="700" fill="#333" text-anchor="middle" transform="rotate(-90 {x0-44} {y0+h/2})">{esc(yl)}</text>')
    c.add(f'<text x="{x0+6}" y="{y0+h+34}" font-size="12" fill="#666">low</text><text x="{x0+w-6}" y="{y0+h+34}" font-size="12" fill="#666" text-anchor="end">high</text>')
    c.add(f'<text x="{x0-10}" y="{y0+h-4}" font-size="12" fill="#666" text-anchor="end">low</text><text x="{x0-10}" y="{y0+14}" font-size="12" fill="#666" text-anchor="end">high</text>')
    return lambda fx, fy: (x0 + fx * w, y0 + (1 - fy) * h)

def dot(c, m, fx, fy, label, key="slate", dashed=False, anc="start", dx=12, dy=5, fs=13, sub=None):
    x, y = m(fx, fy)
    s = C[key][0]
    da = 'stroke-dasharray="3 2"' if dashed else ''
    fl = "white" if dashed else s
    c.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="{fl}" stroke="{s}" stroke-width="2.4" {da}/>')
    tx = x + (dx if anc == "start" else -dx)
    c.add(f'<text x="{tx:.1f}" y="{y+dy:.1f}" font-size="{fs}" font-weight="700" fill="#1b1b1b" text-anchor="{anc}">{esc(label)}</text>')
    if sub:
        c.add(f'<text x="{tx:.1f}" y="{y+dy+fs*1.1:.1f}" font-size="{fs-2}" fill="#555" text-anchor="{anc}">{esc(sub)}</text>')

# ------------------------------------------------------------ d13 power vs interest
def d13():
    c = Canvas(1200, 1010, "Power against interest", "Ordinal placement: the relative position is the finding, not the coordinates")
    m = quad(c, 70, 90, 1100, 820, "Interest in breakfast mess outcomes", "Power over mess decisions", ("Keep satisfied", "Manage closely", "Monitor", "Keep informed"))
    dot(c, m, 0.06, 0.90, "Academic administration", "ext", anc="start", sub="high power over class timing, none over the mess")
    dot(c, m, 0.40, 0.90, "CFS and CDS head", "soc", True, sub="head unresolved; no action on quantity")
    dot(c, m, 0.76, 0.90, "Mess Office", "soc", sub="rules; one reported use of power")
    dot(c, m, 0.66, 0.78, "Mess Committee", "soc", sub="menu approval; beyond that unconfirmed")
    dot(c, m, 0.14, 0.77, "Facility team and QC", "soc", sub="safety and taste, never quantity")
    dot(c, m, 0.42, 0.68, "CDS team", "soc", True, sub="placement provisional")
    dot(c, m, 0.10, 0.62, "Portal and IT owner", "ext", True, sub="latent, named by no one")
    dot(c, m, 0.33, 0.56, "Warden", "soc", sub="stated, not observed")
    dot(c, m, 0.06, 0.48, "Facilities and Estate", "ext", True)
    # operators
    dot(c, m, 0.60, 0.54, "Kadamba: Prism", "biz", anc="end", dx=12)
    dot(c, m, 0.74, 0.48, "Bakul: Vijayalakshmi", "biz")
    dot(c, m, 0.86, 0.58, "Yuktāhār: ABC", "biz")
    c.add(f'<text x="{m(0.52,0.63)[0]:.0f}" y="{m(0.52,0.63)[1]:.0f}" font-size="12.5" fill="#00695c" font-weight="700">Operators: high interest, high local power over quantity,</text><text x="{m(0.52,0.63)[0]:.0f}" y="{m(0.52,0.63)[1]+16:.0f}" font-size="12.5" fill="#00695c" font-weight="700">no rule-making power</text>')
    dot(c, m, 0.84, 0.29, "Parliament mess seats", "soc", anc="end", dx=12, sub="power unconfirmed")
    dot(c, m, 0.70, 0.20, "Serving and kitchen staff", "biz", anc="end", dx=12)
    dot(c, m, 0.97, 0.11, "Students", "users", anc="end", dx=12, sub="very high interest, very low power")
    dot(c, m, 0.74, 0.07, "Mess Cell", "pink", anc="end", dx=12)
    dot(c, m, 0.50, 0.15, "Ping", "pink", anc="end", dx=12)
    dot(c, m, 0.62, 0.30, "Outside diners, Kadamba staff", "green", anc="end", dx=12, sub="no voice")
    dot(c, m, 0.10, 0.34, "Event and exam organisers", "ext")
    dot(c, m, 0.20, 0.25, "Suppliers", "amber")
    dot(c, m, 0.07, 0.15, "Garbage contractor", "red")
    dot(c, m, 0.26, 0.07, "Vindhya, juice canteens, delivery", "ext")
    c.render("d13-power-interest-v2.png")

# ------------------------------------------------------------ d12 power vs leverage
def d12():
    c = Canvas(1200, 960, "Power against leverage over breakfast waste", "Ordinal placement; leverage means a small action producing a large system effect")
    m = quad(c, 70, 90, 1100, 780, "Leverage over breakfast waste", "Power over mess decisions", ("High power, low leverage", "High power, high leverage", "Low power, low leverage", "Low power, high leverage"))
    dot(c, m, 0.05, 0.90, "Academic administration", "ext", sub="controls class start; no stake in the mess")
    dot(c, m, 0.05, 0.76, "Facility team and QC", "soc", sub="present every meal, aimed at safety and taste")
    dot(c, m, 0.26, 0.70, "Mess Committee", "soc", sub="menu authority")
    dot(c, m, 0.28, 0.58, "Warden", "soc")
    dot(c, m, 0.88, 0.89, "Mess Office", "soc", anc="end", dx=12, sub="leverage over student flexibility rules, not over waste")
    dot(c, m, 0.40, 0.84, "CFS and CDS head", "soc", True)
    dot(c, m, 0.58, 0.68, "Operator: Yuktāhār", "biz", sub="daily meeting holds both levers")
    dot(c, m, 0.76, 0.46, "Operator: Kadamba", "biz", sub="ratio is Prism's; supervisor holds the top-up")
    dot(c, m, 0.64, 0.38, "Operator: Bakul", "biz", sub="manager, bounded by his ~70% floor")
    dot(c, m, 0.88, 0.22, "Students collectively", "users", anc="end", dx=12, sub="exercised but unmeasured")
    dot(c, m, 0.72, 0.09, "Mess Cell", "pink", anc="end", dx=12)
    dot(c, m, 0.06, 0.10, "Students individually", "users")
    dot(c, m, 0.06, 0.26, "Outside diners, Kadamba staff", "green", sub="a stake in the ratio staying put")
    c.add(f'<text x="{m(0.50,0.28)[0]:.0f}" y="{m(0.50,0.28)[1]:.0f}" font-size="12.5" fill="#00695c" font-weight="700" text-anchor="middle">Information-flow leverage, routing records to the rule owner, belongs to nobody</text>')
    c.render("d12-leverage-quadrant.png")

# ------------------------------------------------------------ d14 power and information flow
def d14():
    c = Canvas(1320, 1010, "Power and information flow", "Where channels exist, and where they stop")
    G, T, U, R, S = C["biz"][0], C["soc"][0], C["users"][0], C["red"][0], "#37474f"
    c.zone(14, 84, 760, 190, "Governance", "soc", fs=13.5, opacity=0.18)
    cfs = c.node(30, 124, 150, 66, "CFS", "parent of CDS", "soc", "ic-building", fs=14)
    cds = c.node(200, 124, 180, 66, "CDS", "head: two names, unresolved", "soc", "ic-gear", True, fs=14)
    mo = c.node(400, 124, 180, 66, "Mess Office", "rules, portal", "soc", "ic-gear", True, fs=14)
    mc = c.node(600, 124, 160, 66, "Mess Committee", "menu, policy", "soc", "ic-briefcase", fs=13.5)
    c.node(30, 204, 150, 56, "Warden", "vendors", "soc", "ic-shield", fs=14)
    c.node(400, 204, 360, 56, "CDS scan records", "every registration and its scan: no outbound arrow", "red", "ic-chart", True, fs=13.5, sfs=11.5)
    acad = c.node(900, 124, 250, 70, "Academic administration", "class schedule, 8:30 AM", "ext", "ic-building", fs=14)
    c.zone(14, 300, 1292, 360, "Operators: high information, authority over quantity only", "biz", fs=13.5, opacity=0.18)
    prism = c.node(170, 346, 250, 70, "Prism, Kadamba", "tender; operations manager, manager, supervisor", "biz", "ic-pot", fs=14)
    sup = c.node(170, 440, 250, 70, "Kadamba supervisor", "decides top-ups; gram standards only", "biz", "ic-eye", fs=14)
    yuk = c.node(450, 346, 250, 90, "Yuktāhār: ABC", "flat team; book system, reconciled daily", "biz", "ic-book", fs=14)
    c.node(450, 456, 250, 66, "Yuktāhār's books", "no outbound arrow to any rule owner", "red", "ic-book", True, fs=13.5, sfs=11.5)
    bk = c.node(730, 346, 270, 90, "Bakul manager", "weekly judgement; consumption and pairing knowledge", "biz", "ic-person", fs=14)
    c.node(730, 456, 270, 66, "Hafizpet kitchen", "top-up by phone, lead time unknown", "biz", "ic-truck", fs=14)
    c.node(1030, 346, 260, 90, "Facility team and weekly QC", "taste every meal with Prism: safety and taste only", "tech", "ic-thermometer", fs=14, sfs=11.5)
    c.node(1030, 456, 260, 84, "Outside diners and half of Kadamba's staff", "absorb surplus; no voice", "green", "ic-people", fs=13.5, sfs=11.5)
    c.node(1030, 556, 260, 70, "Garbage contractor", "the exit for the rest", "red", "ic-bin", fs=14)
    c.zone(14, 690, 1292, 300, "Students and informal channels", "users", fs=13.5, opacity=0.18)
    stu = c.node(30, 740, 300, 100, "Students", "registered by default; billed on registration", "users", "ic-person", fs=17)
    mcell = c.node(380, 740, 220, 66, "Mess Cell", "resale", "pink", "ic-chat", fs=14)
    c.node(380, 826, 220, 60, "Ping", "public visibility", "pink", "ic-chat", fs=14)
    c.node(640, 740, 230, 66, "Unofficial tools", "alternative interface", "pink", "ic-phone", fs=14)
    c.node(640, 826, 230, 70, "Student committee", "chooses the menu; identity unconfirmed", "soc", "ic-cap", True, fs=14)
    c.edge(cfs, cds, T, None, width=3.4)
    c.edge((290, 192), (290, 344), T, "contract chain", width=3.6, lfs=11.5, lpos=(290, 268))
    c.edge(prism, sup, G, None, width=2.6)
    c.edge((900, 160), (778, 160), R, None, dash="6 5", width=3.2)
    c.pill(838, 108, "NO FORMAL CHANNEL", "red", fs=12)
    c.pill(590, 287, "no route from either set of records to any rule owner", "red", fs=12)
    c.edge((300, 738), (300, 512), U, "complaint at the counter", width=2.6, lfs=11.5, lpos=(300, 640))
    c.edge(stu, mcell, U, None, width=2.4, dash="6 4")
    c.legend(930, 720, [(T, "authority / chain", "line"), (G, "operator decision", "line"), (U, "student channel", "line"), (R, "no channel", "dash")], title="Reading the map", fs=11.5)
    c.render("d14-power-flow-network.png")

# ------------------------------------------------------------ d23 Kadamba command chain
def d23():
    c = Canvas(1100, 960, "Kadamba's command chain", "From the institution to the counter, as the operator describes it (single-sourced)")
    x = 40; w = 470
    steps = [("CFS", "Campus Facilities Services, parent department", "soc", "ic-building", False),
             ("CDS", "head: one name from the operator, another from an earlier interview; unresolved", "soc", "ic-gear", True),
             ("Prism", "outsourced vendor; wins the tender and runs all Kadamba operations", "biz", "ic-pot", False),
             ("Operations manager", None, "biz", "ic-briefcase", False),
             ("Manager", "relays complaints into the WhatsApp group", "biz", "ic-person", False),
             ("Supervisor", "watches the counters; real-time quantity decider; gram standards; top-up ready in 10 to 15 minutes", "biz", "ic-eye", False),
             ("Service staff", "about 10 chefs, veg and non-veg; a head chef joins on biryani days", "biz", "ic-people", False)]
    prev = None
    ys = []
    for i, (t, s, k, ic, d) in enumerate(steps):
        h = 84 if s and len(s) > 60 else (70 if s else 50)
        y = 100 + sum(ys) + i * 34
        nd = c.node(x, y, w, h, t, s, k, ic, d, fs=16, sfs=12.5)
        ys.append(h)
        if prev: c.edge(prev, nd, C[k][0] if k != "soc" else C["soc"][0], None, width=3.4)
        prev = nd
        if t == "Supervisor": sup = nd
    # facility branch
    c.zone(580, 150, 480, 330, "Beside the chain: oversight goes straight to the kitchen", "tech", fs=13.5, opacity=0.2)
    f1 = c.node(600, 190, 440, 84, "Facility team", "tastes every meal with two Prism staff before service; identity unconfirmed", "tech", "ic-thermometer", True, fs=15, sfs=12.5)
    f2 = c.node(600, 296, 440, 64, "Weekly quality-control inspection", "including the store; water TDS read daily", "tech", "ic-flask", fs=15, sfs=12.5)
    c.node(600, 382, 440, 74, "Remit: safety and taste", "temperature checks, a 72-hour sample, a wrapped display plate; never how much is cooked or wasted", "red", "ic-warning", fs=15, sfs=12)
    c.edge((578, 364), (514, 364), C["tech"][0], None, dash="6 4", width=3)
    # Yuktahar contrast
    c.zone(580, 510, 480, 400, "Contrast: Yuktāhār is flat", "biz", fs=13.5, opacity=0.2)
    c.node(600, 550, 440, 70, "Two project managers", "with about three site staff sharing the work", "biz", "ic-briefcase", fs=15, sfs=12.5)
    c.node(600, 636, 440, 80, "No hierarchy", "everyone does every job; peers cross-check each book; mismatches go to the daily meeting", "biz", "ic-people", fs=15, sfs=12.5)
    c.node(600, 732, 440, 70, "Quantity decided by the team", "twice-daily meeting, then the first half hour of service", "biz", "ic-book", fs=15, sfs=12.5)
    c.node(600, 818, 440, 70, "Records stay in the kitchen", "no route to any rule owner", "red", "ic-link-broken", True, fs=15, sfs=12.5)
    c.render("d23-kadamba-command-chain.png")

if __name__ == "__main__":
    d13(); d12(); d14(); d23()
