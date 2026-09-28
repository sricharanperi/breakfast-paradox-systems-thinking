"""Activity 10 charts: hand-built SVG, rasterised through headless Chrome.

Chart 1: kitchen scenarios compared (backtest, 8 to 30 April 2026).
Chart 2: one Sunday veg line, arrivals against the baseline and refined batches.
Chart 3: behaviour-over-time projection of the re-sequenced bundle, with ranges.
Chart 4: stress tests of the refined kitchen design.
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
W, H = 1400, 820
b = [t(40, 48, "How the system might respond over time: the re-sequenced bundle against the baseline", 24, "700"),
     t(40, 76, "Kadamba breakfast. Weeks from the start of Stage 1. Lines are central values, shaded bands the tested ranges. Adoption pace and rule-owner timing assumed; all values projected.", 15, "400", INK2)]
COND = "#6a1b9a"


def band(X, Y, lo_key, hi_key, color, op, rows):
    up = [f"{X(int(r['week'])):.1f},{Y(float(r[hi_key])):.1f}" for r in rows]
    dn = [f"{X(int(r['week'])):.1f},{Y(float(r[lo_key])):.1f}" for r in reversed(rows)]
    return f'<polygon points="{" ".join(up + dn)}" fill="{color}" fill-opacity="{op}"/>'


def panel(y_top, h, key_b, key_n, bands, vmax, step, title, fmt, marks, extra=None, mark_low=False):
    X0, X1 = 130, 1130
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
    for lo, hi, c in bands:
        out.append(band(X, Y, lo, hi, c, 0.16, bot))
    if extra:
        out.append(extra(X, Y))
    pb = " ".join(f"{X(int(r['week'])):.1f},{Y(float(r[key_b])):.1f}" for r in bot)
    pn = " ".join(f"{X(int(r['week'])):.1f},{Y(float(r[key_n])):.1f}" for r in bot)
    out.append(f'<polyline fill="none" stroke="{BASE}" stroke-width="2.5" stroke-dasharray="10 6" points="{pb}"/>')
    out.append(f'<polyline fill="none" stroke="{REF}" stroke-width="3" points="{pn}"/>')
    for r in bot:
        out.append(f'<circle cx="{X(int(r["week"])):.1f}" cy="{Y(float(r[key_n])):.1f}" r="5" fill="{REF}" stroke="white" stroke-width="2"/>')
    for wk, lab in marks:
        out.append(f'<line x1="{X(wk):.1f}" y1="{Yt + 26}" x2="{X(wk):.1f}" y2="{Yb}" stroke="{INK2}" stroke-width="1.5" stroke-dasharray="3 4"/>')
        out.append(t(X(wk) + 5, (Yb - 12) if mark_low else (Yt + 38), lab, 12, "700", INK2))
    last = bot[-1]
    yb_, yn_ = Y(float(last[key_b])), Y(float(last[key_n]))
    if abs(yn_ - yb_) < 20:
        yb_, yn_ = yb_ - 8, yb_ + 14
    out.append(t(X(20) + 10, yb_ + 5, "baseline " + fmt(float(last[key_b])), 14, "700", INK))
    out.append(t(X(20) + 10, yn_ + 5, "bundle " + fmt(float(last[key_n])), 14, "700", INK))
    return "".join(out)


def cond(X, Y):
    rows = [r for r in bot if int(r["week"]) >= 14]
    o = band(X, Y, "conditional_everyday_charge_low", "conditional_everyday_charge_high", COND, 0.14, rows)
    mid = " ".join(f"{X(int(r['week'])):.1f},{Y((float(r['conditional_everyday_charge_low']) + float(r['conditional_everyday_charge_high'])) / 2):.1f}" for r in rows)
    o += f'<polyline fill="none" stroke="{COND}" stroke-width="2.5" stroke-dasharray="4 4" points="{mid}"/>'
    r = rows[-1]
    o += t(X(20) + 10, Y((float(r["conditional_everyday_charge_low"]) + float(r["conditional_everyday_charge_high"])) / 2) + 5,
           "if every-day skip: 123k to 185k", 13, "700", INK)
    return o


b.append(panel(130, 240, "baseline_surplus_per_day", "bundle_surplus_per_day",
               [("baseline_surplus_low", "baseline_surplus_high", BASE), ("bundle_surplus_low", "bundle_surplus_high", REF)],
               500, 100, "First-batch surplus: portions cooked but not eaten by students, per day", lambda v: f"{v:.0f}",
               [(4, "joint reading"), (6, "skip proposed")]))
b.append(panel(500, 220, "baseline_uneaten_charge_rs_per_week", "bundle_uneaten_charge_rs_per_week",
               [("bundle_charge_low", "bundle_charge_high", REF)], 300000, 100000,
               "Charges students pay for breakfasts they do not eat, per week (Rs)", lambda v: f"{v / 1000:.0f}k",
               [(10, "Sunday skip in force"), (14, "decision point")], cond, mark_low=True))
b.append(t(40, H - 44, "Surplus bands: the operator's first-batch ratio at 60 to 80 percent, and the crest share 5 points lighter or heavier. Charge band: skip uptake 25 to 50 percent of no-shows.", 13, "400", MUTED))
b.append(t(40, H - 22, "Purple dashed: the every-day skip from week 16, only if the decision rule at week 14 is met and the calibrated batch runs on every line.", 13, "400", MUTED))
render(svg(W, H, "".join(b)), os.path.join(HERE, "chart-a10-bot-projection.png"), W, H)

# ------------------------------------------------------------------ chart 4: stress and sensitivity
st_rows = list(csv.DictReader(open(os.path.join(HERE, "scen_stress.csv"))))
short_lab = {"normal": ("Normal day", "backtest, 23 days"),
             "exam_unwarned": ("Exam or fest week", "25% fewer eaters, no warning"),
             "exam_warned": ("Exam week, calendar note", "forecast scaled by 0.75"),
             "favourite": ("Favourite-item day", "25% more eaters, no warning"),
             "eaters_minus10": ("Eaters down 10%", "a rule change shifts eaters"),
             "eaters_plus10": ("Eaters up 10%", "a rule change shifts eaters"),
             "crest_plus10": ("Heavier crest", "10 points more after 9:15"),
             "gas": ("Gas shortage", "batches take 30 minutes"),
             "late_fail": ("Failed 9:00 late batch", "reactive top-up only")}
WAIT = "#e65100"
W, H = 1400, 60 + 130 + 9 * 62 + 90
b = [t(40, 48, "Stress tests: where the calibrated batch with a 9:00 late batch holds, and where it breaks", 24, "700"),
     t(40, 76, "Kadamba breakfast, both lines, 23 backtest days. The plan reads normal earlier weeks unless stated. Per day, projected.", 15, "400", INK2)]
y0 = 150
px1, pw1, v1 = 470, 330, 500
px2, pw2, v2 = 900, 380, 50
b.append(t(px1, y0 - 22, "Surplus: cooked, not eaten by students", 15, "700"))
b.append(t(px2, y0 - 22, "Diners short after planned batches, and diners waiting", 15, "700"))
for gx in range(0, v1 + 1, 100):
    xx = px1 + pw1 * gx / v1
    b.append(f'<line x1="{xx:.1f}" y1="{y0}" x2="{xx:.1f}" y2="{y0 + 9 * 62}" stroke="{GRID}"/>')
    b.append(t(xx, y0 + 9 * 62 + 18, str(gx), 12, "400", MUTED, "middle"))
for gx in range(0, v2 + 1, 10):
    xx = px2 + pw2 * gx / v2
    b.append(f'<line x1="{xx:.1f}" y1="{y0}" x2="{xx:.1f}" y2="{y0 + 9 * 62}" stroke="{GRID}"/>')
    b.append(t(xx, y0 + 9 * 62 + 18, str(gx), 12, "400", MUTED, "middle"))
for i, r in enumerate(st_rows):
    yy = y0 + 8 + i * 62
    n, sub = short_lab[r["key"]]
    b.append(t(40, yy + 18, n, 15, "700"))
    b.append(t(40, yy + 37, sub, 13, "400", INK2))
    sv, bv = float(r["refined_surplus_per_day"]), float(r["baseline_surplus_per_day"])
    b.append(bar(px1, yy + 6, max(pw1 * sv / v1, 2), 30, REF))
    bx = px1 + pw1 * bv / v1
    b.append(f'<line x1="{bx:.1f}" y1="{yy}" x2="{bx:.1f}" y2="{yy + 42}" stroke="{BASE}" stroke-width="3"/>')
    b.append(t(px1 + pw1 * sv / v1 + 8, yy + 27, f"{sv:.0f}", 14, "700"))
    shv, wv = float(r["refined_short_per_day"]), float(r["refined_diners_waiting_per_day"])
    b.append(bar(px2, yy + 2, max(pw2 * shv / v2, 2), 18, REF))
    b.append(bar(px2, yy + 22, max(pw2 * wv / v2, 2), 18, WAIT))
    b.append(t(px2 + pw2 * shv / v2 + 8, yy + 16, f"{shv:.1f} short", 12, "700"))
    b.append(t(px2 + pw2 * wv / v2 + 8, yy + 36, f"{wv:.1f} waiting", 12, "400", INK2))
ly = y0 + 9 * 62 + 46
b.append(f'<rect x="40" y="{ly - 12}" width="16" height="16" rx="3" fill="{REF}"/>')
b.append(t(64, ly + 1, "calibrated first batch + 9:00 late batch", 13))
b.append(f'<line x1="380" y1="{ly - 12}" x2="380" y2="{ly + 6}" stroke="{BASE}" stroke-width="3"/>')
b.append(t(392, ly + 1, "baseline surplus (70% of registrations) on the same day", 13))
b.append(f'<rect x="780" y="{ly - 12}" width="16" height="16" rx="3" fill="{WAIT}"/>')
b.append(t(804, ly + 1, "diners who arrive after the first batch runs out, before the next batch lands", 13))
b.append(t(40, ly + 30, "Stresses are assumed shocks applied to the recorded arrivals; they explore how the rule responds, not how often each shock occurs.", 13, "400", MUTED))
render(svg(W, H, "".join(b)), os.path.join(HERE, "chart-a10-stress-tests.png"), W, H)
