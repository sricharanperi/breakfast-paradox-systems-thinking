# Introduction {#ch-intro}

## Background and Motivation {#sec-background}

Every student at the International Institute of Information Technology, Hyderabad, who lives in a hostel is registered for a meal at each of the four dining halls on the campus. The registration is automatic and the charge follows it. The halls are run by caterers who are appointed by the institution, and each of them cooks a quantity of food before the first diner arrives. Breakfast is the meal where this arrangement shows its strain most clearly. A large share of the students who are registered for breakfast do not eat it, yet the food is cooked, the meal is billed, and the surplus leaves the kitchen in ways that no one in the institution tracks.

The course project in Systems Thinking and Design offered four campus puzzles. The one the team selected was the Breakfast Paradox. Its opening description presents a student whose alarm rings several times before 7:45, who stayed awake late the night before, who chooses sleep over breakfast, and who by 11:15 is hungry and unable to concentrate. The hall serves breakfast from 7:30 to 9:30, classes begin at 8:30, and only about a third of the hostel turns up. The remaining food is thrown away. The description names a single cause, the clash between the early class and the late night, and a chain of consequences that follows from it.

The project treated that description as a set of claims to be tested. Over about six weeks the team studied how breakfast registration, billing, cooking, serving and disposal fit together, who is able to change each part, and where a change would do the most good. This document records that work from the first interview to the final recommendation, with the methods used at each step, the deliverables produced, and the decisions that shaped them.

## Problem Statement {#sec-problem}

The puzzle as given asks why students skip a meal that they have registered for. The first phase of the study showed that this question is too narrow. Registration at the halls is a default that students did not choose, so non-attendance cannot be read as a decision about a meal they selected. The operators, for their part, do not cook to the registration count; each applies its own rule of thumb. The problem addressed in this document is therefore stated as follows.

> Breakfast registration at IIIT Hyderabad does not reflect who will eat, by roughly two thirds, while lunch under the same rules mostly does. Each kitchen estimates its own conversion from registrations to cooked food, the records that could calibrate that estimate are already kept, and none of those records reaches the people who set the registration and billing rules. The project asks why this arrangement persists and what a small group of students could propose to change it.

## Aim and Objectives {#sec-aim}

The aim of the project is to explain the persistence of the gap between breakfast registration and breakfast attendance as a property of the whole system, and to recommend an intervention that can be tested on the campus.

The objectives are to:

1. define the boundary of the breakfast system and separate its visible symptoms from their underlying causes;
2. identify the people and bodies that take part in the system, and establish who holds authority and who holds leverage over each decision;
3. trace how a registration becomes a quantity of cooked food, and how the system behaves over a morning, a week and a month;
4. build a model of the system that distinguishes feedback loops which close from those which only appear to;
5. reframe the problem from the evidence and identify the places where intervention would be most effective;
6. generate, test on paper and evaluate alternative interventions, and recommend one with a sequence, a pilot and a plan for withdrawing the project team.

## Scope and Boundary {#sec-scope}

The study covers breakfast in the four dining halls (Kadamba, Palash, Bakul and Yuktāhār) as it is registered, billed, cooked, served and disposed of. Lunch and dinner are outside the boundary and serve as a comparison, since the same portal, rules and caterer apply to them. The class timetable is also outside the boundary but is kept on the maps because it shapes the morning. Quantitative evidence is available for two halls only: Kadamba, from a month of scan records, and Yuktāhār, from photographed attendance registers. Bakul is described from an interview with its manager and from no records, and Palash is recorded as a candidate kitchen that shares its off-site kitchen with Bakul. These limits are repeated where they affect a claim.

## Team and Timeline {#sec-team}

The project was carried out by Team Invictus: Sricharan Peri, Prathyusha Kalluri and Neha. The work ran from the first interview on 3 September 2026 to the rebuilding of the deliverables in early October. [[fig:timeline]] shows the sequence. Two features of the timeline matter for the rest of the document. First, field evidence arrived in three batches (on 26, 27 and 28 September), after the first versions of Phases 1 and 2 had been written, and each batch forced a revision of work already done. Second, Phases 3 and 4 were written on the revised evidence, which is why the later chapters rely on figures that the earlier first submissions did not contain.

![Project timeline, September to October 2026.|Source: team record of activities.](submission/Build/newfig/sub-timeline.png){w=100 #timeline}

## Structure of the Document {#sec-structure}

[[ch:framework]] sets out the course framework and the standards of evidence applied. [[ch:litreview]] reviews the concepts and methods from the literature on which the analysis relies. [[ch:method]] describes the sources of evidence, the ways in which they were collected and analysed, and the ethical position of the study. [[ch:phase1]] to [[ch:phase4]] follow the four phases of the project. Each activity within them is reported under the same headings: purpose, method, process, deliverable, findings, and decisions and trade-offs. [[ch:synthesis]] brings the findings together, [[ch:discussion]] discusses them and the main design decisions, [[ch:limits]] sets out the limitations and ethical considerations, and [[ch:conclusion]] concludes with directions for further work. The appendices hold the glossary, the decision log, the register of deliverables and the list of open questions.

# Project Framework and Approach {#ch-framework}

## The Course Framework {#sec-cframework}

The project follows a generic framework for systems thinking and design projects that is divided into phases and activities, each of which has a purpose, a set of methods and a named deliverable. Phase 1 (Activities 1 to 5) is about understanding the system: its context, its stakeholders, the distribution of power among them, the way the process actually runs, and its behaviour over time. Phase 2 (Activities 6 to 8) builds a model of the system and reframes the problem. Phases 3 and 4 (Activities 9 and 10) look for leverage points, define design principles, and design, test and evaluate interventions. In total there are ten activities and fifteen deliverables. This document treats Phases 3 and 4 as two phases because they answer different questions: where the system could be changed, and what should be built and tested.

[[fig:framework]] shows how the activities and deliverables are arranged. [[tab:deliverables]] lists the methods used for each and the chapter of this document where they are reported.

![Project structure: four phases, ten activities and fifteen deliverables.|Source: course framework, as applied by the team.](submission/Build/newfig/sub-framework.png){w=100 #framework}

Table: Activities, methods and deliverables of the project. {#deliverables cols=17,29,35,19}
| Activity | Main methods | Deliverable | Reported in |
|---|---|---|---|
| 1 System context | Boundary framing; purpose and mechanism comparison; symptom and issue separation | System Context Brief | [[sec:a1]] |
| 2 Stakeholders | Candidate listing through seventeen lenses; tiering; relationship matrix; proximity rings | Stakeholder Map | [[sec:a2]] |
| 3 Power, interest and leverage | Decision-by-decision authority analysis; incentive chains; power-interest placement; information-flow tracing | Power-Interest and Leverage Map; Power Analysis Brief | [[sec:a3]] |
| 4 Existing process | Interviews; site visits; swimlane tracing; rule and exception inventories | Process Trace | [[sec:a4]] |
| 5 Behaviour over time | Record analysis; behaviour-over-time charts; planning-horizon ladder; event timeline | System Timeline / Behaviour-Over-Time Map | [[sec:a5]] |
| 6 System map | Rich picture; service blueprint; causal loop tests | System Map; Causal Loop and Feedback Analysis | [[sec:a6]] |
| 7 Patterns and root causes | Iceberg tracing of seven chains; archetype diagnosis; tension and workaround inventories | Systemic Problem Analysis | [[sec:a7]] |
| 8 Reframing | Assumption testing; stakeholder perspectives; alternative framings against four tests | Reframed Problem Statement; Design Opportunity Statement | [[sec:a8]] |
| 9 Leverage and principles | Twelve-place leverage scale; archetype ordering; natural comparison; intervention-point chain | Leverage-Point and Intervention Map; Design Principles | [[ch:phase3]] |
| 10 Design, test, evaluate | Concept generation; paper prototypes; scenario backtest; simulated responses; gates and weighted scoring | Intervention Concepts; Scenario Model and Impact Evaluation; Final Recommendation | [[ch:phase4]] |

## Standards of Evidence {#sec-evidence}

The data available to a student team are uneven. Some facts are read from a record, some are reported by one person, and some are reasoned from several sources. From the first deliverable onward every claim carries a label that says which of these it is, and the label is kept wherever the claim is repeated. [[tab:labels]] defines the labels. The first four apply to the analysis of the existing system; the last three apply to the design chapters, where the content describes something that has not happened.

Table: Evidence labels used throughout the project. {#labels cols=18,82}
| Label | Meaning |
|---|---|
| Confirmed | Read from a record or observed directly by a member of the team, or stated in the same way by independent sources. |
| Single-sourced | Reported by one person or one document and not yet checked against another. |
| Candidate | Worked out by combining sources; plausible, with one link that is inferred. |
| Assumed | A judgement made to continue the analysis, stated as such. |
| Projected | An output of the scenario model, based on recorded data and stated assumptions. |
| Simulated | A reasoned expectation of how a person or group would respond, with no feedback collected. |
| Planned | A test or activity that has been designed and has not been carried out. |

## Documentation Conventions {#sec-conventions}

The documentation of the project follows a small set of conventions that were fixed early and applied to every deliverable. Stakeholders are named by role, so that interviewees cannot be identified from the text. Where sources disagree, the disagreement is recorded as an open question, and neither version is chosen. Three such questions run through the project: who heads the dining services body (two names are on record), whether a Skip Meal declaration reaches the kitchen at Kadamba, and whether the operators are paid on registered or on served plates. When new evidence overturned an earlier finding, the finding was changed in every deliverable and the change was entered in a correction table, and the two versions were never blended. Each deliverable was written to stand alone, so that the first-submission documents repeat some material; this document tells the story once and gives the location of each original deliverable in Appendix C.

# Literature Review and Conceptual Framework {#ch-litreview}

The analysis uses a small number of established frameworks from the systems thinking and service design literature. This chapter summarises each framework, says what it was used for in the project, and then notes where the literature offered little help. No systematic search was carried out. The sources are the texts used in the course and a few classic papers that those texts point to.

## Systems Thinking and the Idea of Structure {#sec-systems}

Meadows (2008) describes a system as an interconnected set of elements organised to achieve something, and argues that its characteristic behaviour comes mostly from its structure and only partly from the people in it. The corollary for this project is that a persistent problem should first be examined as the output of an arrangement and only then as the result of individual choices. Senge (1994) makes a related point through the notion of mental models: the assumptions that people hold about how the system works are part of the structure, because they decide which signals are noticed. Both ideas guided where to look. The opening description of the puzzle located the cause in the student; the project looked first at the rules and the information flows around the student.

A widely used device for organising this kind of reading is the iceberg, in which an observed event is traced down through the pattern it belongs to, the structure that produces the pattern, and the mental model that sustains the structure. The iceberg is used in Activities 7 and 8.

## Feedback Loops, Delays and Archetypes {#sec-loops}

Feedback is the central concept in the systems literature. A balancing loop corrects a deviation and a reinforcing loop amplifies it, and delays between cause and effect make both hard to see (Sterman, 2000). A causal loop diagram records these links with a polarity sign on each. Sterman also warns that causal diagrams are easily drawn from links that are plausible and untested: each link needs support and the loop must actually close. The project turned this caution into a strict test in Activity 6, which is described in [[sec:a6]].

Senge (1994) and Meadows (2008) catalogue recurring structures, called archetypes, that appear in many systems. Three of them fitted the evidence in this project. In shifting the burden, a quick fix relieves a symptom, which reduces the pressure to apply the fundamental fix. In fixes that fail, a remedy works on its target and produces a side effect that worsens the original problem later. In accidental adversaries, two parties whose interests are compatible damage each other through the way each reads the other's actions. Archetypes were used in Activities 7 and 9 as a way of ordering interventions, since a quick fix can strengthen the structure that it was meant to relieve.

## Stakeholders, Power and Information {#sec-stakeholders}

Mendelow's (1991) power and interest grid places stakeholders by how much power they have over a decision and how much interest they take in it. It is a simple instrument and is well suited to a first reading of who must be managed closely and who must be kept informed. Its weakness, which appeared in Activity 3, is that it assigns one score to each actor, while the same actor can be decisive on one question and absent on the next. The unit of analysis was therefore the decision, and power, the formal ability to decide, was separated from leverage, the effect that a small action by the actor would have on the outcome. Meadows (2008) treats information flows as a point of high leverage, and this guided the later attention to which records reach which person.

## Process Tracing and Service Blueprints {#sec-blueprint}

Shostack (1984) introduced the service blueprint, in which the steps of a service are laid out in lanes divided by a line of visibility between what the customer sees and what the organisation does behind it. It is used in Activity 6 because the breakfast has exactly this form: the student sees a display plate, a queue and a scan, while the kitchen decides, cooks and tops up behind the counter. Hall (2013) provides practical guidance on interviewing, on observation in the field, and on knowing when the evidence is enough, and the fieldwork described in [[ch:method]] follows her advice to ask what people did.

## Leverage Points, Design Principles and Scenario Testing {#sec-leverage}

Meadows (1999) ranked twelve places to intervene in a system, from adjusting parameters, which is easy and weak, to changing the goals and the paradigm from which the system arises, which is hard and strong. The scale is used in Activity 9 with its numbering unchanged, so that place 1 is the deepest and place 12 the shallowest. For testing interventions without a pilot the team relied on a simulation built on recorded data. Sterman (2000) argues that a model should be tested against data and under extreme conditions before it is trusted, and the backtest and stress tests of Activity 10 follow that approach on a small scale. The structure of the decision log in Appendix B follows the lightweight decision record described by Nygard (2011), which states the context, the decision and its consequences.

## Gaps in the Literature and How the Project Responded {#sec-gaps}

The frameworks above are general, and none of them speaks directly to the problem of a default booking in an institutional canteen. Within the material available to the team, no treatment was found of how standing registration, billing at the point of booking and kitchen planning interact. The project therefore adapted the generic methods in four ways, summarised in [[tab:gaps]].

Table: Gaps in the available literature and the project's response. {#gaps cols=38,62}
| Gap | Response in the project |
|---|---|
| Power-interest grids give one score per actor. | Authority and leverage were judged decision by decision (Activity 3). |
| Causal loop diagrams are often drawn from plausible links. | A loop was accepted only if every link was evidenced; the rest were kept as chains (Activity 6). |
| Leverage-point scales rank depth and say little about what a small team can do. | Each lever was ranked by depth and then judged for feasibility, and levers that wait on missing facts were marked as held (Activity 9). |
| Evaluation of interventions usually relies on a single weighted score. | Four pass-or-fail gates were applied before scoring, and a concept expected to fail was kept in every test (Activity 10). |

# Research Methodology {#ch-method}

## Research Design {#sec-design}

The project is a single-case study of one institutional system, carried out in the form of an iterative field investigation. It uses qualitative interviews and observation to understand how the system works, quantitative analysis of administrative records to measure it, and structured modelling to compare alternatives. The case was chosen by the course. Evidence was collected in three batches, and after each batch the analysis written so far was checked against it. This design allowed the team to treat the opening description of the puzzle as a hypothesis and to revise it, but it also meant that the first versions of several deliverables were later overturned. The corrections are collected in [[sec:corrections]].

The study was guided by four research questions.

1. How does a breakfast registration become a quantity of cooked food, and where does the food go?
2. Who has authority and who has leverage over the rules and quantities in the system?
3. Why does the gap between registration and attendance persist when it is measured every day?
4. Where could a change act, what must it protect, and what would it do to the system if it were made?

## Participants and Sources of Evidence {#sec-sources}

[[tab:sources]] summarises the sources. Interviews were held with six students (five students and an account by a team member who lives in a hostel), with the head of the facilities department, and with the operators or managers of three dining halls: Kadamba, Yuktāhār and Bakul. The Bakul manager's account was finalised as a written summary on 28 September. Photographs were taken of four posters displayed in the dining halls and of 26 pages of Yuktāhār's production books. The dining office exported every breakfast scan at Kadamba for April 2026, and the team photographed Yuktāhār's attendance registers for twenty days in September 2026.

Table: Evidence base of the project. {#sources cols=26,30,22,22}
| Source | Content | Period | Principal limit |
|---|---|---|---|
| Student interviews (six voices) | How students decide to eat, cancel, skip or resell | September 2026 | Six people; one transcript with a labelling gap, so four to five distinct people |
| Portal screens and published rules | Registration, cancellation, billing and the Skip Meal button | September 2026 | Describes rules, not practice |
| Facilities head interview | Governance, oversight, menu cycle, kitchens | 13 September 2026 | One account; two names on record for one post |
| Kitchen visits and operator interviews | Planning, cooking, top-up, safety checks, surplus | 13 and 26 September 2026 | One visit per kitchen; operators describe their own practice |
| Yuktāhār production books and registers | Daily issue, cooked, left over, run-out times; attendance for breakfast and lunch | Twenty days, September 2026 | One hall, one month |
| Kadamba scan export | 32,162 breakfast bookings, 11,941 scans with timestamps and line (vegetarian or non-vegetarian) | April 2026 | One hall, one month; the scan records those who eat, not those who are served at the back door without scanning |
| Summary of the Bakul manager's interview | Share cooked by item, weekly review, off-site kitchen and delivery | Summary finalised 28 September 2026 | Single source; no records at all |
| Wall posters | The institution's stated aim for the meal | September 2026 | Statements of intent |

![Yuktāhār's production books, photographed on a kitchen visit: one day's sheet showing what was issued, cooked and left over, and when each item ran out.|Source: field visit photograph, September 2026.](deliverables/phase-1-rebuild/Assets/plate-planning.jpg){w=70 #books}

## Data Collection Methods {#sec-collection}

Interviews were semi-structured. The student interviews asked about the previous week's mornings and about what the person did, with questions on cancellation, Skip Meal and resale. The operator interviews followed the day from the evening before to the bin. Site visits combined observation with requests to see the records that kitchen staff kept for their own use, and these requests produced the most valuable data of the project. Records were photographed page by page and transcribed into tables by the team, and the Kadamba export was read directly. Observations that a team member could verify in person, such as the display plate at the entrance, the layout of the counter and the registers on the table, were labelled confirmed. What operators said about their own practice was labelled single-sourced until a second source agreed.

## Analysis Approach {#sec-analysis}

The analysis used different methods for different questions. The structure of the system was analysed through boundary framing, stakeholder tiering and decision-level authority tables. The process was analysed by tracing each operator end to end in swimlane form and listing formal rules, informal rules and exceptions. The records were analysed by computing turnout (scanned divided by registered) by day, weekday, line and time of arrival, and by comparing breakfast with lunch from the same register at Yuktāhār. System-level reasoning used the loop test, the iceberg and the archetypes described in [[ch:litreview]]. For the design chapters, a scenario model replayed proposed kitchen rules over the recorded April days and the results were tested under assumed shocks, and concepts were assessed through gates and a weighted score.

## Revision Protocol {#sec-revision}

Because evidence arrived in batches, the team fixed a revision protocol in advance. When a new source contradicted a written finding, the finding was changed in every deliverable in the same pass and the contradiction was entered in a correction table. When two sources disagreed and could not be reconciled, both were kept and the question was added to the list of open questions. New data were not waited for indefinitely: the evidence was frozen at a stated date, and the gaps were listed. Brief summaries of the later interviews took precedence over earlier ones where they conflicted, and the earliest summary remained the authority for record-level numbers.

## Ethical Considerations and Limits of the Method {#sec-ethics}

The interviews were conducted as part of a course assignment. Staff and operators are referred to by role, and no figure from a kitchen's own records is used in a way that could be turned against the person who kept it, a rule that later became a design principle. The photographs of kitchen records show production figures and no personal data. The scan export contains booking and scan records at the level of the booking, and the team reported only aggregates. The main limits of the method are the small number of student interviews, a single visit to each kitchen, two halls with two different months of records, and a model that uses only Kadamba's scans. The limits are discussed further in [[ch:limits]].
