# Activity 9 authoring notes (working note, not a submission)

Date: 2026-09-27. Deliverable: `deliverables/phase-3/09-leverage-point-intervention-map-and-design-principles.md`. Diagram: `deliverables/phase-3/assets/gen_leverage_map.py` -> `diagram-a9-leverage-intervention-map.png` (rendered via headless Chrome, viewed three times; band labels drawn last to knock out crossing arrows; callouts moved off the dashed routes).

## Sources used
- MASTER_CONTEXT.md: Section 0, Section 7 (D-2, D-5, D-7, D-12, D-18, D-20, D-24, D-27, D-35, D-40, D-42, D-43, D-45/49/57, D-46, D-47, D-48 to D-62), Section 9, the two 2026-09-27 session entries.
- deliverables/phase-3/00-phase3-input-brief.md (pass 2), used as input and re-checked against Phase 2.
- Phase 2: 07b (loop IDs and verdicts, authoritative), 08-reframed, 08-DOS, 09 consolidated, 07 (structural causes, power, workarounds), 06 (service timeline, safety checkpoints), 08-evidence register headings.
- Phase 1: 03 power-interest-leverage map (authority table, information flows, leverage analysis); 04 and 05 headings for house style.
- Evidence: 2026-09-27 team field account brief (precedence), 2026-09-26 mess operations brief, Kadamba_April2026 CSVs 00/01/02/03/05, and the raw april-data.xlsx (parsed with zipfile, read-only) for new weekday arrival shares.
- Framework PDF Phase 3/4 table; systems-design-toolkit SKILL.md (leverage hierarchy); systems-visual-design SKILL.md + svgkit.py.

## New numbers computed this pass (all from the April export, confirmed records; interpretation candidate)
- Share of a day's scans seen before 8:00 by weekday: Mon 17.7, Tue 17.0, Wed 22.5, Thu 21.9, Fri 13.9, Sat 15.8, Sun 13.5; all days 18.0 (includes 2.7 before 7:30).
- Share after 9:15 (mean of daily pct_after_0915): Sun 45.9, Sat 38.0, Fri 37.8, Mon 35.5, Thu 35.5, Tue 31.6, Wed 31.6; daily range 27.0 to 51.3.
- 70% batch / eaten by weekday: veg Sun 3.07x, Tue 1.90x; non-veg Sun 1.70x.
- "Single factor under-reads Sunday by about a quarter, over-reads Wednesday by about a quarter" = 13.5/18.0 and 22.5/18.0.

## Include / exclude decisions (input brief -> deliverable)
| Brief item | Decision | Reason |
|---|---|---|
| LP-A upward route | LP1 | Enabling lever; merged with LP-H |
| LP-H calendar feed | Folded into LP1 (downward route) | Same principle (route, don't measure), same level; too thin alone |
| LP-B default and exit | LP2 | Deepest ungated lever |
| LP-N operator goal | LP3 | Level 3; natural comparison evidence |
| LP-J practice transfer | LP4 (kept separate from LP3) | Different level (4) and different power holder; paired in ranking |
| LP-E calibration + LP-F learning record | Merged as LP5 | Same intervention point (T-1 plan) and same loop (L11); F alone is the record that makes E a loop |
| LP-I crest-aware top-up | LP6 | Strengthened with new weekday profile finding |
| LP-K cost trigger + LP-O oversight line | Merged as LP7 | O is the carrier of K; separate LP-O had no independent decision |
| LP-G menu voice | LP8 | Only lever on L16 |
| LP-L named owner | LP9, held | DOS 4.3 intervention point must appear; held on CDS head identity |
| LP-C billing + LP-D vendor basis | Merged as LP10, held | Same gating fact (plate basis, D-54); needed for Incentives subsection |
| LP-M institutional paradigm | Not a separate LP | Cannot be pulled directly; carried in the ranking closing paragraph and P6 |
| "Considered and down-ranked" list (ratio as number, cap count, class start, nudges, Skip Meal refund, software-first, waste-exit count, restricting absorbers) | Not listed as dropped candidates | Parameter tweaks appear only as outputs/supporting moves with reasons (LP5, LP2); others appear only as "Rules out" lines of principles P1, P3, P4, P5; waste-exit count kept as IP12 (bin line on the LP1 view) |
| IP14 display plate | Dropped | Cannot inform a skip decision; weak |
| IP15 billing/payment | Kept as a row outside the daily chain (LP10 held) | |
| Six principles P1-P6 | Kept, reworded, each with statement/rationale/rules out | P4 absorbs the scoping rule (hall, weekday, line) |
| Daily field-log templates, question lists, decision triggers (brief s5.2, 5.3) | Not in deliverable | Process material; Outstanding Evidence states the questions as open instead |

## Added methods (each adds a finding)
- Depth vs feasibility ranking table + reasoning.
- Absorber check matrix: only LP5 and LP6 touch a protective absorber; both keep it.
- Stakeholder impact check: Kadamba operator is both the likeliest loser (LP2) and the most needed (LP5), which justifies LP3/LP4 before LP5 at Kadamba.
- "Sunday breakfast: where three levers meet" (new records-based finding).

## House-rule compliance
- Headers follow framework wording and order; "Deliverable 1" and "Deliverable 2" labelled sections. Closing section titled "Outstanding Evidence" per the task instruction (Phase 1 used "Outstanding Data Collection", D-12; rename if the team prefers consistency). A "Key Findings" section precedes it, matching Phase 1 house style.
- Em dash count 0; en dash 0; no file paths other than the embedded image link; people named by role only (Raju/Giri and Ajita not named).
- Loop IDs and verdicts as in 07b; no chain promoted to a loop (reheating branch stays an open branch of L13; L14 ratchet stays candidate).
- Conflicts carried open: CDS head (two names), Skip Meal vs cooks-on-registrations, 5-10% vs 70%/37%, Wastage Book keeper vs honorific.

## Unresolved / for the next step
- The map image title bar and the caption both use "Leverage-Point / System Intervention Map"; the markdown caption is in italics under the image (Phase 2 used alt text only). Adjust in the LaTeX pass if needed.
- MASTER_CONTEXT.md not updated (by instruction); D-54/D-61 should record the final LP1-LP10 renumbering (brief letters -> numbers mapping above).
- The input brief still uses LP-A..LP-O letters; Activity 10 should use LP1-LP10.
- The "cap moved 5 -> 10 -> 5" claim comes from 08-DOS; its original source (the December 2024 tightening) was flagged single-sourced in D-29. Stated as in 08-DOS without a tag.
