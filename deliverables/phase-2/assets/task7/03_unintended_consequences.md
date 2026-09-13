# Task 7 — Supporting Asset: Unintended Consequences

Distinguishes OBSERVED (evidenced in the interview/braindump/poster data) from HYPOTHESIZED (plausible given
the structures, not yet observed).

## UC1 — Monthly Billing Decoupled from Attendance (OBSERVED)

- **ORIGINAL ACTION:** Bill students monthly based on registration, not per meal attended.
- **INTENDED PURPOSE:** Administrative simplicity; predictable revenue for the mess/vendor.
- **FIRST-ORDER EFFECT:** Students register without needing to reconfirm daily.
- **BEHAVIOURAL RESPONSE:** Some students register out of habit/default regardless of actual intent to eat (E1).
- **SECOND-ORDER EFFECT:** A visible gap opens between registration numbers and turnout, concentrated in
  breakfast specifically (E4).
- **UNINTENDED CONSEQUENCE:** Procurement planning (locked at T-4, ST3) is built on a demand signal that is
  known, by the office that owns it, to overstate actual attendance by roughly 60-65% for breakfast (E4).
- **WHO BENEFITS:** Administrative simplicity is preserved; vendor has a stable minimum-order guarantee.
- **WHO BEARS THE COST:** Students who pay for uneaten meals; the kitchen absorbs the planning uncertainty
  that the numbers can't resolve.
- **EVIDENCE:** E1, E4, ST1, ST3.
- **CONFIDENCE:** ✅ CONFIRMED as a structural fact (billing model, turnout gap); 🟡 PLAUSIBLE as a full causal
  story connecting the billing model specifically to the size of the gap (other factors like food quality
  and schedule also contribute, per P5).

## UC2 — Cancellation Cap Intended to Reduce Admin Load (OBSERVED, single-sourced)

- **ORIGINAL ACTION:** Cap cancellations at 5/month (E6).
- **INTENDED PURPOSE:** Presumably to reduce administrative/vendor-notification overhead from frequent
  cancellations, and to discourage casual last-minute flip-flopping.
- **FIRST-ORDER EFFECT:** Students who exceed the cap can no longer formally signal non-attendance.
- **BEHAVIOURAL RESPONSE:** Non-attendance beyond the cap is either absorbed silently (no signal reaches the
  kitchen at all) or redirected into the informal resale channel (E7, ST9).
- **SECOND-ORDER EFFECT:** The formal system's non-attendance signal becomes systematically incomplete —
  understating true non-attendance by exactly the amount the cap excludes.
- **UNINTENDED CONSEQUENCE:** A rule meant to reduce noise in the system instead pushes real information
  (who isn't actually coming) into an informal, institutionally invisible channel (Mess Cell WhatsApp),
  which is arguably worse for planning than if all non-attendance were visible even if administratively
  noisier.
- **WHO BENEFITS:** Whoever set the cap avoids the administrative cost of unlimited cancellations.
- **WHO BEARS THE COST:** Kitchen/procurement, which loses visibility into the true scale of non-attendance;
  students who exceed the cap and have no formal outlet.
- **EVIDENCE:** E6, E7.
- **CONFIDENCE:** 🟡 PLAUSIBLE — the cap's existence and the resale channel's existence are each individually
  evidenced; the causal link between the two (that the cap specifically drives resale volume, rather than
  resale existing for other reasons) is inferred, not directly stated by any respondent.

## UC3 — Advance Menu Transparency Intended to Improve Trust/Satisfaction (HYPOTHESIZED, self-identified risk)

- **ORIGINAL ACTION:** Post the menu rotation in advance (part of the governance process behind loop B3).
- **INTENDED PURPOSE:** Build trust, let students plan, respond to demand for variety (S5 §8).
- **FIRST-ORDER EFFECT:** Students can see upcoming menus.
- **BEHAVIOURAL RESPONSE (HYPOTHESIZED):** Selective attendance concentrated on days with preferred items
  (E8 — this is the CFS Chair's own stated concern, not yet observed in student data).
- **SECOND-ORDER EFFECT (HYPOTHESIZED):** Demand becomes less evenly distributed across the week than it
  would be without visibility, making the T-4 aggregate registration number a worse predictor of any
  single day's actual turnout.
- **UNINTENDED CONSEQUENCE (HYPOTHESIZED):** A transparency measure meant to build trust could make
  day-to-day demand harder to forecast, straining the same procurement pipeline (ST3) that transparency was
  never meant to affect.
- **WHO WOULD BENEFIT:** Students, on the days they most want to attend.
- **WHO WOULD BEAR THE COST:** Kitchen planning, and potentially other-day attendees facing under-provisioning
  on "less popular" days.
- **EVIDENCE:** E8 only.
- **CONFIDENCE:** ❓ UNKNOWN-REQUIRES VALIDATION — this entire entry is a hypothesis one institutional actor
  has flagged about their own policy; it is not confirmed by any independent data source in this evidence set.

## UC4 — Locking Procurement at T-4 to Guarantee Vendor Lead Time (OBSERVED)

- **ORIGINAL ACTION:** Lock registration numbers 4 days before serving for vendor procurement (E3).
- **INTENDED PURPOSE:** Give the vendor enough lead time to source ingredients reliably.
- **FIRST-ORDER EFFECT:** Any registration change in the last 4 days (a student deciding not to attend, a
  new student registering) cannot be reflected in that day's procurement.
- **BEHAVIOURAL RESPONSE:** Kitchen must plan to the T-4 aggregate rather than to any more current signal.
- **SECOND-ORDER EFFECT:** The 35-40% breakfast turnout figure (E4) becomes, structurally, the best the
  system can do — not because no one measured better, but because the timing of the freeze makes finer-
  grained response mechanically impossible regardless of what Skip Meal or resale data shows same-week.
- **UNINTENDED CONSEQUENCE:** A lead-time rule meant to serve the vendor's operational needs incidentally
  caps how responsive the entire registration-to-plate pipeline can ever be, regardless of what other
  balancing mechanisms (Skip Meal, resale) are layered on top.
- **WHO BENEFITS:** Vendor (predictable sourcing window).
- **WHO BEARS THE COST:** Everyone downstream of the freeze — kitchen (stuck with stale numbers), students
  (registration changes late in the week have no effect on that week's provisioning).
- **EVIDENCE:** E3, E4, E9.
- **CONFIDENCE:** ✅ CONFIRMED (the structural mechanism); 🟡 PLAUSIBLE (that this specific rule, rather than
  something else, is the binding constraint on responsiveness — an alternative explanation is explored in
  `../../07-systemic-problem-analysis.md`, the consolidated Systemic Problem Analysis).

## UC5 — Splitting Waste into Production/Plate Streams with External Compost (HYPOTHESIZED benefit; OBSERVED mechanism)

- **ORIGINAL ACTION:** Track production waste and plate waste as separate streams, route to external compost
  and food-safety sampling (E15, S5 §10).
- **INTENDED PURPOSE:** Food safety compliance and (presumably) waste-reduction visibility.
- **FIRST-ORDER EFFECT:** Waste is at least categorically tracked, unlike attendance-gap waste which is not
  quantified in this evidence set.
- **POSSIBLE UNINTENDED CONSEQUENCE (HYPOTHESIZED, not evidenced):** Categorical tracking (does waste exist,
  is it safe to dispose of) may not translate into volume-level tracking usable for demand forecasting — i.e.,
  a system can be fully compliant on food safety while still having no feedback loop from waste volume back
  to registration policy (see `06_feedback_gaps.md`, gap on waste→registration).
- **EVIDENCE:** E15 for the mechanism; the "unintended consequence" itself is not evidenced, only plausible
  given the absence of any waste→policy feedback structure found in the evidence set.
- **RESOLVED, 2026-09-13:** the user directly confirmed there is no formal waste-reduction policy connecting
  waste back to procurement or registration decisions. UC5 is upgraded from HYPOTHESIZED to **OBSERVED**: the
  categorical tracking exists (compost/lab-sampling), and the absence of a volume-level feedback link is now
  a confirmed fact, not an inference. This is the supply-side twin of UC1/UC2 — see loop R6 in
  `02_causal_loop_diagram.md`.

## UC6 — Decoupled Billing May Also Insulate Vendor Revenue From Attendance (ASSUMED, new 2026-09-13)

- **ORIGINAL ACTION:** Bill/pay based on registration (or a fixed contract volume), not attendance or
  satisfaction.
- **INTENDED PURPOSE:** Predictable vendor revenue, administrative simplicity (same as UC1).
- **FIRST-ORDER EFFECT:** Vendor payment is plausibly unaffected by whether registered meals are actually
  eaten or enjoyed.
- **BEHAVIOURAL RESPONSE (ASSUMED):** Reduced vendor incentive to protect quality against falling attendance,
  since revenue doesn't track it either — a symmetrical effect to the student-side incentive problem RC1
  already names.
- **SECOND-ORDER EFFECT (ASSUMED):** A vendor facing thin or fixed margins may substitute cheaper ingredients
  or reduce variety without facing a revenue consequence, compounding the very quality issues that (per
  Cluster D's health/social findings) independently depress breakfast attendance.
- **UNINTENDED CONSEQUENCE:** A billing model designed to protect institutional administrative simplicity may
  also be quietly protecting vendor revenue from a quality-attendance feedback loop that would otherwise
  discipline it — see loop R5.
- **WHO BENEFITS:** The vendor, via protected revenue regardless of attendance or quality choices.
- **WHO BEARS THE COST:** Students (quality), and the institution (a compounding, currently invisible
  contributor to the very attendance gap it is trying to explain).
- **EVIDENCE:** 🔷 ASSUMED throughout — not directly evidenced by any interview, but tightly consistent with
  confirmed billing mechanics and open-tender vendor contracting.
- **CONFIDENCE:** 🔷 ASSUMED.

## UC7 — A Working Fix Exists But Is Retired Once Its Trigger Passes (OBSERVED, new 2026-09-13)

- **ORIGINAL ACTION:** Relax registration to a non-compulsory, walk-in, attendance-tracked model during
  holidays and the LPG shortage (loop B4).
- **INTENDED PURPOSE:** Cope with a short-term demand-uncertainty spike.
- **FIRST-ORDER EFFECT:** The exact registration-attendance gap this project has spent most of its effort
  explaining does not occur under this model — billing tracks actual consumption.
- **BEHAVIOURAL RESPONSE:** The institution returns to the standing, decoupled-billing model once the
  triggering condition passes.
- **SECOND-ORDER EFFECT:** A demonstrably working alternative sits inside the institution's own operating
  history without, so far as this evidence shows, ever being evaluated for partial or permanent adoption.
- **UNINTENDED CONSEQUENCE:** The very success of the shock-adaptive model may be *why* it's never
  reconsidered as a standing option — it was built and framed as an emergency measure, not a policy
  alternative, so its success doesn't naturally prompt the question "should we just do this all the time?"
- **WHO BENEFITS:** Vendor procurement certainty, under the standing model.
- **WHO BEARS THE COST:** Everyone affected by the standing model's registration-attendance gap, every day
  that isn't a holiday or a shortage.
- **EVIDENCE:** ✅ CONFIRMED as historical fact (direct user statement, 2026-09-13); the "why it's never
  reconsidered" framing is 🔷 ASSUMED.
- **CONFIDENCE:** ✅ CONFIRMED mechanism; 🔷 ASSUMED interpretation. This is the single most consequential
  unintended consequence in the report — see Task 7 Finding F1.
- **CONFIDENCE:** ✅ CONFIRMED mechanism; ❓ UNKNOWN-REQUIRES VALIDATION for the consequence claim.
