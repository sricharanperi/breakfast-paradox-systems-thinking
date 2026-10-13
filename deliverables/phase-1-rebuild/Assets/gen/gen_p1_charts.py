import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p1kit import *

DATA = os.path.join(os.path.dirname(__file__), "../../../../Observation images/Extracted Data")
DATA = os.path.abspath(DATA)
def rd(p): return list(csv.DictReader(open(os.path.join(DATA, p), encoding="utf-8-sig")))
BL, GR, OR, RD, AM = "#1565c0", "#90a4ae", "#e65100", "#c62828", "#e08600"

def axes(c, x0, y0, w, h, ymax, step, ylabel, fmt=lambda v: f"{v:g}"):
    for v in range(0, int(ymax) + 1, step):
        y = y0 + h - v / ymax * h
        c.add(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0+w}" y2="{y:.1f}" stroke="#e0e6ec" stroke-width="1.2"/>'
              f'<text x="{x0-8}" y="{y+4:.1f}" font-size="12" fill="#555" text-anchor="end">{fmt(v)}</text>')
    c.add(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="#90a4ae" stroke-width="1.6"/><line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="#90a4ae" stroke-width="1.6"/>')
    c.add(f'<text x="{x0-52}" y="{y0+h/2}" font-size="13" font-weight="700" fill="#333" text-anchor="middle" transform="rotate(-90 {x0-52} {y0+h/2})">{esc(ylabel)}</text>')

# ----------------------------------------------------------- diagram8: arrival curve
def diagram8():
    rows = rd("Kadamba_April2026/03_Arrival_15min.csv")
    per = rd("Kadamba_April2026/04_Arrival_per_minute_0900_0945.csv")
    rows = [r for r in rows if "07:00" <= r["slot_start"] <= "10:00"]
    c = Canvas(1200, 760, "Measured arrival curve, Kadamba breakfast, April 2026", "Share of all 11,941 scans in each fifteen-minute slot; kitchen events marked (confirmed, scan records)")
    x0, y0, w, h = 80, 120, 1080, 400
    ymax = 30
    axes(c, x0, y0, w, h, ymax, 5, "share of all scans (%)", lambda v: f"{v}%")
    n = len(rows); bw = w / n
    def xpos(hhmm):
        hh, mm = int(hhmm[:2]), int(hhmm[3:])
        idx = ((hh * 60 + mm) - (7 * 60)) / 15.0
        return x0 + idx * bw
    # shaded windows
    c.add(f'<rect x="{xpos("07:30"):.1f}" y="{y0}" width="{xpos("08:00")-xpos("07:30"):.1f}" height="{h}" fill="#1565c0" fill-opacity="0.10"/>')
    c.add(f'<text x="{(xpos("07:30")+xpos("08:00"))/2:.0f}" y="{y0+16}" font-size="11.5" fill="#1565c0" text-anchor="middle" font-weight="700">first half hour: 15.3%</text><text x="{(xpos("07:30")+xpos("08:00"))/2:.0f}" y="{y0+31}" font-size="11" fill="#1565c0" text-anchor="middle">Yuktāhār samples this window</text><text x="{(xpos("07:30")+xpos("08:00"))/2:.0f}" y="{y0+45}" font-size="11" fill="#1565c0" text-anchor="middle">(candidate transfer)</text>')
    c.add(f'<rect x="{xpos("09:30"):.1f}" y="{y0}" width="{xpos("10:00")-xpos("09:30"):.1f}" height="{h}" fill="#e08600" fill-opacity="0.14"/>')
    for r in rows:
        v = float(r["pct_of_all_scans"]); s = r["slot_start"]
        bx = xpos(s) + 4; bh = v / ymax * h
        col = RD if s == "09:15" else (AM if s >= "09:30" else BL)
        c.add(f'<rect x="{bx:.1f}" y="{y0+h-bh:.1f}" width="{bw-8:.1f}" height="{bh:.1f}" rx="3" fill="{col}"/>')
        if v >= 1:
            c.add(f'<text x="{bx+(bw-8)/2:.1f}" y="{y0+h-bh-5:.1f}" font-size="12" font-weight="700" fill="#222" text-anchor="middle">{v:.1f}</text>')
        if s.endswith(":00") or s.endswith(":30"):
            c.add(f'<text x="{bx+(bw-8)/2:.1f}" y="{y0+h+18}" font-size="12" fill="#555" text-anchor="middle">{s}</text>')
    c.add(f'<text x="{x0+w/2}" y="{y0+h+42}" font-size="13" font-weight="700" fill="#333" text-anchor="middle">scan time (start of each fifteen-minute slot)</text>')
    # kitchen markers
    for t, lab, dy in [("05:30", "", 0)]:
        pass
    marks = [("07:00", "7:00 live counter opens", RD, "start", -14), ("07:30", "7:30 service opens", BL, "start", -30), ("09:30", "9:30 formal close", "#444", "middle", -14)]
    for t_, lab, col, anc, dy in marks:
        x = xpos(t_)
        c.add(f'<line x1="{x:.1f}" y1="{y0+dy+6}" x2="{x:.1f}" y2="{y0+h}" stroke="{col}" stroke-width="1.8" stroke-dasharray="5 4"/>'
              f'<text x="{x+4:.1f}" y="{y0+dy}" font-size="12" font-weight="700" fill="{col}" text-anchor="{anc if anc!="start" else "start"}">{lab}</text>')
    c.add(f'<text x="{x0+w-4}" y="{y0-34}" font-size="12" font-weight="700" fill="#444" text-anchor="end">the chef batch starts at 5:30, before the first slot shown</text>')
    c.add(f'<text x="{xpos("09:45"):.0f}" y="{y0+h-52}" font-size="12" font-weight="700" fill="#b26a00" text-anchor="middle">back door</text><text x="{xpos("09:45"):.0f}" y="{y0+h-37}" font-size="11.5" fill="#b26a00" text-anchor="middle">9.2% of scans; latest 10:07</text>')
    # inset: per-minute 9:00-9:45
    ix, iy, iw, ih = 110, 590, 560, 120
    vals = [(r["minute"], float(r["avg_per_day"])) for r in per]
    vmax = 10.0
    c.add(f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" fill="#fafbfd" stroke="#cfd8dc"/>')
    bwm = iw / len(vals)
    for i, (m, v) in enumerate(vals):
        bh = v / vmax * ih
        col = RD if "09:15" <= m <= "09:29" else (AM if m >= "09:30" else BL)
        c.add(f'<rect x="{ix+i*bwm+0.5:.1f}" y="{iy+ih-bh:.1f}" width="{bwm-1:.1f}" height="{bh:.1f}" fill="{col}"/>')
        if m.endswith(":00") or m.endswith(":15") or m.endswith(":30") or m.endswith(":45"):
            c.add(f'<text x="{ix+i*bwm+bwm/2:.1f}" y="{iy+ih+15}" font-size="11" fill="#555" text-anchor="middle">{m}</text>')
    for v in (0, 5, 10):
        yy = iy + ih - v / vmax * ih
        c.add(f'<text x="{ix-6}" y="{yy+4:.1f}" font-size="11" fill="#555" text-anchor="end">{v}</text>')
    c.add(f'<text x="{ix}" y="{iy-10}" font-size="13" font-weight="800" fill="#333">Per minute, 9:00 to 9:45: scans per day (still about 9 a minute at 9:29)</text>')
    c.add(f'<text x="740" y="640" font-size="13" fill="#333">Share before 9:15: 64.3%</text><text x="740" y="662" font-size="13" fill="#333">Share 9:15 to 9:29: 26.5%</text><text x="740" y="684" font-size="13" fill="#333">Share 9:30 and after: 9.2%</text>')
    c.render("diagram8-crowd-curve.png")

# ----------------------------------------------------------- d18 daily registered vs eaten
def d18():
    rows = rd("Kadamba_April2026/01_Daily.csv")
    c = Canvas(1250, 640, "Kadamba breakfast, 1 to 30 April 2026: registered and scanned, each day", "Registrations (outline) stay near 1,070; scans (filled: veg, non-veg) swing with the weekday (confirmed, scan records)")
    x0, y0, w, h = 90, 100, 1110, 380
    axes(c, x0, y0, w, h, 1200, 200, "breakfasts per day", lambda v: f"{v:,}")
    n = len(rows); bw = w / n
    for i, r in enumerate(rows):
        x = x0 + i * bw
        reg = float(r["total_registered"]); va = float(r["veg_availed"]); na = float(r["nonveg_availed"])
        hr = reg / 1200 * h; hv = va / 1200 * h; hn = na / 1200 * h
        c.add(f'<rect x="{x+4:.1f}" y="{y0+h-hr:.1f}" width="{bw-8:.1f}" height="{hr:.1f}" fill="#eef2f6" stroke="#9aa5b1" stroke-width="1.4" rx="2"/>')
        c.add(f'<rect x="{x+4:.1f}" y="{y0+h-hv:.1f}" width="{bw-8:.1f}" height="{hv:.1f}" fill="{BL}"/>')
        c.add(f'<rect x="{x+4:.1f}" y="{y0+h-hv-hn:.1f}" width="{bw-8:.1f}" height="{hn:.1f}" fill="{OR}"/>')
        d = int(r["date"][-2:]); wk = r["weekday"]
        col = RD if wk == "Sun" else "#555"
        c.add(f'<text x="{x+bw/2:.1f}" y="{y0+h+16}" font-size="11.5" fill="{col}" text-anchor="middle" font-weight="{800 if wk=="Sun" else 400}">{d}</text><text x="{x+bw/2:.1f}" y="{y0+h+30}" font-size="10" fill="{col}" text-anchor="middle">{wk[0]}{"u" if wk in ("Su","Sun") else ""}</text>')
    c.add(f'<text x="{x0+w/2}" y="{y0+h+56}" font-size="13" font-weight="700" fill="#333" text-anchor="middle">day of April (Sundays in red)</text>')
    xr = x0 + 5 * bw
    c.add(f'<text x="{x0+bw*3.5:.0f}" y="{y0+h-hr-60 if False else y0+30}" font-size="12.5" font-weight="700" fill="#b26a00" text-anchor="middle">1 to 6 April: non-veg registrations climb from 137 to about 300 (cause unknown, not read as a trend)</text>')
    c.add(f'<line x1="{x0+bw*6}" y1="{y0+40}" x2="{x0+bw*6}" y2="{y0+h}" stroke="#e08600" stroke-width="1.4" stroke-dasharray="5 4"/>')
    c.legend(x0 + 20, y0 + 70, [("#eef2f6", "registered (outline)"), (BL, "scanned: veg"), (OR, "scanned: non-veg")])
    c.render("d18-kadamba-daily-registered-vs-eaten.png")

# ----------------------------------------------------------- d19 weekday turnout
def d19():
    rows = rd("Kadamba_April2026/02_By_Weekday.csv")
    c = Canvas(1000, 600, "Kadamba breakfast turnout by weekday, April 2026", "Share of registrations that were scanned; registrations stay flat at about 1,070 (confirmed, scan records)")
    x0, y0, w, h = 90, 110, 860, 380
    axes(c, x0, y0, w, h, 50, 10, "share who ate (%)", lambda v: f"{v}%")
    bw = w / len(rows)
    for i, r in enumerate(rows):
        v = float(r["availed_pct"]); x = x0 + i * bw; bh = v / 50 * h
        col = RD if r["weekday"] == "Sun" else BL
        c.add(f'<rect x="{x+16:.1f}" y="{y0+h-bh:.1f}" width="{bw-32:.1f}" height="{bh:.1f}" rx="4" fill="{col}"/>')
        c.add(f'<text x="{x+bw/2:.1f}" y="{y0+h-bh-8:.1f}" font-size="14" font-weight="800" fill="#222" text-anchor="middle">{v:.1f}%</text>')
        c.add(f'<text x="{x+bw/2:.1f}" y="{y0+h+22}" font-size="14" fill="#333" text-anchor="middle" font-weight="700">{r["weekday"]}</text>')
        c.add(f'<text x="{x+bw/2:.1f}" y="{y0+h+40}" font-size="11.5" fill="#666" text-anchor="middle">{int(float(r["avg_registered"])):,} registered</text>')
    c.add(f'<text x="{x0+w/2}" y="{y0-18}" font-size="13" fill="#555" text-anchor="middle">Weekdays together 39.3%, weekends 31.1%, whole month 37.1%</text>')
    c.render("d19-weekday-turnout.png")

# ----------------------------------------------------------- d20 Yuktahaar breakfast vs lunch
def d20():
    b = rd("csv/02_Attendance_Breakfast.csv"); l = rd("csv/01_Attendance_Lunch.csv")
    c = Canvas(1200, 690, "Yuktāhār, 1 to 20 September 2026: share who ate, breakfast against lunch", "Operator's attendance register, photographed (confirmed, records); seven breakfast rows are partly hidden by a hand")
    x0, y0, w, h = 90, 110, 1090, 380
    axes(c, x0, y0, w, h, 100, 20, "share who ate (%)", lambda v: f"{v}%")
    n = 20; bw = w / n
    pts_l = []; 
    for i in range(n):
        x = x0 + i * bw + bw / 2
        lv = float(l[i]["attendance_pct_computed"]); pts_l.append((x, y0 + h - lv / 100 * h))
        bv = b[i]["attendance_pct_computed"]; wk = b[i]["weekday"]
        if bv:
            v = float(bv); bh = v / 100 * h
            c.add(f'<rect x="{x-bw*0.36:.1f}" y="{y0+h-bh:.1f}" width="{bw*0.72:.1f}" height="{bh:.1f}" rx="3" fill="{RD}"/>')
            c.add(f'<text x="{x:.1f}" y="{y0+h-bh-5:.1f}" font-size="10.5" font-weight="700" fill="#222" text-anchor="middle">{v:.0f}</text>')
        else:
            c.add(f'<rect x="{x-bw*0.36:.1f}" y="{y0+h-26:.1f}" width="{bw*0.72:.1f}" height="26" rx="3" fill="#fff" stroke="#9aa5b1" stroke-dasharray="3 3"/><text x="{x:.1f}" y="{y0+h-9:.1f}" font-size="9.5" fill="#777" text-anchor="middle">hidden</text>')
        col = RD if wk == "Sun" else "#555"
        c.add(f'<text x="{x:.1f}" y="{y0+h+16}" font-size="11.5" fill="{col}" text-anchor="middle" font-weight="{800 if wk=="Sun" else 400}">{i+1}</text><text x="{x:.1f}" y="{y0+h+30}" font-size="10" fill="{col}" text-anchor="middle">{wk[:2]}</text>')
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts_l)
    c.add(f'<path d="{d}" fill="none" stroke="{BL}" stroke-width="3.4"/>' + "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{BL}"/>' for x, y in pts_l))
    y50 = y0 + h - 0.5 * h
    c.add(f'<line x1="{x0}" y1="{y50:.1f}" x2="{x0+w}" y2="{y50:.1f}" stroke="#555" stroke-width="1.8" stroke-dasharray="7 5"/><text x="{x0+w-6}" y="{y50-6:.1f}" font-size="12" fill="#444" text-anchor="end" font-weight="700">the site head believes breakfast runs at about 50%</text>')
    c.add(f'<text x="{x0+w/2}" y="{y0+h+54}" font-size="13" font-weight="700" fill="#333" text-anchor="middle">day of September (Sundays in red)</text>')
    c.legend(x0 + 20, y0 + h + 66, [(RD, "breakfast: 17.7% to 40.2%, mean about 28%"), (BL, "lunch: 56% to 89%, at least 70% on fifteen days", "line")])
    c.render("d20-yuktahaar-breakfast-vs-lunch.png")

if __name__ == "__main__":
    diagram8(); d18(); d19(); d20()
