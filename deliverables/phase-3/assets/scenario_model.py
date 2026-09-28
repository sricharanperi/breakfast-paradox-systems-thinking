"""Activity 10: scenario model for the breakfast interventions.

Reads the Kadamba April 2026 breakfast scan export (one row per registration,
scan time if eaten) and the Yuktahaar September 2026 breakfast register, and
projects, per scenario, the first-batch surplus, the top-up load at the closing
crest and the charges students pay for breakfasts they do not eat.

Every output is PROJECTED. Inputs are tagged in ASSUMPTIONS below. No unit cost
of food and no waste weight is used: surplus is in portions, one portion being
one diner's gram-standard breakfast. Rupee figures are only the posted student
rates multiplied by counted uneaten registrations.

Pure standard library (csv, zipfile, xml), so it runs without pandas.
Run:  python3 scenario_model.py   (writes scen_*.csv next to this file)
"""
import csv, os, re, zipfile, statistics as st
from collections import defaultdict
from datetime import date, datetime

ROOT = "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project"
RAW = os.path.join(ROOT, "Observation images/april-data.xlsx")
DAILY = os.path.join(ROOT, "Observation images/Extracted Data/Kadamba_April2026/01_Daily.csv")
YUK_BF = os.path.join(ROOT, "Observation images/Extracted Data/csv/02_Attendance_Breakfast.csv")
OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- assumptions
ASSUMPTIONS = [
    # (key, value, basis)
    ("ratio_kadamba", 0.70, "single-sourced: Kadamba cooks 70% of registrations in the first batch, per line"),
    ("rate_veg", 48, "confirmed: posted registered rate, Kadamba veg breakfast (Rs); posted Sept 2026 rates applied to April counts (assumed unchanged)"),
    ("rate_nonveg", 66, "confirmed: posted registered rate, Kadamba non-veg breakfast (Rs); same caveat"),
    ("rate_yuk", 53, "confirmed: posted registered rate, Yuktahaar breakfast (Rs)"),
    ("buffer", 0.10, "assumed: safety margin added to a record-based forecast"),
    ("allowance_outside", 30, "single-sourced: about 30 portions cooked for 30-50 outside diners"),
    ("allowance_staff_extra", 30, "assumed: a further allowance for about half of Kadamba staff (headcount unknown)"),
    ("topup_minutes", 15, "single-sourced: on-site top-up lands in 10-15 minutes (upper value used)"),
    ("flat_share_by_0800", 0.25, "assumed stand-in for a flat projection: 30 of 120 service minutes (7:30-9:30)"),
    ("optin_turnout_low", 0.60, "candidate: Yuktahaar June Saturdays, registered students ate at about 60% (regime unconfirmed)"),
    ("optin_turnout_mid", 0.72, "assumed midpoint"),
    ("optin_turnout_high", 0.85, "assumed: a confirmation close to intent"),
    ("walkin_share", 0.05, "assumed: share of Sunday eaters who do not opt in but still come"),
    ("skip_share_info_only", 0.00, "confirmed direction: Skip Meal that returns nothing is almost never used (L2)"),
    ("skip_share_refund_low", 0.25, "assumed: share of eventual no-shows who skip the evening before if skipping removes the charge"),
    ("skip_share_refund_high", 0.50, "assumed: upper value"),
    ("cancel_cap", 5, "confirmed: cancellations per meal type per month"),
]
A = {k: v for k, v, _ in ASSUMPTIONS}
RATE = {"veg": A["rate_veg"], "nonveg": A["rate_nonveg"]}
WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def mins(hhmmss):
    h, m, s = hhmmss.split(":")
    return int(h) * 60 + int(m) + float(s) / 60


# ---------------------------------------------------------------- load raw export
def load_raw():
    z = zipfile.ZipFile(RAW)
    ss_xml = z.read("xl/sharedStrings.xml").decode()
    strings = [re.sub(r"<[^>]+>", "", m) for m in re.findall(r"<si>(.*?)</si>", ss_xml, re.S)]
    sheet = z.read("xl/worksheets/sheet1.xml").decode()
    rows = []
    for rm in re.finditer(r'<row r="(\d+)"[^>]*>(.*?)</row>', sheet, re.S):
        if rm.group(1) == "1":
            continue
        cells = {}
        for cm in re.finditer(r'<c r="([A-Z]+)\d+"([^>]*)>(?:<v>(.*?)</v>)?</c>', rm.group(2)):
            col, attrs, v = cm.groups()
            if v is None:
                continue
            cells[col] = strings[int(v)] if 't="s"' in attrs else v
        d = date.fromordinal(date(1899, 12, 30).toordinal() + int(float(cells["A"])))
        line = "veg" if cells["B"].endswith("-veg") else "nonveg"
        t = None
        if "C" in cells:
            t = mins(cells["C"][11:19])
        rows.append((d, line, t))
    return rows


rows = load_raw()
R = defaultdict(int)
scans = defaultdict(list)
for d, line, t in rows:
    R[(d, line)] += 1
    if t is not None:
        scans[(d, line)].append(t)
for k in scans:
    scans[k].sort()
days = sorted({d for d, _, _ in rows})

# cross-check against the published daily table
with open(DAILY, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        d = date.fromisoformat(r["date"])
        assert R[(d, "veg")] == int(r["veg_registered"]), d
        assert len(scans[(d, "veg")]) == int(r["veg_availed"]), d
        assert R[(d, "nonveg")] == int(r["nonveg_registered"]), d
        assert len(scans[(d, "nonveg")]) == int(r["nonveg_availed"]), d


def E(d, line):
    return len(scans[(d, line)])


def wd(d):
    return WD[d.weekday()]


def cum_share(d, lines, t):
    tot = sum(E(d, l) for l in lines)
    n = sum(sum(1 for x in scans[(d, l)] if x < t) for l in lines)
    return n / tot if tot else 0.0


def pooled_share(ds, t):
    """Share of all scans on days ds that fall before time t (pooled, as in Activity 9)."""
    tot = sum(E(d, l) for d in ds for l in ["veg", "nonveg"])
    n = sum(1 for d in ds for l in ["veg", "nonveg"] for x in scans[(d, l)] if x < t)
    return n / tot if tot else None


def write(name, header, data):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(data)


write("scen_assumptions.csv", ["key", "value", "basis"], ASSUMPTIONS)

T0800, T0900, T0915, T0930 = 8 * 60, 9 * 60, 9 * 60 + 15, 9 * 60 + 30

# ---------------------------------------------------------------- weekday arrival profile (records)
prof_rows = []
for w in WD:
    ds = [d for d in days if wd(d) == w]
    c8 = pooled_share(ds, T0800)
    c9 = pooled_share(ds, T0900)
    c915 = pooled_share(ds, T0915)
    c930 = pooled_share(ds, T0930)
    last15 = st.mean(sum(1 for l in ["veg", "nonveg"] for x in scans[(d, l)] if T0915 <= x < T0930) for d in ds)
    prof_rows.append([w, len(ds), round(100 * c8, 1), round(100 * c9, 1), round(100 * c915, 1),
                      round(100 * c930, 1), round(100 * (1 - c915), 1), round(last15, 1)])
write("scen_weekday_profile.csv",
      ["weekday", "days", "pct_by_0800", "pct_by_0900", "pct_by_0915", "pct_by_0930", "pct_after_0915", "avg_scans_0915_0930"],
      prof_rows)

# ---------------------------------------------------------------- S0 baseline, per day and line
base_rows = []
for d in days:
    for l in ["veg", "nonveg"]:
        r, e = R[(d, l)], E(d, l)
        b0 = A["ratio_kadamba"] * r
        base_rows.append([d.isoformat(), wd(d), l, r, e, round(100 * e / r, 1), round(b0), round(b0 - e),
                          round(b0 / e, 2), (r - e), (r - e) * RATE[l]])
write("scen_baseline_daily.csv",
      ["date", "weekday", "line", "registered", "eaten", "turnout_pct", "first_batch_70pct", "first_batch_surplus",
       "batch_to_eaten", "uneaten_registrations", "uneaten_charge_rs"], base_rows)


# ---------------------------------------------------------------- helpers for the backtest
def prior_same_weekday(d, l):
    """Eaten on earlier April days with the same weekday and line (strictly before d)."""
    return [E(x, l) for x in days if x < d and wd(x) == wd(d)]


def prior_share(d, t):
    """Mean cumulative arrival share by time t on earlier same-weekday days (both lines)."""
    return pooled_share([x for x in days if x < d and wd(x) == wd(d)], t)


def runout(d, l, batch):
    """Clock time at which a batch of `batch` portions runs out, from the real scan order."""
    s = scans[(d, l)]
    n = int(batch)
    return s[n] if n < len(s) else None


def hhmm(m):
    if m is None:
        return ""
    return f"{int(m // 60):02d}:{int(m % 60):02d}"


def staged(d, l, F, trigger, bf, bl):
    """Record-calibrated first batch plus a late batch started at `trigger`.

    The first batch covers the diners expected before the late batch lands
    (trigger + top-up minutes), from the same-weekday arrival profile, plus a
    buffer bf. At the trigger the count so far is scaled by the weekday share
    seen by then to project the day; the late batch is the projected remainder
    plus a buffer bl. Returns cooked, surplus, residual shortfall (left to the
    ordinary reactive top-up at the crest), late batch, diners who arrive after
    the first batch runs out and before the late batch lands, and the run-out time.
    """
    land = trigger + A["topup_minutes"]
    c_land = prior_share(d, land)
    c_trig = prior_share(d, trigger)
    e = E(d, l)
    b1 = F * c_land * (1 + bf)
    n_trig = sum(1 for x in scans[(d, l)] if x < trigger)
    proj = n_trig / c_trig if c_trig else F
    late = max(proj * (1 + bl) - b1, 0)
    total = b1 + late
    ro1 = runout(d, l, b1)
    pre_gap = 0
    if ro1 is not None and ro1 < land:
        pre_gap = sum(1 for x in scans[(d, l)] if ro1 <= x < land)
    return total, max(total - e, 0), max(e - total, 0), late, pre_gap, ro1


# design grid used in the refinement step: trigger time and buffers
GRID = [(t, bf, bl) for t in (8 * 60 + 45, 9 * 60) for bf in (0.10, 0.20, 0.30, 0.40, 0.50) for bl in (0.10, 0.20)]
REFINED = None  # set after the grid below


test_days = [d for d in days if prior_same_weekday(d, "veg")]  # 8 April onward (23 days)

grid_rows = []
for t, bf, bl in GRID:
    acc = defaultdict(float)
    for d in test_days:
        for l in ["veg", "nonveg"]:
            F = st.mean(prior_same_weekday(d, l))
            total, sur, sh, late, gap, _ = staged(d, l, F, t, bf, bl)
            acc["cooked"] += total; acc["sur"] += sur; acc["sh"] += sh; acc["gap"] += gap
            acc["shdays"] += 1 if sh > 0 else 0
    n = len(test_days)
    grid_rows.append([hhmm(t), bf, bl, round(acc["cooked"] / n), round(acc["sur"] / n), round(acc["sh"] / n, 1),
                      int(acc["shdays"]), round(acc["gap"] / n, 1)])
write("scen_design_grid.csv", ["late_batch_trigger", "first_batch_buffer", "late_batch_buffer", "cooked_per_day",
                               "surplus_per_day", "residual_shortfall_per_day", "line_days_with_shortfall_of_46",
                               "diners_waiting_per_day"], grid_rows)
# refined choice: least surplus among designs that keep diners waiting under 5 a day
ok = [g for g in grid_rows if g[7] < 5]
best = min(ok, key=lambda g: (g[4] + g[5]))
REFINED = {"trigger": int(best[0][:2]) * 60 + int(best[0][3:]), "bf": best[1], "bl": best[2]}

# ---------------------------------------------------------------- backtest of kitchen scenarios
bt = []
agg = defaultdict(lambda: defaultdict(float))
for d in test_days:
    for l in ["veg", "nonveg"]:
        r, e = R[(d, l)], E(d, l)
        F = st.mean(prior_same_weekday(d, l))
        c915 = prior_share(d, T0915)
        c900 = prior_share(d, T0900)
        rec = {}
        # S0 baseline: 70% of registrations, whole batch at the start
        rec["S0"] = A["ratio_kadamba"] * r
        # S5 parameter only: ratio lowered to 50% by decree
        rec["S5"] = 0.50 * r
        # S1 calibrated single batch: record forecast plus buffer
        rec["S1"] = F * (1 + A["buffer"])
        for key, b in rec.items():
            short = max(e - b, 0)
            ro = runout(d, l, b)
            agg[key]["surplus"] += max(b - e, 0)
            agg[key]["short"] += short
            agg[key]["short_days"] += 1 if short > 0 else 0
            agg[key]["cooked"] += b
            agg[key]["crest_short"] += short if (ro is not None and ro >= T0915) else 0
            agg[key]["n"] += 1
            bt.append([d.isoformat(), wd(d), l, key, r, e, round(b), round(max(b - e, 0)), round(short), hhmm(ro)])
        # S1b calibrated + staged late batch (crest-aware, weekday profile), refined design
        total, surplus, short, late, pre_gap, ro1 = staged(d, l, F, **REFINED)
        agg["S1b"]["surplus"] += surplus
        agg["S1b"]["short"] += short
        agg["S1b"]["short_days"] += 1 if short > 0 else 0
        agg["S1b"]["cooked"] += total
        agg["S1b"]["crest_short"] += short
        agg["S1b"]["late_batch"] += late
        agg["S1b"]["pre_gap"] += pre_gap
        agg["S1b"]["n"] += 1
        bt.append([d.isoformat(), wd(d), l, "S1b", r, e, round(total), round(surplus), round(short),
                   hhmm(ro1) + f" (late batch {round(late)})"])
write("scen_backtest_daily.csv",
      ["date", "weekday", "line", "scenario", "registered", "eaten", "cooked", "surplus", "shortfall", "first_batch_runs_out"],
      bt)

n_days = len(test_days)
summary = []
labels = {
    "S0": "Baseline: 70% of registrations, one batch",
    "S5": "Parameter only: ratio lowered to 50%",
    "S1": "Record-calibrated single batch (+10%)",
    "S1b": "Record-calibrated first batch + staged late batch",
}
for key in ["S0", "S5", "S1", "S1b"]:
    g = agg[key]
    days_n = g["n"] / 2
    summary.append([key, labels[key], int(days_n),
                    round(g["cooked"] / days_n), round(g["surplus"] / days_n),
                    round(g["short"] / days_n, 1), int(g["short_days"]), round(g["crest_short"] / days_n, 1),
                    round(g.get("late_batch", 0) / days_n), round(g.get("pre_gap", 0) / days_n, 1)])
write("scen_kitchen_summary.csv",
      ["scenario", "label", "test_days", "cooked_per_day", "surplus_per_day", "shortfall_per_day",
       "line_days_with_shortfall_of_46", "shortfall_after_0915_per_day", "late_batch_per_day",
       "diners_waiting_before_late_batch_per_day"], summary)

# ---------------------------------------------------------------- projection accuracy: flat vs weekday profile
pj = []
err = defaultdict(list)
for d in test_days:
    e = E(d, "veg") + E(d, "nonveg")
    n800 = sum(1 for l in ["veg", "nonveg"] for x in scans[(d, l)] if x < T0800)
    n900 = sum(1 for l in ["veg", "nonveg"] for x in scans[(d, l)] if x < T0900)
    p_flat = n800 / A["flat_share_by_0800"]
    p_800 = n800 / prior_share(d, T0800)
    p_900 = n900 / prior_share(d, T0900)
    for k, p in [("flat_0800", p_flat), ("profile_0800", p_800), ("profile_0900", p_900)]:
        err[k].append((p - e) / e)
    pj.append([d.isoformat(), wd(d), e, n800, round(p_flat), round(p_800), n900, round(p_900)])
write("scen_projection_daily.csv",
      ["date", "weekday", "eaten_total", "scans_by_0800", "flat_projection_from_0800", "profile_projection_from_0800",
       "scans_by_0900", "profile_projection_from_0900"], pj)
proj_sum = []
for k in ["flat_0800", "profile_0800", "profile_0900"]:
    xs = err[k]
    proj_sum.append([k, round(100 * st.mean(xs), 1), round(100 * st.mean(abs(x) for x in xs), 1),
                     round(100 * min(xs), 1), round(100 * max(xs), 1)])
write("scen_projection_summary.csv", ["method", "mean_error_pct", "mean_abs_error_pct", "min_error_pct", "max_error_pct"],
      proj_sum)

# ---------------------------------------------------------------- student side: default and exit scenarios (all April)
tot = {l: {"R": sum(R[(d, l)] for d in days), "E": sum(E(d, l) for d in days)} for l in ["veg", "nonveg"]}
charge_base = sum((tot[l]["R"] - tot[l]["E"]) * RATE[l] for l in tot)
sun = [d for d in days if wd(d) == "Sun"]
stud = []


def month_charge(reg_fn):
    return sum((reg_fn(d, l) - E(d, l)) * RATE[l] for d in days for l in ["veg", "nonveg"])


stud.append(["S0", "Baseline", 0, charge_base, 0])
# S2 Sunday opt-in or confirm, at three opt-in turnouts
for tag, t in [("low", A["optin_turnout_low"]), ("mid", A["optin_turnout_mid"]), ("high", A["optin_turnout_high"])]:
    def reg(d, l, t=t):
        if wd(d) == "Sun":
            return E(d, l) * (1 - A["walkin_share"]) / t
        return R[(d, l)]
    c = month_charge(reg)
    stud.append([f"S2-{tag}", f"Sunday opt-in, opted-in turnout {int(t*100)}%", t, round(c), round(charge_base - c)])
# S3 evening-before skip on every day
for tag, s in [("info", A["skip_share_info_only"]), ("refund-low", A["skip_share_refund_low"]),
               ("refund-high", A["skip_share_refund_high"])]:
    def reg(d, l, s=s):
        return R[(d, l)] - s * (R[(d, l)] - E(d, l))
    c = month_charge(reg)
    stud.append([f"S3-{tag}", f"Evening-before skip, {int(s*100)}% of no-shows skip", s, round(c), round(charge_base - c)])
# S3s evening-before skip on Sundays only (the refined pilot form)
for tag, sh in [("refund-low", A["skip_share_refund_low"]), ("refund-high", A["skip_share_refund_high"])]:
    def reg(d, l, sh=sh):
        if wd(d) == "Sun":
            return R[(d, l)] - sh * (R[(d, l)] - E(d, l))
        return R[(d, l)]
    c = month_charge(reg)
    stud.append([f"S3s-{tag}", f"Sunday-only evening-before skip, {int(sh*100)}% of Sunday no-shows skip", sh, round(c),
                 round(charge_base - c)])
# S6 billing at consumption (held)
stud.append(["S6", "Billing at consumption (held)", 1, 0, charge_base])
write("scen_student_charges.csv", ["scenario", "label", "parameter", "uneaten_charge_rs_april", "change_vs_baseline_rs"],
      stud)

# S4 bound: shorter lead with the cap unchanged
students = round(st.mean(R[(d, "veg")] + R[(d, "nonveg")] for d in days))
cap_total = students * A["cancel_cap"]
noshow_total = sum(tot[l]["R"] - tot[l]["E"] for l in tot)
write("scen_cap_bound.csv", ["registered_students_approx", "max_cancellations_per_month", "no_shows_april",
                             "max_share_of_no_shows_removable_pct"],
      [[students, cap_total, noshow_total, round(100 * cap_total / noshow_total, 1)]])

# ---------------------------------------------------------------- Sunday default change: effect on the kitchen
# Sundays with an earlier Sunday on record (12, 19, 26 April). Eaters are held at their
# recorded level (assumed); bookings shrink to the opted-in count.
sun_t = [d for d in test_days if wd(d) == "Sun"]
sk = []
base_sun = [sum(max(A["ratio_kadamba"] * R[(d, l)] - E(d, l), 0) for l in ["veg", "nonveg"]) for d in sun_t]
sk.append(["baseline", "", "70% of registrations", round(st.mean(base_sun)), 0, 0])
for tag, t in [("low", A["optin_turnout_low"]), ("mid", A["optin_turnout_mid"]), ("high", A["optin_turnout_high"])]:
    for fixed in [True, False]:
        surplus = short = crest = 0
        for d in sun_t:
            for l in ["veg", "nonveg"]:
                e = E(d, l)
                booked = e * (1 - A["walkin_share"]) / t
                if fixed:
                    b = A["ratio_kadamba"] * booked
                    sh = max(e - b, 0)
                    ro = runout(d, l, b)
                    surplus += max(b - e, 0)
                    short += sh
                    crest += sh if (ro is not None and ro >= T0915) else 0
                else:
                    F = st.mean(prior_same_weekday(d, l))
                    total, sur, sh, late, gap, ro1 = staged(d, l, F, **REFINED)
                    surplus += sur
                    short += sh
                    crest += sh
        n = len(sun_t)
        sk.append([tag, t, "70% of the new count" if fixed else "record-calibrated, staged",
                   round(surplus / n), round(short / n, 1), round(crest / n, 1)])
write("scen_sunday_kitchen.csv", ["optin_case", "optin_turnout", "first_batch_rule", "surplus_per_sunday",
                                  "shortfall_per_sunday", "shortfall_after_0915_per_sunday"], sk)

# effective first-batch-plus-late ratio to registrations under the refined design (a Level 12 output)
eff = defaultdict(list)
for d in test_days:
    for l in ["veg", "nonveg"]:
        F = st.mean(prior_same_weekday(d, l))
        total = staged(d, l, F, **REFINED)[0]
        eff[(wd(d), l)].append(total / R[(d, l)])
write("scen_effective_ratio.csv", ["weekday", "line", "cooked_to_registered_pct"],
      [[w, l, round(100 * st.mean(eff[(w, l)]), 1)] for w in WD for l in ["veg", "nonveg"]])

# ---------------------------------------------------------------- Yuktahaar: belief versus register
yk = []
with open(YUK_BF, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["read_confidence"] != "High":
            continue
        reg = int(r["registered_total"])
        ate_reg = int(r["ate_registered_regular"]) + int(r["ate_registered_jain"])
        ate_all = int(r["total_ate_computed"])
        plan50 = 0.50 * reg
        yk.append([r["date"], r["weekday"], reg, ate_reg, ate_all, round(100 * ate_all / reg, 1), round(plan50),
                   round(plan50 - ate_all), reg - ate_reg, (reg - ate_reg) * A["rate_yuk"]])
write("scen_yuktahaar.csv", ["date", "weekday", "registered", "ate_registered", "ate_all", "turnout_pct",
                             "plan_at_believed_50pct", "excess_over_eaten", "uneaten_registrations",
                             "uneaten_charge_rs"], yk)

# ---------------------------------------------------------------- behaviour-over-time projection (recommended bundle)
# Per-day average first-batch surplus for three policy mixes, from the backtest rows,
# then a staged adoption path (assumed; P2 says kitchen change is judged over months).
def mix_surplus(apply):
    tot_s = 0
    for d in test_days:
        for l in ["veg", "nonveg"]:
            if apply(d, l):
                F = st.mean(prior_same_weekday(d, l))
                tot_s += staged(d, l, F, **REFINED)[1]
            else:
                tot_s += max(A["ratio_kadamba"] * R[(d, l)] - E(d, l), 0)
    return tot_s / len(test_days)


s_base = mix_surplus(lambda d, l: False)
s_pilot = mix_surplus(lambda d, l: wd(d) == "Sun" and l == "veg")
s_full = mix_surplus(lambda d, l: True)
weekly_charge = charge_base / 30 * 7
sun_charge_week = st.mean(sum((R[(d, l)] - E(d, l)) * RATE[l] for l in ["veg", "nonveg"]) for d in sun)
mid_sun_charge = sun_charge_week * (1 - A["skip_share_refund_low"])  # Sunday skip pilot, low uptake
bot = []
for wk in range(0, 21, 2):
    if wk <= 4:
        surplus, stage = s_base, "Stage 1: routes and paper record"
    elif wk <= 8:
        surplus = s_base - (0.5 if wk == 6 else 1.0) * (s_base - s_pilot)
        stage = "Stage 2: Sunday veg pilot"
    else:
        f = min(1.0, (wk - 8) / 8)
        surplus = s_pilot - f * (s_pilot - s_full)
        stage = "Stage 3: roll-out"
    sunday_rule = wk >= 14
    charge = weekly_charge - (sun_charge_week - mid_sun_charge if sunday_rule else 0)
    bot.append([wk, round(s_base), round(surplus), round(weekly_charge), round(charge),
                stage + (" + Sunday skip" if sunday_rule else "")])
write("scen_bot_projection.csv", ["week", "baseline_surplus_per_day", "bundle_surplus_per_day",
                                  "baseline_uneaten_charge_rs_per_week", "bundle_uneaten_charge_rs_per_week", "stage"],
      bot)

# ---------------------------------------------------------------- refinement check: cap the cooked total at 1.5 x forecast
cap_s = cap_sh = 0
for d in test_days:
    for l in ["veg", "nonveg"]:
        F = st.mean(prior_same_weekday(d, l))
        total, _, _, late, _, _ = staged(d, l, F, **REFINED)
        b1 = total - late
        t2 = b1 + max(min(total, 1.5 * F) - b1, 0)
        cap_s += max(t2 - E(d, l), 0)
        cap_sh += max(E(d, l) - t2, 0)
late_cap = [round(cap_s / n_days), round(cap_sh / n_days, 1)]
write("scen_late_cap.csv", ["surplus_per_day_with_total_capped_at_1_5x_forecast", "shortfall_per_day"], [late_cap])

# ---------------------------------------------------------------- console summary
print("test days:", n_days, "from", test_days[0])
print("late cap (surplus, short):", late_cap)
for r in summary:
    print(r)
for r in proj_sum:
    print(r)
for r in stud:
    print(r)
print("cap bound:", students, cap_total, noshow_total, round(100 * cap_total / noshow_total, 1))
for r in sk:
    print(r)
print("baseline April uneaten charge Rs", charge_base, "veg", (tot["veg"]["R"] - tot["veg"]["E"]) * RATE["veg"],
      "nonveg", (tot["nonveg"]["R"] - tot["nonveg"]["E"]) * RATE["nonveg"])
print("mix surplus base/pilot/full", round(s_base), round(s_pilot), round(s_full), "REFINED", REFINED)
for k in sorted(eff): print(k, round(100*st.mean(eff[k]),1))
for r in prof_rows:
    print(r)
for r in bot:
    print(r)
print("yuk rows", len(yk), "mean excess", round(st.mean(x[7] for x in yk), 1), "mean charge/day",
      round(st.mean(x[9] for x in yk)))
