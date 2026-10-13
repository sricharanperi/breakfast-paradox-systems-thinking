import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

PRO, SYS, CAU, DES, NEU = "#00838F", "#00695C", "#AD1457", "#283593", "#455A64"
RED, AMB, GRN, LGR = "#C62828", "#E08600", "#2E7D32", "#CFD8DC"

def person(c, x, y, s, color, outline=False):
    """person icon centred at x,y, size s"""
    if outline:
        c.add(f'<use href="#ic-person" x="{x-s/2:.1f}" y="{y-s/2:.1f}" width="{s}" height="{s}" fill="#ECEFF1" stroke="{LGR}" stroke-width="1.4"/>')
    else:
        c.add(f'<use href="#ic-person" x="{x-s/2:.1f}" y="{y-s/2:.1f}" width="{s}" height="{s}" fill="{color}"/>')

def card(c, x, y, w, h, title, sub=None, color=NEU, dashed=False, tfs=20, sfs=17, fill="white", tcol=None):
    da = 'stroke-dasharray="9 6"' if dashed else ""
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{color}" stroke-width="3" {da}/>')
    tl = wrap(title, w - 28, tfs, True); sl = wrap(sub, w - 28, sfs) if sub else []
    tot = len(tl) * tfs * 1.25 + (len(sl) * sfs * 1.28 + 6 if sl else 0)
    yy = y + (h - tot) / 2 + tfs * 0.95
    for ln in tl:
        c.add(f'<text x="{x+14}" y="{yy:.1f}" font-size="{tfs}" font-weight="800" fill="{tcol or color}">{esc(ln)}</text>'); yy += tfs * 1.25
    yy += 6 - tfs * 0.2 + sfs * 0.2
    for ln in sl:
        c.add(f'<text x="{x+14}" y="{yy:.1f}" font-size="{sfs}" fill="#2b2f33">{esc(ln)}</text>'); yy += sfs * 1.28

def arrow(c, x1, y1, x2, y2, color, w=4, dash=None, bend=0):
    c.use_color(color)
    da = f'stroke-dasharray="{dash}"' if dash else ""
    if bend:
        mx, my = (x1+x2)/2, (y1+y2)/2; dx, dy = x2-x1, y2-y1; L = math.hypot(dx, dy) or 1
        cx, cy = mx - dy/L*bend*L, my + dx/L*bend*L
        c.add(f'<path d="M {x1} {y1} Q {cx:.1f} {cy:.1f} {x2} {y2}" fill="none" stroke="{color}" stroke-width="{w}" {da} marker-end="url(#ar-{color[1:]})"/>')
    else:
        c.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" {da} marker-end="url(#ar-{color[1:]})"/>')

def title(c, t, sub=None):
    c.add(f'<text x="40" y="52" font-size="32" font-weight="800" fill="#22262B">{esc(t)}</text>')
    if sub: c.add(f'<text x="40" y="86" font-size="19" fill="#6B7480">{esc(sub)}</text>')

# ---------------------------------------------------------------- f-hundred
def f_hundred():
    c = Canvas(1200, 640)
    title(c, "Out of a hundred breakfast bookings", "Filled people ate. Empty ones were booked and billed, and not eaten.")
    def grid(x0, y0, filled, color, lab, big, sub):
        s = 28
        for i in range(100):
            r, col = divmod(i, 10)
            person(c, x0 + col * 31, y0 + r * 31, s, color, outline=(i >= filled))
        c.add(f'<text x="{x0-14}" y="{y0+10*31+42}" font-size="56" font-weight="800" fill="{color}">{big}</text>')
        c.add(f'<text x="{x0+86}" y="{y0+10*31+30}" font-size="22" font-weight="800" fill="#22262B">{esc(lab)}</text>')
        c.add(f'<text x="{x0+86}" y="{y0+10*31+54}" font-size="17" fill="#6B7480">{esc(sub)}</text>')
    grid(70, 140, 37, PRO, "Kadamba, April 2026", "37", "scanned, of every 100 booked")
    grid(450, 140, 28, CAU, "Yuktāhār, September", "28", "about, of every 100 booked")
    c.add(f'<rect x="840" y="130" width="320" height="330" rx="18" fill="#F4F7F8"/>')
    c.add('<text x="866" y="176" font-size="22" font-weight="800" fill="#22262B">Same kitchen, lunch</text>')
    c.add('<text x="866" y="202" font-size="17" fill="#6B7480">Yuktāhār, same days</text>')
    for i in range(10): person(c, 886 + i * 28, 262, 25, SYS, outline=(i >= 7))
    c.add(f'<text x="866" y="340" font-size="56" font-weight="800" fill="{SYS}">70</text>')
    c.add('<text x="950" y="338" font-size="17" fill="#2b2f33">about, of every 100</text>')
    c.add('<text x="866" y="400" font-size="17" fill="#2b2f33">Same portal, same rules,</text><text x="866" y="424" font-size="17" fill="#2b2f33">same caterer.</text>')
    c.render("f-hundred.png")

# ---------------------------------------------------------------- f-river
def f_river():
    W, H = 1200, 860
    c = Canvas(W, H)
    title(c, "From booking to bin", "Bookings flow through three kitchens and one crowded morning, then out through five exits.")
    c.add(f'<rect x="40" y="110" width="1120" height="80" rx="18" fill="#E8EAF6" stroke="{DES}" stroke-width="3"/>')
    c.add(f'<text x="64" y="160" font-size="24" font-weight="800" fill="{DES}">The rule owners: committee, dining office, warden</text>')
    c.add(f'<path d="M 40 300 L 720 300 L 780 420 L 880 420 L 940 340 L 1160 340 L 1160 560 L 940 560 L 880 480 L 780 480 L 720 600 L 40 600 Z" fill="#D7EFF2" stroke="{PRO}" stroke-width="3" stroke-linejoin="round"/>')
    for i, x in enumerate(range(792, 880, 30)):
        c.add(f'<path d="M {x} {452+(i%2)*8} q 8 -10 15 0 t 15 0" fill="none" stroke="{PRO}" stroke-width="3"/>')
    for j, ln in enumerate(["the 9:15", "to 9:30", "crowd"]):
        c.add(f'<text x="1050" y="{430+j*30}" font-size="24" font-weight="800" fill="{RED}" text-anchor="middle">{ln}</text>')
    card(c, 56, 380, 200, 130, "Bookings", "about 1,070 a day, flat all week", PRO, tfs=22)
    isl = [("Kadamba", "fixed share, supervisor tops up", 330, 316), ("Bakul", "weekly judgement, 8 km drive", 330, 410), ("Yuktāhār", "own books, first-half-hour check", 330, 504)]
    for t_, s, x, y in isl:
        c.add(f'<rect x="{x}" y="{y}" width="360" height="82" rx="41" fill="#FFF8E1" stroke="{AMB}" stroke-width="3"/>')
        c.add(f'<text x="{x+30}" y="{y+34}" font-size="21" font-weight="800" fill="#7A4B00">{t_}</text><text x="{x+30}" y="{y+60}" font-size="17" fill="#2b2f33">{esc(s)}</text>')
        arrow(c, 258, 445, x - 4, y + 41, PRO, 3)
    ex = [("Reuse", "Yuktāhār only", GRN, False, 600), ("Outside diners and staff", "at Kadamba", GRN, False, 600), ("Held and reheated", "Kadamba, candidate", AMB, True, 600), ("Latecomers", "back door after 9:30", AMB, False, 480), ("The bin", "then a contractor", RED, False, 560)]
    for i, (t_, s, col, d, y0) in enumerate(ex):
        x = 40 + i * 226
        card(c, x, 650, 210, 112, t_, s, col, d, tfs=20, sfs=17)
        arrow(c, x + 105, y0 if i != 3 else 480, x + 105, 646, col, 3, "7 5" if d else None)
    arrow(c, 1050, 336, 1050, 196, RED, 5, "10 6")
    c.add(f'<text x="1032" y="270" font-size="19" font-weight="800" fill="{RED}" text-anchor="end">records never reach the rule owners</text>')
    c.add('<text x="40" y="808" font-size="17" fill="#6B7480">Each kitchen measures the gap every day. The measurement stops at the kitchen door.</text>')
    c.render("f-river.png")

# ---------------------------------------------------------------- f-loop-grid
def f_loop_grid():
    c = Canvas(1200, 880)
    title(c, "Eighteen loops we tested", "Only three close with every link evidenced.")
    groups = [("Closes, every link evidenced", GRN, [("L4", "menu rotation"), ("L11", "Wastage Book learning"), ("L12", "counter top-up")], False),
              ("Candidate loop: one link assumed", CAU, [("L1", "resale"), ("L3b", "Kadamba lock-in"), ("L9", "waste absorption"), ("L15", "soft close"), ("L17", "skill shifts burden")], True),
              ("Open chain: it never returns to its start", AMB, [("L13", "booking to surplus"), ("L14", "rush to ratchet"), ("L2", "Skip Meal"), ("L5", "menu transparency"), ("L6", "shock switch"), ("L7", "late nights to skip")], False),
              ("Absent, contradicted or static", RED, [("L3", "hall swap"), ("L8", "vendor discipline"), ("L16", "waste to menu"), ("L10", "gap not routed")], False)]
    y = 120
    for name, col, tiles, dashed in groups:
        c.add(f'<text x="40" y="{y+22}" font-size="22" font-weight="800" fill="{col}">{esc(name)}</text>')
        y += 38
        for i, (idv, w) in enumerate(tiles):
            r, k = divmod(i, 4)
            x = 40 + k * 282; yy = y + r * 82
            da = 'stroke-dasharray="9 6"' if dashed else ""
            c.add(f'<rect x="{x}" y="{yy}" width="266" height="70" rx="14" fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-width="3" {da}/>')
            c.add(f'<text x="{x+16}" y="{yy+44}" font-size="28" font-weight="800" fill="{col}">{idv}</text>')
            c.add(f'<text x="{x+16+len(idv)*17+14}" y="{yy+43}" font-size="17" fill="#22262B">{esc(w)}</text>')
        y += ((len(tiles) + 3) // 4) * 82 + 22
    c.render("f-loop-grid.png")

# ---------------------------------------------------------------- f-l11
def f_l11():
    c = Canvas(1100, 760)
    title(c, "How Yuktāhār learns", "A loop that closes: what was left over shapes what is cooked, two weeks later.")
    A = (330, 120, 440, 100, "Leftover is written in the Wastage Book", PRO)
    B = (740, 330, 330, 120, "Two weeks on, the same menu day comes round", NEU)
    C = (330, 560, 440, 100, "A smaller batch is cooked", SYS)
    D = (30, 330, 330, 120, "Less is left over", GRN)
    for x, y, w, h, t, col in (A, B, C, D):
        card(c, x, y, w, h, t, None, col, tfs=22, fill="#FFFFFF")
    arrow(c, 772, 190, 905, 326, NEU, 5, bend=0.12)
    arrow(c, 905, 454, 772, 590, NEU, 5, bend=0.12)
    arrow(c, 328, 610, 195, 454, NEU, 5, bend=0.12)
    arrow(c, 195, 326, 328, 170, NEU, 5, bend=0.12)
    for (x, y, s, col) in [(880, 240, "+", NEU), (880, 520, "-", RED), (222, 520, "+", NEU), (222, 240, "+", NEU)]:
        c.badge(x, y, s, col, r=20, fs=26)
    c.pill(1000, 560, "two-week delay", "navy", fs=17)
    c.add(f'<text x="550" y="400" font-size="26" font-weight="800" fill="{SYS}" text-anchor="middle">balancing</text><text x="550" y="432" font-size="19" fill="#2b2f33" text-anchor="middle">it pushes the leftover down</text>')
    c.add('<text x="40" y="740" font-size="17" fill="#6B7480">+ means both move the same way. - means they move opposite ways. Confirmed at Yuktāhār only.</text>')
    c.render("f-l11.png")

# ---------------------------------------------------------------- f-chain
def f_chain():
    c = Canvas(1200, 520)
    title(c, "The core chain of the paradox", "Each tile makes the next one more likely. The last link is not evidenced.")
    tiles = [("ic-toggle", "Booking is automatic", PRO), ("ic-chart", "The count stays flat", PRO), ("ic-pot", "The kitchen cooks a fixed share", SYS), ("ic-bowl", "Most surplus on low days and the veg line", CAU), ("ic-flame", "Surplus is held and reheated", CAU)]
    x = 36
    for i, (ic, t, col) in enumerate(tiles):
        c.add(f'<rect x="{x}" y="150" width="172" height="230" rx="18" fill="white" stroke="{col}" stroke-width="3.5"/>')
        c.add(f'<circle cx="{x+86}" cy="206" r="32" fill="{col}"/><use href="#{ic}" x="{x+86-20}" y="186" width="40" height="40" fill="white"/>')
        for j, ln in enumerate(wrap(t, 150, 19, True)):
            c.add(f'<text x="{x+86}" y="{276+j*26}" font-size="19" font-weight="800" fill="#22262B" text-anchor="middle">{esc(ln)}</text>')
        if i < 4: arrow(c, x + 176, 265, x + 204, 265, NEU, 5)
        x += 204
    arrow(c, 1050, 265, 1090, 265, RED, 5, "8 6")
    c.add(f'<circle cx="1136" cy="265" r="40" fill="#FDECEA" stroke="{RED}" stroke-width="3.5" stroke-dasharray="8 6"/><text x="1136" y="283" font-size="52" font-weight="800" fill="{RED}" text-anchor="middle">?</text>')
    c.add(f'<text x="1136" y="336" font-size="17" font-weight="800" fill="{RED}" text-anchor="middle">students</text><text x="1136" y="358" font-size="17" font-weight="800" fill="{RED}" text-anchor="middle">leave?</text>')
    c.add(f'<text x="40" y="440" font-size="19" fill="#2b2f33">No evidence yet that poorer food sends students away, so this stays a chain and not a loop.</text>')
    c.render("f-chain.png")

# ---------------------------------------------------------------- f-iceberg
def f_iceberg():
    c = Canvas(1100, 940)
    title(c, "The paradox at four depths", "What you can see sits on top. What holds it up sits underneath.")
    wl = 330
    c.add(f'<rect x="0" y="{wl}" width="1100" height="610" fill="#E3F2FD" fill-opacity="0.55"/>')
    c.add(f'<line x1="0" y1="{wl}" x2="1100" y2="{wl}" stroke="#64B5F6" stroke-width="3"/>')
    bands = [("EVENT", "#90A4AE", [(330, 210), (330, 330), (260, 330), (300, 210)], None),]
    # shapes: tip above water, then 3 bands below
    c.add(f'<path d="M 220 {wl} L 300 170 L 360 215 L 400 {wl} Z" fill="#ECEFF1" stroke="{NEU}" stroke-width="3"/>')
    c.add(f'<path d="M 190 {wl} L 430 {wl} L 470 {wl+160} L 150 {wl+160} Z" fill="#B2EBF2" stroke="{PRO}" stroke-width="3"/>')
    c.add(f'<path d="M 150 {wl+160} L 470 {wl+160} L 500 {wl+320} L 110 {wl+320} Z" fill="#B2DFDB" stroke="{SYS}" stroke-width="3"/>')
    c.add(f'<path d="M 110 {wl+320} L 500 {wl+320} L 430 {wl+520} L 190 {wl+520} Z" fill="#F8BBD0" stroke="{CAU}" stroke-width="3"/>')
    names = [("EVENT", 320, wl - 42, NEU), ("PATTERN", 310, wl + 92, PRO), ("STRUCTURE", 310, wl + 262, SYS), ("BELIEF", 310, wl + 440, CAU)]
    for n, x, y, col in names:
        c.add(f'<text x="{x}" y="{y}" font-size="24" font-weight="800" fill="{col}" text-anchor="middle">{n}</text>')
    ex = [("Booked, not eaten, while items run out at 9:20 and the bin fills.", wl - 120, NEU),
          ("Bookings stay flat all week while turnout swings. The crowd comes in the last quarter hour.", wl + 60, PRO),
          ("An automatic default. Billing at the booking. A gap measured but never routed.", wl + 230, SYS),
          ("\"Registration is demand.\" \"We are paid for the booking.\" \"They are catching us.\"", wl + 400, CAU)]
    for t, y, col in ex:
        c.add(f'<line x1="505" y1="{y+40}" x2="560" y2="{y+40}" stroke="{col}" stroke-width="3"/>')
        for j, ln in enumerate(wrap(t, 480, 20)):
            c.add(f'<text x="575" y="{y+34+j*27}" font-size="20" fill="#22262B">{esc(ln)}</text>')
    c.render("f-iceberg.png")

# ---------------------------------------------------------------- f-pillars
def f_pillars():
    c = Canvas(1200, 710)
    title(c, "What holds the gap in place", "Three structures carry it. Two conditions keep them there.")
    c.add(f'<rect x="60" y="120" width="1080" height="96" rx="20" fill="{CAU}"/>')
    c.add('<text x="600" y="184" font-size="36" font-weight="800" fill="white" text-anchor="middle">The gap between booked and eaten holds</text>')
    pil = [("ic-toggle", "An automatic default with a narrow, early exit"), ("ic-coin", "Billing at the booking, not at the plate"), ("ic-link-broken", "A gap measured twice and routed nowhere")]
    for i, (ic, t) in enumerate(pil):
        x = 110 + i * 350
        c.add(f'<rect x="{x}" y="222" width="270" height="250" rx="14" fill="#FCE4EC" stroke="{CAU}" stroke-width="3.5"/>')
        c.add(f'<circle cx="{x+135}" cy="290" r="38" fill="{CAU}"/><use href="#{ic}" x="{x+135-24}" y="266" width="48" height="48" fill="white"/>')
        for j, ln in enumerate(wrap(t, 236, 21, True)):
            c.add(f'<text x="{x+135}" y="{368+j*28}" font-size="21" font-weight="800" fill="#22262B" text-anchor="middle">{esc(ln)}</text>')
    c.add('<text x="40" y="520" font-size="20" font-weight="800" fill="#6B7480">resting on two conditions</text>')
    conds = [("Loud problems get answered. A run-out reaches a manager. A surplus is silent.", 60), ("Absorbers take the consequence first, so it never becomes a signal.", 620)]
    for t, x in conds:
        c.add(f'<rect x="{x}" y="540" width="520" height="130" rx="16" fill="#ECEFF1" stroke="{NEU}" stroke-width="3"/>')
        for j, ln in enumerate(wrap(t, 480, 22, True)):
            c.add(f'<text x="{x+24}" y="{588+j*30}" font-size="22" font-weight="800" fill="#22262B">{esc(ln)}</text>')
    c.render("f-pillars.png")

# ---------------------------------------------------------------- f-fromto
def f_fromto():
    c = Canvas(1200, 560)
    title(c, "Our question, before and after the reframe")
    def bubble(x, y, w, h, col, fill, head, q, foot, tail_left=True):
        c.add(f'<path d="M {x+30} {y} H {x+w-30} Q {x+w} {y} {x+w} {y+30} V {y+h-30} Q {x+w} {y+h} {x+w-30} {y+h} H {x+90} L {x+50} {y+h+46} L {x+60} {y+h} H {x+30} Q {x} {y+h} {x} {y+h-30} V {y+30} Q {x} {y} {x+30} {y} Z" fill="{fill}" stroke="{col}" stroke-width="4"/>')
        c.add(f'<text x="{x+30}" y="{y+46}" font-size="19" font-weight="800" fill="{col}">{head}</text>')
        for j, ln in enumerate(wrap(q, w - 60, 30, True)):
            c.add(f'<text x="{x+30}" y="{y+100+j*38}" font-size="30" font-weight="800" fill="#22262B">{esc(ln)}</text>')
        c.add(f'<text x="{x+30}" y="{y+h-26}" font-size="18" fill="#2b2f33">{esc(foot)}</text>')
    bubble(40, 130, 480, 280, NEU, "#F4F6F7", "BEFORE: an operations question", "Why do students not eat what they book?", "It looks at students.")
    bubble(680, 130, 480, 280, CAU, "#FCE4EC", "AFTER: a systems question", "Why does this system not notice its own cost?", "It looks at the whole arrangement.")
    arrow(c, 540, 270, 660, 270, NEU, 7)
    c.render("f-fromto.png")

# ---------------------------------------------------------------- f-ips
def f_ips():
    c = Canvas(1200, 700)
    title(c, "Four places to act", "Laid along the breakfast, from booking to bin.")
    ys = 380
    stops = [("Booking", 100), ("Count read", 300), ("First batch", 500), ("9:30 crowd", 700), ("Leftovers", 900), ("Bin", 1100)]
    c.add(f'<line x1="70" y1="{ys}" x2="1130" y2="{ys}" stroke="{NEU}" stroke-width="8" stroke-linecap="round"/>')
    for n, x in stops:
        c.add(f'<circle cx="{x}" cy="{ys}" r="14" fill="white" stroke="{NEU}" stroke-width="5"/><text x="{x}" y="{ys+44}" font-size="19" font-weight="800" fill="#22262B" text-anchor="middle">{n}</text>')
    cards = [("1  THE RULE", "Bring back a breakfast-only version of attendance-based billing.", DES, 40, 100), ("2  THE PROCESS", "Feed recorded turnout into the decision that sets the first batch.", SYS, 425, 500), ("3  INFORMATION", "A trigger that fires on measured cost, not only on complaints.", CAU, 810, 900)]
    for t, s, col, x, sx in cards:
        card(c, x, 110, 350, 170, t, s, col, tfs=21, sfs=19)
        arrow(c, x + 175 if sx != 100 else 100, 284, sx, ys - 20, col, 3)
    arrow(c, 900, ys + 74, 500, ys + 74, CAU, 4, "9 6", bend=0.18) if False else None
    c.add(f'<path d="M 100 {ys+80} V {ys+100} H 1100 V {ys+80}" fill="none" stroke="{DES}" stroke-width="5"/>')
    card(c, 250, ys + 116, 700, 130, "4  WHO DECIDES", "One named owner of the whole booked, cooked and eaten outcome.", DES, tfs=21, sfs=19)
    c.render("f-ips.png")

if __name__ == "__main__":
    f_hundred(); f_river(); f_loop_grid(); f_l11(); f_chain(); f_iceberg(); f_pillars(); f_fromto(); f_ips()
