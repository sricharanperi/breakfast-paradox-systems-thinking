# Prathyusha's Braindump #2 — CFS/CDS Interview + Kadamba Kitchen Visit + Mess Posters

Raw braindump captured 2026-09-13, following the same convention as
[`prathyusha_braindump.md`](prathyusha_braindump.md) (braindump #1, 2026-09-05): dump everything
observed/heard before it gets structured into the formal 15-deliverable framework
(`.claude/skills/systems-design-toolkit/SKILL.md`). Not polished, not yet reconciled
line-by-line against every existing deliverable — that reconciliation is flagged inline
where it matters, but the ideas themselves are kept close to how they were captured.

**Sources feeding this braindump:**
1. Interview with the **CFS Chair** (Campus Facilities Services — the department CDS sits
   under). The **CDS Chair is Giri** — not yet interviewed directly; this is the CFS
   Chair's account of CDS operations.
2. A **walkthrough of the Kadamba kitchen** (equipment, layout, inventory).
3. **Four mess posters** photographed on-site (CDS Student Handbook, CDS Food Card User
   Guide, main CDS overview poster, FSSAI Eat Right Campus certificate) — transcribed in
   full in §11 below.

This is genuinely new primary research: `research/primary-research/index.md` had **"Mess
staff / vendor process walkthrough (their side of the daily routine)"** as an open,
unchecked item — this braindump is the first material that resolves it.

---

## 1. Org structure — CFS and CDS

- **CFS** (Campus Facilities Services) is the parent department.
- **CDS** (Campus Dining System — what the posters call "Campus Dining Services") sits
  under CFS. Other departments also sit under CFS — CLS, CWS, etc. — but **CDS is the one
  in scope for this project.**
- CDS Chair = **Giri** (not yet interviewed). This interview was with the **CFS Chair**
  instead.

**Mapping:** existing deliverables (`deliverables/phase-1/01-system-context-brief.md`,
`02-stakeholder-map.md`) already list "Mess Committee" and "Warden" as the governing
bodies but don't name **CFS** as the parent department above CDS, nor separate out CDS
from sibling departments (CLS/CWS). This is a **structural correction/addition**: the
existing stakeholder map's "Mess Committee" language should probably be reconciled with
"CDS Committee" (see §2) — worth checking whether these are the same body under a
different name, or genuinely different groups. **Open question to resolve before Phase 2
sign-off.**

---

## 2. Decision-making flow for operational changes

Over the last few days there have been many operational and equipment changes. The
decision flow:

1. **CDS committee members** (faculty) make the actual decisions on operational/equipment
   changes.
2. These decisions **go through the CDS Student Council** first.
3. Whatever the CDS Student Council proposes/passes gets **reviewed and approved by the
   CDS committee (faculty)**.
4. Feedback (see §7) is triaged by **intensity**:
   - **High-intensity** feedback → a **CDS committee member** gets involved to decide/change
     something.
   - **Low-intensity** feedback → the **CFS head** handles it directly, no committee
     escalation.

**Mapping:** this is a genuinely new governance detail — feeds directly into deliverable
#3 (Power-Interest/Leverage Map) as a missing escalation pathway, and into #7 (Systemic
Problem Analysis, `deliverables/phase-2/07-systemic-problem-analysis.md`) as a concrete
feedback-loop mechanism (a real, named balancing loop: feedback intensity → escalation
level → decision speed). Also worth cross-checking against the **Student Parliament**
connection already flagged in braindump #1 and in the Phase 1 power analysis (Student
Parliament apparently has mess-related roles) — does "CDS Student Council" = "Student
Parliament's mess-facing subgroup," or a separate body? **Needs reconciling.**

---

## 3. Menu policy — biweekly rotation (a recent governance win)

- **Before:** one fixed menu for the **entire semester** — a real, named pain point
  (people get bored of the food).
- **Now:** CDS convinced the **CDS Student Council**, who convinced the **Student
  Parliament**, to move to a **biweekly rotation**: weeks 1 & 3 share one menu, weeks 2 &
  4 share another.
- Menu also now changes **monthly** and is **seasonal**.
- There will be **one admin per mess**, who is also a **CDS member**, coordinating
  caterers, students, faculty, etc. for that specific mess.

**Mapping:** strong, concrete example of a **leverage point already exercised** — worth
flagging explicitly in deliverable #7 / eventual #11 (Leverage Points) as a *precedent*:
the system has already demonstrated it can respond to a named pain point (menu fatigue)
through the Student Council → Parliament → Committee pathway in §2. That's evidence the
escalation pathway in §2 actually works, not just theoretical governance structure.

---

## 4. Outsourcing and equipment

- Kitchens were **institute-owned** before; catering is now **outsourced**, procured via
  **open tender**.
- Decisions have been made to modernize kitchens for **hygiene** and install **high-value
  equipment** (see §12, kitchen walkthrough).

**Mapping:** confirms/extends braindump #1 §6a's "LPG/gas price → menu shrinkage"
hypothesis — the underlying mechanism (outsourced catering via tender) is now visible.
Should feed a Role C (mess operations) interview question: *does the open-tender contract
pass through ingredient-cost volatility to the caterer, or is it fixed-price?* That
directly determines whether the LPG-cost causal link from braindump #1 is even active
under the new outsourced model.

---

## 5. Registration and vendor communication cadence

- Meal registrations happen **four days ahead** (T-4).
- Once registrations are locked, they are **communicated to the vendor** on the same
  four-day cadence.
- **Weekly stock assessment** happens, driven by **consumption patterns** — high-turnout
  items (paneer, eggs, chicken) get **>90% turnout**; general turnout is **~70%**;
  **breakfast turnout is only 35–40%**, mainly because of **class timings**.

**Mapping:** this directly **confirms and quantifies** the core "Breakfast Paradox"
phenomenon this whole project is about — registered-but-doesn't-show, specifically at
breakfast. The T-4 registration/vendor cadence also **matches the poster data exactly**
(§11.2 — "students must register their meals at least four days in advance," "cancel...
must also be made at least four days in advance"), which is good independent
cross-validation between the interview and the printed CDS handbook. This is
high-confidence, verified data — should go straight into deliverable #7's quantified
loop diagram and into deliverable #5 (`05-system-timeline-bot-map.md`) as a real number
for breakfast turnout, replacing/supplementing the still-open observation item in
`research/primary-research/index.md` ("Direct observation of 2-3 real mess-hours
mornings" — this interview gives an aggregate number where direct observation would give
a time-series; both are still worth doing).

**Breakfast bottleneck mechanism, spelled out:**
- ~80% of students arrive at **9:20 AM**.
- Items are available for **refill until 10:00 AM**, but you **cannot enter the mess after
  9:30 AM**.
- **Lights and fans are switched off after 10:00 AM.**
- Staff are supposed to **clean only after the last student leaves**.

**Mapping:** this is a precise, minute-level account of the exact bottleneck the "5b —
30-min interval observation protocol" in braindump #1 was designed to capture. It
**partially resolves** that open item without needing to run the observation ourselves —
though live observation would still confirm whether the 9:20 AM arrival spike and the
9:30 cutoff actually produce a queue/crowding effect, which this account implies but
doesn't measure directly.

---

## 6. Kadamba specifics

- Kadamba's **breakfast is the most famous** among all the messes.
- Kadamba underwent **renovation** — explicitly **not related to turnout** (i.e., don't
  read the renovation as a turnout-driven investment; it was a separate hygiene/equipment
  decision, see §4).
- Seats vs. turnout: **420 seats**, but **1,200 students turn out**. Institute policy is to
  maintain a **1:3 seats-to-turnout ratio**.
- Extras like **omelets** are now offered so people don't get bored of the fixed menu —
  same anti-boredom logic as the biweekly rotation in §3, applied at the daily/per-item
  level instead of the menu-cycle level.
- Explored: **daily non-veg options** (currently being trialed/discussed, Kadamba-focused).

**Mapping — a data conflict to flag, not silently resolve:** the **main CDS poster
(§11.4)** lists Kadamba's **"Capacity"** as **1200**, in a table column alongside cuisine
and kitchen location. The interview's "420 seats, 1,200 turnout, 1:3 ratio" framing
suggests the poster's "Capacity" column is **student/registration capacity** (how many
students are assigned to that dining hall), **not physical seating capacity** — 420 would
be the physical seat count implied by the 1:3 ratio. This is exactly the kind of
same-number-different-meaning ambiguity worth a one-line clarifying question to the CFS
Chair or Giri before it goes into a deliverable as a hard fact.

---

## 7. Feedback mechanism

- Feedback is collected mostly via **posters and notifications**.
- Feedback gets classified by **intensity** (high/low) — routes to the escalation
  pathway in §2.

**Mapping:** feeds deliverable #7's feedback-loop diagram directly (see §2's mapping
note) — this is the *input* side of that loop.

---

## 8. Menu diversity — cross-state, not just cross-regional-mess

- Even within one mess "labeled" South Indian, the actual menu spans multiple states —
  e.g. avial, kootu, bisibelebath are each from **different states**, all served in what's
  nominally the South Indian mess. Same diversification logic applies across every other
  mess.
- **Risk flagged by the interviewee themselves:** because the menu is now known in
  advance (§3's biweekly rotation), students can **decide in advance not to come** on
  days when they dislike the known menu — i.e., the anti-boredom fix (predictable
  rotation) may have introduced a **new, opposite failure mode** (predictability enabling
  selective no-shows).

**Mapping:** this self-identified risk is a genuinely important addition to deliverable
#7 — it's a **second-order effect of a leverage-point intervention that already
happened**, exactly the kind of unintended-consequence pattern the Iceberg/CLD analysis
(deliverable #8, #7) is supposed to surface. Should be modeled as a **new loop**: menu
transparency ↑ → informed non-attendance ↑ → (offsetting some of) the boredom-driven
attendance gain the rotation was meant to produce. Worth a targeted interview question to
students: *does knowing next week's menu change whether you register/show up?*

---

## 9. Bakul and Palash — off-site kitchens (confirms + corrects braindump #1)

- For **Bakul** and **Palash**, food is **not cooked on-site** — it comes from an
  **outside kitchen**.

**Mapping — correction to braindump #1 §5c:** braindump #1 recorded the open question as
"Bakul = converted warehouse, food partly cooked at Palash and shipped in." **The poster
data (§11.4) resolves this precisely and corrects the hypothesis:** both Bakul *and*
Palash are off-site-kitchen dining halls (not Palash cooking for Bakul specifically) —
food for both is currently prepared at **one approved off-site kitchen** and transported
in, **until the Felicity Kitchen & Dining Facility becomes operational (expected December
2026)**, at which point this is presumably meant to change. This also closes part of the
still-open `research/primary-research/index.md` item: *"Why Bakul's registered/capacity
ratio is far lower than Kadamba's"* — the "newness/warehouse venue" hypothesis is now
better evidenced (off-site kitchen + smaller capacity by design: Bakul 750 vs. Kadamba
1200 per §11.4's table), though the *ratio* question itself isn't fully answered yet.

---

## 10. Waste management and food safety

- Waste is split into **production waste** and **plate waste**; both go to a **garbage
  collector** who transports it to an **outside compost facility**.
- When food is suspected **contaminated**, a **sample is sent to a lab** for testing.
- Prep timing varies by dish but generally **starts around 5:00 AM** (or earlier,
  depending on the dish).
- **Festive meals**: special festive menus are provided in all messes during festivals.

**Mapping:** the lab-testing detail is a strong, concrete tie to the **FSSAI "Eat Right
Campus" 5-star Exemplary certification** transcribed in §11.1 — that certificate is
externally issued, third-party-audited evidence that this internal food-safety process
(sampling + lab testing) is functioning well enough to earn the top rating. This is a
genuinely new "adjacent system" data point that braindump #1 §3 flagged as speculative
("Food safety" listed as a parallel system worth scanning) — now it's real, verified,
dated evidence, not just a category to keep in mind. Waste management (also flagged
speculatively in braindump #1 §3) now has a concrete two-stream, single-collector-to-
compost pipeline — simple enough that it's probably not a major system bottleneck, but
worth a footnote in deliverable #6 (System Map) for completeness.

---

## 11. Mess poster data (verbatim transcription)

Four posters, photographed on-site, saved at
`deliverables/phase-2/assets/WhatsApp Image 2026-09-13 at 12.34.19 AM.jpeg` (poster 1),
`...12.34.20 AM.jpeg` (poster 2), `...12.34.20 AM (1).jpeg` (poster 3), and
`...12.34.21 AM.jpeg` (poster 4). Transcribed word-for-word below; treat this section as
the authoritative source text for anything cited from these posters elsewhere in the
project.

### 11.1 — FSSAI "Eat Right Campus" certificate

> Certificate No: ER/ER/2026030X/11X98 *(partially obscured by glare/QR sticker — exact
> digits not fully legible in the photo)*
>
> **FSSAI** (एफएसएसएसएआई) — Ministry of Health and Family Welfare
>
> INTERNATIONAL INSTITUTE OF INFORMATION TECHNOLOGY
> Hyderabad, Telangana
> is certified as
>
> **Eat Right CAMPUS**
>
> as per guideline established by
> Food Safety and Standards Authority of India
> for the period of **30 March, 2026 – 29 March, 2028**
>
> ★★★★★
> **EXEMPLARY**
>
> Shri U. S. Dhyani
> Executive Director, FSSAI
>
> Implementation Partner: [name obscured] Hospitality Services Pvt Ltd
> Auditing Partner: Hygienia Business Assurance LLP
> Training Partner: Gyancity Educational Trust

### 11.2 — CDS Student Handbook (Monsoon 2026, effective Saturday, 1 August 2026)

- **CDS Portal:** `https://dining.iiit.ac.in` (accessible only through the IIIT internal
  network or VPN; registrations opened 27 July 2026)
- **Email:** cds@iiit.ac.in
- The **semester mess advance is unchanged from the previous year**; **meal prices have
  been revised by approximately 15%** to account for inflation and increased operating
  costs.
- **Semester CDS Charges:** the Semester CDS Advance for Monsoon 2026 is **₹30,500**. This
  amount is deposited at the start of the semester; meal charges are deducted based on
  actual consumption; remaining balance carries forward to subsequent semesters.
- **CDS Infrastructure Fee:** **₹550/month**, applicable to all hostel residents. Six
  months' worth is deducted from the mess balance during the first month of the
  semester. This fee supports: dining hall construction and renovation, kitchen
  infrastructure, commercial kitchen equipment, maintenance, utilities, and long-term
  replacement of infrastructure. **The fee applies even to students with approved mess
  exemptions**, because the dining infrastructure is maintained for the entire
  residential community.
- **Meal Registration:** advance registration lets CDS estimate demand accurately and
  prepare the right quantity of food. Students must register meals **at least four days
  in advance** through the CDS Portal. Benefits: reduced food wastage, better menu
  planning, lower meal prices, improved dining experience.
- **Automatic Meal Allocation:** if no registration is made, CDS automatically allocates a
  **vegetarian meal**; the student is assigned to one of the dining halls; the assigned
  dining hall can be viewed on the CDS Portal.
- **Meal Cancellation:** students may cancel up to **5 breakfasts, 5 lunches, and 5
  dinners every month**. Cancellations must also be made **at least four days in
  advance**.
- **Mess Exemptions:** students proceeding for internships may apply for a mess exemption
  through IMS by attaching their internship offer letter. PhD students may apply without
  supporting documentation. Students requiring long-term medical exemptions should obtain
  a recommendation from Arogya along with a declaration describing their alternative
  dining arrangements.
- **Meal Delivery:** in exceptional medical circumstances, meals may be delivered to
  hostel rooms; requests should be emailed to cds.operations@iiit.ac.in.
- **Contact:** Campus Dining Services — Portal `https://dining.iiit.ac.in`, Email
  cds@iiit.ac.in. For operational issues, meal registrations, hygiene concerns, or
  general enquiries, contact the CDS team through the above channels.

### 11.3 — CDS Food Card User Guide (Monsoon 2026, effective August 1st 2026)

- **CDS Portal:** `https://dining.iiit.ac.in` (IIIT network/VPN only). **Email:**
  cds@iiit.ac.in.
- The CDS Food Card is a **cashless way for non-student diners** to access campus dining —
  replaces handwritten meal registers with a digital system supporting advance meal
  registration, QR-code billing, and online account management. **Mandatory for interns**;
  **recommended for faculty, staff, project staff, and other community members** who dine
  regularly on campus.
- **Benefits:** discounted meal prices through advance registration; fast QR-code-based
  billing; cashless payments; online balance management and recharge; meal registration
  through the CDS Portal; better meal planning and reduced food wastage.
- **Getting your Food Card:** issued at **Campus Facilities Services (CFS), Himalaya
  Administrative Block – Basement**. Bring your IIIT or organization ID card. A **₹100
  card issue fee** is adjusted against the initial recharge. Faculty and staff cards are
  linked to **salary deduction** instead of a prepaid balance.
- **Using your Food Card (3 steps):**
  1. **Recharge** your account through the CDS Portal.
  2. **Register meals** through the CDS Portal at least one day in advance to receive the
     discounted Food Card rate. If a meal is not registered, the regular Unregistered
     (Pay & Eat) price applies.
  3. **Scan your QR code** — present it at the billing counter before every meal. Only one
     discounted meal may be availed per meal session; additional meals are charged at
     Pay & Eat rates.
- **Important information:** meals should be registered one day in advance; cash payments
  are not accepted; your QR code is personal and must not be shared; maintain a
  sufficient account balance before dining; Food Cards may be used at all CDS dining
  halls.
- **Need help?** Food Card issuance, portal access, balance recharge, meal registrations,
  dining services — contact CDS: **Campus Dining Services (CDS)**, Email
  `cds@iiit.ac.in`, **CDS Portal: `https://mess.iiit.ac.in`**.

**Discrepancy on this poster, verified directly against the photograph (not present in the
original transcription above, which had glossed this line as "portal above" without
checking it matched):** the CDS Portal is given as `dining.iiit.ac.in` at the top of this
same poster and `mess.iiit.ac.in` at the bottom contact line — two different domains for
what should be the same portal, on one physical sign. The main CDS overview poster (§11.4)
does **not** have this problem — it says `dining.iiit.ac.in` in both its top and bottom
sections, consistently. So this is specific to the Food Card User Guide poster, not a
project-wide naming question like the CDS/Mess Office one — it looks like a plain
proofreading error on CDS's own signage, physically displayed at Kadamba, not resolved by
any other source here. Worth a one-line question to CDS/CFS: which domain is actually live.

### 11.4 — Main CDS overview poster (Monsoon 2026, effective August 1, 2026)

- **Objective:** "provide nutritious, hygienic, and affordable meals while ensuring
  efficient operations and minimizing food wastage through advance meal planning."
- **What's new this semester:**
  - Four dining halls operate throughout the semester; South Indian, North Indian, Satvik
    and Jain cuisines are available.
  - Kadamba Dining Hall now includes a **commercial dishwasher** for improved hygiene.
  - Until the **Felicity Kitchen & Dining Facility** becomes operational (expected
    **December 2026**), food for **Bakul and Palash** is prepared in an approved off-site
    kitchen and transported under hygienic conditions.
- **Campus dining facilities table** (CDS operates four dining halls):

  | Dining Hall | Capacity | Cuisine | Dining Type | Kitchen |
  |---|---|---|---|---|
  | Kadamba | 1200 | South Indian | Mixed | On-site |
  | Bakul | 750 | North Indian | Mixed | Off-site |
  | Palash | 450 | North Indian | Vegetarian | Off-site |
  | Yuktahar | 350 | Satvik & Jain | Vegetarian | On-site |

  Note: Kadamba also serves a **mildly spicy/salty, less-oil version** of its vegetarian
  dishes at a separate counter, to accommodate diverse tastes. **Unregistered dining is
  limited** in the dining halls, especially near the end of the session, to avoid food
  shortages for registered diners.

- **Meal timings:**

  | Meal | Timing |
  |---|---|
  | Breakfast | 7:30 AM – 9:30 AM |
  | Lunch | 12:30 PM – 2:30 PM |
  | Evening Snacks* | 5:00 PM – 6:00 PM |
  | Dinner | 7:30 PM – 9:30 PM |

  *Snacks are available only at Kadamba and Yuktahar. To allow adequate cleaning and
  preparation for the next meal, students are requested to **vacate the dining hall
  within 30 minutes** after meal service closes.

- **Dining hall etiquette:** present QR code before every meal; keep the dining hall
  clean; return used plates and cutlery to designated counters; don't move around dining
  furniture or stick chewing gum on it; respect the dining hall staff; vacate seats after
  completing the meal; follow queue discipline; report any hygiene concerns immediately;
  avoid wasting food.

- **Meal charges table** (Students / Card / Spot rates; ₹):

  | Item | Kadamba/Bakul/Palash — Students | ...Card | ...Spot | Yuktahar — Students | ...Card | ...Spot | Faculty/Staff Lounge |
  |---|---|---|---|---|---|---|---|
  | Veg Breakfast | 48 | 55 | 81 | 53 | 60 | 92 | — |
  | Double Egg Breakfast | 66 | 76 | 111 | — | — | — | 100 |
  | Veg Lunch | 65 | 75 | 111 | 72 | 82 | 124 | — |
  | Evening Snacks* | 17 | 20 | 28 | — | — | — | — |
  | Veg Dinner | 65 | 75 | 111 | 72 | 82 | 124 | — |
  | Chicken Biryani Lunch | 155 | 178 | 263 | — | — | — | — |
  | Dinner with Egg Curry | 91 | 105 | 154 | — | — | — | — |
  | Dinner with Special Chicken Curry | 106 | 122 | 180 | — | — | — | 200 |

  *Evening Snacks available only at Kadamba and Yuktahar. **Footnote on the poster:**
  "The Students and Card rates apply only if the registration of the meal was done
  before in the CDS portal. Otherwise, the Spot rate will be applicable even for
  students and card holders." *(Note: the Faculty/Staff Lounge column's alignment
  against specific rows was partially ambiguous in the photograph — the 100 and 200
  values are transcribed against the rows they appeared closest to, Double Egg Breakfast
  and Dinner with Special Chicken Curry respectively; worth confirming against a clean
  copy of the poster before treating those two numbers as certain.)*

- **QR code billing & CDS Portal:** every diner receives a unique QR code through the CDS
  Portal or Food Card, shown at the billing counter for every meal. Students without
  smartphones may obtain a printed Food Card from CFS for a nominal charge. The QR code
  is personal and must never be shared; if compromised, it can be regenerated through the
  portal (the old Food Card, if QR is regenerated through the portal, becomes invalid).
  Only one student meal per meal session is permitted at the registered rate; additional
  meals during the same session are billed at spot rate. Cash payments are not accepted;
  guests use a UPI Pay & Eat option at a higher spot rate.

- **Special dietary requirements:** diners requiring special meals for medical reasons may
  avail low-oil, non-spicy meals at **Yuktahar and Kadamba**.

- **Need help?** Food Card issuance, portal access, balance recharge, meal registrations,
  dining services — contact Campus Dining Services (email cds@iiit.ac.in, portal
  `https://dining.iiit.ac.in`).

**Mapping:** this poster set is now the single richest quantitative source in the
project — capacities, cuisines, kitchen locations, exact meal-charge tiers (three-tier
pricing: registered-student < card < walk-in-spot, a real financial incentive structure
that itself shapes registration behavior), and the exact T-4/T-1 registration windows for
students vs. Food Card holders respectively. This should be logged in
`research/primary-research/index.md` as a new dated entry and treated as ground truth
per that file's own protocol (§0 there: "only material logged here... is treated as
ground truth"). It directly feeds deliverables #1 (context brief — capacity/pricing
numbers are currently thin there), #6 (System Map — dining-hall-level structural detail),
and #7 (the three-tier pricing is itself a designed incentive mechanism worth a loop of
its own: registration incentivized by price gap → registration accuracy ↑ → wastage
↓ — but only if the *breakfast-specific* registration/turnout gap from §5 doesn't break
this assumption at breakfast specifically).

---

## 12. Kadamba kitchen walkthrough — equipment and layout

Observed directly during the kitchen visit:

- **Roti line:** a machine that mixes flour into dough, divides it into portions; a
  second machine takes a small dough ball and automatically produces a round, roasted
  (both sides) roti.
- **Multi-item cooker:** one large machine can cook multiple item types simultaneously
  (e.g. chicken, idli) — veg and non-veg cooking are kept **physically separated**.
- **Curry/steaming machine:** does more than boiling/steaming — used for a wide range of
  curries. Notable feature: it **tilts** to drain water, which makes cleaning much
  easier and safer — previously, machinery had to be manually lifted/emptied by hand,
  which was flagged as **risky**; this has since been changed (tilting mechanism now
  standard).
- **Sterilization:** a machine to sterilize knives.
- **Prep automation:** machines to chop vegetables; machines to wash rice and lentils;
  machines to cook rice and lentils.
- **Butchering section:** present in the kitchen, but butchering itself usually happens
  **outside the hostel** and meat arrives ready to use; the on-site section may or may
  not actually be used for butchering.
- **Inventory — cold storage:** a large, low-temperature room functioning as a walk-in
  fridge — stores milk, curd, vegetables, cut vegetables, leafy vegetables, etc.
- **Inventory — dry storage:** separate dry-goods section for rice, sauces, lentils,
  flour, etc.
- **Inventory management:** the entire inventory (cold + dry) is managed by **one
  person**, following **FIFO (first in, first out)** and **FEFO (first in, first
  expiry, first out)**.

**Mapping:** this is the single most detailed physical/spatial account of a mess kitchen
in the project so far — directly answers braindump #1 §5c's call for a **spatial /
component map** ("Map the physical components within a mess... Map the actual space
layout, not just the process flow"), which was flagged there as having **no
floor-plan-level artifact yet**. This equipment list is enough raw material to build
that artifact for Kadamba specifically (still needs an actual floor-plan/Rich-Picture
sketch — the walkthrough gives components and some sequencing, not spatial coordinates).
Feeds deliverable #4 (Process Trace) and #6 (Rich Picture / System Map). The
single-person-inventory-manager detail is also a notable **single point of failure** /
bus-factor risk worth a line in the constraints section (braindump #1 §6) — nobody else
was mentioned as covering FIFO/FEFO discipline if that person is unavailable.

---

## Open items / where this braindump leaves things

- [x] **Resolved:** "Mess staff / vendor process walkthrough" (`research/primary-research/index.md`,
      previously unchecked) — this braindump *is* that walkthrough (CFS Chair interview +
      Kadamba kitchen visit).
- [x] **Partially resolved:** Bakul's capacity/off-site-kitchen question — corrected from
      "cooked at Palash" to "both Bakul and Palash use one shared off-site kitchen until
      Felicity Kitchen opens ~Dec 2026" (§9).
- [x] **Partially resolved:** breakfast turnout number — 35–40%, with a named mechanism
      (9:20 AM arrival spike vs. 9:30 AM entry cutoff) (§5). Live 30-min-interval
      observation (braindump #1 §5b) is still the only way to get a real time-series, but
      the aggregate number and mechanism are no longer missing.
- [ ] **New:** reconcile "CDS Committee" / "CDS Student Council" (this braindump) against
      "Mess Committee" / "Student Parliament" (existing Phase 1 stakeholder map and power
      analysis) — same bodies under different names, or genuinely different groups? (§1, §2)
- [ ] **New:** the "known menu → informed non-attendance" risk self-identified in §8 —
      needs a targeted student interview question; candidate new loop for deliverable #7.
- [ ] **New:** confirm the Kadamba "420 seats vs. 1,200 capacity-on-poster" reconciliation
      (§6) directly with CFS/CDS before citing both numbers as consistent facts in the
      same deliverable.
- [ ] **New:** ask whether the open-tender catering contract is fixed-price or
      cost-passthrough — determines whether braindump #1's LPG-price → menu-shrinkage
      hypothesis is still mechanically active under the outsourced model (§4).
- [ ] **New:** log this braindump's sources formally in `research/primary-research/index.md`
      (new dated row/entry) so it counts as ground truth per that file's own protocol —
      not yet done as of this writing.
- [ ] Still open from braindump #1, unaffected by this one: the Mess Cell WhatsApp resale
      market case study (§8 there); the multiple-stakeholder-maps decision (§2b there).

---

*This file is a scratchpad, not a deliverable — treat everything above as raw material
to be verified against `research/` before it goes into any numbered deliverable under
`deliverables/`. Poster transcriptions in §11 are the exception: they are a direct,
word-for-word source document and can be cited as primary evidence once logged in
`research/primary-research/index.md`.*
