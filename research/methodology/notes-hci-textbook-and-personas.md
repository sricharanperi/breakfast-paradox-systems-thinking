# Research Methodology Notes — Data Gathering, Question Design, User Roles & Personas

Sources read in full for this note:
1. Helen Sharp, Jenny Preece, Yvonne Rogers — *Interaction Design: Beyond Human-Computer
   Interaction* (5th ed., 2019, Wiley) — **Chapter 8, "Data Gathering"** (sections 8.1–8.7, pp.
   259–306 in the book; the ~800-page book was not read cover to cover, only this chapter, which
   is exactly the canonical HCI treatment of interviews/questionnaires/observation).
2. Larry Constantine — **"Users, Roles, and Personas"**, Chapter 8 of Pruitt & Adlin, *The Persona
   Lifecycle* (2006, Morgan Kaufmann) — read in full (25 pages). Filename in the project folder is
   `Constantine_Users-Roles-and-Personas_2006.pdf`; it is this specific contributed chapter, not a
   separate standalone Constantine book — confirmed by checking the source text directly.

Calibration reference used throughout: `ResearchPlan.pdf` in the project root (a different topic —
cybersecurity mental models — but an excellent worked example of the style this note recommends:
Research Goal → Objectives → several open, indirect, narrative-eliciting questions per objective →
explicit mapping of each objective to a literature concept).

---

## Part 1 — Why the first-draft questionnaire was leading (the core problem)

Straight from the textbook (Sharp/Preece/Rogers, §8.4.5, "Developing Interview Questions"):

> "Try to keep questions neutral, both when preparing the interview script and in conversation
> during the interview itself. For example, if you ask **'Why do you like this style of
> interaction?'** this question assumes that the person does like it and will discourage some
> interviewees from stating their real feelings."

This is the exact mechanism to watch for: **a question that presupposes its own answer.** Any
question of the shape "Why do you do X?" or "What makes X true for you?" silently assumes X is
already true, and makes it socially awkward for the respondent to say it isn't. The fix is not to
soften the tone — it's to **ask about the fact before asking about the reason**, and to leave room
for "actually, no" as a comfortable answer.

Concrete rule extracted: **every question implying an assumption about the respondent's behavior,
opinion, or preference must first be tested as a yes/no or open fact-check, and only branch into
"why" after the fact is confirmed** — never assume it in the question's phrasing.

Other concrete wording pitfalls from the same section:
- **Compound/long questions** — split "How do you like X compared to Y?" into two questions:
  "Do you use Y?" → (if yes) "How does X compare?"
- **Jargon** — interviewees may not understand a term and be too embarrassed to say so; use plain
  language.
- **Interviewer body language/tone** — smiling, nodding, or looking disapproving at certain
  answers visibly steers respondents toward telling the interviewer what they want to hear. This
  applies as much to how a written questionnaire *reads* (does the phrasing itself "smile" at one
  answer?) as to live interview conduct.
- **What people say ≠ what they do** (the book's own example: people told interviewers they hadn't
  changed their stair-taking behavior in response to an intervention, but logged data showed they
  had). Mitigate by not over-trusting a single self-report: triangulate with observation/screenshots
  where possible, which this project is already doing.

## Part 2 — Interview/question-type taxonomy (use deliberately, not by default)

| Type | What it is | When to use |
|---|---|---|
| Unstructured/open | Conversational, exploratory, interviewer has topics not fixed questions | Early-stage, don't yet know what matters |
| Structured | Fixed, closed questions, same wording/order for everyone | Goals already specific and well understood |
| Semi-structured | Preplanned open questions + follow-up probing until nothing new emerges | **Best fit for our Phase 1 personas** — we have specific topics (why skip/eat, who has authority) but want room for surprise |
| Focus group | 3–10 people, facilitator-led, good for surfacing shared/conflicting views | Not currently planned, but worth considering later for e.g. a room of students together |

**Neutral probes** to keep in the interviewer's back pocket rather than scripting leading
follow-ups: *"Can you tell me a bit more about that?"* / *"Is there anything else?"* — these move
the conversation forward without injecting the interviewer's assumption.

**Interview structure** (book's recommended sequence): introduction (same for everyone, explain
purpose) → warm-up with easy/non-threatening questions (e.g. basic facts) → main session, logical
order, most probing questions saved for later once rapport is built → cooling-off with easy
questions → closing thanks. Applied to our personas: start each with a simple fact question ("how
many mornings a week do you eat breakfast at the mess"), not the "why" question.

## Part 3 — Questionnaire-specific rules (when there's no interviewer present to clarify)

- Closed questions need a genuine escape hatch: include "no opinion"/"none of these"/"other"
  options — a forced-choice question without an out is itself a mild form of leading.
  - **Concrete example from the book of a broken design to avoid:** age ranges given as "15–20"
    and "20–25" — overlapping at 20, so a 20-year-old can't answer unambiguously. Ranges must be
    contiguous and non-overlapping (e.g. 15–19, 20–24).
- Use Likert scales for opinion/attitude questions (odd number of points, e.g. 5, gives a genuine
  neutral midpoint; even number forces a lean either way — pick deliberately, not by accident).
- Negative-phrased questions ("Do you *not* usually eat breakfast?") are confusing and risk false
  answers — avoid unless deliberately cross-checking an earlier positive-phrased question.
- Only collect demographic/background info that's actually relevant to the research goal (a
  respondent's height doesn't matter here; their year of study or hostel might).

## Part 4 — Roles vs. Personas (Constantine) — how to redo our 4 "personas" properly

**The core distinction, in Constantine's own terms:**
> "Personas describe users, whereas user roles describe relationships between users and systems."

A **persona** is a figurative, fictionalized individual (name, photo, backstory) built for empathy
and memorability. A **user role** is a compact, abstract description of *a relationship* — defined
by three things: **Context** (the responsibilities and environment the role operates in),
**Characteristics** (typical interaction patterns/behaviors/attitudes within that role), and
**Criteria** (what the design/research must satisfy for that role to succeed). Roles are meant to
fit on a single index card — if it doesn't fit, it's not abstracted enough.

**Why this matters for us:** our four "personas" (regular eaters, skippers, vendor/staff, mess
committee/warden) are, properly speaking, **user roles**, not personas — we don't have (and
shouldn't invent) biographical details like a fictional name or backstory for them. Constantine
would say: define each by its *relationship to the mess system*, not by a fabricated life story.
Only *after* real interview data comes back should we consider whether any role is important
enough to become a fleshed-out persona (grounded in real quotes, not invention) — persona-building
should follow data, not precede it.

**Constantine's actual methodology, condensed to what applies here:**
1. Start with **actors** — anyone/anything that interacts with the system. Separate **direct
   actors** (hands-on with the system — e.g. a student scanning their own QR) from **indirect/
   mediated actors** (off-stage but still real stakeholders — e.g. a guest whose meal a student
   registers and pays for on their behalf, or someone influenced by the Mess Cell WhatsApp market
   without registering themselves).
2. **One actor can play multiple roles.** A student is not just "a skipper" — the same person may
   play a Breakfast-Registering role, a Breakfast-Attending (or not) role, and occasionally a
   Mess-Cell-Seller role, all in one week. Don't collapse a person into a single stereotype/role;
   ask what *role* they're in for a given question.
3. **Differential description** — define each role primarily by what distinguishes it from the
   others, not by an exhaustive biography. Avoid "gratuitous details" that don't inform the
   research question (Constantine's own critique of over-elaborated personas: inventing that a
   persona "rides his skateboard" or "arrives home at 3:15" adds nothing and risks smuggling in
   unfounded assumptions).
4. **Rank by frequency and importance** to find "focal" roles worth the most attention — matches
   the priority ordering already given (Persona A/B first, C next, D if accessible).

**Bias-avoidance implication for interviewing:** because a role is a *relationship*, not a person,
the questionnaire for "Persona B: habitual skippers" should not presuppose *why* someone skips
(that bakes a mental model into the question) — it should first establish the *behavior* (do they
skip, how often) as a neutral fact, exactly as Part 1 above requires, before asking about reasons.
Framing a group by an assumed trait ("skippers who are just too busy") before asking them anything
is itself a leading setup, independent of individual question wording.

## Part 5 — Direct checklist to apply when rewriting Section 8's questionnaires

- [ ] No question assumes its own answer (no "why do you like/skip X" — ask "do you X" first)
- [ ] No compound questions — one fact per question
- [ ] No jargon (portal-specific terms like "Skip Meal toggle" should be described plainly first)
- [ ] Fact questions before reason questions; reason questions only follow a confirmed "yes"
- [ ] Order: easy/neutral first (e.g. "how many mornings a week..."), sensitive/probing last
- [ ] Each "persona" is framed as a **role** (relationship to the system), not a fictional bio
- [ ] Acknowledge people can hold multiple roles — don't force one label per respondent
- [ ] Where a closed question is used, include a genuine "other/none of these" option
- [ ] End each persona's question set with a neutral open probe ("anything else you'd add?")

This document is meant to persist as a standing reference for all future interviews/surveys/
experiments in this project, not just this one questionnaire rewrite.
