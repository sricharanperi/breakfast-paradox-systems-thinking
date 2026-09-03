# Dining Portal Screenshot Analysis

**Source:** `[Source: Screenshot — dining.iiit.ac.in, captured by user, 2026-09-03]`. Six
screenshots of the real IIIT-H dining portal (`dining.iiit.ac.in`), CAS-login-gated, browsed by
the user directly. Saved alongside this file. Everything below is read directly off the images —
nothing extrapolated beyond what's visible.

## 1. `2026-09-03_calendar-view-september.png` — Dining Portal calendar, September 2026

Monthly grid, each day showing 4 meal-slot rows: **B**, **L**, **S**, **D** (Breakfast, Lunch, an
**S** slot — not identified by the user verbally at all; likely "Snacks," `[NEEDS
CLARIFICATION]`, and Dinner). For this respondent's actual registrations: B and L are consistently
"Kadamba (V)" (green), D alternates between "Kadamba (V)" and "Bakul (V)" (purple/blue), S is
"Not Registered" on every visible day. Sept 1 shows L and D struck through (green strikethrough =
cancelled that day). Sept 3 (today, boxed/highlighted) shows: B Kadamba(V), L ~~Kadamba(V)~~
(cancelled), S Not Registered, D Bakul(V).

## 2. `2026-09-03_breakfast-not-availed-charge.png` — Edit meal registration, Breakfast 2026-09-03

Direct, dated, real confirmation of the exact anecdote the user gave verbally: **"You did not
avail this meal. You were charged ₹48 at Kadamba (Veg)."** — this is not a generalized claim, it's
today's actual charge screen. Also visible: **Meal Rating** / **Menu** tabs, with a note "The
feedback window hasn't closed yet! We're waiting for everyone to rate their meal" — confirms the
portal has a **per-meal rating/feedback system**, not previously mentioned.

## 3. `2026-09-11_dinner-edit-registration-menu.png` — Edit registration, Dinner 2026-09-11 (future date)

Shows the registration-editing UI: a mess dropdown ("Kadamba (Veg)"), **Save**, **Import Meal**,
and a red **Cancel Meal** button, an "Extra Items" option, and a **Skip Meal** toggle with the
label: *"Let the staff know that you'll be skipping the meal so they don't prepare food for you.
**You will still be charged.**"* — this is an important, previously-unconfirmed distinction:
**Skip ≠ Cancel**. Skipping just tells the kitchen not to prepare your portion (reduces their
waste) but does **not** stop your charge; only Cancel (capped at 5/meal-type/month per the earlier
interview) avoids the charge. Below that, the Menu tab shows Bakul (Veg)'s actual dinner menu:
Soups (Mix Veg Soup), phulka/chapati (Chapati), flavoured rice (Sweet corn pulao), dal (Bengali
Dal), veg wet (Matar Paneer), veg dry (Bhindi Masala), curd/raitha (Curd), pickle/fresh chutney
(Pickle) — confirms menus are structured by fixed food-category slots, not freeform.

## 4. `settings-auth-keys-preferences.png` — dining.iiit.ac.in/settings

Two sections:
- **Auth Keys**: *"These keys allow other applications to log in and manage mess registrations on
  your behalf. Do not share your auth key with untrusted entities."* Two keys listed:
  "2nd-year-2nd-sem" (expires 31 Jan 2027) and "2nd-year-1st-sem" (expired 31 Aug 2026) — this
  reveals (a) the respondent is a 2nd-year student, and (b) **there's an API/auth-key system for
  third-party tools to manage mess registration on a student's behalf** — implying a shadow
  ecosystem of student-built bots/scripts for auto-registration or auto-cancellation. Not
  mentioned verbally by the respondent; worth asking about directly.
- **Preferences**: "Send registration reminder email" (OFF for this user), **"Send random
  allocation email — sends an email with meals if you've been randomly allocated"** (ON) — this
  directly confirms the earlier `[NEEDS CLARIFICATION]` about random allocation: **random
  allocation is a real, named mechanism in the system**, not a misunderstanding. "Auto-reset QR
  code — resets the QR code automatically at 02:00 every day" (OFF for this user) — confirms QR
  reset is real and can be automated nightly, though this respondent has it off.

## 5. `2026-09-10_lunch-capacities.png` — Capacities tab, Lunch 2026-09-10 (future date)

Real, exact numbers. Two sections, "Available" = remaining open slots, "Capacity" = max slots
(so Registered count = Capacity − Available):

| Mess | Available | Capacity | Implied registered |
|---|---|---|---|
| Yuktāhār | 122 | 340 | 218 |
| Yuktāhār (Jain) | 2 | 15 | 13 |
| Kadamba (Veg) | 478 | 1200 | 722 |
| Bakul (Veg) | 584 | 700 | 116 |
| Palāsh | 258 | 400 | 142 |

Plus a separate **"Unregistered"** (walk-in) allotment, flat 30 slots for Yuktāhār, Kadamba (Veg),
Bakul (Veg), and Palāsh (Yuktāhār-Jain has no walk-in row shown).

**This confirms Yuktāhār as a real, named fourth mess** (with diacritics "Yuktāhār" — the
respondent's verbal "Yuktahar" was correct), with its own Jain-food variant as a distinct
sub-registration. Kadamba is by far the largest by capacity (1200) and Bakul's uptake is
strikingly low relative to its capacity (only 116/700 registered vs. Kadamba's 722/1200) —
`[interesting real pattern, not yet explained by any interview data — worth asking why Bakul's
registered/capacity ratio is so much lower]`.

## 6. `2026-09-10_lunch-rates.png` — Rates tab, same Lunch 2026-09-10

| Mess | Registered price | Unregistered (walk-in) price |
|---|---|---|
| Yuktāhār | ₹72 | ₹124 |
| Yuktāhār (Jain) | ₹72 | — |
| Kadamba (Veg) | ₹65 | ₹111 |
| Bakul (Veg) | ₹65 | ₹111 |
| Palāsh | ₹65 | ₹111 |

**Structurally important finding:** walk-in (unregistered) price is ~70-90% higher than the
pre-registered price across every mess. This is a real, quantified incentive to register in
advance even when attendance is uncertain — a direct mechanical driver of the "register anyway,
skip anyway" pattern, on top of the cancellation-cap/billing mechanism already logged. Breakfast
rate for Kadamba (Veg) confirmed here indirectly consistent with the ₹48 charge shown in image 2
(different meal, same mess/veg line item, so not a strict duplicate check, but consistent in
shape).

## 7-9. `2026-09-09_breakfast-*.png` — Edit registration, Capacities, Rates for Breakfast 2026-09-09 (Wed)

**This is the first breakfast-specific (not Lunch) capacity/rate data captured — resolves the
"NEEDS DATA: breakfast-specific numbers" gap from the System Context Brief.** Note this UI shows
finer granularity than the earlier Lunch screenshot — Kadamba and Bakul each split into separate
Veg/Non-Veg registration lines (the Lunch screenshot only showed one "Bakul (Veg)" line; not
necessarily a contradiction, just possibly less granular for that meal/date — flagged, not forced
to reconcile).

**Capacities, Breakfast 2026-09-09 (Registered):**

| Mess | Available | Capacity | Implied registered |
|---|---|---|---|
| Yuktāhār | 232 | 340 | 108 |
| Yuktāhār (Jain) | 7 | 15 | 8 |
| Kadamba (Veg) | 149 | 700 | 551 |
| Kadamba (Non-Veg) | 292 | 600 | 308 |
| Bakul (Veg) | 242 | 350 | 108 |
| Bakul (Non-Veg) | 313 | 350 | 37 |
| Palāsh | 254 | 400 | 146 |

Unregistered (walk-in), flat 30 slots each for Yuktāhār, Kadamba (Veg), Bakul (Veg), Palāsh
(non-veg walk-in rows not shown in this crop).

**Rates, Breakfast 2026-09-09 (Registered):** Yuktāhār ₹53, Yuktāhār (Jain) ₹53, Kadamba (Veg)
₹48, Kadamba (Non-Veg) ₹66, Bakul (Veg) ₹48, Bakul (Non-Veg) ₹66, Palāsh ₹48. (Unregistered/
walk-in rates cut off in this crop, not captured.) Kadamba (Veg) ₹48 matches exactly the charge
shown in the earlier Sept 3 screenshot — good internal consistency.

**Real pattern confirmed with actual breakfast numbers:** Kadamba (Veg) is by far the
highest-uptake option (551/700 registered) — consistent with the user's account that "Kadamba is
usually the go-to place... food was liked by many people." Bakul's both lines (108/350 veg,
37/350 non-veg) are markedly lower uptake even relative to their own (smaller) capacities.
`[Source: Screenshots, 2026-09-09]`

## Summary of what this resolves from the open-items list

- ✅ Yuktāhār confirmed as a real fourth mess (not a vendor name) — mess count is **4**: Kadamba,
  Palash, Bakul, Yuktāhār (Yuktāhār also offers a Jain-food variant as a sub-option)
- ✅ Random allocation confirmed as a real system feature (Settings → "random allocation email")
- 🆕 New, previously unknown facts: Skip ≠ Cancel distinction; per-meal rating/feedback system;
  third-party auth-key API access to registrations; real capacity/registration numbers per mess;
  real registered-vs-walk-in price gap (~70-90% markup)
- ❓ Still open: what the "S" calendar slot is (Snacks?); why Bakul's registered/capacity ratio is
  so much lower than Kadamba's; whether other students use the third-party auth-key ecosystem and
  for what
