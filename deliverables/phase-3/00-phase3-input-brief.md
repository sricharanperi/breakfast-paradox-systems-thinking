---
title: "Phase 3 Input Brief: Leverage Points, Principles and Intervention Points"
subtitle: "Working document for Activity 9. This is not a submission."
date: 2026-09-27
status: working draft, pass 2 (revised against Evidence Brief #2 and the pass-2 Phase 2 set); to be revised again as daily field observations come in
---

# Changes since pass 1

Pass 2 was driven by the team's first-hand field account of Kadamba and Yuktāhār (`research/primary-research/2026-09-27_team-field-account-evidence-brief.md`, "Brief #2") and by the pass-2 revision of Phase 2 built on it. The core structure is unchanged: the booking is the root, the gap is measured but unrouted, and the kitchen's conversion ratio is the intermediate mechanism. What moved:

1. **SC1 is now "default, not choice".** Registration is automatic and mandatory. The only exit is 5 cancellations per meal type per month, each at least 4 days ahead, and the charge cannot be nullified *(confirmed)*. LP-B is recast as a **change to the default and its exit** (Meadows 5), not cap tuning (Meadows 12).
2. **Kadamba vs Yuktāhār is now a natural comparison.** The two kitchens run under the same rules. Kadamba uses a fixed 70% ratio with gram standards, supervisor top-ups and no learning record. Yuktāhār plans from its books by matching week and projects from the first half hour of service. That makes Yuktāhār an existence proof. **LP-J (practice transfer) moves from rank 7 to rank 3**, paired with a **new LP-N, operator goal and culture** (Meadows 3/2).
3. **The absorber set grew** (D-45/D-49 check). Kadamba feeds 30-50 outside diners (about 30 planned portions) and about half its own staff from the same food, not the "20-30 staff" in pass 1. LP-E now has to budget their meals explicitly. **Holding and reheating** is added as a candidate absorber that is *not* worth protecting (08-DOS §5).
4. **The first batch is fixed before any signal exists.** The chef starts at 5:30 and the food-safety sequence runs before service. So a T-1 signal can change the first batch, while a same-morning signal can change only the top-up. Yuktāhār's first-half-hour projection misses the closing crest, so LP-I now needs a **crest-aware projection**.
5. **New design principles:** measurement must be **blame-free** and **paper-first** (Yuktāhār dropped Zoho ERP). The principle set is rewritten to six.
6. **New candidate LP-O:** give the existing per-meal oversight line (facility-team tasting, weekly QC) a quantity remit.
7. **Still held back (D-54):** billing and vendor-payment levers (LP-C, LP-D). Kadamba's "we are paid for it" is a hint toward payment on registered plates, not a contract term.
8. **No rule owner can be named yet.** Raju (CDS head, Brief #2) vs Giri (CDS Chair, CFS interview) is unresolved (D-24). LP-A's receiver, LP-K and LP-L all wait on it.
9. **New evidence gaps:** the base of the 5-10% waste figure; the extra-diner count and entitlement; reheating; back-door counts; the Skip Meal-to-kitchen conflict; the CDS head's identity; Yuktāhār's projection at breakfast.
10. **Figures corrected:** the Kadamba kg waste figures (16/23/100 kg) are **withdrawn**. The 70% ratio is upgraded to *single-sourced (operator, observer-verified)*. The "20-30 staff" figure is replaced.

---

# 0. What this is and how to use it

This brief is the team's working input for **Activity 9, "Define Design Principles & Intervention Opportunities"**. Its purpose is to "identify where and how the system could be changed". It feeds the "Leverage-Point / System Intervention Map and Design Principles" deliverable and sets up the Phase 3/4 deliverables: Intervention Concepts / Prototypes, Scenario Model & Impact Evaluation, and Final System Design Recommendation.

Sources, all in their **pass-2 revised** form:

- `deliverables/phase-2/06-system-map.md`, `07-systemic-problem-analysis.md`, `07b-causal-loop-feedback-analysis.md` (authoritative for loop IDs and verdicts, D-51), `08-reframed-problem-statement.md`, `08-design-opportunity-statement.md` (08-DOS), `08-evidence-and-validation-register.md`
- `deliverables/phase-1/03-power-interest-leverage-map.md` (the power map)
- `research/primary-research/2026-09-26_mess-operations-evidence-brief.md` (Brief #1: records, photographed registers, timestamps) and `2026-09-27_team-field-account-evidence-brief.md` (Brief #2, which **takes precedence where the two conflict**)
- `.claude/skills/systems-design-toolkit/SKILL.md` (Meadows' 12 leverage points: 12 is the shallowest and 1 the deepest)

**Confidence tags (D-35, D-48):** *confirmed (records)*, *confirmed (observed)*, *confirmed (operator, clear audio)*, *single-sourced (operator, observer-verified)*, *single-sourced (noisy audio)*, *candidate*, *assumed*.

- Kadamba numbers heard first-hand by the team are **observer-verified**. The number itself is not in doubt, but it is still the operator's own claim about its practice. These cover the 70% ratio, the gram standards, 5-10% waste, the 30-50 outside diners, half the staff, the 5:30 start and the procurement tiers.
- The **Vijayalakshmi** figures (70→80%, the 30-minute lag, "paid on plates") remain noisy audio.
- The derived "1.9x over-preparation" (2.2x veg, 1.4x non-veg) is *candidate arithmetic* on the 70% figure. It is also in open tension with Kadamba's 5-10% waste (§5, G5). **No waste-reduction size goes on the map as a headline until that tension is resolved.**

## 0.1 Labels used in this brief

| Label | What it is (pass-2 Phase 2) | Where it is stated |
|---|---|---|
| **SC1** | Registration is an **automatic, mandatory default**, not a choice. The only exit is 5 cancellations per meal type per month, each at least 4 days ahead, and the charge cannot be nullified. The count is flat at about 1,070/day at Kadamba on every weekday while turnout runs 27-42%. Whether the cycle is weekly (operator) or monthly (students) is unconfirmed | 07 §2; 07b L13; 08-DOS §1 |
| **SC2** | Student billing fires at the booking, not at consumption | 07 §2 |
| **SC3** | The gap is measured but unrouted. Operators are data-rich and authority-poor. The one oversight line that reaches the kitchen at every meal checks safety and taste, never quantity | 07 §2; 07b L10, L8 |
| **CM** | The conversion step, run in **two logics**: a fixed ratio with reactive top-up and no learning record (Kadamba 70%, Vijayalakshmi 70→80%), and a book-calibrated lookup plus in-service projection (Yuktāhār). Both correct only upward once cooked | 07 §2; 07b L11-L13; 06 "Two Operator Subsystems" |
| **OC** | **Operator culture and goal** *(candidate)*. The same rules produce Kadamba's "cook to what we're paid for" and Yuktāhār's "waste reduction is profit". This sets how much of the booking gap becomes surplus, not whether the gap exists | 07b L11, L8; 08-DOS §3 |
| **FS** | **The food-safety sequence.** Cooking temperature → 72 h sample → wrapped display plate → serving temperature → tasting by the facility team with 2 Prism staff → corrections. It fixes the first batch before any turnout signal exists | 07b L8, L13; 06 §Food-Safety Checkpoints |
| **K1** | Institutional attention follows loudness, not cost | 07 §2; 07b L4 vs L10 |
| **K2** | The absorption layer: resale, operator top-up, reuse, **30-50 outside diners and about half of Kadamba staff**, **holding and reheating** *(candidate)*, walk-in buffer, late and **back-door** service, outside venues, the bin | 07 §2; 07b L9, L17 |

Loop IDs L1-L17 plus L3b follow 07b (D-51). Pass-2 verdicts:
- L4, L11 and L12 close (all balancing).
- Yuktāhār's first-half-hour projection is a second form of L12.
- Reheating is an **open branch of L13**, not a loop (D-40).

## 0.2 Housekeeping flags before designing against D-45 / D-49

- D-49 already removed composting from D-45. Its absorber list still says "staff meals" and does not include the **30-50 outside diners** or **about half of Kadamba's staff**. It also does not mark **holding and reheating** as a route that absorbs surplus at a quality cost. D-49 and `MASTER_CONTEXT.md` §9 (the "20-30 staff" line) need updating before Phase 3 cites them.
- This brief applies the revised absorber set:
  - **Protect:** resale, reuse, outside-diner and staff meals (*by plan, not by accident*), the walk-in buffer, late service including the back door, and top-ups.
  - **Treat as legitimate targets:** the over-cooked first batch, the bin, and repeated holding and reheating. These protect no one, and reheating costs quality (08-DOS §5).

---

# 1. Candidate leverage points

Each entry gives the loop or cause it acts on, the Meadows level, the lever type, the evidence with its confidence, who holds the power (03 map plus the Kadamba command chain from Brief #2), feasibility, and a D-45 check.

Feasibility scale:
- **High:** the team can prototype or pilot it with an actor who has already engaged.
- **Medium:** the team can build an evidenced proposal and get it into an existing forum.
- **Low:** the team can only propose it, because the lever holder has not been reached or the lever is gated.

### LP-A. Upward route from existing records to the rule owner (paper-compatible, blame-free)
- **Acts on:** SC3, L10, L17, K1. It supplies the missing link that would let L13 close.
- **Meadows:** **6, information flows.** **Lever type:** information flow.
- **Change:** a standing breakfast view per hall, per weekday and per line (veg/non-veg) of booked / cooked / eaten / left over. It is built from the CDS scan export plus the operators' own books and goes to the rule owner and to the operators. It needs one agreed definition of "ate": Yuktāhār's two books give 77 vs 110 for 3 Sep *(confirmed, records)*.
- **Design conditions (new in pass 2):**
  - It must **accept paper input**. Yuktāhār keeps paper books and digitises later, and it dropped Zoho ERP on cost and staff digital readiness *(single-sourced)*.
  - It must be **explicitly blame-free**. No figure it carries may become grounds for deductions against the staff who record it (08-DOS §5).
  - At Kadamba no outcome record was seen, so the kitchen-side input starts from the CDS export plus whatever LP-J establishes.
- **Evidence:** Kadamba April breakfast is 32,162 registrations and 37.1% availed *(confirmed, records)*. Yuktāhār September breakfast is 17.7-40.2% against lunch 56-89% *(confirmed, records)*. No route from any book to a rule owner has been found *(confirmed as an absence)*. The CDS scan export exists *(confirmed)*.
- **Power:** CDS produces the data and the operators hold the books. **The receiver cannot be named yet** (CDS head Raju vs CDS Chair Giri, D-24; Mess Office vs CDS). The existing oversight line (LP-O) is a candidate carrier.
- **Feasibility:** **High** for the prototype, which the team can build from the April export plus Yuktāhār's photographed register. **Medium** for delivery, until the receiver is known.
- **D-45:** it removes nothing. It reads the cost from records instead of manufacturing pain.

### LP-B. Rule change: the breakfast default and its exit
- **Acts on:** SC1 and the booking node of L13. It also shortens the T-4 information delay (Meadows 9).
- **Meadows:** **5, rules.** Pass 2 reframes this lever. The booking is a **default**, so the lever is *what the default is and how you leave it*. The cancellation *count* is a parameter (12); the cap has already moved 5 → 10 → 5 without effect.
- **Lever type:** rule (the default).
- **Change options, from lighter to heavier:**
  1. **Shorten the exit lead** for breakfast cancellations from T-4 to T-1 or T-2.
  2. **A T-1 evening confirm/skip** that lowers the count the kitchen sees. The default stays on, but the student gets a cheap nightly off-switch.
  3. **Opt-in breakfast on low-turnout days.** Sunday is the pilot slice: Kadamba 27.3%, Yuktāhār Sundays 17.7-24.1% *(confirmed, records)*.
  4. Stop auto-registering students who are off campus over holidays (they are registered today, *confirmed*).
- **Evidence:**
  - Registrations are flat at about 1,070/day while turnout swings 27-42% *(confirmed, records)*.
  - Only **dry goods** are bought more than 4 days ahead. Perishables are bought the day before and some vegetables 2-3 days ahead *(single-sourced, observer-verified)*. At Yuktāhār, milk comes daily and vegetables 2-3×/week *(confirmed)*. The 4-day lock therefore protects goods that keep, not perishables that get cooked.
  - Kadamba's team challenged the "weekly compulsory" cut-off, but also calls last-minute registrations "a pain" *(single-sourced)*.
  - Lunch works under the same booking *(confirmed)*, so the change can be scoped to breakfast.
- **Why it matters more at Kadamba:** Kadamba cooks a *fixed share of registrations*. If the count it reads falls, its first batch falls with no kitchen change at all. **But this holds only if the change alters the count the operator reads** (G4, the Skip Meal conflict). A Skip Meal or confirm/skip redesign that does not lower that count changes nothing in Kadamba's kitchen.
- **Power:** the Mess Office / CDS portal owner (owner unconfirmed, G12). A student-operator coalition on a shorter lead is the first evidenced shared interest *(candidate)*.
- **Feasibility:** **Medium.** The team can make the case from records, the procurement tiers and operator support. Implementation sits with CDS. The change is not gated on the plate basis, because it changes timing rather than what is billed. However, if plates are paid as registered, a smaller booking also cuts vendor revenue, which shapes how the proposal lands (D-54).
- **D-45:** removes nothing directly. Resale volume may fall because fewer unwanted bookings exist. That is a need disappearing, not an absorber removed.

### LP-C. Rule change: what triggers a bill (standing, breakfast-scoped shock-adaptive model). **Held, D-54**
- **Acts on:** SC2, L1, L2, L6. **Meadows:** 5, bordering 3. **Lever type:** rule + incentive.
- **Evidence:** attendance-tracked billing ran during the LPG shortage and some holiday and fest periods *(confirmed, CFS Chair)*. Students are otherwise auto-registered through ordinary holidays *(confirmed)*, so the precedent may cover only shock and fest periods. Why it reverted is unknown. 07b now reads L6 as a calendar switch, not a self-limiting loop.
- **Power:** Mess Office / CDS and the Warden. **Feasibility:** **Low, gated on G1.** Kadamba's "paid for it" remark leans toward payment on registered plates but is not contract evidence. **D-45:** check student dependence on resale income.

### LP-D. Incentive: the vendor payment basis. **Held, D-54**
- **Acts on:** L8 (unresolved). **Meadows:** 5. **Lever type:** incentive.
- **Evidence:** "paid monthly as a lump sum on plates, with deductions" *(single-sourced, noisy audio, Vijayalakshmi)*. Kadamba says "we are paid for it, so we cook for registrations" *(single-sourced, observer-verified)*, which is a hint, not a term. Yuktāhār shows that a vendor can gain from cutting waste **through cost, whatever the plate basis** *(candidate)*. That route is what LP-N works through.
- **Feasibility:** **Low.** Do not recommend it until tender terms are seen. **D-45:** n/a.

### LP-E. Record-based first-batch calibration by hall, weekday and line, with absorbers budgeted
- **Acts on:** CM, the kitchen half of L13, and L11 (which is absent at Kadamba).
- **Meadows:** **6 feeding 12**, plus **8** (it adds a balancing loop where there is none). It is deliberately **not** "lower the ratio": the lever is the information that sets the ratio.
- **Lever type:** information flow into process.
- **Change at Kadamba:** replace "70% of registrations" with **gram standard × expected turnout per line (from records) + a named absorber allowance + a float allowance** for items diners take more of (bonda, puri, vada, idli). **Start with veg**, the larger over-preparation line: about 2.2x veg vs about 1.4x non-veg *(candidate arithmetic)*; turnout is 32.4% veg vs 48.5% non-veg *(confirmed)*. Kadamba already plans the two lines separately, so a line-specific ratio is cheaper than a global one.
- **Evidence:**
  - 70% first batch, veg and non-veg planned separately; gram standards for every dish *(single-sourced, observer-verified)*.
  - **Biryani is cooked at 100%** *(single-sourced)*. The ratio follows the operator's *expectation* per meal, so better expectations from records by weekday and item can move it without any rule change.
  - Kadamba said of forecasting: "we don't have that idea… it was wasted many times" *(single-sourced)*.
- **Power:** inside the operator's authority, but at Kadamba it runs down the **Prism chain: operations manager → manager → supervisor**. The **supervisor** calls in-service quantities *(single-sourced)*, so any rule must be one the supervisor can read and apply live, on paper, at the counter.
- **Feasibility:** **Medium at Kadamba** (down from High). The operator treats the count as a paid obligation, so "a better input alone may not be wanted" (08-DOS §3), and adoption runs through LP-J/LP-N. **High at Yuktāhār**, where it means re-anchoring the "max 50%" belief to the recorded ~28%.
- **D-45 (revised, pass 2): the absorber is larger and partly planned.**
  - Kadamba cooks about **30 extra portions** for **30-50 outside people** (such as night security) *(single-sourced)*.
  - **About half of Kadamba's internal staff** also eat at the mess *(single-sourced)*. The headcount is unknown.
  - Whether the 30 portions sit inside or on top of the 70% is unknown (G9).
  - Calibration must **name and budget these meals** in the plan, so that they are fed by allocation and not by accident.
  - It must also keep the top-up reserve (10-15 min on-site) and the back-door late share.
  - Paired with LP-A (so it does not deepen L17's invisibility) and LP-I (so it does not trade waste for run-outs).
- **Sizing caveat:** a 70% batch is about 750 portions against about 398 eaten, a first-batch surplus of about 350 before any top-up *(candidate arithmetic)*. That does not fit a 5-10% waste figure unless most of it is eaten by outside diners and staff, held and reheated, or never cooked. **Do not size a waste reduction until G5 is settled.** If the surplus is mostly reheated rather than binned, **the gain is in quality more than tonnage**, and the success metric has to change to match (P6).
- **Co-benefit (candidate):** if the reheat branch of L13 holds, a smaller first batch with more frequent top-ups cuts both surplus and quality degradation. That gives the operator and students a shared, non-cost reason to adopt it. The link from reheating to skipping is **not** evidenced (D-40).

### LP-F. Shorten the learning delay (L11) and start a learning record where none exists
- **Acts on:** the L11 lag (a 1-2 week matching-day lookup) and its **absence at Kadamba**.
- **Meadows:** **9, delays**, and at Kadamba **8** (create the balancing loop). **Lever type:** process.
- **Change:**
  - At Yuktāhār, add yesterday's breakfast booked/eaten/left over to the daily meeting alongside the matching-week lookup.
  - At Kadamba, a one-page daily paper record per line (first batch, top-ups, run-out time, left over, where it went), read the next day by whoever sets the batch.
- **Evidence:** the Wastage Book is read at the matching menu day *(confirmed)*. The site head wants the 6 Sep figure used "not even next month, next week" *(confirmed)*. Culture change at Yuktāhār took about **four months** (Aug → Dec) *(single-sourced)*.
- **Power:** the operator. **Feasibility:** **High** at Yuktāhār; at Kadamba it depends on LP-J/N. **D-45:** as for LP-E.

### LP-G. Operator voice in the menu (item-level waste to the menu owner)
- **Acts on:** L16 (absent) and K1. **Meadows:** 5 (who is consulted) carried by 6. **Lever type:** role + information flow.
- **Change:** a formal operator slot at each 2-week menu cycle, bringing item waste, run-outs and the "floating" items.
- **Evidence:** Kadamba's waste items are uttapam, set dosa and upma; the floating items are bonda, puri, vada and idli *(single-sourced)*. The operators say students or the committee choose the menu *(confirmed at Yuktāhār)*. The precedent is the L4 route (Student Council → Parliament → CDS Committee) *(confirmed)*.
- **Power:** the CDS Committee / menu committee. **Feasibility:** **Medium.** **D-45:** removes nothing.

### LP-H. Institute calendar feed to the planning meeting
- **Acts on:** the downward information break and L7 dips. **Meadows:** 6. **Lever type:** information flow.
- **Evidence:** "We don't come to know until we sit in the meeting" *(confirmed, Yuktāhār)*.
- **Power:** Academic administration (a sleeping stakeholder); the CDS team could relay. This is an information ask only, not a timetable change. **Feasibility:** High/Medium. **D-45:** removes nothing.

### LP-I. Design for the real arrival curve: crest-aware projection, staged late batch, back-door rule
- **Acts on:** L12 (upward-only top-up), L14 (the just-in-case hedge and its candidate ratchet), L15 (soft close).
- **Meadows:** **9** (top-up delay vs the crest), **10** (when cooked stock is created), plus a small rule (5/12).
- **Lever type:** process + minor rule.
- **Change:**
  1. **A crest-aware projection.** Yuktāhār's first-half-hour sample sees about **15%** of a morning's diners on the Kadamba curve, against **26.5% in the last quarter hour** and about **19.8% in 9:20-9:29**. A flat projection lands about 40% short *(candidate arithmetic on confirmed records)*. Use a **weekday arrival profile** as the conversion factor ("by 8:00 we have seen X% of a typical Tuesday") instead of a linear projection. It should be a paper table the supervisor can read.
  2. **A staged late batch** sized at about 9:05-9:10 from that projection, instead of cooking the whole hedge at the start. Any late batch still has to pass the safety checks (FS); whether top-ups are re-tasted is unknown.
  3. **Formalise the back door.** Today, entry after 9:30 cannot be refused *(single-sourced)*; 9.2% of scans come after 9:30 and the latest is at 10:07 *(confirmed)*. That is already an informal grace period. A stated grace period **must come paired with a late batch**, or it only relabels the shortage.
- **Evidence:** 26.5% of scans fall in 9:15-9:30 and the rate is about 9/min at 9:29 *(confirmed)*. The operator's rule of thumb is about 150 in the last 10 minutes *(single-sourced)*, which is larger than the records show and a candidate driver of the hedge. The raw reserve cooks in 10-15 min *(single-sourced)*.
- **Power:** operators for batching (the supervisor at Kadamba); CDS / Mess Office for the service window.
- **Feasibility:** **High** on-site, where the team can build the profile table from the April export now. **Limited** off-site because of the ~30-minute lag.
- **D-45:** keeps the late-service absorber and makes it explicit.
- **Why it matters:** it removes the *reason* for the hedge. Smaller, more frequent batches also cut reheating *(candidate)*.

### LP-J. Lateral practice transfer: the Yuktāhār book system as a template
- **Acts on:** the lateral information break (Vijayalakshmi believes Kadamba gets 90-95%; the records say 37%), the absent L11 at Kadamba, and the uneven quality of balancing loops across kitchens.
- **Meadows:** **6** with **4 (self-organisation)**: operators build the practice among themselves.
- **Lever type:** information flow + role.
- **Change:** an operator-to-operator exchange convened by CDS. It carries concrete content:
  - the Wastage Book with run-out time;
  - the two-book reconciliation (issued = cooked);
  - the weekday attendance register;
  - the wastage board with a declining target;
  - the daily meeting with peer cross-checking.

  Kadamba already has per-dish gram standards to plug these into.
- **Evidence:** all of Yuktāhār's books are photographed *(confirmed, records)*. Waste fell Aug → Dec after weighing was made blame-free *(single-sourced, self-report; no before/after figures)*. Kadamba has no learning record *(single-sourced)*.
- **The transfer carries its preconditions, not just the books:** blame-free weighing, daily discussion, peer cross-checks, and a goal that treats waste as cost (LP-N). Kadamba's layered hierarchy raises the blame risk that Yuktāhār's flat structure avoids.
- **Power:** operators. Nobody convenes them today, and CDS is the natural convenor. Yuktāhār's two project managers are the natural hosts.
- **Feasibility:** **Medium.** No institutional rule change is needed. The team already holds the template (the photographed books) and can build a Kadamba-ready one-page version.
- **D-45:** removes nothing.

### LP-N (new). Operator goal and culture: from "cook to the count" to "surplus is cost"
- **Acts on:** OC, the presence or absence of L11, the L8 route through cost rather than revenue, and L17 (an operator treating the count as its obligation has no motive to signal upstream).
- **Meadows:** **3 (goals of the operator subsystem)** and **2 (mindset)**.
- **Lever type:** goal / culture, carried by information and practice.
- **Change:** make waste a visible operator cost and target inside Prism. Carriers: a wastage board; LP-J's peer exchange; the Prism chain (the operations manager sets the goal, the supervisor applies it); and a blame-free framing. It works **without** touching the payment basis.
- **Evidence:** Yuktāhār states its goals as quality, less waste, lower operating cost, standardisation and **higher profit** *(single-sourced)*. Kadamba says "it doesn't care if people don't want to eat because it is a responsibility and they are getting paid for it" *(single-sourced, observer-verified)*. **Same billing basis, opposite stances** *(candidate)*.
- **Power:** Prism management (above the site; not interviewed). The CDS contract holder (unconfirmed) is the indirect holder.
- **Feasibility:** **Low to medium.** A student team cannot set Prism's goals, but it can put the Yuktāhār case in front of Prism's operations manager, and it can show a cost figure per line from records.
- **Bounded by D-54:** it may not lean on payment-basis changes. If G1 = registered plates, cutting surplus is still a *cost* saving for Prism (less food bought and cooked) even though revenue is unchanged. That is the argument to test.
- **D-45:** n/a. Carries the absorber budget from LP-E.

### LP-K. A cost-based escalation trigger alongside the loudness trigger
- **Acts on:** K1. **Meadows:** 5 (the rule for what gets attention), with 6 underneath. **Lever type:** rule.
- **Change:** a standing threshold, for example "breakfast cooked-vs-eaten beyond X for N weeks goes to the Committee", fed by LP-A and carried by LP-O where possible.
- **Evidence:** menu fatigue was loud and fixed end to end *(confirmed)*; the larger measured gap never entered the pathway *(confirmed)*.
- **Power:** the CDS Committee / Council / Parliament pathway. **The owner cannot be named until G12 is resolved.**
- **Feasibility:** **Medium, after LP-A.** It must be blame-free: a threshold breach triggers a review, not a deduction. **D-45:** removes nothing.

### LP-O (new). Give the existing per-meal oversight line a quantity remit
- **Acts on:** SC3 and the L8 structure. It balances on safety and taste but never on quantity.
- **Meadows:** **6** (a new information flow on an existing channel) and **5** (the facility team's remit).
- **Lever type:** role + information flow.
- **Change:** at the tasting the facility team already does with 2 Prism staff before every meal, and at the weekly QC visit, record one extra line: *cooked first batch per line vs registrations vs yesterday's eaten*. That makes quantity visible on a route that already reaches both the kitchen and the institution.
- **Evidence:** the tasting and the display plate are *confirmed (observed)*. Weekly QC and daily water TDS are *single-sourced*. Nothing in the sequence tests first-batch size *(single-sourced)*.
- **Power:** the facility team. **Its parent body is unknown** (CFS? CDS? G16).
- **Feasibility:** **Medium.** It is cheaper than a new channel, but blame risk is highest here: an inspector recording quantity looks like an audit. It must be framed as information, never a deduction.
- **D-45:** removes nothing. It must not add delay to the safety sequence.

### LP-L. A named owner of the booked → cooked → eaten outcome. **Held pending G12**
- **Acts on:** SC3 (split decision rights). **Meadows:** 5 / 4. **Lever type:** role.
- **Evidence:** decision rights are split at least five ways (08-DOS §4.3). The Kadamba chain runs CFS → CDS → Prism, but the CDS head is Raju or Giri (unresolved).
- **Feasibility:** **Low** until the CDS head is identified and interviewed. A lighter version is a data-owning coordinator inside each operator. It exists at Yuktāhār (Ajita keeps the Wastage Register; the coordinator keeps the wastage board) and is absent at Kadamba.
- **D-45:** removes nothing.

### LP-M. Institutional goal and paradigm: "what is cooked tracks what is eaten"
- **Acts on:** the mental models in 08-reframed §4: that a registration count stands in for demand, and that certainty days ahead is permanently worth more.
- **Meadows:** 3 / 2. **Lever type:** reframing embedded in metrics and forums.
- **Evidence:** the CDS poster already says "minimising food wastage through advance meal planning" *(confirmed)*. The certainty belief has been suspended twice under shock *(confirmed)*.
- **Feasibility:** carried through P6, LP-A and LP-K. It cannot be implemented directly. It is the institutional counterpart of LP-N.

### Considered and deliberately down-ranked
- **Lowering the first-batch ratio as a number** (12). Alone, it moves cost into run-outs at the crest and deepens absorption. It is used only as the output of LP-E.
- **Changing the cancellation count (5 → 10)** (12). The cap has already moved 5 → 10 → 5. The lever is the default and the lead time (LP-B), not the count.
- **Moving the 8:30 class start.** Treated as a fixed boundary. Nearly 60% of scans come at or after 8:45.
- **Nudges or reminders to students.** An event-layer fix aimed at the least-powered actor. Registration is a default students did not choose.
- **Making Skip Meal pay a refund** (5/12). Doubly gated: on G4 (does Skip Meal lower the count Kadamba reads?) and on LP-B, which would largely supersede it. Kept as a fallback.
- **Software-first kitchen tooling** (forecasting apps, ERP, sensors). Yuktāhār dropped Zoho on cost and staff digital readiness. It fails P2.
- **A waste-exit count at the garbage contractor** (6). Kept as an optional add-on to LP-A once the disposal route is known (G5).
- **Anything that restricts resale, outside-diner and staff meals, or late / back-door service.** Fails D-45.

---

# 2. Ranked shortlist: depth vs feasibility

Depth is the Meadows level plus how directly the lever acts on SC1-SC3 and OC rather than on CM. Feasibility is for this student team in the remaining weeks.

| Rank | Leverage point | Meadows | Depth | Feasibility | Gated? | Change vs pass 1 |
|---|---|---|---|---|---|---|
| 1 | **LP-A** Upward route + shared "ate", paper-compatible and blame-free | 6 | High (SC3; lets L13 close) | High (prototype) / Medium (delivery) | Receiver waits on G12 | Same rank; conditions added |
| 2 | **LP-B** Breakfast default and exit (shorter lead, T-1 confirm/skip, Sunday opt-in) | 5 (+9) | Very high (SC1) | Medium | Must change the count the kitchen reads (G4) | Same rank; recast as a default change |
| 3 | **LP-J + LP-N** Yuktāhār book-system transfer carrying an operator goal shift | 6/4 + 3/2 | High (OC; creates L11 at Kadamba) | Medium | Needs Prism access | **Up from 7**; LP-N new |
| 4 | **LP-E + LP-F + LP-I** Record-calibrated, veg-first batch with absorbers budgeted, a daily record, and a crest-aware top-up | 6 → 12, 8, 9, 10 | Medium (CM) | High (Yuktāhār) / Medium (Kadamba) | Size waits on G5; absorbers on G9 | Same rank; absorber budget, crest correction and supervisor-readable form added |
| 5 | **LP-G** Operator voice in the menu | 5/6 | High (L16, K1) | Medium | No | Down from 3 |
| 6 | **LP-K + LP-O** Cost trigger, carried on the existing oversight line | 5/6 | High (K1, SC3) | Medium, after LP-A | G12, G16 | LP-O new |
| 7 | **LP-H** Calendar feed | 6 | Medium | High/Medium | No | Down from 6 |
| Hold | **LP-C** Billing at consumption | 5/3 | Deepest actionable | Low | **G1 (D-54)** | Unchanged |
| Hold | **LP-D** Vendor payment basis | 5 | Deep | Low | **G1 (D-54)** | Kadamba hint noted |
| Hold | **LP-L** Named outcome owner | 5/4 | Deep | Low | **G12** | Now explicitly waits on Raju/Giri |
| Frame | **LP-M** Institutional goal: cooked tracks eaten | 3/2 | Deepest | Carried by P6 | n/a | Paired with LP-N |

**Why this order:**

1. **LP-A stays first.** Every governance lever needs its input, and the team can build the first version itself. Pass 2 adds two conditions and no change in rank: it must work from paper and be blame-free. Its *delivery* is weaker until someone can be named as receiver.
2. **LP-B stays second and is stronger.** The student-side account confirms that registration is a default with a narrow exit, and only dry goods need more than four days. At Kadamba, a lower count flows straight into a lower first batch through the fixed ratio. **Caveat:** this works only if the rule changes the count the kitchen reads (G4).
3. **LP-J + LP-N rises to third** because the natural comparison is the strongest new evidence. Under the same rules, one kitchen learns and one does not, and the difference is goal and culture, not data. Yuktāhār is an existence proof that the balancing loop can run in-house on paper. Kadamba does not lack information (it has gram standards and a supervisor watching the counters). It lacks a reason and a routine to carry learning forward. Without LP-N, LP-E at Kadamba is an input nobody asked for.
4. **LP-E/F/I stays fourth,** because it is the one lever with a fast physical effect. Pass 2 makes it harder, not easier. It must budget 30-50 outside diners plus about half the staff. It cannot be sized until the 5-10% vs 70%/37% tension is measured. It must be readable live by the supervisor. It needs a crest-aware projection. At Kadamba it lands through LP-J/N.
5. **LP-G drops from third to fifth** because nothing new strengthened it, while the kitchen-side levers gained evidence. Its logic is unchanged.
6. **LP-K + LP-O:** the oversight line is a ready carrier, but its owner and its blame risk are both open.
7. **LP-C / LP-D / LP-L stay held.** Kadamba's remark moves G1 forward but does not settle it (D-54). LP-L cannot name a person until G12 is resolved.

**Suggested sequencing:**
1. Route (A, H).
2. Transfer practice and goal (J, N) while calibrating and timing at Yuktāhār first (E, F, I).
3. Voice and attention (G, K, O).
4. Change the default (B).
5. If G1 allows, change billing (C, D) under an owner (L).

---

# 3. Candidate design principles (six)

### P1. Route, don't re-measure; and route on paper
**From:** LP-A, LP-H, LP-K and LP-O.
**Rationale:** the gap is already measured in the CDS scans, Yuktāhār's weekday register and Wastage Book, and Kadamba's stated waste share. What fails is the route (L10, L16). A concept that adds an app, sensor or survey before connecting existing records solves the wrong problem. The records are on paper. Yuktāhār dropped an ERP on cost and staff digital readiness, and office staff digitise later. So routes must start from a book page or a one-page sheet and use channels that already exist (the daily meeting, the tasting, weekly QC). Agree one definition of "ate" first (77 vs 110 on 3 Sep).

### P2. Make measurement blame-free, and expect months, not days
**From:** LP-A, LP-E, LP-F, LP-J, LP-K and LP-O.
**Rationale:** Yuktāhār's waste weighing worked only after the managers made it blame-free and discussed it daily. Staff had first said "they are catching us". Results took about four months (Aug → Dec), and it runs on peer cross-checking in a flat team. Kadamba's layered Prism chain raises the risk that a number becomes a reprimand. Any concept that adds or routes a figure must say who sees it, state that it cannot trigger deductions, and be judged over months.

### P3. Change the default and the goal, not the people
**From:** LP-B, LP-N and LP-M.
**Rationale:**
- On the student side, registration is an automatic default with a capped, four-day exit and no nullification. The lever is the default and the exit, not persuasion.
- On the operator side, the same rules produce opposite stances. The lever is the operator's goal (surplus as cost), not blame.
- Students hold the least power and the most defensible behaviour. Operators run the system's only working balancing loops (L11, L12). Aiming the fix at either discards the actors the system depends on.

### P4. Act on the first batch the day before; act on the day only through the top-up, and plan for the crest
**From:** LP-B, LP-E and LP-I.
**Rationale:**
- The chef starts at 5:30. The safety sequence (temperature, 72 h sample, display plate, serving temperature, tasting) runs before service. The first batch is therefore fixed about 3.5-4 h before the crest and before any turnout signal. So first-batch levers must work at T-1 (count, ratio, line), and same-morning levers must work through smaller, more frequent top-ups.
- Demand crests at close: 26.5% of scans in the last 15 minutes, plus back-door arrivals after 9:30. A first-half-hour projection needs a crest-shaped conversion factor.
- Scope stays **breakfast, per hall, per weekday, per line.** Lunch works (56-89%), veg and non-veg diverge (32/49%), and the three kitchens run different logics.
- Never trade a safety step for speed.

### P5. Feed the absorbers by plan; target only the over-cooked batch, the bin and repeated reheating (revised D-45 / D-49)
**From:** the D-45 checks on LP-E, LP-I and LP-C.
**Rationale:**
- 30-50 outside diners and about half of Kadamba's staff eat from the same food. Resale returns money, reuse turns idli into upma, and the back door serves late-comers. These people are **stakeholders in the intervention**. Any concept that shrinks surplus must name their allocation.
- The bin protects no one. Food held and reheated protects quantity at the cost of what students eat, so it is a target, not an absorber to protect.
- Do not make anyone worse off to create visibility the records already give.

### P6. Measure success as cooked-vs-eaten, run-outs and food quality, not turnout
**From:** LP-M, LP-A, LP-E and LP-K.
**Rationale:**
- A real share of skipping is legitimate (sleep, fasting, regional habit, observance).
- The measure that matters is the cooked-vs-eaten gap plus run-out incidents, which Yuktāhār already logs per item. Where surplus is reheated rather than binned, **food quality at service** also belongs in the measure.
- Kadamba's stated 5-10% is not a baseline until its base is known. Success also means that cost becomes visible to a rule owner.

**Working rule (keep it on every concept card):** scope claims to the evidence. Records cover Kadamba breakfast (April), Yuktāhār (September) and two June sheets. Kadamba's operational figures are the operator's own, observer-verified. Bakul/Palash, and Kadamba lunch and dinner, are *assumed*.

---

# 4. Candidate intervention points on the system map

Placed on the service timeline (06), the process trace (04) and the loops (07b).

| # | Where in the process | When | Loop / cause | What flows today | Proposed change | LP |
|---|---|---|---|---|---|---|
| IP1 | Portal default and exit (Mess Office / CDS) | Monthly or weekly cycle; exit T-4 | SC1, L13 | Automatic registration; 5 cancellations per meal type at T-4; no nullify | Shorter breakfast lead; T-1 confirm/skip **that lowers the kitchen's count**; Sunday opt-in; no auto-registration while off campus | LP-B |
| IP2 | T-1 planning. Yuktāhār: first-half daily meeting. Kadamba: who sets the 70% (manager/supervisor?) is unknown | T-1 | CM, OC, L11, L13 | Portal count + matching-week books (Yuktāhār); a fixed 70% per line (Kadamba) | Weekday × line turnout table; yesterday's record; a named absorber allowance; calendar items | LP-E, LP-F, LP-H, LP-J |
| IP3 | First-batch cook + safety sequence | 5:30 → about 7:30 | CM, FS, L13, L14 | Whole hedge cooked, checked and tasted before any signal | Batch sized to line turnout + absorber allowance; raw reserve held; no safety step shortened | LP-E |
| IP4 | Facility tasting with 2 Prism staff; weekly QC | Every meal, before service; weekly | SC3, L8 | Safety and taste only | Add one quantity line: first batch vs registrations vs yesterday's eaten | LP-O, LP-A |
| IP5 | Supervisor at the counter | 7:30-9:30 | L12, L14 | Watches what is left vs the gram standard; calls top-ups | A crest-aware profile table (% of the day's diners expected by each time, by weekday); staged batch at about 9:05-9:10 | LP-I |
| IP6 | Service close and the back door | 9:30 onward | L15, K2 | Front door closes; back-door entry cannot be refused | Stated grace period paired with a late batch; count back-door arrivals | LP-I |
| IP7 | Surplus handling | During and after service | K2, L9, L13 reheating branch | Held, reheated, moved between vessels; outside diners, staff; bin | Smaller, more frequent batches; planned allocation for outside diners and staff; record where surplus goes | LP-E, LP-I |
| IP8 | Post-service record | After about 9:45 | L11, L9 | Wastage Book (Yuktāhār); no record seen (Kadamba) | A one-page daily record at Kadamba, modelled on Yuktāhār's; it feeds IP2 | LP-F, LP-J |
| IP9 | CDS scan export → receiver | Monthly / on request | SC3, L10 | Exportable, reviewed by no one | Standing breakfast gap view; the receiver is named after G12 | LP-A |
| IP10 | Menu selection | 2-week cycle | L16, L4 | Committee/students choose | Operator slot with item waste and floating items | LP-G |
| IP11 | Escalation pathway | Semester / policy cycle | K1, L4 | Triggered by loudness | Cost threshold, blame-free | LP-K |
| IP12 | Calendar → kitchen | Weekly, ahead of T-1 | L7 | Word of mouth at the meeting | Formal feed of exams, events and holidays | LP-H |
| IP13 | Operator ↔ operator; Prism ops manager | None today | Lateral break, OC | Mutual misbeliefs; no exchange | CDS-convened practice exchange; Yuktāhār books as the template; a waste-as-cost goal | LP-J, LP-N |
| IP14 | Wrapped display plate at the entrance | Every meal | L4, L15 | Shows the menu at the door | *Candidate:* also show crowd timing ("quietest window") or the day's leftover figure. It cannot inform a skip decision, since students see it only at the door | LP-I (minor) |
| IP15 | Student billing / vendor payment | Monthly | SC2, L8 | Bill at booking; vendor paid "on plates" (basis unknown) | Held: bill at consumption; review the plate basis | LP-C, LP-D |

**For the annotated CLD (deliverable 11), mark:**
- LP-A on the **missing link from L10 to the rule owner** (dashed, "proposed route");
- LP-B on the **automatic-default node of L13**;
- LP-N on **L11's goal node**, drawn as present at Yuktāhār and absent at Kadamba;
- LP-E/F on **L11's feedback link and delay**, and on the **open reheating branch of L13**;
- LP-I on the **top-up delay in L12/L14**, with the projection form of L12 annotated "crest-blind";
- LP-O on the **L8 quality-control structure**, adding the missing quantity input;
- LP-G on the **absent L16 link**;
- LP-K on the **trigger node of L4**.

---

# 5. Evidence gaps that would most change these choices, and what to collect next

## 5.1 Gaps, ranked by how much they would move the shortlist

| ID | Gap | What it would change |
|---|---|---|
| **G1** | **Plate basis of vendor payment** (registered vs served) and what the deductions are. Kadamba's "paid for it" is a hint only | Whether LP-C/LP-D leave "hold" (D-54); how Prism receives LP-B and LP-N |
| **G4** | **The Skip Meal-to-kitchen conflict:** does Skip Meal or cancellation lower the count Kadamba cooks against? | Whether LP-B works through the count; whether a Skip Meal refund is a live fallback; L2's kitchen link |
| **G5** | **The base of Kadamba's 5-10% waste** (per meal or per day? by cooked weight? plate waste only?), whether any record exists, and where the ~350-portion first-batch surplus goes | The sizing and the success metric of LP-E. If most surplus is reheated or eaten by staff, the gain is quality, not tonnage |
| **G12** | **Who heads CDS:** Raju (head, Brief #2) vs Giri (Chair, CFS interview). Two roles, or one wrong name? Is CDS the Mess Office? | The receiver for LP-A, the owner for LP-K/LP-L, the portal owner for LP-B |
| **G9** | **The extra-diner count:** 30 portions vs 30-50 people vs the earlier 30-40; inside or on top of the 70%; headcount of "half the staff"; entitlement or informal norm | The absorber allowance LP-E must budget (P5) |
| **G13** | **Reheating:** how much of each batch is held, how many times it is reheated or transferred, and whether quality complaints track it | Whether the L13 quality branch is real; LP-E's co-benefit; the P6 quality measure |
| **G2** | **The real first batch vs the stated 70%**, per line and per weekday (observed, not told); why Vijayalakshmi went 70→80% | LP-E's effect size; the L14 ratchet |
| **G3** | **Who set the T-4 lead and the 5-cancellation cap, and what depends on them**; weekly vs monthly cycle | Whether LP-B is a habit fix or needs portal/contract work |
| **G14** | **Back-door counts after 9:30 at breakfast,** and their times | LP-I's late batch size; whether L15 is a breakfast mechanism |
| **G15** | **Does Yuktāhār use the first-half-hour projection at breakfast, and does it correct for the crest?** Its own arrival curve is unmeasured | The design of LP-I's projection; what LP-J transfers |
| **G16** | **The facility team's parent body and remit;** whether weekly QC is the faculty QC visit | LP-O's feasibility and owner |
| **G6** | Timetable: do first classes end near 9:15-9:25? | Whether IP5/IP6 need an Academic administration ask |
| **G7** | Records beyond Kadamba April breakfast (May-Sept, lunch/dinner, Bakul/Palash/Yuktāhār scans; student ID retained?) | How far every lever generalises; whether LP-C is technically ready |
| **G8** | Which halls the Vijayalakshmi kitchen serves | Whether LP-I's off-site limit applies to Bakul/Palash |
| **G11** | The June Yuktāhār registration regime | Natural evidence for LP-B (a smaller booking roughly doubled registered turnout, to about 60%) |

## 5.2 What to collect next (daily field log, concrete)

**A. Daily breakfast service log at Kadamba and Yuktāhār**
- **Schedule:** every day for two weeks, all weekdays including two Sundays. One observer per mess, **5:30-10:15**. The start is earlier than pass 1 so that the first-batch cook and the safety sequence are seen.
- **What to record** (one row per item per day; suggested CSV header):
  `date, weekday, mess, item, line (veg/nonveg), registrations_portal (as the kitchen reads it), first_batch_qty (kg/pieces), first_batch_cook_start, safety_seq_done_time (tasting complete), topup_n_time, topup_n_qty, runout_time, scans_by_15min (7:30…9:30, after), backdoor_after_930_count (+ times), queue_len_9:15, queue_len_9:25, reheat_events (count), vessel_transfers (count), held_qty_at_9:00, leftover_at_close_qty, leftover_route_qty (outside diners / staff / reuse / held to next meal / bin), outside_diners_served, staff_served, calendar_event, notes`
- **At Yuktāhār add:** `projection_at_8:00 (their estimate of the day's total)` and `projected_vs_actual_total`. This tests G15 against the crest.
- **How to get the numbers:**
  - Ask the supervisor or chef for first-batch and top-up quantities as they happen.
  - Photograph Yuktāhār's Wastage Book and Grocery Book page for the same day.
  - At Kadamba, ask to see whatever sits behind the 5-10% figure (G5).
  - Count scans from the counter screen in 15-minute bins, or count heads at the door.
  - Count back-door entries directly from 9:30 to 10:15 (G14).
  - Count reheat and transfer events for 2-3 items per day (G13).
- **What it firms up:** G2, G5, G9, G13, G14, G15, and the timing of LP-I's staged batch.

**B. At the next operator visit** (record in English where possible)
- **Kadamba** (ask the supervisor and, if reachable, the Prism operations manager):
  - "When a student cancels or uses Skip Meal, does the number you cook against go down?" (G4)
  - "Is the 5-10% waste per meal or per day, by weight, and is it written down anywhere?" (G5)
  - "Are the ~30 outside portions inside the 70% or on top? How many staff eat each breakfast? Is it part of their terms?" (G9)
  - "Who decides the 70%: the manager or the supervisor? Has it ever gone down?" (IP2, G2)
  - "Is Prism paid on registered plates or on scans? What are the deductions?" (G1)
  - "Would a one-page daily sheet like Yuktāhār's be usable by the supervisor, if no one is blamed for the numbers?" (LP-J/N feasibility)
- **Yuktāhār:**
  - "Do you use the first-half-hour projection at breakfast? Do you adjust for the last-15-minutes rush?" (G15)
  - "Would you show your books to another operator?" (LP-J)
  - "What happens to surplus that is not reused?" (G5)
  - "Was June run under non-compulsory registration?" (G11)
  - "Could yesterday's breakfast numbers go into today's meeting?" (LP-F)
- **Vijayalakshmi:**
  - "Which halls does your kitchen serve?" (G8)
  - "Why 70%→80%? Ever moved it down?" (G2)
  - "Registered or served plates?" (G1)

**C. Institution side (CDS team, Mess Office, CFS Chair; request the CDS head interview)**
- **First, resolve G12:** ask the CFS Chair and the CDS admin directly who Raju and Giri are, and which of them owns the registration rules and the scan data.
- Ask who set the T-4 lead and the 5-cap, what breaks at T-1, and whether the cycle is weekly or monthly (G3).
- Ask for the tender document or a contract summary (G1).
- Ask who the facility team reports to (G16).
- Ask whether anyone reviews the scan export today (LP-A).
- Request May-Sept Kadamba breakfast, April lunch/dinner, and any Bakul/Palash/Yuktāhār scans, plus whether the student ID is retained (G7).

**D. Academic side (one email or visit):** get the first-period timetable for the main UG batches (G6), and ask whether an exam/event calendar can be shared weekly (LP-H).

**E. Students, at the crest:** a short intercept at the Kadamba queue, 9:15-9:30, 20-30 students on 3-4 weekdays including one Sunday.
1. When did you decide to come this morning?
2. Why this late?
3. If you could skip tomorrow by 9 pm tonight and not be charged, would you?
4. Do you know you can get in by the back door after 9:30? (G10, L15)
5. Is today's food noticeably reheated? (G13)
6. Mess Cell: how many breakfasts did you buy or sell this week?

**F. Desk work (no field time needed)**
- Build the **weekday arrival-profile table** from the April export: the cumulative % of the day's scans by each 15-minute mark, per weekday. This is LP-I's first prototype and the conversion factor for a crest-aware projection.
- Build the **LP-A one-pager**: Kadamba April + Yuktāhār September, by weekday and line, with the lunch contrast.
- Build a **Kadamba-ready one-page daily record** adapted from Yuktāhār's Wastage Book columns (LP-J/F prototype).
- Re-listen to the Vijayalakshmi audio for the 70→80% and "plates" statements (G1, G2).

## 5.3 Decision triggers for the team

- **If G1 = served plates:** promote LP-C/LP-D. Operators become allies of a smaller booking, and LP-N gains a revenue argument as well as a cost one. Re-rank LP-B to 1 alongside LP-A.
- **If G1 = registered plates:** keep LP-C/LP-D as a renegotiation proposal. Lead with LP-A + LP-B (timing only) + LP-J/N (the cost argument) + LP-E/I.
- **If G4 = Skip Meal does *not* lower Kadamba's count:** LP-B must be specified as a change to *the count the kitchen reads*, and a Skip Meal refund drops out as a fallback.
- **If G5 shows the surplus is mostly eaten by outside diners/staff or reheated:** re-express LP-E's success as quality and planned allocation, not tonnage. P5 becomes the binding constraint.
- **If G5 shows the first batch is much smaller in practice than 70%:** the kitchen half shrinks, and LP-B and LP-I carry more weight.
- **If G9 shows outside and staff meals are a written entitlement:** the absorber allowance in LP-E becomes a fixed line in the plan, not a variable.
- **If G12 resolves to one person with authority over registration and the scan data:** name them as LP-A's receiver and LP-L's candidate owner. Move LP-K up.
- **If G15 shows Yuktāhār already corrects for the crest:** transfer its method as-is under LP-J. If it does not, the LP-I profile table becomes something the project contributes back to Yuktāhār as well.
- **If G3 shows nothing depends on T-4:** LP-B becomes the headline recommendation.
- **If G6 shows classes ending at about 9:15-9:20:** add an Academic administration information ask (not a timetable change) to IP5/IP6.
