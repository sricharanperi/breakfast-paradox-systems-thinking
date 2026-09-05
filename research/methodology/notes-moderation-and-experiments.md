# Research Methodology Notes — Live Interview Moderation & Experiment Design

Sources read for this note:
1. Joseph S. Dumas & Beth A. Loring — *Moderating Usability Tests: Principles and Practices for
   Interacting* (2008, Morgan Kaufmann) — read Chapters 1-6 in full (through "Dealing with
   Failure"), focusing on Rule 8 ("Be Unbiased") and the probing/encouragement sections, which are
   the parts directly about avoiding leading behavior live.
2. Rochelle King, Elizabeth F. Churchill, Caitlin Tan — *Designing with Data: Improving the User
   Experience with A/B Testing* (2017, O'Reilly) — read Chapters 3-4 in full (A Framework for
   Experimentation; The Definition Phase / hypothesis-building), plus the confounding-variables
   and launch-readiness portion of Chapter 6 (statistical-significance mechanics themselves were
   skimmed/skipped as instructed — not relevant to *designing* the experiment).

Calibration reference: `ResearchPlan.pdf` (project root) — a different topic (cybersecurity mental
models) but an exemplary worked example of open, indirect, narrative-eliciting research design.

---

## Part 1 — Staying neutral live (Dumas & Loring)

### The core mechanism to avoid, in the book's own terms
"One of the most critical aspects of successful moderating is to avoid biasing the participants."
Bias creeps in through **four channels**, and a written questionnaire being neutral on paper isn't
enough — all four apply just as much to how you actually run the conversation:
1. A biased script/question itself
2. Biased *questions* asked live (spontaneous follow-ups you didn't script)
3. Biased *answers you give back* when the participant asks you something
4. Nonverbal cues (tone, posture, face) — bias can leak out even through a perfectly neutral script

### Concrete good-vs-bad phrasing

**Framing a question:**
- ❌ "Did you like that, or not?" — the book's own finding: people hear the *dominant thought* in
  a statement, so this is heard as "did you like that?" Appending "or not" doesn't neutralize it.
- ❌ Using adjectives/adverbs at all (*easy*, *hard*, *helpful*, *frustrating*) — these smuggle in
  an evaluation. "Was that easy?" pre-loads the answer.
- ✅ "What did you think of that?" — fully open, no adjective, no pre-loaded direction.
- If you must offer a binary, give both sides genuinely equal weight and a pause: "Did you like
  that, or did you *not* like that?" — better, but the fully open version above is still stronger.

**Answering a question the respondent asks you:**
- ❌ Answering "Did I do that right?" with a direct "Yes"/"No" — whoever you answer gets
  information the next person doesn't, contaminating comparability.
- ✅ Turn it around: *"Did you think that was the way to do it?"* / for "Why is it asking me for
  my username?" → *"Why do you think it's asking for that?"*
- ✅ **Give identical neutral feedback regardless of sentiment.** If someone says "Wow, that's a
  great feature," respond "OK, thank you for the comment" — and give the *exact same* "OK, thank
  you for the comment" when someone says "I hate that feature." Differential warmth toward
  positive vs. negative comments is itself a leading signal.

**Probing (asking for more, without leading):**
- The book's actual technique: use a **"curious command"** — grammatically an imperative, but
  delivered in an empathetic tone so it doesn't feel like an interrogation. Concrete phrases:
  *"Tell me a little more about that."* / *"Describe a bit more about..."* / *"Share some more
  about..."* / *"Help me understand a little about..."*
- ❌ Don't use a probe to fish for a stronger version of a comment for an audience's benefit — the
  book's own example: participant says "This screen is too busy," and you say "What did you
  say?" even though you heard clearly — this is "talking indirectly to developers through the
  participant," pressuring them to repeat/amplify a negative comment. Subtly different, and fine:
  *"Tell me more about what you mean."*
- **Common neutral probes list (usable as-is):** "Tell me what you think about that." / "Is that
  what you expected, or not what you expected?" / "Did you notice [X], or not notice it?" / "What
  would you do next?" / "You just said [quote]. Help me understand what you meant by that." / "I
  noticed [specific observed behavior]. Share with me what you were thinking at that point."
  Note the last two: **anchor the probe to something you actually observed or they actually said**,
  not to an interpretation of it.

**Encouragement, without reinforcing a specific answer:**
- ❌ Praising immediately after a specific statement/action ("That was great!" right after they
  say something positive) — this teaches them what response you want to hear more of.
- ✅ Give encouragement **decoupled from any specific moment** — e.g. pick it at a fixed point
  (say, after the 3rd question) regardless of what was just said: *"You're doing fine." "You're
  really helping us." "You're giving us exactly the kind of information we need."*

**Nonverbal / conduct:**
- Neutral, consistent posture and facial expression regardless of what's said; same nod for a
  positive comment as a negative one; don't audibly react.
- If taking notes, either take a *lot* of notes throughout (so silence isn't read as "that wasn't
  interesting") or take almost none and rely on a recording — inconsistent note-taking density
  itself signals which comments you found important.
- **Speakership rule:** in a well-run session, the respondent should be doing ~80% of the talking.
  If you notice yourself talking more than that, that's a signal you're steering.
- Silence-handling: if someone asks a direct question mid-interview that you don't want to answer
  yet, say so plainly rather than staying silent — unexplained silence gets *misread* (as not
  hearing them, or as a "gotcha" test), which is its own subtle distortion.

## Part 2 — Designing an experiment (King, Churchill & Tan)

"Designing an experiment" in this book's sense means turning a vague idea into a falsifiable,
structured hypothesis *before* building anything, specifically to prevent the design from
smuggling in the answer you already expect.

### The hypothesis formula (their core practical tool)
> **For [user group(s)], if [change], then [effect], because [rationale], which will impact
> [measure].**

A shorter tech-company variant they also give:
> **We predict that [doing this] for [these people] will achieve [this outcome] because of [these
> reasons]. We will know this is true when we see [this metric change].**

Every component matters for avoiding a biased experiment:
- **User group** — be explicit about who the change targets; don't silently generalize from
  whoever happened to respond.
- **Change** — stated abstractly enough to leave room for multiple possible concrete designs, not
  pre-committed to one specific fix.
- **Effect / rationale** — the *reason* you believe the change causes the effect must be written
  down explicitly, so it can be checked/challenged rather than assumed.
- **Measure** — defined *before* the test runs, not chosen afterward once you see which numbers
  look good (the single most important discipline against confirmation bias in this whole
  section — deciding the metric after seeing the data is how people quietly rig their own
  experiments).

### "Predict," not "believe" — the epistemic move that prevents confirmation bias
Deliberate word choice in the book: frame it as a **prediction**, not a **belief**. "A false belief
can make you wrong [as a person]; a prediction can be false without any reflection on you." This
reframing matters because it's what makes it psychologically safe to accept a result that
contradicts your hypothesis instead of unconsciously reinterpreting the data to protect being
"right." Apply this directly to our project: when we eventually test a proposed Breakfast Paradox
intervention, write it as a prediction we're trying to falsify, not a belief we're trying to prove.

### Confounding variables and validity
Before trusting a result, check that nothing *other* than your intended change could explain it —
their example: seasonal variation, edge-case conditions, or a non-representative subset of users
being exposed to the change. Directly relevant to us: if we ever compare, say, registration rates
before/after some change, we'd need to rule out things like exam season, holidays, or a menu
change happening at the same time before crediting our intervention.

## Part 3 — Practical checklist: asking a follow-up live, without leading

1. Before reacting at all, decide: is my next line an observation-anchored probe ("I noticed you
   paused — tell me what you were thinking") or an interpretation I'm about to sneak in as a
   question? Only ask the former.
2. Use a curious command, not a question: "tell me more about..." beats "did that confuse you?"
3. Whatever you say after a positive comment, say the equivalent after a negative one. If you're
   not sure you'd say the exact same thing either way, don't say it.
4. If you're about to praise, ask whether it's tied to what they *just* said or done — if yes,
   hold it and give it at a fixed, content-independent point instead.
5. If they ask you a direct question, turn it back to them rather than answering, or explicitly
   say you'll answer at the end — don't just go quiet.
6. Watch your own talk-time. If you're talking more than ~20% of a given stretch, stop.

## Part 4 — What this adds to the existing checklist

`notes-hci-textbook-and-personas.md` Part 5 is a **written-questionnaire** checklist (no
presupposing questions, fact-before-reason, no compound questions, roles not personas, escape
hatches, sequencing). This note is about **live conduct during the interview itself**, which that
checklist doesn't cover. Add these live-specific items when actually running the Section 8
interviews:

- [ ] Give identical neutral acknowledgment regardless of whether the answer was positive or
      negative about the mess system ("thanks, got it" every time — not warmer for answers that
      confirm what you expected)
- [ ] Use curious-command probes ("tell me more about that") instead of interpretive follow-up
      questions ("did that frustrate you?")
- [ ] Don't repeat/echo a comment back to make the person elaborate/amplify it for the record —
      ask "tell me more about what you mean" instead
- [ ] Decouple any encouragement ("this is really helpful") from the content of what was just
      said — give it at a fixed point in the conversation, not as a reaction
- [ ] Track your own talk-time; the respondent should be doing most of the talking
- [ ] If a proposed intervention is ever tested later (Phase 3/4), write it as a **prediction**
      using the hypothesis formula above, with the success **measure fixed in advance** — never
      choose the metric after seeing which number looks best
