# Rebuild Plan: Phase 1 and Phase 2 submissions from the revised markdown

**Status:** working document, not a submission (D-35, D-42, D-52). **Checked on 2026-10-06: nothing in this plan has been executed yet.** Read Section 9 first; it lists what changed after Sections 1 to 8 were written and the decisions to take before starting. The repo-root `README.md` is the short step-by-step guide to running this plan. Written 2026-09-27 after the two revision passes (pass 1 on Evidence Brief #1, the mess operations brief; pass 2 on Evidence Brief #2, the team field account). Paths are relative to the repo root unless stated otherwise.

**What this plan is for.** Every Phase 1 and Phase 2 markdown file has been revised twice. No docx, PDF, LaTeX report, bundle or diagram has been regenerated since. This plan lists everything that must be regenerated, what each diagram must now show, the exact commands, the checks to run on the rendered output, and the data questions worth settling first. The goal is that whoever runs the rebuild does not have to re-read the audits or re-derive any content.

**Sources this plan was built from:** `MASTER_CONTEXT.md` Sections 1, 3, 5 (5.4, 5.5, 5.6, 5.7), 7 (D-13, D-20, D-35, D-42, D-43, D-44, D-47, D-49 to D-54) and 9; `.claude/skills/systems-visual-design/SKILL.md`; the pass-1 audits `deliverables/phase-*/revisions/2026-09-27_*-gap-audit.md`; the pass-2 audits `deliverables/phase-*/revisions/2026-09-27-pass2_*-gap-audit.md`; the diagram notes the pass-2 editors reported; `research/primary-research/2026-09-27_team-field-account-evidence-brief.md` (Brief #2, which takes precedence over Brief #1 where they conflict); the image references and diagram caveat sentences found in each revised markdown.

**Ground rules for the rebuild (standing decisions):**
- The markdown is the source of truth. Do not hand-edit a docx or PDF. Any content fix goes into the `.md` and is re-rendered.
- Diagrams are hand-composed SVG via the `systems-visual-design` skill (`svgkit.py`), rasterised with headless Chrome (D-20). No Mermaid. The Phase 1 `.mmd` files are retired as sources; keep them only as a record of the old content.
- A redraw keeps its existing filename, so the markdown image reference does not change (only the caption may). A genuinely new diagram gets a new number.
- Every diagram label uses D-51 loop IDs (L1 to L17 plus L3b), the D-35 confidence vocabulary (confirmed / single-sourced / candidate / assumed; "observer-verified" as a qualifier for Brief #2 Kadamba statements), the spelling "Yuktāhār" and "Palash" (D-52), no em dashes in labels (D-43), and dashed grey styling for anything unconfirmed or conflicting (D-24).
- Evidence corrections from Brief #2 that must appear in every diagram that touches them: Kadamba staff meals "20 to 30" is replaced by **about 30 portions for 30 to 50 outside diners plus about half of Kadamba's staff**; the Kadamba kilogram waste figures are **withdrawn** (use "about 5 to 10% daily, base unstated"); registration is an **automatic default** with a capped exit (**5 cancellations per meal type per month, at least 4 days ahead, no way to remove the charge beyond that**), not "weekly blocks"; composting is **not** an absorber (D-49), the bin and garbage contractor are the exit; the Kadamba vendor is **Prism**; Yuktāhār's vendor is **ABC Hospitality Services** with **two project managers**; the CDS head is **open (Raju in Brief #2 vs Giri as CDS Chair earlier)**; the Skip Meal to kitchen link is **conflicting**, not confirmed.

---

## 1. Status table

"Current" means revised twice (pass 1 and pass 2) as of 2026-09-27 16:40 to 17:06. "Stale" means built before 2026-09-27 and does not match the markdown.

### 1.1 Phase 1 (`deliverables/phase-1/`)

| # | Deliverable | Markdown (source) | Docx | PDF | Embedded diagrams (all in `assets/`) | Regenerate | Order |
|---|---|---|---|---|---|---|---|
| 1 | System Context Brief | `01-system-context-brief.md` (current) | `System Context Brief.docx` (stale, 6 Sep) | `System Context Brief.pdf` (stale, 7pp) | diagram1-system-boundary, diagram2-context-map | 2 redraws, docx, PDF | P1-a |
| 2 | Stakeholder Map | `02-stakeholder-map.md` (current) | `Stakeholder Map.docx` (stale) | `Stakeholder Map.pdf` (stale, 10pp) | diagram3, diagram4, diagram5 | 3 redraws, docx, PDF | P1-b |
| 3 | Power-Interest / Leverage Map and Power Analysis Brief | `03-power-interest-leverage-map.md` (current) | `Power-Interest Leverage Map.docx` (stale) | `Power-Interest Leverage Map.pdf` (stale, 12pp) | d13, d12, d14; new d23 | 3 redraws, 1 new, docx, PDF | P1-c |
| 4 | Process Trace | `04-process-trace.md` (current) | `Process Trace.docx` (stale) | `Process Trace.pdf` (stale, 11pp) | diagram6, diagram7, d9; new d15, d16, d17 | 3 redraws, 3 new, docx, PDF | P1-d |
| 5 | System Timeline / BOT Map | `05-system-timeline-bot-map.md` (current) | `System Timeline BOT Map.docx` (stale) | `System Timeline BOT Map.pdf` (stale, 8pp) | diagram8, diagram9, d10, d11; new d18 to d22 | 4 redraws, 5 new, docx, PDF | P1-e |
| - | Phase 1 Consolidated Report | `00-consolidated-phase1-report.md` (current) | `Phase 1 Consolidated Report.docx` (stale) | `Phase 1 Consolidated Report.pdf` (stale, 8pp) | diagram2, diagram3, d13, diagram7, diagram8, d10 (all reused) | docx, PDF only (after P1-a to P1-e) | P1-f |
| - | Bundle | none | none | `Invictus_Phase1.pdf` (stale, 42pp; concat of #1 to #5 only, no consolidated report, no cover) | none | re-concatenate | P1-g |
| - | LaTeX report | `report/main.tex` (stale: predates every 2026-09-27 finding, 210 LaTeX `---` em dashes, `\confirmed`/`\hypo` tag macros, own figure copies in `report/figures/`) | none | `report/main.pdf` (stale, 35pp, unscrubbed metadata: Creator "LaTeX with hyperref", Producer "xdvipdfmx") | uses `report/figures/d1` to `d14` (old Mermaid copies) | rewrite (Section 4), recompile, scrub | P1-h |

### 1.2 Phase 2 (`deliverables/phase-2/`)

| # | Deliverable | Markdown (source) | Docx | PDF | Embedded diagrams (all in `assets/`) | Regenerate | Order |
|---|---|---|---|---|---|---|---|
| 1 | System Map | `06-system-map.md` (current) | `System Map.docx` (stale, 14 Sep) | `System Map.pdf` (stale, 17pp) | diagram1, diagram13, diagram8, diagram12, diagram9, loop images (see 2.3); new diagram32, diagram33, d17 copy, L11 to L14 images | 5 edits, relabels, 2+ new, 3 caveat sentences removed, docx, PDF | P2-a |
| 2 | Causal Loop and Feedback Analysis | `07b-causal-loop-feedback-analysis.md` (current; authoritative loop scheme, D-51) | `Causal Loop and Feedback Analysis.docx` (stale) | `Causal Loop and Feedback Analysis.pdf` (stale, 10pp) | diagram24, diagram26, diagram25, diagram28, diagram27; new diagram34 to diagram37 | 4 edits, 4 new, docx, PDF | P2-b (before P2-a, since 06 reuses its loop images) |
| 3 | Systemic Problem Analysis | `07-systemic-problem-analysis.md` (current; seven chains) | `Systemic Problem Analysis.docx` (stale) | `Systemic Problem Analysis.pdf` (stale, 13pp) | diagram18 to diagram23; new diagram39 (Chain 7) | 6 edits, 1 new, docx, PDF | P2-c |
| 4 | Reframed Systemic Problem Statement | `08-reframed-problem-statement.md` (current) | `Reframed Systemic Problem Statement.docx` (stale) | `Reframed Systemic Problem Statement.pdf` (stale, 6pp) | diagram30, diagram31 | 2 edits, docx, PDF | P2-d |
| 5 | Design Opportunity Statement | `08-design-opportunity-statement.md` (current) | `Design Opportunity Statement.docx` (stale) | `Design Opportunity Statement.pdf` (stale, 4pp) | none | docx, PDF (optional: embed d23 in 4.3, see DW-P2-19) | P2-e |
| 8e | Evidence and Validation Register (supporting, not one of the five) | `08-evidence-and-validation-register.md` (current) | `Evidence and Validation Register.docx` (stale) | `Evidence and Validation Register.pdf` (stale, 6pp) | diagram29 | 1 edit, docx, PDF | P2-f |
| - | Phase 2 Consolidated Report | `09-phase2-consolidated-report.md` (current) | `Phase 2 Consolidated Report.docx` (stale) | `Phase 2 Consolidated Report.pdf` (stale, 6pp) | diagram1 (reused); caveat sentence at line 22 to remove; optional diagram33 | docx, PDF | P2-g |
| - | Cover page | `assets/cover-page.md` (current, no content change needed) | none | rendered into the bundles | none | re-render | P2-h |
| - | Bundle | none | none | `Invictus_Phase2.pdf` (stale, 51pp = cover 1 + System Map 17 + CLFA 10 + SPA 13 + Reframed 6 + DOS 4; the register is **not** in it) | none | re-concatenate | P2-h |
| - | Condensed bundle | none | none | `Invictus_Phase2_Condensed.pdf` (stale, 7pp = cover 1 + consolidated report 6) | none | re-concatenate | P2-h |
| - | LaTeX report | `report/phase2.tex` (stale: composting 6 mentions, four-day lock framing 7, no L-IDs, no operators, uses retired diagram15/16/17) | none | `report/phase2.pdf` (stale, 18pp) | via `\graphicspath{{../deliverables/phase-2/assets/}}` | rewrite (Section 4), recompile, scrub | P2-i |

### 1.3 Overall order

0. Settle or explicitly park the open data questions in Section 5, and declare an **evidence freeze** (D-53 says new batches arrive daily; a rebuild started mid-batch will be redone). Record the freeze date in `MASTER_CONTEXT.md`.
1. Housekeeping (Section 3.1).
2. Shared diagram infrastructure: new icons, Phase 1 generator scripts (Section 2.1).
3. Phase 1 diagrams, then Phase 1 markdown touch-ups (image references, captions), then P1-a to P1-g, then P1-h.
4. Phase 2 diagrams in the order 07b, 06, 07, 08r, 08e, then Phase 2 markdown touch-ups, then P2-b, P2-a, P2-c, P2-d, P2-e, P2-f, P2-g, P2-h, then P2-i.
5. Compliance checks (Section 3.5) on every rendered file, then a page-by-page visual read (MASTER_CONTEXT 5.5).
6. `MASTER_CONTEXT.md` session entry, Section 1 status tables flipped to current, Section 9 render items closed. Commit only when the user asks (D-14: no Claude attribution in commits unless asked).

Phase 1 goes before Phase 2 because several Phase 2 diagrams reuse Phase 1 content (food-safety sequence, Kadamba command chain, arrival curve) and D-53 fixes that order.

---

## 2. Consolidated diagram work list

Deduplicated across pass 1 (MASTER_CONTEXT Section 9 and the `2026-09-27_*` audits) and pass 2 (the `2026-09-27-pass2_*` audits and the editors' diagram notes). Where pass 2 supersedes pass 1 (for example "20 to 30 staff" or the kilogram figures), only the pass-2 content is listed.

Action codes: **keep** (no change), **edit** (existing SVG generator, change content), **redraw** (Mermaid or unknown source, build a new SVG generator reproducing and correcting the content), **new** (new diagram and generator), **retire** (stop embedding).

### 2.1 Shared infrastructure (do first)

- **Skill path.** Import from `.claude/skills/systems-visual-design/` (every existing `gen_*.py` hardcodes it). `.agents/skills/systems-visual-design/` is an untracked mirror with "Codex" wording substitutions and identical `svgkit.py`/`icon-defs.svg`; do not edit it in parallel. Decide before committing whether to keep or delete it.
- **New icons** to add to `icon-defs.svg` (same `viewBox="-16 -16 32 32"` convention): `ic-book` (registers), `ic-thermometer` (temperature checks), `ic-truck` (off-site transport, suppliers), `ic-bin` (waste exit), `ic-door` (back door, 9:30 close), `ic-scale` (gram standards, weighing), `ic-plate` (wrapped display plate), `ic-flask` (72 h sample), `ic-flame` (reheat, LPG), `ic-chart` (wastage board). Check each at chip scale before use.
- **Known `svgkit` sharp edge:** `chip()` draws line 2 in dark grey regardless of `text_color`; use light fills for two-line chips (MASTER_CONTEXT 5.6).
- **Phase 1 has no generators at all.** Create them in `deliverables/phase-1/assets/`, grouped by deliverable so one script re-renders one PDF's worth of figures:
  - `gen_p1_context.py`: diagram1, diagram2
  - `gen_p1_stakeholders.py`: diagram3, diagram4, diagram5
  - `gen_p1_power.py`: d12, d13, d14, d23
  - `gen_p1_process.py`: diagram6, diagram7, d9, d15, d16, d17 (d17 is also written to `deliverables/phase-2/assets/`)
  - `gen_p1_charts.py`: diagram8, d18, d19, d20 (data-driven, see below)
  - `gen_p1_timelines.py`: diagram9, d21, d22
  - `gen_p1_loops.py`: d10, d11 (copy `loop_diagram()` from `deliverables/phase-2/assets/gen_clds.py`)
- **Data-driven charts** (diagram8, d18, d19, d20) must read numbers from CSV, never hardcode them. Inputs live under `Observation images/Extracted Data/`, which is gitignored:
  - `Kadamba_April2026/01_Daily.csv` (per day: veg/non-veg/total registered and availed, availed %)
  - `Kadamba_April2026/02_By_Weekday.csv` (weekday averages)
  - `Kadamba_April2026/03_Arrival_15min.csv` (15-minute slots, % of scans, cumulative %)
  - `Kadamba_April2026/04_Arrival_per_minute_0900_0945.csv` (per-minute crest)
  - `Kadamba_April2026/05_Service_Window_Daily.csv` (first/median/last scan per day)
  - `csv/01_Attendance_Lunch.csv`, `csv/02_Attendance_Breakfast.csv` (Yuktāhār September register; use `total_ate_computed` and `attendance_pct_computed`, and mark the 7 partly hidden breakfast rows)
  
  **Team decision needed:** copy these aggregate CSVs (no student IDs) into `deliverables/phase-1/assets/data/` so the charts are reproducible from git, or keep reading from the gitignored folder and accept that only this machine can rebuild them.
- Every chart and diagram: render, then read the PNG (skill step 3). Every CLD: loop actually closes, every link has a polarity sign, dashed links for designed-but-not-firing or unconfirmed.

### 2.2 Phase 1 diagrams (`deliverables/phase-1/assets/`)

| ID | File | Embedded in | Action | Exact content changes | Generator |
|---|---|---|---|---|---|
| DW-P1-01 | `diagram1-system-boundary.png` | 01 | redraw (Mermaid, 5 Sep) | Three rings. **Inside:** registration/billing platform and scan; the four halls; the Prism kitchen at Kadamba; the ABC Hospitality Services kitchen at Yuktāhār; the off-site kitchen plus transport link serving Bakul/Palash (Vijayalakshmi Caterers a candidate operator, dashed); day-before planning, top-up, reuse and disposal inside the kitchen layer; governance layer. **On the boundary ring:** suppliers in three tiers (a week, 2 to 3 days, the day before); garbage contractor (bin exit, no composting at Kadamba, single-sourced); facility team and weekly QC; CDS site team / complaint channel; tender/contract; non-student diners (30 to 50 outside people plus about half of Kadamba's staff). **Outside:** class schedule / academic calendar, alternative venues, Mess Cell. Lunch/dinner shown outside as the comparison. | new `gen_p1_context.py` |
| DW-P1-02 | `diagram2-context-map.png` | 01, 00 | redraw (P0) | Replace the Mess Office "ordering"/"orders" labels with "administers platform; operators read registration count". Delete any "T-4 food order" and "Bakul cooked at Palash" edges. Replace the single "Mess Vendors" box with named operators (Prism at Kadamba, ABC Hospitality Services at Yuktāhār, off-site operator for Bakul/Palash, Vijayalakshmi candidate). Add the chain CFS -> CDS -> Prism -> operations manager -> manager -> supervisor with the CDS head marked open (dashed label "Raju or Giri, unresolved"). Show extra diners as a food sink off the Kadamba kitchen. Add the garbage-contractor exit. | `gen_p1_context.py` |
| DW-P1-03 | `diagram3-stakeholder-map.png` | 02, 00 | redraw (Mermaid) | Add operator cluster: Prism (Kadamba) and ABC Hospitality Services (Yuktāhār) as operator nodes with site management; off-site operator (candidate Vijayalakshmi). External ring next to operators: "Non-student diners fed at Kadamba". Add suppliers, garbage contractor, CDS site team, facility tasting team (identity flagged, dashed), event and exam organisers. Relabel "Mess Office" as "Mess Office (candidate: CDS)" per D-24. 24 stakeholders total, matching 02's table. | new `gen_p1_stakeholders.py` |
| DW-P1-04 | `diagram4-relationship-network.png` | 02 | redraw (Mermaid) | Replace "Vendor: South Indian Kadamba" / "Vendor: Jain Yuktahar". Draw the Kadamba chain CFS -> CDS (Raju, flagged vs Giri) -> Prism -> operations manager -> manager -> supervisor -> staff. Draw Yuktāhār as a flat peer ring of books and keepers: two project managers, the mess in-charge (Ajita), the cross-checker (Bhavani), coordinator, store function, tasting/cutting/cleaning teams (see Q9 on names). Add the surplus-absorber node (outside diners, half the staff) and a supplier/waste cluster (three supply tiers, garbage contractor). Five clusters, 24 stakeholders. | `gen_p1_stakeholders.py` |
| DW-P1-05 | `diagram5-onion-proximity.png` | 02 | redraw (Mermaid) | Replace "floor manager" with the in-service deciders: Kadamba supervisor; Yuktāhār coordinator and kitchen team. Place non-student diners near the operators ring. Operators move inward (they touch every breakfast). | `gen_p1_stakeholders.py` |
| DW-P1-06 | `d12-leverage-quadrant.png` | 03 (report fig) | redraw (Mermaid source in `report/figures/`) | Operators: high leverage over waste, local not rule-making power. Show the Kadamba supervisor as holder of the in-service top-up lever and Yuktāhār's collective daily meeting as its equivalent. Add facility team / QC as high power, zero leverage over waste (optional but recommended). Keep the "ordinal placement" note in the caption, not in the image. | new `gen_p1_power.py` |
| DW-P1-07 | `d13-power-interest-v2.png` | 03, 00 | redraw | Split "Mess operators" into Kadamba/Prism and Yuktāhār/ABC if space allows. Add CFS, CDS head (label open), facility team/QC (high power over safety, none over quantity), outside diners and staff (low power, low voice). Anything not placed must match the text placements in 03 line 232 (event/exam organisers etc.). | `gen_p1_power.py` |
| DW-P1-08 | `d14-power-flow-network.png` | 03 | redraw | Add the Kadamba chain CFS -> CDS (head open, dashed label) -> Prism -> operations manager -> manager -> supervisor -> service staff. Add facility team / QC -> kitchen arrow labelled "safety and taste only". Add Yuktāhār's book system as a node with **no outbound arrow** to any rule owner, and CDS scan records likewise (the measured-but-unrouted finding, D-50). Outside diners and Kadamba staff as absorber nodes. Operators: high information, authority over quantity only. | `gen_p1_power.py` |
| DW-P1-09 | `d23-kadamba-command-chain.png` | 03 (Operator-side authority, after the chain paragraph) | new | Vertical chain CFS -> CDS (head: Raju per team account; CDS Chair Giri per CFS interview; dashed "unresolved") -> Prism (tender-bid vendor running all operations) -> operations manager -> manager -> supervisor (real-time quantity decider, gram standards) -> service staff. Side branch: facility tasting team + 2 Prism tasters, weekly QC, remit "safety and taste, not quantity". Contrast inset: Yuktāhār flat, two PMs, peer cross-checking, no hierarchy. | `gen_p1_power.py` |
| DW-P1-10 | `diagram6-monthly-cycle.png` | 04 | redraw (Mermaid) | Registration path becomes: automatic registration including holidays -> 5 cancellations per meal type per month, at least 4 days ahead -> beyond that no way to nullify the charge; Skip Meal marks "designed to reduce kitchen prep, conflicting evidence" (dashed); billing at the booking; monthly bill. Remove "weekly blocks". | new `gen_p1_process.py` |
| DW-P1-11 | `diagram7-daily-cycle.png` | 04, 00 | redraw (Mermaid) | Keep student-only (04 now says the diagram shows the student side and the operator side follows in a table and d15/d16). Align times with records: first scans about 7:28, median about 9:00, 26.5% of scans 9:15 to 9:30, formal close 9:30, back door after 9:30, latest scan 10:07. Remove any recall-only peak claims. | `gen_p1_process.py` |
| DW-P1-12 | `d9-exception-paths.png` | 04 | redraw | Add an operator exception lane: QR scanner failure (hand-logged ID and name), gas (LPG) shortage (cut quantities, buy outside), broken grill/toaster, events and exams known only via the meeting, supplier impurity (reported, supplier changed), back-door late-comers after 9:30, biryani cooked at 100% (lunch, contrast), store vs physical book mismatch (raised at the meeting). Change node "Skip Meal toggle - reduces kitchen prep only" to "Skip Meal: designed to reduce kitchen prep (unconfirmed at Kadamba)". | `gen_p1_process.py` |
| DW-P1-13 | `d15-yuktahaar-operator-swimlane.png` | 04, "Yuktāhār: the book system as a process" | new | Swimlane (lanes: meeting / store / kitchen / counter / records). Daily meeting (inputs: matching-week Wastage Book, month pattern, events, registrations as regular + Jain + cash) -> store/ingredient book -> Grocery Book issue with Bhavani cross-check -> clean against the impurity norm (feedback arrow to supplier) -> cook 5:30 to 7:30, mostly one batch, poha in two -> service with first-half-hour projection -> top-up and re-cook cut-off by run-out time -> two roti counters at peak -> leftover idli to idli upma/poha at lunch, batter to fridge, milk to curd -> Wastage Book (Ajita: bin plus leftover) -> two-book reconciliation -> daily meeting -> matching week (two-week delay mark). | `gen_p1_process.py` |
| DW-P1-14 | `d16-kadamba-operator-swimlane.png` | 04, "The breakfast day, operator side" (after the table) | new | Governance strip on top: CFS > CDS (head open) > Prism chain. Lanes: planning / kitchen / safety / counter / after close. Veg and non-veg registrations -> 70% first batch by gram standard plus about 30 portions for outside people -> 5:30 chef batch items (sambar, upma) -> food-safety sequence (embed d17 as a compact band) -> live counter from 7:00 (dosa etc.) -> supervisor watches item levels -> top-up (10 to 15 min) -> hold and reheat (team judgement, candidate) -> last-10-minute crest -> 9:30 close, back door after 9:30 -> outside diners and about half the staff -> bin -> garbage contractor. Side exception: biryani lunch at 100%. | `gen_p1_process.py` |
| DW-P1-15 | `d17-food-safety-sequence.png` | 04 (optional, if d16 does not embed it), Phase 2 06 "Food-Safety Checkpoints" | new | Horizontal strip: cook -> cooking temperature -> 72 h sample -> wrapped display plate at entrance (confirmed, observed) -> serving temperature per item -> tasting by facility team + 2 Prism (confirmed, observed) -> corrections -> service by 7:30. Side notes: weekly QC; TDS daily for cooking and drinking water. Written to both assets folders. | `gen_p1_process.py` |
| DW-P1-16 | `diagram8-crowd-curve.png` | 05, 00 | redraw (replace recall curve with record-based chart) | Bars: % of April scans per 15-minute slot (`03_Arrival_15min.csv`), optional per-minute inset 9:00 to 9:45 showing the rate still climbing at 9:29. Kitchen markers at 5:30 (chef), 7:00 (live counter), 7:30 (service), 9:30 (close). Shade 7:30 to 8:00 as "Yuktāhār first-half-hour projection window (about 15% of diners on the Kadamba curve; candidate transfer)". Shade a back-door band after 9:30 to the latest scan 10:07. Optional ghost line: the operator's 100 / 100 / 150 rule of thumb against the bars. Caption to change from "Crowd Build Through the Breakfast Window" to "Measured arrival curve, Kadamba breakfast, April 2026". | new `gen_p1_charts.py` |
| DW-P1-17 | `d18-kadamba-daily-registered-vs-eaten.png` | 05, "Daily and weekday pattern: measured" | new | Daily registered vs availed, 1 to 30 April, veg and non-veg stacked or paired; flat registrations (~1,070) vs varying turnout. Annotate the 1 to 6 April non-veg ramp as "cause unknown, not a trend". | `gen_p1_charts.py` |
| DW-P1-18 | `d19-weekday-turnout.png` | 05, same section | new | Availed % by weekday (Tue 42.1% to Sun 27.3%) with average registered as a flat reference. | `gen_p1_charts.py` |
| DW-P1-19 | `d20-yuktahaar-breakfast-vs-lunch.png` | 05, same section | new | September register, breakfast vs lunch attendance % per day (breakfast about 28%, 17.7 to 40.2%; lunch 56 to 89%), hidden rows marked. Optional marker for the site head's "about 50%" belief as a horizontal dashed line. | `gen_p1_charts.py` |
| DW-P1-20 | `d21-two-kitchen-daily-timeline.png` | 05, "Daily service timeline: two kitchens" | new | Two lanes, Kadamba vs Yuktāhār, 5:30 to the next-day meeting, matching the table in that section: chef 5:30, live counter 7:00 / cooking done 7:30, service 7:30, supervisor top-up vs first-half-hour projection, crest, close 9:30, back door, leftovers (outside diners and staff vs reuse), records (gram standards, 5 to 10% figure vs Wastage Book), meeting. | new `gen_p1_timelines.py` |
| DW-P1-21 | `d22-planning-horizon-ladder.png` | 05, "Planning-horizon timeline: when each decision is fixed" | new | Decision ladder: month (automatic registration) -> T-4 (last cancellation) -> 1 week (dry goods) -> 2 to 3 days (some vegetables) -> T-1 (perishables, quantity set, Yuktāhār meeting) -> 5:30 (first batch cooked, the binding constraint, D-50) -> in service (top-up, upward only) -> 72 h (sample held). | `gen_p1_timelines.py` |
| DW-P1-22 | `diagram9-provisional-timeline.png` | 05 | redraw as two lanes (governance / operator) | Governance lane: existing items; mark the holiday non-compulsory precedent **disputed**. Operator lane: Prism wins the Kadamba tender (date unknown); Yuktāhār takeover (candidate 2025); August 2026 blame-free waste weighing starts; about December staff report waste falling, farm training trip; about March 2026 pink salt and cold-pressed oil ("previous six months"); Zoho tried and dropped (date unknown); Bakul/Palash off-site until the Felicity facility (~Dec 2026). Undated items drawn in a separate "date unknown" gutter, not guessed. | `gen_p1_timelines.py` |
| DW-P1-23 | `d10-loop-r1.png` | 05, 00 | redraw | Fix the polarity error (Mistake #14: "financial pain of no-show" -> "pressure to fix billing" signed minus; should be plus, with Mess Cell relief as the balancing symptomatic fix). Label with its Phase 2 ID in the subtitle ("L1 in the Phase 2 loop scheme"). Relabel registration as automatic default with T-4 cancellation. | new `gen_p1_loops.py` |
| DW-P1-24 | `d11-loop-b1.png` | 05 | redraw | Conflict marker (dashed, amber) on Skip Meal -> kitchen ("Kadamba cooks on registrations only"). Add Yuktāhār's second, within-meal channel: first-half-hour projection plus run-out re-cook, upward only. Retitle once Q2 is answered; until then use "B1: Skip Meal and Kitchen Preparation, link unresolved" and update the markdown caption at 05 line 210 to match. | `gen_p1_loops.py` |

**Phase 1 markdown edits that go with the diagrams** (do them in the same pass, then re-run the em dash check on the `.md`):
- 03: add `![Kadamba command chain](assets/d23-kadamba-command-chain.png)` in "Operator-side authority".
- 04: add d15 in "Yuktāhār: the book system as a process"; add d16 after the table in "The breakfast day, operator side"; optionally d17.
- 05: add d18, d19, d20 in "Daily and weekday pattern: measured"; d21 in "Daily service timeline: two kitchens"; d22 in "Planning-horizon timeline"; update the diagram8 and d11 captions.
- 00: update the diagram8 caption to match 05.

### 2.3 Phase 2 diagrams (`deliverables/phase-2/assets/`)

| ID | File | Embedded in | Action | Exact content changes | Generator |
|---|---|---|---|---|---|
| DW-P2-01 | `diagram1-system-map.png` | 06, 09, phase2.tex | edit | Add the operator layer with two contrasting on-site subsystems (Kadamba layered chain plus fixed 70% ratio; Yuktāhār flat plus book system) and the off-site kitchen; the extra-diner sink (30 to 50 outside people plus about half the staff); the garbage-contractor bin exit; the absent link from operator records (and CDS scans) to the rule owner (broken-link icon, red). Then **delete the caveat sentence** in 06 line 81 ("The diagram does not yet show ...") and in 09 line 22 ("The diagram draws the operators as one box."). | `gen_diagram1.py` |
| DW-P2-02 | `diagram13-kitchen-supply-subsystem.png` | 06, phase2.tex | edit | Kadamba three procurement tiers (1 week dry goods / 2 to 3 days some vegetables / day before perishables); food-safety checkpoint sequence before 7:30 (or a pointer node to d17); hold-and-reheat loop-back from surplus into service (dashed, candidate); bin -> garbage contractor. Delete 06 line 85's caveat sentence ("The diagram does not yet show those tiers ..."). | `gen_kitchen.py` |
| DW-P2-03 | `diagram32-yuktahaar-book-network.png` | 06, "The Yuktāhār Book System"; optionally Phase 1 04 | new | Network of books and their feeds: Grocery Book header (day's registrations regular + Jain) -> Wastage Book (per meal, per dish: issued, cooked, left, %, run-out time, re-cook, plate waste + leftover) -> weekday attendance register -> planning meeting -> store/ingredient book -> issue -> stock register -> fortnightly purchasing; vegetable book and indent (2 to 3 times a week, spoilage remarks); milk/fruit/gas/electricity/water register (Wednesday idli-grinding spike); fridge logs and cleaning checklist; wastage board (coordinator target); two-book reconciliation rule (store book = physical book, mismatch raised at meeting). Mark every book "confirmed (records)"; the connections "single-sourced (operator)". **No outbound edge** to CDS or any rule owner. | new `gen_book_system.py` |
| DW-P2-04 | `diagram33-operator-subsystems-compared.png` | 06, "Two Operator Subsystems Side by Side"; optional 09 | new | Two columns, Kadamba (Prism) vs Yuktāhār (ABC): organisation (six-level chain vs flat, two PMs); first batch (fixed 70% veg/non-veg vs matching-week lookup); in-service correction (supervisor against gram standards vs first-half-hour projection); records (gram standards, 5 to 10% base unstated vs full book system); surplus route (outside diners, staff, reheating candidate, bin vs reuse into lunch, curd); stance ("paid for the registration" vs "waste is cost"); measured turnout (37.1% vs about 28%). Mirrors the table in 06 line ~97 to 114; do not add facts not in that table. | new `gen_operator_compare.py` |
| DW-P2-05 | `diagram8-service-blueprint.png` | 06 | edit | Add a live top-up lane (supervisor call to kitchen, backstage); Yuktāhār first-half-hour projection; wrapped display-plate touchpoint at the entrance (physical evidence); back-door late entry after 9:30; Wastage Book support lane carrying records forward two weeks. Remove "four day ordering lock" as a stated reason. Delete 06 line 142's caveat sentence ("The blueprint as drawn does not yet show ..."). | `gen_blueprint.py` |
| DW-P2-06 | `diagram12-governance-escalation.png` | 06, phase2.tex | edit | Vendor layer under CDS via tender: Prism chain for Kadamba (ops manager, manager, supervisor), flat Yuktāhār box; CDS head conflict marked (Giri as Chair vs Raju as head, dashed). Keep the four D-24 terminology flags. Add the operational complaint path (director email -> manager -> WhatsApp group, CDS site team) as working for incidents; rule-change path absent. | `gen_governance.py` |
| DW-P2-07 | `diagram9-power-flow-network.png` | 06 | edit | Add operator node(s) (high information, authority over quantity only), Prism, the facility team (identity open, dashed). Operator records with no outbound arrow. Delete 06 line 174's caveat sentence ("That network does not yet include ..."). | `gen_pfn.py` |
| DW-P2-08 | Loop images in 06 (`diagram4`, `diagram5`, `diagram6`, `diagram7`, `diagram10`, `diagram11`, `diagram14`) | 06 | dedupe + relabel | **One canonical image per loop ID across Phase 2.** In 06 swap `diagram4-cld-r1-resale` -> `diagram25-cld-l1-resale`, `diagram5-cld-b1-skipmeal` -> `diagram28-chain-l2-skipmeal`, `diagram10-cld-b3-menu-rotation` -> `diagram26-cld-l4-menu-rotation`, `diagram14-cld-b4-shock-adaptive` -> `diagram27-cld-l6-shock-adaptive`. Keep `diagram6` (L3), `diagram11` (L5), `diagram7` (L7) but edit their in-image titles from R/B names to L3/L5/L7 and D-51 verdicts. Then retire diagram4, 5, 10, 14. | `gen_clds.py` (L3, L5, L7 only) |
| DW-P2-09 | `diagram24-loop-status-dashboard.png` | 07b | edit | Rows must match the 07b dashboard table exactly (18 mechanisms): status/delay text for L1 (automatic default with T-4 cancellation), L2 (Skip Meal conflict), L3b, L8 (plate basis), L9 (outside diners, staff, held food absorbers, not compost), L11, L12 (supervisor + gram standards; first-half-hour projection), L13 (quality branch), L14 (delay against the last-10-minute crest). Add a "Kitchen conversion" domain. Tally line: 3 closed (L4, L11, L12), 5 candidate closures, 6 chains, L3 contraindicated, L8 unresolved, L16 absent, L10 static. | `gen_task7b_loops.py` |
| DW-P2-10 | `diagram25-cld-l1-resale.png` | 07b, 06 (after DW-P2-08) | edit | Relabel registration from weekly/standing booking to "automatic default, 5 cancellations per meal type per month, T-4". Title keeps "reinforcing, candidate". | `gen_task7b_loops.py` |
| DW-P2-11 | `diagram26-cld-l4-menu-rotation.png` | 07b, 06 | keep (check title uses L4) | none beyond verifying labels | `gen_task7b_loops.py` |
| DW-P2-12 | `diagram27-cld-l6-shock-adaptive.png` | 07b, 06 | edit | Trigger label: relaxation is episodic (LPG shortage), not "all holidays"; title "condition-triggered chain", not a loop (D-51). Holiday precedent marked disputed. | `gen_task7b_loops.py` |
| DW-P2-13 | `diagram28-chain-l2-skipmeal.png` | 07b, 06 | edit | Skip Meal -> kitchen link drawn dashed amber "unresolved: Kadamba cooks on registrations only; earlier finding says declarations reach the kitchen". Add "no operator named it as a planning input". | `gen_task7b_loops.py` |
| DW-P2-14 | `diagram34-cld-l11-wastage-book.png` | 07b "L11", 06 loops section | new | Balancing loop at Yuktāhār: meal outcome -> Wastage Book entry -> matching-week lookup (two-week delay mark) -> next issue quantity -> cooked vs eaten gap -> (closes). Note "absent at Kadamba (gram standards, no turnout record)". | `gen_task7b_loops.py` |
| DW-P2-15 | `diagram35-cld-l12-two-forms.png` | 07b "L12", 06 | new | Two side-by-side balancing loops: Kadamba supervisor-reactive against gram standards; Yuktāhār first-half-hour projection plus run-out re-cook. Both upward only. Delay mark: 10 to 15 minute cook against the last-10-minute crest. | `gen_task7b_loops.py` |
| DW-P2-16 | `diagram36-chain-l13-quality-branch.png` | 07b "L13", 06 | new | Open chain: automatic registration -> fixed 70% first batch -> surplus -> held food -> reheating and vessel transfers -> quality degradation (four negative links on quality, team judgement, candidate) -> dashed, unevidenced closure through skipping/complaints. Side branch: surplus -> outside diners/staff and bin. Plus the unresolved 5 to 10% vs 70%/37% tension note. | `gen_task7b_loops.py` |
| DW-P2-17 | `diagram37-chain-l14-late-crest.png` | 07b "L14", 06 | new | Closing rush -> run-outs at the crest -> just-in-case larger first batch -> surplus; candidate ratchet closure (off-site 70% to 80%). Crest data from the April records. | `gen_task7b_loops.py` |
| DW-P2-18 | `diagram38-cld-l9-absorption.png` | 07b "L9" (optional) | new, optional | Members relabelled: reuse, outside diners and operator staff, held food (reheating candidate), back-door late-comers, bin exit; composting removed. Only build if the team wants every candidate loop drawn. | `gen_task7b_loops.py` |
| DW-P2-19 | `diagram18-chain1-registration.png` | 07 | edit | Replace "weekly blocks / cancellation four days, five a month" with auto-registration (5 per meal type per month, 4 days ahead, no nullify); mark Skip Meal -> kitchen as conflicting. | `gen_task7_chains.py` |
| DW-P2-20 | `diagram19-chain2-runouts.png` | 07 | edit | First batch now two logics (Kadamba fixed 70% veg/non-veg vs Yuktāhār lookup + first-half-hour projection); supervisor top-up; food-safety sequence before 7:30; back-door late entry; procurement tiers; floating items (bonda, puri, vada, idli). | `gen_task7_chains.py` |
| DW-P2-21 | `diagram20-chain3-complaints.png` | 07 | edit | Kadamba oversight chain (CFS, CDS, Prism, ops manager, manager, supervisor) covering safety/taste, not quantity; the waste-weighing blame event (Aug) at Yuktāhār; flat Yuktāhār organisation (two PMs). | `gen_task7_chains.py` |
| DW-P2-22 | `diagram21-chain4-shelved-fix.png` | 07 | edit | "30 to 40 extra portions for walk-ins" -> "about 30 portions for 30 to 50 outside diners"; "fixed weekly count" -> "automatic, pre-committed count". | `gen_task7_chains.py` |
| DW-P2-23 | `diagram22-chain5-menu-rotation.png` | 07 | edit (optional) | Optionally add the biryani 100% lunch contrast. | `gen_task7_chains.py` |
| DW-P2-24 | `diagram23-chain6-invisible-mess.png` | 07 | edit | Default auto-registration of absent and fasting students. | `gen_task7_chains.py` |
| DW-P2-25 | `diagram39-chain7-kitchen.png` | 07, "Chain 7" (currently has no image, breaking the D-44 one-per-chain pattern) | new | **Do not name it diagram24** (the pass-2 note suggested `diagram24-chain7-kitchen`, which collides with the loop dashboard). Two-lane Kadamba vs Yuktāhār layout in the chain template (event / pattern / structures / mental models) with absorbers (outside diners + half the staff, reheating candidate, reuse, bin) and the unresolved 5 to 10% tension. Mental models: Kadamba "cook what is registered", Yuktāhār "waste is cost", "measurement means blame" (then blame-free). | `gen_task7_chains.py` |
| DW-P2-26 | `diagram29-assumption-evidence-map.png` | 08e | edit | Rows must mirror 08e Section 2's assumption table as revised: add the operator-side assumptions (L11 and L12 as evidenced), revised Bakul/Palash row (shared off-site kitchen), cuisine row downgraded (registration fill, not attendance), Kadamba tier split (observer-verified vs translated gist), kilogram figures withdrawn, outside diners replacing "20 to 30 staff", composting removed. | `gen_evidence_register.py` |
| DW-P2-27 | `diagram30-stakeholder-perspective-grid.png` | 08r | edit | Split operators into Kadamba (Prism: "we are paid for the registration") and Yuktāhār (ABC: "waste is cost") cards; revise Students row to automatic registration; restrict the Faculty and staff row to Yuktāhār's 0 to 2 per breakfast; add rows for Non-student diners at Kadamba (30 to 50 outside people plus about half the staff) and Facility team and QC (safety and taste, not quantity). | `gen_reframe_diagrams.py` (`stakeholder_grid()`) |
| DW-P2-28 | `diagram31-reframe-iceberg.png` | 08r | edit | Events: add the display plate and a dated instance (e.g. Sunday 6 Sep Yuktāhār, 267 registered / 50 ate), per D-38. Patterns: crest spilling past 9:30; veg first batch about 2.2 times veg turnout. Structures: replace "weekly blocks / cancellation capped at five a month / Skip Meal tells the kitchen" with automatic registration and the 5-per-meal-type, 4-day exit; Skip Meal conflict flag; Kadamba 70% vs Yuktāhār matching-week plus first-half-hour; "oversight inspects safety and taste, never quantity". Mental models: replace "cooks by feel" with Kadamba "cook what is registered" vs Yuktāhār "waste is cost", and add "measurement means blame". | `gen_reframe_diagrams.py` (`reframe_iceberg()`) |
| DW-P2-29 | `diagram16-root-cause-network.png` | phase2.tex only | edit (only if phase2.tex keeps a root-cause figure) | Rebuild to the canonical causes in 07 Section 2 (D-50): automatic standing default; billing at the booking; gap measured but unrouted; two conditions (loudness at institution level, the absorption layer); intermediate mechanism: the uncalibrated conversion ratio. | `gen_task7_diagrams.py` |
| DW-P2-30 | `diagram15-iceberg-model.png`, `diagram17-loop-overview-dashboard.png` | phase2.tex only | retire | Pre-D-51 content. Replace in phase2.tex with diagram31 (iceberg) and diagram24 (dashboard). | none |
| DW-P2-31 | `d10-loop-r1.png`, `d11-loop-b1.png`, `diagram2-underprovisioning-loop.*`, `diagram3-mapping-sprint-quadrants.png` in `phase-2/assets/` | not embedded | retire (leave on disk or delete; team choice) | none | none |
| DW-P2-32 | 08d intervention/decision-rights diagram | 08d | none exists | The pass-2 notes are conditional ("any diagram that ..."). 08d embeds no diagram, so nothing to change. If the team wants one for 4.3, reuse d23 (Kadamba command chain) with the facility-team remit, and change any absorber label to "30 to 50 outside diners + about half of Kadamba staff", add held-and-reheated surplus as a non-protected absorber, and show the bin as the exit. Otherwise defer to Phase 3. | none |

**Phase 2 markdown edits that go with the diagrams:**
- 06: delete the four caveat sentences (lines 81, 85, 142, 174, each beginning "The diagram / blueprint / network does not yet ..."); add diagram32 in "The Yuktāhār Book System", diagram33 in "Two Operator Subsystems Side by Side", d17 in "Food-Safety Checkpoints"; swap the four loop images per DW-P2-08; add diagram34 to diagram37 in the loops section after L7.
- 07b: add diagram34 under L11, diagram35 under L12, diagram36 under L13, diagram37 under L14 (and diagram38 under L9 if built).
- 07: add `![Chain 7: The kitchen cooks to a guess, then absorbs the difference](assets/diagram39-chain7-kitchen.png)` under Chain 7.
- 09: delete the "The diagram draws the operators as one box." clause at line 22 once diagram1 is edited.
- Re-read any sentence that describes what a diagram shows after regenerating it; a caveat left in after the fix is a factual error.

---

## 3. Render recipe per deliverable

All commands from the repo root. Tools verified earlier on this machine: `pandoc`, `pdftotext`, `pdftoppm`, `pdfinfo`, Python 3 with `pypdf`, Google Chrome at `/Applications/Google Chrome.app`. Not available: `exiftool`, `qpdf`, `pikepdf`. Re-check before starting.

### 3.1 Housekeeping (once)

```sh
cd "/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project"
git fetch && git log -1 --oneline origin/main   # pull teammate work first (Section 9 standing rule)
grep -n "Observation images" .gitignore          # already ignored as of 2026-09-27; confirm
# decide: keep or delete .agents/skills/systems-visual-design/ (Codex mirror)
```

Pre-render source check on every markdown (D-43, D-42):

```sh
for f in deliverables/phase-1/0*.md deliverables/phase-2/0*.md; do
  printf "%s em:%s paths:%s\n" "$f" "$(grep -c '—' "$f")" \
    "$(grep -vE '^!\[' "$f" | grep -cE '\.(md|csv|xlsx|mp3|m4a|py|tex|html)\b|MASTER_CONTEXT|braindump|research/|Observation images')"
done   # every count must be 0
```

### 3.2 Diagrams

```sh
python3 deliverables/phase-1/assets/gen_p1_context.py      # etc., one per group in 2.1
python3 deliverables/phase-2/assets/gen_task7b_loops.py
python3 deliverables/phase-2/assets/gen_diagram1.py
python3 deliverables/phase-2/assets/gen_kitchen.py
python3 deliverables/phase-2/assets/gen_blueprint.py
python3 deliverables/phase-2/assets/gen_governance.py
python3 deliverables/phase-2/assets/gen_pfn.py
python3 deliverables/phase-2/assets/gen_clds.py
python3 deliverables/phase-2/assets/gen_task7_chains.py
python3 deliverables/phase-2/assets/gen_reframe_diagrams.py
python3 deliverables/phase-2/assets/gen_evidence_register.py
python3 deliverables/phase-2/assets/gen_book_system.py        # new
python3 deliverables/phase-2/assets/gen_operator_compare.py   # new
```

Each `render()` call screenshots at 2x with headless Chrome. Open and read every PNG before moving on (labels inside boxes, no overlapping arrow labels, nothing clipped, loops close, polarity signs visible). Harmless macOS stderr warnings (`CVDisplayLinkCreateWithCGDisplay`) can be ignored; confirm the PNG timestamp changed.

### 3.3 PDF and docx per deliverable (Section 5.7 pipeline)

PDF: `build_pdf.py` (pandoc gfm -> HTML fragment + `report-style.css` + Chrome `--print-to-pdf --no-pdf-header-footer`, with `<base href>` set to the markdown's folder so `assets/...` resolves). Docx: plain pandoc from the same markdown (`--toc`, resource path set to the markdown's folder). The Phase 1 docx files were once hand-finished; the markdown now carries all their content, so regenerating them from markdown is correct.

```sh
B=deliverables/phase-2/assets/build_pdf.py
P1=deliverables/phase-1; P2=deliverables/phase-2

# Phase 1
python3 $B $P1/01-system-context-brief.md        "$P1/System Context Brief.pdf"
python3 $B $P1/02-stakeholder-map.md             "$P1/Stakeholder Map.pdf"
python3 $B $P1/03-power-interest-leverage-map.md "$P1/Power-Interest Leverage Map.pdf"
python3 $B $P1/04-process-trace.md               "$P1/Process Trace.pdf"
python3 $B $P1/05-system-timeline-bot-map.md     "$P1/System Timeline BOT Map.pdf"
python3 $B $P1/00-consolidated-phase1-report.md  "$P1/Phase 1 Consolidated Report.pdf"
for pair in "01-system-context-brief:System Context Brief" "02-stakeholder-map:Stakeholder Map" \
  "03-power-interest-leverage-map:Power-Interest Leverage Map" "04-process-trace:Process Trace" \
  "05-system-timeline-bot-map:System Timeline BOT Map" "00-consolidated-phase1-report:Phase 1 Consolidated Report"; do
  src="${pair%%:*}"; out="${pair#*:}"
  pandoc "$P1/$src.md" -o "$P1/$out.docx" --toc --resource-path="$P1"
done

# Phase 2
python3 $B $P2/06-system-map.md                        "$P2/System Map.pdf"
python3 $B $P2/07b-causal-loop-feedback-analysis.md    "$P2/Causal Loop and Feedback Analysis.pdf"
python3 $B $P2/07-systemic-problem-analysis.md         "$P2/Systemic Problem Analysis.pdf"
python3 $B $P2/08-reframed-problem-statement.md        "$P2/Reframed Systemic Problem Statement.pdf"
python3 $B $P2/08-design-opportunity-statement.md      "$P2/Design Opportunity Statement.pdf"
python3 $B $P2/08-evidence-and-validation-register.md  "$P2/Evidence and Validation Register.pdf"
python3 $B $P2/09-phase2-consolidated-report.md        "$P2/Phase 2 Consolidated Report.pdf"
python3 $B $P2/assets/cover-page.md                    /tmp/cover.pdf   # use the scratchpad dir in practice
# docx: same loop as Phase 1 with the Phase 2 names above, --resource-path="$P2"
```

Note: `build_pdf.py` with `cover-page.md` sets `<base>` to `assets/`, which is harmless because the cover has no images. Check the cover is exactly one page.

### 3.4 Bundles and LaTeX reports

```python
# bundle.py  (run after every component PDF is scrubbed and checked)
from pypdf import PdfWriter
def cat(parts, out, title):
    w = PdfWriter()
    for p in parts: w.append(p)
    w.add_metadata({"/Title": title, "/Author": "", "/Subject": "", "/Creator": "", "/Producer": ""})
    with open(out, "wb") as f: w.write(f)
P1 = "deliverables/phase-1/"; P2 = "deliverables/phase-2/"
cat([P1+"System Context Brief.pdf", P1+"Stakeholder Map.pdf", P1+"Power-Interest Leverage Map.pdf",
     P1+"Process Trace.pdf", P1+"System Timeline BOT Map.pdf"], P1+"Invictus_Phase1.pdf", "Invictus Phase 1")
cat([COVER, P2+"System Map.pdf", P2+"Causal Loop and Feedback Analysis.pdf", P2+"Systemic Problem Analysis.pdf",
     P2+"Reframed Systemic Problem Statement.pdf", P2+"Design Opportunity Statement.pdf"],
    P2+"Invictus_Phase2.pdf", "Invictus Phase 2")
cat([COVER, P2+"Phase 2 Consolidated Report.pdf"], P2+"Invictus_Phase2_Condensed.pdf", "Invictus Phase 2 Condensed")
```

Team decision: whether the Evidence and Validation Register joins `Invictus_Phase2.pdf` (it was not in the 14 Sep bundle) and whether Phase 1 gets a cover page like Phase 2.

LaTeX reports (tectonic, from `report/` so relative figure paths resolve):

```sh
cd report && tectonic main.tex && tectonic phase2.tex
```

Then scrub both with the 5.4 `pypdf` snippet (they currently carry "LaTeX with hyperref" / "xdvipdfmx"). If `₹` appears, keep the `\rs` macro approach already in `phase2.tex` or add `newunicodechar` (5.4b).

### 3.5 Metadata scrub (D-13) for every rendered PDF

Chrome writes `Creator: Chromium` and `Producer: Skia/PDF`. Scrub each component PDF before bundling:

```python
import sys; from pypdf import PdfReader, PdfWriter
for p in sys.argv[1:]:
    r = PdfReader(p); w = PdfWriter(); w.append(r)
    t = r.metadata.title if r.metadata and r.metadata.title else ""
    w.add_metadata({"/Title": t, "/Author": "", "/Subject": "", "/Creator": "", "/Producer": ""})
    with open(p, "wb") as f: w.write(f)
```

For docx, inspect `unzip -p "X.docx" docProps/core.xml` and blank any creator/lastModifiedBy that names a tool or person the team does not want shown.

### 3.6 Compliance checks on the rendered output (D-42, D-43, D-47, D-13)

Run on every PDF, including bundles and `report/*.pdf`. Every count must be zero unless marked.

```sh
for p in deliverables/phase-1/*.pdf deliverables/phase-2/*.pdf report/*.pdf; do
  t=$(pdftotext "$p" - 2>/dev/null)
  em=$(printf "%s" "$t" | grep -o '—' | wc -l)
  paths=$(printf "%s" "$t" | grep -ciE '\.(md|csv|xlsx|mp3|m4a|py|tex|html|png)\b|assets/|deliverables/|research/|MASTER_CONTEXT|braindump|revisions/')
  resid=$(printf "%s" "$t" | grep -ciE 'pandoc|tectonic|xdvipdfmx|xetex|skia|chromium|claude|anthropic|chatgpt|codex|whisper|ai-generated|synthetic pilot')
  meta=$(pdfinfo "$p" | grep -E '^(Creator|Producer|Author|Subject):' | grep -v ':\s*$' | wc -l)
  echo "$p em=$em paths=$paths residue=$resid meta=$meta"
done
```

Note on "whisper": the transcription tool must not be named in a submitted PDF; phrase it as "translated recordings" if the method needs describing.

**Stale-content grep** (should find nothing, or only an explicit "revised" or "withdrawn" sentence per D-32):

```sh
grep -niE 'weekly block|procurement lock|places (food )?orders|20 to 30 (cooking|staff)|30 to 40 extra|16 ?kg|23 ?kg|compost|cooked at Palash|Adit Amma|Yuktahar|Palāsh|cooks by feel|~?30 ?% gap'
```

run over `pdftotext` output of each PDF. For Phase 2 PDFs and `phase2.pdf` also grep `\b(R[1-5]|B[1-4])\b` (old loop names; Phase 1's R1/B1 captions are allowed if they carry the L-ID note). Any "Giri" or "Raju" hit must sit next to the unresolved flag.

**Visual read (5.5):** `pdftoppm -png -r 90 "X.pdf" /tmp/x` (scratchpad in practice), then read every page: each figure has its caption and sits near its introducing text; no near-empty page from `break-inside: avoid` (acceptable once, fix if repeated by resizing the image); tables inside margins; the new wide swimlanes (d15, d16, d21) legible at print size, otherwise split or rotate.

---

## 4. The LaTeX reports

Both reports are compressed rewrites, not merges, in the existing template (`report/main.tex` preamble; `phase2.tex` already carries `\deliv` and `\statementbox`). The fastest reliable route is: for each source markdown section, `pandoc -f gfm -t latex --shift-heading-level-by=1` into a scratch file, then trim by hand to report length, keeping every finding and confidence word and dropping cross-document repetition. After writing, `grep -c -- '---' report/*.tex` should be 0 except in structural separators restored as colons (D-47), and the D-35 prose vocabulary replaces the old `\confirmed`/`\hypo`/`\openq` tag macros.

### 4.1 `report/main.tex` (Phase 1)

Set `\graphicspath{{../deliverables/phase-1/assets/}}` and reference the same filenames the markdown uses, then stop using `report/figures/` (this closes the Section 9 item about two unsynchronised figure copies; keep the folder only as history).

| main.tex section (current) | Rewrite from | Notes |
|---|---|---|
| Introduction | 00 "Introduction" + 00 "Status Summary" | Remove "validated drafts ... will be updated once interview data replaces hypotheses"; state the evidence base now includes operator visits, registers and 11,941 timestamped scans. |
| Task 1 (System Boundary, Context, Purpose, Symptoms, Actors..., Initial Problem Framing) | 01 all sections, including the new "Actual Mechanism" and "Gap Between Purpose and Mechanism" | Figures: diagram1, diagram2. Replace ~30% gap with ~63% / ~72%; drop Bakul-at-Palash; T-4 is a registration lock. |
| Task 2 (Use Case ... Findings) | 02 all sections | Figures: diagram3, diagram4, diagram5. 24 stakeholders, operator cluster, non-student diners. |
| Task 3 (Executive Summary ... Evidence Gaps) | 03, restructured to its framework headers (Assess Decision-Making Authority, Identify Formal and Informal Power, Analyse Incentives, Who Can Influence, Unequal Access, the Map, Implications, Key Findings, Outstanding Data Collection) | Figures: d13, d12, d14, d23. Operator-side authority, Kadamba chain, facility-team remit, information flows. |
| Task 4 ("A. Weekly Cycle", "B. Daily Cycle", "C. Exception and Workaround Paths", rules, escalation, confirmed vs hypothesised) | 04 all sections (Decision points: students / operators, book system as a process, the breakfast day operator side, rules both sides, escalation, exceptions, dependencies, findings) | Figures: diagram6 (monthly, not weekly), diagram7, d15, d16, d9. The old "weekly cycle" framing goes. |
| Task 5 (within-window, week scale, recurring pattern, loops) | 05 all sections | Figures: diagram8 (measured), d18 to d22, diagram9, d10, d11. |
| Summary and Status | 00 "Consolidated Findings" + "Outstanding Data Collection" | Carry the open questions in Section 5 of this plan that remain open. |

### 4.2 `report/phase2.tex` (Phase 2)

| phase2.tex section | Rewrite from | Figures (after this rebuild) |
|---|---|---|
| Introduction (incl. deliverable-to-section map) | 09 "Introduction" | none |
| Activity 6, Deliverable 1: System Map | 06 Overview, Actors/Process (Operator Layer; Registration, Procurement and Service), Three Kitchens, Yuktāhār Book System, Waste, Service Timeline, Food-Safety Checkpoints, Formal and Informal Structure (Raju/Giri flag), What Stands Out Most | diagram1, diagram33, diagram32, diagram13, diagram12 (optionally diagram8 blueprint) |
| Activity 6, Deliverable 2: Causal Loop / Feedback Analysis | 07b Overview, Dashboard (all 18 mechanisms), closed loops L11, L12, L4, candidates, chains L13, L14, L2, L6, absent/disconfirmed, structural causes | diagram24 (replaces diagram17), diagram35 or diagram34, diagram36, diagram28 (replaces diagram5), diagram27 (replaces diagram14); drop diagram4/diagram10 or swap for diagram25/diagram26 |
| Activity 7: The Iceberg Model, six chains | 07 Section 1, now **seven** chains | replace diagram15 with diagram39 (Chain 7) or one representative chain image |
| Activity 7: Structural root causes | 07 Section 2 (automatic standing default, billing at booking, measured but unrouted; loudness and absorption as conditions; uncalibrated conversion ratio as intermediate mechanism) | diagram16 rebuilt per DW-P2-29, or drop |
| Activity 7: Unintended consequences, archetypes, tensions | 07 Sections 4 to 6 (plus 7 Power Asymmetries and 8 Workarounds, compressed) | none |
| Activity 8, Deliverable 4: Reframed Systemic Problem Statement | 08r all sections | optionally diagram31 |
| Activity 8, Deliverable 5: Design Opportunity Statement | 08d all sections (four intervention points incl. 4.3 decision rights, constraints incl. blame-free measurement, gating questions, what Phase 3 inherits) | none |
| Outstanding Data Collection | 08e Section 5 + 07b "What Remains Untested" + 08d Section 7 | none |

Specific stale content in `phase2.tex` to remove: all six composting mentions (absorber list per D-49), the four-day lock as a procurement lock (D-50), old R/B loop names, any "20 to 30 staff" or kilogram figures. Decide whether the Evidence and Validation Register gets a short appendix (it is currently absent).

---

## 5. Open data questions to settle before rebuilding

Ordered by how many diagrams and sections a late answer would force to be redone. Each can be drawn as "unresolved" if it cannot be answered, but then the rebuild must not be repeated when the answer arrives unless it changes a label.

| # | Question | Blocks | How to settle |
|---|---|---|---|
| Q1 | **Payment basis:** is the operator paid per registered or per served plate, and what are the deductions? | L8 status (diagram24), d13/d14 incentive arrows, 08d levers held back (D-54), 07 Section 2 paragraph | Ask CDS for the tender terms; Kadamba floor staff do not know (owner side) |
| Q2 | **Skip Meal to kitchen:** do Skip Meal / cancellation counts reach each operator's planning, or does Kadamba cook on the registration count regardless? | d11, diagram28, diagram18, diagram6, d9 label, L2 status, 05 caption | One direct question to each operator |
| Q3 | **Kadamba 5 to 10% waste base:** per meal or per day, cooked weight or plate waste; is there a record? | diagram36, diagram39, 06 operator table, diagram33 | Ask the Kadamba supervisor; ask to see the record |
| Q4 | **CDS head: Raju or Giri?** Two roles or one name wrong? | diagram2, diagram4, d14, d23, diagram12 | Ask CFS or CDS directly (D-24: never merge) |
| Q5 | **Facility tasting team / weekly QC identity:** CDS committee faculty, CFS, or another body; do visits carry deductions? | d13, d14, d23, diagram9, diagram20, diagram30 | Ask the operator and CDS |
| Q6 | **Outside diners:** is "about 30 portions for 30 to 50 outside people" the same allocation as the earlier "30 to 40 walk-in portions"; are staff meals a written entitlement or a norm? | diagram2, diagram3, diagram36, diagram39, 08d absorber list (P5 tension) | Ask Prism |
| Q7 | **Waste route:** garbage contractor with no composting (Kadamba) vs outside compost facility (CFS Chair); who pays the contractor; Yuktāhār's route | diagram1, diagram2, diagram13, d16 exit labels | Ask the contractor or CDS |
| Q8 | **Off-site kitchen:** is Vijayalakshmi Caterers the Bakul/Palash operator (IIIT Road 54/55)? | diagram1, diagram2, diagram3, diagram1-system-map | Visit or ask CDS |
| Q9 | **Names in diagrams:** Ajita vs "Adit Amma" (likely same person); and whether individual staff first names (Ajita, Bhavani, Nazir) should appear in submitted diagrams at all, or roles only | diagram4, d15, diagram32 | Team decision; roles-only avoids the question |
| Q10 | **Dates for the operator timeline:** Prism tender award, Yuktāhār takeover year, Zoho trial, pink salt / cold-pressed oil start; is the holiday non-compulsory precedent real | diagram9 | Ask each operator; CDS for the tender date |
| Q11 | **Back door and first-half-hour projection at breakfast:** does the after-9:30 back-door entry and Yuktāhār's first-half-hour projection (and re-cook rule) apply at breakfast, not only lunch/dinner? | diagram8 bands, diagram8-service-blueprint, diagram35, d15, d16 | One question each; a 30-minute observation at close |
| Q12 | **Menu authority at Kadamba** and the identity of the operator-described "student committee" | d14, diagram12 | Ask CDS / committee |
| Q13 | **Yuktāhār breakfast record conflict:** Wastage Book 77 vs attendance register 110 on 3 Sep; which drives planning; why the head believes about 50% | d20 annotation, diagram32 | Ask the coordinator |
| Q14 | **Portal snapshot reliability** (116 vs 276 registered; 404 above a 355 capacity) | 01 cuisine row; any chart using portal capacity | Ask CDS; otherwise keep the row downgraded |
| Q15 | **Evidence freeze:** will another D-53 batch land before submission? | everything | Team decision; record the freeze date |

Questions that do **not** block the rebuild (draw as open and move on): Mess Council vs Mess Committee naming, the organised student email effort, R2 energy-crash confirmation, the "Daily eater - 2" respondent count, the 420 seats vs 1,200 capacity reconciliation.

---

## 6. Definition of done

- Every diagram in Sections 2.2 and 2.3 regenerated from a `gen_*.py` that sits next to its PNG, and read after rendering.
- Every caveat sentence about a diagram "not yet showing" something removed, and every new image referenced in its markdown.
- Every PDF and docx in Section 1 re-rendered from its markdown, scrubbed, and passing Section 3.6 with zero counts, then read page by page.
- Both bundles re-concatenated from the scrubbed components.
- `report/main.tex` and `report/phase2.tex` rewritten, compiled, scrubbed and checked.
- `MASTER_CONTEXT.md` updated: session entry, Section 1 status flipped to current, Section 9 render/diagram/report items closed, the `report/figures/` duplicate-copy item closed if main.tex now uses `deliverables/phase-1/assets/`.

---

## 7. Phase 3 additions (appended 2026-09-27, Phase 3 start)

Activities 9 and 10 were written in markdown on 2026-09-27 (MASTER_CONTEXT D-63 to D-69) and revised on 2026-09-28 against Lectures 11-15 (D-70 to D-78). No render in this section has been executed; the diagrams and charts in 7.2 are built. Phase 3 renders come after Phase 1 and Phase 2 (D-53 order).

### 7.1 Status rows (`deliverables/phase-3/`)

| # | Deliverable | Markdown (source) | Docx | PDF | Embedded images (all in `assets/`) | Regenerate | Order |
|---|---|---|---|---|---|---|---|
| 1-2 | Leverage-Point / System Intervention Map and Design Principles (Activity 9) | `09-leverage-point-intervention-map-and-design-principles.md` (revised 2026-09-28, ~14,760 words, 0 em dashes; LP1-LP12 with "Place n of 12" labels, P1-P7; verifier applied fixes, no second verification run recorded) | none yet | none yet | diagram-a9-leverage-intervention-map | quick re-check, docx, PDF (diagram current, re-rendered 2026-09-28) | P3-a |
| 3-5 | Intervention Concepts, Scenario Model and Final System Design Recommendation (Activity 10) | `10-design-test-evaluate-interventions.md` (revised 2026-09-28, ~17,770 words, 0 em dashes; verified pass: true) | none yet | none yet | diagram-a10-intervention-prototype, chart-a10-kitchen-scenarios, chart-a10-sunday-veg-batches, chart-a10-stress-tests, chart-a10-bot-projection | docx, PDF (images current, re-rendered 2026-09-28) | P3-b |
| - | Phase 3 input brief | `00-phase3-input-brief.md` (working input, never submitted; still LP-A..LP-O, mapping in D-64) | none | none | none | do not render | - |
| - | Bundle | none | none | `Invictus_Phase3.pdf` (not yet created) | none | concatenate cover + 09 + 10 | P3-c |
| - | LaTeX report | `report/phase3.tex` (not yet created) | none | `report/phase3.pdf` | via `\graphicspath{{../deliverables/phase-3/assets/}}` | write (7.4), compile, scrub | P3-d |

Before P3-b: re-run `python3 deliverables/phase-3/assets/scenario_model.py` and check that every number in 10 still matches its `scen_*.csv` (22 files, including `scen_late_cap.csv` and the 2026-09-28 sensitivity and stress files) and that the weighted scores recompute (weights 15/15/15/15/10/10/10/5/5 out of 400; both bundles 79%, single concepts 48 to 68%). The 2026-09-28 verification already did this for 10; repeat only if a source changes. Re-check 09 once (its verifier's fixes had no second run).

### 7.2 Diagrams: built vs still needed

**Built (current, each viewed after rendering; all re-rendered 2026-09-28):**

| File | Embedded in | Generator |
|---|---|---|
| `diagram-a9-leverage-intervention-map.png` (+ `.html`) | 09 (Deliverable 1) | `gen_leverage_map.py` (svgkit, headless Chrome, 2400x1580; IP1-IP14 tags; "Place n of 12" depth palette for places 2, 3, 4, 5, 6, 8, 10; LP11 and LP12 markers; LP5 at 6 and 8, LP6 at 6 and 10; 12-item key; no overlaps, nothing off the canvas. LP3's place 8 target is not drawn separately, stated in caption and legend. Rendered before the verifier's text-only fixes to 09) |
| `diagram-a10-intervention-prototype.png` (+ `.html`) | 10 (Prototypes) | `gen_a10_prototype.py` (lanes labelled quick fix / fundamental fix; "charged" ledger chip; joint-reading chip) |
| `chart-a10-kitchen-scenarios.png` (+ `.html`) | 10 (Scenario 1) | `gen_a10_charts.py` (numbers unchanged) |
| `chart-a10-sunday-veg-batches.png` (+ `.html`) | 10 (Scenario 3) | `gen_a10_charts.py` (numbers unchanged) |
| `chart-a10-stress-tests.png` (+ `.html`) | 10 (Scenario 6, new 2026-09-28) | `gen_a10_charts.py` (reads `scen_stress.csv`) |
| `chart-a10-bot-projection.png` (+ `.html`) | 10 (Scenario 7) | `gen_a10_charts.py` (reads `scen_bot_projection.csv`; rebuilt 2026-09-28 with range bands, stage markers for the joint reading, skip proposal, Sunday skip in force and decision point, and a conditional every-day band) |

**Still needed (none blocks the render):**
- DW-P3-01 (optional): annotated CLD overlay showing where the recommended bundle acts on L10, L11, L12, L13, L14 and L17 (loop IDs and verdicts from 07b; no chain promoted to a loop).
- DW-P3-02 (optional): the Activity 10 scoring table as a heat table for the PDF (currently a markdown table; now 9 criteria, 4 gates).
- DW-P3-04 (optional): the Activity 9 archetype table or the Activity 10 scenario-by-indicator matrix (Scenario 8, 6 x 11) as a figure, if the markdown tables do not fit the page width.
- DW-P3-03 (blocked on data): a Yuktāhār version of the Sunday arrival chart, once Yuktāhār breakfast scan times exist.
- Style check: the Activity 10 charts draw a white background while svgkit's page is #fbfbfd (harmless in PDF); Activity 9's caption is italic text under the image, whereas Phase 2 used alt text only. Pick one convention at render time.

### 7.3 Render recipe (same Section 5.7 pipeline as 3.3)

```sh
B=deliverables/phase-2/assets/build_pdf.py
P3=deliverables/phase-3

# diagrams and model (only if a source changed)
python3 $P3/assets/scenario_model.py
python3 $P3/assets/gen_leverage_map.py
python3 $P3/assets/gen_a10_prototype.py
python3 $P3/assets/gen_a10_charts.py

# PDF
python3 $B $P3/09-leverage-point-intervention-map-and-design-principles.md "$P3/Leverage-Point Intervention Map and Design Principles.pdf"
python3 $B $P3/10-design-test-evaluate-interventions.md                     "$P3/Intervention Design and Evaluation.pdf"

# docx
pandoc $P3/09-leverage-point-intervention-map-and-design-principles.md -o "$P3/Leverage-Point Intervention Map and Design Principles.docx" --toc --resource-path="$P3"
pandoc $P3/10-design-test-evaluate-interventions.md -o "$P3/Intervention Design and Evaluation.docx" --toc --resource-path="$P3"
```

Then: bundle (add to `bundle.py`: `cat([COVER3, P3+"Leverage-Point Intervention Map and Design Principles.pdf", P3+"Intervention Design and Evaluation.pdf"], P3+"Invictus_Phase3.pdf", "Invictus Phase 3")`, with a Phase 3 cover made like `deliverables/phase-2/assets/cover-page.md`); D-13 metadata scrub (3.5); compliance checks (3.6: zero em dashes, zero file-path references, no AI/tool residue). Phase 3 specific checks: the ₹ symbol renders (5.4b); every scenario number still carries "projected" and every stakeholder response "simulated" (D-66); people are named by role only (Raju/Giri and Ajita not named, D-24); the wide tables (the map table in 09, the scoring table in 10) fit the page width. The output file names above are proposals; the team may choose others.

### 7.4 Phase 3 LaTeX report

A Phase 3 LaTeX report, `report/phase3.tex`, should **mirror `report/phase2.tex`**: same preamble, macros (including `\rs`) and style, `\graphicspath{{../deliverables/phase-3/assets/}}`, an Introduction with a deliverable-to-section map, then one `\section` per activity with one `\subsection` per deliverable, written from the markdown, not independently.

| phase3.tex section | Rewrite from | Figures |
|---|---|---|
| Introduction (incl. deliverable-to-section map) | 09 and 10 Overviews | none |
| Activity 9: Identify leverage points; explore changes to rules, roles, incentives, information flows and processes | 09 "Identify Leverage Points" (LP1-LP12, archetypes, ranking) and "Explore Changes..." (five subsections, natural comparison) | none |
| Activity 9, Deliverable 1: Leverage-Point / System Intervention Map | 09 "Identify Potential Intervention Points" (IP1-IP14, Sunday breakfast) and "Deliverable 1" (map, table, absorber and stakeholder checks) | diagram-a9-leverage-intervention-map |
| Activity 9, Deliverable 2: Design Principles | 09 "Develop Design Principles" (Design Objective, Case for the Status Quo, P1-P7) | none |
| Activity 10, Deliverable 3: Intervention Concepts / Prototypes | 10 "Generate Alternative Interventions" and "Prototypes" | diagram-a10-intervention-prototype |
| Activity 10, Deliverable 4: Scenario Model and Impact Evaluation | 10 Scenario Model (Scenarios 1-8), "Simulate Stakeholder Responses", "Test Interventions Against System Objectives", "Identify Unintended Consequences" | chart-a10-kitchen-scenarios, chart-a10-sunday-veg-batches, chart-a10-stress-tests, chart-a10-bot-projection |
| Activity 10, Deliverable 5: Final System Design Recommendation | 10 "Refine the Intervention" and "Deliverable 5" | none |
| Key Findings and Outstanding Evidence | 09 and 10 closing sections, merged without duplicates | none |

Compile with `cd report && tectonic phase3.tex`, then scrub with the 5.4 `pypdf` snippet. Keep the projected/simulated labels (D-66) and zero `---` em dashes.

### 7.5 Open data questions added by Phase 3

These extend Section 5 (Q1, Q2, Q3, Q4, Q5, Q6, Q11, Q12 and Q13 also bear on Phase 3 content): whether a late batch can be cooked at 9:00 at Kadamba without delaying crest service; the real first batch per line and weekday and whether the supervisor already cooks in stages; Sunday skip uptake (assumed 25 to 50%); which registration regime applied to Yuktāhār's June breakfasts. None blocks the Phase 3 render; each is stated as open in the Outstanding Evidence sections of 09 and 10.

---

## 8. Pass 3 additions (appended 2026-09-28, Bakul Niwas evidence, D-79 to D-84)

Every Phase 1, 2 and 3 markdown file was revised a third time against Evidence Brief #3 (`research/primary-research/2026-09-28_bakul-niwas-evidence-brief.md`). Pass-3 audits: `deliverables/phase-*/revisions/2026-09-28-pass3_<id>-gap-audit.md`. Nothing was rendered (D-60 continues), so every PDF, docx, bundle and LaTeX report is now three passes stale (Phase 3: never rendered).

**Evidence corrections every touched diagram must carry:** Bakul's operator is **Vijayalakshmi Caterers**, cooking at **the Hafizpet kitchen, ~8 km** (not "near the airport"); Palash's kitchen is candidate (dashed). **Three operator regimes**, not two: Kadamba fixed ratio; Bakul 70-80% by item, adjusted weekly, **~70% shortage floor** (L11 at Bakul: candidate, floor-bounded); Yuktāhār books. The **"70 → 80%" change is withdrawn**: remove it from any timeline or loop. Bakul's peak is **8:00-8:30** (manager); the closing crest is **Kadamba's records**, not every hall's. L12 carries the **transport delay** (lead time unknown) and the ~50 reserve at 9:20 (candidate). Payment basis: Bakul says **"plates served"** (flagged, unresolved). Bakul complaint route: CDS team → manager → kitchen → MD (do not write "Hafizpet" into it).

| Diagram (embedding file) | Pass-3 change |
|---|---|
| Phase 1 `diagram1-system-boundary`, `diagram2-context-map` (01) | Name Bakul's operator and the Hafizpet kitchen; show hot holding at the hall; Palash dashed |
| Phase 1 `diagram3-stakeholder-map`, `diagram4-relationship-network` (02) | Bakul operator named; Bakul information, food, complaint and money flows (text diagram now in 02) |
| Phase 1 `d14-power-flow-network` (03) | Bakul manager as a node holding consumption and pairing knowledge with no route to the menu owner. The Phase 1 copy exists (checked 2026-09-28); the pull removed only the Phase 2 copy and `deliverables/phase-2/assets/diagram1-system-map.svg` |
| Phase 1 `diagram8-crowd-curve` (05) | Caption/subtitle: Kadamba records only; Bakul's manager describes an 8:00-8:30 peak |
| Phase 1 `diagram9-provisional-timeline` (05) | Remove the "70 → 80%" event; add the ~3 AM prep → ~7 AM arrival → 9:20 reserve morning if space allows |
| Phase 1 `d11-loop-b1` (05) | Bakul's weekly channel, bounded by the floor, plus the upward-only phoned top-up |
| Phase 2 `diagram1-system-map` (06) | Bakul + Hafizpet off site, ~8 km link, hot holding, three regimes |
| Phase 2 `diagram13-kitchen-supply-subsystem` (06) | Add a Bakul panel or companion off-site supply diagram (from the text diagram in 06): temperature kept, texture lost |
| Phase 2 `diagram8` service blueprint, `diagram9` power flow, `diagram12` governance (06) | Bakul lane (30-min check, phoned top-up, 9:20 reserve); Bakul manager node; Bakul complaint route |
| Phase 2 `diagram24` loop dashboard (07b) | L11 row: Bakul candidate; L12: off-site delay, lead time unknown; L14: 70 → 80 evidence removed |
| Phase 2 `diagram19`, `diagram20`, `diagram22`, `diagram39` (07) | Chain 2 per-hall crest + Bakul reserve; Chain 3 Bakul complaint route; Chain 5 menu-formation tension; Chain 7 three regimes, no 70 → 80 |
| Phase 2 candidate new diagram | Menu-formation tension (text diagram in 06) |
| Phase 3 `diagram-a9-leverage-intervention-map.png` (09) | Learning link "confirmed at Yuktāhār, candidate at Bakul (floor-bounded), absent at Kadamba"; IP5/IP8 off-site branch and 9:20 reserve; LP6 "per hall". Then delete 09's sentence saying the drawing does not yet show Bakul |
| Phase 3 `diagram-a10-intervention-prototype.png` (10) | Bakul chip (check variant of B, per-hall C) and learning-link note |
| Phase 3 `chart-a10-stress-tests.png` (10) | Subtitle "Kadamba only" |

**No model re-run needed:** Activity 10's scenario model and every `scen_*.csv` are unchanged (checksum verified); scores recompute unchanged.

**Open data questions added (Brief #3 §10):** Critical: plate basis per operator (Bakul "served" vs Kadamba "paid for" registrations); Bakul breakfast scan export; does Bakul write anything down; Hafizpet top-up lead time. Important: Bakul residents' reasons for skipping; item-level draw and waste at Bakul; basis of the 9:20 reserve; menu decision rights. Nice-to-have: protein target basis; regional preference in menu setting; Palash's operator and kitchen.

---

## 9. Status check and additions (appended 2026-10-06)

### 9.1 Where things stand

Checked against the files and the git history on 2026-10-06:

- **Markdown: current.** Every Phase 1, 2 and 3 markdown file has been revised three times (pass 1 on Brief #1, pass 2 on Brief #2, pass 3 on Brief #3, the Bakul evidence). These are the source of truth.
- **Phase 1 and Phase 2 PDFs, docx files, bundles and diagrams: stale.** All are dated 6 to 14 September and predate every revision pass. No commit on any branch re-renders them.
- **LaTeX reports: stale.** `report/main.tex` and `report/phase2.tex` predate every revision pass; `report/phase3.tex` does not exist.
- **Phase 3 diagrams and charts: current as of 2026-09-28**, but each still needs its pass-3 change from Section 8.
- **Phase 3 has a submission-facing report that Section 7 does not know about.** See 9.3.

So the work in Sections 2, 3, 4, 7 and 8 is all still to do. Count: 56 diagram items (Section 2) plus 17 pass-3 items (Section 8), 13 PDFs, 12 docx files, 3 bundles, 3 LaTeX reports.

### 9.2 Decisions to take before starting

These change how much work the rebuild is. Take them as a team and record the answers in `MASTER_CONTEXT.md` before anyone renders anything.

| # | Decision | Suggested default |
|---|---|---|
| T1 | **Evidence freeze (Section 5, Q15).** Is any more field data coming before submission? | Freeze now. Draw every open question in Section 5 and Section 8 as "unresolved" (dashed grey) and do not wait for answers |
| T2 | **Phase 3 submission form.** Render 09 and 10 as two PDFs plus `Invictus_Phase3.pdf` (Section 7), or keep the team's condensed report (9.3) as the submission | Keep the condensed report as the submission; treat 09 and 10 as working documents and skip P3-a to P3-c |
| T3 | **LaTeX reports.** Are `report/main.pdf`, `report/phase2.pdf` and a new `report/phase3.pdf` actually submitted? | If not submitted, skip Section 4 and 7.4 entirely; they are the largest single item |
| T4 | **Humanizing pass (9.4).** Run it on every Phase 1 and Phase 2 document before rendering? | Yes, per D-85, done by whoever has the skill installed |
| T5 | **Chart data in git (Section 2.1).** Copy the aggregate CSVs (no student IDs) into `deliverables/phase-1/assets/data/` so charts rebuild from git | Yes; otherwise only a machine with `Observation images/` can rebuild diagram8, d18, d19, d20 |
| T6 | **Field photos (9.5).** Which photos go into which deliverable | Decide per deliverable; none are embedded today outside the Phase 3 report |
| T7 | **Evidence and Validation Register in the Phase 2 bundle, and a Phase 1 cover page** (Section 3.4) | Keep the 14 Sep composition unless the team wants otherwise |

### 9.3 The Phase 3 report

On 2026-09-29 the team's condensed Phase 3 report was rebuilt as markdown and re-rendered. It is the submission-facing Phase 3 text; `09-...md` and `10-...md` remain the full working documents.

| File (`deliverables/phase-3/`) | What it is |
|---|---|
| `Invictus_Phase3_Activities_9_10.md` | Markdown source of the condensed report (about 15,900 words) |
| `Invictus_Phase3_4..pdf` | Rendered report, 36 pages |
| `Invictus_Phase3_Activities_9_10_humanized.docx` | Editable copy |
| `Invictus_Phase3_Activities_9_10_temp.pdf` | The team's original 39-page PDF, kept untouched |
| `assets/build_pdf.py`, `assets/phase3-style.css` | Its renderer and stylesheet (separate from the Phase 2 pair) |
| `humanize/` | Working files: the faithful rebuild, section chunks, extracted figures |

To re-render it after an edit:

```sh
python3 deliverables/phase-3/assets/build_pdf.py \
  deliverables/phase-3/Invictus_Phase3_Activities_9_10.md \
  "deliverables/phase-3/Invictus_Phase3_4..pdf"
```

Then run the Section 3.5 scrub and the Section 3.6 checks on it. Before treating it as final, read it once against the pass-3 audits `deliverables/phase-3/revisions/2026-09-28-pass3_09-gap-audit.md` and `..._10-gap-audit.md`: it already names Bakul as the Vijayalakshmi Caterers hall at the Hafizpet kitchen, but nobody has checked it line by line against pass 3. If its figures are re-exported, they must carry the Section 8 changes to the two Phase 3 diagrams and the stress chart.

### 9.4 Humanizing pass (D-85)

Standing rule since 2026-09-29: every Word or PDF deliverable is rewritten to read as human-written before its final render, keeping every section, table, figure, number, ID and confidence label. In the order of work it sits **after the markdown is final and before Section 3.3**.

- The method is in the repo at `.claude/skills/ai-humanizer/SKILL.md` (added 2026-10-06): the contract, the catalogue of tells to remove, and the order of work. Anyone can follow it by hand or with an assistant. `scripts/check_preservation.py` beside it compares the before and after text and must report PASS; `scripts/fix_ligatures.py` repairs text extracted from a PDF.
- Whatever the method, the test is the same: no heading, ID or number lost or invented, zero em dashes, and the Section 3.6 checks still pass.
- Humanize the markdown, not the PDF. The humanized markdown replaces the source file, so the docx and PDF are both built from it.
- Expect documents dense with tables to shrink 5 to 10 percent. Do not cut facts to reach a target.

### 9.5 Field photos

Nothing in Sections 2 or 3 places a photograph. What exists:

- `Observation images/Photos/`: 26 photos of Yuktāhār's registers and kitchen (26 Sep 2026), indexed in `Observation images/Extracted Data/csv/00_Image_Index.csv`. Gitignored (D-59), so only on machines that were given the folder.
- `deliverables/phase-2/assets/WhatsApp Image 2026-09-13 *.jpeg`: 4 CDS and CFS posters. In git.
- `deliverables/phase-3/humanize/figs/`: 10 figures extracted from the team's Phase 3 PDF, some of them photos. In git.

No Kadamba photo files were found in the repo or in `Observation images/` on 2026-10-06. If Kadamba photos exist, add them to `Observation images/Photos/` and index them before anyone plans a layout around them.

A photo used in a deliverable must be copied into that deliverable's `assets/` folder (the gitignored folder cannot be referenced from a render another teammate will repeat), must show no student ID, face or name the team has not agreed to show, and follows the roles-only rule for staff (D-24, Section 5 Q9).

### 9.6 Corrections to earlier sections

- Section 3.1 hardcodes one machine's path. Run every command from your own clone's root instead.
- Section 7.1 says "Docx: none yet, PDF: none yet" for Phase 3. True for 09 and 10; see 9.3 for the condensed report.
- Decision IDs: the Bakul pass uses D-79 to D-84. The humanizing rule, first logged as D-79, is **D-85**.
- The Phase 3 scenario model (`deliverables/phase-3/assets/scenario_model.py`) reads the raw `Observation images/april-data.xlsx`. It does not need re-running (Section 8), and cannot be re-run without that folder.

