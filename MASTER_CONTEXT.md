# MASTER CONTEXT — Breakfast Paradox / Systems Thinking Capstone

**This file is the single source of truth for this repository's history, decisions, research, technical pipeline, and open threads.** It exists so that any person or any AI agent (Claude or otherwise, on any account) can pick this project up cold and have full context — no prior chat log required.

---

## 0. HOW TO MAINTAIN THIS FILE (read this first, every time)

- **Update this file after every significant piece of work** — a new deliverable, a bug fix, a research finding, a pipeline change, a decision the user made. "Significant" means: if it would matter to someone resuming this project from scratch, it goes in here.
- **Append, don't rewrite.** Add new dated entries to the `SESSION LOG` (Section 4). Only edit earlier sections (People, Repo Map, Playbook, Open Items) when the underlying fact actually changed — e.g. a new tool became available, an open question got answered.
- **Every session entry should cover:** what the user asked for, what inputs/data the user gave, what was investigated, every decision made and *why*, every mistake hit and how it was found/fixed, what was produced, and what's left open.
- **When an open item (Section 6) gets resolved, move it** from "Open Items" into the session log entry that resolved it, and delete it from Section 6.
- **This file is committed and pushed to `origin/main`** (the user's explicit choice — see Session 2026-09-12, decision D-14). That is a deliberate departure from this repo's usual practice of scrubbing AI-pipeline fingerprints from submitted deliverables (see Section 5, "AI-fingerprint scrubbing"). This file itself is *not* scrubbed — it is allowed to say "Claude," "pandoc," "tectonic," etc. freely, because it lives outside `deliverables/` and is not itself submitted for grading. If that assumption ever changes, flag it to the user before continuing to write AI-process detail into a tracked file.
- **Do not blindly trust old entries as still true of the live repo.** Before recommending or reusing anything referenced below (a file path, a script, a tool flag), verify it still exists — treat this file the way the harness's own memory-system guidance treats memory: a snapshot in time, not a live oracle.

---

## 1. PROJECT OVERVIEW

**Course:** Systems Thinking, Semester 3, PDM program (per `Courses-Syllabus_M26-V1.pdf` in the parent folder).

**Project name:** "Breakfast Paradox" — a systems-thinking capstone studying why students at IIIT Hyderabad register for the hostel breakfast mess in large numbers but a large share don't actually show up to eat, despite billing being tied to registration, not attendance.

**Repository:** `https://github.com/sricharanperi/breakfast-paradox-systems-thinking` (git repo lives at `/Users/Shared/Files From e.localized/PDM/Sem3/Systems Thinking/Project`; the parent `Systems Thinking` folder holds this repo plus unrelated course materials — lecture slides, the syllabus, reference textbooks — that are **not** part of the git repo).

**Team submission name:** "Invictus" (per the final merged-PDF filename, `Invictus_Phase1.pdf`).

**Deliverable structure (Phase 1, complete):**
| # | Deliverable | Markdown source | Docx | PDF |
|---|---|---|---|---|
| 1 | System Context Brief | `01-system-context-brief.md` | `System Context Brief.docx` | `System Context Brief.pdf` |
| 2 | Stakeholder Map | `02-stakeholder-map.md` | `Stakeholder Map.docx` | `Stakeholder Map.pdf` |
| 3 | Power-Interest / Leverage Map | `03-power-interest-leverage-map.md` | `Power-Interest Leverage Map.docx` | `Power-Interest Leverage Map.pdf` |
| 4 | Process Trace | `04-process-trace.md` | `Process Trace.docx` | `Process Trace.pdf` |
| 5 | System Timeline / BOT Map | `05-system-timeline-bot-map.md` | `System Timeline BOT Map.docx` | `System Timeline BOT Map.pdf` |
| — | Consolidated Report | `00-consolidated-phase1-report.md` | `Phase 1 Consolidated Report.docx` | `Phase 1 Consolidated Report.pdf` |
| — | Final submission bundle | — | — | `Invictus_Phase1.pdf` (straight concatenation of the five deliverable PDFs, 42 pages, no re-summarization) |

All six live in `deliverables/phase-1/`, alongside `assets/` (mermaid `.mmd` diagram sources + rendered `.png`s) and a set of `prathyusha_*.md` files (a teammate's raw/working documents, kept as historical record rather than deleted once consolidated).

**Deliverable structure (Phase 2, in progress):**
| # | Deliverable | Markdown source | Docx | PDF |
|---|---|---|---|---|
| 6 | System Map | `06-system-map.md` | *(not yet built)* | *(not yet built)* |
| 7 | Systemic Problem Analysis | `07-systemic-problem-analysis.md` | *(not yet built)* | *(not yet built)* |

Both live in `deliverables/phase-2/`, with their own `assets/` (some newly drawn, some reused/copied from `deliverables/phase-1/assets/` — see Session 2026-09-12 (Phase 2 kickoff) below). As of the last pull, Phase 2 exists only as markdown + diagram assets — no `.docx`/`.pdf` conversion pass has happened yet, unlike Phase 1's fully-built pipeline.

There is also a `report/` directory with a separate LaTeX-based write-up (`report/main.tex` → `report/main.pdf`) and its own `report/figures/` — a parallel, more traditional academic-report rendering of the same diagrams, distinct from the `deliverables/phase-1/*.docx→pdf` submission pipeline.

---

## 2. PEOPLE

| Git identity | Real name (as committed) | Role in this repo |
|---|---|---|
| `sricharanperi` <sricharanperi27@gmail.com> | (the user of this Claude Code session) | Repo owner; System Context Brief author; Phase 1 consolidation, docx→PDF conversion pipeline, final submission prep |
| `Kalluri Lakshmi Prathyusha` | Prathyusha | Teammate; Stakeholder Map, Power-Interest/Leverage Map, Power Analysis Brief, governance research (Student Parliament, Mess Committee/Office), interview guides 1 & 3, most of the primary interview fieldwork |
| `neha771` <nehasusan369@gmail.com> | Neha | Teammate; interview guide contributions, independent interview-transcript summary/cross-check, report figure assets; authored Phase 2 Tasks 6-7 (System Map, Systemic Problem Analysis) solo |

All three commit to the same `main` branch directly (no PR workflow observed in this repo — merges are plain `git merge` after concurrent pushes).

---

## 3. REPOSITORY / ENTITY MAP

```
Project/                                   (git repo root)
├── MASTER_CONTEXT.md                      ← this file
├── .gitignore                             (excludes copyrighted book PDFs + OS cruft)
├── deliverables/phase-1/                  Submission-ready outputs (the graded artifact)
│   ├── 00-consolidated-phase1-report.md … 05-system-timeline-bot-map.md   (markdown source of truth for each deliverable's prose)
│   ├── *.docx                              Word versions, hand-finished (diagrams manually placed, occasional manual edits post-generation)
│   ├── *.pdf                               Submission format, generated FROM the .docx via pandoc+tectonic (see Section 5 playbook)
│   ├── Invictus_Phase1.pdf                 Final bundle: straight concat of the 5 deliverable PDFs
│   ├── prathyusha_*.md                     Prathyusha's raw working documents (superseded by the consolidated .md files above, kept for provenance)
│   └── assets/                             Diagram sources (.mmd = Mermaid source) and rendered .png exports, used both in the docx files and report/
├── deliverables/phase-2/                  Phase 2 outputs (IN PROGRESS — markdown + diagrams only, no docx/pdf yet)
│   ├── 06-system-map.md                    Task 6: System Map (actors/process/resources/constraints synthesis of Phase 1)
│   ├── 07-systemic-problem-analysis.md     Task 7: Systemic Problem Analysis (events→patterns→structures→mental models, feedback loops, root causes)
│   └── assets/                             Some diagrams newly drawn (diagram1-system-map, diagram2-underprovisioning-loop); others are direct copies of Phase 1 loop diagrams (d10-loop-r1.png, d11-loop-b1.png, d14-power-flow-network.png) reused as-is
├── report/                                 A separate, parallel LaTeX academic write-up of the same project
│   ├── main.tex / main.pdf
│   └── figures/                            Its own .mmd + .png diagram set (numbered d1–d14, overlaps conceptually with deliverables/phase-1/assets but is a separate copy)
├── research/                               All research inputs and methodology notes (NOT submitted directly, but everything above is built from this)
│   ├── primary-research/
│   │   ├── interviews/                     Real interview transcripts (the project's core evidence base)
│   │   ├── screenshots/                    Portal screenshots (registration UI, capacities, rates) — filenames are dated by the calendar date shown IN the screenshot's content, not necessarily the capture date
│   │   ├── team-contributions/             Teammate-authored research notes folded into the main brief
│   │   └── index.md
│   ├── methodology/                        Interview guides (1, 2, 3), synthetic pilot-testing notes, UX-research-method reading notes
│   ├── working-drafts/                     Superseded early drafts, kept as historical record
│   ├── dt-worksheets/                      Design Thinking Toolbox worksheet templates (vendored reference material)
│   ├── service-design-playbook/            Vendored reference material (license + README only tracked)
│   ├── book-notes-fifth-discipline*.md     Reading notes on Senge's "The Fifth Discipline" / Fieldbook
│   ├── course-and-syllabus-study.md
│   └── tool-notes.md
├── tools/                                  Vendored open-source diagramming tools (Loopy, a CLD editor, a stakeholder-map tool) — reference/inspiration, not built or run as part of the pipeline
├── project_framework .pdf                  The assignment's own methods framework — deliverable section headers are written to match this document's wording exactly (a deliberate, repeated decision — see D-2 below)
├── prathyusha_braindump.md
└── (large reference textbook PDFs — gitignored, not redistributed)
```

**Key cross-references (entity relationships worth knowing):**
- Every `deliverables/phase-1/0N-*.md` file's section headers are written to match `project_framework .pdf`'s own activity/method wording verbatim — a standing constraint, not a one-off choice.
- Every `deliverables/phase-1/0N-*.md` traces back to specific `research/primary-research/interviews/*.md` entries and `research/methodology/*` guides; the "Outstanding Data Collection" section at the end of Tasks 3–5 explicitly lists which claims still need mess-committee/vendor-side data that hasn't been collected yet.
- `deliverables/phase-1/assets/*.mmd` and `report/figures/*.mmd` are Mermaid diagram sources rendered to `.png` for embedding — these are two separate copies of conceptually overlapping diagrams (one set feeds the Word/PDF deliverables, the other feeds the separate LaTeX `report/`).
- `prathyusha_*.md` files in `deliverables/phase-1/` are raw inputs that were manually folded into the numbered `0N-*.md` files by sricharanperi in later commits; they are intentionally not deleted (explicit decision, see commit `312b663`: "Mark context-brief corrections file as superseded... kept as historical record rather than deleted").

---

## 4. SESSION LOG (chronological, most recent last)

> Each entry below covers one working session (one Claude Code conversation). Sessions before 2026-09-12 are reconstructed from git commit messages, diffs, and file timestamps — no original chat transcript survived for them, but by the user's explicit instruction (2026-09-12 session, decision D-13) they are written with the same level of narrative detail as a directly-observed session, not flagged as lower-confidence.

### Session: 2026-09-03 — Project bootstrap
**Commit:** `dbf9247` "Initial commit: Breakfast Paradox systems-thinking capstone project"
**By:** sricharanperi, with Claude (`session_019kay9AyBmu5aLpaiUKTt3M`)

- First commit of the whole repo: course materials, `project_framework .pdf`, primary research (first interview, portal screenshots), the first draft of the System Context Brief, research methodology notes, and the vendored diagramming tools (Loopy, CLD editor, stakeholder-map tool).
- **Decision D-1:** Copyrighted commercial book PDFs (Buxton, Carroll, Becker, Constantine, Hall, Tidwell, etc.) are excluded from git via `.gitignore`, even though they were used as research input — "not ours to redistribute." This is the origin of the current `.gitignore`.

### Session: 2026-09-05 (morning) — Prathyusha: synthetic pilot interviews
**Commits:** `7453b41` (braindump), `9c4ca4d` (synthetic pilot + Guide 1 rewrite), `600e009` (progress plan)

- Prathyusha ran two AI-simulated personas (an "attender" and a "skipper") through draft Interview Guide 1 to stress-test the questions before real interviews were conducted.
- A third AI critique pass on those synthetic transcripts caught 4 leading/binary questions in the guide and surfaced new angles worth asking about: batch weekly registration, a "companion-absence effect" (does a friend not attending change your own decision), and skepticism toward proposed levers/interventions.
- **Decision D-2:** Guide 1 was rewritten based on this critique. The synthetic transcripts and the critique log were kept but explicitly marked **non-ground-truth** — a recurring, important discipline in this project: synthetic/simulated data is never allowed to silently masquerade as real respondent evidence. (This discipline is why, later on 2026-09-06, the "synthetic pilot" methodology references get scrubbed from the Power Analysis Brief once real data supersedes them — see that session.)

### Session: 2026-09-05 (afternoon/evening) — sricharanperi: System Context Brief overhaul + Prathyusha's Activity 2
**Commits:** `a967e3a`, `4f65c2c`, `325974f`, `45254b1` (merge), `5da4d00`, `a5f7a4c`, `00c5489`, `bc4dc25` (merge), `312b663`, `20d21eb`
**By:** sricharanperi with Claude (`session_01UURzEtfrZ3EbRSeQgXD8kp`), interleaved with Prathyusha's own commits (`session_01UwZvjo2cHAtuzXRd1NgoyS`)

This was a big, multi-pass session. Key decisions and work:

- **Decision D-3:** Split the System Context Brief's "Purpose" section into three: true purpose (2a), the actual operating mechanism (2b), and the gap between them (2c). Rationale: the registration/billing mechanism rewards pre-committing over actually attending, which the team judged explains more of the observed paradox than the previously-assumed "class-schedule overlap" explanation alone.
- Integrated a teammate's independent hypothesis (Skip Meal vs. Mess Cell as a dominant strategy for students), added behavioral-economics lenses (loss aversion, present bias, sunk-cost numbing, default effects) and 8 research verticals, archiving the teammate's verbatim contribution under `research/primary-research/team-contributions/` rather than paraphrasing it into the main text — **decision D-4: attribution and traceability of teammate research is preserved by keeping their verbatim file, not just their conclusions.**
- Added a fifth persona ("Role E — rush/latecomer") and revised bias-loaded questions.
- Read and incorporated UX-research methodology texts (Erika Hall's *Just Enough Research*, Nunnally & Farkas, Dumas & Loring, King/Churchill/Tan) into the project's own interview standard (Section 11 of the Context Brief).
- Reconciled sricharanperi's independent Context Brief rewrite with Prathyusha's parallel Phase 1 work (which had been developing Stakeholder Map, Power-Interest Map, Process Trace, System Timeline, and Guide 3 concurrently) — fixed one stale cross-reference that the merge introduced.
- **Decision D-5:** Rewrote the Context Brief to match `project_framework .pdf`'s Activity 1 wording exactly, in the framework's own order, and **removed all hedging language, source citations, and process narration** in favor of direct factual statements — the working draft with that narration was archived to `research/working-drafts/`, not deleted. This "state findings directly, no visible research-process narration, no citations" style is a standing decision that shows up again and again in later sessions.
- Prathyusha's Activity 2 (Stakeholder Map) work: corrected mess structure from a veg/non-veg framing to a cuisine-based one (Kadamba=South Indian, Bakul/Palash=North Indian, Yuktahar=Jain); split a previously-collapsed "Mess Committee/Mess Office" into distinct governance actors; discovered Ping (an informal/unofficial coordination tool) and portal-IT as stakeholders; replaced a weak "Bakul is newer" explanation for its low uptake with a stronger cuisine-preference hypothesis, evidenced across three messes.
- sricharanperi then integrated those corrections into the Context Brief: cuisine-based mess framing; governance split into Mess Committee (policy, faculty-chaired — *later found to need softening, see 2026-09-06*), Mess Office (operations, ~4-day procurement lead time, issuer of a workload-driven cancellation-policy change), and Warden (vendor management); corrected the escalation-mechanism symptom from "no channel exists" to "three channels exist, none with a confirmed record of producing policy change"; rewrote the Initial Problem Framing into short plain sentences ending in one direct question.
- Prathyusha then **consolidated** the Stakeholder Map: merged a diagram-first map and a separate stakeholder-register file into one document (every stakeholder now carries role/interest/need/expectation in prose, not split across files) — **decision D-6, a repeating pattern in this project: raw/working files get merged into one polished, submission-shaped document, and the redundant intermediate file is deleted with cross-references fixed**, except where explicitly kept for provenance (see D-4, and `312b663` marking a corrections file "superseded... kept as historical record").
- sricharanperi then built the final `02-stakeholder-map.md` + `.docx`, consolidating Prathyusha's `prathyusha_02-stakeholder-map.md` into the **Design Thinking Toolbox's own stakeholder-map template structure** (Use Case, Stakeholders, Create the Map, Relationships, Findings) — **decision D-7: deliverable structure follows the assignment's method-toolbox templates, not an ad hoc structure**, covering all four of Activity 2's required methods: primary/secondary/indirect classification (17 stakeholders included, 4 minor, 3 excluded — explicitly quantified), a full interests/needs/expectations table, a relationship/dependency/conflict matrix, and formal-vs-informal role distinctions. Added three new diagrams (a DT-template concentric-ring map, a relationship-network view, an onion/proximity-to-student view), with the source PowerPoint template kept in `assets/` for provenance.

### Session: 2026-09-06 (early) — neha771: interview guide + report assets
**Commits:** `0f07e6e`, `9f865e9`

- Neha contributed a "quick interview guide" and some in-progress report assets. (No Claude co-authorship trailer on these two commits — likely done without an AI session, or without the trailer being added.)

### Session: 2026-09-06 (mid-afternoon) — Prathyusha: Activity 3 (Power-Interest/Leverage Map)
**Commits:** `84e16d2`, `46d5196` (merge), `c15a748`, `b939e4c`, `6cd091a`
**By:** Prathyusha with Claude (`session_01UwZvjo2cHAtuzXRd1NgoyS`)

- Built a full first-principles power/leverage analysis from scratch: a power taxonomy, a 26-domain decision-rights matrix, formal-vs-informal power tracing, five incentive chains, bargaining/dependency asymmetry analysis, historical precedent research, resource-control mapping, and leverage-rights analysis.
- **Key findings this pass:** Mess Committee / Mess Office / Warden are three separate governance actors with an *unconfirmed* relationship between them; Academic Administration has zero relationship to any of the three (confirmed three independent ways); students control the one input (registration intent) every other actor's forecasting depends on, while bearing no cost for its inaccuracy — a central systemic tension of the whole project; students' collective organizing capacity (proven to exist via the informal Mess Cell resale market) has never been observed aimed at governance rather than peer-to-peer transactions — termed "sleeping leverage" at this point.
- **Decision D-8:** Ten open questions were logged and explicitly left unanswered rather than guessed at, with raw discovery notes kept separate from the polished brief — a discipline of not inventing certainty maintained throughout the project.
- A follow-up commit (`c15a748`) folded answers to those ten questions back in. Two answers **revised** findings rather than just filling gaps: (1) a confirmed student representative on the Mess Committee softened the "consulted but cannot decide" finding; (2) a confirmed prior instance of organized student action aimed at governance (not just peer-to-peer) overturned "sleeping collective leverage," relabeling it **"exercised-but-unmeasured leverage"** since the subject/outcome of that action was still unknown. Also surfaced a new term, "Mess Council," as the confirmed recipient of a public complaint-email channel, with an unresolved relationship to the Mess Committee (this ambiguity is later mostly resolved — see next session).
- A synthetic pilot transcript for Guide 3 (governance) was logged (`b939e4c`), explicitly flagged as **weaker evidentiary status** than the student-side synthetic pilots, since no real governance-side account existed anywhere in the project yet to validate the persona against. Its stated purpose was only to check that the Guide 3 questions elicit honest uncertainty rather than manufactured confidence — not to produce findings.
- A full audit pass (`6cd091a`) self-scored the Power-Interest/Leverage Map + Power Analysis Brief at "75/100, Strong not yet distinction-level," logged a completion plan for every gap, and applied P0/P1 fixes directly: corrected evidence-confidence drift on the "faculty-chaired" Mess Committee claim, added false-precision disclaimers to both quadrant charts, added a precedent-honesty statement, added a domain-specific "Authority at a Glance" table, flagged two incentive chains as hypothesis-only.
- **Independent research finding (verified from source, not a search snippet):** IIIT-H's Student Parliament maintains an elected Mess Secretary and per-mess Mess Deputy Secretaries — a real, reachable stakeholder that had been entirely missing from the Stakeholder Map. Added there. Also found that "Mess Council" was very likely a naming mix-up with a *different* institution (IIT Hyderabad, not IIIT-H) — an important correction, not a new confirmed actor. Found two new historical precedents ("Let Them Eat Frogs," "Water Mess") showing a recurring "complaint ignored until crisis" pattern, and a strong-but-unconfirmed candidate match for the previously-unidentified organized student email effort. The interview guide was updated to prioritize the Mess Secretary as the single best remaining research target.

### Session: 2026-09-06 (evening) — neha771 + Prathyusha: real interview data, Activities 4 & 5
**Commits:** `5eedfbf` (merge), `cdb36c0`, `edc55e6`, `1f074ae`
**By:** Prathyusha with Claude (`session_01UwZvjo2cHAtuzXRd1NgoyS`), plus neha771's independent transcript work

- Five real student interviews were conducted and logged (2 daily eaters, 3 skippers) — `research/primary-research/interviews/2026-09-06_five-student-interviews-guide1.md` — giving Activities 4 (Process Trace) and 5 (System Timeline/BOT Map) their first real evidentiary base. Both were explicitly split into an "A" part (established now, from real data) and a "B" part (a completion plan for the entirely-unobserved mess/kitchen side) — **decision D-9, same discipline as D-8: don't claim what you haven't observed, and say explicitly what's still missing.**
- **Key findings:** monthly (not weekly) batch registration confirmed directly by respondents; Skip Meal shows **zero real usage** across every respondent who addressed it — strong confirmation of the dominant-strategy hypothesis; peer influence was **disconfirmed** as a decision-determining factor and downgraded to a weak motivator only; a new finding that staff-promised restocks often don't arrive; a new "under-provisioning for real attendees" candidate loop, independently corroborated by two respondents; every respondent who offered a fix suggestion converged on the same one (extend closing time, don't shift the start time); across six respondents there is **no single population-level attendance trend** — some rising, some falling, one flat at zero all semester. This "no single trend" finding recurs as a headline caution against over-claiming throughout the later Process Trace / BOT Map documents.
- **Decision D-10 — cross-validation practice:** this reading of the five interviews was cross-checked against neha771's *independent* synthesis of the same transcripts (`student_interview_summary_neha.md`). Two corrections were adopted specifically *because* her independent reading was better supported: "monthly" (not "weekly") cycle terminology, and reconciling an apparent two-peak crowding contradiction into a single continuously-building crowd cresting near the 9:30 close.
- A further reconciliation pass (`1f074ae`) cross-checked two **independent transcriptions of the same five interviews** (one from `Interview data.pdf`, one from `Interview data.docx`) and confirmed they described the same five real respondents, not ten. It also caught a genuine ambiguity in the *source* data — a labeling collision where "Daily eater - 2" and "Daily eater - 3" both appear as labels but only one transcript follows both, meaning a true "-2" respondent's answers might be missing from the source entirely. **Decision D-11: this was flagged explicitly in both files rather than silently resolved by guessing**, since neither guess (mislabeled vs. genuinely missing) was verifiable from the source alone. This is a strong instance of the project's "don't invent certainty" discipline being applied to a data-hygiene problem, not just a findings problem.

### Session: 2026-09-06 (night) — sricharanperi: Finalize Tasks 3–5 + Consolidated Report
**Commit:** `f3faa1c` "Finalize Tasks 3-5 and consolidated Phase 1 report; fix cross-document consistency gaps"
**By:** sricharanperi with Claude (`session_01UURzEtfrZ3EbRSeQgXD8kp`)

- Built the final submission-ready Task 3 (Power-Interest/Leverage Map + Power Analysis Brief), Task 4 (Process Trace), and Task 5 (System Timeline/BOT Map) documents, each as matched `.md` + `.docx` pairs in the same style as Tasks 1–2: exact `project_framework .pdf` wording as section headers, no hedging, no citations (continuing decision D-5/D-7).
- Task 3 built from Prathyusha's governance research (Student Parliament roles, Mess Committee/Office split, four historical precedents) plus the already-audited power/leverage/authority analysis.
- Task 4 built from the six real interviews: monthly (not weekly) registration, disconfirmed peer-influence hypothesis, broken restock promises, zero real Skip Meal usage.
- Task 5: reconciled crowd-peak curve, confirmed R1/B1 feedback loops, plus the new under-provisioning loop.
- **Decision D-12:** Tasks 3–5 each end with an explicit "Outstanding Data Collection" section stating that mess-committee/vendor-side data will be collected and submitted later, rather than treating open items as answered — the same discipline as D-8/D-9, now made a standard closing section across every deliverable.
- **Consistency-fix pass across Tasks 1–2:** so nothing in the earlier deliverables contradicted the newer governance research — softened the unverified "faculty-chaired" Mess Committee detail, added the Student Parliament stakeholder to the Stakeholder Map (which Prathyusha's own research had flagged as missing), added the confirmed class-attendance-policy trade-off to Task 1's symptom table. This is a recurring maintenance pattern worth naming: **whenever a later deliverable's research contradicts or refines an earlier one, the earlier one gets patched, not left inconsistent.**
- New diagrams: monthly registration cycle, corrected daily attendance cycle, reconciled crowd-build curve, provisional governance timeline; some figures reused from `report/figures/` for Tasks 3 and 5.
- Built `Phase 1 Consolidated Report.pdf`: all five deliverables' main concepts combined into one **8-page** submission-ready PDF — explicitly **not** a full concatenation but a compressed synthesis — compiled via pandoc+tectonic to get a real, page-numbered table of contents. (Contrast with `Invictus_Phase1.pdf` later, which *is* a full concatenation of the five full deliverables — two different documents serving two different purposes: a short synthesis vs. the complete submission bundle.)

### Session: 2026-09-06 (late night) — sricharanperi: docx→PDF conversion pipeline, all five deliverables
**Commit:** `3885a3c` "Convert all five Phase 1 deliverables to submission-ready PDFs; fix docx-conversion bugs and strip tool metadata"
**By:** sricharanperi with Claude (`session_01UURzEtfrZ3EbRSeQgXD8kp`)

This is the session that established the **pandoc+tectonic conversion pipeline** documented in full in Section 5 below. Summary of what happened:

- Generated PDFs for all five individual deliverables directly from their `.docx` files (including a stakeholder-map infographic the user had manually added to the Stakeholder Map docx — preserved as-is, not regenerated), plus `Phase 1 - All Five Deliverables (Merged).pdf` (later renamed to `Invictus_Phase1.pdf` — see 2026-09-12 session) as a straight concatenation: 42 pages in, 42 pages out, no content loss, no re-summarization.
- **Bugs found and fixed during a full dry-run pass** (the direct ancestor of the same class of bugs re-encountered on 2026-09-12):
  1. A stray, unpopulated "Table of Contents" heading/link-block left over from each docx's own (unrefreshed) Word TOC field — stripped before re-typesetting.
  2. A dropped Unicode "interrupted relationship" glyph in the Stakeholder Map's diagram legend — replaced with a LaTeX-safe `X`.
  3. The user's manually-added stakeholder-map infographic had inherited a duplicate "Onion Proximity Map" caption from the image above it — relabeled to its own accurate caption, image itself untouched.
  4. The leverage-quadrant chart's title was clipped by Mermaid's own `quadrantChart` rendering at its original long title length — shortened to "Power vs Leverage" and regenerated.
  5. The provisional-timeline diagram was too tall for one page and got sliced across a page break — rebuilt as a horizontal (`LR`) Mermaid layout instead of vertical.
- **Decision D-13 (established here, still active): AI-pipeline residue removal.** Two "synthetic pilot/persona" methodology references in the Power Analysis Brief were removed — judged no longer load-bearing once six real respondents independently corroborated the same findings. And **every output PDF's `Title`/`Author`/`Creator`/`Producer`/`Subject` metadata is blanked** before submission (previously "LaTeX via pandoc" / "xdvipdfmx" was visible in PDF file properties). A final text-and-metadata scan across all seven PDFs confirmed zero remaining hits for any tool-fingerprint or AI-pipeline term. **This is the standing policy that governs every PDF this project submits — see Section 5's "AI-fingerprint scrubbing" subsection for the exact recipe.**

### Session: 2026-09-07 (post-session manual edits, uncommitted until 2026-09-12)

Between the previous commit (2026-09-06 23:41) and this timestamp (2026-09-06 23:39–23:51 — the same night, just after the AI session ended), the user made three changes **by hand, outside any Claude session**, which then sat uncommitted in the working tree for six days:
1. Renamed `Phase 1 - All Five Deliverables (Merged).pdf` → `Invictus_Phase1.pdf` (identical bytes, just the final submission filename).
2. Manually edited `Process Trace.docx` and `System Timeline BOT Map.docx` in Word: added a Table of Contents to each (via Word's TOC field feature), and removed a "Source"/"Respondent" identifier column (with interview dates like `2026-09-03`, `2026-09-06`) from the evidence tables in both — an apparent anonymization/cleanup pass.
3. Never regenerated the PDFs from these edits, and never committed anything.

This gap is exactly what the 2026-09-12 session below was asked to resume and close.

### Session: 2026-09-12 — Resume, close the gap, regenerate stale PDFs, fix TOC bug, write this file
**By:** sricharanperi with Claude (this session; no separate `Claude-Session` URL trailer on the resulting commit — see D-14)

**User's opening request:** "I want you to resume the session we did for the submission of the deliverables last week Sunday night. I am not able to retrieve that chat context." No other input or data was given beyond that sentence — everything else in this session was derived by investigating the actual state of the repo and filesystem.

**How I (Claude) approached it — reasoning, step by step:**
1. No memory existed yet for this project directory (checked `MEMORY.md` — didn't exist), so there was no shortcut; I had to reconstruct state from the ground truth.
2. Explored the working directory (`ls`), found the `Project/` subfolder was the actual git repo (the parent `Systems Thinking` folder is not a repo).
3. Ran `git log --oneline` and `git status` in parallel with directory listings of `deliverables/`, `report/`, `tools/`. `git log` immediately gave a highly detailed history (see Section 4 above, reconstructed from these same messages). `git status` revealed the uncommitted state described in "Session: 2026-09-07" above: a delete+rename of the merged PDF, two modified `.docx` files, one untracked new PDF.
4. To figure out *what* had changed in the two modified `.docx` files (binary diff is useless), I extracted both the git-committed (`HEAD`) version and the working-tree version to plain text via `pandoc … -t plain` and ran `diff`. This is what surfaced: a newly-added (but, it turned out, stale/frozen) Table of Contents, and a dropped "Source"/date column from two evidence tables.
5. Confirmed the renamed PDF (`Invictus_Phase1.pdf`) was byte-identical to the deleted `Phase 1 - All Five Deliverables (Merged).pdf` (same file size) — a pure rename, not a content change.
6. Checked file modification timestamps precisely (`ls -la` with full timestamps): the two edited `.docx` files were modified at 23:51, **twelve minutes after** their corresponding PDFs were generated at 23:39 — proof the PDFs were now stale relative to the docx content, not merely different by chance.
7. **Decision point — asked the user rather than guessing** (via `AskUserQuestion`, two questions): (a) whether to regenerate the two stale PDFs, just report the diff, or leave them as-is; (b) whether the merged `Invictus_Phase1.pdf` should also be regenerated to reflect the docx edits, or left untouched. **User answers:** regenerate the two stale PDFs (recommended option); leave `Invictus_Phase1.pdf`'s content untouched (do not regenerate the merge). This scoped the rest of the session precisely: only `Process Trace.pdf` and `System Timeline BOT Map.pdf` needed new work.

**Technical pass 1 — naive regeneration, and why it wasn't good enough:**
8. Checked what conversion tools existed on the machine: `pandoc` and `tectonic` were both present (`which pandoc tectonic`); no script or Makefile existed anywhere in the repo encoding the exact pipeline used on 2026-09-06 — that session's exact commands were never saved anywhere, only their *effects* (the committed PDFs) and a prose description in the commit message.
9. First attempt: `pandoc "Process Trace.docx" -o out.pdf --pdf-engine=tectonic` (the simplest possible invocation matching the commit message's "LaTeX-typeset via pandoc+tectonic, directly from the current .docx files"). This produced a PDF, but:
   - **Mistake/bug found #1:** it was **11 pages**, versus the previously-committed version's **8 pages**, for what should have been very similar content (same doc, minus one table column, plus a TOC block). This size mismatch was the first sign something about the pipeline wasn't being reproduced faithfully.
   - I rendered pages to PNG (`pdftoppm`) and visually inspected them (via the `Read` tool's image support). **Mistake/bug found #2, the important one:** a flowchart diagram ("Daily Attendance-Decision Cycle") that fit cleanly on one page in the already-committed, official PDF was **overflowing off the bottom of the page** in my naive regeneration — the last node ("Billed by registration count...") was clipped, and the figure's caption and page number were missing entirely because the image had pushed them off the page.
   - I confirmed this wasn't a pre-existing/acceptable defect by regenerating the *old* (pre-edit) docx with the same naive command and comparing: same clipping bug appeared there too (12 pages vs. the real committed file's 8), proving my plain command was **not** equivalent to whatever pipeline actually produced the committed PDFs — there had to be image-fitting logic in the original session that was never written down.
10. **Root cause and fix, iteration 1:** LaTeX's default `\includegraphics` (from `graphicx`, which pandoc uses) doesn't constrain an image to fit within the remaining space on a page — it just inserts it at whatever size the source specifies. I wrote a LaTeX header snippet (`fit-images.tex`) redefining `\includegraphics` to route through the `adjustbox` package's `max width`/`max height`/`keepaspectratio` keys, passed via `--include-in-header` to pandoc.
    - **Mistake #3:** first version errored out — `Package xkeyval Error: 'max width' undefined in families 'Gin'` — because plain `\includegraphics` (the `graphicx` `Gin` key family) doesn't understand `adjustbox`'s keys unless you either load `adjustbox` with its `export` option, or call `\adjincludegraphics` directly. **Fix:** redefined `\includegraphics` to call `\adjincludegraphics` instead of `\includegraphicsold`.
    - **Mistake #4:** with that fixed, the build succeeded, but the image was still overflowing — no visible change. **Root cause:** the pandoc-generated `\includegraphics[width=…,height=…]{…}` call already carries an explicit, absolute `height` from the docx's own image sizing; my `max height` key was listed *before* that explicit height in the merged key list, and in LaTeX key-value processing, keys are applied left-to-right, so the later explicit `height=` silently overrode my earlier `max height=` constraint. **Fix:** reordered the key list so my constraints (`max width`, `max height`, `keepaspectratio`) come *after* the pass-through of the original keys (`#1`), so mine win.
11. Re-ran; confirmed visually (rendered every page, read every image) that the diagram now fit correctly on its page with caption and page number intact — matching the quality bar of the already-committed original.

**Technical pass 2 — the "fix everything, not just make it work" decision, and a second real bug:**
12. Having gotten the PDFs to a reasonable state, I rendered and visually inspected *every single page* of both regenerated PDFs (not just the one known problem page) — this is a general practice worth naming: **verify PDF/diagram output by actually rendering to images and looking, not by trusting exit codes or page counts alone.**
13. While doing that inspection, I noticed the newly-added Word Table of Contents in both documents showed **the literal digit "1" next to every single entry** — every section, regardless of its real page number. **Diagnosis:** Word's TOC is a "field" that caches page numbers at the moment it's last refreshed (via Word's "Update Field"); if you insert a TOC and save without ever triggering that refresh, every entry keeps whatever placeholder/initial value Word wrote, which in this case was uniformly "1." Pandoc doesn't understand Word TOC fields as fields at all — it just flattens the field's cached text into plain paragraphs, so this defect passes straight through into any PDF built from the docx as-is.
14. **Decision point — flagged to the user rather than silently "fixing" it by guessing real page numbers.** I could not know the user's intended page numbers without recomputing them myself, and doing so myself and calling it "the TOC" would have been fabricating certainty (violates the same discipline the project itself keeps applying to its own research findings — see D-8/D-9/D-11). Asked the user directly (`AskUserQuestion`): regenerate with a proper, pandoc-native, accurate, hyperlinked TOC, or leave the broken one as-is. **User chose: regenerate with a proper TOC.**

**Technical pass 3 — building the native-TOC pipeline, and a third real bug:**
15. To get pandoc to generate its own accurate TOC, I needed to (a) strip the stale, hand-typed TOC block out of the source content, and (b) pass `--toc` on a *content* pandoc run rather than a direct docx→PDF run (pandoc's native `--toc` flag works the same way regardless of input format, but I needed to edit the content first, which meant going through an editable intermediate).
16. Converted each `.docx` to **standalone Markdown** (`pandoc … -t markdown --standalone`), which captures the docx's core-properties (`title`, `subtitle`) as YAML front matter — needed because the title page text ("Current-State Process Map / Process Trace" / "IIIT Hyderabad Breakfast Mess System") turned out to live in docx *metadata*, not in the document body text, and would otherwise have been silently lost by going through a markdown round-trip.
17. Wrote a small Python script to programmatically strip the stale TOC block: find the line starting `# Table of Contents`, delete through (but not including) the next top-level `# ` heading. Ran it on both documents.
18. Re-ran pandoc from the cleaned Markdown with `--toc -V toc-title="Table of Contents"` plus the same image-fitting header from pass 1.
    - **Mistake #5:** images failed to resolve (`Could not fetch resource media/image1.png`). **Root cause:** `pandoc --extract-media=DIR` nests the extracted files one level deeper than expected — a docx-internal path of `media/image1.png` gets extracted to `DIR/media/image1.png`, so when the markdown itself *also* says `media/image1.png` relative to some resource path, you need `--resource-path=DIR/media` (not `DIR`) so that `DIR/media` + `media/image1.png` resolves to the real `DIR/media/media/image1.png`. **Fix:** corrected `--resource-path`.
    - **Mistake #6, the more serious one:** once images resolved and the build succeeded, the native TOC now had *correct, non-"1" page numbers* — but visually inspecting every page again, I found **Figure 2 ("Daily Attendance-Decision Cycle") had drifted from page 4 (where it belonged, right after the paragraph that introduces it) to page 7**, several sections later. **Root cause:** going through the Markdown intermediate makes pandoc emit LaTeX images inside standard floating `figure` environments, and LaTeX's float placement algorithm is free to defer a float to wherever it next finds room — which, combined with the `adjustbox`-constrained sizing, pushed this particular figure several pages down the document, disconnecting it from its surrounding narrative. This hadn't happened in pass 1 because that was a *direct* docx→PDF conversion (pandoc's docx reader apparently doesn't route images through the same floating mechanism, or does so in a way LaTeX resolves differently) — the round-trip through Markdown was the specific trigger. **Fix:** added `\usepackage{float}` + `\floatplacement{figure}{H}` to the shared header, forcing every figure to render exactly where it appears in the source ("here," not floated), at the cost of occasionally awkward-but-acceptable page breaks — which the existing `max height` constraint from pass 1 already keeps from overflowing a page.
19. Re-verified: rendered and read every page of both final PDFs again. Confirmed all figures now sit in their correct in-sequence position with working captions and page numbers, confirmed the TOC page numbers are now accurate, and did a final content sanity pass (sorted, page-number-stripped text diff between this version and the pass-1 version) to make sure no prose content had been lost or duplicated in the process — differences found were only line-wrap reflow artifacts from different table column widths, not real content changes.

**Finishing — metadata, fingerprint scan, placement, git:**
20. Stripped tool-fingerprint PDF metadata using `pypdf` (`PdfReader`/`PdfWriter`, `writer.add_metadata({...})`), keeping the document's real `Title` but blanking `Author`, `Subject`, `Creator`, `Producer` — replicating the exact policy established in D-13, since no `exiftool`/`qpdf`/`pikepdf` were available on this machine (checked; only `pypdf` was installed).
21. Ran the same tool-fingerprint text scan as the 2026-09-06 session (`pdftotext … | grep -iE "pandoc|tectonic|xdvipdfmx|xetex|claude|anthropic|chatgpt|ai-generated"`) — clean, zero hits, on both files.
22. Copied the two final PDFs over the stale ones in `deliverables/phase-1/`.
23. **Decision point on git — asked before touching anything:** confirmed with the user (two more `AskUserQuestion` calls) whether to commit at all, and whether to push. **User's answers, verbatim intent:** commit, but **authored as themselves, explicitly not attributed to Claude** ("chat with sricharanperi (me) as the commitor, not under the name of claude"); and yes, push to `origin/main`.
24. **Decision D-14 — this is a deliberate, explicit override of my own default behavior.** My harness's standing instruction is to append a `Co-Authored-By: Claude …` / `Claude-Session: …` trailer to every commit I make. The user directly instructed otherwise for this commit, and per that instruction's own stated precedence rule ("the user's own instructions about these lines... take precedence over this reminder"), I honored the user's instruction: the commit `0b83c06` carries no Claude attribution at all, authored purely as `sricharanperi <sricharanperi27@gmail.com>` (which was already the configured git identity in this repo — verified via `git config user.name`/`user.email` before committing, not assumed). **This is consistent with the broader AI-fingerprint-scrubbing policy (D-13) — the user does not want this repo's visible history/authorship to read as AI-assisted**, which is important context for any future session: **do not add Claude attribution to commits in this repo unless the user asks for it in that specific instance.**
25. Committed (`0b83c06`, message: "Rename merged Phase 1 PDF for submission and fix TOC in two deliverables") and pushed. `git push` succeeded cleanly: `3885a3c..0b83c06  main -> main`.

**Then — this file:**
26. The user asked for exactly the document you're reading now: an exhaustive, continuously-updated, single-source-of-truth master context file covering every decision, every pass, all research, mistakes, thought process, and enough detail that another agent/account could resume cold.
27. **Decision D-15, made by asking rather than assuming, given a real tension:** the user had *just* asked me to scrub AI-authorship from commits and PDFs (D-14, D-13) — a document that narrates "how the agent thought" and "how subagents were created" in loving detail is in direct tension with that, if it's tracked and pushed to the same GitHub repo. I surfaced this tension explicitly and asked two questions: (a) where should this file live — gitignored-but-in-repo, committed-and-pushed, or entirely outside the repo; (b) how should pre-2026-09-12 history (reconstructed from git log, not a lived transcript) be represented — flagged as reconstructed, or written identically to directly-observed sessions. **User's answers:** commit and push it (i.e., it's fine for *this specific file* to be AI-transparent even though the submitted deliverables aren't — the scrubbing policy applies to the graded artifact, not to this project-management file); and write reconstructed history with the same level of confidence/detail as directly-observed history, no hedging distinction. Both are reflected in how this file is written and in Section 0's maintenance instructions above.
28. Wrote this file (`MASTER_CONTEXT.md`) at the repo root. **Next action after writing:** commit and push it, same as any other significant change, per the instruction in Section 0.

**Agent/tooling notes for this session specifically:**
- No subagents (`Agent` tool) were spawned during this session. Every investigative and technical step above was done directly, in the main conversation thread. Rationale: none of the sub-tasks were independent enough to parallelize usefully (each pandoc/tectonic debugging step depended on the visual result of the previous one), and none produced large enough intermediate output to justify off-loading into a fork purely to save context. If a future session needs to, e.g., regenerate PDFs for *all five* deliverables in parallel, or run an independent second opinion on a finding, spawning parallel forks or fresh subagents would be the right call then — this session just didn't have that shape of work.
- Heavy use of direct visual verification via the `Read` tool's image support (rendering PDF pages to PNG with `pdftoppm`, then reading them as images) rather than trusting text-only signals like page counts or LaTeX warnings alone. This was the single most load-bearing technique in the whole session — every real bug found (the clipped diagram, the frozen TOC numbers, the drifted figure) was caught by looking at rendered pages, not by reading logs.
- `AskUserQuestion` was used four times this session, each at a genuine decision point where guessing would have meant either fabricating certainty (TOC page numbers) or making an irreversible/visible choice on the user's behalf (whether to touch the merged submission PDF, whether/how to commit and push, where this very file should live). This matches the project's own long-standing internal discipline (D-8, D-9, D-11) of not inventing certainty — applied here to the *process* of working on the repo, not just to its research content.

### Session: 2026-09-12 (Phase 2 kickoff, by teammate) + pull/review pass (by this session)
**Commit:** `b7c69ac` "task 6,7 with pending interview" — **By:** neha771 <nehasusan369@gmail.com>, pushed directly to `origin/main` at 14:45 that day (after this session's own `882cc72` MASTER_CONTEXT.md commit, so it was never seen locally until fetched). No commit body, no Claude-Session trailer — can't tell from the commit alone whether this was done with AI assistance or not.

**User's request this pass:** "Pull everything from the repo regarding the changes done by the other team members, understand what has been done, and update everything into the new thing and also into MASTER_CONTEXT.md."

**What I (Claude) did:**
1. `git fetch origin`, then compared `git log --oneline -1` (local) against `origin/main` — found one commit ahead (`b7c69ac`) not yet pulled.
2. `git log 882cc72..origin/main` to read the commit message before pulling anything, then `git pull --ff-only` (fast-forward only, deliberately — no merge commit needed since local had no divergent work).
3. `git show --stat b7c69ac` to see the full file list, then read both new markdown files in full and viewed the two newly-drawn diagram images (`diagram1-system-map.png`, `diagram2-underprovisioning-loop.png`) to actually understand the content, not just infer from filenames.
4. Confirmed via `git branch -a` there's only ever been a single `main` branch in this repo's history — no stray unmerged branches to also account for.

**What Phase 2 (Tasks 6-7) actually contains — understood from reading the files directly:**

**Task 6 — System Map (`06-system-map.md`).** Explicitly framed as a *synthesis*, not new research: "Everything below is built from facts already confirmed in Tasks 1-5. No new claim is introduced here." Section headers again follow the assignment framework's own wording (continuing D-7): Map Actors/Processes/Information/Resources/Constraints; Identify Conflicts and Dependencies; Represent Formal and Informal Structures; Highlight Bottlenecks, Tensions and Feedback Loops; Key Findings; Outstanding Data Collection. It lays the full system out as one flow diagram (`assets/diagram1-system-map.png`, newly drawn — actors, registration→billing→vendor forecast→service window→outcome, with three explicit bottleneck callouts and the Academic-administration disconnect shown as a red dashed line) plus the reused Phase 1 "Power and Information Flow Network" diagram. Names three concrete bottlenecks (the 4-day procurement lead time; the 9:30 AM close; zero formal channel between Academic administration and any mess-governance actor) and states the core synthesis finding plainly: every no-show exit path (cancel, Skip Meal, resale, waste) is a workaround for the same missing mechanism — nothing lets a same-day intent change affect billing or cooking.

**Task 7 — Systemic Problem Analysis (`07-systemic-problem-analysis.md`).** A classic events→patterns→structures→mental-models iceberg analysis, again headers matching the framework's wording: Distinguish Events, Patterns, Structures and Mental Models; Identify Reinforcing and Balancing Feedback Loops; Analyse Unintended Consequences; Identify Structural Causes and Systemic Tensions; Key Findings; Outstanding Data Collection.
- Explicitly labels the **mental-models layer as inference**, not fact — "none directly stated by name in any interview but consistent with everything observed" — the same "don't invent certainty" discipline as D-8/D-9/D-11, now applied to a new kind of claim (inferred beliefs, not just missing data).
- Names four loops: **R1 — Shifting the Burden via Mess Cell** (reinforcing; reuses Phase 1's `d10-loop-r1.png`), **B1 — Kitchen Waste Control via Skip Meal** (balancing but incomplete — flags that Skip Meal's zero real usage means it may not be closing the loop even on the kitchen's own terms, a sharper version of a Phase 1 finding; reuses `d11-loop-b1.png`), **B2 — Capacity Redistribution** (weak/broken — Kadamba doesn't organically redistribute to Bakul/Palash; capacity was instead added administratively by building Bakul), and a **candidate structure, not yet a confirmed loop** — under-provisioning for real attendees (new diagram, `diagram2-underprovisioning-loop.png`), explicitly split into an evidenced first half (inflated registration vs. low true attendance) and an unconfirmed second half (whether kitchen prep is actually calibrated to the low true-attendance figure rather than peak-hour demand).
- An unintended-consequences table covering five rules/actions, including a sharp new claim: the December 2024 cancellation-cap tightening (originally a Mess Office workload-reduction move, per Phase 1) "plausibly increases, not decreases, the pattern of uncancelled no-shows it targeted" — a fix that may be working against its own goal.
- Three structural root causes named directly: (1) billing decoupled from attendance — the single structure behind the largest share of symptoms; (2) the four-day procurement lead time as a fixed ceiling on system responsiveness, "not a policy choice any single actor is making badly"; (3) governance fragmented across four disconnected actors (Mess Committee, Mess Office, Warden, and functionally Academic administration), none of which holds both the authority and the incentive to fix the core mismatch end-to-end.
- Two systemic tensions named: individual rationality vs. system-level cost (everyone's individually-sensible choices sum to the paradox — "no single actor is behaving irrationally"), and administrative simplicity vs. demand-matching.

**Outstanding Data Collection (both Task 6 and Task 7):** both explicitly say the mess-committee/vendor interview is **pending institutional approval** — this is a firmer, more specific status than Phase 1's more general "will be collected and submitted later" language, and it's the same single pending interview referenced by both new documents (not two separate gaps). See Section 9.

**Decisions/patterns confirmed as continuing into Phase 2 (not new decisions, but worth recording that they held):**
- Phase 2 reuses D-7 (section headers match the assignment framework's own wording) and D-9/D-12 (explicit "Outstanding Data Collection" closing section) without any prompting from this session — evidence these are now settled team conventions, not just this-session choices.
- Phase 2 explicitly re-applies D-11's inference-vs-fact discipline to a new domain: labeling the entire "mental models" layer of an iceberg analysis as inferred rather than confirmed, and explicitly splitting the under-provisioning loop into its evidenced half vs. its unconfirmed half rather than presenting it as one settled loop.
- Diagram reuse pattern continues: three Phase 2 diagrams are literal copies of Phase 1 assets (`d10-loop-r1.png`, `d11-loop-b1.png`, `d14-power-flow-network.png`) rather than redrawn — same pattern already noted for `report/figures/` vs. `deliverables/phase-1/assets/` (Section 3's cross-reference notes, Section 9's open item about the two figure sets not being automatically linked). **This is now a three-way duplication** (Phase 1 assets / report figures / Phase 2 assets) worth watching if any of these diagrams ever need a correction.

**What I did *not* do this pass:** no docx/PDF conversion, no edits to the Phase 2 markdown content itself, no changes to Phase 1 files. This was purely a pull-and-document pass — the user's request was to understand and record what teammates had done, not to build on it yet. If the next ask is "now build the docx/PDF for Tasks 6-7," the playbook in Section 5 applies directly (Phase 2 docs currently have no Word-TOC or embedded-infographic complications like Phase 1 did, so the simple direct route in 5.1 is the likely starting point — check for a Word-authored TOC field first per 5.2's checklist regardless).

---

## 5. TECHNICAL PLAYBOOK — the docx→PDF pipeline (reusable recipe)

This is the exact, working recipe for turning a `deliverables/phase-1/*.docx` file into a submission-quality PDF, as of 2026-09-12. Read this before touching the pipeline again — it encodes three real bugs' worth of hard-won fixes.

**Tools available on this machine (verified 2026-09-12):** `pandoc`, `tectonic`, `pdftoppm`/`pdftotext`/`pdfinfo` (poppler-utils), Python 3 with `pypdf` installed. **Not available:** `exiftool`, `qpdf`, `pikepdf`, `PyPDF2`. Check again before assuming any of this if picking this up much later — the machine's tool set can change.

### 5.1 If the docx has no stale/broken Table of Contents
Simple, direct conversion:
```
pandoc "Document.docx" -o "Document.pdf" --pdf-engine=tectonic --include-in-header=fit-images.tex
```
This alone fixes image overflow (see 5.3) but does **not** add a table of contents — pandoc's docx reader flattens any Word TOC field into plain text as-is, whatever it currently says.

### 5.2 If the docx has a Word Table of Contents field (check first: does every entry show the same page number, e.g. all "1"? If so, it's stale/unrefreshed and must not be trusted or shipped as-is)
1. Extract to standalone Markdown, preserving title/subtitle metadata and extracting images to a known folder:
   ```
   pandoc "Document.docx" -t markdown --standalone --extract-media=OUTDIR -o doc.md
   ```
2. Strip the stale TOC block: find the line `# Table of Contents {#table-of-contents .TOC-Heading}` and delete everything from there up to (not including) the next top-level `# ` heading. (A short Python script does this reliably — see the session log above for the exact logic: scan for the first line starting with `# Table of Contents`, then scan forward for the next line matching `^# `, delete the span between.)
3. Convert the cleaned Markdown to PDF with a **native** TOC and the image/figure fixes below:
   ```
   pandoc doc.md -o "Document.pdf" --pdf-engine=tectonic --toc -V toc-title="Table of Contents" \
     --include-in-header=fit-images.tex --resource-path=OUTDIR/media
   ```
   Note the `--resource-path` points at `OUTDIR/media`, **not** `OUTDIR` — `--extract-media=OUTDIR` nests files one level deeper than you'd expect (`OUTDIR/media/media/imageN.png` for a docx-internal path of `media/imageN.png`), and the resource path needs to combine with the markdown's own `media/imageN.png` references to land on the real location.

### 5.3 `fit-images.tex` — the header-include that fixes image overflow and figure drift
```latex
\usepackage{float}
\floatplacement{figure}{H}
\usepackage{adjustbox}
\let\includegraphicsold\includegraphics
\renewcommand{\includegraphics}[2][]{\adjincludegraphics[#1, max width=\linewidth, max height=0.85\textheight, keepaspectratio]{#2}}
```
Two independent fixes bundled together, **both required** whenever converting through the Markdown-intermediate route (5.2); only the `adjustbox` half is needed for the direct route (5.1):
- **`float` + `\floatplacement{figure}{H}`:** forces every figure to render exactly in place ("here") instead of floating away to wherever LaTeX finds room — without this, a figure can drift several pages from its caption/surrounding text when converting via the Markdown intermediate.
- **`adjustbox` override of `\includegraphics`:** constrains every image to fit within the page's remaining width/height, preserving aspect ratio, so a tall diagram can never overflow off the bottom of a page. Two things about this specific override are easy to get wrong (both were gotten wrong once, on 2026-09-12):
  - You must route through `\adjincludegraphics`, not plain `\includegraphics` with `adjustbox`'s `export` option — plain `\includegraphics` doesn't understand `max width`/`max height` keys without the reroute.
  - **Key order matters.** The original pandoc-generated call already carries explicit `width=`/`height=` from the docx's own image sizing. Your `max width`/`max height` constraints must be listed **after** the pass-through of those original keys (`#1`), because LaTeX key-value parsing applies keys left-to-right and a later explicit `height=` silently overrides an earlier `max height=`.

### 5.4 Metadata stripping (AI-fingerprint scrubbing — standing policy since 2026-09-06, D-13)
Every PDF this project submits has its tool-fingerprint metadata blanked before being considered final, using `pypdf` since no other metadata tool was available:
```python
from pypdf import PdfReader, PdfWriter
reader = PdfReader(src)
writer = PdfWriter()
writer.append(reader)
title = reader.metadata.title if reader.metadata else None
writer.add_metadata({"/Title": title or "", "/Author": "", "/Subject": "", "/Creator": "", "/Producer": ""})
with open(dst, "wb") as f:
    writer.write(f)
```
**Keep `/Title`** (it's the document's real title, e.g. "Current-State Process Map / Process Trace" — not a tool fingerprint). **Blank `Author`, `Subject`, `Creator`, `Producer`** — these are the fields that otherwise leak `LaTeX via pandoc` / `xdvipdfmx (0.1)` etc.

After stripping, always run a final text+metadata scan for residue:
```
pdftotext "Document.pdf" - | grep -iE "pandoc|tectonic|xdvipdfmx|xetex|claude|anthropic|chatgpt|ai-generated|synthetic pilot"
```
Expect **zero** hits before considering a PDF submission-ready. (`synthetic pilot`/`persona` methodology language is included because the 2026-09-06 session specifically decided that language becomes residue once real data supersedes it — see D-13 — not because it's a tool fingerprint per se; use judgment on whether that specific phrase still applies to whatever document you're scrubbing.)

### 5.5 Verification discipline (don't skip this)
Every conversion pass in this project's history that shipped a real defect (the 2026-09-06 session's five listed bugs; the 2026-09-12 session's three) was caught by **rendering pages to images and looking at them**, not by trusting pandoc/tectonic exit codes, page counts, or warning text alone:
```
pdftoppm -png -r 90 "Document.pdf" outprefix
```
then read the resulting PNGs. Check specifically: does every figure have its caption and page number visible (not clipped)? Is the figure positioned near the text that introduces it, not drifted pages away? Does the TOC (if any) show real, distinct page numbers, not a repeated placeholder? Do table columns fit inside the page margins without visibly bleeding past them?

---

## 6. RESEARCH INVENTORY

**Phase 2 (Tasks 6-7) introduces no new research sources** — both documents draw exclusively on the primary research already listed below plus the confirmed findings already written into Phase 1's deliverables (D-16). The one still-pending source relevant to Phase 2 is the mess-committee/vendor interview, awaiting institutional approval (Section 9).

**Primary research (the project's actual evidence base):**
- `research/primary-research/interviews/2026-09-03_student-self-account-and-mess-system-overview.md` — the original respondent, a habitual skipper, general system informant (interviewed 2026-09-03).
- `research/primary-research/interviews/2026-09-06_five-student-interviews-guide1.md` — five more real students (2 daily eaters, 3 skippers), interviewed 2026-09-06 using Guide 1. This is the project's core quantitative-ish evidence base for Activities 4 and 5.
- `research/primary-research/interviews/student_interview_transcpirt_neha.md` and `student_interview_summary_neha.md` — neha771's independent transcription and synthesis of the same five interviews, used as a cross-validation source (see D-10, D-11).
- `research/primary-research/screenshots/` — portal screenshots of registration UI, meal capacities, rates, and edit-registration flows, used as ground truth for how the registration/billing mechanism actually works (not self-reported). Filenames are dated by the calendar date **shown inside** the screenshot's UI content, which can postdate the commit that added the file — don't assume the filename date is the capture date.
- `research/primary-research/team-contributions/2026-09-05_teammate-constraints-edge-cases-verticals.md` — a teammate's independently authored hypothesis/verticals document, kept verbatim (D-4).
- Two rounds of **synthetic (AI-simulated) pilot interviews** (`research/methodology/prathyusha_synthetic-pilot-interviews.md`) — explicitly non-ground-truth, used only to stress-test interview guide wording before running real interviews (D-2). Never cited as findings; explicitly flagged as weaker/removed once real data exists (D-13).

**Secondary research / methodology reading (folded into the interview standard and analysis approach, not cited directly in deliverables per D-5):**
- Erika Hall, *Just Enough Research*
- Nunnally & Farkas, *UX Research: Practical Techniques*
- Dumas & Loring, *Moderating Usability Tests*
- King, Churchill & Tan, *Designing with Data*
- Sterman, *Business Dynamics: Systems Thinking and Modeling* (added as a reference text 2026-09-05)
- Senge, *The Fifth Discipline* and *The Fifth Discipline Fieldbook* (`research/book-notes-fifth-discipline*.md`)
- Design Thinking Toolbox worksheets (`research/dt-worksheets/`) — the direct source of the Stakeholder Map's template structure (D-7)
- A larger set of HCI/UX textbooks (Buxton, Carroll, Becker, Constantine, Tidwell, etc.) present on disk as research input but **excluded from git** as copyrighted material not ours to redistribute (D-1) — see `.gitignore`.

**Reference frameworks:**
- `project_framework .pdf` — the assignment's own methods framework; every deliverable's section structure is written to match this document's own activity/method wording (D-7, recurring).
- `Courses-Syllabus_M26-V1.pdf` — course syllabus (lives in the parent folder, outside the git repo).

---

## 7. DECISION LOG (flat index, cross-referenced to Section 4 for full context)

| ID | Decision | Session |
|---|---|---|
| D-1 | Exclude copyrighted reference book PDFs from git via `.gitignore`, even though used as research input | 2026-09-03 |
| D-2 | Synthetic/AI-simulated interview data is explicitly marked non-ground-truth, never treated as a finding | 2026-09-05 |
| D-3 | Split Context Brief "Purpose" into true purpose / actual mechanism / gap between them | 2026-09-05 |
| D-4 | Preserve teammate research verbatim in its own file, not just paraphrased conclusions | 2026-09-05 |
| D-5 | Deliverable prose: no hedging, no citations, no process narration — direct factual statements only; drafts with narration archived, not deleted | 2026-09-05 |
| D-6 | Working/raw files get consolidated into one polished deliverable; redundant intermediates removed and cross-references fixed | 2026-09-05 |
| D-7 | Deliverable structure follows the assignment's own method-toolbox templates (`project_framework .pdf`, DT Toolbox), not ad hoc structure | 2026-09-05 |
| D-8 | Open research questions logged and left explicitly unanswered rather than guessed at | 2026-09-06 |
| D-9 | Split Activities 4/5 into "established now" vs. "completion plan for unobserved side"; standardized "Outstanding Data Collection" closing section | 2026-09-06 |
| D-10 | Cross-validate independent readings of the same raw data; adopt corrections where the other reading is better supported | 2026-09-06 |
| D-11 | Flag genuine source-data ambiguity explicitly rather than silently guessing a resolution | 2026-09-06 |
| D-12 | Standardize "Outstanding Data Collection" as a closing section across Tasks 3–5 | 2026-09-06 |
| D-13 | Standing AI-fingerprint-scrubbing policy: blank PDF tool metadata (keep Title), remove now-superseded synthetic-pilot language, scan final text for tool/AI residue — applies to every submitted PDF | 2026-09-06 |
| D-14 | This repo's commits do not carry Claude attribution unless the user asks for it in that specific instance — consistent with D-13's scrubbing policy | 2026-09-12 |
| D-15 | This file (`MASTER_CONTEXT.md`) is committed and pushed to the repo despite D-13/D-14, because it is a process/context document, not a submitted deliverable | 2026-09-12 |
| D-16 | Phase 2 (Tasks 6-7) built as a pure synthesis of Phase 1 findings, explicitly re-confirmed as introducing no new claims — same "don't invent certainty" discipline as D-8/D-9/D-11, now also applied to labeling an entire analysis layer (iceberg-model mental models) as inference rather than fact | 2026-09-12 (Phase 2 kickoff, by neha771) |

---

## 8. MISTAKES & ERRORS LOG (technical)

| # | Mistake | Root cause | Fix | Session |
|---|---|---|---|---|
| 1 | Stray unpopulated TOC heading/link block rendered into early PDFs | Word TOC field flattened to plain text by pandoc's docx reader | Stripped before typesetting | 2026-09-06 |
| 2 | Dropped Unicode "interrupted relationship" glyph in a diagram legend | LaTeX/font couldn't render the glyph | Replaced with LaTeX-safe "X" | 2026-09-06 |
| 3 | Duplicate "Onion Proximity Map" caption on a manually-added infographic | Caption inherited from the image above it during editing | Relabeled to accurate caption | 2026-09-06 |
| 4 | Leverage-quadrant chart title clipped | Mermaid `quadrantChart` title too long for its rendering | Shortened title, regenerated | 2026-09-06 |
| 5 | Provisional-timeline diagram sliced across a page break | Diagram too tall for one page in vertical layout | Rebuilt as horizontal (`LR`) layout | 2026-09-06 |
| 6 | Regenerated PDF was 11 pages vs. committed original's 8, with more LaTeX overfull-hbox warnings | Naive `pandoc --pdf-engine=tectonic` doesn't replicate whatever image-fitting the original session used (never saved as a script) | Investigated via page-image rendering; built explicit image-fit header (see #7 below) | 2026-09-12 |
| 7 | Flowchart diagram clipped off the bottom of its page, caption/page-number missing | LaTeX's default `\includegraphics` doesn't constrain to remaining page space | `adjustbox`-based `\includegraphics` override with `max width`/`max height`/`keepaspectratio` | 2026-09-12 |
| 8 | `adjustbox` header errored: `'max width' undefined in family 'Gin'` | Plain `\includegraphics` doesn't understand adjustbox keys without rerouting | Redefined `\includegraphics` to call `\adjincludegraphics` | 2026-09-12 |
| 9 | Image still overflowed after adjustbox was wired in, no visible change | Explicit `height=` from the original pandoc call came *after* `max height=` in the merged key list, silently overriding it (LaTeX key-value is left-to-right) | Reordered keys so constraints come after the pass-through of original keys | 2026-09-12 |
| 10 | Word TOC showed page "1" for every single entry | Word TOC field never refreshed ("Update Field") before the docx was saved; pandoc flattens the frozen field text as-is | Stripped the stale block; regenerated via pandoc's native `--toc` on cleaned Markdown | 2026-09-12 |
| 11 | Extracted images failed to resolve (`Could not fetch resource media/image1.png`) | `--extract-media=DIR` nests files one level deeper (`DIR/media/media/...`) than the markdown's own relative reference expects | Set `--resource-path=DIR/media` instead of `DIR` | 2026-09-12 |
| 12 | Figure 2 drifted from page 4 to page 7, disconnected from its introducing paragraph | Going through a Markdown intermediate causes pandoc to emit standard floating `figure` environments, which LaTeX is free to place wherever it finds room | Added `\usepackage{float}` + `\floatplacement{figure}{H}` to force in-place rendering | 2026-09-12 |

**Non-technical/process "mistakes" worth naming (source-data and research hygiene, not pipeline bugs):**
- A source-data labeling collision in the raw interview transcripts (two different files both labeling a respondent "Daily eater - 2") was caught by cross-transcription comparison, not assumed away (D-11).
- The "Mess Council" stakeholder was initially treated as a confirmed IIIT-H actor before independent verification revealed it was very likely a naming mix-up with a different institution (IIT Hyderabad) — corrected once checked against source, not left as an unverified assumption (2026-09-06 audit session).
- "Sleeping collective leverage" was stated as a finding, then overturned by a later-discovered precedent and relabeled "exercised-but-unmeasured leverage" rather than quietly edited without explanation (2026-09-06).

---

## 9. OPEN ITEMS (as of 2026-09-12, updated after pulling Phase 2 kickoff — check before assuming any of these are still open)

- **Mess-committee / vendor-side interview has not been conducted; is now specifically "pending institutional approval."** Every deliverable that touches governance or kitchen operations (Tasks 3, 4, 5, and now 6, 7) says so in its "Outstanding Data Collection" section — Phase 2's wording is more specific than Phase 1's ("will be collected and submitted later"), confirming it's the same single pending interview referenced everywhere, not several separate gaps. This is the single biggest acknowledged gap in the project's evidence base, and it now blocks two additional specific claims: (a) how a preparation quantity is actually decided and whether waste/shortfall data reaches a decision-maker (Task 6), and (b) whether kitchen prep is actually calibrated to low true-attendance rather than peak-hour demand — the unconfirmed half of the under-provisioning candidate loop (Task 7).
- **Phase 2 has no `.docx`/`.pdf` yet** — only the two markdown files and their diagram assets exist so far (`06-system-map.md`, `07-systemic-problem-analysis.md`). Whoever builds the Word/PDF versions should follow the Section 5 playbook and specifically check early whether Word's own TOC-field bug (Mistake #10) recurs, since these docs don't have that history yet to know either way.
- **Direct observation of a live breakfast service window has not been conducted**, despite a 30-minute-interval observation protocol (7:15/7:30 AM setup through post-close) being written and ready to run. Would resolve the unconfirmed exact shape/timing of the crowd-peak curve.
- **The true respondent count behind "Daily eater - 2" is unresolved** (see Mistake/finding above) — either a mislabeling or a genuinely missing sixth transcript; unverifiable without the original interview source re-checked directly with whoever conducted it.
- **The relationship between "Mess Council" and the Mess Committee remains unresolved**, compounded by the likelihood that "Mess Council" is a cross-institution naming mix-up rather than a real IIIT-H body — needs direct confirmation, not further inference.
- **The subject and outcome of the historically-referenced "organized student email effort"** is still the single highest-priority open governance question per the 2026-09-06 audit, with only a strong-but-unconfirmed candidate match found so far.
- **Whether the ~30% registration-to-attendance gap figure is accurate** is unverified — cited by two respondents but not confirmed against records.
- **No single population-level attendance trend exists** across the six real respondents (some rising, some falling, one flat at zero) — any future claim that "the paradox is worsening/improving" needs to specify for whom, not assert it generally. This is a standing caution for anyone extending this research, not a to-do item to resolve.
- **`report/` (the separate LaTeX write-up) has its own figure set** (`report/figures/`) that overlaps conceptually but is a distinct copy from `deliverables/phase-1/assets/` — if a diagram is corrected in one location, check whether the other copy needs the same correction; there is currently no automated link between them.
- **~~This `MASTER_CONTEXT.md` file itself needs to be committed and pushed~~ — done** (commit `882cc72`, 2026-09-12). Resolved.
- **Before pulling/pushing in future sessions, always check `origin/main` for teammate commits first** (`git fetch` + compare `git log -1` local vs. `origin/main`) — this session found a full day-old teammate commit (`b7c69ac`, Phase 2 kickoff) sitting unpulled on the remote simply because nothing had triggered a fetch since it landed. There is no other signal that surfaces a teammate's push automatically in this workflow.
