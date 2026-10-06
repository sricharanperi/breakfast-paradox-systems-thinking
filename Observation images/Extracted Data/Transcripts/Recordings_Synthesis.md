# Mess Field Recordings – What Was Said and What It Means

Source: 8 audio files in `Observation images/` (about 2 h 15 min in total), recorded during the team's visits to the campus messes in September 2026.
Method: Whisper large-v3 run locally, translating Telugu and mixed Telugu/English speech into English. Raw machine output is in `raw_machine_translation/`. This file is the cleaned, interpreted version.

**How far to trust it.** The mess audio is noisy and the speakers switch between Telugu and English. The Yuktahar recording is mostly English and is reliable. The Kadamba and IIIT Road recordings are mainly Telugu, so their translations get the gist right but garble individual sentences. Numbers and statements marked *(unclear)* should be checked against the audio before being quoted in a deliverable. Timestamps are given as [mm:ss] so each point can be traced back.

---

## 1. Which recording is which

| File | Length | Where / who | Language | Reliability |
|---|---|---|---|---|
| **Yuktahar Mess.mp3** | 49:48 | Yuktahar mess: the operator's senior manager / project lead (ABC Hospitality Services) walks the team through all the registers | Mostly English | High |
| **Kadamba Mess.mp3** | 37:24 | Kadamba mess: the operator's floor/mess manager ("we are the Prism team"), plus a student complaint at the end | Telugu + English | Medium |
| IIIT Road 51.m4a | 25:52 | Same Kadamba conversation as above: the first ~26 minutes, with more of the opening | Telugu + English | Medium |
| IIIT Road 52.m4a | 0:37 | Kadamba: short exchange on menu items that always get wasted (also in the Kadamba file at 26:00) | Telugu | Medium-low |
| IIIT Road 53.m4a | 3:18 | Kadamba: breakfast timing, tasting and food-sample process (also in the Kadamba file from 33:41) | Telugu | Medium-low |
| IIIT Road 54.m4a | 9:32 | A mess run by **Vijayalakshmi Caterers**: tender, pricing, off-site kitchen, 70–80% cooking rule | Telugu + English | Medium |
| IIIT Road 55.m4a | 8:23 | Probably the same Vijayalakshmi mess: the manager on timings, rush hours, menu involvement, paneer supplier, complaints | Telugu + English | Medium |
| IIIT Road 50.m4a | 0:44 | Unclear which mess: asking a staff member about the reporting chain | Telugu | Medium |

> **Overlap:** *Kadamba Mess.mp3* contains the same conversation as IIIT Road 51 (whole), 52 and 53, plus about 5 extra minutes (LPG shortage, broken toaster, portion sizes, QC visits, water/TDS). Treat them as one interview, not four. Clips 54 and 55 are a separate visit. The operator says "if we compare with Kadamba…", so it is **not** Kadamba, and they buy paneer while Yuktahar makes its own, so it is not Yuktahar either. **Please confirm which mess 54/55 was.**

---

## 2. Yuktahar Mess (operator: ABC Hospitality Services) – the planning system

*Speaker: the site head / project lead, who has been running it since the operator took over "last year" (August start). Reliable English transcript.*

### 2.1 How tomorrow's quantities are decided (the core loop)
- **Daily planning meeting, twice a day.** [00:11–01:15], [06:58–07:30]
  - *First half of the day:* the storekeeper, coordinator and kitchen staff decide **tomorrow's breakfast and lunch**.
  - *Second half of the day:* the same group decides **snacks and dinner**, and also reviews "positives, negatives, where we can improve, any discrepancy".
- **Inputs to the meeting:**
  1. **Registrations from the portal** ("the portal tells us how many").
  2. **The Wastage Book for the matching past day.** The menu repeats on a two-week cycle (**weeks 1 & 3 are the same menu, weeks 2 & 4 are the same**). For a week-4 Tuesday they look up the week-2 Tuesday: how many registered, how many ate, what was left over, what time it ran out. [00:39–01:08], [05:47–06:02]
  3. **The attendance register by weekday** (all Sundays together, all Mondays together…) to see the trend. [15:19–17:38]
  4. Known **events, exams, holidays** ("event at Burrito/Salad bar → cook less"). These are only known if someone brings them up in the meeting: *"We don't come to know… until we sit in the meeting."* [09:06–09:49]
- **Output:** a written **issue list per meal** (the Grocery Book page with BF / L / S / D columns), issued to the kitchen the evening before or that morning. [25:07–25:38]
- **The store step** between issue and kitchen: the storekeeper takes out the items and **cleans and sorts them** (stones and sticks in rice and dal). If impurities are found, they are weighed and reported back to the supplier. *"For 2 kg I got 50 g of stones… a 50 kg bag, just imagine."* [07:30–08:46]

### 2.2 How the Wastage Book works (the "Sat-1&3" / "Thu wk 1&3" pages you photographed)
[03:37–06:50]
- One page per menu day, with weeks 1 and 3 side by side.
- For each item it records: **raw material issued → cooked quantity → left over → % wasted**. There is also a **time column (when the item ran out)** and a **re-cook column** (how much extra was cooked, and what was left of that).
- Header: **Registration "32 + 5"** = regular + Jain. **Actual eaten "20 + 2 + 6 + 5"** = registered + Jain + unregistered + cash/paid.
- Bottom of page: **student wastage** (plate waste scraped into the bin) and kitchen wastage, weighed in kg (milk in litres).
- **What the time column is used for:** *"If it runs out at 1:30 we will re-cook; if it runs out at 2:20 we won't."* [06:32–06:50]

### 2.3 Cooking in batches and the rush
- Most items are **cooked in one go**. Only items that dry out on the counter (e.g. **poha**) are cooked in **two batches** (e.g. 3 kg as 1.5 + 1.5). [04:22–04:49], [09:59–10:30]
- He argued *against* cooking everything in batches, because *"student fluctuation is very high"*: you can't know whether the second batch will be needed. [10:37–11:27]
- **The rush is always at closing time.** Queues are longer on **aloo paratha / dosa days**. [11:39–11:51]
- **Checks every half-hour from about 1:45 (lunch).** For a meal closing at 2:30 (lunch) or 9:30 (breakfast), monitoring starts about 45 minutes before close. A second roti counter is opened during surges and closed when the crowd thins. [11:57–13:25]

### 2.4 The numbers he quoted
- **Breakfast is the lowest, about 50% of registrations on average** (*"it can go down or up depending on the item"*). [13:37–13:59]
- **Lunch is above 70% most days.** He read out the September lunch %: *70, 72, 74, 77, 66, 56, 78, 73, 87, 89, 79, 71, 79, 74, 75, 61, 78.* These **match the attendance register we transcribed**. [19:15–19:35]
- **Sunday-night paneer dinner: 92% turnout.** Wednesday paneer is not as high (*"another mess might be serving something"*). Turnout against registration is **highest on Sunday night**. [14:04–14:42]
- Worked example from the breakfast register: **Sunday 6 Sep, 257 + 10 registered, 50 ate = 18.7%.** He says *"not even next month – next week"* they will adjust using this. [16:56–17:48]
- Sundays are generally very low. Hackathons mean students sleep late, and exams push numbers down: *"This cannot be helped."* [18:38–19:06]
- Peak mess size: **300–350 at most; about 150 on Sunday biryani days** (the reason he gives for ERP being "too much" for them). [38:49–39:03]

### 2.5 Reusing leftovers
- **Leftover idli** is chopped, sautéed and served as an upma-style dish. [20:01–20:26]
- **Dosa batter** goes back into the fridge and is used the next day. Leftover batter can be turned into roti. [20:27–21:33]
- Breakfast parathas (e.g. aloo paratha) are served **without oil or ghee**; students add ghee themselves. [21:03–21:18]
- **Surplus milk** is set as curd the same night. Curd goes sour if it isn't used, so the milk has to be planned (3 days buttermilk, 3 days curd). [33:07–33:43]

### 2.6 The registers (what each book you photographed is for)
| Register | Kept by | Purpose |
|---|---|---|
| **Wastage book** (production sheets, week 1&3 / 2&4) | Kitchen + coordinator | Raw → cooked → left over → %, run-out time, re-cook, student wastage |
| **Attendance register by weekday** (Breakfast / Lunch pages) | Coordinator | Registered vs actually ate, by category, %, by weekday |
| **Grocery issue book** (3 pages, BF/L/S/D, "→ balance") | Storekeeper + **Bhavani** cross-checks | Daily issue per meal and the running physical balance |
| **Stock register** (per article) | Storekeeper | Receipts, issues, balance; **bought fortnightly** ("every 15 days") |
| **Vegetable register** (Sheet1) | **Adit Amma** + a cross-checker | Opening + purchase − issues = balance, physically verified daily. Vegetables arrive 2–3 times a week |
| **Milk / fruit / gas / electricity / water register** | Project team | Paneer is made in-house (tracks how much milk goes into how much paneer); curd; utilities |
| **Fridge temperature and cleaning sheets** | Project management team | Hygiene documentation on every fridge (Fridge 1/2/3) |

- **Cross-checking is "not to find fault"**: the person checking is paid less than the person being checked, and *"there is no hierarchy"*. [30:24–30:57]
- **Why electricity is tracked daily:** they spotted that **Wednesday consumption is much higher** (idli batter is ground that night). [35:06–35:45]
- **Digitisation:** staff are not "computer savvy". Soma / Vinod digitise from the books later. They **tried Zoho** for grocery prediction and dropped it: *"Prediction will be based on our data only… I want to remain close to the data."* He writes in the registers himself every day. [31:06–32:21], [38:40–40:22]
- **5-person project management team** (3 operator staff + 2 more) oversees documentation, hygiene and cleaning. There are **16 kitchen staff**. [28:38–29:12], [36:53–36:57], [42:15–43:16]
- The printer can't produce A3 sheets, which causes trouble with printing the register formats. [22:43–23:01]

### 2.7 Quality choices
- Spices are bought **whole** and ground on site or in front of him (haldi, dhaniya). Wheat is ground on site. [36:29–37:23]
- **Pink (rock) salt** only, no white salt. **Cold-pressed oils** (groundnut, sesame, mustard), and he visited the oil mill. [37:32–38:17]
- **Tasting team:** two tasters per shift (breakfast: 1 woman + 1 man, because women staff don't come in that early; lunch and snacks: 1 woman + 1 man; dinner: 2 men). No red chilli powder; only green chillies and dried red chillies, to control heat. [45:57–48:04]

### 2.8 Culture and change management (strong quotes for the report)
- The waste tracking started in **August**. At first staff *complained ("they are catching us")*. By **December**, on a team trip to his farm, *"one of the guys said actually wastage has reduced"*. [43:42–44:25]
- *"This is like a proposal. You follow this; if you find any problems come back to me… you may have a better option."* [44:36–44:52]

---

## 3. Kadamba Mess (the Prism team) – rules of thumb, not records

*Sources: Kadamba Mess.mp3 and IIIT Road 51/52/53. The speaker is the mess/floor manager. The Telugu translation is noisy, so this section is interpreted.*

### 3.1 How they decide quantities
- The **student committee** is given a menu; they choose and hand it back, and the operator follows it. [51: 00:30–00:42]
- **Quantities come from registrations**, split veg / non-veg (*"400 non-veg, 300 veg… we prepare accordingly"*). Breakfast works the same way. Decided **the day before**, from the **weekly menu**. [K 00:00–00:26]
- **Rule of thumb: cook 70% of registrations in the first batch.** *"If 100 register we prepare for 70 first… if you don't come, 30 portions are wasted."* The remaining raw material is kept ready and can be cooked in **10–15 minutes**. [K 01:02–01:22], [K 08:00–08:39]
- **Arrival pattern** as they describe it: 200–300 at the start → 300–400 by 8:30 → about 100 more → **100–150 in the last moments**. [K 01:22–01:43]
- They **watch the scan data live** (how many came, time left) and chefs cook more on request (*"wait 5 minutes"*). [K 01:48–02:39]
- **Portioning by grams:** 4 idlis ≈ 120 g raw per person. × 700 = about 84 kg batter. Sambar about 100 g per person. Ragi idli is cut back (less popular). White steamed idli is increased. [K 02:50–04:01]
- **No real forecasting.** Asked how they predict demand: *"We don't have that idea… some came and we did it, but they didn't come. It was wasted many times."* [K 07:39–08:00]
- **Pongal portions vary** (80–200 g per person); *"we eat by our mind"*. [K 32:22–32:46]

### 3.2 Waste
- Items that **move well**: puri, bonda, vada, idli. Items that get **wasted**: uttapam, "Chettinad" / set dosa. Upma (*"uggani"*) is mentioned as wasted. [K 04:47–05:18], [52]
- **Waste is recorded**, with example figures of **plain rice about 16 kg, flavoured rice about 16 kg, a food pan about 16 kg, dal about 23 kg**, and *"leave it 4 hours and it becomes 100 kg"* *(unclear)*. [K 06:09–06:31]
- **Where waste goes:** a dustbin; the garbage contractor takes it away. **No composting.** Cooked food keeps only 3–4 hours. [K 06:37–06:51]
- **Minimum waste is about 10 kg per meal** *(from clip 52, unclear)*.
- **Sambar was dropped from dinner.** A **student** complains: *"Till last month they served sambar daily, now removed completely… but they are taking more money from us."* The operator says the menu is decided by the students / committee. [K 26:48–27:47]

### 3.3 Registration system and students
- Registration closes **about 4 days in advance** ("weekly compulsory"), yet perishables are ordered **one day ahead** (meat, eggs, milk and paneer arrive daily; vegetables last 2–3 days; groceries are stocked weekly). The team **questioned why the cut-off is 4 days**. [K 12:05–12:25], [K 13:14–14:36]
- **A maximum of 5 cancellations** is allowed *(unclear)*. [K 15:39–15:44]
- The manager's view of no-shows: students register **even when away** ("even if you are in the village"), and a friend eats in their place. [K 16:05–16:31]
- **QR scanner failures:** when the system doesn't work, staff note down ID and name by hand. [K 16:39–17:18]
- **About 30–40 extra** is prepared on top of registrations for non-registered or paying students. **Biryani days: about 700 registered.** [K 17:22–17:54]
- **Late arrivals after 9:30** (and after the lunch close): *"We open the door again for 5–10 minutes."* On one day, **25 students came after close** for biryani. [K 21:35–22:23]
- **Staff meals:** 20–30 cooking and security staff eat from what is left, after students. [51: 19:39–20:03]

### 3.4 Operations
- **About 10 chefs**, with separate veg and non-veg chefs (names are garbled in the audio). [K 20:03–20:41]
- **Timeline:** staff arrive at **5:30 am**. **Live items (dosa, vada) start at 7:00**. Other items (sambar, upma) are cooked in bulk. Before food reaches the counter: **weigh → taste (salt) → temperature check → display**. **Food samples are kept for 72 hours** (another passage says 3 days) in the fridge, in case of food-poisoning complaints. [K 33:45–35:02], [K 23:07–23:26]
- **Complaints route:** director email → manager → a **WhatsApp group**. The "site team" (the facility / CDS side) reports to them. [K 24:00–25:15]
- **LPG shortage:** they cut back a little and bought some items from outside. [K 28:11–28:29]
- **Equipment:** the **bread grill / toaster is broken** (*"a student broke it"*), and there is no replacement yet. [K 29:36–30:45]
- **Water:** RO for cooking and drinking. **TDS readings are recorded.** Raw water is used only for cleaning. [K 36:30–37:08]
- **QC visits** from IIIT (faculty) check the store. There is "no backup" (they cannot keep excess stock). [K 33:29–33:41]

---

## 4. The Vijayalakshmi Caterers mess (IIIT Road 54 & 55) – mess name to be confirmed

### 4.1 Contract and cost (clip 54)
- The company won a **tender**. The institute publishes the project details and cost. **Base rate about ₹80 per plate; they bid about ₹60** under tender conditions, and the closest or lowest bid is selected *(figures unclear)*. [00:40–01:31]
- **Paid monthly**, as a lump sum based on the **number of plates**, with deductions. [01:34–01:54]
- **Food is cooked in an off-site kitchen** about **40 minutes away (near the airport)** and **transported in insulated boxes** at a controlled temperature. [02:22–03:03]

### 4.2 Planning rule (clip 54)
- **They do NOT cook for 100% of registrations.** *"We used to cook for 70%; now 80%… if more than 70% come, the extra comes from the kitchen within 30 minutes."* They check **every 30 minutes**, e.g. *"projection for 300, 150 have come, this much food left"*. [03:32–04:46]
- They claim **Kadamba gets 90–95%** of registered students, versus 60–70% for them (85–90% on non-veg days) *(unclear)*. [05:34–06:00]
- **Leftovers:** some go back to the kitchen and are reused; the rest is thrown away. *"Many people are not coming for breakfast."* [06:47–07:12]
- The manager wants to **tune curry-to-rice/roti ratios** (they eat more curry and less rice here) and says the **menu is decided by the student community**. [08:30–09:28]

### 4.3 Manager interview (clip 55)
- The manager has been there **about 1 month**. Cooks start **around 5–5:30 am**, and food should be ready by **6:30**. Breakfast ends at **9:30**, with the counter inspected **around 9:20–9:30** and a buffer kept. [00:23–02:13]
- **Peak crowd:** breakfast **8:30–9:00+**, lunch around **1:30**. People come in waves of 30–35 every 10 minutes. [01:11–01:45]
- **Weekends are lower**, and turnout is **under 70% of registrations**, so **food is prepared for 70–80%**. [02:16–02:49]
- **Menu:** the manager wants a say, e.g. better dish pairings (raj kachori with chana sabzi, pav bhaji-style combos). *"It's good if you increase the flexibility."* [03:06–04:00]
- **Paneer supply problems:** Amul, then Heritage, both with complaints; now switching to **Milky Mist**. [05:13–05:42]
- **Complaints:** CDS team → manager → kitchen team → MD. [06:58–07:20]
- **Aloo paratha tastes best eaten straight away**, yet it is cooked 1–2 hours before service. [07:32–07:47]

### 4.4 Reporting chain (clip 50)
- Staff → **Supervisor** → **Manager** → **Operations Manager** → (then the director) *(clip cut off)*.

---

## 5. Cross-checking against the data we hold

| Claim in the recordings | What the data says | Verdict |
|---|---|---|
| Yuktahar: "breakfast is about 50% of registrations" | Yuktahar breakfast register, Sept: **18–40%** (average about 28% across the 13 days where the % is known) | **Lower than he believes.** 50% is optimistic, and a good point to raise with him |
| Yuktahar: lunch "above 70% most days" | Lunch register: **56–89%**, 15 of 20 days ≥ 70% | Confirmed |
| Kadamba: "cook 70% in the first batch" | April Kadamba breakfast data: **37.1% availed** overall (veg 32%, non-veg 49%) | **70% is about double what shows up.** Structural over-preparation at breakfast |
| Kadamba: "last-moment rush of 100–150" | April data: **26.5% of all breakfast scans fall between 9:15 and 9:30**, peaking around 9:29 (about 9 per minute per day) | Confirmed |
| Kadamba: "students register even when away" | April data: **registrations flat at about 1,070/day every weekday, Sunday included**, while turnout falls from 42% (Tue) to 27% (Sun) | Consistent: registration is not a daily decision |
| Vijayalakshmi: "Kadamba gets 90–95%" | April data: Kadamba breakfast **37%** | Wrong for breakfast (possibly true for lunch or dinner, but we have no data) |
| Yuktahar: "dosa / aloo paratha days have longer queues" | Thursday 3 Sep (aloo paneer methi paratha) breakfast: 77 ate (28%). Attendance register: 110 (40%) | Mixed; also the two books disagree |
| Yuktahar: weeks 1&3 and 2&4 share a menu | Production sheets are headed "Sat-1&3" and "Thu wk 1&3" | Confirmed |

---

## 6. What this means for the systems map (early reading)

1. **Registration is not a demand signal.** It is a standing booking (at Kadamba, a 4-day cut-off and ~5 cancellations; registrations are flat all week). Actual breakfast demand is about 35–40% of it, and every operator plans around a guessed conversion factor (Yuktahar 50%, Kadamba 70%, Vijayalakshmi 70–80%).
2. **Each operator runs its own balancing loop** (cook part of it → watch the counter → top up in 10–30 minutes). How good that loop is varies a lot: Yuktahar has a documented feedback loop (wastage book, time-out column, weekday register, twice-daily meetings); Kadamba runs on rules of thumb and experience; Vijayalakshmi on 30-minute checks with a delivery lag from the off-site kitchen.
3. **Information that arrives too late:** exams, events and holidays reach the kitchen only if someone mentions them in the meeting. Nothing formal feeds this in from the institute.
4. **The closing-time surge** (last 15 minutes) is the same everywhere. It drives both kinds of failure: shortages (late re-cooks, opening the door again) and waste (cooking extra "just in case").
5. **Menu ownership is spread out:** students or the committee pick the menu, operators see the waste, and the feedback between them is weak (the dinner sambar case, the uttapam/set dosa waste, the manager wanting a say).
6. **Waste disposal is a dead end:** a dustbin to the garbage contractor, no composting, and only 3–4 hours before cooked food is unusable.
7. **People and culture matter:** Yuktahar's cut in waste came from building a routine and staff buy-in (August → December), not from software (Zoho was dropped).

---

## 7. Open questions to verify or ask next time
- Which mess do IIIT Road 54 and 55 come from (Vijayalakshmi Caterers)?
- Kadamba: the exact cancellation rule ("maximum 5"?) and why registration closes 4 days ahead.
- Kadamba waste figures (16 kg / 23 kg / "100 kg"): per meal or per day? Can we see the waste record?
- Yuktahar thinks breakfast turnout is 50%, but its own register shows 18–40%. Show them this.
- The ₹60 vs ₹80 plate rate and how deductions work: ask CDS for the tender terms.
- Does the April data exist for lunch and dinner, and for Yuktahar? (The file we have is Kadamba breakfast only.)
