# Gap Audit, pass 2: 01 System Context Brief (Activity 1)

**Audited file:** `deliverables/phase-1/01-system-context-brief.md` (174 lines, as revised in pass 1 today; zero em dashes)
**Audit date:** 2026-09-27 (second pass)
**Evidence read, in order:** Brief #2 `research/primary-research/2026-09-27_team-field-account-evidence-brief.md` ("B2", authoritative where it conflicts), the verbatim account `research/primary-research/interviews/2026-09-27_team-field-account-kadamba-yuktahaar.md` ("TA"), Brief #1 `research/primary-research/2026-09-26_mess-operations-evidence-brief.md` ("B1", still authoritative for records), `MASTER_CONTEXT.md` §7 (D-24, D-35, D-45, D-48 to D-54) and the pass-1 audit `deliverables/phase-1/revisions/2026-09-27_01-gap-audit.md`, plus the diagram sources `deliverables/phase-1/assets/diagram1-system-boundary.mmd` and `diagram2-context-map.mmd`.
**Status:** working document, never submitted (D-35, D-42, D-52). The deliverable was not edited.

**Confidence tags (B2 vocabulary, mapped to D-35 prose for the deliverable):**
- *confirmed (records)* / *confirmed (observed)*: write as **confirmed**.
- *single-sourced (operator, observer-verified)*: write as **single-sourced**; the number is no longer *(unclear)*, but it remains the operator's own claim. The deliverable may say "stated by the operator and heard directly by the team" once, in the Context section, rather than on every line.
- *team observer judgement*: the team's own assessment; write as **candidate** (it is an inference, not an operator statement or a record).
- *candidate*, *assumed*: unchanged.

**Framework wording (D-7), unchanged:** the four top-level headers already match Activity 1 ("Define the system boundary and context; Identify the system's purpose and intended outcomes; Identify visible symptoms and underlying issues; Identify key actors, institutions, processes, resources and constraints") and the deliverable line "system boundary, purpose, context, symptoms, constraints and initial problem framing". Keep them. All gaps below fit inside existing headers; no new top-level section is needed.

Priority key: **P0** = contradicts a B2 correction (or states one side of a B2-flagged conflict as settled fact, or is otherwise materially wrong in submission prose); **P1** = a missing element the framework asks for that B2 can now supply, or a confidence upgrade on a headline claim; **P2** = enrichment or precision.

---

## 0. Headline findings

1. **Four statements contradict B2's correction table (P0):** the Kadamba staff-meal figure "20 to 30" (twice), the Yuktāhār "five-person project management team", and Prism described as a floor team that "calls itself the Prism team". B2 §3 replaces all three.
2. **One B2-flagged conflict is stated as settled fact (P0):** the Processes list says Skip Meal "notifies the kitchen for production planning", while B2 §1.2 reports Kadamba cooks on registrations only. B2 asks for this to be flagged, not resolved.
3. **The context diagram is stale and contradicts the text (P0):** `diagram2-context-map` (5 Sept) still labels the Mess Office as "ordering"/"orders", which pass 1 revised away (D-50). Neither diagram shows operators, suppliers, or the extra diners.
4. **The governance picture lacks the only command chain anyone has actually described end to end.** B2 gives CFS → CDS (head Raju) → Prism → operations manager → manager → supervisor → service staff. The brief still uses only Mess Committee / Mess Office / Warden and never mentions CFS. The Raju vs Giri conflict must be shown as open (D-24).
5. **"Standing booking" can now be sharpened to "a default, not a choice".** B2 §1.7 (confirmed: poster on record + student experience) says students are registered automatically and mandatorily, including off campus and on holidays; the only exit is 5 cancellations per meal type per month made at least 4 days ahead, and the charge cannot be nullified. This upgrades the "random allocation" symptom from candidate and strengthens the Purpose-vs-Mechanism gap.
6. **Two new symptoms are missing:** reheating and repeated transfer degrading Kadamba food quality (team judgement, candidate) and back-door late arrivals after 9:30 that the mess cannot refuse (single-sourced).
7. **Two new constraints are missing:** Kadamba's three procurement tiers and the pre-service food-safety sequence, which together fix when the first batch must exist.
8. **The waste picture needs one stated tension, not a resolution:** Kadamba's operator says about 5 to 10 percent daily wastage (base unstated), against a 70 percent first batch and 37 percent recorded turnout. The kg figures from B1 are withdrawn (the brief does not use them; keep it that way).

---

## 1. Gap register

### Section: System Boundary (lines 8 to 22)

**G2-01 (P1, add). Name the vendors and the extra diners on the boundary.**
- Wrong/missing: line 13 says "the outside catering firms that run each hall" without names; line 16's boundary actors omit the people outside the student registration who eat from the same food.
- Evidence: Prism is Kadamba's outsourced vendor, wins the contract by tender bid, registers as a vendor and runs all operations at Kadamba (single-sourced, operator, observer-verified; B2 §1.1, TA "Prism is basically the vendor for Kadamba mess ... They bid for the money and they come here as a third party"). ABC Hospitality Services runs Yuktāhār (confirmed in B1; restated in TA). At Kadamba about 30 extra portions are cooked for roughly 30 to 50 outside people such as night-shift security, and about 50 percent of Kadamba's internal staff also eat at the mess (single-sourced, observer-verified; B2 §1.3).
- Proposed change: in the kitchen-layer bullet, name "Prism at Kadamba and ABC Hospitality Services at Yuktāhār" (Vijayalakshmi stays candidate for Bakul/Palash). In line 16 add "non-student diners fed from the same kitchen: at Kadamba, 30 to 50 outside people such as night-shift security, and about half of the operator's own staff" as a material flow crossing the boundary. Add the institution's facility team (tasting) and the weekly QC inspection as boundary actors on the quality side.

**G2-02 (P1, revise). Diagram 1 is still the 5 September Mermaid version.**
- Wrong/missing: `assets/diagram1-system-boundary.png` shows only the platform and four halls; it has no kitchen layer, no operators, no suppliers, no garbage contractor, no extra diners. Pass-1 G-01 asked for a three-ring redraw; it was not done. It is also Mermaid, against D-20.
- Evidence: B1 §2, B2 §1.1, §1.3, §1.6, §2.2.
- Proposed change: redraw with `systems-visual-design` (D-20): inside ring (platform and scan; four halls; Prism kitchen at Kadamba; ABC Hospitality kitchen at Yuktāhār; off-site kitchen plus transport for Bakul/Palash), boundary ring (suppliers in three tiers, garbage contractor, facility team/QC, CDS site team, tender, extra diners), outside (class schedule, alternative venues, Mess Cell).

### Section: Context (lines 24 to 44)

**G2-03 (P0, contradicts_existing). Diagram 2 labels the Mess Office as placing orders.**
- Wrong: `diagram2-context-map` shows `Office["Mess Office ordering, platform, operations"]` and "orders, administers platform". Pass 1 revised the text (line 132) to say quantities are set by the operator the day before, and D-50 retired the "T-4 procurement lock". The submitted PDF still embeds the old claim as an image.
- Evidence: B1 §2 (operators plan T-1); B2 §1.2 (Kadamba supervisor tells the kitchen how much to cook), §2.3 (Yuktāhār planning meeting and issue list).
- Proposed change: redraw diagram 2 (D-20). Replace "orders" with "administers platform; operators read registration count". Add the CFS → CDS → Prism chain (with the Raju/Giri flag) and ABC Hospitality; replace the single "Mess Vendors" box with the named operators.

**G2-04 (P1, add). Add the Kadamba command chain; flag Raju vs Giri and CDS vs Mess Office (D-24).**
- Wrong/missing: line 37 describes governance only as Mess Committee / Mess Office / Warden and notes that operators say "CDS team". CFS is absent from the entire brief, although braindump #2 (2026-09-13) and B2 both describe CFS → CDS. Line 38 attributes the only operator chain ("supervisor, manager, operations manager, director") to an unnamed operator; B1 shows that was the Vijayalakshmi chain ("MD").
- Evidence: "CFS → CDS (head: Raju) → contractor Prism → operations manager → manager → supervisor → service staff" (single-sourced, operator, observer-verified; B2 §1.1; TA opening paragraph). "The supervisor constantly checks the counters and tells the kitchen how much to cook" (same). Conflict: earlier research names the CDS Chair as Giri (braindump #2, CFS Chair interview); B2 names Raju as CDS head. May be two roles or one wrong name.
- Proposed change: in the governance bullet add one sentence: "The Kadamba operator describes its line of authority as running from CFS to CDS, then to Prism and down through an operations manager, a manager and a supervisor to the service staff (single-sourced). The operator names the CDS head as Raju, while an earlier institutional interview names the CDS Chair as Giri; whether these are two roles or one is unconfirmed, as is whether CDS is the body this brief calls the Mess Office." In the operators bullet, attribute the "director" chain to the off-site operator and give Kadamba's chain separately. Do not merge any names.

**G2-05 (P1, strengthen). Name the vendors and their different operating models in the structure paragraph.**
- Wrong/missing: line 32 names Vijayalakshmi but not Prism or ABC Hospitality; Yuktāhār is "Satvik and Jain" but not stated as vegetarian only.
- Evidence: Yuktāhār is vegetarian only, with Jain service alongside regular (confirmed, observed + registers; B2 §2.1). Kadamba plans veg and non-veg separately, 70 percent each (single-sourced, observer-verified; B2 §1.2).
- Proposed change: "Kadamba ... run by Prism from its own on-site kitchen ... Yuktāhār serves vegetarian Satvik food with a Jain variant, run by ABC Hospitality Services from its own on-site kitchen."

**G2-06 (P1, revise). Registration is automatic and mandatory; the "weekly blocks" wording needs to sit beside that.**
- Wrong/missing: line 42 says registration and cancellation close four days ahead and "operators describe breakfast registration as made in weekly blocks". It never says students are registered by default. Line 126 (Processes) says "a student selects a hall and meal through the platform", which implies an active choice per meal.
- Evidence: "Registration is mandatory and automatic. Students are registered whether or not they are on campus, including over holidays, and the only way out is 5 cancellations per month (per meal type, made at least 4 days ahead)" and "we don't have any opportunity to nullify it" (confirmed: poster on record + team member's own student experience; B2 §1.7, §3). Note also that the Phase 1 student interviews (MASTER_CONTEXT §4, Task 4) reported monthly, not weekly, batch registration; with B2 this becomes weekly (operators) vs monthly (students) vs automatic default (B2), which the brief should not paper over.
- Proposed change: line 42: "Registration is automatic: every student is registered for every meal by default, on campus or not, including holidays (confirmed). The only way out is a cancellation, allowed five times per meal type per month and only at least four days before the meal; a registered meal cannot otherwise be removed from the bill." Line 126: "Registration: students are registered automatically for their hall and dietary category; the student's action is to opt out, not to opt in." Keep "weekly blocks" only as the operators' description of how counts reach them, and note the monthly/weekly discrepancy as open.

**G2-07 (P2, strengthen). Kitchen start times now have a second, direct source.**
- Line 26: "Kitchen staff start work between 5:00 and 5:30 AM (single-sourced, consistent across two operators)."
- Evidence: Kadamba chef arrives 5:30 and batch-cooks sambar and upma; live items (dosa) cooked in front of diners from 7:00 (single-sourced, observer-verified; B2 §1.6). Yuktāhār breakfast cooking starts 5:30, ready by 7:30 (B2 §2.3).
- Proposed change: add "Batch items are cooked from 5:30 and ready by about 7:30; at Kadamba live items such as dosa are made at the counter from 7:00."

### Section: Purpose / Actual Mechanism / Gap (lines 46 to 68)

**G2-08 (P1, strengthen). "Standing booking" becomes "a default, not a choice".**
- Wrong/missing: line 56 opens "Registration is a standing booking" and supports it only with the four-day close and flat weekday counts.
- Evidence: B2 §1.7 (confirmed, as G2-06); B2 §4 "the booking is a default, not a choice → confirms the 'standing booking' root cause from the student's own vantage point".
- Proposed change: "Registration is a default rather than a choice. Every student is registered automatically, and the only way out is one of five cancellations per meal type per month, made at least four days ahead (confirmed). The booking therefore records the absence of an opt-out, not a decision to eat." Carry this into the Gap paragraph (line 68): the method "advance meal planning" assumes registration expresses intent; under automatic registration it cannot.

**G2-09 (P1, add). The operators have purposes of their own, and they point in opposite directions.**
- Wrong/missing: Purpose gives only the student-facing and institutional purpose. The actual mechanism does not say what each operator is trying to achieve.
- Evidence: Kadamba "will cook everything based on the number of registrations done. It doesn't care if people don't want to eat because it is a responsibility and they are getting paid for it" (TA; single-sourced, operator stance as reported by the observer). Yuktāhār's project-management goal is explicit: best quality, less waste, optimised workflow, lower operating cost, standardisation and higher profit (single-sourced, observer-verified; B2 §2.4). B2 §4: same billing basis, opposite operator stances.
- Proposed change: add a short paragraph under Actual Mechanism: "The two operators with on-site kitchens read the same registration count with different aims. Kadamba's treats the count as its obligation, since it is paid against it; Yuktāhār's names waste reduction as a route to lower cost and higher profit (single-sourced)." Do **not** state that Kadamba is paid per registered plate: the quote is the team's paraphrase of an operator stance, not the contract (D-54 hold stands; see G2-10).

**G2-10 (P1, revise). The plate-basis unknown now has a hint, not an answer.**
- Line 38 / line 120: "Whether 'plates' means registered plates or plates actually served is not known."
- Evidence: TA "they are getting paid for it" in the sentence about cooking to registrations (single-sourced, paraphrased). Not a contract term.
- Proposed change: keep "not known" and add "Kadamba's operator speaks of being paid for what is registered (single-sourced), which points to a registered-plate basis but does not confirm it." Mark as candidate.

**G2-11 (P1, strengthen + revise). Kadamba's rule is now observer-verified and has more structure than "no forecasting method".**
- Line 61: "Kadamba cooks a first batch for about 70 percent of registrations ... Its floor manager says the kitchen has no forecasting method: 'it was wasted many times' (single-sourced)."
- Evidence: 70 percent first batch, planned separately for veg and non-veg (e.g. 400 non-veg + 300 veg); per-dish gram standards (idli 4 per person, sambar 100 g, separate standards for poha, pulao and others); "floating" items people over-take (bonda, puri, vada, idli); the supervisor watches the counters and tells the chef how many more portions to cook from registrations plus turnout so far; biryani lunch is cooked at 100 percent (all single-sourced, observer-verified; B2 §1.2).
- Proposed change: "Kadamba cooks a first batch for about 70 percent of registrations, veg and non-veg separately, portioned by a gram standard for each dish; a supervisor watches the counters and tells the kitchen how much more to cook, within 10 to 15 minutes (single-sourced). It keeps no record that carries one day's outcome into the next day's ratio." Keep the "wasted many times" quote. Optionally note biryani lunch at 100 percent as the contrast case (lunch, outside the boundary).

**G2-12 (P1, add). Yuktāhār's forecasting now has an in-service step.**
- Line 60 lists the matching-week Wastage Book and weekday register, used before service.
- Evidence: the month's turnout pattern and holidays, special weeks and campus events are also read; the first half hour of service is used as a sample to project the rest and drive top-up (single-sourced, observer-verified; B2 §2.3 steps 2 and 3). Meetings: first half of the day for next day's breakfast and lunch, second half for snacks and dinner; everyone attends, not only storekeeper and coordinator (B2 §2.3, §2.1).
- Proposed change: add to line 60: "During service the first half hour is used as a sample to project how many will come for the rest of the meal (single-sourced)." Note, as a candidate, that this sample is taken before the closing crest in which about a quarter of Kadamba's breakfast diners arrive (records); the same crest shape at Yuktāhār is not measured.

**G2-13 (P0, contradicts_existing). Staff-meal absorber figure is corrected by B2.**
- Wrong: line 64 "by the 20 to 30 cooking and security staff who eat after students at Kadamba".
- Evidence: B2 §3 correction row: "Kadamba staff meals '20–30' → 30–50 outside people (e.g. night security) + about 50% of internal staff" (single-sourced, observer-verified). About 30 extra portions are cooked for them (B2 §1.3): this is planned food, not only leftovers.
- Proposed change: "by about 30 to 50 people from outside the registration, such as night-shift security, for whom about 30 extra portions are cooked, and by about half of Kadamba's own staff, who eat from the same food (single-sourced)".

**G2-14 (P1, add). State the Kadamba waste figure as a tension.**
- Wrong/missing: the brief gives no Kadamba waste quantity (correctly; the B1 kg figures are withdrawn and must stay out). It also does not state the tension B2 §1.5 and §5 ask for.
- Evidence: "About 5 to 10 percent daily wastage" (single-sourced, observer-verified; base not stated: per meal or per day, by weight or not). 70 percent first batch vs 37.1 percent recorded turnout (records).
- Proposed change: add to line 64 or the Gap paragraph: "Kadamba's operator puts daily waste at about 5 to 10 percent, without saying of what (single-sourced). A first batch at 70 percent of registrations against 37 percent turnout could only produce that little waste if most of the difference is eaten by the extra diners, held and reheated into later service, or offset by smaller top-ups, or if the figure is measured on a different base. Which of these holds is not known." No "therefore" in either direction.

### Section: Intended Outcomes (lines 70 to 76)

**G2-15 (P1, add). Close-of-service strain includes back-door entry.**
- Line 72 mentions the door being reopened for 5 to 10 minutes.
- Evidence: "even if the front door is closing, people are coming from the back door after 9:30 and would demand to eat it", "mess can't say no to them"; last-minute registrations are "a pain" (single-sourced, observer-verified; B2 §1.7).
- Proposed change: "the Kadamba kitchen reopens the door for 5 to 10 minutes, and students who arrive after 9:30 also come in through the back door and are served, since the mess cannot refuse them (single-sourced)".

**G2-16 (P1, add). The quality outcome has a candidate failure mechanism.**
- Line 73 treats the quality-and-quantity outcome only as a quantity failure.
- Evidence: team observer judgement: Kadamba food is cooked ahead, reheated repeatedly and transferred between vessels for display and service, so it degrades fast (B2 §1.4; TA "the main problem in Kadamba is that the food is cooked before and reheated again and again"). This is the team's assessment, not the operator's, and the link to skipping is not evidenced (B2 §4, D-40).
- Proposed change: add "At Kadamba the team observed food cooked ahead and reheated and moved between vessels several times before it is eaten, which it judged to lower quality (candidate)."

### Section: Visible Symptoms and Underlying Issues (table, lines 80 to 98)

**G2-17 (P0, contradicts_existing). Skip Meal row and Process line state one side of a flagged conflict.**
- Wrong: line 129 "Skip Meal ... notifies the kitchen for production planning but does not affect billing"; line 86 "The mechanism ... serves only the kitchen's production planning". These restate the 2026-09-13 finding (MASTER_CONTEXT line 465: Skip Meal declarations do reach the kitchen) as settled.
- Evidence: "mess will automatically cook based only on the number of registrations" (single-sourced, observer-verified; B2 §1.2). B2 flags the conflict and offers a possible reconciliation (Skip Meal may adjust the count the operator sees) that needs one direct question. Line 86's own last sentence ("None of the three operators names Skip Meal among the inputs") already half-flags it.
- Proposed change: line 129: "Skip Meal: a registered student may flag in advance that they will not attend. It is designed to inform the kitchen and does not affect billing. Whether it changes what Kadamba cooks is unresolved: the institution's account says the declarations reach the kitchen, while Kadamba's operator says it cooks on registrations alone." Mirror in line 86.

**G2-18 (P1, revise). Random-allocation row can be upgraded.**
- Line 96: "Some registrations are generated by the system rather than by active student choice ... (candidate)."
- Evidence: automatic, mandatory registration (confirmed; B2 §1.7).
- Proposed change: rewrite as "Students are registered automatically for every meal, whether or not they are on campus (confirmed), and the platform also has a random-allocation notification. Registration counts therefore record the absence of an opt-out, not an intention to attend." Remove "(candidate)" for the automatic part; keep random allocation as a separate candidate detail.

**G2-19 (P1, add). Cancellation-cap row lacks the four-day rule and the no-nullify consequence.**
- Line 85 row.
- Evidence: 5 per meal type per month, at least 4 days ahead, "otherwise auto-registered" (confirmed; B2 §3).
- Proposed change: add "and each must be made at least four days ahead; beyond the five, there is no way to remove a meal from the bill." Underlying issue: "the cap limits exits from a default booking, rather than limiting bookings."

**G2-20 (P1, add). New symptom row: reheated, repeatedly transferred food at Kadamba.**
- Evidence: as G2-16 (candidate, team judgement). Also B1: cooked food usable 3 to 4 hours (single-sourced).
- Proposed row: symptom "At Kadamba, food is cooked ahead, reheated several times and moved between vessels for display and service; the team judged its quality to fall quickly (candidate)." Underlying issue: "A first batch cooked well above turnout is held rather than discarded, so surplus reappears as reheated food later in service. Whether this lowers attendance is not evidenced; it is a chain, not a loop."

**G2-21 (P1, strengthen). Arrival-pile-up row: add the operator's rule of thumb and the back door.**
- Line 91.
- Evidence: operator rule: about 100 in the opening phase, about 100 through the middle, about 150 in the last 10 minutes; "for any meal the highest flow is in the last 10 minutes" (single-sourced, observer-verified). Records remain the measurement (26.5 percent in 9:15 to 9:30, confirmed). B1's "200 to 300 then 300 to 400" arrival figures are superseded (not used in the brief; keep them out). Back-door entry (G2-15).
- Proposed change: add "Kadamba's operator plans around roughly 150 arrivals in the last ten minutes, and late arrivals come in through the back door after close (single-sourced)." Do not let the operator's 100/100/150 replace or sum against the record figures (they total 350, far below ~400 daily scans, and are a rule of thumb).

**G2-22 (P1, strengthen). Over-cooking row: upgrade Kadamba 70 percent and note veg/non-veg separation.**
- Line 92: "Kadamba's floor manager describes a first batch for about 70 percent (single-sourced)".
- Evidence: B2 §3 row 1 (observer-verified).
- Proposed change: "Kadamba's operator plans a first batch of 70 percent of registrations for veg and non-veg separately (single-sourced, heard directly by the team)". Underlying-issue cell: add "Kadamba applies a fixed ratio with reactive top-up and no record of outcomes; Yuktāhār learns from its own books and re-projects from the first half hour of service. Neither is calibrated to measured breakfast turnout."

**G2-23 (P2, add). Item-waste row: add floating items and gram standards.**
- Line 93.
- Evidence: bonda, puri, vada and idli "float" (diners take more than the 4-idli / 100 g standard) (single-sourced, observer-verified).
- Proposed change: "puri, bonda, vada and idli are eaten, often beyond the per-person standard".

**G2-24 (P2, strengthen). Operator-level change row: add blame-free measurement.**
- Line 94: "Yuktāhār began tracking waste in August ... staff reported that waste had fallen (confirmed)".
- Evidence: staff initially feared blame; managers made weighing explicitly blame-free and discussed it daily (single-sourced, observer-verified; B2 §2.1). The coordinator watches a wastage board daily and aims to push the waste share down (B2 §2.2).
- Proposed change: add "after the managers made the weighing blame-free".

### Section: Actors (lines 102 to 114)

**G2-25 (P0, contradicts_existing). Prism described as a floor team's self-name.**
- Wrong: line 108 "the Kadamba operator, whose floor team calls itself the Prism team (single-sourced)".
- Evidence: B2 §3: "Prism (vaguely 'the Prism team') → Prism = Kadamba's outsourced vendor, tender-bid, runs all operations" (single-sourced, observer-verified).
- Proposed change: "Prism, an outside vendor contracted by tender, which runs all of Kadamba's operations (single-sourced)".

**G2-26 (P0, contradicts_existing). Five-person PM team and 20-to-30 staff figure.**
- Wrong: line 109 "Yuktāhār also has a five-person project management team"; "Cooking and security staff, 20 to 30 at Kadamba, eat from what is left after students".
- Evidence: "Yuktahaar project management team of 5 → 2 project managers (plus site staff doing PM work)" (team account preferred; B2 §3, §2.1). Staff/extra diners as G2-13.
- Proposed change: "Yuktāhār's vendor has two project managers, with some site staff sharing project-management work"; "At Kadamba, 30 to 50 outside people such as night-shift security, and about half the operator's staff, eat from the same food (single-sourced)."

**G2-27 (P1, revise). Operator staff roles differ in kind between the two kitchens.**
- Wrong/missing: line 109 lists "a storekeeper, a coordinator, cross-checkers, tasting pairs" as if one uniform role set.
- Evidence: Yuktāhār: no hierarchy, everyone does every job, no dedicated storekeeper-only role, peer cross-checking; kitchen teams for tasting, cutting and cleaning; no formal leave policy (load shared by agreement in the daily meeting); Ajita is mess in-charge, keeps accounts and the Wastage Register; Bhavani cross-verifies and writes the grocery register (single-sourced, observer-verified + her signature on the Fridge 3 log, confirmed records; B2 §2.1). Kadamba: a layered chain (G2-04); Nazir is the main veg chef, a head chef joins for biryani days (B2 §1.8).
- Proposed change: split into two sentences, Kadamba hierarchical (supervisor → manager → operations manager under Prism) and Yuktāhār flat with rotating roles and peer cross-checks. Names: the brief so far names no individual; if the editor names anyone, use **Ajita** (not "Adit Amma" or "Sylaja") and **Bhavani**; otherwise use roles ("the mess in-charge, who also keeps the accounts and the wastage register"). The "Adit Amma" = Ajita identity remains a candidate (B2 §2.1); do not print "Adit Amma" anywhere.

**G2-28 (P1, add). Governance actors: add CFS and CDS; add the facility team.**
- Wrong/missing: lines 105 to 107, 111, 118 have no CFS and no CDS actor; "Faculty quality-control visitors inspect the operators' stores" is the only QC actor.
- Evidence: CFS → CDS chain (G2-04). Tasting before service by the facility team together with 2 Prism staff; QC inspects weekly (single-sourced, observer-verified; display plate and tasting confirmed observed; B2 §1.4).
- Proposed change: add "CFS and CDS: named by the Kadamba operator as the institutional line above the vendor (single-sourced; their relation to the Mess Committee, Mess Office and Warden is unconfirmed)". Replace line 111 with "Quality control: a weekly QC inspection, and a facility team that tastes each meal with two Prism staff before service (single-sourced; tasting observed)." Keep the faculty-visitor detail only if it is sourced separately.

**G2-29 (P1, revise). Walk-in portions vs extra-diner portions may be the same allocation.**
- Line 136: "Kadamba prepares 30 to 40 extra portions for such diners (single-sourced)" (from B1, noisy audio, paying/unregistered diners).
- Evidence: B2 §1.3 says about 30 extra portions are cooked for outside people such as security (observer-verified). B2 does not mention a separate walk-in allocation.
- Proposed change: do not present both as separate buffers. Write "Kadamba cooks about 30 extra portions beyond registrations; the operator described these as for outside diners such as night-shift security, and an earlier recording as for paying walk-ins (single-sourced); whether they are one allocation or two is unconfirmed." Add to open items.

### Section: Institutions (lines 116 to 122)

**G2-30 (P1, add). Yuktāhār's book system is the institution, and the brief under-describes it.**
- Line 121 says "a set of paper registers maintained daily with paired cross-checking".
- Evidence (confirmed records for each book, photographed; operator explanation single-sourced): Daily Meal Wastage Book (kept by the mess in-charge: per dish raw issued, cooked, leftover, percentage, run-out time, re-cook quantity; registered and ate by category; student plate waste plus leftover = daily meal wastage); weekday attendance register; wastage board; Grocery/issue book (header carries the day's registrations); store/ingredient book; stock register; vegetable book and indent (with spoilage remarks); milk, fruit, gas, electricity and water register; fridge temperature and cleaning logs. **Two-book reconciliation rule:** the store book (issued) must match the physical book (cooked); mismatches are raised in the daily meeting; the Dal Toor cross-check held on 18-9-26 (confirmed records). B2 §2.2.
- Proposed change: one compact sentence listing the books by what they record, plus "the issue book must reconcile with what was cooked, and any mismatch is raised the same day (confirmed)". Keep "not to find fault" and add "made blame-free deliberately when weighing began".

**G2-31 (P1, add). Food-safety regime: give the sequence.**
- Line 122: "an external 'Eat Right Campus' certification, food samples retained for 72 hours, laboratory testing ... and water-quality records (single-sourced)".
- Evidence: cooking temperature checked → sample retained 72 hours (to test if anyone falls ill, including to tell illness from outside food) → wrapped display plate at the entrance for every meal → serving temperature per item → tasting by the facility team with 2 Prism staff → corrections → service; weekly QC; daily TDS on cooking and drinking water, failure triggers a full check (single-sourced, observer-verified; display plate confirmed observed; B2 §1.4, §3).
- Proposed change: replace with the sequence in plain prose.

### Section: Processes (lines 124 to 139)

**G2-32 (P1, revise). Procurement line: Kadamba's three tiers.**
- Line 131: "at Kadamba, meat, eggs, milk and paneer one day ahead (single-sourced)".
- Evidence: dry goods (rice, groundnut, putna, masala, ghee, podi) one week ahead; perishables (milk, fruit, meat, eggs, most vegetables) the day before; some vegetables 2 to 3 days ahead (single-sourced, observer-verified; B2 §1.6). Yuktāhār: raw materials bought from many local shops and godowns, cleaned and segregated before issue against a per-item impurity norm; exceeding it means complaining to or changing the supplier; the operator also visits mills (B2 §2.3, §2.4).
- Proposed change: state Kadamba's three tiers; extend the Yuktāhār impurity sentence with "against an expected grams-of-impurity norm per item, above which the supplier is challenged or changed".

**G2-33 (P1, revise). Quantity-planning and top-up lines.**
- Lines 132, 133.
- Evidence: G2-11, G2-12. Yuktāhār: two roti counters at peak; rotis handmade without oil (B2 §2.3).
- Proposed change: add Kadamba's veg/non-veg split, gram standards and supervisor-called top-up; add Yuktāhār's first-half-hour projection.

**G2-34 (P1, revise). Late-entry line.** Line 135: add back-door entry after 9:30 (as G2-15).

**G2-35 (P2, revise). Leftover reuse line.** Line 137 / line 64: "leftover idli becomes an upma-style dish" → "leftover idli becomes idli upma or idli poha for lunch" (B2 §2.3). Keep Kadamba's dustbin-and-contractor route (B1; B2 §1.5 says it still stands). Add "held food is reheated for later service at Kadamba (candidate, team observation)".

### Section: Resources (lines 141 to 148)

**G2-36 (P1, revise). Operator records.**
- Line 144 lists Yuktāhār registers and, for Kadamba, "the live scan count watched during service and a waste record".
- Evidence: G2-30 for Yuktāhār; for Kadamba, per-dish gram standards (single-sourced), 72-hour samples, daily TDS log (single-sourced). Yuktāhār tried Zoho ERP and dropped it: the tool cost "lakhs of rupees" to predict what its books already show, and its staff are not digitally inclined; office staff digitise later (single-sourced, observer-verified; B2 §2.4). Utility data is used: a Wednesday electricity spike from idli-batter grinding informs how long machines run (B2 §2.2).
- Proposed change: add the missing books and Kadamba's gram standards; add one sentence: "Yuktāhār tried a commercial ERP to predict demand and dropped it, judging its own books sufficient and its staff not suited to digital tools (single-sourced)."

**G2-37 (P2, add). Inputs.** Yuktāhār uses pink salt and cold-pressed oil (for about six months, team account; B2 §2.4 notes compatibility with B1's "since takeover"). Relevant only as evidence of a quality-and-cost stance; optional.

### Section: Constraints (lines 150 to 164)

**G2-38 (P1, add). Procurement tiers as a constraint.**
- Line 153 already says perishables T-1 and vegetables keep 2 to 3 days, and that the supply chain "does not require the four-day lead (candidate)".
- Evidence: G2-32. Dry goods are bought a week ahead, which is longer than the four-day lead, but they are non-perishable and not quantity-sensitive at the scale of a day.
- Proposed change: "Kadamba buys dry goods a week ahead, some vegetables two or three days ahead and all other perishables the day before (single-sourced). Only non-perishable stock is committed before the four-day registration close, so the kitchen's supply chain does not need the four-day lead (candidate)." Also reconcile line 157 "Kadamba cannot hold excess stock (single-sourced)" with a week of dry goods: specify "cannot hold excess perishable or cooked stock" or flag.

**G2-39 (P1, add). The pre-service food-safety sequence fixes the first batch in time.**
- Evidence: G2-31 (sequence), G2-07 (5:30 start, ready 7:30).
- Proposed change: "Before service, each item passes a cooking-temperature check, a retained sample, a display plate, a serving-temperature check and a tasting (single-sourced). The first batch must therefore be cooked and approved before the first diner arrives, before any sign of the day's turnout exists (candidate)."

**G2-40 (P1, add). Digital capacity and measurement culture as constraints.**
- Evidence: staff not digitally inclined, ERP dropped (B2 §2.4); measurement worked only once made blame-free (B2 §2.1).
- Proposed change: "At Yuktāhār the records are on paper and staff are not digitally inclined; a commercial ERP was tried and dropped (single-sourced). Its waste measurement took hold only after it was made blame-free."

**G2-41 (P2, add). Veg and non-veg are planned separately at Kadamba** (append to line 159).

### Section: Initial Problem Framing (lines 166 to 174)

**G2-42 (P0, contradicts_existing). "Eaten by staff" understates and mis-describes the absorber.**
- Wrong: line 170 "Surplus is partly reused, partly eaten by staff, and the rest is thrown away."
- Evidence: G2-13 (30 to 50 outside people plus about half of Kadamba's staff, with about 30 portions cooked for them); G2-16 (held and reheated, candidate); G2-14 (5 to 10 percent operator waste figure, base unstated).
- Proposed change: "Surplus is partly reused, partly eaten by people outside the registration and by the operators' own staff, partly held and reheated into later service, and the rest is thrown away. Kadamba's operator puts the waste at 5 to 10 percent a day, a figure hard to square with a first batch cooked for nearly twice the turnout."

**G2-43 (P1, revise). Student-side paragraph: from "two tools" to "a default with a narrow exit".**
- Line 172: "The system gives students two ways to avoid paying ... against a registration that closes four days ahead in weekly blocks."
- Evidence: G2-06, G2-08.
- Proposed change: "Students do not choose to book breakfast; they are booked automatically, on campus or not. To avoid paying for a breakfast they will not eat they can cancel it, at most five times a month per meal and at least four days ahead, or mark it as skipped, which returns nothing. A student who decides on the morning itself has no option at all."

**G2-44 (P1, revise). Framing question: add the operator contrast.**
- Line 174 asks why each kitchen has to guess its conversion.
- Evidence: B2 §4: two forecasting philosophies side by side (Kadamba fixed ratio + reactive top-up, no learning record; Yuktāhār matching-week learning from its books + first-half-hour projection), neither calibrated to measured turnout; same billing basis, opposite operator stances.
- Proposed change: extend the second question: "... when the data needed to calibrate it is already being recorded, and when one operator already learns from its own books while the other applies a fixed ratio?" Keep the question form; do not name a fix (D-45).

---

## 2. Items checked and found consistent (no change)

- No B1 Kadamba kg waste figures appear (withdrawn by B2); keep them out.
- No "Adit Amma" or "Sylaja" appears; no "200 to 300 / 300 to 400" arrival figures appear.
- Yuktāhār breakfast "about 50 percent" belief vs 28 percent record (line 64, 92) matches B2 §2.3.
- Record figures (37.1 percent, 32,162, ~1,070/day, 42.1/27.3 percent, 26.5 percent 9:15 to 9:30, Yuktāhār 18 to 40 / 56 to 89 percent) are unchanged by B2.
- Dustbin → garbage contractor, no composting (line 137) still stands (B2 §1.5).
- Zero em dashes (D-43); headers match D-7.

---

## 3. Phase 3 implications

1. **Absorber check (D-45, D-49, P5):** first-batch calibration at Kadamba would take food from 30 to 50 outside diners and about half the staff, who are fed partly by design (about 30 planned portions) and partly from surplus. Any LP that trims the first batch (LP ranked 4 in `00-phase3-input-brief.md`) must budget these meals explicitly. This replaces the "20 to 30 staff" tension in MASTER_CONTEXT §9.
2. **Default-not-choice strengthens the booking-rule lever (ranked 2, T-1 confirm/skip):** the root cause is an opt-out default with a narrow, four-day-ahead exit, so a lever that changes the default (opt-in or confirm) acts at Meadows level 5 rather than tuning the cap.
3. **Operator culture as a leverage point:** the same billing basis yields "we cook to what we are paid for" at Kadamba and "waste reduction is profit" at Yuktāhār. Practice-sharing between operators (ranked 7) gains weight; Yuktāhār's book system is the ready-made template.
4. **Blame-free measurement and non-digital staff (P2 principle):** any new measurement must be paper-compatible and explicitly non-punitive; Yuktāhār's ERP rejection argues against a software-first intervention in the kitchen.
5. **Timing of any signal (P4):** the food-safety sequence and 5:30 start mean the first batch is fixed before any turnout signal. A T-1 confirm signal fits; a same-morning signal cannot change the first batch, only the top-up. Yuktāhār's first-half-hour projection misses the closing crest; interventions must address the crest separately.
6. **Quality chain:** surplus → holding and reheating → lower quality is a candidate chain that could make over-preparation self-defeating for attendance; it must not be written as a loop (D-40) until the closing link is evidenced.
7. **D-54 hold stands:** Kadamba's "paid for registrations" is a hint, not the contract; billing and vendor-payment levers remain held back.
8. **Governance addressee is unclear:** a routing lever (ranked 1, route records to the rule owner) needs to know who the rule owner is; the CFS → CDS (Raju/Giri) vs Mess Office/Committee/Warden ambiguity must be resolved before naming a recipient.

---

## 4. Open items (new or changed by this pass)

- **Raju vs Giri** at CDS: two roles or one wrong name (D-24, do not merge).
- **CDS vs Mess Office vs Mess Committee**: is CDS the body this brief calls the Mess Office? (pre-existing, now sharpened by the CFS → CDS chain).
- **Skip Meal reaching Kadamba's kitchen**: institution says yes (2026-09-13), Kadamba operator says it cooks on registrations only.
- **Kadamba 5 to 10 percent waste**: base (per meal/day, weight, plate vs kitchen) and how it squares with 70 percent vs 37 percent.
- **Kadamba extra portions**: are the ~30 portions for outside diners and the 30 to 40 walk-in portions one allocation or two?
- **Registration cadence**: weekly blocks (operators) vs monthly (student interviews) vs automatic default (B2).
- **Diagrams 1 and 2**: still 5 September Mermaid; diagram 2 still says the Mess Office "orders".
- "Kadamba cannot hold excess stock" vs dry goods bought a week ahead: scope of the claim.

**Resolved or upgraded by B2:** Kadamba 70 percent first batch (now observer-verified); Prism's identity (outsourced tender vendor running all operations); Yuktāhār PM team size (two); Kadamba extra-diner count (30 to 50 outside + ~50 percent of staff, replacing 20 to 30); Kadamba cancellation rule (5 per meal type per month, ≥4 days ahead, confirmed); cross-checker identity (Ajita; "Adit Amma" link candidate); Kadamba procurement cadence (three tiers).
