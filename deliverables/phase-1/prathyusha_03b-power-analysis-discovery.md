# Phase 1 · Activity 3 — Power Analysis: Discovery Notes (prathyusha, 2026-09-06)

**Status:** 🟡 Working notes from the first-principles power/leverage discovery pass —
Parts 1-13 of the analysis framework, stopping deliberately before finalizing any map
(per the framework's own instruction to interrogate before concluding). This file is
the reasoning and evidence base; `prathyusha_03-power-interest-leverage-map.md` is the
polished deliverable built on top of it. Confidence legend: ✅ confirmed · 🟡 plausible/
inference · ❓ unknown/research target · ⛔ considered and rejected.

Ten open questions are logged at the end, unanswered as of this writing — everything
downstream that depends on them is flagged accordingly rather than assumed.

---

## Part 1 — Read and Audit Previous Work

**System boundary (unchanged from Activity 1):** breakfast registration/billing/service
across four messes, intersecting the academic schedule at the boundary. Lunch/dinner,
upstream supply chain, and IT infrastructure remain outside the drawn boundary —
several Activity 2 boundary-actors (Portal/IT owner, Facilities) live in that grey zone.

**Reconstructed flows (confirmed unless marked otherwise):**
- Decision flow: Mess Committee (policy) → Mess Office (execution) → Vendors
  (day-to-day) — three separate actors, previously collapsed into one, now split ✅
- Money flow: Students → Mess Office (billing) → Vendors (contract-based, mechanism ❓)
  — no reward anywhere for attendance accuracy
- Information flow: student intent → portal → Mess Office → 4-day-old forecast →
  kitchen; feedback (rating/email/Ping) flows in, whether it flows anywhere
  consequential is ❓
- Resource flow: per-mess procurement (✅), cuisine-specialized (South Indian/North
  Indian/Jain)
- Conflicts already identified: convenience vs. Mess Office workload; billing
  certainty vs. attendance uncertainty; Academic schedule vs. mess schedule
- Missing relationships already identified: Academic administration ↔ any
  mess-governance actor (zero edge, three ways); Vendors ↔ Students (no direct
  channel)

**Stakeholder Map revision flagged:** Activity 2 confirmed Academic administration has
no formal role in mess timing. It did **not** determine whether Academic
administration has veto/blocking power over a hypothetical mess-side proposal to shift
service hours — a different question a power lens exposes. Left open, not assumed
either way (see Q1).

## Part 2 — Power Taxonomy for This System

| Power type | Who holds it here | Confidence |
|---|---|---|
| Formal authority | Mess Committee (menu/policy), Mess Office (operations), Warden (vendor/structural) | ✅ split confirmed; Office/Warden boundary ❓ |
| Decision power | Mess Committee for menu; Mess Office for operational rules (Dec 2024 change issued by Office alone) | ✅ for the one precedent |
| Veto power | ❓ unknown who can veto a Committee decision | ❓ |
| Implementation power | Vendors (cook/serve); Mess Office (orders) | ✅ |
| Operational power | Vendors, kitchen/serving staff | ✅ |
| Resource power | Vendors (kitchens/labor); Mess Office (ordering relationship) | ✅ |
| Information power | Mess Office (registration/ordering data); Portal/IT owner (❓ identity) | 🟡/❓ |
| Technical power | Portal/IT owner (❓); unofficial tool developers (✅ exist) | 🟡 |
| Expertise power | ❓ no evidence any actor's expertise is currently load-bearing | ❓ |
| Positional power | Mess Committee's faculty chair — plausible informal access to other faculty | 🟡, inferred |
| Network power | Mess Cell (slack↔need); Ping (sentiment↔visibility) | ✅ existence, 🟡 effect |
| Access power | ❓ who among students has personal access to Warden/Committee | ❓ |
| Bargaining power | Vendors (if switching costs high, ❓); Academic administration (needs nothing from mess system) | 🟡/✅ |
| Exit power | Students — can substitute to Vindhya/delivery/skipping; system cannot exit students | ✅ |
| Economic power | Mess Office/vendors absorb a bad forecast better than a student absorbs walk-in markup | 🟡 |
| Collective power | Students, hypothetically, via Mess Cell scale or coordinated feedback — untested | 🟡, central open question |
| Social/normative power | Roommates/friends over attendance (✅); seniors→juniors (❓) | ✅/❓ |
| Reputational power | Ping — can attach public reputational cost | ✅ existence, 🟡 effect |
| Legitimacy power | Mess Committee's faculty chair, via faculty status | 🟡 |
| Agenda-setting power | Mess Office — its own workload concern set the last policy item on record | ✅ Office, ❓ anyone else |
| Non-decision power | Academic administration, by omission — no mechanism for the overlap to become a decision anywhere | ✅ (a confirmed absence) |
| Interpretive/framing power | Mess Office's Dec 2024 framing ("workload"/"food safety") vs. students' ("less flexibility") | 🟡 |
| Dependency power | Vendors — Mess Office depends on them with no confirmed backup | 🟡 |
| Procedural power | Mess Office — controls the portal, the only channel most intentions become visible through | ✅ |
| Informal power | Roommates/friends, Mess Cell, Ping, unofficial tool developers | ✅ |

## Part 3 — Decision-Rights Matrix (26 domains, compressed by shared structure)

| Domain | Proposes | Approves | Vetoes | Implements | Bears risk | Consulted | Not consulted | Precedent |
|---|---|---|---|---|---|---|---|---|
| Grouped: registration rules, cancellation limits, Skip Meal, walk-in pricing, portion guidance, feedback handling, exceptional-case enforcement | Mess Office (✅ one case) | ❓ Committee sign-off required? | ❓ | Mess Office + Vendors | Students (cost/flexibility); Vendors (workload) | ❓ | Students appear informed, not consulted (Dec 2024) | Dec 2024 change |
| Menu design | Mess Committee, "with student input" | Mess Committee | ❓ | Vendors | Students; Vendors | Students (✅ channel exists) | ❓ weight of input | ❓ none confirmed |
| Mess capacity, veg/non-veg/Jain structure | ❓ | ❓ | ❓ | Warden | Students; Vendors | ❓ | ❓ | Bakul's creation |
| Vendor selection/contract terms | ❓ | Warden | ❓ | Warden, Vendors | Vendors; students indirectly | ❓ not evidenced | Students | ❓ none |
| Breakfast timing | ❓ nobody has ever proposed a change, evidenced | ❓ | ❓ | — | Students (the whole paradox) | ❓ | Everyone, apparently | Unknown — no evidence timing ever changed |
| Academic class timing | Academic administration | Academic administration | ❓ | Academic administration | Students | Faculty presumably | Mess-side actors entirely | ❓ |
| Portal/data/reporting | ❓ entirely unidentified | ❓ | ❓ | ❓ | Everyone dependent on it | ❓ | Everyone | ❓ |
| Waste handling | ❓ | ❓ | ❓ | ❓ Facilities placeholder | ❓ | ❓ | ❓ | ❓ |
| Mess Cell/informal resale | Students | N/A | N/A | Students | Students | N/A | The formal system entirely | The market's own emergence *is* the precedent |

**Clearest finding:** for most domains, "who approves"/"who can veto" is ❓ unknown, not merely undocumented — no source has described an approval/veto step for anything except the menu and the one Dec 2024 change. Absence of evidence about power is itself evidence about where power is invisible.

## Part 4 — Formal Power Trace

| Actor | Formal mandate (evidenced) | Confirmed domain | ❓ Unknown |
|---|---|---|---|
| Mess Committee | Menu/policy, faculty-chaired | Menu | Whether it approves Office operational changes |
| Mess Office | Operations — ordering (4-day lead), portal, policy communication | Dec 2024 change | Whether Committee sign-off is needed; relationship to Warden |
| Warden | Vendor management, structural change | Stated in Activity 1 | Never observed in action — no precedent names it doing anything specific |
| Academic administration | Class schedule, total | Class timing | Whether ever *asked* about coordination vs. simply never engaging |

No org chart, reporting line, or budget document exists for any of these — every claim
traces to one respondent's account or two dated public-source articles about one
policy event. Thin evidence base, stated directly rather than smoothed over.

## Part 5 — Informal Power Trace

| Source | Mechanism | Target | Outcome | Confidence |
|---|---|---|---|---|
| Roommate/friend presence | Direct social prompt | Individual attendance decision | Increases attendance probability | 🟡 (real + 2 synthetic personas agree, still 1 real datum) |
| Mess Cell | Collective visibility, informal pricing | Students with slack registrations | Converts total loss into partial recovery | ✅ exists, 🟡 scale |
| Ping | Public reporting/visibility | Mess Committee/Office | 🟡 salience increase, no confirmed decision produced | 🟡 |
| Unofficial tool developers | Technical intermediation | Adopting students | 🟡 manual→automated registration shift | 🟡 low confidence |
| Faculty chair | Personal collegial access | Academic administration (hypothetical) | ❓ no evidence bridge used | ❓ |
| Seniors → juniors | Hypothesized norm modeling | Junior habits | ❓ | ❓ |

## Part 6 — Interest Analysis (stated vs. structural incentive vs. observed behavior)

| Stakeholder | Stated interest | Structural incentive | Observed behavior | Gap |
|---|---|---|---|---|
| Students | Convenient, affordable, timely food | Billing identical regardless of attendance — no accuracy incentive | Register broadly; attendance varies | Large |
| Mess Office | Not directly stated | Reduce operational workload (confirmed motive) | Tightened cancellation rules (Dec 2024) | Small — unusually clean alignment |
| Mess Committee | Balance satisfaction/feasibility | ❓ unclear what it's rewarded/penalized for | ❓ no observed independent action | Unknown — least-evidenced pairing |
| Vendors | Contract renewal, predictable volume (inferred) | Paid on 4-day forecast regardless of attendance (❓ mechanism) | Continue producing to forecast | ❓ |
| Academic administration | Its own scheduling goals | No incentive tied to mess outcomes | Total non-engagement | None — explains the sleeping stakeholder |
| Mess Cell participants | Recoup cost | Direct financial, immediate | Active market | None — cleanest match in the system |

## Part 7 — Incentive → Behaviour → System Effect Chains

1. Billing by registration, not attendance → no accuracy incentive → registration
   count structurally overstates true intended attendance. ✅
2. Skip Meal returns ₹0 vs. Mess Cell's partial/full recovery → rational students
   prefer resale over Skip Meal with advance notice → low Skip Meal usage reflects
   incentive design, not low awareness. 🟡 (teammate's dominant-strategy hypothesis)
3. Walk-in priced 70-90% above registered → standing incentive to register under
   uncertainty ("register just in case") → registration inflated independent of any
   subsequent no-show. 🟡 (teammate hypothesis)
4. Mess Office rewarded for reduced workload → tightens flexibility (Dec 2024) →
   reduces students' ability to correct a registration close to service → plausibly
   *increases* the very pattern the policy targeted. 🟡 — candidate "fix that fails"
5. Academic administration experiences zero consequence from the overlap → issue never
   reaches its agenda → persists indefinitely with no actor positioned to resolve it
   unilaterally. ✅ structurally confirmed by the total absence of relationship.

## Part 8 — Bargaining Power / Dependency Analysis

| Relationship | A depends on B for | B depends on A? | Classification |
|---|---|---|---|
| Students → Vendors | Food itself | No | Strongly asymmetric |
| Vendors → Mess Office | Forecast, 4 days ahead | Yes, partially | Moderately asymmetric |
| Mess Office → Students | Accurate registration behavior | No — students bear no cost of inaccuracy | Strongly asymmetric, in the inconvenient direction |
| Academic administration ↔ Mess system | Nothing | N/A | Zero dependency, either way |
| Mess Cell ↔ formal system | Nothing (operates outside it) | Formal system may be quietly benefiting without acknowledging it | Mutual independence, functionally convenient |

**Central finding:** the actor with least to lose from inaccurate registration (the
individual student) controls the one input every other actor's forecasting depends on
— an unusual bargaining position, not conventionally "powerful," but holding an
irreplaceable, costless-to-misreport input.

## Part 9 — Precedent

| Precedent | Trigger | Raised by | Decision-maker | Decision | Outcome |
|---|---|---|---|---|---|
| Bakul's creation | Kadamba's non-veg capacity ceiling | ❓ unknown | ❓ unknown, generically "the institute" | New mess established | ✅ exists; uptake remains low relative to capacity |
| Dec 2024 cancellation tightening | Staff workload + Kadamba renovation constraints | Mess Office | Mess Office (unilateral, as far as evidenced) | Re-registration after cancellation banned; weekly caps | 🟡 unclear if still in force |
| Anything re: breakfast hours, class-timing coordination, or a complaint producing policy change | — | — | — | — | **"Precedent currently unknown"** — no source produces a single example |

## Part 10 — Resource Control Map

| Resource | Controls | Can access | Cannot access | Advantage created |
|---|---|---|---|---|
| Money (billing) | Mess Office | Students (as payers) | — | Office sets terms students can't negotiate individually |
| Food/kitchen infrastructure | Vendors | Serving staff, students (as recipients) | — | Vendors control what everyone ultimately needs |
| Registration/attendance/complaint data | Mess Office (presumed); Portal/IT owner (❓) | ❓ unclear if Committee sees it directly | Students — no aggregate visibility | Data-holder controls the only evidence base for the paradox |
| Formal complaint channels | Mess Office (recipient) | Students (senders) | — | One-directional, no confirmed downstream visibility |
| Informal escalation (Ping, Mess Cell) | Students/Ping collectively | Any student, in principle | Students unaware they exist | Two-tier access depending on informal knowledge |
| Time (4-day procurement window) | Mess Office/Vendors, structurally | — | Students — cannot affect same-day decisions | A hard constraint limiting everyone equally — an exception to "unequal access" |
| Institutional legitimacy | Mess Committee (via faculty chair) | — | Students, structurally, as individuals | Not acquirable individually, only collectively |

**Flag:** students experience the full cost of every domain above and control access to
none of them directly — not billing terms, not the evidence base, not the legitimacy
needed to be taken seriously collectively.

## Part 11 — Leverage Rights Table

| Stakeholder | Can change directly | Can block | Can implement | Can bypass | Can mobilize | Can provide info | Can create workaround |
|---|---|---|---|---|---|---|---|
| Students (individual) | Own registration/cancellation | No | N/A | Walk-in, substitutes | No | Own data | Mess Cell, unofficial tools |
| Students (collective, hypothesized) | ❓ untested | ❓ | N/A | N/A | 🟡 via Mess Cell/Ping — untested as deliberate strategy | Aggregate patterns, if pooled | The informal system already is this |
| Mess Committee | Menu | ❓ | No (relies on Office/Vendors) | N/A | Faculty-chair network, unconfirmed | ❓ unclear what data reaches it | N/A |
| Mess Office | Operational rules, ordering | ❓ | Yes | N/A | N/A | Registration/ordering data | N/A |
| Warden | Vendor contracts, structural | ❓ | Via Vendors | N/A | N/A | ❓ | N/A |
| Vendors | Day-to-day quality/quantity | Could refuse a term (❓ never observed) | Yes — literal production | N/A | N/A | Waste/shortfall data — not confirmed to reach anyone | N/A |
| Academic administration | Class schedule, entirely | N/A — no mess actor has ever needed its approval | N/A | N/A | N/A | N/A | N/A |

Avoiding flat "high leverage" labels: e.g. Mess Office has high leverage over
operational rules specifically, unconfirmed leverage over menu, and zero leverage over
class timing — three different values for one actor.

## Part 12 — Power vs. Leverage, Investigated Not Assumed

**Does evidence support students having high collective leverage?** Partially,
unevenly: Mess Cell demonstrates real capacity for self-organization around a shared
problem — already realized informally. No evidence that capacity has ever been
*directed at* a governance decision rather than a peer-to-peer transaction. Ping shows
a visibility channel exists; no confirmed instance of it producing a decision.

**Conclusion, held as hypothesis:** students plausibly occupy a **low formal power /
potentially high but currently unexercised leverage** position — "sleeping leverage,"
not simply "low power, high leverage." The mechanism exists in miniature (Mess Cell)
but has never been aimed at the governance layer. High-value, testable — see Q7.

| Quadrant | Stakeholders | Basis |
|---|---|---|
| High power + high leverage | Mess Office | Confirmed operational authority; its one action changed real behavior |
| High power + low leverage (over the paradox specifically) | Academic administration | Total authority over its own domain, structurally disconnected from mess outcomes |
| Low power + high leverage (hypothesized, sleeping) | Students (collectively); Mess Committee's faculty chair individually | Neither observed exercising this; both structurally positioned to |
| Low power + low leverage | Individual students acting alone, guest diners | Real but marginal |

---

## Part 13 — Ten Open Questions (unanswered as of 2026-09-06)

1. Has the breakfast/class-timing overlap ever been raised *with* the Academic
   administration by anyone, even informally?
2. Does the Mess Committee need to approve Mess Office operational changes, or can the
   Office act unilaterally?
3. How are vendors actually compensated — fixed contract, per-meal, per-registration,
   or something else?
4. Is there any known instance of a vendor renegotiating or pushing back on a term?
5. Who actually sees per-meal ratings once submitted?
6. Is there an elected/appointed student representative on the Mess Committee, or is
   input gathered another way?
7. Has there ever been an organized student effort (petition, mass message) aimed at
   changing a mess rule, as opposed to individual complaints?
8. Are the Kadamba renovation and its Dec 2024 policy changes still in effect, reverted,
   or something in between?
9. Is there a named person/office the public email channel reaches, or a general inbox?
10. Does the Mess Committee ever discuss anything beyond the menu, or is menu
    understood as its full remit by everyone involved?

Everything in `prathyusha_03-power-interest-leverage-map.md` that depends on these
remains flagged 🟡/❓ until answered.
