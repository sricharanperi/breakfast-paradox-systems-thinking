# Mess Operations Evidence Brief: field visit data, registers, recordings, CDS breakfast records

**Collected:** September 2026 field visits by the team (Yuktahar and Kadamba messes, plus a third mess run by Vijayalakshmi Caterers), plus one records dataset from the CDS team.
**Logged:** 2026-09-27.
**Status:** the project's first *operations-side* primary evidence from the mess operators themselves, and its first *record-level* attendance data. It supersedes several claims that Phases 1 and 2 could previously support only with student recall or with the CFS Chair's single-sourced account.

> **Superseded in part (2026-09-27):** the team's first-hand field account (`2026-09-27_team-field-account-evidence-brief.md`, §3 correction table) upgrades or corrects several Kadamba and Yuktahaar details below: the 70% rule is now observer-verified; the Kadamba kg waste figures are withdrawn in favour of "5–10% daily"; staff and extra diners are 30–50 outside people plus about half the staff; the project management team is 2; the cross-checker is Ajita. Where the two briefs conflict, Brief #2 wins. The record-level data here (§1) is unaffected.

This file is the canonical summary. Every downstream revision should cite facts from here (or from the raw files listed in §0), using the project's confidence vocabulary (D-35):
- **confirmed (records):** read directly off a register, a photographed form or the CDS dataset.
- **confirmed (operator, clear audio):** stated clearly on the Yuktahar recording, which is mostly English.
- **single-sourced (operator, noisy audio):** stated in the Telugu-heavy Kadamba or Vijayalakshmi recordings. The machine translation may garble sentence detail but not the gist.
- **candidate:** an inference drawn by combining sources, not stated anywhere directly.

---

## 0. Raw sources (all under `Observation images/`, repo root)

| Source | What it is | Processed output |
|---|---|---|
| `Photos/` (26 phone photos, 13:05–13:06 on 26 Sep 2026) | Yuktahar mess registers and forms, photographed page by page | `Extracted Data/Yuktahaar_Mess_Observation_Data.xlsx` + `Extracted Data/csv/*.csv` (22 tables, with a per-row read-confidence column) |
| `Yuktahar Mess.mp3` (49:48) | Yuktahar site head / project lead walking the team through every register | `Extracted Data/Transcripts/raw_machine_translation/Yuktahar Mess.en.txt` |
| `Kadamba Mess.mp3` (37:24) + `IIIT Road 51/52/53.m4a` | Kadamba floor/mess manager ("the Prism team"). The IIIT Road clips are cuts of the same interview | `…/Kadamba Mess.en.txt`, `…/IIIT Road 5x.en.txt` |
| `IIIT Road 54.m4a`, `IIIT Road 55.m4a` | Third mess, operator **Vijayalakshmi Caterers**: owner/staff (54) and the mess manager (55) | `…/IIIT Road 54.en.txt`, `…/IIIT Road 55.en.txt` |
| `IIIT Road 50.m4a` | Short clip on the operator's reporting chain | `…/IIIT Road 50.en.txt` |
| `april-data.xlsx` | CDS team export: **Kadamba breakfast, 1–30 April 2026**, one row per registration | `Extracted Data/Kadamba_April2026/*` |
| Interpreted synthesis of all recordings | Per-recording summary with timestamps, cross-checked against the data | `Extracted Data/Transcripts/Recordings_Synthesis.md` (**read this for timestamps and fuller detail**) |

Transcription: Whisper large-v3, run locally with Telugu→English translation. The Yuktahar recording is reliable. The Kadamba and Vijayalakshmi recordings have the gist right with noisy sentences, and every number from them that needs audio verification is marked *(unclear)* in the synthesis.

---

## 1. Record-level attendance data (new category of evidence; this project previously had none)

### 1.1 Kadamba breakfast, April 2026 (CDS export). Confirmed (records)
- **32,162 registrations; 11,941 availed (37.1%); 20,221 no-shows (62.9%).** By type: veg 22,715 registered / 32.4% availed; non-veg 9,447 / 48.5%.
- **Registrations are flat at about 1,070 per day on every weekday, Sunday included** (range 928–1,123), while **turnout varies by weekday**: Tue 42.1%, Mon 41.1%, Thu 39.5%, Fri 37.5%, Wed 37.0%, Sat 34.8%, **Sun 27.3%**. Registration therefore does not track the daily decision to eat.
- **Arrival curve:** scans begin at about 7:28–7:30 (a few from 6:38, likely staff or early service), and the median scan is 8:51–9:11 depending on weekday. **26.5% of all scans fall in 9:15–9:30 and 13.5% in 9:00–9:15.** The per-minute rate climbs steadily to about 9 scans per minute per day at 9:29. Service closes about 9:35–9:45, with the latest scan at 10:07. There is no batch or bulk-marking artifact: at most 2 scans share a second, and 82 duplicate-second pairs out of 11,941.
- **What the export lacks:** student ID, meal type (inferred as breakfast from the timestamps), lunch/dinner, quantities, waste. It cannot show which individuals skip repeatedly.
- **Resolves / updates:** the "~30% gap unverified" item (for Kadamba breakfast the gap is **~63%**, not ~30%); the CFS Chair's "breakfast 35–40%" figure (**now record-confirmed for Kadamba, April**); the "crowd-peak curve shape/timing unobserved" item (**now measured**: one continuously building crowd cresting just before close, matching the D-10 reconciliation).

### 1.2 Yuktahar attendance register, September 2026 (photographed). Confirmed (records)
Columns: registered regular + Jain; ate as registered regular, registered Jain, unregistered, paid, F/S (faculty/staff), advance, events; total; %.
- **Lunch, 1–20 Sep:** 56%–89% (15 of 20 days ≥70%). The written totals match their components on every row.
- **Breakfast, 1–20 Sep:** **17.7%–40.2%** on the 13 days with a legible %, mean about 28%. Several rows are partly hidden by a hand in the photo.
- Sunday breakfasts are among the lowest: 18.7%, 17.9% and 24.1% as written (6, 13 and 20 Sep). The single lowest day is Monday 14 Sep at 17.7%. (Corrected 2026-09-27: an earlier version of this line wrongly attributed 17.7% to a Sunday.) Registrations for Yuktahar breakfast run 228–404 per day.
- File: `csv/01_Attendance_Lunch.csv`, `csv/02_Attendance_Breakfast.csv`.

---

## 2. How quantities are actually decided (the kitchen-side mechanism the project never had)

### 2.1 Yuktahar (operator: ABC Hospitality Services). Confirmed (operator, clear audio) + confirmed (records)
- **A planning meeting twice a day:** the first-half meeting fixes tomorrow's breakfast and lunch issue, and the second-half meeting fixes snacks and dinner. Attendees: storekeeper, coordinator, kitchen staff. They also review positives, negatives and discrepancies.
- **Inputs:**
  1. portal registrations;
  2. the **Wastage Book** entry for the *matching past day* (the menu repeats with **weeks 1 & 3 identical and weeks 2 & 4 identical**, so a week-3 Thursday looks up the week-1 Thursday);
  3. the **attendance register grouped by weekday**;
  4. events, exams and holidays, **but only if someone brings them up in the meeting**: *"We don't come to know until we sit in the meeting."* There is no formal feed from the institute.
- **The Wastage Book** (photographed: "Sat-1&3" 13/6/26 and 2?/6/26; "Thu wk 1&3" 03/9/26) records per item: raw issued → cooked qty → left over → % waste, **run-out time**, re-cook qty, plus registered (regular + Jain), actual eaten by category, student (plate) wastage and kitchen wastage. It is **used as a rule**: *"If it runs out at 1:30 we re-cook; if at 2:20 we don't."*
- **Output:** a per-meal issue list in the **Grocery Book** (BF / L / S / D columns → total → running balance). The store then **cleans and sorts** the issued grains (stones and sticks are weighed and reported back to the supplier).
- **Cooking:** mostly one batch. Only items that dry out (poha) are cooked in two. The operator argued against general batching because "student fluctuation is very high." Monitoring runs **every 30 minutes from about 45 minutes before close**, a second counter opens during surges, and **the rush is always at closing time**, with longer queues on aloo paratha and dosa days.
- **Operator's belief vs. their own records:** he says breakfast turnout is **"about 50%"**. His own September register shows **18–40% (mean ~28%)**. Lunch "above 70% most days" is confirmed by the register. Sunday-night paneer dinner reaches 92% (his figure).
- **Leftover reuse:** idli is chopped and sautéed into an upma-style dish; dosa batter goes back into the fridge; surplus milk is set as curd overnight; paneer is made in-house (the milk-to-paneer yield is tracked).
- **Procurement:** groceries are bought **fortnightly** (stock register), vegetables arrive **2–3 times a week**, milk daily. Spices are bought whole and ground in-house; rock salt and cold-pressed oils are used.
- **Staffing and governance:** 16 kitchen staff; a 5-person project management team; paired cross-checking ("not to find fault", "no hierarchy"); tasting pairs every shift; hygiene sheets on every fridge (temperature 3×/day, cleaning daily). Digitisation happens later, by the office. **Zoho was tried and dropped:** *"prediction will be based on our data only… I want to remain close to the data."* Waste tracking started in **August** (last year), staff first resisted ("they are catching us"), and by **December** staff themselves reported waste had fallen.
- **Records seen for 18-9-26:** Grocery Book header BF 265+14, L 338+15, S 7+0, D 237+14. The Dal Toor stock register and the Grocery Book agree (4.5 kg issued, 49.45 balance).

### 2.2 Kadamba (the "Prism team"). Single-sourced (operator, noisy audio)
- **Quantity rule: prepare about 70% of registrations in the first batch.** The remaining raw material is kept ready and can be cooked in **10–15 minutes** on request from the counter. Veg and non-veg are planned separately from registrations. Portioning is by grams (about 120 g raw per 4 idlis per person, about 100 g sambar).
- **No forecasting method:** *"We don't have that idea… it was wasted many times."* They watch live scan counts.
- **Against the records:** 70% first batch vs **37% actual** Kadamba breakfast turnout (April) means structural over-preparation at breakfast of roughly 1.9×, before any top-up.
- **Waste:** recorded. Example figures quoted: plain rice ~16 kg, flavoured rice ~16 kg, a food pan ~16 kg, dal ~23 kg *(unclear whether per meal or per day)*. Disposed of **to a dustbin collected by the garbage contractor. No composting at Kadamba.** Cooked food is usable for only 3–4 hours. Items that consistently waste: uttapam, set/"Chettinad" dosa, upma (uggani). Items that move: puri, bonda, vada, idli.
- **Registration and perishables mismatch:** registration closes **about 4 days ahead** ("weekly compulsory"), while meat, eggs, milk and paneer are ordered **one day ahead** and vegetables last 2–3 days. The team explicitly challenged the 4-day cut-off. **Max ~5 cancellations** *(unclear)*.
- **Manager's mental model of no-shows:** students register even when away ("even if you are in the village") and a friend eats in their place.
- **Other:** about 30–40 extra portions are prepared for paying or unregistered diners; biryani days reach ~700 registrations; **late-comers after the 9:30 close get the door reopened for 5–10 minutes** (25 came after close on one biryani day); staff (20–30 cooking and security) eat from what is left after students; QR scanner failures are handled by writing ID and name by hand; complaints run director email → manager → WhatsApp group; the site / CDS-side team reports into that group; an LPG shortage was handled by cutting quantities and buying outside; the **toaster/grill is broken**; food samples are kept 72 h; TDS records are kept for water.
- **Menu dispute (student voice, same recording):** dinner sambar was dropped *"while they are taking more money from us"*. The operator says students or the committee decide the menu.

### 2.3 Vijayalakshmi Caterers mess (IIIT Road 54/55). Single-sourced (operator, noisy audio)
> **Superseded in part (2026-09-28):** Evidence Brief #3 (`2026-09-28_bakul-niwas-evidence-brief.md`, §2 conflict table C1-C11) confirms this mess is **Bakul Niwas**, moves the kitchen to **Hafizpet (~8 km; ~20 min early, ~40 min normally)**, replaces "70% now 80%" with 70-80% by item adjusted weekly from historical attendance, moves the breakfast peak to 8:00-8:30, and reports payment on plates **served** (flagged, not resolved). Where the two conflict, Brief #3 wins.

- Won a **tender**. Plate rate about **₹80 base, ₹60 bid** *(unclear)*. **Paid monthly as a lump sum on plates**, with deductions.
- **Food is cooked off-site**, about 40 minutes away near the airport, and transported in insulated boxes. **Candidate:** this is the off-site kitchen that the CDS posters and the CFS Chair describe for **Bakul/Palash**. The mess name was not stated on tape, so this needs confirmation.
- **Prepares for 70% of registrations (now 80%)**, checks every 30 minutes, and the extra arrives from the kitchen **within 30 minutes**. Reports turnout under 70%, weekends lower, non-veg days 85–90%. Claims Kadamba gets 90–95% *(contradicted by the April records for breakfast)*.
- The manager (1 month in the role) wants menu input and pairing flexibility. Paneer supply has had problems (Amul → Heritage → Milky Mist). Complaints go CDS team → manager → kitchen → MD. Peaks: breakfast 8:30–9:00+, lunch ~1:30, arriving in waves.

### 2.4 Reporting chain (IIIT Road 50). Single-sourced
Staff → supervisor → manager → operations manager → (director).

---

## 3. What this changes, mapped to the project's existing open items and findings

| Existing item (MASTER_CONTEXT §9 / deliverables) | What the new evidence does |
|---|---|
| "Mess-committee / vendor-side interview not conducted" | **Largely closed for operations.** Three operators interviewed; Yuktahar walked through all its records. Still open: CDS Chair (Giri), contract terms. |
| "Exact mechanism connecting weekly stock assessment to per-item preparation quantity" | **Answered per mess.** Yuktahar: matching-week wastage book + weekday attendance register + twice-daily meeting. Kadamba: fixed ~70% of registrations + live top-up. Vijayalakshmi: 70–80% + 30-minute top-up from off-site. None is calibrated to actual breakfast turnout. |
| "~30% registration-to-attendance gap unverified" | **Superseded:** Kadamba breakfast gap ~63% (April records); Yuktahar breakfast gap ~72% (Sept register). Lunch gap ~10–44%. The "30%" was a lunch-like figure. |
| "Scope of CFS Chair's 35–40% breakfast figure" | **Confirmed for Kadamba (37.1%, April 2026)**; Yuktahar lower (~28%, Sept). |
| "Direct observation of a live breakfast window not conducted" | **Substantially answered by 11,941 timestamped scans.** Direct observation of waste disposal is still not done. |
| "Composting absorbs the physical surplus" (Task 8, D-45 absorption layer) | **Contradicted for Kadamba:** dustbin → garbage contractor, "no composting". Yuktahar reuses leftovers (idli, batter, milk) but its disposal route was not stated. The absorption layer needs revising: at Kadamba surplus is absorbed by staff eating it, late-comer top-ups and the bin, not composting. |
| "Aggregate-only feedback / no one sees the gap" (RC2/RC3, D-45) | **Refined:** the gap *is* measured, locally and repeatedly, by the operator (wastage book, weekday register, % columns). What is missing is (a) a route from that measurement into registration or billing policy, and (b) the institution's awareness that operators hold this data. Yuktahar's head even misremembers his own breakfast % (50 vs 28). |
| T-4 procurement lock (Tasks 4, 7) | **Refined:** the T-4 lock applies to *registration*. Actual procurement is mixed: groceries fortnightly, vegetables 2–3×/week, perishables T-1. The binding constraint on waste is **cooked food prepared at a fixed ratio to registrations**, not raw procurement. Raw surplus is largely recoverable; cooked surplus is not (3–4 h life). |
| Skip Meal "near-zero uptake" | Not directly addressed. Kadamba mentions "max 5 cancellations" *(unclear)*. Still open. |
| Menu rotation (loop L4 / B3) | **Confirmed mechanism:** a 2-week cycle (weeks 1&3 / 2&4) is exactly what makes the Wastage Book lookup possible. Students or the committee choose the menu; operators observe waste per item but have weak influence (the dinner sambar case, the Vijayalakshmi manager asking for menu input). |
| Crowd peak / closing rush | **Confirmed by records and all three operators.** It drives both shortages (re-cook, door reopened) and "just in case" over-preparation. |
| Bakul/Palash off-site kitchen (braindump #2) | **Candidate match** with the Vijayalakshmi Caterers off-site kitchen. |

## 4. New stakeholders or roles to consider (Phase 1 maps)
- **Mess operator site head / project lead** (Yuktahar, ABC Hospitality Services): owns a documented planning system; high local power over quantities; no power over registration rules.
- **Operator floor/mess manager** (Kadamba "Prism team"; the Vijayalakshmi mess manager).
- **Storekeeper**, **coordinator**, **cross-checkers** (Bhavani; Adit Amma for vegetables), **tasting pairs**, **project management team (5)**, **kitchen staff (16 at Yuktahar; ~10 chefs at Kadamba)**, **supervisor → manager → operations manager → MD/director** chain.
- **Suppliers** (grocery, vegetables, milk; paneer brands Amul/Heritage/Milky Mist; oil mill), **garbage contractor** (waste exit at Kadamba), **the CDS "site team"** that relays complaints into the operator's WhatsApp group.
- **Vijayalakshmi Caterers** as a distinct vendor with an off-site kitchen and a transport link.

## 5. Evidence limits (state these wherever these facts are used)
- The April records cover **Kadamba breakfast only**. There are no lunch/dinner records, and no Yuktahar/Bakul/Palash records beyond Yuktahar's September photos.
- The Yuktahar September registers are photographs; some breakfast rows are hidden.
- The Kadamba and Vijayalakshmi numbers (70%, 16 kg, 23 kg, ₹60/₹80, 5 cancellations) come from noisy machine translation. Check them against the audio before any is used as a headline number.
- One visit per mess. The operators are describing their own practice, which carries self-presentation bias; e.g. the Yuktahar head's 50% claim vs 28% in his own records.
