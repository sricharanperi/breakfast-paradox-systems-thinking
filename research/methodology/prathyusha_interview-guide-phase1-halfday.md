# Interview Guide — Phase 1 Half-Day Push (prathyusha, 2026-09-05)

Written under a real time constraint: Phase 1 (deliverables 1-5) needs to close in half a
day. Today's 7:30-9:30 AM live-observation window has already passed, so this guide
substitutes recall for direct observation where needed (see Guide 1, Q4). Everything else
in Phase 1 that *doesn't* strictly need a human account is being drafted from existing
data + intuition — see `deliverables/phase-1/prathyusha_02-stakeholder-map.md`,
`prathyusha_03-...`, `prathyusha_05-...` for what's already assumption-built and flagged
for correction from these interviews.

**v2 — sharpened 2026-09-05 after a synthetic pilot run.** Two AI-simulated interviews
(one attender persona, one skipper persona — SYNTHETIC, not real, logged in
`prathyusha_synthetic-pilot-interviews.md`) were run through Guide 1 to stress-test the
questions before using them on real people. A third review pass caught four leading/
binary questions — both synthetic respondents gave near-identical answers to them,
which is the classic tell of a question anchoring its own answer — and they're rewritten
below. See that file's "Critique" section for the full reasoning and additional
follow-up probes not folded into the main flow.

---

## Guide 1 — Student interviews (30 min each, today, 2-3 people, mixed attend/skip)

Works whether the person mostly attends, mostly skips, or is mixed — Q1 routes the rest.
Semi-structured: ask these, let follow-ups happen naturally. Two neutral probes to fall
back on instead of improvising a leading one: *"Can you tell me a bit more about that?"*
and *"Is there anything else?"*

**Opening (1 min):** "This is for a systems-thinking project on the mess breakfast
system — no right answers, just what actually happens for you."

**1. Fact gate** *(1 min)* — In a typical week, roughly how many mornings do you eat
breakfast at the mess, and how many do you not?

**2. Full process-trace walkthrough** *(~10 min — the core of the interview)*
Pick whichever happened most recently:
- Walk me through this morning (or the last morning you skipped), from when you woke up
  to whatever happened with breakfast — as close to minute-by-minute as you can recall.
- Probes as needed: What made you decide to go / not go, at the moment you decided? Did
  you check the app at any point? **Was anyone else part of your morning at all — tell
  me about that** *(rewritten: was a compound multiple-choice probe — let them describe
  freely instead of picking from a list)*. What did the counter/queue look like when you
  got there (or would have)? Did anything not go as expected (item ran out, long queue,
  food quality)? What did you do about it?
- If they mention a regular companion: **if they were away for a week, what do you think
  would happen to your attendance? Has that actually happened — what happened?** *(new —
  both synthetic personas leaned heavily on a companion's active prompt as the real
  trigger; push past the mention to test how load-bearing it actually is)*

**3. Workarounds and exceptions** *(~5 min, fact-first each)*
- **How do you usually register — day by day, or all at once for the week?** *(new —
  both synthetic personas batch-registered every Sunday, which would decouple the
  registration decision from the morning-of attendance decision and could mechanically
  explain a lot of the no-show pattern on its own; not previously asked anywhere)*
- Have you ever cancelled a registration? → if yes, walk me through the last time.
- Have you ever used "Skip Meal"? → if yes, **what do you think it actually does, if
  anything?** *(rewritten: "symbolic or not" was a binary that anchored the answer)*
- Have you ever bought or sold a registration on the Mess Cell WhatsApp group? → if yes,
  walk me through the last time — how was the price decided? Roughly how many times have
  you bought, sold, or seen a transaction go by in the group in the last month?
- Have you ever eaten as a walk-in without being registered? → if yes, what made that
  happen that day?

**4. Retrospective pattern** *(~4 min — substitutes for the live observation we can't
do today; this directly rewrites the hypothesis section in
`prathyusha_05-system-timeline-bot-map.md` §A)*
- Has how often you eat breakfast changed over this semester? **Can you point to a
  specific week or event when it changed, or has it been pretty steady?** *(rewritten to
  ask for a pinned date, not a vague impression)*
- **Do you have a clear sense of when the mess is busiest, or not really?** — if they do:
  which half-hour, and what's different about what's being served or left over at each?
  **Have you personally seen an item run out — which one, roughly what time, how do you
  know?** *(rewritten: license "I don't know" before asking for a guess, and push for
  direct evidence over impression)*

**5. Relationships and power** *(~5 min)*
- Do you usually eat with others, and does that affect whether you go, on a given
  morning?
- Have you or anyone you know ever tried to get a mess rule or timing changed? What
  happened?
- **What's your sense of how much input students actually have in mess decisions? Can
  you think of a specific example, either way?** *(rewritten: "one-directional or not"
  was a false binary — both synthetic answers converged on near-identical phrasing,
  which is the classic sign a question is leading rather than eliciting)*
- **If breakfast started an hour later, do you think that would actually change
  anything for you?** *(new — directly tests whether the mess-hours/class-overlap
  framing is even the real driver, since one synthetic respondent argued it's habit/
  willpower, not timing)*

**6. Close** *(~2 min)* — **How much money do you think you've spent this semester on
breakfasts you didn't eat?** *(new — tests whether concretizing the cost changes the
"doesn't feel like a big deal" framing that came up in the pilot)* Anything else about
breakfast or the mess we haven't touched on?

---

## Guide 2 — Mess staff, tomorrow AM (~20-25 min each, 1-2 people)

Priority target: settle whether the **cook-on-site vs. catering-supplied** split (new
information, 2026-09-05) explains the Kadamba/Palash/Bakul differences better than the
"Bakul is newer" hypothesis currently in `deliverables/phase-1/01-system-context-brief.md`
§3. This is the single highest-value fact this interview can produce.

1. Which mess do you work at/for, and is food here cooked on-site or brought in through
   a catering service?
2. Walk me through a typical breakfast service, from when prep starts to when you close.
3. *(If catering)* How does the handoff work — what time does food arrive, who decides
   the quantity?
4. *(If on-site cook)* Who decides what's on the menu and how far ahead — and has the
   cost of ingredients or gas ever changed what gets served?
5. On a typical day, roughly how many plates go unclaimed out of what's registered?
6. When someone marks "Skip Meal," does that change what you prepare — and how far
   ahead do you actually see it?
7. What happens to food that isn't claimed?
8. How would you describe how busy your mess gets compared to the others, on a typical
   morning?
9. If you could change one thing about how registration/serving works from where you
   sit, what would it be?

---

## After each interview

Log the raw answers (close to verbatim) in
`research/primary-research/interviews/` following the existing file-naming pattern
(`YYYY-MM-DD_short-description.md`), then come back to the three
`prathyusha_0X-*.md` deliverable drafts and replace the 🟡-flagged assumptions with what
was actually said — don't just append, overwrite the hypothesis so the doc stays
internally consistent.
