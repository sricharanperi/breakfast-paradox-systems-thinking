# Task 7 — Supporting Asset: Structural Root Cause Analysis + Network

Not a mechanical 5-Whys chain. Each candidate is run through the 8-question diagnostic and the ROOT-CAUSE
TEST template. Candidates that only explain one symptom, or that are themselves downstream of something more
structural, are demoted to "intermediate mechanism" rather than labelled root cause.

## Candidate Root Structures

### RC1 — Billing/Registration Decoupled from Attendance (ST1)

- **CANDIDATE:** The billing model charges for registration, not attendance.
- **SYMPTOMS EXPLAINED:** Ghost registration (P1), cancellation underuse relative to true non-attendance (P2).
- **PATTERNS EXPLAINED:** P1, P2.
- **MECHANISM:** Removing per-meal cost consequence from non-attendance removes the main lever that would
  otherwise make registration track intent.
- **STRUCTURE MAINTAINING IT:** Administrative simplicity of monthly billing; no per-meal metering
  infrastructure evidenced to exist.
- **ACTORS:** Mess Committee/CDS (sets billing policy), students (respond to its incentive structure).
- **EVIDENCE:** ST1, E1, cross-corroborated independently by S7 (Neha's parallel draft identifies the same
  structural cause).
- **COUNTEREVIDENCE:** None found against the mechanism itself; P5 shows non-billing factors (habit, quality
  history, visibility) also drive skipping, so billing decoupling is not the *only* driver.
- **CONFIDENCE:** ✅ CONFIRMED as a structure; 🟡 PLAUSIBLE as a full explanation of the *size* of the gap (other
  factors contribute).
- **IF REMOVED, WOULD THE PROBLEM DISAPPEAR:** Partially — per-meal billing would likely shrink ghost
  registration, but P5's evidence shows some skipping (habit, taste, visibility, non-daily schedule
  conflicts) is not price/billing-driven and would persist regardless.
- **INTERACTIONS WITH OTHER ROOT CAUSES:** Directly enables RC2 (T-4 lock has to plan against inflated numbers
  because RC1 doesn't discipline registration accuracy in the first place).

### RC2 — Temporal Rigidity of the T-4 Procurement Lock (ST3)

- **CANDIDATE:** Registration is frozen 4 days before serving for vendor procurement.
- **SYMPTOMS EXPLAINED:** Persistence of the registration-attendance gap regardless of any same-week
  correction mechanism (Skip Meal, resale).
- **PATTERNS EXPLAINED:** P1 (structurally caps how correctable it can ever be).
- **MECHANISM:** Even a perfectly honest, fully-updated registration signal on day-of would not reach
  procurement — the lock happens too early in the cycle.
- **STRUCTURE MAINTAINING IT:** Vendor contract terms requiring lead time (institutional/commercial
  constraint, not a student-behavior issue).
- **ACTORS:** CDS/vendor contract, kitchen.
- **EVIDENCE:** E3, E9.
- **COUNTEREVIDENCE:** None found; this is stated plainly by the CFS Chair as an operational necessity, not
  disputed anywhere in the evidence set.
- **CONFIDENCE:** ✅ CONFIRMED.
- **IF REMOVED, WOULD THE PROBLEM DISAPPEAR:** No — shortening the lock would improve responsiveness to
  RC1's inflated numbers, but would not remove the underlying incentive (RC1) that inflates them in the
  first place. Removing RC2 alone treats a symptom of RC1, not RC1 itself.
- **INTERACTIONS:** Downstream of / compounds RC1. Also interacts with RC3 (fragmented decision rights mean
  no single actor is positioned to renegotiate the lead time against the billing model).

### RC3 — Fragmented Decision Rights Across Menu, Kitchen Execution, and Academic Timetable (ST6)

- **CANDIDATE:** No single actor owns "actual attendance" as an outcome — menu (Mess Committee, ~1 month out),
  daily execution (kitchen/vendor), and academic scheduling (explicitly outside mess governance) are each
  decided independently.
- **SYMPTOMS EXPLAINED:** Why the problem persists across multiple governance-side improvements (menu
  rotation, transparency, feedback mechanisms) that each work within their own silo but don't touch the
  registration-attendance gap.
- **PATTERNS EXPLAINED:** Indirectly explains why P1 hasn't been resolved despite B3 (menu governance loop)
  functioning well — a well-functioning menu loop cannot fix a registration-incentive problem it doesn't
  own.
- **MECHANISM:** Structural fragmentation means improvements accumulate within silos without ever
  addressing the cross-cutting registration/billing/procurement chain.
- **STRUCTURE MAINTAINING IT:** Institutional org design (Mess Committee, Warden, kitchen/vendor, academic
  office as four separate authorities); confirmed explicitly that academic office has no say in mess
  timings/hostel matters.
- **ACTORS:** Mess Committee, Warden, kitchen/vendor, academic office.
- **EVIDENCE:** S1 (confirms academic office exclusion), S5 (confirms Mess Committee's scope is menu, not
  billing/procurement policy).
- **COUNTEREVIDENCE:** B3's success (a fully confirmed, closed loop) shows fragmentation does not prevent
  *all* improvement — it prevents improvement specifically on cross-cutting issues like the registration gap.
- **CONFIDENCE:** ✅ CONFIRMED (the fragmentation itself); 🟡 PLAUSIBLE (that fragmentation, rather than simple
  inattention, is *why* RC1/RC2 haven't been addressed — an alternative explanation, e.g. "no one has
  prioritized it yet," is considered in the main file's Section 23).
- **IF REMOVED, WOULD THE PROBLEM DISAPPEAR:** Unknown — unifying decision rights is necessary but not
  sufficient; it would create the *possibility* of addressing RC1/RC2 together, not guarantee it.
- **INTERACTIONS:** Sits structurally "above" RC1 and RC2 — it is why no one actor has both the information
  (RC1's gap size, known to CFS Chair) and the authority (billing policy) to close the loop.

### RC4 — Information Fragmentation Between Aggregate Data and Actionable Granularity (ST4, ST5)

- **CANDIDATE:** Feedback exists (CFS Chair knows the turnout split; a feedback mechanism exists per S5 §7)
  but only at a level too coarse to change day-to-day or per-student behavior, compounded by public-facing
  information inconsistency (the two-domain portal contradiction, E11).
- **SYMPTOMS EXPLAINED:** Why known institutional knowledge (the 35-40% figure) hasn't visibly translated
  into a registration-policy change.
- **MECHANISM:** Category-level knowledge without a channel to act on it at the registration-design level.
- **STRUCTURE MAINTAINING IT:** No evidenced mechanism connecting CFS Chair's aggregate knowledge to
  registration-policy redesign authority (which may itself sit with a different actor — unconfirmed, see
  validation gaps).
- **ACTORS:** CDS/CFS office (holds the data), whichever actor owns registration-policy design (unconfirmed).
- **EVIDENCE:** E4, E11, ST4.
- **COUNTEREVIDENCE:** None found.
- **CONFIDENCE:** 🟡 PLAUSIBLE — the coarseness of feedback is confirmed; that this coarseness (rather than a
  deliberate choice or a resourcing constraint) is why nothing has changed is inferred, not directly stated.
- **IF REMOVED, WOULD THE PROBLEM DISAPPEAR:** Partially — better information alone doesn't fix RC1's
  incentive structure, but it would let *someone* connect cause to fix.
- **INTERACTIONS:** Compounds RC3 (fragmented rights mean even good information has no clear owner to act on
  it).

## Root Cause Test Summary Table

| Candidate | Structural (not a symptom label)? | Upstream of ≥2 patterns? | Would pattern persist unchanged if removed? | Verdict |
|-----------|-----------------------------------|----------------------------|---------------------------------------------|---------|
| RC1 — Billing/registration decoupling | ✅ Yes | ✅ Yes (P1, P2) | Partially — some non-billing skip reasons persist | **Root cause** |
| RC2 — T-4 procurement lock | ✅ Yes | Partial (P1 only, and only its correctability) | Yes — RC1's incentive would remain | **Intermediate mechanism**, not primary root cause — it compounds RC1 rather than independently generating the pattern |
| RC3 — Fragmented decision rights | ✅ Yes | ✅ Yes (explains persistence across RC1, RC2, and why governance wins like B3 don't transfer) | Unknown — necessary but not sufficient | **Root cause** (structural, meta-level) |
| RC4 — Information fragmentation | ✅ Yes | Partial | Partially | **Contributing structural factor**, not independently sufficient — folded into RC3's diagnosis as a symptom of the same fragmentation rather than treated as a fully separate root cause |

## Root Cause Network

```
RC1 (Billing/registration decoupled from attendance)
   │  produces
   ▼
Ghost registration incentive (individual level)
   │  interacts with
   ▼
RC2 (T-4 procurement lock) ── compounds RC1: even honest late signals can't reach procurement
   │  produces
   ▼
Registration-attendance gap persists as a structural ceiling (P1)
   │  visible only as
   ▼
Category-level turnout figures (35-40% breakfast) — known to CFS Chair (RC4: information fragmentation)
   │  cannot reach
   ▼
Registration-policy redesign authority — because:
   ▲
   │  root-caused by
RC3 (Fragmented decision rights: menu / kitchen execution / academic timetable / billing-procurement
     each owned separately, none owning "close the attendance gap")
```

**RC1 ↔ RC3 interaction:** RC3 is why RC1 hasn't been revisited even though its effects (P1, P2) are visible
and quantified — no actor holds both the incentive-design lever (billing policy) and full accountability for
the attendance outcome.

**RC2 ↔ RC4 interaction:** The T-4 lock and information coarseness compound each other — even if information
were finer-grained, the T-4 lock would still prevent it from being actioned in the same cycle.
