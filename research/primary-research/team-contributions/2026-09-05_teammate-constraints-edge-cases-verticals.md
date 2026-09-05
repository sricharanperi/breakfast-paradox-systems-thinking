# Teammate Contribution — Constraints, Edge Cases & Research Verticals

**Submitted:** 2026-09-05, by a team member, pasted directly (not a screenshot). Archived here
verbatim in spirit (reformatted from the pasted text, no content added or removed) per the
project's standing rule of preserving every piece of team input. This is a **hypothesis
framework**, explicitly not verified fact — see the document's own framing below. It has been
integrated into `deliverables/phase-1/01-system-context-brief.md` (Skip Meal vs. Mess Cell
analysis, Behavioral/Research Verticals sections, new Role E, and new interview questions on
Roles B/C/D) — this file is the original, unedited source of that integration.

---

# Phase 1 · Supplementary — Constraints, Edge Cases & Research Verticals

**Puzzle:** The Breakfast Paradox `[Source: ProblemStatements.pdf]`
**Status:** DRAFT — hypothesis framework, not verified fact. Built from team reasoning
(2026-09-03 meeting transcript) plus one team member's direct account of the Skip Meal /
Mess Cell mechanism. **Purpose:** sharpen Role A–D interview questions before fieldwork,
per `01-system-context-brief.md` §8 methodology (fact-before-reason, no leading questions).
Everything below is a **hypothesis to test in interviews**, not a claim about what's true.

## 0. Core mechanism to test — Skip Meal vs. Mess Cell (a dominant-strategy problem)

**The insight (from team discussion, 2026-09-03):** the Skip Meal toggle exists, but using
it gives the student **nothing back** — no refund, no credit, nothing. It only reduces
kitchen waste. So for a student who already knows they won't eat — because of food quality,
not feeling like it, or any other reason — Skip Meal is a **strictly dominated** choice
compared to reselling the slot on the Mess Cell WhatsApp group, where they can recover some
or all of the money instead of recovering nothing.

**Why this matters more than "people forget to skip":** if this holds, low Skip Meal usage
isn't primarily a forgetfulness or awareness problem — it's a **rational response to how the
two options are priced.** Skip Meal = certain ₹0 return. Mess Cell resale = possible partial
or full return. A rational actor picks resale every time they have advance notice they won't
attend. This reframes the "underused Skip Meal toggle" from a UX/awareness issue to an
**incentive-design issue**: the toggle was built to solve the kitchen's waste problem, but it
asks the student to absorb 100% of the cost of solving it, while a peer-to-peer workaround
lets them absorb 0-?%. No wonder the informal market won by design, not by accident.

**This produces a testable prediction, not yet confirmed:**
- Students who decide *in advance* (know the night before, or days before) that they won't
  attend should overwhelmingly prefer Mess Cell over Skip Meal, if they know Mess Cell exists.
- Students who decide *last-minute* (overslept, ran out of time) have no time to use either —
  this is the group where the mess actually eats the loss (food cooked, no toggle, no resale).
- So the "food is registered but unclaimed and nobody profited from it" case should
  correspond specifically to **last-minute, unplanned no-shows** — not planned skips, since
  planned skips get siphoned into Mess Cell instead. If this is right, Skip Meal toggle usage
  should be *rare precisely because* it only ever gets used by the subset of planned-skippers
  who don't know about, don't trust, or can't be bothered with Mess Cell — a shrinking group.

## 1. Production Planning ("food getting over")

- **Constraint:** kitchens commit to a batch size before service starts; can't elastically
  cook more mid-service.
- **Hypothesis:** mess cooks to a *historical average / discounted-expectation* number, not
  to live registration count — meaning any day that beats the average runs short regardless
  of how much was technically registered.
- **Edge case — item-level vs. meal-level scarcity:** "food is over" may mean the popular
  item (eggs, a specific curry) ran out while base items (rice, idli) remained. Two very
  different problems wearing the same complaint.
- **Edge case — rush clustering, not true shortage:** if most eaters arrive in the last
  20-30 minutes before the 8:30 class cutoff, the *serving rate* becomes the bottleneck even
  if total quantity was adequate. Looks identical to a student as "food ran out."
- **Edge case — vendor dependency (Palash/Bakul):** these are supplied pre-cooked, not
  cooked on-site — a vendor under-order or delivery delay the night before is a single point
  of failure the on-site staff cannot correct same-day.
- **Edge case — special-day spikes:** Biryani-day-style demand breaks the averaging
  assumption on a per-day basis, not just a per-mess basis.

## 2. Temporal / Rush Dynamics

- Breakfast window 7:30-9:30, but effective window for 8:30-class students is closer to 60
  minutes.
- **Hypothesis — bimodal arrival:** early-birds (no class conflict), rush-cluster (racing
  the 8:30 bell), and late/no-class stragglers likely have different experiences of
  crowding and "availability" — worth asking which bucket a respondent falls in before
  interpreting their answer.
- **Edge case:** students with an 8:30 class may skip breakfast *entirely by design*, not by
  accident — a planned trade-off, not a failure mode.

## 3. Academic / Workload Calendar

- **Hypothesis (from transcript):** assignment deadlines due late night push sleep to
  3-5 AM, causing a missed *entire window*, not a 10-minutes-late miss. This is likely
  **cyclical** (clusters around specific weekdays/deadline patterns), not random noise.
- **Edge case — conscious vs. unconscious skip:** "slept through it" (unconscious) and
  "chose sleep over breakfast, awake enough to decide" (conscious trade-off) need different
  fixes — an alarm/notification helps only the first.

## 4. Social / Peer Effects

- **Hypothesis (Charan's point):** attendance may cluster by friend group — "if none of my
  friends are going, I skip too" — rather than being an independent per-student decision.
- **Edge case:** roommate/group registration mismatches — does one person's skip decision
  influence another's, and does that show up as coordinated Mess Cell listings (e.g., a
  group selling multiple slots together)?

## 5. Information / Awareness Gaps

- **Hypothesis:** low Skip Meal usage may be partly awareness (some students may not know
  it exists or what it does) layered on top of the incentive problem in §0 — worth
  separating "didn't know" from "knew but chose resale" in the data.
- **Edge case — cliff-edge behavior:** does hitting the 5-cancellations/month cap cause
  students to stop bothering to cancel/skip/sell for the *rest* of the month, even for
  meals they know they'll miss?
- **Edge case — Mess Cell as insider knowledge:** is the WhatsApp group genuinely
  accessible to everyone (e.g., new students, first-years), or is it an insider-only
  workaround that quietly disadvantages people who don't know it exists?

## 6. Economic / Incentive Structure (beyond §0)

- **Sunk-cost numbing:** once charged either way, the marginal cost of *not attending* is
  zero at decision time — this may weaken the incentive to show up independent of the
  Skip-Meal-vs-resale question above.
- **"Register just in case":** the 70-90% walk-in premium may push some students to
  register even when they expect to skip, purely to keep the cheaper option open — which
  would mean registration counts are inflated relative to true intended attendance *before*
  any no-show even happens.

## 7. Physical / Spatial & Environmental

- Distance from hostel to each of the 4 messes may correlate with attendance more than food
  quality does — worth capturing which mess is "home" for a respondent.
- Bakul's warehouse-conversion identity/ambience may suppress uptake independent of the
  capacity/novelty hypothesis already in the brief (§3) — a perception factor, not just a
  supply-side one.
- Weather (monsoon walk to mess), and Kadamba-specific queue/seating crowding as a deterrent
  distinct from "food ran out."

## 8. Governance / Decision Latency

- Menu is set ~1 month ahead with student input (per brief §3) — does that input loop ever
  reach the *quantity-to-cook* decision, or only the *what's-on-the-menu* decision? These
  may be entirely separate decision paths inside the mess committee.

## Suggested new research role

**Role E - Rush/Latecomer** (attends, but consistently arrives in the last 20-30 minutes):
isolates the queueing/rush-crowding hypothesis (§1-2) from the skip/no-show hypothesis,
since current Role A ("mostly line up") and Role B ("frequently doesn't attend") don't
capture someone who *does* eat but regularly experiences scarcity/crowding as a result of
when they arrive, not whether they show up.

## Still missing — before this can inform Activity 2

- [ ] Role A/B/C/D interviews, now including the §0 Skip-Meal-vs-Mess-Cell questions
- [ ] Direct confirmation from a mess staff member (Role C) of what quantity they actually
      cook to — this is the single most load-bearing unconfirmed hypothesis in this document
- [ ] Any rough day-of-week / deadline-calendar correlation with skip behavior (§3)
- [ ] Whether Mess Cell is genuinely open-access or informally gatekept (§5)
