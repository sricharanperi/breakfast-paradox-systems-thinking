# Phase 1 · Activity 2 (Deep Dive) — Master Stakeholder Universe Register

**Status:** 🟡 first full pass, built from first-principles system decomposition (17 lenses)
+ primary interview/screenshot data + public-source research + user confirmations on
2026-09-05. This document supersedes the mess-structure and governance assumptions in
`prathyusha_02-stakeholder-map.md` (being updated separately) and is the source of truth
for stakeholder detail going forward. Confidence legend: ✅ confirmed · 🟡 plausible/
needs validation · ❓ unknown/research target · ⛔ considered and rejected.

---

## A. Candidate Register — every actor surfaced, including excluded ones

| ID | Actor | Type | Direct/Indirect/Latent | Formal/Informal | Confidence | Include in final map? | Reason |
|---|---|---|---|---|---|---|---|
| S1 | Students (collective) | Human group | Direct | Formal (registrant) | ✅ | **Yes** | Core actor; internal roles/segments (attender, skipper, gym-goer, etc.) are states, not separate stakeholders — see §D |
| G1 | Mess Committee | Institution | Indirect (governs, doesn't touch daily ops) | Formal | ✅ (public source + user-confirmed the split is real) | **Yes** | Faculty-chaired policy body — previously collapsed with Mess Office |
| G2 | Mess Office | Institution | Indirect | Formal | ✅ | **Yes** | Operational/administrative arm — sends policy emails, places orders, runs the portal relationship |
| G3 | Warden | Individual/role | Indirect | Formal | ✅ | **Yes** | Vendor management, structural mess changes — relationship to G2 still ❓ |
| G4 | Academic Office / timetable authority | Institution | Boundary | Formal | ✅ (confirmed no mess role) | **Yes** | The "sleeping stakeholder" — holds the class-time lever, zero mess engagement |
| V1 | Vendor — South Indian (Kadamba, veg+non-veg) | Commercial | Direct | Formal | ✅ | **Yes** | Full-stack: procures + cooks (per-mess procurement, confirmed) |
| V2 | Vendor — North Indian (Palash veg + Bakul veg/non-veg) | Commercial | Direct | Formal | ✅ | **Yes** | One vendor org spanning two serving points — Palash cooks the shared veg line |
| V3 | Vendor — Jain/Yuktāhār | Commercial | Direct | Formal | 🟡 | **Yes** | Existence confirmed, relationship to V1/V2 (shared or independent) unconfirmed |
| O1 | Mess serving/counter staff | Human group | Direct | Formal | ✅ | **Yes** | Front-line; eat leftover mess food themselves (confirmed) |
| O2 | Kitchen/cooking staff | Human group | Direct | Formal | ✅ | **Yes** | Distinct role from serving staff; per-vendor |
| O3 | Cleaning staff | Human group | Indirect | Formal | 🟡 | Maybe | Mentioned generically; no evidence of distinct stakeholder relevance beyond "mess has cleaning" |
| F1 | Facilities/Estate team | Institution | Boundary | Formal | 🟡 (user's own inference — "there will be") | **Yes**, low confidence | Real Kadamba renovation confirmed; who runs facilities is unconfirmed |
| T1 | Portal/IT system owner (dining.iiit.ac.in) | Institution/individual | Boundary | Formal | ❓ | **Yes**, as placeholder | Structurally critical (controls the interface every decision passes through), identity entirely unknown |
| T2 | Unofficial tool developers (e.g., MCP bot ecosystem) | Individual(s) | Boundary/informal | Informal | ✅ tool exists, 🟡 impact | **Yes** | Publicly documented, MIT-licensed, "built for students of IIIT Hyderabad"; usage/impact unconfirmed |
| N1 | Mess Cell WhatsApp community | Informal group | Direct | Informal | ✅ | **Yes** | Self-organized resale market |
| N2 | Ping (student publication) | Institution (informal) | Boundary | Informal | ✅ (public source) | **Yes** | Real public-pressure/awareness channel, previously entirely missing from the map |
| C1 | Vindhya canteen (+ staff) | Commercial | Direct (substitute) | Formal | ✅ | **Yes** | Competing alternative |
| C2 | Juice canteens | Commercial | Direct (substitute) | Formal | ✅ | Maybe | Minor; low evidence of systemic leverage |
| C3 | Delivery platforms/riders (Swiggy/Zomato/Blinkit) | Commercial | Direct (substitute) | Formal | ✅ | **Yes** | Gate-restricted, same friction as the "11 O'Clock Cliff" puzzle |
| C4 | Campus security/gate staff | Human group | Indirect | Formal | 🟡 | Maybe | Relevant to delivery friction, low direct relevance to breakfast itself |
| S2 | Guest diners (relatives, CIE-affiliated, researchers) | Human group | Indirect | Formal | ✅ (confirmed to exist) | Maybe | Real but marginal — affects walk-in slot competition only |
| — | "Friends" / "Roommates" as separate nodes | — | — | — | — | **No — corrected** | **Self-critique from last pass:** these aren't a distinct stakeholder type, they're *other students*. The real finding is a **peer-influence edge between Student nodes**, not a new actor category. Collapsing them into separate peripheral nodes previously overstated the stakeholder count without adding information — folded into S1's card instead. |
| — | Campus health/wellbeing office | — | — | — | ⛔ | **No** | Zero evidence of any relationship to breakfast-skipping in this population; including it would be medicalizing the problem on no basis (explicitly warned against) |
| — | Seniors/juniors norm transmission | — | — | — | — | **No** | A mechanism/hypothesis, not an actor — no evidence either way |
| — | Parents/guardians (financial) | — | — | — | ❓ | **No** | Mess fee is bundled into hostel fees per general web research; no evidence parents make any per-meal decision — too indirect to include without evidence |

**17 stakeholders included, 6 excluded/maybe, 4 explicitly rejected or reframed.** This is
deliberately not the largest possible list — several lenses (health, seniors/juniors,
parents) turned up nothing beyond speculation and are left out rather than padded in.

---

## B. Why the mess-vendor structure changed the register, not just the diagram

The cuisine-based reframe (Kadamba=South Indian, Bakul=North Indian veg+non-veg,
Palash=North Indian veg-only, Yuktāhār=Jain) does more than fix a naming error. Laid
against the real uptake numbers:

| Mess | Cuisine | Breakfast uptake (2026-09-09) |
|---|---|---|
| Kadamba (Veg) | South Indian | 551/700 = **79%** |
| Kadamba (Non-Veg) | South Indian | 308/600 = 51% |
| Bakul (Veg) | North Indian | 108/350 = **31%** |
| Bakul (Non-Veg) | North Indian | 37/350 = **11%** |
| Palāsh | North Indian (veg-only) | 146/400 = 36.5% |
| Yuktāhār | Jain-adjacent | 108/340 = 32% |

Every North Indian option clusters around 11-36%; the only South Indian option is at
51-79%. This is a **much stronger pattern than "Bakul is newer"** — it held for exactly
one mess before; now it holds across three independent messes sharing one variable
(cuisine). 🟡 Still a hypothesis, not confirmed by anyone saying "I prefer South Indian
breakfast" directly — but it's now the best-evidenced explanation on the table, and it
demotes "Bakul's warehouse origin" from primary explanation to a possible secondary
factor at most.

---

## C. Final Stakeholder Taxonomy (multiple lenses, not one classification)

### 1. Direct / Indirect / Latent
- **Direct:** Students, Vendors (V1/V2/V3), serving/kitchen staff, Mess Cell, Vindhya, delivery platforms
- **Indirect:** Mess Committee, Mess Office, Warden, cleaning staff, guest diners
- **Latent** (currently inert, would activate under specific conditions): Academic Office, Facilities team, Ping, unofficial tool developers

### 2. Formal / Informal
- **Formal:** everything institutional/commercial (G1-G4, V1-V3, O1-O2, F1, C1-C3)
- **Informal:** Mess Cell (N1), Ping (N2), unofficial tool developers (T2)

### 3. Internal / Boundary / External
- **Internal** (inside the currently-drawn system boundary): Students, Mess Committee, Mess Office, Vendors, serving/kitchen staff, Mess Cell
- **Boundary** (touches the system but sits at its edge, easy to overlook): Academic Office, Facilities team, Portal/IT owner, unofficial tool developers, Ping
- **External:** Vindhya, delivery platforms, guest diners

### 4. Operational / Managerial / Governance / Environmental
- **Operational:** serving/kitchen staff, Mess Office, vendors
- **Managerial:** Warden
- **Governance:** Mess Committee, Academic Office
- **Environmental (competing/adjacent systems):** Vindhya, delivery platforms, Mess Cell, Ping

### 5. Proximity to the breakfast experience (high → low)
Students → serving staff → kitchen staff → vendors → Mess Office → Mess Cell →
Warden/Mess Committee → Facilities/Portal-IT → Academic Office/Ping/unofficial tools

---

## D. Segment vs. Role vs. Stakeholder vs. System Condition — Students, precisely

Per the distinction the analysis explicitly requires: none of the following are separate
*stakeholders*. They are states/roles a single student moves through, often within the
same week:

| Category | What it actually is |
|---|---|
| "Attends regularly" / "skips regularly" | **Behavioural state**, not fixed identity — both synthetic personas and the real respondent describe this shifting over a semester |
| "Has an 8:30 AM class" | **Analytical segment** — a scheduling fact about a given day, not a person-type |
| "Uses Mess Cell to buy/sell" | **Temporary role**, activated only when a specific registration goes unused |
| "Uses the unofficial bot tool" | **Behavioural segment**, cuts across attend/skip status |
| "Prefers South Indian food" | 🟡 **Possible segment**, newly hypothesized (§B) — not yet confirmed as a real division among students |

The one stakeholder-level distinction worth keeping separate: **guest diners (S2)** are
not students at all, and sit in a genuinely different formal relationship to the system
(pay-per-meal, no registration/billing cycle) — that's a true stakeholder-type
difference, not just a behavioural segment.

---

## E. Stakeholder Cards (final "Yes" stakeholders only — 17 cards)

**S1 — Students (collective)**
Role: registrant, billed party, attendee/non-attendee. Interest: convenient, affordable,
timely food; avoid double-paying. Formal authority: none beyond registering/cancelling
within rules. Informal influence: Mess Cell market, peer influence on each other (the
former "Friends/Roommates" edge — see §A). Resources: money, time, registration slots.
Information held: their own intent/schedule. Information lacked: real-time queue state,
kitchen prep decisions, whether feedback ever gets read. Dependencies: on Mess
Office/vendors for food; on Academic Office for schedule. Pain: billed regardless of
attendance; walk-in markup; unclear if feedback matters. Incentive: registering costs
nothing extra whether attended or not — no incentive to be accurate. Evidence: ✅
(interview, screenshots). Confidence: ✅ for structure, 🟡 for how typical any given
behavior is (still one real respondent).

**G1 — Mess Committee**
Role: sets menu (~1 month ahead), overall policy authority, chaired by a faculty member.
Interest: balancing student satisfaction with operational feasibility. Formal authority:
high — can set/change rules. Informal influence: the chair's individual standing as
faculty could plausibly bridge to Academic Office (unused so far). Resources: policy
authority. Information: aggregate registration data, presumably. Dependencies: on Mess
Office to execute; on student input (channel/quality unconfirmed). Pain/tension: the one
confirmed policy change (Dec 2024) was driven by *staff* workload, not student
complaints — suggesting operational pressure outweighs student-facing pressure in
practice. Evidence: 🟡 (public source, user-confirmed the Committee/Office split is
real, chair identity not independently re-verified for 2026). Confidence: 🟡.

**G2 — Mess Office**
Role: day-to-day administration — places food orders (4-day lead time, user-confirmed),
runs the portal relationship, sends policy-change emails. Interest: reducing operational
workload (explicit, stated motive for the one confirmed policy change). Formal
authority: implementation-level, not policy-setting. Information: registration counts,
ordering data — likely the actual node that "sees the final registration count before
food preparation begins" (Guide 1's original Q1 target, still not directly confirmed by
a named person). Dependencies: constrained by the 4-day procurement lead time itself —
a hard information-flow bottleneck between same-day student intent and kitchen supply.
Evidence: ✅ existence (public source + user confirmation), 🟡 exact scope of duties.

**G3 — Warden**
Role: vendor management, structural mess changes. Formal authority: high on
infrastructure/vendor matters. Relationship to G2: ❓ unconfirmed — do they overlap,
report to each other, or operate in separate lanes? Evidence: ✅ existence (interview),
❓ relationship to Mess Office specifically.

**G4 — Academic Office / timetable authority**
Role: sets class schedules, including the 8:30 AM start. Formal authority: total, over
its own domain — zero engagement with mess matters (confirmed). Why invisible: no
adjacent relationship connects it to daily student mess experience or to mess
governance at any ring of the onion map — the "sleeping stakeholder" finding stands,
strengthened rather than weakened by everything found this round.

**V1/V2/V3 — Vendors (South Indian/North Indian/Jain)**
Role: per-mess procurement + cooking (confirmed per-mess, not centralized). Interest:
contract terms, margin, volume. Formal authority: controls actual food quality/quantity
served, within Mess Office's ordering parameters. Resources: kitchens, staff, supply
chains — all currently ❓ in detail (Lens C remains the least-evidenced lens overall).
Dependency: bound by the 4-day ordering window — cannot respond same-day to
registration/skip signals. Evidence: ✅ existence and cuisine-split, ❓ everything about
internal operations, procurement sourcing, staffing.

**O1/O2 — Serving staff / Kitchen staff**
Role: front-line execution. Notable fact: serving/cleaning staff eat the mess's own
food themselves post-service (confirmed) — a real, if informal, waste-absorption
mechanism nobody had to design. Formal authority: none. Informal influence: "cook's
mood" (braindump hypothesis) remains untested — no evidence either way yet. Information
lacked: whether Skip Meal toggles reach them in time to matter, given the 4-day
procurement lag likely dominates over any same-day signal. Evidence: ✅ existence, 🟡
operational detail (Guide 2, not yet run).

**F1 — Facilities/Estate team**
Role: physical mess infrastructure (the Kadamba renovation is real, user-confirmed).
Identity: entirely unconfirmed — included as a placeholder because a real event (a
renovation) requires *someone* to have authorized/executed it, not because any specific
office has been named. Confidence: 🟡, weakest-evidenced "Yes" in this register.

**T1 — Portal/IT system owner**
Role: maintains `dining.iiit.ac.in` (current, user-confirmed), controls the literal
interface for every registration decision. Identity: ❓ completely unknown — institute
IT, an external vendor, or something else. Included specifically because Test 4 ("who
knows?") and Test 5 ("who can say no?") in a systems audit cannot be answered without at
least naming this gap.

**T2 — Unofficial tool developers**
Role: built and publish (MIT-licensed) tools that let students manage registration via
an AI agent, "for students of IIIT Hyderabad." Real, verifiable, but usage/impact among
this specific student population is completely unconfirmed (you don't know of anyone
using one). Kept in the register at "Yes" because its mere *existence* changes what
"batch registration" could mean (manual weekly habit vs. fully automated), which is
significant enough to track even at low confidence.

**N1 — Mess Cell WhatsApp community**
Role: informal resale market for unused registrations. Already well-documented; no
change this round beyond the standing open question of its real scale (still ❓).

**N2 — Ping (student publication)**
Role: publishes investigative/explainer pieces on mess issues (2 articles found, Dec
2024/Jan 2025). Function: public-pressure/awareness channel — distinct from, and
possibly more effective than, the "public email" escalation channel you confirmed,
since it reaches a passive readership rather than requiring the reader to already be
subscribed to a thread. Newly discovered; zero presence in any prior version of the
stakeholder map.

**C1 — Vindhya canteen**
No change from prior map; substitute food source, hours still partially uncertain
(6 PM vs. 8 PM close, still open).

**C3 — Delivery platforms/riders**
No change; gate-restricted substitute, shared friction point with the separate "11
O'Clock Cliff" puzzle.

---

## F. Relationship Matrix (12 core stakeholders — full 17×17 would be unreadable; this
covers every pair with a meaningful, evidenced-or-hypothesized relationship)

Legend: A=authority, M=money, S=service, I=information, F=food/material, D=dependency,
C=conflict, Inf=informal influence. 🟡 marks a hypothesized (not confirmed) relationship.

| | Students | MessComm | MessOffice | Warden | AcadOffice | Vendors | Staff | MessCell | Ping | Vindhya | PortalIT |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Students** | — | I (feedback, ✅exists/❓read) | M, D | — | D (schedule) | M, S | S | M, S, Inf | — | M, S (substitute) | I, D |
| **MessComm** | A, I | — | A | 🟡 overlap? | *no edge* | A (menu) | — | — | 🟡 (subject of coverage) | — | — |
| **MessOffice** | M, D | A (reports to?) | — | 🟡 overlap? | *no edge* | A, D (ordering) | A | — | 🟡 (subject of coverage) | — | I, D |
| **Warden** | — | 🟡 | 🟡 | — | *no edge* | A (contracts) | — | — | — | — | — |
| **AcadOffice** | D (schedule) | *no edge* | *no edge* | *no edge* | — | — | — | — | — | — | — |
| **Vendors** | S, F | A | A, D | A (contract) | — | — | A (manages) | — | — | C (competes for students) | — |
| **Staff** | S | — | A | — | — | A | — | — | — | — | — |
| **MessCell** | M, S, Inf | — | — | — | — | — | — | — | — | — | — |
| **Ping** | Inf (awareness) | 🟡subject | 🟡subject | — | — | — | — | — | — | — | — |
| **Vindhya** | M, S | — | — | — | — | C | — | — | — | — | — |
| **PortalIT** | I, D | — | I, D | — | — | — | — | — | — | — | — |

**The most important cells are the empty ones:** Academic Office has *no edge at all*
to Mess Committee, Mess Office, or Warden — three separate governance actors, zero
formal connection to the one office that controls the actual competing time constraint.
That's not a gap in this matrix; it's the matrix correctly showing a gap in the real
system.

---

## G. Flow Traces (condensed — full detail lives in `prathyusha_04-process-trace.md`)

- **Money:** Students → Mess Office (billing) → Vendors (per-mess, contract-based,
  mechanism ❓) . No money flows toward reducing waste — nobody is rewarded for a
  no-show being caught early.
- **Food/material:** Vendor procurement (4-day lead, ✅) → cooking → serving → (if
  unclaimed) → staff's own consumption (✅, confirmed) → true waste, if any, beyond that
  point is ❓ untraced.
- **Information:** Student intent → portal (or 🟡 an unofficial bot) → Mess Office → 4-day-old
  forecast → kitchen. Feedback ratings flow *in* (✅ confirmed to exist) but whether they
  flow *anywhere consequential* is ❓ — this is the single most consequential unresolved
  information-flow question in the whole register.
- **Decision/authority:** Mess Committee (policy) → Mess Office (execution) → Vendors
  (day-to-day). Warden's place in this chain specifically is ❓.
- **Feedback/complaint:** now known to have **two real channels** — an in-app per-meal
  rating (✅ exists) and public email (✅, user-confirmed) — plus Ping as an indirect
  public-pressure channel (✅ exists). All three converge on the same unresolved
  question: does any of them provably change a decision?
- **Waste:** cooked food → unclaimed → staff eat it (✅, confirmed, the one clean data
  point in this entire flow) → anything beyond that is ❓.

---

## H. Hidden / Overlooked Stakeholders

*"Stakeholders we would probably have missed without systems thinking."*

- **Mess Office**, specifically as distinct from Mess Committee — the single largest
  correction this round. Every prior document (including last session's stakeholder
  map) quietly merged "who decides" with "who executes," which hid a real internal
  governance split.
- **Unofficial tool developers** — invisible unless you specifically go looking at
  GitHub for a campus-specific mess API, which nothing in any interview would surface.
- **Ping** — a student publication is an obvious *category* of thing to check once
  named, but nothing in the interviews or screenshots pointed toward it; it only
  surfaced through direct web research.
- **The Portal/IT owner** — everyone interacts with `dining.iiit.ac.in` constantly and
  nobody (real respondent or synthetic persona) ever mentioned who runs it.
- **The 4-day procurement lead time itself** — not a person, but a hidden structural
  constraint that quietly determines how "responsive" any stakeholder *can* be,
  regardless of goodwill.

## I. Sleeping Stakeholders (high potential leverage, low current involvement)

- **Academic Office** — unchanged from last round, now reinforced: still zero edges to
  any mess-governance actor in the relationship matrix.
- **Mess Committee's faculty chair** — a real individual with cross-institutional
  standing that no student-only channel has. Nothing in any evidence shows this bridge
  being attempted, despite it being the most structurally plausible one available.
- **Ping** — has already published on mess issues twice; has not (as far as evidence
  shows) been used as a deliberate escalation *strategy* by students trying to change a
  specific policy, only as after-the-fact reporting.

## J. Conflict Map

| Conflict axis | Side A | Side B |
|---|---|---|
| Convenience vs. waste | Students (want flexible registration) | Mess Office (wants predictable, low-workload ordering — explicit motive for Dec 2024 policy) |
| Billing certainty vs. attendance uncertainty | Mess Office/Vendors (need a stable number to order against) | Students (attendance is genuinely uncertain day-to-day) |
| Cuisine preference vs. procurement efficiency | Students (🟡 apparent South Indian preference) | Vendors/Mess Committee (four fixed cuisine lines, not demand-responsive) |
| Academic schedule vs. meal schedule | Academic Office (owns class timing, no stake in mess outcome) | Students (bear the actual overlap cost) |
| Flexibility vs. workload | Students/Mess Cell (want more cancellation flexibility) | Mess Office (tightened rules in Dec 2024 specifically to *reduce* flexibility and staff workload) |

## K. Dependency Map (asymmetric dependencies flagged)

- Students depend on Vendors for food quality/timing; Vendors do **not** depend on any
  individual student — classic asymmetric dependency, consistent with why walk-in
  pricing can simply be set high with no negotiation.
- Vendors depend on Mess Office for a 4-day-old registration forecast; Mess Office
  depends on Students to register accurately — but nothing in the system *requires*
  accuracy (billing happens either way), so this dependency chain has a broken
  incentive at its weakest link (Students' side).
- Mess Committee depends on Mess Office to execute policy; Mess Office's stated
  motivation (workload reduction) doesn't obviously depend on the Committee at all —
  worth watching whether Mess Office effectively drives policy bottom-up rather than
  the reverse.

## L. Missing Relationships (logically expected, apparently absent)

- **Academic Office ↔ any mess-governance actor** — still the standing finding, now
  triple-confirmed empty (no edge to Committee, Office, or Warden).
- **Portal/IT owner ↔ Mess Committee** — a policy body setting rules with no visible
  direct line to the system that enforces them technically (Mess Office presumably
  mediates, but this itself is unconfirmed).
- **Vendors ↔ Students, direct** — all vendor-facing information seems to route through
  Mess Office/the portal; no evidence of vendors ever hearing from students directly
  (e.g., a vendor-specific feedback channel), which would matter if the cuisine-
  preference hypothesis (§B) is real and actionable.
- **Ping ↔ Mess Committee/Office, formal** — Ping's coverage exists but nothing shows it
  being treated as an official input channel, only as ambient public information.

## M. Research Gaps

**Critical before submission:**
| Gap | Evidence needed | Best interviewee | Question | Why it matters |
|---|---|---|---|---|
| Does feedback (rating, email, or Ping coverage) ever lead to a real change | A concrete example, either way | Role D (governance) | "Can you point to a specific mess policy that changed because of student feedback?" | Directly resolves the escalation-mechanism question, now that we know inputs exist |
| Cuisine-preference hypothesis (§B) | Direct student statements about mess choice reasoning | Role A/B (students) | "When you choose which mess to register at, what actually drives that choice?" | Could replace "Bakul is newer" as the primary explanation for the uptake gap |
| Mess Office ↔ Warden relationship | Direct account from either role | Role D | "How does the Mess Office's work relate to the Warden's — separate lanes, or overlapping?" | Resolves a genuine structural unknown in governance |

**Useful to validate:**
| Gap | Best interviewee | Why |
|---|---|---|
| Whether the Dec 2024 policy changes (weekly caps, no re-registration) are still in effect | Any student, or Guide 2 staff | Calibrates how much of the public-source research is current vs. historical |
| Real usage of the unofficial bot tool | Any student, informally | Determines whether "batch registration" should be reframed as "automated registration" |
| Who owns/maintains the portal | Role D, or IT-adjacent contact if accessible | Fills a structural gap in the information-flow trace |

**Interesting but optional:**
| Gap | Why it's lower priority |
|---|---|
| Facilities/estate team's exact identity | Real but not obviously load-bearing for the paradox itself |
| Guest-diner volume/impact | Marginal effect on capacity, unlikely to be a major lever |

## N. Interview Recruitment Plan (revised from the generic "students" ask)

- **P0 — absolutely necessary:**
  - Role A student (regular attender) — already planned, add the cuisine-preference
    question
  - Role B student (regular skipper) — already planned, same addition
  - Role D — Mess Committee or Warden contact, if reachable even briefly — this is now
    the single highest-value interview in the whole plan, since it's the only source
    that can resolve the feedback-efficacy question, the Mess Office/Warden
    relationship, and independently check the cuisine-preference hypothesis from the
    supply side
- **P1 — high value:**
  - Role C, specifically a **North Indian-line (Palash or Bakul) staff member** — can
    speak directly to whether low uptake reads as a demand problem from their side,
    which would support or undercut §B
  - Role C, a **South Indian-line (Kadamba) staff member** for contrast — already
    planned via Guide 2
- **P2 — useful if accessible:**
  - Anyone who has actually used the unofficial bot tool
  - A Ping writer/editor, if reachable, on whether mess coverage ever produced feedback
    from the Mess Committee/Office

## O. Final Systems-Thinker Audit

1. **Overlooked:** the Portal/IT owner remains a complete blank — the single weakest
   node in the whole register given how central it structurally is.
2. **Overestimating:** the unofficial bot tool (T2) — real, but its actual behavioral
   impact is pure speculation dressed as a stakeholder; keep it at low confidence.
3. **Collapsed too aggressively (corrected this round):** Friends/Roommates were
   wrongly treated as separate peripheral stakeholders last session — fixed in §A.
4. **Only inferred, no direct evidence:** Facilities/Estate team (F1) exists purely
   because a renovation must have *some* owner — nobody has named one.
5. **Assumed rather than observed:** the cuisine-preference hypothesis (§B) — strong
   pattern, zero direct testimony yet.
6. **Boundary choice hiding something:** the upstream food-supply chain (Lens C)
   remains almost entirely outside scope and almost entirely unevidenced — the
   project's stated boundary (registration-and-billing) may be too narrow if the real
   lever turns out to be cuisine/menu design rather than timing at all.
7. **Where is power located?** Mess Committee (faculty-chaired) and Mess Office
   (operational) jointly — Academic Office holds power over a *different* variable
   entirely and never exercises it here.
8. **Where is information located?** Mess Office (registration counts, ordering) and
   the unnamed Portal/IT owner — students hold intent-information nobody else has
   until the moment of registration, then lose visibility into what happens to it.
9. **Where is money located?** Students pay in, Mess Office/Vendors receive — no
   money flow currently rewards accuracy or waste reduction on any side.
10. **Where are consequences located?** Students (cost, hunger), vendors/staff (waste,
    workload) — Academic Office and Mess Committee's chair experience essentially none
    of the downstream consequences of the schedule/registration mismatch they each
    partially control.
11. **Experiences consequences but can't change causes:** Students, most directly —
    cannot change class timing or ordering lead times, only their own behavior within
    a fixed structure.
12. **Can change causes but doesn't experience consequences:** Academic Office, most
    starkly — total authority over class start time, zero exposure to the breakfast
    paradox it partially causes.
13. **Strongest misaligned incentive:** Mess Office is incentivized toward *less*
    flexibility (lower workload); students would benefit from *more* flexibility
    (accurate last-minute cancellation) — directly opposed, and the Dec 2024 policy
    change shows Mess Office's incentive winning in practice.
14. **Missing feedback loop:** nothing connects "a student rated a meal poorly" or
    "cuisine uptake is consistently lower for North Indian lines" back into menu
    planning in any confirmed way — two real feedback inputs exist, with an unconfirmed
    output on either end.
15. **Non-stakeholder system element with outsized influence:** the **4-day procurement
    lead time** — not a person, but it mechanically caps how responsive the entire
    system can ever be to same-day information, regardless of which stakeholder wants
    to act on it.

This register will be revised, not appended to, once P0 interviews land.
