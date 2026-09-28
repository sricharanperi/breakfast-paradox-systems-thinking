# Activity 10 authoring notes (working note, not a submission)

Date: 2026-09-27. Deliverable: `deliverables/phase-3/10-design-test-evaluate-interventions.md` (Deliverables 3, 4, 5).
Assets (all in `deliverables/phase-3/assets/`):
- `scenario_model.py` -> `scen_*.csv` (13 CSVs). Pure stdlib (no pandas on this machine); parses `Observation images/april-data.xlsx` directly with zipfile and asserts every day/line count against `Kadamba_April2026/01_Daily.csv` (all pass). Runtime < 1 s.
- `gen_a10_charts.py` -> `chart-a10-kitchen-scenarios.png`, `chart-a10-sunday-veg-batches.png`, `chart-a10-bot-projection.png` (hand SVG, svgkit `render`, headless Chrome; all three viewed; label collisions fixed on second render).
- `gen_a10_prototype.py` -> `diagram-a10-intervention-prototype.png` (swimlane prototype; viewed twice; "quantity line" label moved off the green learning arrow).

## Sources read
- MASTER_CONTEXT.md: Section 0, Section 7 D-1 to D-62, Section 9, the two 2026-09-27 session entries (via Section 9 summaries).
- Activity 9 deliverable and its authoring notes (authoritative for LP1-LP10, IP1-IP14, P1-P6); 00-phase3-input-brief.md headings (input only).
- Phase 2: 07b (loop IDs/verdicts, Unintended Consequences, What Remains Untested), 08-design-opportunity-statement (full), 09 consolidated (style), 07 chain 6 (student segments).
- Phase 1: 03 power-interest-leverage map (incentives, coalitions, precedent), 01 (posted rates Rs48/66/53, walk-in Rs81/111), 05 respondent table, 02 roles.
- Evidence: Brief #2 (precedence) and Brief #1 (records). CSVs: Kadamba_April2026 01/02/03/05, raw april-data.xlsx, csv/02 breakfast, 05/06 production sheets.
- dataviz skill (palette validated: #8e24aa, #e65100, #1565c0 pass; grey #757575 kept as neutral baseline, fails chroma by design) and systems-visual-design skill.

## Modelling decisions and assumptions (full table in scen_assumptions.csv)
- Out-of-sample backtest: forecast = mean eaten on earlier same-weekday days, so test window is 8-30 April (23 days, 46 line-days). Arrival shares are pooled over earlier same-weekday days (matches Activity 9's pooled by-8:00 figures; card table in the deliverable is pooled over all April).
- Portion = one diner's gram-standard breakfast. No food cost, no kg. Rupees only = posted registered rate x counted uneaten registrations; applying Sept posted rates to April is labelled assumed.
- Outside-diner/staff allowance reported separately (net cooked reduction 214-274/day) because inside-vs-on-top of the 70% is open.
- Refined staged design chosen from `scen_design_grid.csv` by rule: least (surplus + shortfall) with diners waiting < 5/day -> trigger 9:00, first batch = F x share-by-9:15 x 1.5, late = projection(9:00 count / weekday share) x 1.1 - first batch.
- Tested but not adopted: capping the late batch at 1.5 x forecast (saves 16 portions/day, +1.2 short) - mentioned as a pilot option.
- BOT adoption pace is assumed (weeks 5-8 Sunday veg pilot, half adopted at week 6; linear roll-out weeks 9-16). Sunday skip in force from week 14 at 25% uptake.
- Evaluation weights (O1 15, O2 20, O3 15, O4 15, O5 10, O6 5, O7 10, O8 10) and 0-4 scores are the author's judgement; stated with reasons in the deliverable.

## Key numbers (all projected)
- Baseline Kadamba: cooked 759/day, surplus 362/day (veg 288, non-veg 74) on backtest days; Sunday veg 563 cooked vs 190 eaten.
- Ratio 50%: surplus 150, short 4.5/day on 7 line-days (all non-veg).
- Calibrated single batch: surplus 60, short 16.8/day (13.7 after 9:15); 26 Apr veg 45 short at 9:24.
- Refined (calibrated + 9:00 late batch): cooked 485, surplus 91, short 2.6/day, 3.4 diners wait/day; Sunday veg 233 cooked, 45 surplus, 2 short. Effective cooked/registered 29% (Sun veg) to 67% (Fri non-veg).
- Projection MAE: flat from 8:00 34.8% (bias -26.9%); profile at 8:00 28.6%; profile at 9:00 13.4%.
- April uneaten charges Rs10.58 lakh (veg 7.37, non-veg 3.21). Sunday skip w/ refund 25-50%: Rs0.40-0.80 lakh/month; every-day skip: Rs2.65-5.29 lakh; Sunday opt-in: Rs1.23-1.53 lakh; info-only skip: 0; cap bound 26.5% of no-shows.
- Default-off Sunday with 70% ratio kept: 22.7 (72% turnout) to 64.8 (85%) short per Sunday, all after 9:15.
- Yuktahaar (9 legible days): planning at believed 50% = +63 portions/day over eaten; ~Rs10.5k/day uneaten charges.

## Include / exclude decisions
- Seven concepts A-G built from LP1-LP10 (not LP letters). G (ratio cut) kept as an explicit foil to satisfy "obvious and unstable" rule; F (LP10) scored but held (fails gate G3). LP9 appears only as the ledger's eventual receiver and as held in the recommendation.
- Simulation covers A, B+C, D only (the non-held concepts that pass principles); E omitted from simulation as low-stakes. Stakeholders named by role; Raju/Giri and Ajita not named (D-24 conflicts carried as open questions).
- Opt-in (default off) refined into an evening-before skip that removes the charge; opt-in retained as a later option. Rationale: crest shortfall under fixed ratio + walk-in penalty for non-opters.
- Vijayalakshmi/off-site kitchen not modelled (no records; 30-minute top-up would change the late-batch timing).
- "Outstanding Evidence" used as the closing section title per task (Phase 1 used "Outstanding Data Collection").

## House-rule checks
- Em dash count 0; no file paths in prose (only embedded image links); no process narration; projected/simulated labels applied; loop IDs as in 07b; L13 reheating branch kept open; L14 ratchet and L15, L17, L9, L1 kept candidate.

## Diagrams still to build (for the later rebuild)
- An annotated CLD overlay showing where the bundle acts on L10/L11/L12/L13/L14/L17 (optional).
- A Yuktahaar version of the Sunday arrival chart once breakfast scan times exist for Yuktahaar (none now).
- Evaluation scoring could be rendered as a heat table for the PDF; left as a markdown table for now.
- Charts use a white background (svg rect) while svgkit's page background is #fbfbfd; harmless in PDF.

## Unresolved
- All D-24 conflicts (Raju/Giri, Skip Meal vs cooks-on-registrations, 5-10% vs 70%/37%, Ajita vs honorific) remain open and are listed in Outstanding Evidence.
- Late-batch feasibility at 9:00 at Kadamba (labour at crest) is unevidenced; flagged in consequences and outstanding evidence.
- Skip uptake (25-50%) and BOT adoption pace are assumptions; the pilot is designed to measure them.
- MASTER_CONTEXT.md not updated (by instruction); a later step should log D-entries for: concept letters A-G, the refined 9:00 staged design, the evaluation weights, and the Sunday-skip refinement.
- The Activity 9 carried claim about the cap moving 5->10->5 is not used here.
