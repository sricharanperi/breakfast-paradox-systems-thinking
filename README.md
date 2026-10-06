# The Breakfast Paradox: Team Invictus

Systems Thinking and Design capstone, IIIT Hyderabad. The project asks why students are registered and billed for hostel breakfasts that about two thirds of them never eat, and where the system could change.

**If you are here to rebuild the submissions, this page is your guide and [`deliverables/REBUILD_PLAN.md`](deliverables/REBUILD_PLAN.md) is your work list.** Read this page top to bottom once, then work from the plan.

## Where the project stands (6 October 2026)

| Layer | State |
|---|---|
| Research and evidence briefs | Current |
| Markdown for every deliverable, Activities 1 to 10 | Current. Revised three times against the field evidence |
| Phase 3 diagrams and charts | Built on 28 September; each needs one small Bakul update |
| Phase 3 condensed report (36-page PDF) | Rendered on 29 September |
| Phase 1 and Phase 2 PDFs, Word files, bundles and diagrams | **Stale.** Dated 6 to 14 September, before every revision. They still show overturned facts |
| LaTeX reports in `report/` | **Stale.** `phase3.tex` does not exist yet |

The rebuild is the job of making the stale rows match the markdown. Nothing in the rebuild plan has been run yet.

## The rule that matters most

**The markdown is the source of truth.** Never edit a PDF or Word file by hand. If something is wrong, fix the `.md` and render again. The same goes for diagrams: fix the `gen_*.py` script and re-run it.

## What to read, in this order

You do not need to read everything. This order gets you ready in about an hour.

| # | File | Why |
|---|---|---|
| 1 | [`deliverables/REBUILD_PLAN.md`](deliverables/REBUILD_PLAN.md), **Section 9 first**, then Section 1 | Section 9 is the current status and the decisions to take before starting. Section 1 is the table of every file to regenerate |
| 2 | [`MASTER_CONTEXT.md`](MASTER_CONTEXT.md), Sections 1, 5 and 7 | Project overview, the render pipeline and its known bugs, and the decision log (D-1 to D-85). Section 4 is the full history; read it only when you need the reason behind something |
| 3 | The three evidence briefs in [`research/primary-research/`](research/primary-research/) | The facts every diagram and document must agree with. Brief #3 (Bakul, 28 Sep) overrides Brief #2 (team field account, 27 Sep), which overrides Brief #1 (mess operations, 26 Sep) wherever they conflict. Brief #1 stays the authority for record-level numbers |
| 4 | [`.claude/skills/systems-visual-design/SKILL.md`](.claude/skills/systems-visual-design/SKILL.md) | How diagrams are made here: hand-composed SVG through `svgkit.py`, rendered with headless Chrome. No Mermaid |
| 5 | [`.claude/skills/ai-humanizer/SKILL.md`](.claude/skills/ai-humanizer/SKILL.md) | The humanizing pass every document goes through before rendering: what to rewrite, what must never change, and how to check nothing was lost |
| 6 | The gap audits in `deliverables/phase-*/revisions/` for the deliverable you are rebuilding | Each audit says exactly what its diagrams must now show. Three passes per deliverable: `2026-09-27_*`, `2026-09-27-pass2_*`, `2026-09-28-pass3_*` |

Reference only, when a question comes up: [`project_framework .pdf`](project_framework%20.pdf) (the assignment's activities and deliverables; section headings in every deliverable follow its wording) and `ProblemStatements.pdf`.

## The source files

These are what you render from. Do not render anything else.

| Activity | Markdown source | Output name |
|---|---|---|
| 1 | `deliverables/phase-1/01-system-context-brief.md` | System Context Brief |
| 2 | `deliverables/phase-1/02-stakeholder-map.md` | Stakeholder Map |
| 3 | `deliverables/phase-1/03-power-interest-leverage-map.md` | Power-Interest Leverage Map |
| 4 | `deliverables/phase-1/04-process-trace.md` | Process Trace |
| 5 | `deliverables/phase-1/05-system-timeline-bot-map.md` | System Timeline BOT Map |
| Phase 1 summary | `deliverables/phase-1/00-consolidated-phase1-report.md` | Phase 1 Consolidated Report |
| 6 | `deliverables/phase-2/06-system-map.md` | System Map |
| 6 | `deliverables/phase-2/07b-causal-loop-feedback-analysis.md` | Causal Loop and Feedback Analysis |
| 7 | `deliverables/phase-2/07-systemic-problem-analysis.md` | Systemic Problem Analysis |
| 8 | `deliverables/phase-2/08-reframed-problem-statement.md` | Reframed Systemic Problem Statement |
| 8 | `deliverables/phase-2/08-design-opportunity-statement.md` | Design Opportunity Statement |
| 8, supporting | `deliverables/phase-2/08-evidence-and-validation-register.md` | Evidence and Validation Register |
| Phase 2 summary | `deliverables/phase-2/09-phase2-consolidated-report.md` | Phase 2 Consolidated Report |
| 9 and 10, condensed | `deliverables/phase-3/Invictus_Phase3_Activities_9_10.md` | Invictus_Phase3_4..pdf |
| 9, full working text | `deliverables/phase-3/09-leverage-point-intervention-map-and-design-principles.md` | not rendered yet |
| 10, full working text | `deliverables/phase-3/10-design-test-evaluate-interventions.md` | not rendered yet |

Files named `prathyusha_*.md`, everything under `revisions/`, `humanize/` and `00-phase3-input-brief.md` are working material. They are never submitted.

## What you need on your machine

- `pandoc`, `tectonic` (only for the LaTeX reports), and poppler (`pdftotext`, `pdftoppm`, `pdfinfo`)
- Python 3 with `pypdf` (`pip install pypdf`)
- Google Chrome at `/Applications/Google Chrome.app`. The diagram scripts and both `build_pdf.py` files call it headless. On Windows or Linux, change the `CHROME` path at the top of those scripts
- Nothing else. The field data the charts read is in the repo under `Observation images/`: the Kadamba April scan export, the extracted tables, the register photos and the translated transcripts. Only the audio recordings are left out, and the rebuild does not need them

Check before you start:

```sh
which pandoc pdftotext pdftoppm pdfinfo
python3 -c "import pypdf; print(pypdf.__version__)"
ls "/Applications/Google Chrome.app"
```

## The rebuild, step by step

Run every command from the root of your clone. Section numbers refer to `deliverables/REBUILD_PLAN.md`, which has the exact commands.

**Step 0. Agree the open decisions.** Plan Section 9.2 lists seven: whether evidence is frozen, how Phase 3 is submitted, whether the LaTeX reports are needed, the humanizing pass, chart data in git, field photos, and bundle contents. Agree them on the team chat and write the answers into `MASTER_CONTEXT.md`. These decide how much work there is, so do not skip this.

**Step 1. Pull first, then say what you are taking.** `git pull`, then tell the team which rows of the plan's Section 1 you are doing. Two people rendering the same PDF will overwrite each other, because PDFs cannot be merged.

**Step 2. Check the markdown is clean.** Run the pre-render check in Section 3.1. Every deliverable must show zero em dashes and zero references to files outside itself.

**Step 3. Shared diagram setup.** Section 2.1: add the new icons to `icon-defs.svg`, and create the seven Phase 1 generator scripts. Phase 1 has no generators today, because its diagrams were Mermaid. One person should do this step, since everyone else depends on it.

**Step 4. Phase 1 diagrams.** Section 2.2, plus the Phase 1 rows of the Section 8 table. For each diagram: write or edit the generator, run it, then open the PNG and look at it. A redraw keeps its old filename, so the markdown does not need to change.

**Step 5. Phase 2 diagrams.** Section 2.3 plus the Phase 2 rows of Section 8, in this order: 07b, 06, 07, 08 reframed, 08 register. 07b goes first because 06 reuses its loop images.

**Step 6. Phase 3 diagrams.** The three Phase 3 rows of the Section 8 table. Small label changes only. The scenario model does not need re-running.

**Step 7. Markdown touch-ups.** Add the image line for every new diagram, update captions, and delete the sentences that say a diagram "does not yet show" something. Section 2 lists each one.

**Step 8. Humanizing pass.** Section 9.4. Done on the markdown, before rendering. The method is written out in [`.claude/skills/ai-humanizer/SKILL.md`](.claude/skills/ai-humanizer/SKILL.md), with a checker script beside it that confirms no heading, ID or number was lost.

**Step 9. Render PDFs and Word files.** Section 3.3 for Phases 1 and 2, Section 9.3 for the Phase 3 report. Phase 1 before Phase 2.

**Step 10. Scrub metadata.** Section 3.5, on every PDF. Chrome writes its own name into the file properties.

**Step 11. Run the checks.** Section 3.6 on every PDF. Every count must be zero. Then convert each PDF to page images and read every page; this is how every real layout bug in this project has been caught.

**Step 12. Bundles.** Section 3.4: `Invictus_Phase1.pdf`, `Invictus_Phase2.pdf`, `Invictus_Phase2_Condensed.pdf`. Only after every component PDF has passed Step 11.

**Step 13. LaTeX reports,** if the team decided they are needed. Section 4 and Section 7.4.

**Step 14. Record and push.** Add a dated session entry to `MASTER_CONTEXT.md` Section 4, flip the status tables in its Section 1 to current, close the render items in its Section 9, and tick the plan's Section 6. Then commit and push.

## Facts every diagram and document must now carry

The old files get these wrong. The full list is at the top of the plan and in its Section 8.

- Breakfast turnout is about 37 percent at Kadamba (April records) and about 28 percent at Yuktāhār (September register). The gap is 63 to 72 percent, not "about 30 percent".
- Registration is an automatic default. The only exit is five cancellations per meal type per month, each at least four days ahead.
- Three operators, three ways of deciding how much to cook: Kadamba (Prism) cooks a fixed 70 percent; Bakul (Vijayalakshmi Caterers, cooking at Hafizpet about 8 km away) cooks 70 to 80 percent by item, reviewed weekly, never below about 70; Yuktāhār (ABC Hospitality Services) plans from its own books.
- Composting is not where the surplus goes. Kadamba's waste goes to a garbage contractor.
- "20 to 30 staff eat leftovers" is replaced by about 30 portions for 30 to 50 outside diners, plus about half of Kadamba's own staff.
- Loops are numbered L1 to L17 plus L3b. Only three close with every link evidenced: L4, L11 and L12. The old R1, B1, B2 names are retired.
- Leverage points are LP1 to LP12, intervention points IP1 to IP14, design principles P1 to P7.

## House rules for anything submitted

- Every claim carries one of four labels: confirmed, single-sourced, candidate, assumed. Phase 3 adds projected (model output), simulated (expected stakeholder response) and planned (test not yet run).
- People are named by role only. Where two sources disagree (who heads CDS, whether Skip Meal reaches the kitchen, the plate basis for operator payment), show it as open. Never pick one.
- No em dashes. No mention of any file, tool, lecture or book inside a submitted document; the grader gets only the PDF.
- Spellings: Yuktāhār, Palash, Kadamba, Bakul.
- When a finding was overturned, say so in the text as a revision. Do not quietly swap the number.

## Repository map

```
MASTER_CONTEXT.md          Project history, decisions, pipeline notes, open items
README.md                  This page
deliverables/
  REBUILD_PLAN.md          The rebuild work list
  phase-1/                 Activities 1 to 5: markdown, Word, PDF, assets/, revisions/
  phase-2/                 Activities 6 to 8: same layout; assets/ holds the gen_*.py diagram scripts and build_pdf.py
  phase-3/                 Activities 9 and 10: markdown, the condensed report, assets/ (diagrams, charts, scenario model)
research/
  primary-research/        Evidence briefs, interviews, portal screenshots
  methodology/             Interview guides and method notes
  book-notes-*.md, lecture-notes-*.md
report/                    LaTeX reports and their figures
tools/                     Vendored diagramming tools, for reference only
.claude/skills/            systems-visual-design (diagram toolkit) and ai-humanizer (humanizing pass)
Observation images/        Field data: Photos/, april-data.xlsx, Extracted Data/ (tables, transcripts). Audio is not in git
```

## Team

Sricharan Peri, Prathyusha Kalluri, Neha. Everyone commits to `main`, so pull before you start and before you push.
