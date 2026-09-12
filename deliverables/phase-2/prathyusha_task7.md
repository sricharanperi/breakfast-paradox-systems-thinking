# Task 7 — Identify Systemic Patterns & Root Causes

**The Breakfast Paradox — Systemic Problem Analysis**

Author: Prathyusha. Builds on the System Context Brief, Stakeholder Map, Power-Interest Map, Process Trace,
and System Map (Tasks 1-6), and on primary research: a single-respondent self-account (2026-09-03), five
student interviews (2026-09-06), and a CFS Chair interview plus Kadamba kitchen walkthrough and mess-poster
review (2026-09-13).

The fictional Rohan/Adit scenario from the original problem brief is used nowhere in this document as
evidence. It was the framing device that got us to ask the question; everything below is answered from real
data about IIIT-H.

---

## 1. Purpose & Scope

Task 6 mapped the system's actors, flows, and a first set of causal loops. This task moves one level down:
from *what the system looks like* to *why it keeps producing the same outcome* — a persistent gap between
students registering for breakfast and students eating it — even though no individual actor in the system is
behaving irrationally. A student who registers out of habit, a kitchen that plans to the only number it has,
a governance office that runs a well-functioning menu-feedback loop are all making locally sensible choices.
The paradox is that these locally sensible choices add up to a stable, structural mismatch that nobody
individually intends and nobody individually can fix.

Scope: this document covers events, patterns, structures, and mental models (Iceberg); feedback loops and
delays; unintended consequences; structural root causes and their interactions; systemic tensions;
structural power asymmetries; missing feedback; workarounds; and one system archetype with real support. It
stops at diagnosis — no interventions or recommendations are proposed here; that is Task 9-11's job.

Every claim below carries one of four evidence tags:
✅ **CONFIRMED** — directly stated by a source, or observed directly.
🟡 **PLAUSIBLE-PROVISIONAL** — consistent with evidence, not independently verified.
❓ **UNKNOWN-REQUIRES VALIDATION** — a real open question, named as such.
⛔ **UNSUPPORTED** — flagged only when rejecting a claim someone might otherwise make.

A one-respondent account is never written up as a population fact. A category-level institutional number
(like the CFS Chair's turnout figures) is treated as stronger than any individual's self-report, but its
scope and methodology are still checked before being generalized. Full evidence tables, the complete
Iceberg matrix, and the validation backlog live in `assets/task7/`; this file carries only what's needed to
follow the argument.

---

## 2. From Symptoms to Systemic Explanation

**Symptoms** (what is directly observed):

- Students register for breakfast and then do not attend — confirmed for one respondent as a repeated
  personal pattern, and confirmed at the institutional category level: breakfast turnout runs 35-40%,
  against 70% for general items and over 90% for high-demand items (CFS Chair). *What we don't know:* the
  exact scope of the 35-40% figure — whether it covers all four messes or Kadamba specifically (see
  `assets/task7/08_validation_gaps.md`, P1-1).
- At least one interviewed student gives an internally contradictory account of their own attendance
  ("haven't been to mess all semester" vs. "whenever I went, items ran out") — a real data-quality signal,
  not a system fact, and treated as such throughout this report.
- A public mess poster shows two different domains for what should be one registration portal
  (dining.iiit.ac.in vs. mess.iiit.ac.in) — found and corrected narrowly during this project's own review of
  the posters.
- An informal resale channel (Mess Cell WhatsApp) exists for offloading registered-but-unwanted meal slots —
  confirmed to exist, unmeasured in scale.

**Underlying causes are not explained here** — Sections 3, 9, and 10 build up to them through evidence, not
by asserting them up front.

---

## 3. Iceberg Analysis

Full detail (every event/pattern/structure/mental-model row, with sourcing and confidence) is in
`assets/task7/01_iceberg_matrix.md`. This section carries the condensed version needed to follow the
argument.

### 3.1 Events (selected)

| Event | Confidence |
|-------|------------|
| Respondent registers daily for Kadamba veg breakfast (~₹48), does not attend, describes it as ongoing | ✅ (n=1) |
| CFS Chair: registration locks at T-4 (4 days before serving) and goes to the vendor for procurement | ✅ |
| CFS Chair: turnout by category — high-demand >90%, general ~70%, breakfast 35-40% | ✅ |
| CFS Chair self-identifies a risk that posting the menu rotation in advance could cause selective attendance on "good menu" days | ✅ (as a stated concern) |
| Cancellation is capped at 5/month | 🟡 (single-sourced) |
| Mess poster shows two different portal domains | ✅ |
| Respondent's own 8:30 AM class occurs only twice a week | ✅ (n=1) |
| One person manages both cold and dry storage inventory at Kadamba | ✅ |

### 3.2 Patterns

- **Ghost registration, concentrated in breakfast** — the gap between registering and attending is
  consistently wider for breakfast than for any other meal category. 🟡 PLAUSIBLE at the mechanism level
  (the *existence* of a wider breakfast gap is ✅ CONFIRMED via the CFS Chair's numbers; *why* it's wider is
  provisional).
- **Cancellation underuse relative to true non-attendance** — a 5/month cap cannot plausibly cover daily or
  near-daily non-attendance implied by the turnout numbers. 🟡 PLAUSIBLE-PROVISIONAL.
- **Informal resale exists as a release valve** outside the formal registration/cancellation system. 🟡
  mechanism confirmed, scale unknown.
- **Self-reported skip reasons are heterogeneous** — habit, food-quality history, environmental
  visibility ("I don't usually see the mess"), and non-daily schedule conflict all appear for the one
  respondent with a full account, rather than one dominant "can't make it to an 8:30 class" story. 🟡 for
  that respondent; ❓ UNKNOWN whether this generalizes.
- **Transparency/attendance interaction** — a candidate pattern, self-identified by the CFS Chair, not yet
  corroborated on the student side. ❓ UNKNOWN-REQUIRES VALIDATION.

### 3.3 Structures

| Structure | Category | Confidence |
|-----------|----------|------------|
| Monthly billing decoupled from per-meal attendance | Rules/Incentives | ✅ |
| Cancellation capped at 5/month | Rules | 🟡 |
| Vendor procurement locked at T-4 | Temporal | ✅ |
| Turnout feedback exists only at aggregate/category level | Information flows | 🟡 |
| Registration portal identity fragmented across two domains | Information/Technology | ✅ |
| Decision rights split: menu (Mess Committee), execution (kitchen/vendor), academic timetable (explicitly excluded from mess governance) | Decision rights | ✅ |
| Kadamba (on-site) vs. Bakul+Palash (shared off-site, transitional) are structurally different supply systems | Physical/Organizational | ✅ |
| Single person manages both inventory streams at Kadamba | Resource | ✅ |
| Mess Cell WhatsApp as informal secondary market | Social | ✅ |

### 3.4 Mental Models

Only three are evidenced well enough to name (full reasoning in `assets/task7/11_mental_models_evidence.md`):

- **MM1 (students):** "Registering costs me nothing extra if I don't show up." 🟡 Potential — inferred from
  repeated behavior, not a direct quote.
- **MM2 (institution):** "Aggregate registration is close enough to actual demand for procurement." 🟡
  Potential — inferred from a practice that continues despite the same office knowing the gap's size. This
  is the single mental model whose validation would most change this report's conclusions (see Section 19).
- **MM3 (CFS office):** "More menu transparency is straightforwardly good" — a belief the CFS Chair is
  visibly revising in real time, evidenced by their own self-identified concern about it. 🟡 PLAUSIBLE,
  closest of the three to direct confirmation.

---

## 4. Key Recurring System Patterns

The single most important recurring pattern in this whole analysis is that **breakfast behaves differently
from every other meal category on the same registration/billing/procurement infrastructure.** High-demand
items clear above 90%, general items around 70%, and breakfast alone sits at 35-40%. The infrastructure is
identical across categories; only the outcome differs. That single fact is what earns "billing/registration
decoupling" and "menu-timetable-academic fragmentation" the status of structural explanation rather than
"students are being irresponsible" — the same students, under the same rules, behave very differently for
lunch and dinner.

The second recurring pattern is that **every workaround in this system routes around the registration
number rather than correcting it** — Skip Meal, cancellation, and informal resale all give a student a way
to not eat a registered meal without changing what the registration number itself represents to procurement.

---

## 5. Structural Mechanisms

The mechanisms that turn the above patterns into a stable equilibrium:

1. **Decoupled billing (ST1)** removes the per-meal cost signal that would otherwise make registration track
   intent to attend.
2. **The T-4 procurement lock (ST3)** freezes the (inflated) registration number 4 days before serving,
   which structurally caps how responsive the pipeline can ever be to any later correction — even a perfect
   same-week Skip Meal system could not fix procurement that has already committed.
3. **Fragmented decision rights (ST6)** mean no actor owns the cross-cutting outcome. The Mess Committee owns
   menu quality and runs it well (Section 6, loop B3). The kitchen owns execution. The academic office is
   confirmed to have no say in mess timings at all. Billing/registration policy sits with yet another part of
   CDS. None of these four is positioned, alone, to close the registration-attendance gap.
4. **Aggregate-only feedback (ST4)** means the CFS Chair can state the exact size of the gap (35-40%) without
   that knowledge being shown to translate into a registration-policy conversation anywhere in this evidence
   set.

---

## 6. Feedback Loops

Full templates, closure checks, and the Mermaid source are in `assets/task7/02_causal_loop_diagram.md`. Six
loops carry forward from Task 6; this section re-verifies them against the root-cause question rather than
rebuilding them.

### R1 — Registration/Resale (Reinforcing) — 🟡 PLAUSIBLE, two of three links confirmed

Low registration friction → ghost registrations → resale-market viability (via Mess Cell WhatsApp) → back to
tolerance for loose registration. The closing link (resale making loose registration feel lower-risk) is
inferred, not directly quoted, but the loop's shape and its first two links are solid.

### B3 — Menu Rotation Governance (Balancing) — ✅ CONFIRMED, the only fully closed loop in the system

Menu complaints → feedback to Mess Committee → rotation adjustment (~1-month cycle, with student input) →
improved satisfaction → reduced complaints. This loop matters for the diagnosis precisely *because* it works:
it proves the institution is capable of running closed feedback loops in general, which means the
registration-attendance gap is not persisting for lack of institutional capacity — it is persisting because
*this specific* feedback path has no evidenced owner or channel.

### R3 — Menu Transparency Backfire (Reinforcing, candidate) — ❓ UNKNOWN, self-identified by CFS Chair only

Advance posting → students learn "good day" items → selective attendance → demand unpredictability on other
days → pressure back on posting practice. Only the first link is confirmed; the rest is the CFS Chair's own
named concern, not yet observed.

### B1 — Skip Meal, B2 — Capacity Redistribution (Balancing, designed) — ❓ UNKNOWN, not confirmed closed

Both mechanisms exist by design. Neither has evidence in this dataset that its closing links (declaration →
forecast adjustment; overcrowding → cross-mess redistribution) actually operate. B2 is additionally weakened
structurally by ST7 — Kadamba and Bakul/Palash are different kitchens with (presumably) separate registration
pools, which makes cross-mess redistribution mechanically questionable even before checking for behavioral
evidence.

### R2 — Sleep/Energy (Reinforcing, candidate) — ❓ UNKNOWN, only first link confirmed

Carried forward from Task 6 as a named candidate only. Not promoted to a confirmed loop here.

### Rejected: Under-Provisioning "Loop"

The existing parallel Task 7 draft proposes a T-4-lock → shortage → students-turned-away chain that would,
if it looped back to lower future registration, be a genuine balancing loop. No evidence in this dataset
shows that closing link. It is a real, evidenced *chain* (used in Sections 8 and in the root-cause network)
but not a loop, and is not diagrammed as one.

---

## 7. Delays

| Delay | From → To | Approx. duration | System effect | Evidence | Confidence |
|-------|-----------|-------------------|-----------------|----------|------------|
| Registration-to-procurement freeze | Registration change → procurement action | 4 days (T-4) | Caps responsiveness of the entire pipeline regardless of any other mechanism | E3 | ✅ |
| Menu feedback cycle | Complaint → rotation adjustment | ~1 month | The one delay in the system matched to a functioning closed loop (B3) | S5 §3, §7 | ✅ |
| Prep-start lead time | Kitchen prep start (~5:00 AM) → service | Same day, hours | Same-day registration signals arrive too late to be actionable even if they existed | S5 §12 | ✅ |
| Resale-channel coordination | Ghost registration → informal resale | Unknown, presumably short (WhatsApp) | Removes the visible cost of ghost registration before it becomes a forcing function for policy change | E7 | 🟡 |
| Institutional-knowledge-to-policy delay | CFS Chair's known turnout gap → any registration/billing policy response | Unknown — no evidence a response has started | If this delay is, in fact, indefinite rather than merely long, it reclassifies from a delay into a genuinely missing loop | E4, RC4 | ❓ UNKNOWN — this is the single most consequential open question in the report (see Section 19) |

---

## 8. Unintended Consequences

Full table in `assets/task7/03_unintended_consequences.md`. The two OBSERVED consequences with the strongest
evidence:

- **Decoupled billing**, intended for administrative simplicity, produces a procurement signal known by its
  own owners to overstate breakfast attendance by roughly 60-65 percentage points. Students pay for uneaten
  meals; the kitchen plans against numbers it knows are wrong. (✅ structure, 🟡 full causal weight.)
- **The 5/month cancellation cap**, plausibly intended to reduce administrative noise, likely pushes real
  non-attendance signal into the informationally invisible resale channel once a student exceeds it —
  making the formal system's picture of "who isn't coming" less complete than if cancellation were unlimited
  but noisier. (🟡 PLAUSIBLE — the cap and the resale channel are each confirmed; the causal link between
  them is inferred.)

One HYPOTHESIZED consequence, self-flagged by its own policy owner rather than by this research: advance
menu transparency, meant to build trust, may make day-to-day demand harder to forecast if it concentrates
attendance on posted "good" days (❓ UNKNOWN).

---

## 9. Systemic Tensions

Full detail in `assets/task7/05_systemic_tensions.md`.

- **T1 — Administrative simplicity vs. demand-matching accuracy.** Billing stays simple by not metering
  attendance; the kitchen pays for that simplicity in planning uncertainty. ✅ CONFIRMED structure.
- **T2 — Vendor lead-time certainty vs. registration responsiveness.** A 4-day lock protects the vendor's
  sourcing window at the cost of the entire pipeline's ability to react to anything that changes inside that
  window. ✅ CONFIRMED structure; the exact minimum feasible lead time is unconfirmed.
- **T3 — Menu transparency (trust) vs. demand predictability.** The same office (CFS) holds both goals and
  is visibly weighing them against each other in real time. ❓ UNKNOWN whether the tension is operating at
  meaningful scale, though it is certainly real as a *stated* concern.
- **T4 — Fragmented governance autonomy vs. cross-cutting problem ownership.** Each governance silo can run
  its own feedback loop well (proven by B3) while the cross-cutting registration-attendance problem has no
  natural owner under that same structure. ✅ CONFIRMED structural condition.

---

## 10. Root Cause Analysis

Full ROOT-CAUSE TEST templates and the network diagram are in `assets/task7/04_root_cause_network.md`.

### 10.1 Immediate (symptom-level, not root causes)

- A student not showing up for a registered breakfast.
- A specific day's shortage or over-preparation at Kadamba.
- One respondent's self-contradictory account of their own attendance.

These are individual instances, not structural causes — labelling any of them a "root cause" would be
exactly the kind of blame-the-individual mislabelling this analysis is built to avoid.

### 10.2 Intermediate Mechanisms

- **The T-4 procurement lock (RC2).** Structural and real, but tested against the root-cause criteria and
  found to be an *intermediate mechanism*, not a primary root cause: removing it would improve
  responsiveness to the registration-attendance gap but would not remove the incentive (RC1) that inflates
  registration numbers in the first place.
- **Information fragmentation (RC4).** Real, but folded in as a contributing factor under RC3 rather than
  treated as independently sufficient — coarse feedback compounds fragmented ownership rather than being a
  separate root cause in its own right.

### 10.3 Structural Root Causes

**RC1 — Billing/registration decoupled from attendance.** Upstream of both the ghost-registration pattern
and the cancellation-underuse pattern; independently corroborated by a second, separately authored Task 7
draft reaching the same structural conclusion. ✅ CONFIRMED as a structure. If removed, the problem would
shrink but not disappear — self-reported skip reasons (habit, food-quality history, environmental
visibility) are not billing-driven and would persist regardless.

**RC3 — Fragmented decision rights across menu, kitchen execution, academic timetable, and billing policy.**
This is the meta-level root cause: it explains *why* RC1 has not been revisited even though its size (the
35-40% figure) is known and quantifiable by the very office that could, in principle, act on it. It also
explains why a genuinely well-functioning governance mechanism elsewhere in the same institution (B3, menu
rotation) has not transferred to this problem — good governance in one silo does not automatically reach a
cross-cutting issue that silo doesn't own.

Both pass the root-cause test: structural rather than a symptom label, explain multiple patterns, sit
upstream of individual behavior, and are evidenced rather than assumed. Neither is asserted with false
certainty — RC1's *full* explanatory weight and RC3's role as *cause* (as opposed to one of several
plausible explanations for policy inertia — see Section 19) are both marked provisional.

---

## 11. Root Cause Network

```
RC1 (billing decoupled from attendance)
      │ produces
      ▼
Ghost-registration incentive
      │ compounded by
      ▼
RC2 (T-4 procurement lock) ── caps correctability of RC1's effect
      │ produces
      ▼
Persistent registration-attendance gap (35-40% breakfast turnout)
      │ visible only as
      ▼
Category-level data known to CFS Chair — cannot reach registration-policy design because:
      ▲
      │ root-caused by
RC3 (fragmented decision rights — no actor owns both the incentive lever and the outcome)
```

RC1 and RC3 interact directly: RC3 is the best-supported explanation for why RC1 persists unaddressed despite
being known and quantified. RC2 and information fragmentation (RC4) compound each other similarly — even
finer-grained data would still hit the T-4 wall before it could be actioned same-cycle.

---

## 12. Missing/Weak Feedback

Full table in `assets/task7/06_feedback_gaps.md`. The single highest-priority gap: **the CFS office's known
turnout gap does not have a confirmed channel to registration/billing policy design.** The data exists; the
office holding it can state it precisely; no evidence in this project shows it reaching a policy conversation.
This is stated as an open question (see Section 19, P0-1), not as a confirmed institutional failure — it may
simply be outside what this project's interviews were positioned to observe.

By contrast, the menu-complaint-to-rotation feedback path (underlying loop B3) is the one channel in this
entire system confirmed to be fully closed — proof the institution can run this kind of loop when the
ownership question is settled.

---

## 13. Structural Power & Consequence Asymmetries

Drawing on Task 3's Power-Interest/Leverage analysis:

- **High-consequence / low-control:** Students bear the full financial and time cost of the registration-
  billing mismatch (RC1) but have no control over billing policy, the T-4 lock, or how registration data is
  used downstream.
- **High-information / low-authority:** The CFS Chair's office holds the most precise diagnostic information
  in the whole system (the exact turnout split by category) but Task 3's power analysis found the
  inter-relationships between the Mess Committee, the CDS Office, and the Warden on registration/billing
  *policy authority* specifically to be unconfirmed — meaning the office with the clearest picture of the
  problem may not be the office empowered to redesign the rule causing it. This is the same structural gap
  named as RC3/RC4 here, seen from the power-mapping side rather than the process side.
- **Low-authority / high-actionable-input:** Students individually control the one input (registration
  intent) that most directly determines the accuracy of the whole downstream pipeline, while bearing no cost
  for inaccuracy beyond their own bill (RC1) — a textbook case of the actor with the best real-time
  information having the weakest incentive to report it accurately.
- **Unmeasured collective leverage:** Task 3 identified the Mess Cell WhatsApp channel as a form of
  "sleeping" or exercised-but-unmeasured collective student leverage. This report's evidence confirms the
  channel exists (ST9) but, consistent with Task 3's framing, its actual leverage — whether it could be
  mobilized to pressure a policy change, versus merely absorbing individual inconvenience — remains
  unmeasured. 🟡 PLAUSIBLE that it currently functions as a pressure release rather than organized leverage
  (per the Shifting the Burden reading in Section 15), but this has not been tested directly.

---

## 14. Workarounds as Signals

| Workaround | Structural problem compensated | Why the formal system doesn't handle it | Reduces pressure for formal change? |
|------------|-----------------------------------|--------------------------------------------|----------------------------------------|
| Mess Cell WhatsApp resale | Ghost registration under decoupled billing (RC1) | No formal per-meal transfer mechanism exists | 🟡 Plausibly yes — a working release valve removes the pain that would otherwise force RC1 onto someone's agenda |
| Skip Meal declaration | Same-week non-attendance beyond the cancellation cap | Not confirmed to reach kitchen forecasting distinctly from T-4 aggregate | ❓ Unknown — depends on whether it functions at all (Section 6) |
| Students' own coping (intermittent fasting, habit, eating elsewhere) | Food-quality history, lack of environmental visibility, non-daily schedule conflicts | These are individual-level adaptations to conditions the mess system doesn't track or respond to per-student | Not evidenced either way — these are individual choices, not organized workarounds, so they don't obviously reduce institutional pressure the way a visible collective channel would |

The clearest signal here is the resale channel: its existence is itself evidence that the formal
registration/cancellation system is not adequate to actual student behavior, and per Section 15's Shifting
the Burden reading, its effectiveness at the individual level plausibly reduces the systemic pressure that
would otherwise push RC1 toward being fixed.

---

## 15. System Archetype

Full fit-testing (including five rejected candidates) is in `assets/task7/09_system_archetypes.md`. One
archetype is retained:

**Shifting the Burden — Registration/Resale.** The symptomatic solution (informal resale via Mess Cell
WhatsApp) relieves the immediate waste of an individual ghost-registered meal. The fundamental solution
(redesigning billing so that registering only when intending to attend is the natural default) is not
currently being pursued. The mechanism connecting them — that a well-functioning symptomatic fix quietly
removes the pressure that would otherwise drive the fundamental fix — is plausible and consistent with every
piece of evidence gathered, but not independently proven; policy inertia could equally be explained by RC3
alone. Both explanations may be true simultaneously. 🟡 PLAUSIBLE.

A second candidate, Fixes That Fail (a reported December 2024 cancellation-cap tightening allegedly
worsening the no-show pattern it targeted), is **not promoted** here: it rests on a single secondary source
(the parallel Task 7 draft), not on any primary interview or institutional statement independently
gathered for this analysis. It is flagged, not asserted.

---

## 16. Systemic Problem Diagnosis

**Short:** Breakfast attendance is low not because students are careless or lazy, but because billing,
procurement timing, and governance authority are each designed sensibly in isolation and none of them, alone
or together, currently connects registration accuracy to any consequence or correction.

**Detailed:** The Breakfast Paradox is not "students skip breakfast." It is that a monthly, attendance-blind
billing model (RC1) removes the one incentive that would otherwise make registration track real intent, a
four-day procurement freeze (RC2) makes even a perfectly accurate late signal unusable, and decision rights
over menu, kitchen execution, academic scheduling, and billing policy are split across four separate
authorities (RC3) with no one of them positioned to see the whole chain and act on it — even though the
office that could name the exact size of the resulting gap (35-40% breakfast turnout) sits inside this same
institution. Individual coping mechanisms (informal resale, Skip Meal, personal habit adjustments) absorb
enough of the resulting friction that the underlying structure has not been forced to change. The paradox
persists not despite everyone behaving reasonably, but because of it.

---

## 17. Core Systemic Findings

**F1 — The registration-attendance gap is real, structural, and breakfast-specific.**
Pattern: turnout is 35-40% for breakfast vs. 70-90%+ for other categories on identical infrastructure.
Underlying structure: RC1 (decoupled billing), RC2 (T-4 lock).
Feedback mechanism: R1 (registration/resale), not yet self-correcting.
System consequence: a stable, self-reinforcing low-turnout equilibrium specific to one meal.
Evidence: E1, E2, E4. Confidence: ✅ gap confirmed; 🟡 mechanism weighting provisional.

**F2 — The gap is known by the institution but not confirmed to reach the policy level that could act on it.**
Pattern: aggregate turnout data exists at CFS level; no evidence of registration-policy discussion.
Underlying structure: RC3 (fragmented decision rights), RC4 (information coarseness).
Feedback mechanism: the missing link identified in Section 12.
System consequence: known problems can persist indefinitely without any actor being at obvious fault.
Evidence: E4, absence-of-evidence flagged explicitly. Confidence: ❓ UNKNOWN — the report's most important
open question.

**F3 — The institution is fully capable of closed feedback loops; this specific one just isn't closed.**
Pattern: menu complaints reliably produce rotation adjustments (B3).
Underlying structure: Mess Committee's menu authority, matched to a real feedback channel.
Feedback mechanism: B3, fully confirmed and closed.
System consequence: rules out "the institution can't do feedback" as an explanation — the problem is
ownership-specific, not capacity-wide.
Evidence: S5 §3, §7. Confidence: ✅ CONFIRMED.

**F4 — Designed balancing mechanisms (Skip Meal, cross-mess redistribution) are not confirmed to function.**
Pattern: mechanisms exist by design; no usage or effectiveness data found.
Underlying structure: B1, B2.
System consequence: the system may have less real self-correction capacity than its design suggests.
Evidence: absence of data in S1/S2/S5 despite the mechanisms' documented existence. Confidence: ❓ UNKNOWN.

**F5 — Self-reported skip reasons are heterogeneous, not dominated by academic scheduling.**
Pattern: habit, food-quality history, environmental visibility, and non-daily schedule conflicts all appear
for the one respondent with a full account; that same respondent's own 8:30 class occurs only twice weekly.
Underlying structure: none of the four decision-rights silos (Section 10.3, RC3) currently tracks these
individual-level factors.
System consequence: a purely schedule-based intervention would likely under-address the real driver mix.
Evidence: E14, E17, S1. Confidence: 🟡 for this respondent; ❓ UNKNOWN for generalization.

**F6 — An informal resale market functions as an unmeasured release valve.**
Pattern: Mess Cell WhatsApp absorbs ghost-registered slots outside the formal system.
Underlying structure: ST9, interacting with R1's Shifting-the-Burden dynamic.
System consequence: individually beneficial, but plausibly removes pressure for structural fixes and hides
the true scale of ghost registration from institutional view.
Evidence: E7. Confidence: 🟡 mechanism confirmed, systemic effect inferred.

**F7 — A public information inconsistency (two portal domains) shows institutional communication is not
fully coherent even on simple, correctable matters.**
Pattern: found directly on physical mess signage.
System consequence: small on its own, but a leading indicator consistent with RC3's broader diagnosis of
fragmented ownership across the mess-governance apparatus.
Evidence: E11. Confidence: ✅ CONFIRMED.

---

## 18. What Is Root Cause vs. What Is Not

**Root causes (structural, upstream, evidenced):** RC1 (billing/registration decoupling), RC3 (fragmented
decision rights).

**Not root causes, even though structurally real:** RC2 (T-4 lock) and RC4 (information coarseness) are
compounding *mechanisms* — real, evidenced, and worth fixing, but each is downstream of or secondary to RC1/
RC3; removing either alone would not make the pattern disappear.

**Explicitly not root causes:** individual student choices (habit, sleep, taste preference), one respondent's
contradictory self-report, a single day's kitchen shortage. These are symptoms or noise, not structure —
labelling them root causes would misattribute a systemic outcome to individual failure, which is exactly the
mislabelling this analysis exists to avoid.

**A live alternative explanation not yet ruled out:** it is possible that RC1 has, in fact, been considered
and deliberately retained (e.g., because attendance-based billing is operationally harder to implement than
it looks), in which case the correct diagnosis shifts from "an unowned gap" to "a considered trade-off no one
has been able to improve on yet." This alternative is not rejected here — it is exactly the question posed
in `assets/task7/08_validation_gaps.md` P0-1, and the honest answer is that this evidence set cannot
currently distinguish the two.

---

## 19. Current Evidence Gaps

The two gaps that would most change this report's conclusions if answered (full list, with exact
non-leading questions, in `assets/task7/08_validation_gaps.md`):

1. **Has the CFS office's known turnout gap ever reached a registration or billing policy conversation?**
   This single answer decides whether RC3 describes an unowned gap or a deliberately retained trade-off —
   two materially different diagnoses.
2. **Does Skip Meal data ever reach kitchen forecasting distinctly from the T-4 aggregate?** This decides
   whether loop B1 is a genuinely functioning (if weak) balancing mechanism or effectively decorative.

Secondary gaps worth closing before any intervention design: the exact scope of the 35-40% figure (all
messes or Kadamba only), independent confirmation of the 5/month cancellation cap, and whether the menu-
transparency concern (R3/T3) shows up in any actual attendance data.

---

## 20. Conclusion

The Breakfast Paradox persists not because any actor in this system is behaving irrationally, but because
the system currently has no path connecting an accurate demand signal to a policy that would create one.
Students respond rationally to a billing structure that charges them the same whether they attend or not.
The kitchen responds rationally to the only number it is given, four days before it needs it. The CFS office
runs a genuinely well-functioning feedback loop for menu quality — proof the institution can do this — while
the specific loop that would close the registration-attendance gap has no confirmed owner anywhere in the
four-way split of menu, execution, academic scheduling, and billing authority. The paradox is not a
breakdown; it is four locally coherent systems interacting to produce a jointly incoherent outcome, held
stable by an informal resale channel that quietly absorbs the worst of the individual cost before it can
accumulate into pressure for structural change. This is a system reproducing its own outcome, not a
collection of individuals failing to show up for breakfast.

---

## Appendix — Evidence/Confidence Legend

✅ **CONFIRMED** — directly stated by a named source or directly observed.
🟡 **PLAUSIBLE-PROVISIONAL** — consistent with evidence, mechanism or scope not independently verified.
❓ **UNKNOWN-REQUIRES VALIDATION** — a real, named open question; not decided either way.
⛔ **UNSUPPORTED** — used only to explicitly reject a claim, never to assert one.

Source key: S1 = 2026-09-03 self-account interview · S2 = 2026-09-06 five-student interviews · S3 = Neha's
independent cross-transcription of the same five interviews · S4 = braindump #1 · S5 = braindump #2 (CFS
Chair interview + kitchen walkthrough) · S6 = Task 6 System Map · S7 = existing parallel Task 7 draft
(cross-reference only) · S8 = Task 3 Power-Interest/Leverage Map · S9 = mess poster photographs.

## Supporting Assets

- `assets/task7/01_iceberg_matrix.md` — full Events/Patterns/Structures/Mental Models tables and the
  complete linkage matrix.
- `assets/task7/02_causal_loop_diagram.md` — full loop templates for R1, B1, B2, R2, B3, R3, the rejected
  under-provisioning chain, and the consolidated CLD Mermaid source.
- `assets/task7/03_unintended_consequences.md` — full unintended-consequences table.
- `assets/task7/04_root_cause_network.md` — full ROOT-CAUSE TEST templates and network diagram.
- `assets/task7/05_systemic_tensions.md` — full tensions table.
- `assets/task7/06_feedback_gaps.md` — full missing/weak feedback table.
- `assets/task7/07_evidence_traceability.md` — every finding traced to its sources.
- `assets/task7/08_validation_gaps.md` — prioritized P0/P1/P2 validation backlog with exact questions.
- `assets/task7/09_system_archetypes.md` — full archetype fit-testing, including rejected candidates.
- `assets/task7/10_quantitative_analysis.md` — every real number available, labelled by type, with an
  explicit list of what cannot be computed from available data.
- `assets/task7/11_mental_models_evidence.md` — full reasoning chain for each mental model.
