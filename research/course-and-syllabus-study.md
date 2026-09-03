# Course & Syllabus Deep Study — System Thinking and Design (Raman Saxena)

Compiled 2026-09-01 from `Courses-Syllabus_M26-V1.pdf` (pp.261-263), all lecture decks
(`Lecture 1,2,3.pdf`, `Lecture_4.pdf`, `Lecture_5.pdf`, `Lecture_6.pdf`, `Lecture_7 & 8.pdf`),
`ProblemStatements.pdf`, and `project_framework .pdf`.

## 1. Course identity

System Thinking and Design — Raman Saxena (PDM Program + Software Engineering Research
Centre, IIIT Hyderabad). 2 credits (L-T-P 1.5-0-3), 3rd Semester–Year 2. Prerequisites: Product
Management Foundations, Service Design, basic math (variables/rates of change/logic).

Objectives: see "the whole" not just the parts; identify leverage points in complex systems;
anticipate 2nd/3rd-order effects of product decisions.

## 2. Official 6-week lecture syllabus (teaching schedule, separate from the project's own 4-week cycle)

| Week | Unit | Topics |
|---|---|---|
| 1 | The Systems Lens | Reductionism vs. Holism; Elements, Interconnections, Purpose |
| 2 | Mapping Causality | CLDs; Reinforcing (R) / Balancing (B) loops; Delay |
| 3 | System Archetypes | Tragedy of the Commons, Shifting the Burden, Success to the Successful |
| 4 | Stocks, Flows & Dynamics | System Dynamics intro; Vensim / InsightMaker |
| 5 | Leverage Points | Where to intervene; designing for emergence; wicked problems |
| 6 | Systems in Practice | Platform ecosystems (UPI, Amazon); socio-technical systems; ethics |

Named case studies (per syllabus, not yet seen in lectures 1-8): UPI ecosystem, Climate
Change & Policy via the EN-ROADS simulator, "The Cobra Effect." Also: the Beer Game
simulation (Bullwhip Effect), and the Iceberg Model applied to every product-failure discussion
as a running technique (not a standalone week).

## 3. Assessment — CONFIRMED authoritative figures (per user, 2026-09-01)

Lecture 3's own slide is the real, in-force grading scheme — not the syllabus PDF's 20/30/40/10
table (that document is a filed template; the numbers below are what was actually announced
in class and confirmed by the student):

| Component | Marks |
|---|---|
| Individual Assignments | 20 |
| Quiz | 10 |
| Project | 60 (+10 bonus) |

Grading basis: **Relative** (per Lecture 3). Project specifics from Lecture 6: **team size = 3
members**, **duration = 4 weeks**. The "Project" line is the syllabus PDF's "Capstone:
Intervention" — identify a wicked problem, design a systemic intervention with 3rd-order
effect analysis — i.e. the "Pick Your Puzzle" project.

(The syllabus PDF's 20/30/40/10 System Audit / Modelling Lab / Capstone / Active Synthesis
breakdown should be treated as superseded by the above for this cohort.)

## 4. What's been taught so far (Lectures 1-8) vs. what's still ahead

**Covered:** Week 1 (Systems Lens: reductionism/holism, elements/interconnections/purpose,
structure-drives-behavior via the Slinky demo, "embedded in a larger system" feedback
diagram, wolf-deer-grass food chain example) + the Iceberg Model (taught as a running
technique, Lectures 4-5, applied to a Hyderabad traffic-flyover case study) + Week 2 (Causal
Loop Diagrams: R/B loop definitions, worked examples — Food Delivery App Discounts, Traffic
Congestion, Exam Pressure) + supplementary software/systems-engineering material (Black
Box concept, Emergence, a lemonade-stand analogy for load balancing/caching/sharding).

**Not yet covered (still ahead per the 6-week syllabus):** System Archetypes by name (Week 3:
Tragedy of the Commons, Shifting the Burden, Success to the Successful, Fixes that Fail),
Stocks-and-Flow modeling + Vensim/InsightMaker tooling (Week 4), the formal Leverage Points
framework — Meadows' 12 points (Week 5, needed for the project's own Phase 3), Systems in
Practice / platform ecosystems (Week 6), and the UPI/EN-ROADS/Cobra Effect case studies +
Beer Game.

**Pacing note:** lecture content lines up with project deadlines — Iceberg Model (Lectures 4-5)
lands right before the project's Week 2 "Dig Deeper" deliverable; CLDs (Lectures 6-8) land
right before the project's Week 3 "Connect the Dots" deliverable. Expect a Leverage Points
lecture before the project's Week 4 deliverables are due.

## 5. Reference books — official list + how slides actually cite them

Syllabus reading list:
1. *Thinking in Systems: A Primer* — Donella Meadows
2. *The Fifth Discipline* — Peter Senge (learning organizations)
3. *Systemic Design: Theory, Methods, and Practice* — Peter Jones & Kyoichi Kijima (not yet
   surfaced in any lecture through Lecture 8 — likely feeds Week 6, given its socio-technical/
   service-ecosystem focus)

Explicit in-slide citations found:
- Donella Meadows, *Thinking in Systems* — system definition (Lecture 1-3)
- Wikipedia — "Systems Theory" article — alternate system definition (Lecture 1-3)
- "The Donella Meadows Project" — source of the Iceberg Model (Lecture 4)
- ***The Fifth Discipline Fieldbook*** (Senge, Kleiner, Roberts, Ross & Smith) — CLD definition
  (Lecture 6). Note: this is a *different, companion* book to "The Fifth Discipline" on the
  official reading list — same Senge-led team, distinct title. Worth citing precisely if asked.

Uncited but clearly sourced content:
- "Elements / Interconnections / Purpose" triad (Lecture 1-3) — verbatim Meadows' own
  framework, Ch.1 of *Thinking in Systems*, not attributed on the slide.
- Slinky "structure drives behavior" demo — classic device from the Waters Foundation /
  *The Systems Thinking Playbook* tradition (Meadows & Linda Booth Sweeney).
- Traffic-jam "purpose ≠ stated goal of parts" argument — Meadows-style reasoning, uncited.
- "Embedded in a larger system" feedback diagram — structurally the classic System Dynamics
  decision-maker-in-a-feedback-loop figure (MIT/Forrester-Sterman lineage, cf. Sterman's
  *Business Dynamics*), uncited.

Original/instructor-authored, not book-sourced: Hyderabad SRDP flyover case study; the three
CLD worked examples (food delivery discounts, traffic congestion, exam pressure); Black Box /
Emergence / lemonade-stand system-design analogy.

## 6. Project framework, reconciled

`ProblemStatements.pdf` gives the simple week story (Week 1 Understand → Week 2 Dig Deeper/
Iceberg → Week 3 Connect the Dots/CLD → Week 4 Solution & Share, deliverables released each
Monday). `project_framework .pdf` is the granular 10-activity / 15-deliverable breakdown of
that same arc — see the `systems-design-toolkit` skill (`.claude/skills/systems-design-toolkit/`)
for the full deliverable-by-deliverable method map. Team = 3 people, puzzle = **The Breakfast
Paradox**.

## 7. Lectures 9-10 (added 2026-09-02)

**Lecture 9** — closes out the "System Design" software-engineering tangent (CAP theorem: pick
2 of Consistency/Availability/Partition-tolerance, e.g. Facebook chooses Availability over
Consistency), then pivots to **"Systems in Product Development"**: a product is framed as a
living system embedded in six forces — Technology, User Behavior, Market, Regulations, Data,
Ethics. Introduces a 3-part **System Failures in Products** typology, each with 2 worked
examples:
- *Over-optimisation* (e.g. aggressive battery-saving killed notification reliability, hurting trust)
- *Ignoring stakeholders* (e.g. smart-city cameras optimized safety, ignored privacy advocates →
  legal/policy backlash; e-scooters optimized for commuters, ignored pedestrians/city
  maintenance → bans)
- *Lack of feedback loops* (e.g. enterprise software shipped on assumptions not usage data;
  fitness wearables gave data with no interpretive coaching → high drop-off)

Then gives the **first fully formal CLD definition** of the course: Variables, Arrows (causal
links), Polarity signs (+ same-direction / − opposite-direction), and Loops (R reinforcing / B
balancing) — with two complete worked examples (Mobile App Notifications: engagement vs.
annoyance vs. uninstalls; Learning & Skill Improvement: a pure reinforcing loop of
practice→skill→confidence→opportunity→practice). This is the most rigorous CLD-construction
walkthrough given so far — use it as the template for the Breakfast Paradox CLD in Week 3.

**Lecture 10** — delivers **System Archetypes** (syllabus Week 3), but teaches a **different
trio than the syllabus PDF lists**. Syllabus says: Tragedy of the Commons, Shifting the Burden,
Success to the Successful. Lecture 10 actually teaches: **Fixes That Fail, Tragedy of the
Commons, Limits to Growth** (Tragedy of the Commons is the only one both documents agree on).
Treat the lecture as authoritative for what you'll be tested/assessed on, same as the
assessment-weight discrepancy in §3.

| Archetype | Core idea | Structure pattern | Worked examples given |
|---|---|---|---|
| Fixes That Fail | A quick fix relieves the symptom short-term but creates a bigger problem later | Problem → Quick Fix → Temporary Improvement → Unintended Consequence → Bigger Problem → more quick fixes (vicious cycle) | App sends more push notifications to fix low engagement → users feel spammed → uninstalls → engagement worse than before. Painkillers for headaches → dependency, root cause (sleep/stress/posture) never addressed |
| Tragedy of the Commons | Individuals acting in self-interest collectively deplete a shared resource | Shared Resource → Individual Usage↑ → Resource Depletion → System Collapse | Hostel wifi bandwidth (everyone streams HD → network degrades for all); open-source maintainer burnout (many use, few contribute back) |
| Limits to Growth | Rapid growth eventually hits a hidden constraint that slows/stops it | Growth Loop → Constraint Appears → Slowing Growth → Plateau/Decline | Social platform virality hits moderation/infra/regulatory limits; startup hiring fast hits coordination overhead/culture dilution |

**Relevance flag for the Breakfast Paradox:** *Fixes That Fail* is a strong candidate lens for
Phase 3 (any "just wake up earlier" / "just extend mess hours" quick fix likely has an
unintended-consequence tail worth mapping). *Tragedy of the Commons* fits Puzzle 3 (Research
Lab Commons) much better than Breakfast Paradox — don't force it onto the wrong puzzle.

## 8. Thinking in Systems — ⚠️ only the audiobook figure supplement was attached, not the book

The file `thinking in systems audible companion pdf -- Donella Meadows -- 2018` is a **33-page
Audiobook Supplement** (Chelsea Green Publishing, ed. Diana Wright) — it's just the list of
figures/diagrams referenced in the audiobook (stock-and-flow bathtub diagrams, feedback loop
diagrams, the "Systems Zoo" archetype figures, etc.), not the actual chapter prose. If you want
the real text studied and quoted precisely, attach the actual book PDF/epub. Until then, any
Meadows content beyond what's already directly quoted on lecture slides (§5 above) will be
drawn from general knowledge of the book's well-established structure (Ch.1 systems basics —
stocks/flows/feedback; Ch.2 the "systems zoo" of archetypes; Ch.3 why systems surprise us —
bounded rationality, resilience; Ch.4 leverage points, the famous 12-point list; Ch.5-6
system traps and system design principles) rather than this specific file, and will be labeled
as such rather than cited as if quoted from the attached PDF.

## 9. Fifth Discipline / Fifth Discipline Fieldbook — full texts attached, deep read in progress

Both are real, complete, text-extractable: *The Fifth Discipline* (Senge, 1994 Currency pbk
ed., 412 pp.) and *The Fifth Discipline Fieldbook* (Senge/Kleiner/Roberts/Ross, 2011 Nicholas
Brealey epub). Sample extraction confirms genuine chapter prose (e.g. p.100-101, Ch.7 "The
Principle of Leverage": *"the bottom line of systems thinking is leverage—seeing where actions
and changes in structures can lead to significant, enduring improvements... the best results
come not from large-scale efforts but from small, well-focused actions"*).

Two background deep-read passes were launched (2026-09-02) to fully read both texts chapter by
chapter and cross-reference against lecture content — see `research/book-notes-fifth-discipline.md`
and `research/book-notes-fifth-discipline-fieldbook.md` once complete.

## 10a. Consolidated verdict — the archetype question, resolved (added 2026-09-02)

Full deep-reads of both Senge books are done (`research/book-notes-fifth-discipline.md`,
`research/book-notes-fifth-discipline-fieldbook.md`). Between them they resolve the "which
archetypes actually matter" question raised in §7:

| Archetype | Syllabus PDF (Wk 3) | Lecture 10 taught? | Main book (9 official) | Fieldbook (5 covered) |
|---|---|---|---|---|
| Fixes That Fail (≈"Fixes That Backfire") | – | ✅ | ✅ #8 | ✅ |
| Tragedy of the Commons | ✅ | ✅ | ✅ #7 | ✅ |
| Limits to Growth | – | ✅ | ✅ #2 | ✅ |
| **Shifting the Burden** | ✅ | ❌ | ✅ #3 (+3a intervenor variant) | ✅ |
| **Success to the Successful** | ✅ | ❌ | ✅ #6 | ❌ (not one of its 5) |
| Balancing Process w/ Delay, Eroding Goals, Escalation, Growth & Underinvestment | – | ❌ | ✅ #1,4,5,9 | ❌ |
| Accidental Adversaries | – | ❌ | ❌ (not in Senge's 9) | ✅ (Fieldbook addition, post-Senge) |

**Verdict:** *Success to the Successful* is a real, well-defined Senge archetype (main book,
Ch.6/App.2, his protégé example) — it exists, the Fieldbook just didn't happen to include it in
its 5. So the syllabus's two named archetypes (Shifting the Burden, Success to the Successful)
are both legitimate and well-sourced — they just haven't been taught yet. Treat them as likely
still coming in a future lecture, and feel free to use them anyway (esp. Shifting the Burden,
see below) since they're solidly grounded in the assigned reading even before lecture catches up.

**Directly relevant to the Breakfast Paradox:** **Shifting the Burden** is a better structural
fit than the taught "Fixes That Fail" — Rohan's VC-canteen run is the "symptomatic fix," and the
real risk is that its easy availability prevents the actual mess-hours/class-time mismatch (the
"fundamental fix") from ever getting fixed, because the pressure that would force a fix keeps
getting relieved. Flag this explicitly for the Phase 2 Systemic Problem Analysis.

## 10b. Other high-value material from the two books, not yet in lecture

- **Senge's 11 "Laws of the Fifth Discipline"** (Ch.4) — none named on any slide yet, though
  several lecture examples are unlabeled instances of them (e.g. Lecture 10's Fixes-That-Fail
  notifications example ≈ Laws #1-3). Full list in `book-notes-fifth-discipline.md` §3. Law #7
  ("cause and effect are not closely related in time and space") and Law #11 ("there is no
  blame") are both directly usable framing for the System Context Brief.
- **The Seven Learning Disabilities** (Ch.2) — "I am my position" and "the enemy is out there"
  map cleanly onto this puzzle's cast (Kadamba optimizing its own window without owning the
  8:30-class collision; VC canteen absorbing blame rather than being seen as part of the same
  system).
- **The 5-step "tell the story from the loop" method** and the **Process Map vs. CLD
  distinction** (Fieldbook Ch.17/23) — concrete, more rigorous than anything in lecture so far;
  use these as the actual working method for the Week 3 CLD and the Phase-1 Process Trace.
- **The Ladder of Inference** (Fieldbook Ch.35) — directly usable for interview/observation work
  in Phase 1 (separating what was actually observed from what's an assumed mental model).
- **The Beer Game**, described in full in the main book (Ch.3) — same "structure determines
  behavior" point as the course's own Slinky demo, MIT Sloan supply-chain version. Confirms the
  syllabus's mention of it; not yet run in class.
- Citation nuance: the Lecture 6 CLD-definition quote is real and located (Fieldbook, "The five
  disciplines" front matter) but is actually the book's definition of Systems Thinking as a
  discipline generally, not narrowly of CLDs — and the slide has a minor transcription slip
  ("natural processes" vs. the book's "larger processes"). Use the book's actual wording if
  quoting precisely in a deliverable.

## 10c. Reminder for future sessions

The full extracted book texts were **not** persisted anywhere (only these synthesized notes
were saved) — if a later deliverable needs something not already summarized in
`book-notes-fifth-discipline.md` / `book-notes-fifth-discipline-fieldbook.md`, the PDF/epub
would need to be re-extracted from the source files in the project root.

## 11. Still pending before Phase 1 deliverables start

*Systemic Design: Theory, Methods, and Practice* (Jones & Kijima) — not yet attached, to follow.
Once the Fifth Discipline deep-reads land and (if provided) the real Thinking in Systems text
and Systemic Design are studied, Phase 1 (System Context Brief, Stakeholder Map, Power-Interest
Map, Process Trace, System Timeline) begins for the Breakfast Paradox.
