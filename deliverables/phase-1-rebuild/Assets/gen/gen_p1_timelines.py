import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

def cell(c, x, y, w, h, text, key, dashed=False, fs=11.5, bold=None):
    s, f = C[key]
    da = 'stroke-dasharray="5 4"' if dashed else ""
    c.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{f}" fill-opacity="0.75" stroke="{s}" stroke-width="1.8" {da}/>')
    lines = wrap(text, w - 14, fs)
    yy = y + (h - len(lines) * fs * 1.25) / 2 + fs * 0.95
    for ln in lines:
        c.add(f'<text x="{x+8}" y="{yy:.1f}" font-size="{fs}" fill="#1b1b1b">{esc(ln)}</text>'); yy += fs * 1.25

# ------------------------------------------------------------ d21
def d21():
    c = Canvas(1300, 760, "Two kitchens' mornings, and Bakul's longer one", "Kadamba and Yuktāhār on site; Bakul cooked at Hafizpet. Single-sourced unless marked; no Bakul records")
    cols = ["About 3:00", "5:30", "7:00 to 7:30", "7:30 to 8:00", "8:00 to 9:00", "9:15 to 9:30", "9:30", "After close"]
    x0, cw, gap = 150, 133, 6
    for i, t in enumerate(cols):
        c.add(f'<rect x="{x0+i*(cw+gap)}" y="84" width="{cw}" height="34" rx="8" fill="#37474f"/><text x="{x0+i*(cw+gap)+cw/2}" y="106" font-size="13.5" font-weight="800" fill="white" text-anchor="middle">{t}</text>')
    lanes = [("Kadamba", "biz", ["", "Chef arrives; batch items at 70% of registrations, by gram standard", "Live dosa and vada from 7:00; safety checks and tasting done", "Service opens; supervisor watches item levels", "Top-ups ready in 10 to 15 minutes; the crowd builds", "The crest: 26.5% of scans; about 150 in the last ten minutes", "Front door shuts; back door serves latecomers", "Outside diners and staff eat; the rest to the bin"]),
             ("Yuktāhār", "tech", ["", "Cooking starts; mostly one batch, poha in two", "Food ready by 7:30", "First half hour sampled to project the rest", "Counter checks every 30 minutes from about 8:45; re-cook by the run-out rule", "Closing rush (the head's account; unmeasured)", "Fridge cleaning", "Wastage Book entry; reuse; meeting fixes tomorrow; matching page read in two weeks"]),
             ("Bakul", "users", ["Labour-heavy items start at Hafizpet", "", "Arrives about 7; hot-water holding", "Service opens", "Main rush 8:00 to 8:30; check every 30 minutes; phone top-up if short", "Reserve for about 50 at 9:20; 10 to 15 arrive in the last ten minutes", "", "Some leftovers back to Hafizpet, the rest thrown; no record"])]
    y = 130
    for name, key, cells in lanes:
        s, f = C[key]
        c.add(f'<rect x="14" y="{y}" width="126" height="190" rx="10" fill="{s}"/><text x="77" y="{y+100}" font-size="15" font-weight="800" fill="white" text-anchor="middle">{name}</text>')
        for i, t in enumerate(cells):
            if t: cell(c, x0 + i * (cw + gap), y, cw, 190, t, key, dashed=(name == "Bakul"), fs=12)
        y += 200
    c.add(f'<text x="14" y="{y+14}" font-size="12.5" fill="#555">Bakul rows are the manager account; the dashed outline marks that no records exist. The kitchens start two hours before the first student scans.</text>')
    c.render("d21-two-kitchen-daily-timeline.png")

# ------------------------------------------------------------ d22
def d22():
    c = Canvas(1250, 800, "When each decision is fixed", "From the month before to the 72-hour sample; the first batch is the binding constraint")
    steps = [("A month ahead", "Automatic registration: the default every kitchen plans from", "tech", False),
             ("About two weeks ahead", "Yuktāhār's Wastage Book page for this menu day; groceries bought fortnightly", "biz", False),
             ("About one week ahead", "Kadamba buys dry goods; Bakul's manager resets each item's share from attendance history", "biz", False),
             ("About four days ahead", "Last cancellation: five per meal type per month; the count becomes final", "red", False),
             ("Two to three days ahead", "Kadamba buys some vegetables", "amber", False),
             ("One day ahead", "Perishables bought; Yuktāhār's meeting fixes the issue; quantities set", "biz", False),
             ("5:30 on the day", "First batch cooked: before any sign of turnout, the binding constraint", "red", False),
             ("During service", "Top-up and re-cook: upward only (Yuktāhār also projects from the first half hour)", "tech", False),
             ("Three to four hours after cooking", "Cooked food is no longer usable", "amber", False),
             ("Up to 72 hours after", "Sample held for testing", "ext", False)]
    for i, (t, s, k, d) in enumerate(steps):
        x = 30 + i * 74; y = 90 + i * 66
        nd = c.node(x, y, 520 if i < 8 else 520, 58, t, s, k, None, d, fs=14, sfs=11.5)
        if i:
            c.add(f'<path d="M {x+20} {y-8} L {x+20} {y}" stroke="#90a4ae" stroke-width="2.4"/>')
    c.add(f'<text x="840" y="170" font-size="13.5" font-weight="800" fill="#c62828">Registration is fixed days ahead,</text><text x="840" y="190" font-size="13.5" font-weight="800" fill="#c62828">the decision to eat on the morning itself.</text>')
    c.add(f'<text x="840" y="230" font-size="12.5" fill="#444">Raw stock bought ahead is largely recoverable.</text><text x="840" y="250" font-size="12.5" fill="#444">Cooked food is not.</text>')
    c.add(f'<text x="840" y="300" font-size="12.5" fill="#444">Bakul: the first batch leaves Hafizpet by about 7 AM,</text><text x="840" y="320" font-size="12.5" fill="#444">and a top-up needs a call, cooking and a 20 to 40</text><text x="840" y="340" font-size="12.5" fill="#444">minute drive; lead time unknown.</text>')
    c.add(f'<text x="840" y="390" font-size="12.5" fill="#444">Kadamba biryani lunch is the contrast:</text><text x="840" y="410" font-size="12.5" fill="#444">cooked at 100% of registrations.</text>')
    c.render("d22-planning-horizon-ladder.png")

# ------------------------------------------------------------ diagram9
def diagram9():
    c = Canvas(1300, 900, "Provisional system timeline", "Governance history (secondhand, candidate) and operator history, with undated items kept apart")
    x0, x1 = 170, 1260
    tx = lambda m: x0 + (m / 26.0) * (x1 - x0)
    for m, lab in [(0, "Oct 2024"), (3, "Jan 2025"), (9, "Jul 2025"), (15, "Jan 2026"), (21, "Jul 2026"), (26, "Dec 2026")]:
        x = tx(m)
        c.add(f'<line x1="{x:.0f}" y1="96" x2="{x:.0f}" y2="575" stroke="#e3e8ee" stroke-width="1.4"/><text x="{x:.0f}" y="90" font-size="12" fill="#555" text-anchor="middle" font-weight="700">{lab}</text>')
    c.add(f'<rect x="14" y="104" width="136" height="210" rx="10" fill="#6a1b9a"/><text x="82" y="204" font-size="14" font-weight="800" fill="white" text-anchor="middle">Governance</text><text x="82" y="224" font-size="11.5" fill="white" text-anchor="middle">secondhand</text>')
    c.add(f'<rect x="14" y="330" width="136" height="250" rx="10" fill="#00695c"/><text x="82" y="450" font-size="14" font-weight="800" fill="white" text-anchor="middle">Operators</text>')
    c.add(f'<line x1="{x0}" y1="300" x2="{x1}" y2="300" stroke="#6a1b9a" stroke-width="3"/><line x1="{x0}" y1="566" x2="{x1}" y2="566" stroke="#00695c" stroke-width="3"/>')
    def ev(m, bx, y, w, text, key, axis_y, dashed=False, fs=12):
        s, f = C[key]
        lines = wrap(text, w - 14, fs)
        hh = len(lines) * fs * 1.25 + 14
        x = tx(m)
        by = y if axis_y > y else y
        c.add(f'<circle cx="{x:.0f}" cy="{axis_y}" r="6" fill="{s}"/>')
        ytop = y + hh if axis_y > y else y
        c.add(f'<line x1="{x:.0f}" y1="{axis_y}" x2="{bx + w/2:.0f}" y2="{(y + hh) if axis_y > y else y}" stroke="{s}" stroke-width="1.6" stroke-dasharray="3 3"/>')
        da = 'stroke-dasharray="5 4"' if dashed else ""
        c.add(f'<rect x="{bx:.0f}" y="{y:.0f}" width="{w}" height="{hh:.0f}" rx="8" fill="{f}" stroke="{s}" stroke-width="1.8" {da}/>')
        yy = y + 8 + fs
        for ln in lines:
            c.add(f'<text x="{bx+7:.0f}" y="{yy:.0f}" font-size="{fs}" fill="#1b1b1b">{esc(ln)}</text>'); yy += fs * 1.25
    ev(1, 170, 118, 270, "Nov 2024: Kadamba non-veg cancelled after a reported frog in the biryani", "soc", 300, True)
    ev(2, 460, 118, 330, "Dec 2024: cancellation rules tightened, reportedly for staff workload; Ping opinion survey; two Parliament meetings with the Mess Office", "soc", 300, True)
    ev(3, 810, 118, 330, "Jan 2025: policy defended by the incoming Committee chair; portal migration problems reported", "soc", 300, True)
    c.add(f'<text x="{x0}" y="262" font-size="12.5" fill="#6a1b9a" font-weight="700">No change to registration or billing rules is confirmed for the current semester.</text>')
    ev(10, 300, 346, 290, "About Aug 2025 (year candidate): ABC takes over Yuktāhār; per-item waste weighing starts, made blame-free", "biz", 566)
    ev(14, 610, 430, 250, "About Dec 2025: staff report waste falling", "biz", 566)
    ev(17, 890, 346, 250, "About Mar 2026: rock salt and cold-pressed oil", "biz", 566)
    ev(19, 700, 500, 250, "2026: Bakul switches paneer supplier twice", "biz", 566)
    ev(22, 960, 430, 300, "About Aug 2026: a new Bakul manager; Kadamba drops daily dinner sambar", "biz", 566)
    ev(26, 1100, 500, 180, "Dec 2026 (expected): Felicity kitchen opens", "ext", 566, True)
    c.zone(14, 600, 1272, 280, "Date unknown: kept apart, not guessed", "ext", fs=13.5, opacity=0.3)
    und = ["Bakul created when Kadamba's non-veg capacity was reached", "Prism wins Kadamba's tender and runs all operations (single-sourced)", "LPG shortage: Kadamba cuts quantities and buys outside; registration non-compulsory and the cap raised from five to ten (the holiday part is disputed)", "Zoho tried for grocery planning and prediction, then dropped", "A project manager takes staff to his farmhouse for training", "Kadamba's toaster broken, not replaced", "A supposed change of Bakul's ratio from 70 to 80% is withdrawn: the share varies by item and week"]
    for i, t_ in enumerate(und):
        cell(c, 30 + (i % 4) * 312, 634 + (i // 4) * 116, 300, 104, t_, "ext", fs=12.5)
    c.render("diagram9-provisional-timeline.png")

if __name__ == "__main__":
    d21(); d22(); diagram9()
