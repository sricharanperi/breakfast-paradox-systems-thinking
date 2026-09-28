# Activity 10 revision against Lectures 11-15 (working note, not submitted)

Date: 2026-09-28. File revised: `deliverables/phase-3/10-design-test-evaluate-interventions.md`. Model: `assets/scenario_model.py` (extended; original outputs reproduced unchanged). Charts: `assets/gen_a10_charts.py` (chart 3 rebuilt with ranges and re-sequenced stages; new chart 4 `chart-a10-stress-tests.png`), `assets/gen_a10_prototype.py` (lanes labelled quick fix / fundamental fix; ledger chip "charged"; joint reading chip). All four changed PNGs viewed.

| # | Change item | What was done |
|---|---|---|
| 1 | Re-sequence around shifting the burden | Overview states the quick fix / fundamental fix split. Concept table has a Role column. New Concept H (LP11, LP12). Recommendation retitled; stage table splits fundamental (fixed dates: joint reading week 4, Sunday skip proposal week 6) from quick fix. New "Architecture Path" table DP1-DP4 with rules and fallbacks (Sunday skip -> every-day skip at week 14 rule -> default matched to intent -> billing/payment basis) |
| 2 | Ledger charge line | Prototype A gains "Charged, not eaten" column (Sunday 19 April: ₹30,624 veg, ₹10,428 non-veg) and a foot rule that the weekly charge total sits beside surplus; also run-out days marked as censored, hand-logged scans on own line |
| 3 | Co-design and user testing | New "Co-design and User Testing (Planned)" subsection: portal wording (students), plan card and 9:00 rule (supervisor, cook), ledger (Yuktāhār PMs and keeper), export effort (CDS). Each with what it checks and result that changes the design. "Planned" label added to vocabulary. Nothing presented as done |
| 4 | Evaluation framework | Gate G4 added (quick fix paired with fundamental fix on an independent date). O9 desirability (10). Quality 5 -> 10; O2 20 -> 15; O7 and O8 10 -> 5 each; justified in text. Result measures vs process checks separated (framework text and pilot table). All concepts rescored, with first-draft scores shown |
| 5 | Policy resistance | New table "How the System Might Adapt: Policy Resistance", 10 rows, each with loop, likelihood (assumed), early warning, mitigation |
| 6 | Scenario model | Sensitivity (ratio 60-80, crest -5..+10, uptake 10-75, skip-then-eat 0-25%) and stress (exam unwarned/warned, favourite item, eaters ±10%, heavier crest, gas shortage 30 min, failed late batch). New Scenario 6 with tables and chart; BOT became Scenario 7 with ranges. "Cannot cause" replaced by "unlikely to ... provided uptake stays below ..." with a threshold table. No-adaptation assumption tested at ±10% and ±25%. Censored-demand limitation stated, with ledger rule and mitigation. Theory of change now in ranges. New Scenario 8: scenario × indicator matrix (6 scenarios × 11 indicators), figures projected where modelled, directions otherwise |
| 7 | Multi-level table | "Interventions Across the Iceberg" in Deliverable 5: events, patterns, structures, mental models, each with action and indicator |
| 8 | Monitoring | "Monitoring Beyond the Pilot": owner (CDS office by role plus operator data roles; LP9 when head of CDS known), handover weeks 16-20, team exit test, comparison lines/days; archetype indicator table; explicit better-before-worse / worse-before-better paragraph |
| 9 | Convening | Joint convening row in pilot design (week 4, repeated week 12); simulation conclusion argues for a joint reading rather than separate proposals |
| 10 | Blame framing | "one coalition and one blocker" paragraph removed; new table of each actor's rational position and what would change its incentive. "Resists" reworded |
| 11 | Labels, D-45, D5 | Simulated / projected / planned labels kept; absorbers kept (G1, allowance); pilot success/stop criteria, BOT table, theory of change, Who Must Act, Before and After updated |
| 12 | Charts | Chart 1 and 2 re-rendered (unchanged numbers). Chart 3 with bands, stage markers (joint reading, skip proposed, Sunday skip in force, decision point) and conditional every-day band. Chart 4 new (stress tests). Prototype diagram relabelled |

## New scores (weights O1 15, O2 15, O3 15, O4 15, O5 10, O6 10, O9 10, O7 5, O8 5)

A 68 (was 74); H 65 (new); C 63, fails G4 alone (64); F 63, fails G3 (61); D skip 60 (59); E 60 (61); B 58, fails G4 alone (65); D every-day 50 (new); D opt-in 50 (51); G 48, fails G1 (58); first-draft bundle 79, fails G4 (80); re-sequenced bundle 79, passes. Ranking changed (B 2nd -> 7th, H new 2nd). Recommendation: same parts plus H, re-sequenced; the weighted score cannot see order, so G4 decides between the two bundles.

## Model outputs (all projected)

- Base results reproduced: baseline 759 cooked / 362 surplus; G 150 surplus, 4.5 short; B alone 60 / 16.8; refined 485 / 91 / 2.6 / 3.4 waiting.
- Ratio 60/70/80: baseline surplus 254/362/471; cooked reduction 165/274/382; net of 0-60 allowance 105-382; Sunday veg batch/eaten 2.5/3.0/3.4.
- Crest -5/0/+5/+10: surplus 120/91/69/52; short 0.5/2.6/7.7/12.6; waiting 5.7/3.4/1.1/0.3.
- Stress: exam unwarned 123 surplus, 0 short; warned 67, 2.1; favourite +25% 89, 9.1 short, 14.2 waiting; eaters -10% 100, 1.4; +10% 89, 5.6; gas 91, 2.6 short, 25.3 waiting; failed late batch 33, 43.6 short, 32.5 waiting.
- Safe skip uptake with fixed ratio (min over April days): 70% ratio non-veg Sundays 67.2%, all days 38.0% (7 of 30 days short at 50%); 60% ratio non-veg Sundays 49.0%.
- Skip-then-eat: Sundays none short at 25-50% uptake with up to 25% still eating; every day at 50% uptake 1.4 / 3.0 / 8.9 short a day at 0/10/25%.
- Uptake 10/25/50/75%: Sunday ₹4,010/10,025/20,050/30,075 a week; every day ₹24,692/61,729/1.23 lakh/1.85 lakh; fewer registered plates Sunday 78/194/389/583, every day 472/1,180/2,359/3,539 a week.
- Share of scans at/after 9:30: 9.2%.
- BOT: bundle surplus week 16-20 91 (69-120); charges ₹2.37 lakh (2.27-2.37) from week 10; conditional every-day ₹1.23-1.85 lakh from week 16.
- New CSVs: scen_sens_ratio, scen_sens_crest, scen_stress, scen_skip_threshold, scen_skip_gaming, scen_skip_uptake, scen_monitor_anchors; scen_bot_projection has new band columns.

## Unresolved issues

- Stress shocks (25%, 10 points, 30 minutes) are assumed magnitudes; their frequency is unknown (added to Outstanding Evidence).
- Handover owner is "CDS office by role" because the head of CDS is unresolved (D-24).
- The architecture-path thresholds (25% uptake, 10 short, "more than half of no-shows for a term") are the team's judgement.
- O9 desirability rests on simulated responses until the planned tests run; the text says so.
- Concept H is new (not in MASTER_CONTEXT D-65's A-G list); D-65 and D-67/D-68 describe the old sequencing and weights and would need updating by whoever maintains MASTER_CONTEXT (not edited per instructions).
- Em dash count 0; en dash count 0; no books, authors or lectures named; no file paths in prose.
