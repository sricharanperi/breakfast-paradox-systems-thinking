---
title: "System Map"
subtitle: "IIIT Hyderabad Breakfast Mess System"
---

# Overview

Phase 1 established who is involved (Stakeholder Map), who holds power (Power-Interest/Leverage Map), what actually happens step by step (Process Trace), and how it repeats over time (System Timeline). This map holds all four still images side by side, as one picture: actors, the process flow, the resources and constraints that shape it, and the points where the system visibly strains — a bottleneck, a tension, or a feedback channel that carries input without a confirmed output.

Everything below is built from facts already confirmed in Tasks 1-5. No new claim is introduced here; this map is a synthesis, not a new data-collection round.

# Map Actors, Processes, Information, Resources and Constraints

**Actors:** Students (registrant, billed party, consumer); three governance bodies — Mess Committee (policy), Mess Office (operations), Warden (vendors and structural change); per-mess vendors and kitchen staff; Academic administration (sets the class schedule, holds no formal role in mess governance); the informal Mess Cell resale market; three feedback channels (in-app rating, public email, Ping).

**Process flow:** registration (monthly, in advance) feeds billing (calculated from registration count, not attendance), which feeds a four-day forecast to vendors, who cook against that fixed figure. The service window runs 7:30-9:30 AM, with the crowd building continuously toward the close. The outcome for any given registration is one of: eaten, run out, or no-show.

**Resources:** the registration and billing platform; four physically distinct mess facilities and kitchens; the personal QR access credential; the four-day procurement lead time itself, which functions as a resource constraint shared equally by every actor rather than an asset any one of them controls.

**Constraints:** billing is registration-based, not attendance-based; cancellation is capped at five per meal type per month; the four-day lead time means no same-day signal — a cancellation, a Skip Meal toggle, a sudden rush — can change what is actually cooked; mess hours and the academic class schedule are set independently, with no formal coordination mechanism between them.

![System Map](assets/diagram1-system-map.png)

The registration/billing platform, personal QR credential, in-app rating feature, Skip Meal toggle and cancellation flow are the system's technology layer; the billing model, walk-in markup, procurement lead time, per-mess capacities and vendor contracts are its business layer; the class schedule, cuisine-preference culture, peer presence and the four physically separate kitchens are the social/environmental layer the technology and business layers sit inside but do not control. Grouped this way:

![Users, Technology, Business and Social/Environmental Factors](assets/diagram3-mapping-sprint-quadrants.png)

Two things this grouping makes visible that the process-flow view above does not: first, every technology component in this system is a **student-facing** one — there is no equivalent digital tool on the vendor/Mess Office side visible to this research, so the system's only real-time data comes from one side of the transaction. Second, the social/environmental layer contains the two factors with the least formal connection to anything else in the system — the class schedule and the cuisine-preference culture — yet both visibly shape registration and attendance behaviour more than any single business rule does.

# Trace the Service Delivery Timeline (Frontstage, Backstage and Support Processes)

The same system, cut a third way: not by actor or by category, but by what a student can and cannot see, laid out across the actual timeline of one registration-to-plate cycle. This is a service blueprint — physical evidence, frontstage student actions, the line of visibility, backstage mess/vendor actions, and the support processes underneath, mapped against five time stages from monthly registration through the morning's service window to the feedback channels that follow it.

![Service Blueprint](assets/diagram8-service-blueprint.png)

The line of visibility is crossed only twice in the entire monthly cycle: once at registration, once (rarely) at rating. Every decision that actually determines the outcome — whether to go, what to eat, whether to wait for a friend — happens entirely within the frontstage lane, with nothing crossing back from backstage to inform it in real time, and nothing crossing forward from that decision to backstage in time to change what gets cooked. The four-day procurement lead time and the billing-by-registration rule, named separately elsewhere in this document, are visible here as the specific structural reason the blueprint has no real-time crossings in either direction.

# Identify Conflicts and Dependencies

**Dependencies:** students depend on vendors for food itself; vendors do not depend on any individual student. Vendors depend on the Mess Office for a forecast fixed four days ahead; the Mess Office depends on students to register accurately, but nothing in the billing structure requires that accuracy. This is the one dependency in the system where the party with less to lose controls an input the other party cannot substitute.

**Conflicts:** billing certainty (needed by the Mess Office and vendors to forecast) against attendance uncertainty (a real feature of student life, not a defect); flexibility (students and the Mess Cell market want more of it) against workload (the Mess Office's confirmed motive for its one policy change, which reduced flexibility); the 8:30 AM class start against the 7:30-9:30 AM breakfast window, a conflict neither side is positioned to resolve alone since Academic administration and mess governance share no formal channel.

# Represent Formal and Informal Structures

**Formal structure:** three separate governance actors (Mess Committee, Mess Office, Warden), each with a defined but partially-overlapping authority, sitting alongside Academic administration, which is formally external to mess governance entirely.

**Informal structure:** the Mess Cell WhatsApp resale market, which recovers value from an unused registration that the formal Skip Meal tool does not; Ping, the student publication, which creates public visibility for mess issues without any confirmed authority to act on them; at least one unofficial registration-management tool operating outside the official portal.

![Power and Information Flow Network](assets/diagram9-power-flow-network.png)

The formal and informal structures do not meet cleanly at one point. Academic administration has no formal or informal relationship to any of the three governance actors — a confirmed absence, not a gap in this research. The Mess Cell market operates entirely outside the formal registration and billing system, transacted through the same access credential the formal system issues.

# Highlight Bottlenecks, Tensions and Feedback Loops

**Bottlenecks:**

- The four-day procurement lead time. Nothing in the system lets a same-day signal change what is cooked, regardless of which actor wants to act on it.
- The 9:30 AM close. Item run-outs are confirmed by respondent accounts, concentrated in the period just before close.
- The complete absence of a formal channel between Academic administration and the three mess-governance actors. The one variable most likely to resolve the core schedule overlap sits with an actor no governance body can formally reach.

**Tensions:**

- Registering broadly (individually rational, given walk-in pricing and scarcity at popular messes) against system-level waste (the aggregate effect of that same behaviour).
- The Mess Cell resale market outcompeting Skip Meal for the identical situation — advance knowledge of non-attendance — because it returns value and Skip Meal does not.

**Feedback loops (student-input channels):** three real channels — in-app rating, public email, and Ping coverage — carry student input into the system. None has a confirmed instance of producing a policy change. Inputs exist; a confirmed output does not.

**Feedback loops (causal loop diagrams):** the four loops below trace *why* the system keeps producing the same outcomes, not just that it does. Each is drawn as a closed cycle with a polarity sign (+ = moves the same direction as its cause, − = moves the opposite direction) on every link — a loop is reinforcing (R) if it contains an even number of − links, balancing (B) if odd.

**R1 — registering broadly, recovering via resale (reinforcing, confirmed).** Because registering costs nothing extra and unused registrations can be resold, the perceived cost of over-registering stays low — which sustains the same registration behaviour that produces the next round of unused registrations.

![R1 — Registration/Resale Reinforcing Loop](assets/diagram4-cld-r1-resale.png)

This is a textbook Shifting the Burden structure (Senge): the Mess Cell resale market is a *symptomatic* solution — it relieves the financial pain of a no-show without anyone needing to fix the *fundamental* problem (billing decoupled from attendance). Precisely because the symptomatic fix works well enough, the pressure that would otherwise force the fundamental fix never builds.

**B1 — Skip Meal was designed to balance kitchen preparation against no-shows (balancing, intended — but the corrective link does not fire).**

![B1 — Skip Meal Balancing Loop](assets/diagram5-cld-b1-skipmeal.png)

The loop as designed is a standard balancing structure: a gap between actual over-preparation and the zero-waste target should drive Skip Meal usage, which should reduce preparation, which should close the gap. The dashed red link is where it breaks — zero of six respondents who addressed Skip Meal have ever used it. The gap persists not because the mechanism is poorly designed in principle, but because the first link in the loop never actually engages.

**B2 — capacity should redistribute toward under-used messes as Kadamba nears capacity (balancing, intended — again broken at one link).**

![B2 — Capacity Redistribution Loop](assets/diagram6-cld-b2-redistribution.png)

Same pattern as B1: the loop is structurally sound (scarcity should push demand toward Bakul/Palash), but the confirmed evidence shows the opposite micro-behaviour at the one link that matters — a respondent registers at Kadamba *because* it is scarce, not in spite of it. Demand concentrates instead of redistributing. The institution's actual response (building Bakul) added capacity from outside the loop rather than closing it.

**R2 — the original "energy crash" cycle (candidate, reinforcing — not yet confirmed beyond its first link).** The project's own starting brief frames breakfast-skipping as feeding a same-day energy crash that drives compensatory canteen spending and, eventually, more late nights — a second reinforcing loop layered on top of R1.

![R2 — Candidate Skip/Crash/Compensate Loop](assets/diagram7-cld-candidate-skip-crash.png)

Only the first link (late nights drive skipping) is directly confirmed, repeatedly, across real respondents. Nothing in the six real interviews to date confirms or denies the energy-crash, compensatory-purchase, or sluggishness links — no interview question has asked what a respondent does *after* skipping. This loop is kept in the map because it is the paradox's own original framing and a plausible mechanism, not because it is evidenced; see Outstanding Data Collection.

# Key Findings

1. The system's process flow and its governance structure are only loosely coupled: the Mess Office controls billing and ordering, but the actor with the single most relevant lever over the core problem — Academic administration, over class timing — sits entirely outside that structure.
2. Every no-show exit path (cancel, Skip Meal, resale, or simply waste) is a workaround for the same missing formal mechanism: nothing in the system lets a same-day change in intent affect what gets billed or cooked.
3. The resale market's success is itself evidence of a formal gap: students built a working alternative to Skip Meal because Skip Meal does not do what a student in that situation actually needs.
4. Only one of this system's four traced loops actually closes as designed: R1 (registration/resale) is a genuinely reinforcing loop and it is the one nobody designed on purpose. Both designed balancing mechanisms (B1's Skip Meal, B2's redistribution) are structurally sound on paper but break at the exact link that would require a student to act against their own short-term interest — using a no-refund tool, or registering somewhere less convenient. A rule that depends on that kind of self-sacrifice to close its own loop should be expected not to close it.
5. Every technology component identified in this system (portal, QR credential, rating, Skip Meal, cancellation) is student-facing; none gives the Mess Office or vendors real-time visibility into anything happening at the student's decision point. The system is only instrumented on one side of the transaction it is trying to balance.
6. The service blueprint makes the same finding as #5 visible on a timeline instead of a category map: the line of visibility is crossed only twice a month, and every morning's actual go/skip decision happens in a lane the backstage side never sees until billing, which by then can no longer be changed.

# Outstanding Data Collection

The kitchen and vendor half of this map is drawn from the confirmed four-day lead-time constraint and vendor role only; the internal detail of how a preparation quantity is actually decided, and how (if at all) waste or shortfall data reaches a decision-maker, requires a mess-committee or mess-vendor interview. That interview round is pending institutional approval and **will be collected and submitted later**, consistent with the same outstanding item already logged against Tasks 3-5.

The R2 candidate loop (energy crash → compensatory purchase → sluggishness → more late nights) needs one direct, simple addition to the existing student interview guide: what a respondent actually does in the hours after skipping breakfast, and whether it changes their evening routine. This does not require a new interview round — it can be asked of the same six respondents, or added to any remaining Guide 1 interviews, whichever comes first.
