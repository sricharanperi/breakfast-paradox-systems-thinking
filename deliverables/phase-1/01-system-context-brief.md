# Phase 1 · Activity 1 — System Context Brief

**Puzzle:** The Breakfast Paradox `[Source: ProblemStatements.pdf]`
**Status:** DRAFT — v4, restructured 2026-09-05. Pending team review.
**Activity source:** *"Define the system boundary and context; identify the system's purpose and
intended outcomes; identify visible symptoms and underlying issues; identify key actors,
institutions, processes, resources and constraints."* `[Source: project_framework .pdf, Activity 1]`

**What changed in this version:** the Purpose section (§2) was previously just a description of
the registration mechanism — that's *process*, not *purpose*, and a teammate correctly caught
this. Purpose has been rewritten to actually ask what the system is *for*, per the Elements /
Interconnections / Purpose framework this course teaches (`[Source: Course — Lecture 1-3]`), and
a new §2c names the gap between that stated purpose and what the mechanism actually produces —
which turns out to be the single most important lens in this whole document. A teammate's
"Constraints, Edge Cases & Research Verticals" analysis (2026-09-05, archived in full at
`research/primary-research/team-contributions/2026-09-05_teammate-constraints-edge-cases-verticals.md`)
is integrated throughout, mainly as new §6-8, new Role E, and new questions on Roles B/C/D.
**Reconciled 2026-09-05** with prathyusha's parallel escalation-gap finding (§4, pulled from
`origin/main`) after a clean auto-merge — one stale section cross-reference was fixed, nothing was
dropped. Note: prathyusha has also independently built `prathyusha_02` through `05` (Stakeholder
Map, Power-Interest Map, Process Trace, System Timeline) and her own `prathyusha_interview-guide-
phase1-halfday.md` ("Guide 1"/"Guide 2") in parallel with this file's §11 (Roles A-E) — these two
interview guides currently overlap rather than being unified; see the chat for a comparison and a
question about how to reconcile them.

**Tagging note:** this version formalizes a fifth tag alongside the original four
(`ProblemStatements.pdf` / `Course` / `Interview·Observation·Survey` / `NEEDS DATA`):
`[Hypothesis — <whose reasoning>, <date>, not yet tested]` — for team or AI reasoning that goes
beyond confirmed facts but isn't a data gap either. It must never be read as a confirmed claim;
it's there to be tested, per §11's questions.

---

## Stated assumptions (scope decisions, not fact claims)

1. **Real site = the team's own IIIT Hyderabad mess system.** Per the approved project plan, the
   `ProblemStatements.pdf` narrative (Rohan, Adit, Kadamba mess, 7:30-9:30 hours) is treated as the
   course's *prompt scenario*, not verified fact — this brief is grounded in the real IIIT-H system
   instead, using the prompt only for framing/motivation.
2. **Scoped to Breakfast specifically**, not Lunch or Dinner, even though the same mess
   infrastructure (registration, QR, billing, cancellation) runs all three meals — because
   Breakfast is what the assigned puzzle is about.
3. **Confidence caveat:** most confirmed facts below still trace to a single respondent plus that
   respondent's own portal screenshots — real, not invented, but not yet cross-checked against a
   second person. Treat §4 "symptoms" as *confirmed to happen*, not yet as *confirmed typical*.
4. **§6-8 below are explicitly hypotheses**, not additions to the confirmed-fact record — see the
   tagging note above. They exist to sharpen the interview questions in §11, not to be cited as
   findings until tested.

---

## 1. System boundary

**In scope:** the IIIT-H dining/mess registration-and-billing system for Breakfast, across all
four messes — Kadamba, Palash, Bakul, and Yuktāhār (incl. its Jain-food variant) — and its
interaction with the academic class schedule. `[Source: Interview — student self-account,
2026-09-03; Screenshots analysis, 2026-09-03]`

**In scope as environmental/competing factors:** the on-campus alternatives a student can choose
instead of mess breakfast — Vindhya canteen (Mon-Sat, open from 10 AM, closes 6 or 8 PM — exact
closing time still `[NEEDS DATA]`; serves food, coffee, Horlicks), juice canteens, and delivery
apps (Swiggy/Zomato/Blinkit, gate-restricted, rider pickup required).
`[Source: Interview, 2026-09-03; 2026-09-09/10]`

**Out of scope for this document:** Lunch and Dinner registration behavior specifically (assumption
#2 above); off-campus dining entirely; the other three "Pick Your Puzzle" problems.

## 2. Purpose of the system

### 2a. What the system is actually for (the purpose, not the mechanism)

Stripped of implementation, a campus mess system exists to reliably **nourish resident students**
— adequate, good-quality, timely food; accommodating real dietary needs (veg/non-veg/Jain); at a
predictable, affordable cost — in a way that supports health, energy, and academic performance,
and ideally contributes to hostel community and a positive daily experience, not just caloric
intake. `[Hypothesis — team/AI reasoning per project_framework Activity 1's own instruction to
"identify the system's purpose," 2026-09-05, not yet confirmed by any stakeholder — a good Role D
question, added in §11, is whether an official stated purpose/mission for the mess system exists
at all]`

### 2b. The current operating mechanism (this is process, not purpose — kept for reference)

Students pre-register per meal per mess through the official IIIT-H app/portal
(`dining.iiit.ac.in`), are billed monthly **by registration count, not attendance**, access their
meal via a personal QR code scanned at the mess, and receive a veg/non-veg plate matched to their
registration type. `[Source: Interview, 2026-09-03; Screenshots analysis, 2026-09-03]` This is
one possible way to pursue 2a's purpose — it is not itself the purpose, and per 2c below, it may
not even be pursuing 2a very well.

### 2c. The purpose-vs-structure gap — the central systems-thinking observation of this document

This course's own teaching is direct on this point: *"the purpose of a system isn't always the
stated goal of its parts"* `[Source: Course — Lecture 1-3, traffic-jam example]`, and Donella
Meadows makes the same argument — a system's real purpose is revealed by what it *does*, not by
what its designers *say* it's for.

Three already-confirmed facts, read together, suggest the mechanism (2b) may be structurally
optimizing for something other than 2a:
1. Billing is by **registration**, not **attendance** `[Source: Interview, 2026-09-03]`.
2. Walk-in (unregistered) eating costs far more than pre-registering `[Source: Screenshots
   analysis, 2026-09-10]`.
3. The Skip Meal toggle returns **nothing** to the student — no refund or credit, only reduced
   kitchen waste `[Source: Screenshots analysis, 2026-09-03]`.

Together, these three facts reward **pre-committing** and do nothing to reward **actually
attending** or to cushion **flexibility**. `[Hypothesis — team reasoning, 2026-09-03 meeting,
formalized 2026-09-05]`: the mechanism's revealed purpose looks less like "make sure this
specific student eats well this morning" and more like "guarantee predictable registration
counts and vendor revenue" — a fundamentally different, narrower goal than 2a's. If this holds,
the "paradox" isn't that students behave irrationally — it's that they're responding rationally
to a structure whose incentives quietly drifted away from the system's own stated purpose. This
reframing is carried through §6 below and should directly shape Phase 2's Systemic Problem
Analysis and Phase 3's leverage-point search: a fix that improves the *mechanism* without closing
this gap (e.g. reminder notifications) will likely under-perform a fix that closes the gap itself
(e.g. making Skip Meal or cancellation actually valuable to the student, not just to the kitchen).

## 3. Context — the real, confirmed facts

- **Mess hours:** Breakfast 7:30-9:30 AM, Lunch 12:30-2:30 PM, Dinner 7:30-9:30 PM.
  `[Source: Interview, 2026-09-03]`
- **Class schedule:** classes start 8:30 AM, last class ends 6:40 PM, class lunch break 1-2 PM.
  Classes are **not continuous** — most students have relatively few classes on a given day; the
  respondent has an 8:30 AM class only twice a week. `[Source: Interview, 2026-09-03]`
- **Four messes, each with a distinct role:**
  - *Kadamba* — largest by capacity (1200 seats at Lunch on the one date sampled), serves non-veg.
  - *Palash* — cannot serve non-veg (kitchen/structural constraint); its cooked food is also
    shipped to Bakul.
  - *Bakul* — serves Palash's veg food plus its own non-veg; created specifically because Kadamba
    alone couldn't cover non-veg demand once it hit capacity.
  - *Yuktāhār* — a fourth mess, offers a separate Jain-food registration variant.
  `[Source: Interview, 2026-09-03; Screenshots analysis, 2026-09-03]`
- **Breakfast registered rates (2026-09-09, confirmed directly):** Yuktāhār ₹53, Yuktāhār (Jain)
  ₹53, Kadamba (Veg) ₹48, Kadamba (Non-Veg) ₹66, Bakul (Veg) ₹48, Bakul (Non-Veg) ₹66, Palāsh ₹48.
  Walk-in/unregistered rates for breakfast weren't captured in this batch, but Lunch data (Sept 10)
  showed walk-in running ~70-90% above registered price, and the same billing model applies to all
  meals, so a similar markup at breakfast is plausible but **not yet directly confirmed**.
  `[Source: Screenshots analysis, 2026-09-09]`
- **Breakfast capacity/registration (2026-09-09):** Kadamba (Veg) 551/700 registered — clearly the
  highest-uptake option; Bakul, by contrast, has notably lower uptake on both its veg (108/350)
  and non-veg (37/350) lines. `[Source: Screenshots analysis, 2026-09-09]`
- **Why Bakul's numbers are lower — respondent's own explanation, not yet independently verified:**
  Kadamba is the established, larger, well-liked "go-to" mess. Bakul is newer, physically a
  converted warehouse (cleaned, tables and a serving counter added), created specifically to add a
  second non-veg option once Kadamba alone couldn't cover demand; its veg food is cooked at Palash
  and carried over, non-veg cooked separately on-site. The respondent attributes both Bakul's
  lower admin-set capacity and lower registration uptake to this newer/secondary status — plausible,
  but capacity (set by mess administration) and registration (student choice) are mechanically
  different things being explained by one story here, so this is flagged as a hypothesis pending a
  Bakul-side or Mess Committee confirmation, not stated as settled fact.
  `[Source: Interview, 2026-09-09/10]`
- **Governance:** the Mess Committee decides mess-specific matters (menu, set ~1 month ahead, with
  student input); the Warden handles vendor management and any changes to the mess; the academic
  office has **no role** in mess timing or hostel matters. `[Source: Interview, 2026-09-03]`

## 4. Symptoms observed (real, not narrative)

- **Direct, dated instance:** the respondent's own Sept 3, 2026 breakfast registration — charged
  ₹48 at Kadamba (Veg), not availed. `[Source: Screenshots analysis, 2026-09-03]`
- **Structural evidence of a recurring pattern:** the system caps cancellations at 5 per meal-type
  per month — a rule that only makes sense if uncancelled no-shows are common enough to need
  limiting. `[Source: Interview, 2026-09-03]`
- **A "Skip Meal" toggle exists** specifically so kitchens aren't over-preparing for known
  no-shows — but it does not reduce the charge, only kitchen waste. This confirms the system's
  designers are aware of the no-show pattern at the kitchen-planning level, even though the
  billing model doesn't address it — see §2c. `[Source: Screenshots analysis, 2026-09-03]`
- **An emergent, unofficial secondary market** ("Mess Cell" WhatsApp group) where students resell
  registrations they know they won't use — a self-organized workaround for exactly this waste
  problem, not part of the official system design. See §6 for why this specific workaround, and
  not Skip Meal, likely absorbs most planned no-shows. `[Source: Interview, 2026-09-03]`
- **An unexplained quantitative anomaly:** on the one Lunch date sampled, Bakul's
  registered-to-capacity ratio (116/700) was far lower than Kadamba's (722/1200) — real numbers,
  cause unknown, and this is Lunch not Breakfast. `[Source: Screenshots analysis, 2026-09-03;
  NEEDS DATA — breakfast-specific capacity numbers, and an explanation for the Bakul gap]`
- **No confirmed negotiation or escalation mechanism** — added 2026-09-05 while building the
  Process Trace (`deliverables/phase-1/prathyusha_04-process-trace.md`). Beyond the Mess
  Committee "taking student input" on the menu, neither the one real respondent nor two
  synthetic pilot interviews could describe what actually happens after a student gives mess
  feedback — no one could point to a real example of feedback leading to a change. This is a gap
  in the system itself, not just in what's been asked so far, and it directly explains why the
  Academic Office / class-timing lever (§5's last bullet, and §2c above) has never been pursued:
  there's no visible channel for anyone to even raise it formally — a second, independent piece of
  evidence for the purpose-vs-structure gap in §2c. `[Source: Interview, 2026-09-03; Synthetic
  pilot, 2026-09-05 — flagged 🟡 pending a real Role D/governance confirmation. Renumbered
  2026-09-05: originally cited "§7" under the pre-restructure section numbering.]`

## 5. Constraints

- Billing is by registration, not attendance; only 5 cancellations/meal-type/month are allowed.
- Walk-in eating costs substantially more than registering in advance (structural disincentive to
  simply not register when uncertain).
- Veg/non-veg plates are hard-segregated by registration type at the point of service.
- Palash's kitchen cannot produce non-veg at all (physical/structural, not policy).
- Governance authority sits with the Mess Committee and Warden; the academic office/timetable side
  has no formal lever over mess timing, so any fix touching "when mess runs vs. when class starts"
  would need to cross that organizational boundary.
`[Source: Interview, 2026-09-03; Screenshots analysis, 2026-09-03]`

## 6. Incentive structure — Skip Meal vs. Mess Cell (a dominant-strategy hypothesis)

*Contributed by a teammate, 2026-09-03 team discussion; full original preserved at
`research/primary-research/team-contributions/2026-09-05_teammate-constraints-edge-cases-verticals.md`.*
`[Hypothesis — team reasoning, not yet tested]`

The Skip Meal toggle gives the student **nothing back** — no refund, no credit, only reduced
kitchen waste (confirmed fact, §4). Reselling the same slot on Mess Cell can recover **some or
all** of the money instead. For a student who already knows in advance they won't eat, Skip Meal
is therefore a **strictly dominated choice** next to resale — a rational actor picks resale every
time they have advance notice, which reframes "low Skip Meal usage" from an awareness/UX problem
into an **incentive-design problem**: the toggle asks the student to absorb 100% of the cost of
solving the kitchen's waste problem, while the peer workaround lets them absorb far less. This is
the sharpest concrete instance of the §2c purpose-vs-structure gap found so far.

**Testable predictions, not yet confirmed:**
- Students who know *in advance* they won't attend should overwhelmingly prefer Mess Cell over
  Skip Meal, if they know Mess Cell exists.
- Students who decide *last-minute* (overslept, ran out of time) have no time to use either — this
  is the group where food is actually cooked and wasted with no offsetting benefit to anyone.
- So the true "wasted, unprofited food" case should correspond specifically to **unplanned,
  last-minute no-shows**, not planned skips (which get siphoned into Mess Cell instead) — meaning
  Skip Meal usage should be rare *precisely because* the rational alternative outcompetes it, not
  because people forget it exists.

New interview questions testing this directly are in §11 (Role B, Role C, Role D).

## 7. Behavioral lenses (applying named behavioral-science concepts to what's already known)

Per the user's request, this section reasons through behavioral dimensions the document hadn't
named yet — no new data was collected for it; every point below is a lens applied to facts or
hypotheses already stated elsewhere in this document, tagged as reasoning to be tested, not fact.
`[Hypothesis — systems/behavioral reasoning, 2026-09-05, not yet tested]`

- **Loss aversion (Kahneman & Tversky):** §6's "dominant strategy" argument holds even for a
  purely rational actor, but loss aversion predicts the preference for Mess Cell over Skip Meal
  should be even *stronger* than pure expected-value reasoning implies — a guaranteed ₹0 return
  (Skip Meal) is coded as a certain loss, and humans are disproportionately motivated to avoid a
  certain loss versus a merely probable one (Mess Cell resale, which isn't guaranteed to sell).
  Worth asking directly whether students frame it this way.
- **Present bias / hyperbolic discounting:** the original puzzle text itself already describes
  this exactly — *"choosing twenty extra minutes of sleep gives him immediate relief, while the
  benefit of eating breakfast feels far away"* `[Source: ProblemStatements.pdf]`. This is a
  textbook present-bias pattern (immediate reward weighted far above a delayed one), independent
  of any mess-specific mechanism — worth testing whether it's the dominant driver for
  unplanned/last-minute skips specifically (see §6's second predicted group).
- **Sunk-cost reasoning, and why it might not fire here:** classic sunk-cost logic would predict
  "I already paid, so I should go" (this is literally Adit's stated reasoning in
  `[Source: ProblemStatements.pdf]`) — yet the existence of habitual skippers who still register
  suggests this reasoning doesn't reliably fire for everyone. One candidate explanation: because
  billing is monthly and somewhat abstracted from the moment of decision (no felt, real-time
  transaction at the point of skipping), the "I already paid" feeling may be numbed compared to a
  scenario with a real-time visible cost. Worth asking whether respondents even think about the
  charge at the moment they decide not to attend.
- **Default/status-quo effects:** the portal has a confirmed "random allocation" feature
  `[Source: Screenshots analysis, 2026-09-03]` — if some registrations happen by default/auto-
  allocation rather than active choice, registration counts could be inflated by default-effect
  behavior independent of any real intent to eat, which would also help explain elevated
  registered-but-unclaimed rates without needing a skip-*decision* at all. A new Role B question in
  §11 tests this directly.
- **Social norms / descriptive norms:** covered in more depth in §8 (Social/Peer Effects, from the
  teammate's contribution) — the general behavioral-science version of the same point is that
  people infer "what's normal" partly by observing peers, so a friend group's collective
  attendance pattern may function as a norm-setting signal independent of each individual's own
  food/sleep/schedule situation.

## 8. Research verticals — further hypotheses to test

*Contributed by a teammate, 2026-09-03 team discussion; full detail (including all edge cases) at
`research/primary-research/team-contributions/2026-09-05_teammate-constraints-edge-cases-verticals.md`.*
`[Hypothesis — team reasoning, not yet tested]`

| Vertical | Core hypothesis | Sharpest edge case |
|---|---|---|
| Production planning | Mess cooks to a historical-average number, not live registration count — meaning any above-average day runs short regardless of registrations | "Food's over" may mean one popular item ran out, not a true meal-wide shortage; and Palash/Bakul's pre-cooked supply chain is a single point of failure the on-site staff can't fix same-day |
| Temporal/rush dynamics | Arrival is bimodal — early-birds, an 8:30-rush cluster, and no-class stragglers — with different crowding experiences | A rush-hour bottleneck (serving *rate*) can look identical to a student as "food ran out" even when total quantity was adequate |
| Academic/workload calendar | Late-night deadlines push sleep to 3-5 AM, causing a missed *entire window*, likely clustering around specific weekdays | "Slept through it" (unconscious) vs. "chose sleep, awake enough to decide" (conscious trade-off) need different fixes — only one is helped by a reminder |
| Social/peer effects | Attendance clusters by friend group rather than being an independent per-student decision | Roommate/group registration mismatches may show up as coordinated multi-slot Mess Cell listings |
| Information/awareness | Low Skip Meal usage is partly awareness on top of §6's incentive problem | Whether the 5-cancellation cap causes students to stop bothering for the rest of the month once hit; whether Mess Cell is genuinely open-access or informally gatekept against newcomers |
| Economic/incentive (extends §6) | The 70-90% walk-in premium may push "register just in case" behavior, inflating registration counts before any no-show even happens | Sunk-cost numbing (see §7) may separately weaken the pull to attend once already charged |
| Physical/spatial | Distance from hostel to each mess may correlate with attendance more than food quality does | Bakul's warehouse-conversion identity/ambience may suppress uptake as a *perception* factor, separate from the capacity/novelty hypothesis in §3; weather and Kadamba-specific queue crowding are distinct deterrents |
| Governance/decision latency | Student input into the menu (§3) may only reach the "what's on the menu" decision, not the separate "how much to cook" decision | Worth asking Role D whether these are genuinely separate decision paths inside the Mess Committee |

## 9. Key actors (high-level only — full mapping is Activity 2)

Students (a range of breakfast habits, now understood to include at least an attending role, a
skipping role, and — per §8's temporal-dynamics vertical — a distinct rush/latecomer role that
attends but experiences scarcity differently; see the interview file §7 for one respondent's
detailed account), Mess Committee, Warden, per-mess vendors (Kadamba's, and Palash/Bakul's shared
vendor), mess serving/cleaning staff, Vindhya/juice canteens, delivery riders (gate-restricted),
and the informal Mess Cell WhatsApp community — which §6 suggests may function as a more
economically significant actor than its "unofficial" status implies.
`[Source: Interview, 2026-09-03; Hypothesis — team reasoning re: rush role and Mess Cell's
significance, 2026-09-05]`

## 10. Initial problem framing (a question, not an answer — per Week 1 methodology)

Given §2c and §6, this question can now be asked more precisely than the original draft: why do
students routinely register for breakfast and then not attend, and — separating the mechanism
from the behavior — does the current structure (registration-based billing, no-value-return Skip
Meal, high walk-in cost) actively reward this pattern rather than merely fail to prevent it? Is
the resulting no-show/waste split mainly *planned* skips absorbed by Mess Cell, or *unplanned*
last-minute misses that the mechanism does nothing for either way? `[Framing informed by:
Interview, 2026-09-03; §2c/§6 above; course concept — Iceberg Model, Source: Course — Lecture
4/"The Donella Meadows Project"]`

---

## 11. Research Instruments — who to talk to next, and exactly what to ask

**v4 — updated 2026-09-05,** adding a teammate's new questions (§6/§8 above) and a new Role E, on
top of the v3 bias-corrected base (all six methodology sources in `research/methodology/`).

**Standing rules from the methodology (unchanged from v3):** these are Constantine's **user
roles** (a relationship to the system — Context/Characteristics/Criteria), not fictional personas;
one person can hold multiple roles at once. **Fact before reason**, always. Every question checked
against 4 bias types (leading / shallow / personal / unconscious) and tied to a stated objective.
New questions below were held to the same standard — one (Role D's refund question) was softened
from presupposing "a refund was considered" to asking the fact first.

**How to run these:** semi-structured; curious-command probes ("tell me a little more about
that"), not interpretive ones; identical neutral acknowledgment regardless of sentiment;
decoupled encouragement; note exact words; allow silence; keep your own talk-time under ~20%;
brief intro → easy fact question → narrative questions → closing open question; write answers
close to verbatim. These interviews support *mechanism* claims ("here's how/why"), not
*prevalence* claims ("most students...") — that needs a survey.

**Priority order:** Role A and B first, Role C next (checks both the Bakul hypothesis in §3 *and*
the production-planning/§6 hypotheses), Role D if accessible, Role E as a useful addition once A-C
are underway (it isolates rush-crowding from skip/no-show, per §8).

### Role A — Breakfast-attending role (currently registers and regularly eats)
*Context:* the relationship of someone whose registrations and actual attendance mostly line up.
1. On a typical week, roughly how many mornings do you eat breakfast at the mess? *(fact, warm-up)*
2. Walk me through what happens between waking up and sitting down to eat, on a morning you go.
3. Do you usually go alone or with others? *(fact)* — if with others: what's that like?
4. Has there ever been a morning you were registered but didn't go? *(fact)* — if yes: tell me
   about one of those mornings, what happened?
5. Walk me through a morning when you have an early class, from waking up onward.
6. Is there anything about breakfast at the mess — good or bad — we haven't touched on?

### Role B — Breakfast-skipping role (frequently registers-but-doesn't-attend, or doesn't register)
*Context:* the relationship of someone who often doesn't eat mess breakfast, whatever the reason.
1. On a typical week, roughly how many mornings do you *not* eat breakfast at the mess? *(fact)*
2. Think of the last morning you didn't eat breakfast — walk me through what happened from when
   you woke up. Was there anything due the night before — an assignment, a deadline? *(fact,
   tests §8's academic-calendar vertical)*
3. Were you registered for breakfast that day? *(fact)* — if yes: what happened between
   registering and not going?
4. Did you end up eating or getting food later that morning, or before lunch? *(fact)* — if yes:
   tell me about that, where did it come from?
5. Have you ever used the Mess Cell WhatsApp group to buy or sell a meal registration? *(fact)* —
   if yes: walk me through the last time.
6. When you know *in advance* you won't eat a meal you're registered for, what do you usually do —
   nothing, the Skip Meal toggle, sell it, something else? *(fact — directly tests §6)*
7. Have you ever used Skip Meal instead of trying to sell it? *(fact)* — if yes: what made you
   choose that?
8. Was that registration something you actively chose, or does it ever happen automatically —
   like a random allocation? *(fact — tests §7's default-effect hypothesis)*
9. Thinking back over the last month, has how often you eat breakfast changed at all? What comes
   to mind?
10. Is there anything about your mornings, or the mess, we haven't touched on?

*Optional, sparing use only — explicitly hypothetical, label it as such when writing up the
answer:* "If Skip Meal actually gave you money back, would that change what you do?"

### Role C — Mess operations role (vendor or serving staff, ideally one from Kadamba, one from Bakul)
*Context:* the relationship of someone preparing/serving food, experiencing registration from the
supply side — the only source that can independently check §3's Bakul hypothesis and §8's
production-planning vertical.
1. Walk me through a typical breakfast service, from when you start preparing to when you close.
2. What number do you actually cook to — registrations, yesterday's turnout, something else?
   *(fact — the single most load-bearing unconfirmed hypothesis in this whole document, per the
   teammate's own flag)*
3. On a typical day, roughly how many plates go unclaimed out of what's registered? *(approximate
   is fine)*
4. What happens to food that isn't claimed?
5. When someone marks "Skip Meal" in the app, what if anything changes about what you prepare, and
   how far ahead do you actually see it?
6. Do you know whether a plate was marked "skipped" by the toggle, versus just never claimed with
   no toggle used? *(fact)* — does that distinction matter to you either way?
7. *(Bakul staff only)* How would you describe how busy Bakul gets compared to Kadamba, on a
   typical morning?
8. If you could change one thing about how registration works, from where you sit, what would it be?

### Role D — Mess governance role (Mess Committee member or Warden)
*Context:* the relationship of someone with decision authority over hours, rules, and vendors.
1. Is there a stated purpose or mission for the mess system that you know of? *(fact — tests §2a)*
2. Walk me through how breakfast hours came to be what they currently are.
3. Has changing them ever come up in discussion? *(fact)* — if yes: what was that like?
4. What's the thinking behind the 5-cancellations-per-month limit specifically?
5. Has a refund or credit tied to Skip Meal ever been discussed? *(fact)* — if yes: what was the
   reasoning for or against it?
6. Has the overlap between breakfast hours and early class times ever come up as something to
   address? *(fact)* — if yes: tell me about that.
7. In your own account, why was Bakul set up the way it was?
8. Do you track how often registered meals go unclaimed? *(fact)* — if yes: would you be willing
   to share what that looks like?
9. Is there anything about how the mess system works that outsiders usually get wrong?

### Role E — Rush/latecomer role (attends regularly, but typically arrives late in the window)
*Context:* the relationship of someone who eats breakfast most days but consistently arrives in
roughly the last 20-30 minutes of the 7:30-9:30 window — isolates §8's rush/crowding hypothesis
from the skip/no-show question Roles A/B are built around.
1. On a typical week, roughly how many mornings do you eat breakfast, and around what time do you
   usually get there? *(fact, warm-up)*
2. Walk me through your most recent breakfast at the mess, from arriving to sitting down.
3. Has there ever been a morning where a specific food item, or the food generally, wasn't
   available when you got there? *(fact)* — if yes: tell me about that morning.
4. What usually determines what time you end up getting to the mess?
5. On mornings you arrive later versus earlier in the window, what's different about the
   experience?
6. Is there anything about arriving when you do — the queue, the food, anything else — we haven't
   touched on?

---

## Still Missing — needed before this brief can be considered validated

- [ ] Role A/B/C/D/E interviews above — the main open item now
- [ ] **Highest priority (Role C Q2):** what quantity the kitchen actually cooks to — the single
      most load-bearing hypothesis in §6/§8
- [ ] Independent confirmation (or correction) of the Bakul hypothesis in §3, from Role C or D
- [ ] Whether an official stated purpose/mission for the mess system exists (§2a, Role D Q1)
- [ ] Vindhya canteen's exact closing time (6 PM or 8 PM — respondent gave both)
- [ ] What the calendar's "S" meal slot is, and whether/how the third-party auth-key API gets used
      (both from `screenshots/analysis.md`, not yet asked about directly)
- [ ] Any rough day-of-week / deadline-calendar correlation with skip behavior (§8)
- [ ] Whether Mess Cell is genuinely open-access or informally gatekept (§8)
- [ ] Confirmation this document's scope (Breakfast-only, real-IIIT-H-grounded) is what the team
      wants before Activity 2 builds on it
