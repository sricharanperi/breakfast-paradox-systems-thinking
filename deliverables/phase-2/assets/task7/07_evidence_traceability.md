# Task 7 — Supporting Asset: Evidence Traceability Register

Every systemic finding in `prathyusha_task7.md`, traced back to its evidence sources. Source key as in
`01_iceberg_matrix.md` (S1-S9). ID scheme: E# = event, P# = pattern, ST# = structure, MM# = mental model,
RC# = root cause, T# = tension, F# = finding (main-file Section 15), UC# = unintended consequence.

| Finding ID | Systemic finding | Evidence sources | Confidence | Missing validation |
|------------|-------------------|-------------------|------------|----------------------|
| F1 | Registration-attendance gap is structural, concentrated in breakfast, and known but unactioned at the policy level | E1, E2, E4, ST1, ST3, ST4, RC1, RC4 | 🟡 PLAUSIBLE (gap ✅ confirmed; "unactioned" is inferred from absence of evidence, not confirmed absence) | Direct evidence of whether registration policy has been discussed against the turnout data internally |
| F2 | Billing/registration decoupling (RC1) is a genuine root cause, not merely a symptom label | ST1, E1, S7 (independent cross-corroboration) | ✅ CONFIRMED as structure; 🟡 as full explanatory weight (P5 shows other contributing factors) | Controlled comparison (e.g., per-meal billing pilot) |
| F3 | T-4 procurement lock compounds but does not independently cause the gap | E3, E9, RC2 | ✅ CONFIRMED | Vendor's actual minimum feasible lead time (is 4 days negotiable?) |
| F4 | Fragmented decision rights (RC3) explain why the gap persists despite functioning governance elsewhere (B3) | S1, S5, RC3, T4 | ✅ CONFIRMED (fragmentation); 🟡 (fragmentation as *cause* of inaction, vs. alternative explanations in main file Section 23) | Direct account from Mess Committee/CDS on whether registration-policy redesign has been considered and by whom |
| F5 | Skip Meal (B1) and cross-mess redistribution (B2) are designed balancing mechanisms not confirmed to close in practice | Task 6 loop definitions, no independent evidence found in S1/S2/S5 of their closing links | ❓ UNKNOWN-REQUIRES VALIDATION | Usage-rate data for Skip Meal; evidence of any actual cross-mess redistribution behavior |
| F6 | Menu governance (B3) is the one fully confirmed, closed feedback loop in the system | S5 §3, §7 | ✅ CONFIRMED (mechanism); 🟡 (satisfaction/complaint-reduction closing links) | Direct complaint-volume trend data over rotation cycles |
| F7 | Menu transparency may carry a self-identified demand-concentration risk (R3/T3) | E8 only | ❓ UNKNOWN-REQUIRES VALIDATION | Day-of-week / item-level attendance data cross-referenced against posted menus |
| F8 | Self-reported skip reasons are heterogeneous (habit, quality history, visibility, non-daily schedule conflict), not dominated by a single "early class" narrative | E14, E17, S1's fuller account, partial S2 echoes | 🟡 PLAUSIBLE for the individual respondent; ❓ UNKNOWN-REQUIRES VALIDATION for generalization | Structured skip-reason survey across a larger, representative student sample |
| UC1 | Billing decoupling produces a known, quantifiable but unaddressed procurement-planning distortion | E1, E4, ST1, ST3 | 🟡 PLAUSIBLE | See F1 |
| UC2 | Cancellation cap likely pushes real non-attendance signal into an informationally invisible resale channel | E6, E7 | 🟡 PLAUSIBLE | Resale transaction volume |
| T1 | Administrative simplicity vs. demand-matching accuracy is a genuine, unresolved systemic tension | ST1, E3, E4, S7 | ✅ CONFIRMED | Quantify "who absorbs how much" of the cost |
| — | Data-quality caveat: at least one respondent's self-report is internally contradictory | E5 | ✅ CONFIRMED (as a data-quality fact) | Re-interview or triangulate Skip-2 |

## Notes on Traceability Discipline

- No finding in the main file appears here without at least one source in this table.
- Findings sourced from a single respondent (S1 alone, or one interview in S2) are never phrased in the
  main file as population-level claims — see `08_validation_gaps.md` for the explicit list of what would
  need to change before that phrasing is warranted.
- The fictional Rohan/Adit narrative from the original problem-statement brief does not appear anywhere in
  this table because it is never used as evidence — only as the original framing device, consistent with
  the standing project rule.
