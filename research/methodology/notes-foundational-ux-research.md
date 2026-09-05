# Research Methodology Notes — Just Enough Research & UX Research (Practical Techniques)

Sources read in full for this note:
1. Erika Hall — *Just Enough Research* (2013, A Book Apart), 187 pages, all 9 chapters skimmed,
   Ch.5 "User Research" (stakeholder + user interviews) and Ch.9 "Quantitative Research" (surveys,
   analytics, split testing) read closely.
2. Brad Nunnally & David Farkas — *UX Research: Practical Techniques for Designing Better Products*
   (2016, O'Reilly), 255 pages, Ch.2 "Good Research Starts with Good Questions" and Ch.5 "Choosing
   Your Methods" read closely; other chapters skimmed for relevance.

Calibration reference used throughout: `ResearchPlan.pdf` (cybersecurity mental models exemplar).
Companion note, already written from a different source pair: `notes-hci-textbook-and-personas.md`
(Sharp/Preece/Rogers + Constantine) — this file avoids repeating what's already covered there and
flags only what's genuinely new or sharper.

---

## Part 1 — Four named pitfalls (Nunnally & Farkas), each with a concrete fix

This is more concrete than the single "fact before reason" rule already logged — it's a fuller
taxonomy, each with a bad/good example pair straight from the book:

1. **Leading questions** — give the participant a clue toward the answer you want.
   Bad: *"How do you use Outlook to communicate your work status?"*
   Good: *"How do you communicate your work status?"* (doesn't presuppose the tool)
2. **Shallow questions** — yes/no questions that let the participant off the hook without thinking.
   Bad: *"Do you use Yammer for team discussions?"*
   Good: *"How do you communicate with your team throughout the day?"*
3. **Personal bias** — the interviewer's own frustrations/opinions leaking into the question.
   Bad: *"I know I always struggle with invoices; what challenges do you have with your
   software?"*
   Good: *"Tell me about your experience with your accounting software."*
4. **Unconscious bias** — social assumptions baked into wording without realizing it. The book's
   own example: *"Where do you guys go to unwind after work?"* (implicit gender framing) vs.
   *"Where does your team go after work?"* (neutral). **Directly relevant to our Role
   C/D questions** — worth a pass checking for assumed gender/seniority/hostel-affiliation framing.

**Advanced/optional technique, noted but not recommended for this team's first round:** both
authors note that experienced researchers sometimes deliberately break these rules — e.g. asking a
mildly leading question *when you expect the real answer to be the opposite* of the hint, as a way
to validate a participant will push back rather than just agree. This is a sharp tool that assumes
a lot of interviewing experience to use safely; stick to the four rules above for now rather than
attempting this deliberately.

## Part 2 — Question anatomy (new structural model, complements the existing checklist)

Nunnally & Farkas break every good question into four parts:
- **Setup** — the what/why/how/when/where framing that tells the participant what kind of answer
  and how long a response is expected.
- **Area of inquiry** — what you actually want to learn.
- **Laddering** — the "why" follow-up chain that gets from a surface answer to underlying
  motivation/rationale. (Their own joke: "this is when we get to act like two-year-olds, asking
  'Why?'" — but they stress probing *enough without being obnoxious*.)
- **Segue** — how this question's answer sets up the next one, so the session reads as one
  conversation, not "a verbal questionnaire" read off a script.

**"Relate back to research goals" — a concrete tightening technique:** if a question doesn't
clearly serve one of your stated objectives, cut it. Their own example:
Goal: *learn how people decide which photos to share.*
Bad (technique-focused, drifts from the goal): *"How do you ensure good composition when you're
out taking photos?"*
Revised (ties back to the actual decision being studied): *"When you're out taking photos, how do
you know a particular shot is worth sharing with people?"*
**Applied to our Role A/B questions:** worth re-checking each question against "does this serve
the actual research goal (why do registration and attendance diverge), or is it just adjacent
color?" before finalizing.

**"Rabbit holes"** — questions sometimes trigger a tangent. The book's guidance: don't cut these
off automatically. A tangent is "helpful" if it surfaces real motivation/story (their example: a
photography question leading into a childhood mentorship story); "unhelpful" if it's just a
shrug-level fact with nothing underneath. Worth remembering for Role D (governance) interviews
especially, where a tangent about institutional history could be the most valuable part.

## Part 3 — Interview conduct, live (Erika Hall) — genuinely new material, not covered in the HCI notes file

The existing notes file covers question *wording*; this adds concrete guidance on interviewer
*behavior* during the conversation itself:
- **Three-act structure**: introduction/warm-up (state purpose without over-explaining — over-
  explaining the topic *before* asking can itself bias the answer) → body (open questions, use the
  question list as a checklist not a script) → conclusion (a genuine open close: *"Is there
  anything else you'd like to tell me about what we discussed?"*).
- **Breathe, and practice active listening** (mm-hmm sounds, eye contact/nodding) — tension is
  contagious and can make a participant guarded.
- **Don't talk about yourself.** It's easy for "active listening" to slide into "let me tell you
  about a similar experience I had" — that's the interviewer's story crowding out the
  participant's.
- **Allow silence.** Don't rush to fill a pause — that's often exactly when the participant adds
  the real detail.
- **Note exact phrases and vocabulary the participant uses**, not just paraphrased meaning — their
  own words often reveal the mental model more precisely than a summary would (directly useful for
  the Iceberg Model's Mental Models layer later).
- **Stakeholder interviews specifically** (most relevant to our Role D — Mess Committee/Warden):
  Hall gives a "just enough" saturation heuristic — you've talked to enough people once you're
  confident you know who all the stakeholders are, their attitudes/influence, how they stand to
  gain or lose, and whether what you're hearing is in harmony or conflict with other accounts. If a
  stakeholder turns defensive/hostile, stay calm, don't take the bait, and it's fine to cut a
  session short rather than force it.

## Part 4 — Survey/quantitative guidance (thinner than expected — noted honestly)

Neither book has a deep, dedicated "how to word a Likert-scale survey item" section comparable to
what's already logged from the HCI textbook (that remains the best source for closed-question
mechanics like non-overlapping ranges and neutral midpoints). What these two books *do* add is
guidance on **when a survey is the right tool at all**, which matters for this project's next
steps:
- **Quantitative/survey methods fit best with a large, accessible population** and a question
  that's about *prevalence* (e.g. "what % of students skip breakfast weekly") rather than *why*.
  Qualitative interviews fit better for exploring an unfamiliar workflow or mechanism (Nunnally &
  Farkas, Ch.5 "Choosing Your Methods" — factors: sample size, sample location/travel cost, budget,
  and what will actually resonate with your "stakeholders," i.e. the course grader in our case).
- **Recommendation for this project:** stick with semi-structured interviews for Roles A-D now
  (small, accessible population, exploring an unfamiliar mechanism) — but if the team later wants
  to claim something like "most students skip breakfast for reason X," that specific
  prevalence claim would need a short survey across a larger sample, not just the handful of
  interviews planned now. Worth flagging this distinction explicitly in any deliverable that makes
  a "most students..." claim — an interview sample can suggest it, only a survey can support it.

## Part 5 — Designing an experiment (Erika Hall, Ch.9 — directly answers the user's separate question about experiment design)

Hall's split/A-B testing process, condensed:
1. **Pick one specific, quantifiable goal** — not vague ("improve engagement") but a named metric
   and target ("5% → 7% conversion on the Buy button").
2. **Create variations** that change only what you're testing — she stresses this is real design
   work, not a free afterthought.
3. **Determine required traffic/sample size before starting** — smaller expected effect sizes need
   larger samples to be trustworthy; a small effect in a small sample is more likely to be noise
   than signal.
4. **Run to a defined confidence threshold** (she uses the standard 95%) **and long enough to
   cancel out confounds** — day-of-week effects, a one-off external event (e.g. unrelated press
   coverage) skewing a short window. Ideally a full two-week, holiday-free cycle.
5. **Review, then decide**: keep the control, adopt the variation, or run more tests — don't
   declare a winner before reaching the confidence threshold.

**Relevance to this project:** not immediately needed for Phase 1 (we're gathering qualitative
understanding, not testing a variation yet), but this is exactly the discipline to apply later in
Phase 3 if the team wants to validate a proposed intervention (e.g. "does moving breakfast to 8-10
AM reduce no-shows?") rather than just asserting it will work.

## What this adds to the existing 9-item checklist (`notes-hci-textbook-and-personas.md` Part 5)

Confirms rather than contradicts everything already there. Genuinely new additions worth folding
in:
- [ ] Check every question for **personal or unconscious bias**, not just presupposition (the
      "where do you guys" gender-framing example is a good self-check pattern)
- [ ] Check every question **ties back to a named research objective** — cut anything that's just
      adjacent color, not evidence toward answering the actual question
- [ ] During live interviews: **note participants' exact words**, allow silence, don't insert your
      own stories, and know the "just enough" stopping heuristic for stakeholder-style interviews
      (Role D)
- [ ] Distinguish **prevalence claims** (need a survey / larger sample) from **mechanism/reason
      claims** (fine with the current small-sample interview plan) — don't let an interview-sample
      finding get written up as if it were survey-level evidence
