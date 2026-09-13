# Breakfast Paradox — Feedback Loop Analysis, Rebuilt from Primary Evidence
## (Independent re-derivation; prior draft used only as an audit checklist, not as a source of truth)

**Method note.** Every loop below was built by starting from the raw variables and testing each
link against the actual primary documents, not by inheriting the prior team draft's (`06-system-map.md`,
`07-systemic-problem-analysis.md`, `MASTER_CONTEXT.md`) framing or loop count. Where my conclusion
matches the prior draft, I say so and give my own independent evidence chain. Where it diverges —
and it diverges in several important places — I say that explicitly and explain why (usually: the
prior draft asserted a link or a closure that the source material does not actually support).

**Evidence tags used consistently below:**
- **CONFIRMED** — stated directly, in the primary-source wording, by a named respondent/document, or true by definition/mechanical necessity given confirmed facts.
- **SINGLE-SOURCED** — one respondent or one account; not cross-checked against a second independent source.
- **CANDIDATE** — a plausible, specifically-named mechanism, not yet confirmed by any respondent.
- **ASSUMED** — a systems-thinking inference with no direct testimony behind it at all (used freely per the task brief, never presented as fact).
- **DISCONFIRMED** — direct evidence contradicts the mechanism.

**Closure rule applied throughout:** a set of links only counts as a *loop* if the last variable
causally returns to affect the first. Reinforcing (R) = even number of `−` links (including zero).
Balancing (B) = odd number of `−` links. If no evidenced or even plausible closing link exists, it is
presented as a **chain**, explicitly not a loop, per the task's own instruction.

**Primary sources actually read for this pass:** `MASTER_CONTEXT.md` (full, both halves),
`research/primary-research/interviews/2026-09-03_student-self-account-and-mess-system-overview.md`,
`research/primary-research/interviews/2026-09-06_five-student-interviews-guide1.md`,
`prathyusha_braindump.md`, `prathyusha_braindump_2.md`, plus `deliverables/phase-2/06-system-map.md`
and `07-systemic-problem-analysis.md` (read in full, but used only as an audit target — every claim
in them is re-derived here from the sources above, not copied). One important evidentiary distinction
carried through this whole document: a good deal of the richest "systems-boundary expansion" content
in `06-system-map.md` (kitchen-technology-to-trust effects, the Canine Council mechanism, faculty/staff
demand, cultural/mental-model inventory) was produced by a prior session's `fork` subagents under an
explicit user authorization to "assume freely," and does **not** appear in any interview transcript or
braindump I read directly. I flag every place this matters below — it means several loops that read as
polished/confident in the existing deliverables are, on inspection of the actual named primary sources,
resting on zero direct testimony. I do not treat "the previous AI session labeled it ASSUMED" as
equivalent to having independently verified it; I re-derive the evidence status from the source text
itself.

---

## Summary Table

| ID | Name | Type (closes?) | Status | Domain |
|---|---|---|---|---|
| L1 | Speculative Registration / Resale Safety Net | **Reinforcing, closes** | Confirmed core (3/4 links), one assumed closing link | Registration billing / Mess Cell |
| L2 | Skip Meal "designed balancing loop" | **Chain — does not close** | Confirmed mechanism, near-zero uptake, no evidenced return link | Kitchen forecasting |
| L3 | Capacity Redistribution (Kadamba→Bakul/Palash) | **Disconfirmed** — the load-bearing link is empirically false | Rejected as a functioning loop | Capacity/demand |
| L3b | Kadamba Demand Concentration | **Reinforcing, closes (assumed closing link)** | Candidate | Capacity/demand |
| L4 | Menu Rotation Governance Response | **Balancing, closes** | **Confirmed, strongest loop in the set** | Governance/menu |
| L5 | Menu Transparency → Selective Non-Attendance | **Chain — does not close on its own; feeds L1** | Single-sourced (1st link), candidate (2nd link) | Menu/attendance |
| L6 | Shock-Adaptive Registration Relaxation | **Balancing, closes (assumed self-limiting mechanism)** | Confirmed trigger + mechanism; single-sourced (chat testimony, not a written transcript) | Registration/billing precedent |
| L7 | Late-Night Workload → Skip → Energy Crash → Compensate | **Chain — does not close; mostly unconfirmed** | Confirmed (1st link only); rest inherited from the fictional puzzle brief | Individual behavior |
| L8 | Vendor Quality Market-Discipline | **Absent/missing loop (structurally severed)** | Assumed | Vendor economics |
| L9 | Waste-Disposal Effectiveness Suppresses Demand-Planning Pressure | **Reinforcing, closes (assumed links)** | Confirmed 1 link, assumed rest | Waste/procurement |
| L10 | "Known-But-Unowned Gap" | **Not a loop — a static state, no cyclical evidence** | Confirmed facts, no evidenced dynamic | Governance |
| — | Kitchen technology (Kadamba automated / Yuktahar manual / Bakul-Palash external) → attendance/trust | **No loop or chain built — insufficient evidence** | Structural fact confirmed; causal claim unconfirmed | Kitchen/quality |
| — | Peer/companion-absence effect on attendance | **Tested and disconfirmed as decision-determining** | Confirmed disconfirmation | Social |
| — | "Silo success masking systemic gap" | **Not built — zero direct evidence, pure inference** | Assumed, noted only in passing | Governance |

---

## L1 — Speculative Registration / Resale Safety Net (Reinforcing, closes)

**Variables**
- **SR** — Speculative Registration Rate: registrations made without firm intent to attend a given meal.
- **UR** — Unused Registration Volume: registered-and-billed meal slots the student does not attend.
- **RA** — Mess Cell Resale Activity: WhatsApp-market listings/transactions per cycle.
- **NC** — Net Cost of a Speculative Registration: money actually lost on an unused slot after any resale recovery.

**Links**
1. SR → UR **(+)**, CONFIRMED. Registering without intent mechanically produces unused slots when the student doesn't show. Direct first-person instance: *"Kadamba veg breakfast costs around ₹48 and I book it every day and never avail it"* (2026-09-03 interview). This price (₹48) is independently cross-validated by the CDS poster's Student-rate Veg Breakfast price of ₹48 (`prathyusha_braindump_2.md` §11.4) — a rare case of two independent sources agreeing on an exact figure.
2. UR → RA **(+)**, CONFIRMED. Unused slots are literally the supply feeding the resale market: *"students who've registered for a meal they know they won't eat post in a campus-wide WhatsApp group (e.g. 'Sell Kadamba veg')... Described by the respondent as common and functioning smoothly for them personally"* (2026-09-03 interview §4). Daily eater‑1: *"Yes, I have both bought and sold registrations."*
3. RA → NC **(−)**, CONFIRMED (direction). A liquid, "functioning smoothly" resale market recovers money for an otherwise-total loss, i.e., it reduces the net cost of an unused registration below the full sticker price. Skip‑3 explicitly frames resale as a source of financial upside: *"I resell breakfast very rarely, because breakfast registrations can sometimes be available at a nice price."*
4. NC → SR **(−)**, **ASSUMED** — this is the closing link and it is the weakest one. No respondent states "I register more because I know I can resell it." The strongest available evidence actually points to a *different* driver of SR — capacity-securing, not cost-insurance (see L3b) — Skip‑3: *"I do register for breakfast for the whole month because Kadamba is hard to get and it gets full."* The economic logic (a safety net lowers the marginal cost of over-committing, so people over-commit more) is standard and plausible, but it is not directly evidenced here and should not be presented with the same confidence as links 1–3.

**Closure test:** 4 links, 2 negative (links 3, 4) → **even → Reinforcing.** The loop does close, but only if the assumed link 4 holds.

**Trigger/context:** Standing, continuous — active every registration cycle (monthly), not condition-triggered.

**Delays:** Registration→realized-non-attendance delay ≈ up to a month (registration is monthly, per Daily eater‑1: *"I register for a month, not day by day"*). Resale itself is fast — same-day or near-same-day, since the WhatsApp market operates close to the meal in question.

**What it explains:** The headline paradox itself — high registration/billing volume coexisting with low attendance, without individual financial pain building into pressure on the institution, because the pain is privately absorbed and recirculated among students rather than surfaced.

**What would falsify it:** Evidence that students who use resale heavily do *not* register more speculatively than students who don't (i.e., no correlation between resale access/use and speculative-registration behavior) would kill link 4 and reduce L1 to a 3-link open chain (confirmed) rather than a closed loop.

**Note on a companion, un-closing mechanism worth naming but not counting as its own loop:** the classic "Shifting the Burden" reading of this system — that resale's success removes the *institutional* pressure that would otherwise force a billing fix — requires a second path (ghost-registration pain → institutional complaint → policy change) that is not evidenced to exist at meaningful volume anywhere in the primary sources (the project's own finding, carried over from Phase 1 governance research, is that none of the three student feedback channels has a confirmed instance of producing policy change on its own). I do not build this as a second loop because the "fundamental-fix" path essentially never fires in the evidence — there's nothing to show closing. It is better described as a **dormant/never-observed balancing path**, mentioned here for completeness, not diagrammed as an operating loop.

---

## L2 — Skip Meal: a Designed Balancing Mechanism That Does Not Close (Chain, not a loop)

**Variables**
- **NAI** — Non-Attendance Intent known in advance (a student knows before the meal that they won't attend).
- **SU** — Skip Meal declarations actually made.
- **KP** — Kitchen same-week prep-quantity forecast for that meal.
- **OW** — Over-preparation / wasted-food volume.

**Links**
1. NAI → SU **(+ as designed)**. This is the feature's entire purpose, but the evidence shows the link barely fires. CONFIRMED near-zero uptake: Daily eater‑1: *"I never use Skip Meal because it doesn't return the money."* Skip‑1: *"I have not used Skip Meal."* Skip‑2 (zero mess breakfasts all semester — maximal NAI): *"I haven't ever used Skip Meal... I don't think I've ever used that feature."* Skip‑3: *"No, I've never used Skip Meal."* Only Daily eater‑2's transcript is silent on it (not "confirmed no," genuinely unaddressed). This is 4/5 respondents confirming zero use despite several having very high NAI. **This is a real, confirmed link — it just has almost no throughput.**
2. SU → KP **(−)**. **SINGLE-SOURCED, and importantly not from a written transcript I read directly**: this comes from `MASTER_CONTEXT.md`'s record of a direct user correction made mid-session on 2026-09-13 ("Skip Meal declarations do reach the kitchen and are used for same-week prep-quantity forecasting"). Neither interview file nor either braindump states this. I carry it forward because `MASTER_CONTEXT.md` is one of my designated primary sources and records it as a direct statement, but I flag explicitly that this is weaker provenance than a transcribed interview — it is testimony recorded in a session log, not a document I can independently cross-check.
3. KP → OW **(+)**, CONFIRMED by definition — less prep relative to registered count mechanically means less over-preparation.
4. **The closing link, OW → NAI, does not exist in the evidence at all.** No mechanism connects "how much food the kitchen wasted last cycle" back to "whether a given student forms non-attendance intent." I looked specifically for an institutional feedback mechanism (e.g., a waste-driven nudge encouraging more Skip Meal use) and found none in any source. The only related feature mentioned is a registration-reminder email toggle, which is about registering, not about Skip Meal or waste.

**Closure test: this does not close.** The chain NAI→SU→KP→OW is real (with link 1's throughput near-zero and link 2 weakly sourced), but nothing evidenced or even plausible returns the causal arrow to NAI. **This corrects the prior draft's own framing**, which called this "B1" (a balancing loop) throughout, including after being revised to "confirmed mechanism, uptake near-zero" — that revision fixed link 1 and 2's status but never actually tested whether the structure closes. It doesn't. Presented here as a **chain**, not B1.

**Trigger/context:** Standing, continuous (whenever a student has non-attendance intent and the app is open).

**Delays:** SU must be declared same-week (per the two-stage model: T-4 for sourcing, same-week for prep) — i.e., days, not months.

**What it explains:** Why kitchens over-prepare relative to true attendance even though a mechanism exists that could in principle correct it — adoption failure, not design failure. This reframes "why is there always food left over/run out unpredictably" as an uptake problem, not an engineering problem.

**What would falsify/refine this:** A follow-up question ("why don't you use Skip Meal") could turn this from a chain into an actual loop if it revealed, e.g., that high perceived waste reduces trust in the app's registration system generally (a genuine candidate closing mechanism I did not find evidence for and am not asserting). Currently: no such link exists in evidence.

---

## L3 — Capacity Redistribution (Kadamba → Bakul/Palash): Disconfirmed as a Functioning Loop

**As designed/intended (not evidenced, only inferred as the "obvious" mechanism a capacity planner might expect):** Kadamba nears capacity → students redirect registration to Bakul/Palash → Kadamba's load eases → (closing) redistribution continues only as needed.

**Why this fails at the very first link, DISCONFIRMED:** the evidence shows the opposite behavior. Scarcity at Kadamba does not push students toward Bakul/Palash — it pushes them to lock in Kadamba harder. Skip‑3: *"I try to catch the registrations... I register for breakfast for the whole month because Kadamba is hard to get and it gets full."* This is a direct, first-person statement that scarcity produces **hoarding of the scarce resource**, not diversion away from it. Braindump #1's independently-sourced explanation for Bakul's persistently low registration-to-capacity ratio agrees: *"Kadamba is the established 'go-to' mess — larger, and its food is well-liked. Bakul is a comparatively new mess..."* (`prathyusha_braindump.md` §10, cross-referenced) — i.e., the gap is explained by a standing preference difference, not by any redistribution dynamic responding to Kadamba's scarcity.

**Conclusion:** this is not "a loop broken at one link" (the prior draft's framing) — it is a **loop that was never real to begin with**, because the one link that would make it operate (scarcity → diversion) is actively contradicted by direct testimony, not merely unconfirmed. I present it as **disconfirmed**, a stronger and more useful finding than "broken."

---

## L3b — Kadamba Demand Concentration (Reinforcing, candidate — closing link assumed)

This is the *actual* dynamic the evidence supports in place of L3, built independently rather than inherited.

**Variables**
- **KR** — Kadamba's perceived quality/reputation ("go-to" status).
- **KSC** — Kadamba registration scarcity (how quickly/fully its slots fill).
- **KLOCK** — Student registration-locking behavior specifically for Kadamba (registering the full month, avoiding cancellation, to guard a scarce slot).

**Links**
1. KR → KSC **(+)**, SINGLE-SOURCED / candidate. Higher perceived quality drives more demand for a fixed number of slots, so scarcity rises. Consistent with braindump #1's "go-to mess, well-liked" framing, but that framing is itself a respondent's own hypothesis, not independently verified against registration data.
2. KSC → KLOCK **(+)**, CONFIRMED directly by Skip‑3's own statement above.
3. KLOCK → KR **(?)**, **ASSUMED, low confidence — the weakest link in this document.** The only plausible closing story is a social-proof effect (a visibly full, hard-to-get mess reads as more desirable/prestigious). But the *only* direct testimony about Kadamba's crowding describes it as a **negative** experience, not a status signal: Daily eater‑1: *"most days I go around 9:00 to 9:30, and it is usually very crowded... especially after 9:15, it's very crowded, and it's not guaranteed that I'll get all the things I want."* Daily eater‑2 similarly frames crowding as a supply problem, not a draw. **I flag this closing link as genuinely uncertain, possibly even sign-reversed** (crowding could plausibly erode rather than reinforce reputation over time, which would make this a self-limiting balancing dynamic instead of a reinforcing one — the evidence does not resolve this either way).

**Closure test (as stated, assuming the link holds):** 3 links, 0 negative → even → **Reinforcing.** But given how weak link 3 is, this loop's very existence (not just its strength) should be treated as a low-confidence candidate, not a settled finding.

**Trigger/context:** Standing/continuous, not condition-triggered.

**What it explains:** Why Kadamba stays saturated and Bakul stays under-registered independent of any capacity-rebalancing policy — pure preference-driven concentration, self-sustained by registration-locking behavior, without needing any redistribution mechanism to fail (there was never one operating).

**What would falsify it:** Evidence that Kadamba's registration numbers are driven purely by fixed regional/cuisine preference (a stable trait, not a self-reinforcing dynamic) would collapse this to a static fact rather than a loop — i.e., if new students entering the system already prefer Kadamba at the same rate regardless of how scarce/crowded it currently is, there's no actual feedback, just a persistent preference. This is not ruled out by current evidence.

---

## L4 — Menu Rotation Governance Response (Balancing, closes) — the strongest confirmed loop

**Variables**
- **MF** — Menu Fatigue (dissatisfaction from menu repetition).
- **FI** — Feedback Intensity reaching the CDS Student Council.
- **ESC** — Escalation and approval by the CDS Committee.
- **MV** — Menu Variety actually implemented.

**Links, all CONFIRMED directly from the CFS Chair interview (`prathyusha_braindump_2.md` §2–3):**
1. MF → FI **(+)**. *"Before: one fixed menu for the entire semester — a real, named pain point (people get bored of the food)."* Feedback is explicitly triaged by intensity (§2), so fatigue driving feedback intensity is the document's own stated mechanism.
2. FI → ESC **(+)**. *"High-intensity feedback → a CDS committee member gets involved to decide/change something"* — an explicit, named escalation rule, not an inference.
3. ESC → MV **(+)**. *"CDS convinced the CDS Student Council, who convinced the Student Parliament, to move to a biweekly rotation. Menu also now changes monthly and is seasonal."*
4. MV → MF **(−)**, CONFIRMED by stated purpose (the rotation was explicitly done "so people get bored of the food" less), though the *magnitude* of fatigue reduction achieved was not independently measured — this is the stated intent and mechanism, not a post-hoc satisfaction survey.

**Closure test:** 4 links, 1 negative (link 4) → **odd → Balancing.** Closes cleanly. **This is the only loop in the entire project where every link traces to a single, direct, named-source account with no assumed link at all** (the caveat on link 4's magnitude is about strength of effect, not about whether the causal direction exists).

**Trigger/context:** Standing governance mechanism, active whenever complaint intensity crosses the informal high/low threshold — not condition-triggered like L6.

**Delays:** Multi-cycle — the rotation itself now runs on a biweekly/monthly cadence, and the escalation from complaint to policy change plausibly took a full semester or more (implied by "one fixed menu for the entire semester" as the prior state).

**What it explains:** That the governance structure is *capable* of closing a feedback loop end-to-end — this is the reference case that makes every *broken* loop elsewhere in this analysis (L2, L3, L10) diagnostically interesting: the failure elsewhere isn't "governance can't respond," it's "this specific channel (registration/billing accuracy) doesn't generate the kind of visible, high-intensity signal that triggers this exact escalation pathway."

**What would falsify it:** If the biweekly rotation is shown to have been decided independently of the Student Council pathway (e.g., a unilateral CDS/vendor cost decision that happened to also reduce repetition), the ESC→MV link would be spurious. Nothing in the source suggests this, but it rests on one interview account (the CFS Chair), not independent institutional minutes.

---

## L5 — Menu Transparency → Selective Non-Attendance (Chain, does not close on its own)

**Variables**
- **MV** — Menu Variety/rotation, posted in advance (shared with L4).
- **MP** — Menu Predictability (students know in advance what's being served).
- **SNA** — Selective Non-Attendance (skipping specifically on days with a disliked posted item).

**Links**
1. MV → MP **(+)**, CONFIRMED by definition — a posted rotation calendar is definitionally predictable menu information.
2. MP → SNA **(+)**, **CANDIDATE, single-sourced to the CFS Chair's own self-identified risk**, not confirmed by any student: *"because the menu is now known in advance, students can decide in advance not to come on days when they dislike the known menu"* (`prathyusha_braindump_2.md` §8). No student interview in this project's evidence base was ever asked whether they check the menu before deciding to attend — the closest related datum is Daily eater‑1's *"There is an option in the app to check the mess crowd, but I rarely check it"* (crowd, not menu, and explicitly says they rarely check even that).

**Does this close?** I looked for a plausible return path and could not find or construct one with any evidentiary support. The two candidate closing stories are: (a) SNA feeds back into L1's front end (more registered-but-unattended slots concentrated on unpopular-menu days) — this is real but it closes *into a different loop*, not back to MV/MF; (b) SNA generates per-item attendance data that CDS could use to refine future menus, closing back to MV — there is zero evidence CDS uses attendance data this way (feedback is explicitly described as poster/notification-based, §7 of the braindump, not attendance-analytics-based). **Conclusion: this is a chain, not a loop.** I explicitly correct the prior draft's "R3" label — labeling this reinforcing implies it self-escalates, but nothing shows it returning to affect its own starting variable. Its real systemic role is as an *input* to L1 (it likely raises SR/UR on specific days), not a loop of its own.

**Trigger/context:** Standing, continuous, once the rotation calendar exists (post the governance fix in L4). This is a genuine unintended second-order consequence of L4's own success.

**What it explains:** Why the L4 governance fix (menu rotation) may not have produced the full attendance improvement its designers expected — some of the gain from "less fatigue" may be offset by new, informed day-specific skipping. Not evidenced as a confirmed net effect — a plausible one.

**What would confirm it as a real loop:** A direct question already identified by the project itself and never yet asked: *"does knowing next week's menu change whether you register/show up?"* This single question, asked of existing respondents, could resolve link 2.

---

## L6 — Shock-Adaptive Registration Relaxation (Balancing, closes) — the LPG-shortage/holiday precedent, worked through carefully

**A provenance note that matters more than usual for this loop:** every fact below traces to `MASTER_CONTEXT.md`'s record of "a direct user statement" made mid-session on 2026-09-13. It is **not** present in either interview transcript or either braindump file I read. I am treating it as primary evidence because `MASTER_CONTEXT.md` is one of my five designated sources and records it as a first-person, direct account (the same evidentiary class as the 2026-09-03 self-account interview — testimony from someone with direct knowledge of the system, transcribed into a project record) — but its provenance is one level thinner than a transcribed interview, and I flag that explicitly rather than presenting it with unearned confidence.

**Getting the mechanism precisely right — this is two separate shocks, not one, and the source material's own summary sentence blurs them together while its detailed passage keeps them apart:**

- **Shock A — LPG/gas shortage:** the mess *"reduced to serving only one item for the same cost."* During the *same period*, the cancellation cap was *"raised from five to ten per month."* This is a **supply-rationing response** (fewer menu items) plus a **flexibility increase** (more cancellation headroom) — it is not, on its own wording, a switch to attendance-tracked billing.
- **Shock B — holidays/long weekends (e.g., Felicity fest, when a large share of students leave campus):** *"the mess has made registration non-compulsory — students could simply walk in and scan a QR, or register one to two days ahead at any mess, with no auto-billing penalty for non-use."* This is the actual **attendance-tracked billing precedent** — the one directly relevant to the registration/billing paradox this whole project studies.

I build the loop around **Shock B** specifically, and treat Shock A's cancellation-cap raise as a related, smaller, separately-evidenced lever (a designed flexibility increase, structurally similar in kind to L2's cancellation mechanism, not folded into this loop's causal chain).

**Variables**
- **WA** — Walk-in / actual-attendance-tracked billing in effect (degree to which billing follows real consumption rather than pre-commitment).
- **PU** — Vendor Procurement Uncertainty (day-of demand unpredictability facing the outsourced caterer).
- **IC** — Institutional Confidence in sustaining the walk-in model as standing policy.
- (Non-loop output variable, for reference: **DWM** — Demand-Waste Mismatch, which WA reduces by definition; this measures what the loop *achieves*, but is not part of the causal cycle back to WA.)

**Links**
1. WA → PU **(+)**, **ASSUMED**. More reliance on walk-in tracking removes the T-4 sourcing lock's lead-time guarantee, which is the entire stated purpose of that lock (`06-system-map.md`'s own reasoning, itself unconfirmed against a vendor-side interview — the vendor contract terms are an explicit, still-open data gap in every version of this project's research).
2. PU → IC **(−)**, ASSUMED. Higher day-of demand unpredictability plausibly lowers institutional willingness to keep running the model as a standing policy, rather than a rare exception. No institutional statement confirms this causal attribution specifically (as opposed to the simpler, non-loop explanation that the model just reverts because the holiday/shock ends — see falsification below).
3. IC → WA **(+)**, ASSUMED — lower confidence, model reverts toward the compulsory/registration-based default.

**Closure test:** 3 links, 1 negative (link 2) → **odd → Balancing.** This closes, but *only* under the endogenous "self-limiting" reading. **I deliberately separate this from a much simpler, non-loop explanation that the prior draft's language conflates with a real feedback closure: the model could just as easily revert purely because the exogenous trigger (the holiday) ends**, with zero causal contribution from PU/IC at all. That would make WA a triggered on/off switch, not a loop — a state change activated and deactivated by an external condition, no different in kind from a thermostat's schedule versus its thermostat feedback. **This is a genuine, currently unresolved ambiguity in the evidence, and I present it as such rather than asserting the loop version with the prior draft's confidence.**

**Trigger/context:** Condition-triggered only — an exogenous demand-uncertainty shock (supply shortage or a mass-exodus holiday/fest). This is **not** a standing loop; it does not run under ordinary conditions.

**Delays:** Onset (shock → policy relaxation) is plausibly fast — an administrative decision, likely days. The self-limiting mechanism (if real) accumulates over the shock's duration. Reversion happens at or shortly after the shock ends.

**What it explains:** (1) That decoupled billing is not a technical necessity — an attendance-tracked alternative has actually been operated successfully at least once; (2) a candidate explanation, not asserted as confirmed, for why it hasn't become the standing default even though it demonstrably works.

**What would falsify or disconfirm this loop:** Direct institutional testimony that the model reverts *purely* because the holiday ends (with no vendor-procurement-risk reasoning ever invoked) would collapse this from a "self-limiting balancing loop" to a simple triggered state-change — still a real and important finding, but not a loop in the strict sense used throughout this document. This is the single most important validation question this analysis produces, and it does not currently have an answer in any source I read.

---

## L7 — Late-Night Workload → Skip → Energy Crash → Compensatory Purchase (Chain, mostly unconfirmed)

**This loop is explicitly requested by the task brief in two forms** ("any loop connecting late-night eating/workload to breakfast-skipping," and the original puzzle brief's energy-crash cycle). I address both together since the evidence for them overlaps almost completely, and I am careful not to let the fictional `ProblemStatements.pdf` framing pass as evidence about IIIT‑H beyond what real respondents actually said.

**Variables**
- **AW** — Academic workload/deadline load driving late nights.
- **LST** — Late sleep time (going to bed at 3–4 AM).
- **BS** — Breakfast-skip decision.
- **EC** — Mid-morning energy crash.
- **CP** — Compensatory canteen/delivery purchase ("paying twice").

**Links**
1. AW/LST → BS **(+)**, **CONFIRMED, repeatedly, independently, across multiple real respondents** — this is the best-evidenced single causal link in the entire project. Daily eater‑1: *"Maybe if I've stayed up late because of assignments or classes, or if I sleep around 3:00 or 4:00 a.m. or later, I don't tend to wake up. I prefer sleep over breakfast."* Daily eater‑2: *"Usually, it's because I've slept very late, sometimes around 3:00 or 4:00 a.m."* Skip‑3: *"The usual reason is that I sleep very late, sometimes until around 3 or 4 in the morning, and then I'm not feeling hungry in the morning."*
2. BS → EC, **NOT CONFIRMED ANYWHERE.** No interview in this project's evidence base has ever asked a respondent what happens in the hours *after* skipping breakfast. This gap is explicitly named in `MASTER_CONTEXT.md` itself.
3. EC → CP, **NOT CONFIRMED.**
4. CP → (low-nutrition sluggishness) → back to LST, **NOT CONFIRMED**, and this closing step is pure hypothesis carried over from `ProblemStatements.pdf`'s fictional Rohan/Adit brief — explicitly excluded from being treated as evidence about IIIT‑H per this task's own instruction.

**Additional variant tested directly (late-night *eating*, not just late sleeping):** the task specifically names late-night *eating*, distinct from late *sleep*. Evidence that this specific variant exists mechanically: delivery apps accept orders campus-wide *"from morning until 11 PM"* and food can be *"eaten after that, inside"* (2026-09-03 interview §5) — so late-night eating is structurally possible and enabled. But no respondent connects eating late at night specifically (as opposed to merely staying up) to reduced morning hunger; Skip‑2's *"I might eat something after 10 or 10:30, but not before that"* is the closest adjacent datum and does not establish the causal direction either way.

**Closure test: this does not close.** Only link 1 is confirmed; nothing evidences links 2–4, and no primary source offers even a plausible closing mechanism beyond what the fictional brief supplies. **Presented here explicitly as an unconfirmed hypothesis chain with one solid, real-world-evidenced first link**, not as a loop, and not with the label "R2"/"R7" implying loop status, which both the prior deliverables used.

**Trigger/context:** If real, would be standing/continuous — driven by ordinary academic workload cycles (heavier near deadlines).

**What it explains, to the extent link 1 alone can explain anything:** why skipping breakfast correlates with staying up late — a real, well-evidenced individual behavioral pattern, distinct from and additive to the registration/billing-decoupling mechanism (L1). It does *not* currently explain any downstream financial/nutritional consequence, because that part of the chain has never been investigated.

**What would confirm the rest of the chain:** A single additional interview question, already identified as low-cost and requiring no new interview round: what do respondents actually do in the hours after skipping breakfast, and does it change their evening routine?

---

## L8 — Vendor Quality Market-Discipline (an absent/missing loop, assumed)

**This addresses the task's specific request to investigate vendor contract economics and whether decoupled billing also protects vendor revenue.**

**The key finding here is structural, not narrative: the evidence best supports the *absence* of a loop that would normally exist, rather than an actively operating reinforcing spiral.**

**Variables**
- **QD** — Quality Deficit (ingredient/menu quality shortfall relative to what would sustain full attendance).
- **AT** — Attendance for a given mess/meal.
- **VR** — Vendor Revenue realized.
- **MP** — Market pressure on the vendor to fix quality.

**The mechanism that would normally close a corrective (balancing) loop, and why it's severed:**
1. QD → AT **(−)**, weak/**SINGLE-SOURCED**: the only direct testimony connecting quality to attendance is general and not vendor- or mess-specific: *"When living in the hostel specifically, mess breakfast quality was poor, which reinforced skipping"* (2026-09-03 interview §7). Notably, for Kadamba specifically, the opposite reputation is reported (*"its food is well-liked,"* `prathyusha_braindump.md` §10) — so this link, where it exists at all, is not evenly true across all four dining halls.
2. **AT → VR, the critical link, is CONFIRMED SEVERED, not merely weak.** Billing is *"monthly and tied to the number of registrations, not attendance"* (2026-09-03 interview §4) — a direct structural confirmation that vendor/institutional revenue does not respond to attendance at all under the standing model. This is exactly the link a normal market-discipline balancing loop needs, and it is confirmed absent by design.
3. Because AT→VR does not function, MP is never generated by falling attendance, so QD is never corrected through this channel.

**Conclusion:** rather than present this as an operating reinforcing loop (which is how the prior draft's "R5" framed it, entirely as ASSUMED), I present it as what the evidence actually and more precisely supports: **a structurally absent balancing loop** — the billing-decoupling rule (RC1, already established as the project's central structural cause) doesn't just fail to punish students for inaccurate registration; it *symmetrically* removes the vendor's own market incentive to protect quality as attendance falls. This is a real, if assumed, second-order implication of a confirmed structural fact (billing decoupling), not an independently-evidenced reinforcing spiral of its own. I would not present this with a loop diagram implying an escalating cycle; the honest version is "a corrective mechanism is disabled," which is a finding about a *missing* balancing loop (Meadows leverage point #8, strength of balancing feedback), not a confirmed *positive* reinforcing one.

**Trigger/context:** Standing/continuous, wherever billing-decoupling (RC1) holds — i.e., every day the standing model is in effect (not under the L6 shock-adaptive exception, where AT→VR is, notably, briefly restored).

**What it explains:** Why any quality problems that do exist (Bakul's off-site sourcing and reported "untidy" facilities condition, if real — see below on evidentiary weakness) would have no automatic path to self-correction under the standing billing model, independent of whether anyone has evidenced that vendors are actually cutting corners.

**What would falsify/refine this:** Direct confirmation of the open-tender contract's terms (fixed-price vs. cost-passthrough — an explicit open item in `prathyusha_braindump_2.md`'s own list) would determine whether there's even a margin incentive for a vendor to want to cut quality in the first place; this analysis cannot currently confirm that motive exists, only that the corrective mechanism that would catch it if it did exist is absent.

---

## L9 — Waste-Disposal Effectiveness Suppresses Demand-Planning Pressure (Reinforcing, closes — assumed links)

**This addresses the task's specific request to investigate waste/composting and whether it removes pressure for a demand-planning fix.**

**Variables**
- **UR** — Unused Registration Volume (shared with L1).
- **WV** — Waste Volume generated.
- **WD** — Waste Disposal Effectiveness (how well/invisibly waste is handled).
- **VP** — Visible Cost/Pressure perceived from the waste problem.

**Links**
1. UR → WV **(+)**, plausible but **its magnitude is explicitly unmeasured** — `MASTER_CONTEXT.md` states directly: *"no waste volume figure exists anywhere in this project."* I flag an important complication the prior draft did not fully reckon with: if kitchens already portion for something closer to *true expected* attendance rather than full registered count (a live, separately-flagged, evidenced-but-unclosed candidate mechanism — see the "under-provisioning" chain noted in `07-systemic-problem-analysis.md`, itself explicitly rejected as a loop for lacking a closing link), then UR does **not** map cleanly 1:1 onto WV — some of the registration/attendance gap may already be silently absorbed by under-cooking relative to registered count, not converted into visible plate waste at all. This is a genuine, unresolved tension between two candidate mechanisms in the evidence, not a settled fact either way.
2. WV → WD **(+)**, CONFIRMED. Kadamba's waste is *"split into production waste and plate waste; both go to a garbage collector who transports it to an outside compost facility. When food is suspected contaminated, a sample is sent to a lab for testing"* (`prathyusha_braindump_2.md` §10), independently corroborated by the externally-audited FSSAI "Eat Right Campus" 5-star Exemplary certificate (§11.1) — real, third-party evidence the disposal/food-safety process functions competently.
3. WD → VP **(−)**, ASSUMED. A competently and invisibly disposed-of waste stream generates no visible cost signal — standard systems logic, not directly evidenced (no source discusses institutional "pressure" language at all).
4. VP → UR **(−)**, ASSUMED, and with essentially **zero observed instances of this ever actually firing**: none of this project's documented institutional responses (the confirmed menu-rotation fix in L4, the single-sourced-and-unverified December 2024 cancellation-cap tightening, the shock-triggered L6 relaxation) were driven by waste-visibility pressure specifically — they were driven by menu-fatigue complaints, workload, and external shocks respectively. This closing link is the weakest kind of assumption in this document: not just unconfirmed, but never observed to occur in any of the concrete institutional-response episodes this project has actually documented.

**Closure test:** 4 links, 2 negative (links 3, 4) → **even → Reinforcing.** Closes only under fully assumed links 3–4, and link 1's magnitude is itself unmeasured.

**Trigger/context:** Standing/continuous.

**What it explains:** Why an efficient, well-run, externally-certified disposal operation can coexist indefinitely with an unaddressed registration/attendance gap — the same "Shifting the Burden" shape as L1, on the supply side rather than the demand side: the symptom (waste) is competently absorbed before it can ever generate the political pressure needed to fix the root cause (billing decoupling).

**What would falsify it:** A single waste-volume measurement campaign (never yet run) that showed waste volume is small/stable/insensitive to registration accuracy would substantially weaken this loop's premise (link 1). Independent evidence that a facilities/finance office has, at any point, cited waste cost data in a mess-policy discussion would confirm the currently-unobserved link 4.

---

## L10 — "Known-But-Unowned Gap": a Confirmed Static State, Not a Reinforcing Loop

**The prior draft's "R4" claims a reinforcing loop (awareness → inaction → normalization → reduced urgency → less future awareness-refresh → repeat, worsening). I tested this rigorously and it does not hold up as a loop.**

**What is actually confirmed, from `MASTER_CONTEXT.md`'s record of the 2026-09-13 correction (again, chat-session testimony, not a written transcript):** the CFS Chair is aware of the turnout gap (a tentative 35–45% breakfast figure), and this awareness *"has never reached a registration or billing policy discussion."* Combined with confirmed structural fragmentation (the academic office has explicitly *"no say in mess timings or hostel matters"* — 2026-09-03 interview §9 — and CDS/CFS's own governance structure splits menu, execution, and billing decision rights across different bodies per `prathyusha_braindump_2.md` §1–2), this describes a **persistent equilibrium of inaction**, not a documented escalating cycle.

**Why I do not build this as a loop:** a reinforcing loop requires evidence that the condition is getting *worse over successive cycles* — that inaction this month causes more inaction (or a bigger gap, or lower future urgency) next month, measurably more than the month before. Nothing in any source shows this. The gap is described as stable and known, not growing, and "normalization" and "reduced urgency" are plausible narrative color with no testimony behind either variable. **This is a confirmed fact pattern presented honestly as a static structural condition** (fragmented authority + known gap + no action), not dressed up as a self-worsening feedback loop it isn't evidenced to be.

**What would turn this into a real loop:** Evidence across multiple points in time that the gap's visibility to decision-makers is *decreasing* over successive cycles (e.g., the same 35–40% figure being treated as more "normal"/less noteworthy in a later conversation than an earlier one) would support an actual reinforcing dynamic. No such time-series exists in this project's evidence.

---

## Investigated and explicitly rejected as loops or chains (negative findings, stated plainly)

**Kitchen technology differences (Kadamba automated / Yuktahar manual / Bakul-Palash externally-sourced) → attendance or quality perception.** The *structural* fact of three different kitchen models is CONFIRMED: Kadamba runs an on-site automated kitchen (roti line, multi-item cooker, tilting curry/steam machine — `prathyusha_braindump_2.md` §12); Bakul and Palash currently run off an external, off-site kitchen pending the Felicity facility (§9, §11.4). **But no primary source I read — neither interview file, neither braindump — connects any of this to a student's attendance decision or perceived trust/freshness.** The "manual/live cooking at Yuktahar," "staff-run conveyor belt at Kadamba," and "plate-trust deficit" claims that appear in the existing `06-system-map.md` originate entirely from a prior session's authorized-assumption subagent pass, not from any source I was asked to read directly, and I decline to promote them to even a labeled "assumed chain" here — the evidentiary floor is below what this document's own bar requires. This is a genuine negative finding, not an oversight: **investigated, insufficient evidence for a loop or even a candidate chain.**

**Peer/companion-absence effect on attendance.** Explicitly tested by the interview guide (a purpose-built question: *"If that person was away for a week, do you think your attendance would change?"*) and answered consistently across respondents: Daily eater‑1 — *"No, it wouldn't really matter."* Daily eater‑2 — *"Probably not."* Skip‑1 — *"No, not particularly."* Skip‑2 — *"No, my attendance wouldn't change."* Skip‑3 (the one partial exception) — *"Not really. My friends are a positive factor in deciding to go, but if I have to go, I'll go."* **CONFIRMED, disconfirmed as a decision-determining mechanism** across 5/5 respondents who addressed it; at most a weak, non-determining motivator for one respondent. No loop built.

**"Silo success masking systemic gap"** (the idea that L4's own visible success reduces institutional appetite to audit the quieter registration/billing gap). This is entirely a systems-thinking inference with no testimony behind any of its variables (no institutional actor discusses "auditing appetite" anywhere in any source). Noted here for completeness per the task's instruction not to hide plausible mechanisms, but explicitly **not built out as a loop** — there is nothing to evidence-check.

---

## Cross-Loop Synthesis: the shared structural parameters

Several loops above are not independent mechanisms so much as different symptoms of the same two or three confirmed structural facts, worth stating once rather than re-deriving per loop:

1. **Billing decoupled from attendance (CONFIRMED, 2026-09-03 interview §4)** is the single parameter that (a) enables L1's low-net-cost-of-speculation dynamic, (b) severs the corrective link in L8, and (c) is the exact thing L6 demonstrates the institution *can* suspend, on a temporary, condition-triggered basis. This is a Meadows-leverage-point-5 "rule of the system" — nearly every loop in this document either runs *because* this rule exists (L1, L8, L9) or exists specifically to show a rare case where it doesn't (L6).
2. **Fragmented decision rights** (menu ≠ execution ≠ academic scheduling ≠ billing policy, no single owner) is why L4 can close (menu has a real owner and escalation path) while L10 cannot move past a static state (registration/billing accuracy has no equivalent owner or escalation path) — the *presence* of L4 and the *absence* of an L10-equivalent loop are best read as two outputs of the same governance-fragmentation fact, not two unrelated findings.
3. **No source in this project ever measures waste volume, attendance-by-mess time-series, or vendor contract terms.** L9's magnitude, L8's motive, and L3b's true driver all terminate in the same three open data gaps. This is worth naming as a single finding rather than three separate "outstanding data collection" bullets: the project's evidentiary ceiling is set by the same three missing instruments across multiple otherwise-distinct loops.

---

## Falsification Summary (one line per loop, for quick reference)

| ID | Falsified/disconfirmed if… |
|---|---|
| L1 | Resale users don't register more speculatively than non-users |
| L2 | (n/a — already a chain) confirmed as such unless a real OW→NAI mechanism is found |
| L3 | (already disconfirmed) |
| L3b | New students prefer Kadamba at a fixed rate regardless of current scarcity/crowding |
| L4 | The rotation decision is shown to be independent of the Student Council escalation path |
| L5 | Students report never checking the posted menu before deciding to attend |
| L6 | Institution states the model reverts purely because the holiday ends, never citing vendor/procurement risk |
| L7 | (largely already unconfirmed) — falsified further if respondents report no behavior change at all after skipping |
| L8 | Vendor contract is shown to be fully cost-passthrough with no margin incentive to cut quality |
| L9 | A waste-volume measurement shows waste is small/stable and insensitive to registration accuracy |
| L10 | Time-series evidence shows the gap's visibility to decision-makers actually declining cycle over cycle |
