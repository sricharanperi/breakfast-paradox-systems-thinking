# Primary Research — Student Self-Account & Mess System Overview

**Source:** the user (team member, IIIT Hyderabad student), dictated/verbal account, transcribed
and organized here without adding or inferring facts. Where the original statement was unclear or
internally inconsistent, that is flagged explicitly rather than resolved.

**Date:** 2026-09-03
**Type:** Self-report interview + general campus-system knowledge (the respondent is both a
stakeholder — a habitual breakfast-skipper — and a general informant on how the system works)

**Attempted supplementary source:** `dining.iiit.ac.in` (corrected by user from an initial
"mess.888.ac.in" / "mess.iiit.ac.in" guess — likely a mishearing of "IIIT" as "888" in dictation).
WebFetch could not retrieve content: the portal sits behind IIIT's CAS single sign-on
(`login.iiit.ac.in/cas`) and appears to be a JS-rendered app, so an unauthenticated fetch returns
an empty shell. Not attempting to use the user's institutional credentials to log in. If the user
browses the portal themselves while logged in and pastes/screenshots specific pages (menu
calendar, pricing table, any vendor/admin info), that becomes usable primary data.

---

## 1. The messes — ⚠️ contains an unresolved contradiction, do not treat as settled

Three messes were named explicitly: **Kadamba** (K-a-d-a-m-b-a), **Palash**, **Bakul**.
Non-vegetarian food is served at Kadamba and at Bakul.

**Contradiction:** the respondent twice referred to "all four messes" / "there are four messes"
elsewhere in the same account, but only ever named three. It's unclear whether there's a fourth,
unnamed mess, or whether "Yuktahar" (see below) is actually the fourth mess's name rather than a
vendor/kitchen name, or whether this was simply a slip. **Needs direct confirmation from the
user/team before the Stakeholder Map or System Context Brief states a mess count as fact.**

A web search (not the portal itself, which is login-gated) turned up an external claim of "two
vegetarian messes and one non-vegetarian mess" (i.e. 3 total) — but that doesn't cleanly match the
user's account either (user says 2 of the 3 named messes, Kadamba and Bakul, serve non-veg, with
only Palash veg-only). This external claim is **not confirmed** and is noted only so it isn't
silently used later — treat the actual mess count/names as `[NEEDS DATA — confirm exact number
and names of messes]` until the user settles it directly.

## 2. Vendor structure

- Palash and Bakul share the same vendor.
- Food for Bakul is cooked at Palash and physically shifted/packed over to Bakul, because Palash
  itself cannot serve non-veg; Bakul then serves the Palash-cooked veg food plus non-veg on top.
- Reason given: non-veg eaters are a majority on campus; originally only Kadamba served non-veg,
  and when Kadamba reached capacity there was no non-veg fallback — Bakul was created to cover
  that overflow.
- "**Yuktahar**" was mentioned as somewhere food is "cooked... separately" alongside Kadamba and
  Palash — `[NEEDS CLARIFICATION — is Yuktahar a vendor/kitchen name (e.g. Kadamba's caterer), or
  a fourth mess? The sentence structure in the original account is ambiguous.]`

## 3. Real timings (replaces assumed/puzzle timings for the actual System Context Brief)

- Breakfast: **7:30–9:30 AM**
- Lunch: **12:30–2:30 PM**
- Dinner: **7:30–9:30 PM**
- Classes start **8:30 AM**; last class ends **6:40 PM**; class lunch break is **1:00–2:00 PM**.
- Important nuance the puzzle narrative doesn't capture: **classes are not continuous** — most
  students have relatively few classes per day, so not everyone has an 8:30 AM class on a given
  day. The respondent personally has an 8:30 AM class only **twice a week**.

## 4. Registration / QR system (Process Trace material)

- All mess activity runs through the official IIIT-H mobile app (referred to by the respondent as
  "Triple IT" / transcribed as "Triple ID" — the institute's own app, which also carries
  attendance, timetable, assignments, transcripts, credits, leave status, sports attendance, and
  courier tracking).
- Within the app's Mess section: a personal QR code, today's meal status per meal
  (missed/attended/upcoming/ongoing), a monthly view of registrations, per-day meal pricing, and a
  preference toggle for registration-reminder emails.
- **Booking:** a calendar view shows each day's menu per mess; clicking a date/menu lets a student
  register for a specific mess for a specific meal. (Respondent described this as effectively
  random/first-come unless actively chosen — `[NEEDS CLARIFICATION — respondent said "if it is
  randomly allocated," suggesting registration may sometimes be auto-assigned rather than always
  actively chosen; not fully clear from the account]`.)
- **Cancellation:** capped at **5 cancellations per meal-type per month** (e.g. 5 breakfast
  cancels/month, 5 dinner cancels/month) — described as the "standard limit."
- **Billing mechanism — structurally important:** billing is monthly and tied to the number of
  registrations, not attendance. This is a more precise mechanism than the fictional puzzle's
  vague "already paid the mess fee" framing — it explains why an unused, uncancelled registration
  still costs money regardless of whether the student shows up.
- **QR use at the mess:** each student sets a passkey in the portal to get their QR; the QR is
  scanned at the mess entrance to receive a plate. Veg/non-veg plates are kept separate and matched
  to the student's registration type. The QR can be reset at any time.
- **Walk-in to a different mess than registered:** if a student shows up at a mess other than the
  one they registered for, mess staff can rescan and reassign the QR to that mess on the spot.
- **Mess-full fallback:** if a mess's registration cap for that slot is reached, a student who
  didn't register can pay the vendor directly on the spot and eat — at a higher cost than the
  standard registered price.
- **Guests:** relatives, parents, friends, and non-student campus affiliates (e.g. people
  associated with the Center for Innovation & Entrepreneurship, researchers/job-holders working on
  campus) can pay the vendor directly, buy a QR, and eat, subject to registration-count
  availability.
- **Informal secondary market — "Mess Cell" WhatsApp group:** students who've registered for a
  meal they know they won't eat post in a campus-wide WhatsApp group (e.g. "Sell Kadamba veg"),
  negotiate a price privately, and transfer the QR/registration to a buyer for that meal. Described
  by the respondent as common and functioning smoothly for them personally; they note it's
  theoretically possible for someone's QR to be used without their knowledge if never reset/sold
  deliberately, though this hasn't happened to them.
- Illustrative real anecdote directly from the respondent: **"Kadamba veg breakfast costs around
  ₹48 and I book it every day and never avail it."** — a real, first-person instance of the
  register-but-never-attend pattern the puzzle describes, with a real price point attached.

## 5. Other real food/dining options on campus

- **Vindhya canteen** — open in the afternoon (exact hours not stated —
  `[NEEDS DATA — confirm Vindhya's actual operating hours]`).
- **Juice canteens** — open mornings, for juice/fruit.
- **Delivery apps (Swiggy, Zomato, Blinkit, etc.)** — orders accepted campus-wide from morning
  until 11 PM; delivery riders are **not allowed inside the gate**, so the student must walk out to
  the gate to collect the order themselves, any time up to 11 PM (food can then be eaten after
  that, inside).

## 6. Stakeholders named or implied (Stakeholder Map material)

- Mess vendors/contractors (per-mess; Kadamba's and Palash/Bakul's are distinct)
- Mess committee — decides the menu roughly one month in advance, incorporating student input
- Possibly the academic/timetable office — respondent's own sentence trailed off incomplete
  ("mess arts are decided by the mess committee by also taking the opinion of students... I think
  even academic office has the..." — `[NEEDS CLARIFICATION — what role, if any, does the academic
  office actually play in mess decisions?]`)
- Warden / hostel affairs office — named as a stakeholder category by the respondent, no specifics
  given on their actual role in mess matters
- Mess serving and cleaning staff — notable detail: **they eat the mess food themselves after
  student serving hours end**, and the respondent believes menus are planned with this in mind
- Guest diners: relatives/parents/friends, CIE-affiliated people, working professionals/researchers
  on campus
- The informal "Mess Cell" WhatsApp community — a self-organized, unofficial secondary market
  among students themselves, not an official system component but a real, active part of how the
  system actually functions
- Delivery riders (Swiggy/Zomato/Blinkit) — gate-restricted, same friction point the course's own
  "11 O'Clock Cliff" puzzle (a different team's problem) describes

## 7. Respondent's own breakfast-skipping account (Mental Model layer — ONE respondent only, not yet a pattern)

Direct first-person reasons given, kept as close to original wording as possible:
- Practices intermittent fasting; does not want to eat breakfast as a personal dietary choice.
- Habit formed years ago — used to cook their own breakfast, stopped cooking, found preparing/
  eating breakfast "felt like a time waste in the morning," shifted to eating more at lunch instead.
- When living in the hostel specifically, mess breakfast quality was poor, which reinforced skipping.
- Sleeps very late at night, making a 7:30 AM wait difficult.
- Has an 8:30 AM class only twice a week; on those days wakes at 8:00, rushes to get ready, no time
  to eat.
- On non-class mornings, despite theoretical motivation to walk to the mess, "I don't usually see
  the mess" even when it's in the same hostel — i.e. lack of visibility/environmental cue, not
  just willpower.
- Social factor: few friends join for breakfast specifically, more join for lunch — meal
  companionship pulls attendance toward lunch over breakfast.
- Two contrasting sub-groups mentioned (general observation, not the respondent): students who go
  to the gym tend to wake early and eat breakfast deliberately for their diet/fitness goals; and a
  separate group who simply have a stable personal routine of never skipping the morning meal.

**Caution for later deliverables:** this is rich, real, first-person data, but it is currently
**one respondent's account**. The Iceberg Model's "Pattern" layer needs more than one person's
experience to claim this is a widespread pattern rather than an individual habit — additional
interviews with other students (a mix of habitual skippers and non-skippers) are still needed
before generalizing.

## 8. Open items — confirm before these get baked into any deliverable

1. ~~Exact number and names of the messes~~ — **RESOLVED 2026-09-03**: 4 messes confirmed —
   Kadamba, Palash, Bakul, **Yuktāhār**. See §9 and `../screenshots/analysis.md`.
2. ~~What "Yuktahar" actually is~~ — **RESOLVED**: a real fourth mess, confirmed by both the user
   directly and the portal's own capacity/rates tables (also has a Jain-food variant).
3. Whether mess registration is ever auto/random-assigned vs. always actively chosen —
   **PARTIALLY RESOLVED**: the portal's Settings page has a "random allocation" email preference
   ("sends an email with meals if you've been randomly allocated"), confirming random allocation
   is a real system feature. Mechanism/trigger for *when* allocation happens automatically vs.
   student-chosen is still `[NEEDS DATA]`.
4. ~~The academic office's actual role~~ — **RESOLVED 2026-09-03**: the academic office has **no
   say** in mess timings or hostel matters. Mess-related decisions are made by the Mess Committee;
   the Warden handles vendor management and any changes to the mess. See §9.
5. Vindhya canteen's actual operating hours — still `[NEEDS DATA]`.
6. Any additional respondents beyond this one team member — still `[NEEDS DATA]`, still needed to
   check whether §7's breakfast-skipping reasons generalize.
7. **New from screenshots (2026-09-03):** what the calendar's "S" meal slot is (possibly Snacks,
   unconfirmed); why Bakul's registered-to-capacity ratio (116/700) is so much lower than
   Kadamba's (722/1200); whether/how the third-party auth-key API (Settings page) is actually used
   by students.

## 9. Follow-up clarifications from the user (2026-09-03, same day)

- **Warden's role, confirmed:** wardens take care of the mess, arrange the "largest statistical
  things" (unclear exact meaning — `[NEEDS CLARIFICATION]`), handle vendor management, and are
  the ones who make any changes regarding the mess. `[Source: Interview, 2026-09-03]`
- **Academic office's role, confirmed:** no say in mess timings or hostel matters at all —
  everything is decided by the Mess Committee itself. `[Source: Interview, 2026-09-03]`
## 10. Follow-up, round 2 (2026-09-09/10 dictation, same respondent)

- **Bakul's low uptake — respondent's own explanation (a hypothesis, not independently verified):**
  Kadamba is the established "go-to" mess — larger, and its food is well-liked. Bakul is a
  comparatively new mess, set up in a converted warehouse (cleaned, tables and a serving counter
  added) specifically because non-veg eaters were judged to be the majority and Kadamba alone
  couldn't cover non-veg demand once it hit capacity. Bakul's non-veg is cooked separately there;
  its veg food is prepared at Palash and physically carried over. The respondent attributes both
  Bakul's lower admin-set capacity and its lower student registration numbers to this
  newer/secondary status. **Caveat:** capacity (an admin-set number) and registration uptake
  (a student-choice number) are mechanically different things being explained by the same story
  here — worth independently checking with a Bakul vendor/mess-committee source before treating
  this as the full explanation, rather than just the respondent's read on it.
  `[Source: Interview, 2026-09-09/10]`
- **Vindhya Canteen hours, confirmed (with one remaining uncertainty):** open Monday-Saturday,
  from 10 AM; closing time uncertain — respondent said both "6:00" and "8:00" without settling on
  one. Serves food, coffee, Horlicks, and similar. `[Source: Interview, 2026-09-09/10; NEEDS DATA
  — exact closing time, 6 PM or 8 PM]`
- **"Largest statistical things" (Warden) — RETRACTED by the respondent.** Confirmed as a
  transcription/mishearing artifact, not a real claim. Removed from open items rather than carried
  forward as something to resolve.

- **Correction to my own earlier framing:** I had characterized the mess-hours/class-time clash as
  possibly "a minority case" for the System Context Brief draft. The user corrected this directly:
  the clash is a real, standing fact regardless of how many students are affected on a given day,
  and should be treated as such — not minimized. Equally, the fact that many students skip
  breakfast **for reasons unrelated to class timing** (per §7) is itself a separate, real pattern
  worth investigating on its own terms, not folded into or explained away by the class-clash
  narrative. Both are live, factual threads to pursue, not competing explanations to rank.
