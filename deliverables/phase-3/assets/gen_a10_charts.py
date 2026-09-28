"""Activity 10 charts: hand-built SVG, rasterised through headless Chrome.

Chart 1: kitchen scenarios compared (backtest, 8 to 30 April 2026).
Chart 2: one Sunday veg line, arrivals against the baseline and refined batches.
Chart 3: behaviour-over-time projection of the recommended bundle.
All values come from scenario_model.py; every value is projected.
Palette: project palette; grey marks the baseline (neutral reference), and the
three scenario hues were checked with the dataviz validator (light mode, pass).
"""
import sys, io, contextlib, runpy, os, csv
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project/.claude/skills/systems-visual-design")
from svgkit import render

with contextlib.redirect_stdout(io.StringIO()):
    M = runpy.run_path(os.path.join(HERE, "scenario_model.py"))

INK, INK2, MUTED, GRID = "#1b1b1b", "#444", "#777", "#e6e6e6"
BASE, PARAM, SINGLE, REF = "#757575", "#8e24aa", "#e65100", "#1565c0"
CREST = "#fdecea"
FONT = 'font-family="Helvetica,Arial,sans-serif"'


def t(x, y, s, size=14, w="400", c=INK, a="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" {FONT} font-size="{size}" font-weight="{w}" fill="{c}" text-anchor="{a}">{s}</text>'


def svg(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="{w}" height="{h}" fill="white"/>{body}</svg>'


def bar(x, y, w, h, c):
    # 4px rounded data end, square at the baseline
    r = min(4, w / 2)
    return (f'<path d="M{x},{y} H{x + w - r} Q{x + w},{y} {x + w},{y + r} V{y + h - r} '
            f'Q{x + w},{y + h} {x + w - r},{y + h} H{x} Z" fill="{c}"/>')


# ------------------------------------------------------------------ chart 1
rows = list(csv.DictReader(open(os.path.join(HERE, "scen_kitchen_summary.csv"))))
lab = {"S0": ("Baseline", "70% of registrations, one batch", BASE),
       "S5": ("Ratio cut to 50%", "parameter only", PARAM),
       "S1": ("Calibrated, one batch", "record forecast + 10%", SINGLE),
       "S1b": ("Calibrated + late batch", "refined design", REF)}
W, H = 1400, 560
b = [t(40, 48, "Kitchen scenarios on the April records: surplus and shortage per day", 24, "700"),
     t(40, 76, "Kadamba breakfast, both lines, backtested on 23 days (8 to 30 April 2026). Portions a day. Projected.", 15, "400", INK2)]
panels = [("surplus_per_day", "Cooked but not eaten by students", 420, 400),
          ("shortfall_per_day", "Diners short at the counter after the batches", 900, 20)]
y0 = 130
for key, title, px, vmax in panels:
    pw = 380
    b.append(t(px, y0 - 14, title, 16, "700"))
    for gx in range(0, vmax + 1, vmax // 4):
        xx = px + pw * gx / vmax
        b.append(f'<line x1="{xx:.1f}" y1="{y0}" x2="{xx:.1f}" y2="{y0 + 4 * 90 - 20}" stroke="{GRID}" stroke-width="1"/>')
        b.append(t(xx, y0 + 4 * 90 - 2, str(gx), 12, "400", MUTED, "middle"))
    for i, r in enumerate(rows):
        v = float(r[key])
        yy = y0 + 10 + i * 90
        c = lab[r["scenario"]][2]
        w = max(pw * v / vmax, 2)
        b.append(bar(px, yy, w, 44, c))
        b.append(t(px + w + 8, yy + 28, f"{v:.0f}" if key == "surplus_per_day" else f"{v:.1f}", 15, "700", INK))
for i, r in enumerate(rows):
    yy = y0 + 10 + i * 90
    n, sub, c = lab[r["scenario"]]
    b.append(f'<circle cx="48" cy="{yy + 16}" r="7" fill="{c}"/>')
    b.append(t(62, yy + 21, n, 16, "700"))
    b.append(t(62, yy + 41, sub, 13, "400", INK2))
b.append(t(40, H - 30, "Shortage is counted after every planned batch; the ordinary counter top-up (10 to 15 minutes) still acts on it. The ratio cut's shortage falls entirely on the non-veg line.", 13, "400", MUTED))
render(svg(W, H, "".join(b)), os.path.join(HERE, "chart-a10-kitchen-scenarios.png"), W, H)

# ------------------------------------------------------------------ chart 2
from datetime import date
d = date(2026, 4, 19)
l = "veg"
sc = M["scans"][(d, l)]
Rg = M["R"][(d, l)]
e = len(sc)
F = M["st"].mean(M["prior_same_weekday"](d, l))
ref = M["REFINED"]
land = ref["trigger"] + M["A"]["topup_minutes"]
b1 = F * M["prior_share"](d, land) * (1 + ref["bf"])
n_trig = sum(1 for x in sc if x < ref["trigger"])
late = max(n_trig / M["prior_share"](d, ref["trigger"]) * (1 + ref["bl"]) - b1, 0)
base_b = 0.7 * Rg
W, H = 1460, 700
X0, X1, Y0, Y1 = 120, 1180, 610, 130
tmin, tmax, vmax = 7 * 60, 9 * 60 + 45, 600
X = lambda m: X0 + (X1 - X0) * (m - tmin) / (tmax - tmin)
Y = lambda v: Y0 - (Y0 - Y1) * v / vmax
b = [t(40, 48, "One Sunday on the veg line: who arrives, and what each rule cooks", 24, "700"),
     t(40, 76, f"Kadamba, Sunday 19 April 2026: {Rg} registered, {e} ate (records). Batches are projected under each rule.", 15, "400", INK2)]
b.append(f'<rect x="{X(555):.1f}" y="{Y1}" width="{X(570) - X(555):.1f}" height="{Y0 - Y1}" fill="{CREST}"/>')
b.append(t((X(555) + X(570)) / 2, Y1 + 18, "closing crest", 13, "700", "#c62828", "middle"))
for v in range(0, vmax + 1, 100):
    b.append(f'<line x1="{X0}" y1="{Y(v):.1f}" x2="{X1}" y2="{Y(v):.1f}" stroke="{GRID}"/>')
    b.append(t(X0 - 10, Y(v) + 5, str(v), 13, "400", MUTED, "end"))
for m in range(tmin, tmax + 1, 30):
    b.append(t(X(m), Y0 + 24, f"{m // 60}:{m % 60:02d}", 13, "400", MUTED, "middle"))
b.append(t(X0 - 60, Y1 - 16, "portions or diners", 13, "400", MUTED))
# cumulative arrivals
pts = [(X(tmin), Y(0))]
n = 0
for x in sc:
    if x < tmin:
        n += 1
        continue
    pts.append((X(x), Y(n)))
    n += 1
    pts.append((X(x), Y(n)))
pts.append((X(tmax), Y(n)))
b.append('<polyline fill="none" stroke="#1b1b1b" stroke-width="2.5" points="' + " ".join(f"{a:.1f},{c:.1f}" for a, c in pts) + '"/>')
b.append(t(X(tmax) + 8, Y(e) - 10, f"diners so far ({e} by close)", 14, "700", INK))
# baseline batch
b.append(f'<line x1="{X(tmin)}" y1="{Y(base_b):.1f}" x2="{X(tmax)}" y2="{Y(base_b):.1f}" stroke="{BASE}" stroke-width="3" stroke-dasharray="10 6"/>')
b.append(t(X(tmax) + 8, Y(base_b) + 5, f"baseline: {base_b:.0f} cooked", 14, "700", INK))
# refined: first batch, then late batch lands
b.append(f'<polyline fill="none" stroke="{REF}" stroke-width="3" points="{X(tmin)},{Y(b1):.1f} {X(land)},{Y(b1):.1f} {X(land)},{Y(b1 + late):.1f} {X(tmax)},{Y(b1 + late):.1f}"/>')
b.append(t(X(tmax) + 8, Y(b1 + late) + 22, f"refined: {b1:.0f} first + {late:.0f} late", 14, "700", INK))
b.append(f'<circle cx="{X(ref["trigger"]):.1f}" cy="{Y(n_trig):.1f}" r="6" fill="white" stroke="{REF}" stroke-width="3"/>')
b.append(t(X(ref["trigger"]) - 12, Y(n_trig) + 50, f"9:00: {n_trig} seen, late batch started", 14, "400", INK2, "end"))
b.append(f'<line x1="{X(ref["trigger"]) - 8:.1f}" y1="{Y(n_trig) + 36:.1f}" x2="{X(ref["trigger"]):.1f}" y2="{Y(n_trig) + 8:.1f}" stroke="{MUTED}"/>')
b.append(t(X0, H - 20, f"Gap between the dashed line and the black curve at close is the baseline surplus ({base_b - e:.0f}); the refined batches leave {max(e - b1 - late, 0):.0f} diners to the ordinary counter top-up in the last minutes.", 13, "400", MUTED))
render(svg(W, H, "".join(b)), os.path.join(HERE, "chart-a10-sunday-veg-batches.png"), W, H)

# ------------------------------------------------------------------ chart 3
bot = list(csv.DictReader(open(os.path.join(HERE, "scen_bot_projection.csv"))))
W, H = 1400, 760
b = [t(40, 48, "Projected behaviour over time: the recommended bundle against the baseline", 24, "700"),
     t(40, 76, "Kadamba breakfast. Weeks from the start of Stage 1. Adoption pace is assumed; all values projected.", 15, "400", INK2)]


def panel(y_top, h, key_b, key_n, vmax, step, title, fmt):
    X0, X1 = 130, 1160
    Yb, Yt = y_top + h, y_top
    X = lambda wk: X0 + (X1 - X0) * wk / 20
    Y = lambda v: Yb - (Yb - Yt) * v / vmax
    out = [t(40, y_top - 16, title, 16, "700")]
    for s0, s1, name in [(0, 4, "Stage 1"), (4, 8, "Stage 2"), (8, 20, "Stage 3")]:
        out.append(f'<rect x="{X(s0):.1f}" y="{Yt}" width="{X(s1) - X(s0) - 2:.1f}" height="{h}" fill="{"#f5f7fb" if name != "Stage 2" else "#eef3fb"}"/>')
        out.append(t(X(s0) + 8, Yt + 18, name, 12, "700", MUTED))
    for v in range(0, vmax + 1, step):
        out.append(f'<line x1="{X0}" y1="{Y(v):.1f}" x2="{X1}" y2="{Y(v):.1f}" stroke="{GRID}"/>')
        out.append(t(X0 - 10, Y(v) + 5, fmt(v), 12, "400", MUTED, "end"))
    for wk in range(0, 21, 4):
        out.append(t(X(wk), Yb + 22, f"week {wk}", 12, "400", MUTED, "middle"))
    pb = " ".join(f"{X(int(r['week'])):.1f},{Y(float(r[key_b])):.1f}" for r in bot)
    pn = " ".join(f"{X(int(r['week'])):.1f},{Y(float(r[key_n])):.1f}" for r in bot)
    out.append(f'<polyline fill="none" stroke="{BASE}" stroke-width="2.5" stroke-dasharray="10 6" points="{pb}"/>')
    out.append(f'<polyline fill="none" stroke="{REF}" stroke-width="3" points="{pn}"/>')
    for r in bot:
        out.append(f'<circle cx="{X(int(r["week"])):.1f}" cy="{Y(float(r[key_n])):.1f}" r="5" fill="{REF}" stroke="white" stroke-width="2"/>')
    last = bot[-1]
    yb_, yn_ = Y(float(last[key_b])), Y(float(last[key_n]))
    if abs(yn_ - yb_) < 20:
        yb_, yn_ = yb_ - 8, yb_ + 14
    out.append(t(X(20) + 10, yb_ + 5, "baseline " + fmt(float(last[key_b])), 14, "700", INK))
    out.append(t(X(20) + 10, yn_ + 5, "bundle " + fmt(float(last[key_n])), 14, "700", INK))
    return "".join(out)


b.append(panel(130, 230, "baseline_surplus_per_day", "bundle_surplus_per_day", 400, 100,
               "First-batch surplus: portions cooked but not eaten by students, per day", lambda v: f"{v:.0f}"))
b.append(panel(470, 200, "baseline_uneaten_charge_rs_per_week", "bundle_uneaten_charge_rs_per_week", 300000, 100000,
               "Charges students pay for breakfasts they do not eat, per week (Rs)", lambda v: f"{v / 1000:.0f}k"))
b.append(t(40, H - 22, "Stage 1: routes and paper record. Stage 2: Sunday veg-line pilot. Stage 3: roll-out to every day and line; from week 14 the Sunday evening-before skip, if the rule owner adopts it (25% uptake assumed).", 13, "400", MUTED))
render(svg(W, H, "".join(b)), os.path.join(HERE, "chart-a10-bot-projection.png"), W, H)
