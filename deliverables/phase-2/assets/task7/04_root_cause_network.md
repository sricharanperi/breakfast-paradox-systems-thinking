# The Breakfast Paradox — Unintended Consequences, Structural Root Causes, and Systemic Tensions

**Purpose of this file.** A ground-up rebuild of three analytical sections for the IIIT Hyderabad Breakfast Paradox capstone, derived directly from primary evidence rather than copied from `deliverables/phase-2/07-systemic-problem-analysis.md` or `06-system-map.md`. Those two documents are treated as **one input among several** — every claim in them has been re-traced to its underlying source (interview transcript, braindump, or poster transcription) and re-tested, not restated. Where this rebuild agrees with the existing deliverables, that agreement is because independent re-derivation converged on the same answer, not because the answer was copied.

**Sources used, read in full:** `MASTER_CONTEXT.md` (session log + decision log + mistakes log); `research/primary-research/interviews/2026-09-03_student-self-account-and-mess-system-overview.md`; `research/primary-research/interviews/2026-09-06_five-student-interviews-guide1.md`; `prathyusha_braindump.md`; `prathyusha_braindump_2.md`; `deliverables/phase-2/06-system-map.md`; `deliverables/phase-2/07-systemic-problem-analysis.md`.

**Evidence tagging.** This project's established discipline (`MASTER_CONTEXT.md` §7, D-35) is a four-tier prose vocabulary: **confirmed** (directly stated by a named source, or independently corroborated), **single-sourced** (one respondent/account, not cross-checked), **candidate** (a plausible, named mechanism not yet independently verified), **assumed** (an explicitly-authorized systems-thinking inference, never carrying the weight of a confirmed claim). The task brief for this document asks additionally for an **OBSERVED / HYPOTHESIZED** split. Rather than run two incompatible tagging systems, this file maps them onto one axis and states both on every claim:

| This file's tag | Maps to project's tier | Meaning |
|---|---|---|
| **OBSERVED — confirmed** | confirmed | Directly stated by a named respondent/source, or independently corroborated by two sources |
| **OBSERVED — single-sourced** | single-sourced | Directly stated, but by only one account, not cross-checked |
| **HYPOTHESIZED — candidate** | candidate | A named, plausible mechanism, logically implied by confirmed facts, not yet directly verified |
| **HYPOTHESIZED — assumed** | assumed | A systems-thinking inference used to widen the analysis honestly; weakest tier |

Nothing below is asserted more strongly than its tag supports. The fictional Rohan/Adit puzzle brief (`ProblemStatements.pdf`) is not used as evidence anywhere in this file.

---

## PART 2 — STRUCTURAL ROOT CAUSES

### 2.1 Method

Each candidate is run through four tests before being called a root cause:
1. **Structural test** — is it a rule, incentive, information flow, decision right, or physical/organizational/temporal/resource structure, not an individual's behavior or a symptom restated?
2. **Breadth test** — does it explain multiple, independently observed patterns, not just one?
3. **Counterfactual test** — would the pattern plausibly persist if this cause were removed, or would it collapse?
4. **Evidence test** — is it evidenced (confirmed/single-sourced), or does it rest on assumption alone?

Candidates that pass all four are **root causes**. Candidates that are real and structural but demonstrably downstream of / caused by a root cause, or that only explain a narrow slice of the pattern, are labeled **intermediate mechanisms** — real, worth naming, but not where the leverage is.

### 2.2 Root Cause 1 — Billing is decoupled from attendance (a registration-triggered, not consumption-triggered, cost)

- **Structural test:** passes. This is a rule about *when* the financial obligation is created — at registration, not at the plate.
- **Breadth test:** passes, broadly. It explains: the incentive to over-register (§1.1); why Skip Meal has no adoption despite working (§1.3, direct quote — "it doesn't return the money"); why a cancellation cap is needed at all (there would be little to cancel if cost tracked attendance); why the Mess Cell resale market exists (recovering value a decoupled bill doesn't); why waste is generated at the volume it is; and why a vendor might have a quiet interest in the standing model (§1.7). Six independent symptoms trace to one rule.
- **Counterfactual test:** passes, and unusually for this kind of analysis, **the counterfactual has actually been run** — the LPG-shortage/holiday exception (§1.5) is a real, confirmed instance of attendance-based billing operating at IIIT-H, and it visibly closed the gap it replaced. This is the strongest possible evidence a root-cause claim can have: not "if we removed this, X would probably not happen," but "when this was removed, X did not happen."
- **Evidence test:** **OBSERVED — confirmed.**

### 2.3 Root Cause 2 — Decision rights over the registration-attendance outcome are fragmented across four domains, with no actor holding both the authority and the incentive to fix it end-to-end

- **What it is:** menu content (CDS Committee), kitchen execution/procurement (vendor, under a lead-time contract), academic scheduling (Academic administration — confirmed to hold *zero* formal or informal relationship with any mess-governance actor), and billing/registration policy itself (nominally CDS/CFS, but per Task 3's power-analysis finding, its authority over registration/billing *policy specifically* is unconfirmed) are four separate loci of control.
- **Structural test:** passes — this is a decision-rights/organizational structure, not a behavior.
- **Breadth test:** passes. It explains: why the CFS Chair can name the exact size of the turnout gap and yet it has **never reached a registration or billing policy discussion** (confirmed directly, 2026-09-13); why the proven shock-adaptive fix (RC1's counterfactual) has never been evaluated for standing adoption even though it demonstrably works; why the 8:30 AM class-time collision persists despite being named as a friction point in nearly every skip-reason interview, since the one actor who could move it (Academic administration) has no channel connecting it to mess outcomes at all; and why the menu-rotation win (§1.4) required threading through a *specific* consultative pathway (Student Council → Committee) that the billing/registration question has apparently never been routed through.
- **Counterfactual test:** passes — a single actor holding both the CFS Chair's knowledge *and* registration-policy authority would very plausibly have already evaluated the shock-adaptive precedent for wider use, given it is already proven and already known.
- **Evidence test:** **OBSERVED — confirmed** ("confirmed this pass as the reason," per the CFS Chair's direct 2026-09-13 statement that awareness never reached policy discussion).

### 2.4 Root Cause 3 — Institutional attention is triggered by complaint *intensity*, not by data *severity* (a systems-visible synthesis, not previously named this crisply in either existing deliverable)

- **What it is:** the confirmed CDS/CFS escalation design routes **high-intensity feedback** to a CDS Committee member for action, and **low-intensity feedback** to the CFS Head for direct, uncommitteed handling. This is a rule about *what counts as worth escalating* — and it is calibrated to how loudly and individually a problem is felt, not to its aggregate cost.
- **Why this is distinct from Root Cause 2:** RC2 is about *who has the authority* to act. RC3 is about *what gets an actor's attention in the first place*, independent of who holds the authority. Even a hypothetical single, empowered owner of the registration-billing outcome would still need a signal loud enough to trigger action under this design — and a quietly deducted monthly overcharge generates no such signal, however large its aggregate size.
- **Breadth test:** passes. It explains the sharpest paradox inside this project's own evidence: **menu fatigue** (an individually, repeatedly, viscerally felt daily annoyance) generated enough complaint intensity to travel the full Student Council → Committee pathway and produce a real policy change (§1.4) — the project's only confirmed, fully closed governance loop. **The registration-billing gap** (a quiet, once-a-month, diffuse cost, never experienced as a single sharp moment of frustration the way a bad meal is) has never generated comparable intensity, *despite being larger in aggregate cost and already quantified by the one office positioned to know it.* Waste's invisibility (§1.6) is the same mechanism again: there is no volume metric, so there is no data to escalate even if the design *did* respond to data — the absence of a data-triggered pathway means the absence of a metric is never itself a problem worth fixing.
- **Counterfactual test:** passes. If escalation triggered on quantified aggregate cost as well as on complaint volume, a confirmed, named, precisely-sized gap sitting on the CFS Chair's own desk is exactly the kind of item that would very plausibly have already been escalated.
- **Evidence test:** **OBSERVED — confirmed** for the escalation-design mechanism itself (directly described by the CFS Chair) and for its two contrasting outcomes (B3 succeeded, RC1 never escalated); **HYPOTHESIZED — candidate** for "this is *why*" as the general causal law, since no source states the design principle in those exact terms — it is a synthesis across two confirmed facts, not a single quoted mechanism.

### 2.5 A compounding, lower-confidence candidate root cause — the vendor's economic interest in the standing model

- Registration-based billing guarantees the vendor predictable revenue regardless of whether registered students actually attend (§1.7). This gives the vendor a plausible, independent interest in **not** having the standing model replaced by the shock-adaptive alternative it already knows works.
- **Structural test:** passes (an incentive structure).
- **Breadth test:** partial — it compounds RC1's persistence and helps explain why RC1 survives even when a working alternative exists, but it does not by itself generate the original registration-attendance gap (student behavior under RC1 does that).
- **Counterfactual test:** unclear without contract-term data (the open item "is the tender contract fixed-price or cost-passthrough" is unresolved).
- **Evidence test:** **HYPOTHESIZED — assumed.** Included as a compounding factor in the network below, not counted among the three primary root causes, precisely because it fails the evidence test at anything above "assumed."

### 2.6 Intermediate mechanisms — real and structural, but downstream, not independently root

| Mechanism | Why it is real and structural | Why it is demoted, not promoted |
|---|---|---|
| **The T-4 procurement/sourcing lock** | A genuine timing rule capping how responsive ingredient sourcing can be to last-minute signals. | Fails the breadth test on its own: Skip Meal operates *after* this lock (same-week) and still has near-zero uptake, meaning the core registration-attendance gap survives even where the T-4 lock isn't the binding constraint. It is downstream of two things: the vendor's need for lead-time certainty (itself downstream of the outsourcing/contracting choice, §1.7) and RC1's institutional preference for procurement certainty over demand-matching accuracy (the explicit trade-off named in Root Cause 1's own counterfactual). |
| **Aggregate-only, average-based demand information reaching the kitchen** | A real information-granularity limitation: the kitchen portions against an average-consumption assumption applied uniformly across items with very different demand skew (this is the most plausible explanation, per the System Map's own reasoning, for why high-demand items like biryani, idli, puri, and bhatura run out even when *overall* attendance is only 35–45%). | Downstream of RC1 (the only demand signal generated by the system is an aggregate registration count, a direct byproduct of billing being count-based) compounded by RC3 (there has never been institutional pressure to build a finer-grained signal, because the run-out pattern generates individual, per-morning frustration rather than an aggregated, escalatable metric). Removing this mechanism alone (better portioning math) would likely reduce run-outs without touching the registration-attendance gap itself — narrow scope, not a root cause of the paradox as a whole. |
| **The cancellation cap (in either direction)** | A real administrative throttle with real, documented effects (§1.2). | It is a coping/throttling mechanism layered on top of RC1's incentive to over-register — it manages the *symptom volume*, it does not touch the underlying cost structure that produces the volume. Tightening or loosening it moves where the pressure leaks out (formal cancellation vs. informal resale vs. silent no-show), not whether the pressure exists. |
| **Three-tier pricing gap (Student < Card < Spot)** | A real, confirmed incentive amplifier (§1.1). | It intensifies RC1's effect but would have no incentive-shaping power at all if billing were attendance-based rather than registration-based — it is entirely parasitic on RC1, not an independent cause. |

### 2.7 The root-cause network — how these interact and compound

```
                         ┌────────────────────────────────────────┐
                         │  RC2 — Fragmented decision rights        │
                         │  (menu / execution / academic / billing) │
                         └───────────────┬──────────────┬──────────┘
                                         │              │
                     gates whether a     │              │  Academic admin holds the timing
                     known gap becomes   │              │  lever, has zero channel to mess
                     a decision at all   │              │  governance → arrival clustering
                                         ▼              ▼
   ┌─────────────────────────┐   ┌─────────────────────────────┐
   │ RC3 — Attention triggers │◄──┤  Known gap never escalated,  │
   │ on complaint intensity,  │   │  even though quantified      │
   │ not data severity        │   │  (CFS Chair, 2026-09-13)      │
   └───────────┬──────────────┘   └─────────────────────────────┘
               │ suppresses pressure to fix ▲
               │                            │ symmetric: same design
               ▼                            │ explains why B3 (loud,
   ┌─────────────────────────┐              │ individually-felt) succeeded
   │ RC1 — Billing decoupled  │──────────────┘
   │ from attendance          │
   └───────────┬───────────┬─┘
               │           │
   generates   │           │  removes marginal cost of
   the incentive│          │  inaccurate registration for
   to over-     │          │  BOTH student (register freely)
   register     │          │  AND vendor (revenue guaranteed
               ▼           ▼  regardless of attendance)
   ┌───────────────┐  ┌─────────────────────────────┐
   │ Intermediate:  │  │ Candidate compounding cause:  │
   │ T-4 lock,      │  │ vendor's economic interest in │
   │ aggregate-only │  │ the standing model (assumed)  │
   │ demand signal, │  └─────────────────────────────┘
   │ cancellation   │
   │ cap, price gap │──► produces run-outs + waste + Mess Cell resale
   └───────────────┘     + near-zero Skip Meal uptake (§1.1–1.3, 1.6)
```

**Reading the network:** RC1 and RC2 are co-primary and mutually reinforcing rather than one strictly upstream of the other — RC1 generates the incentive problem; RC2 is why nobody with both the knowledge and the authority ever revisits RC1, even once a working counterfactual (the shock-adaptive exception) exists inside the institution's own history. RC3 sits *between* RC2's formal decision-rights structure and RC1's quiet cost: it is the specific reason RC2's fragmentation is never overcome by an unusually well-informed individual actor (the CFS Chair) simply escalating on their own initiative — the escalation design itself only listens for complaint intensity, so a known-but-quiet cost has no route upward regardless of who could, in principle, act on it. The intermediate mechanisms (T-4 lock, aggregate demand data, the cancellation cap, the pricing gap) are the *visible, symptom-level* structures most easily mistaken for root causes; each is real, but each would be reconfigured, not eliminate the paradox, if fixed in isolation while RC1/RC2/RC3 remained.

---

