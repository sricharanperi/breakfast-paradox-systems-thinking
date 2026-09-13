# Task 7 — Supporting Asset: Quantitative Validation

> **Superseded framing note (2026-09-13):** the Iceberg Model (Events/Patterns/Structures/Mental Models) and the feedback-loop analysis were rebuilt from scratch after a correction — see `01_iceberg_matrix.md` and `02_causal_loop_diagram.md` for the current, authoritative versions. The specific facts, quotes, and numbers below remain valid evidence; only the older Events/Patterns/Structures/Mental-Models labels and old loop IDs (R1/B1/B2/R2/B3/R3/B4/R4/R5/R6/B5/B6) elsewhere in this project are superseded by the new L1-L10 loop numbering.

Every number below is labelled DESCRIPTIVE RELATIONSHIP, ASSOCIATION, or CAUSAL HYPOTHESIS. No value is
fabricated or interpolated beyond what a source states; where a number is missing, it is marked as missing
rather than estimated.

## Available Real Numbers

| Metric | Value | Source | Type | Confidence |
|--------|-------|--------|------|------------|
| High-demand item turnout | >90% | CFS Chair (S5 §5) | DESCRIPTIVE RELATIONSHIP (a category-level attendance rate) | ✅ CONFIRMED |
| General category turnout | ~70% | CFS Chair (S5 §5) | DESCRIPTIVE RELATIONSHIP | ✅ CONFIRMED |
| Breakfast-specific turnout | 35-40% | CFS Chair (S5 §5) | DESCRIPTIVE RELATIONSHIP | ✅ CONFIRMED (methodology/scope not fully specified — see `08_validation_gaps.md` P1-1) |
| Respondent's own estimate of breakfast turnout | ~30% | Daily eater-2 (S2) | DESCRIPTIVE RELATIONSHIP, but a personal estimate about others, not a count | 🟡 PLAUSIBLE-PROVISIONAL |
| Vendor procurement lock point | T-4 (4 days before serving) | CFS Chair (S5 §3) | DESCRIPTIVE RELATIONSHIP (a fixed operational parameter) | ✅ CONFIRMED |
| Cancellation cap | 5 per month | Respondent self-report (S1) | DESCRIPTIVE RELATIONSHIP | 🟡 PLAUSIBLE-PROVISIONAL (single-sourced) |
| Kadamba veg breakfast price | ~₹48 | Respondent self-report (S1), echoed by Daily eater-1 (S2) | DESCRIPTIVE RELATIONSHIP | ✅ CONFIRMED (two independent respondents state the same figure) |
| Respondent's 8:30 AM class frequency | Twice per week | Respondent self-report (S1) | DESCRIPTIVE RELATIONSHIP (n=1) | ✅ CONFIRMED for this respondent only |
| Kitchen prep start time | ~5:00 AM (dish-dependent) | S5 §12 (direct observation) | DESCRIPTIVE RELATIONSHIP | ✅ CONFIRMED |
| Kadamba certification | FSSAI "Eat Right Campus" 5-star (Exemplary) | S5 §10 | DESCRIPTIVE RELATIONSHIP (external audit result) | ✅ CONFIRMED |

## What Cannot Be Computed From Available Data (explicitly not fabricated)

- **Ghost-registration rate as a direct measure** (registered-but-didn't-attend, per student, per day) — no
  individual-level dataset exists in this evidence set; only the category-level turnout rate (a proxy) and
  one respondent's self-report exist.
- **Waste volume** (kg/day, ₹ value, or % of prepared food) — waste is tracked categorically (production vs.
  plate, per `03_unintended_consequences.md` UC5) but no volume figure appears anywhere in the sources read.
- **Resale transaction volume** on Mess Cell WhatsApp — mechanism confirmed, scale entirely unmeasured.
- **Skip Meal usage rate** — mechanism confirmed to exist by design (Task 6), no usage count found.
- **Cross-mess comparison of turnout** (Kadamba vs. Bakul/Palash vs. Yuktahar) — the 35-40% figure's scope
  (which mess(es) it covers) is itself a P1 validation gap; no independent per-mess breakdown exists.

## Associations vs. Causation — Explicit Statement

The only relationship in this data that could be mistaken for causal is: *lower turnout is specific to the
breakfast category, not other meal categories, served by the same institutional system.* This is a
DESCRIPTIVE RELATIONSHIP (breakfast turnout is lower) that supports an ASSOCIATION (something about
breakfast specifically, not the registration/billing system in general, differs) but does **not** establish
*which* of the candidate mechanisms (billing decoupling, schedule conflict, food quality history, visibility/
habit, sleep patterns) is doing the causal work, nor their relative weights. Sections 9-10 of the main file
treat RC1 (billing decoupling) as the best-supported *structural* root cause because it is upstream of the
widest set of patterns and is corroborated by an independent second source (S7), not because a causal
estimate has been computed from these numbers — no such estimate is possible with the data in hand.
