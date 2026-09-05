# Prathyusha's Braindump — Mess/Breakfast System

Raw braindump captured 2026-09-05, before it gets structured into the formal
15-deliverable framework (`.claude/skills/systems-design-toolkit/SKILL.md`). Purpose of
this file: dump everything in my head about how to approach this project — not
polished, not yet fact-checked against `research/` — so nothing gets lost, and so we
(me + Claude) can brainstorm on top of it in later sessions.

**How to read this doc:** each section is a raw idea cluster from the braindump,
followed by a short note on where it plugs into the existing project (which deliverable,
which research file it should feed, what's already done vs. still open). The mapping
notes are the only "processed" part — the ideas themselves are kept close to how I said
them.

---

## 1. Steps to do the project (my mental model of the workflow)

Roughly the order I'm thinking in:

1. Go through the context — read what's already there, ask questions, observe.
2. Map the stakeholders — there will be **multiple maps**, not just one (different
   lenses: who's affected, who has power, who's adjacent-but-not-obvious).
3. Map journeys — walk through what a student/cook/staff member actually experiences,
   step by step.
4. Identify **functions** — what is each part of the system actually *for*, not just who's
   in it.
5. Map the physical space and the process (components, timing).
6. Layer in constraints and factors (business, social, physical).
7. Build the system diagram(s) — pain points marked directly on it.
8. Go deeper: iceberg model, causal loops.
9. Only then — design the solution. Solution can be *anything*: a game, an app, a
   framework, a policy, a blueprint, etc. Don't lock into "app" too early.
10. Also think about system *characteristics* throughout (not a separate step — a lens
    to keep applying: is it centralized/decentralized, tightly/loosely coupled, what
    are its feedback delays, etc.)

**Mapping to the course framework:** this is basically the same order as the 10-activity
framework already in `.claude/skills/systems-design-toolkit/SKILL.md` (Context Brief →
Stakeholder Map → Power-Interest → Process Trace → Timeline → Rich Picture → CLD →
Iceberg → Reframe → Design Opportunity → Leverage Points → Principles → Prototypes →
Scenario → Final Recommendation). Good — my instinct matches the structure. The one
thing I'm adding here that isn't explicit in the framework doc is the **30-min interval
physical observation protocol** (see §5) and the **explicit "solution can be anything"**
framing for deliverable #13 (Intervention Concepts).

---

## 2. Stakeholders

### 2a. Core list (mine, from the braindump)

- Students
- Mess (as an institution/operator)
- Admin — specifically for controlling *number of students* (registration caps,
  capacity allocation)
- Hostel
- Academics — can change things like first-class time (a lever outside the mess's own
  control)
- Friends
- Roommates

**Cross-check against what's already logged:** `deliverables/phase-1/01-system-context-brief.md`
§6 already lists: Students, Mess Committee, Warden, per-mess vendors, mess
serving/cleaning staff, Vindhya/juice canteens, delivery riders, the informal Mess Cell
WhatsApp community. My list above adds **Friends** and **Roommates** explicitly as social
stakeholders (peer influence on whether someone goes to breakfast) and **Academics** as
an institutional lever (class start time), which the existing brief already flags as
*out of the Mess Committee/Warden's authority* (§5 Constraints — "academic office has no
role in mess timing"). That's a real tension worth keeping: Academics is a stakeholder
who could pull a lever (shift 8:30 AM start) but has no incentive or mandate to.

### 2b. Onion diagram — multiple maps needed

Not one stakeholder map — **several**, layered like an onion, e.g.:
- Core/direct (student, mess staff, cook)
- Operational/institutional (Mess Committee, Warden, admin)
- Peripheral/social (friends, roommates, Mess Cell WhatsApp group)
- Environmental/adjacent (competing food options, other systems below)

**Maps to deliverable #2 (Stakeholder Map)** — but per the toolkit, that's normally one
Mermaid graph clustered by tier. My instinct to do *multiple* maps (one per lens:
power/interest onion, social-influence onion, physical-space onion) is a legitimate
extension — worth deciding whether to fold into #2/#3 or treat as a supplementary
artifact.

---

## 3. Adjacent / parallel systems to think about

Systems that touch or resemble the mess system, worth scanning for patterns or
borrowed structure:

- Agriculture (where the food itself originates — supply chain upstream of the mess)
- Transportation (getting food/ingredients in; also students getting to the mess in time)
- Market / marketplace dynamics (pricing, walk-in vs. registered — and see §8, market
  manipulation)
- Food safety
- Catering / chefs (the actual production side)
- Cleaning
- Healthcare — specifically **allergies** (a stakeholder concern not yet in any existing
  doc)
- Drainage
- Waste management (directly tied to the no-show/wasted-food problem already central to
  the Breakfast Paradox puzzle)
- Vendor (procurement/supply relationships — Palash/Bakul's shared vendor is already
  noted in the context brief)

**Not yet in `research/`** — allergies/healthcare and drainage are genuinely new angles.
Waste management and vendor are already implicit in the existing brief but not spelled
out as their own system lens. Worth deciding: are these full parallel systems to study,
or just factors to fold into the Constraints layer (§6)? My instinct: treat as
**context/background systems** that inform constraints, not full separate stakeholder
maps — otherwise scope explodes past a 4-week project.

---

## 4. Relationships

Need to map relationships between stakeholders/components, not just list them —
who depends on whom, who has power over whom, who's affected without having a say.
This is basically deliverable #3 (Power-Interest/Leverage Map) plus the *edges* of
deliverable #2's graph. Also connects to §2b (multiple onion layers) — relationships
*between* layers (e.g., Academics ↔ Mess Committee has essentially no relationship/edge
at all, which is itself the interesting finding).

---

## 5. Research methodology

### 5a. General approach
Go through context, ask questions, observe, map the journey, identify functions.
Already mirrors what's logged in `research/methodology/index.md` and the Role A/B/C/D
questionnaires in the context brief §8 — good, consistent with what's already built.

### 5b. NEW — Mess condition mapping protocol (30-min intervals)

Map the mess condition every 30 minutes across the full breakfast window, 7:30–9:30 AM:

- 7:30–8:00: counter situation, how many students, what's consumed more/less
- 8:00–8:30: same
- 8:30–9:00: same
- 9:00–9:30: same

For each interval, track: counter/queue situation, headcount, what's consumed
more vs. less (which items run out, which are left over).

**This is exactly the open item already flagged in
`research/primary-research/index.md`:** *"Direct observation of 2-3 real mess-hours
mornings (headcount over time, discarded food)"* — currently unchecked. My braindump
here gives it a concrete protocol (30-min buckets, specific variables to track per
bucket). This should become the actual observation instrument — feeds directly into
deliverable #5 (System Timeline / Behaviour-Over-Time Map), which needs exactly this
kind of time-series data and currently has none.

### 5c. Spatial / component mapping

Map the physical components within a mess:
- Kitchen
- Cleaning (area/process)
- Wipe/dry (station)
- Dining (seating area)
- Service counter

Map the actual space layout, not just the process flow. This feeds deliverable #4
(Process Trace) and #6 (Rich Picture / System Map) — a Rich Picture in particular wants
the physical layout, not just an abstract flowchart. Also directly relevant to the
Bakul question already open in the context brief (Bakul = converted warehouse, food
partly cooked at Palash and shipped in) — a spatial map would make that structural
difference visible.

---

## 6. Constraints and factors

### 6a. Business factors
- LPG/gas price increases → fewer items served (direct cost-driven menu shrinkage).
  Concrete, causal, quantifiable if we can get price/menu data over time — strong
  candidate for a causal loop link (cost ↑ → variety ↓ → attendance/satisfaction ↓).

### 6b. Social/operational factors
- Dish-washing area getting clogged (bottleneck, affects turnaround/seating availability)
- Crowd at the counter (queue dynamics, ties into §5b's 30-min mapping)
- Mood of the cook (a genuinely soft, human factor — hard to quantify but real; affects
  food quality/pace, worth at least noting even if not measurable)
- General pain points to be identified via observation + interviews

**These are new, concrete constraint examples** beyond what's in
`deliverables/phase-1/01-system-context-brief.md` §5 (which currently only has
billing/cancellation/veg-nonveg-segregation/Palash's-kitchen/governance constraints —
all administrative/structural). The LPG-price and cook's-mood examples add the
**business** and **human/social** constraint categories that aren't represented yet.
Should be verified with Role C (mess operations) interview questions already drafted in
the context brief §8 — e.g. add a direct question about ingredient/gas cost pressure on
menu decisions.

---

## 7. Frameworks to apply (confirms existing plan, doesn't change it)

- **System diagram(s)** — plural, multiple journey maps too, pain points marked
  directly on the diagram rather than as a separate list.
- **Iceberg model** — Events → Patterns → Structures → Mental Models (deliverable #8,
  already scaffolded in the toolkit).
- **Causal loop diagrams** — reinforcing/balancing loops (deliverable #7).
- **System characteristics** — keep asking, throughout: what kind of system is this
  (centralized/decentralized, feedback delays, buffers, etc.)? Not a separate
  deliverable, more a lens to keep re-applying at every stage.

---

## 8. Market manipulation angle

Also want to map how systems like marketplaces can be *manipulated* — e.g. the
informal Mess Cell WhatsApp resale market already documented in the context brief
(students reselling registrations they won't use) is itself a small emergent market
with its own dynamics (scarcity, informal pricing, trust). Worth treating as a case
study in miniature: what rules/incentives created it, and could it be manipulated
(gamed) the way real marketplaces are — hoarding registrations to resell, artificial
scarcity, etc.? This is a genuinely new analytical angle not yet in any existing
deliverable — could feed into deliverable #6 (Rich Picture, as a "shadow system") or
get its own callout in deliverable #8 (Iceberg — this market is a *Structure* that
emerged in response to the billing-by-registration rule).

---

## 9. Solution space — stays open

Explicitly: the solution can be a **game, app, framework, policy, blueprint**, or
anything else. Don't converge early. This matches deliverable #13's framing
("Intervention Concepts / Prototypes") — the toolkit doesn't prescribe a medium either.
Decision on format should come *after* the leverage-point analysis (#11), not before —
i.e., resist picking "let's build an app" until we know which leverage point we're
actually targeting (Meadows' 12 points, already in the toolkit reference section).

---

## Open items / where to go next

Things this braindump raises that aren't yet resolved anywhere in the project:

- [ ] Turn §5b into an actual scheduled observation session (2-3 real mornings,
      7:30-9:30, 30-min buckets) — this is the single highest-value next action since
      it's already the top unchecked item in `research/primary-research/index.md`.
- [ ] Add gas/ingredient-cost and cook's-mood/staff-experience questions to the Role C
      (mess operations) interview in the context brief §8.
- [ ] Decide: do the "adjacent systems" in §3 get their own analysis, or fold into
      constraints only? (My lean: fold in, keep scope tight.)
- [ ] Decide: multiple stakeholder maps (§2b) as one deliverable #2 with layered
      clustering, or as separate supplementary artifacts?
- [ ] Spatial/component map of at least one mess (kitchen/counter/dining/cleaning) —
      no floor-plan-level artifact exists yet.
- [ ] Mess Cell WhatsApp resale market (§8) as its own mini case study — worth a
      dedicated few paragraphs somewhere, probably in the Iceberg/Structures layer.

---

*This file is a scratchpad, not a deliverable — treat everything above as raw material
to be verified against real data (interviews, observation, screenshots) before it goes
into any of the numbered deliverables under `deliverables/`.*
