# Process log: the project story document

Purpose: a handover. Any model or person can read this file and continue the work without the chat history. Update it at every decision. Newest entries at the bottom of each section.

## 1. What the user asked for (verbatim intent, 2026-10-12)
- One combined project document covering Phases 1 to 4 and all their deliverables and sections, but NOT a concatenation of the stand-alone PDFs. Tell it as a story: start with the problem and our approach at every stage, the trade-offs, our decisions and the rationale.
- Simple language, like project documentation, humanized (the ai-humanizer skill at .claude/skills/ai-humanizer). Easy to read and understand, "like a book of experiments", nice to look at. Not a 150-page document; a person publishing it should be able to hand it to readers who then understand everything.
- Not a repetition of facts. No repeated information across chapters (the stand-alone PDFs repeat because each stands alone; the story must not).
- Check the images repeated across the PDFs: are they at apt places, can something better replace them.
- Research how to make project documentation interesting; inspiration: `Project/TOJO by Dinu.pdf` (a graduation project told as a journey). Do not copy its style. (It is CC BY-NC-SA; we take structural ideas only, no text or images.)
- Keep this log of the whole thinking and decision process so another model can continue.
- Earlier standing rules still apply: markdown is the source of truth; evidence labels (confirmed / single-sourced / candidate / assumed; Phase 3 adds projected / simulated / planned); people by role only; no em dashes; spellings Yuktāhār, Palash, Kadamba, Bakul; never name files, tools or lectures inside submitted text; zero tool residue in PDF metadata.

## 2. State of the repo at the start of this task
- deliverables/phase-1-rebuild/: Phase 1 rebuilt, 92-page combined PDF (cover + 6 PDFs) plus Source/, Assets/ (25 diagrams, 8 photo plates), Build/ (LaTeX pipeline: build.py, header.tex, tables.lua, bundle.py, check_headings.py).
- deliverables/phase-2-rebuild/: five Phase 2 deliverable PDFs, a one-page corrections table, 79-page combined.
- deliverables/phase-3-4-rebuild/: Activity 9 (13 pp) and Activity 10 (18 pp) PDFs, 32-page combined.
- Original (stale, untouched) submissions remain in deliverables/phase-1, phase-2, phase-3.
- The full project history and ~85 decisions (D-1 to D-85+) live in Project/MASTER_CONTEXT.md; evidence in research/primary-research (Briefs #1 to #3) and Observation images/Extracted Data.

## 3. Decisions about the story document (with reasons)
(see bottom of file, appended as made)

### 3.1 Image audit across the rebuilt PDFs (2026-10-12)
Findings: the same figure was reused across stand-alone documents because each had to stand alone. Counts: crowd curve in 6 documents; loop pictures B1 (kitchen channels) and R1 (Mess Cell) in 4 each; Yuktāhār books photo plate in 4; command chain, power-flow network in 3 each; about a dozen others in 2.
Verdict: acceptable inside stand-alone PDFs, wrong for a story. Several are also "dense engineer diagrams" (power-flow network, command chain, B1) that a general reader cannot read at book size.
Decision: in the book every figure appears ONCE, at the chapter where the idea is introduced; later chapters refer back by name. Dense diagrams are replaced by simpler drawings (pictograms, cast cards, strips, before/after panels). Data charts (arrival curve, weekday, Yuktāhār breakfast vs lunch, scenario charts) are kept once each because they carry real evidence. Photos are used as evidence moments, one plate per chapter at most.

### 3.2 Book structure decided (before research came back; reconcile with RESEARCH_NOTES.md)
Parts and chapters follow the project's real order of discovery, not the deliverable order: 1 The puzzle; 2 Drawing the edges (Context Brief); 3 Who is in the room (Stakeholder Map, Power-Interest/Leverage); 4 Walking the real morning (Process Trace, student interviews); 5 The day the numbers arrived (Timeline, field visits and records: the turning point); 6 One page for the whole system (System Map); 7 What loops and what only looks like a loop (Causal Loops); 8 Why it keeps happening (Systemic Problem Analysis); 9 Changing the question (Reframe, Design Opportunity); 10 Where to push (leverage points, principles); 11 Ideas on trial (concepts, scenario model, scoring); 12 What we recommend (recommendation, pilot); 13 What we got wrong and what we still do not know; Appendices: plain-words glossary, ID keys, source list, and a "where each original deliverable and section lives" map (so every deliverable and section is still traceable).
Reason: the user wants the journey, decisions and trade-offs, not a re-statement of facts. The surprise of Sept 26 (operators and records overturning the first findings) is the book's turning point, so it sits mid-book where it happened.
Length target: about 14,000 words, 60 to 70 pages at 8.5 x 8.5 in, at least one visual per spread.
Chapter template: question we asked / what we did / what we saw / the trade-off / the decision and why / what changed in our mind. Devices: Experiment card, Turning point, We were wrong about, Trade-off, Plain words, Decision strip.
Rule: one home per fact. Numbers like 37.1%, 62.9%, 70% batch, 26.5% crest, 30 to 50 outside diners appear once in full, later only by name.
Rule: the book never mentions AI tools, scripts or file names (same scrub policy as every submission).

## 4. Research outcome (2026-10-12)
- Studied the reference book for structure only (question-led parts, divider pages, one idea per spread, card devices, a Direction section between inquiry and tools, closing reflection). No text or images reused.
- Web research (case-study templates, Nygard decision records, explorable explanations) confirmed three principles: show the decisions and their rationale, list bad consequences too, and give the reader something to compare against.
- No ready template exists for systems-thinking storytelling; the blueprint is our own synthesis.
- Output: RESEARCH_NOTES.md with a 14-chapter plan, a six-beat chapter template, six devices, a visual system and a no-repetition rule.
- Implication: write a new book (not a merge), square 8.5 in pages, about 55 pages plus back matter.

### 3.3 Writing and build (2026-10-12)
- Book text written in three parts (Source/partA.md chapters 0 to 5, partB.md 6 to 10, partC.md 11 to 14 + back matter), concatenated to Source/book.md (about 10,700 words). 23 numbered decisions, listed in the Decision log at the back.
- Layout: Build/story_build.py (pandoc + tectonic), story_header.tex (square 8.5 in pages, devices as tcolorbox environments), story.lua (turns ::: divs into devices: .exp .turning .wrong .tradeoff .plain .decision .quote .chapter; [text]{.c .s .k .a .p .sm .pl} into evidence tags).
- Each figure appears once in the whole book. Reused existing evidence images (arrival curve, weekday chart, Yuktāhār breakfast vs lunch, R1 loop, two-kitchen timeline, leverage map, scenario charts, projection, prototype, five photo plates) are copied into Assets. 28 NEW simple illustrations are generated by Assets/gen/gen_story_*.py with prefix f-.
- Chapter text deliberately keeps numbers once at their home chapter: gap and crowd in ch 6, kitchens in ch 7, loops in ch 8, structures in ch 9, payment-basis question in ch 10, model results in ch 12, recommendation in ch 13.

## 5. Build, layout and final state (2026-10-12, later)
Output: `PDFs/The_Breakfast_Paradox_Story_Book.pdf`, 68 square pages (8.5 in), 39 figures (28 new `f-*.png`, 11 reused evidence charts and photo plates), 23 numbered decisions, zero em/en dashes, blank PDF metadata. Source: `Source/partA.md` + `partB.md` + `partC.md`, joined with a blank line between into `Source/book.md` (always rebuild book.md before building: `(cat partA.md; echo; cat partB.md; echo; cat partC.md) > book.md`).
Layout decisions and why:
- Figures float with `[!htbp]` and are capped at 0.65 of text height (build script rewrites `height=\textheight`). Earlier fixed placement (`[H]`) left half-empty pages; uncapped floats pushed whole figures to the next page.
- Chapter openers are a coloured band with the big numeral, then the title and one-line question, then the text on the same page. Full-page dividers gave 82 pages with many half-empty pages; the compact opener gives 68. The old full-page divider is kept in `Build/story_header_fullpage.tex.bak`.
- Dropped from the book as unreadable at book size: the leverage and intervention map and the intervention prototype diagram (their content is carried by the depth ladder, the 14 intervention places and the 20-week sequence). The R1 resale loop picture is kept but is small; every other reused chart is legible.
- The word "brief" is not used in the running text (it says "opening story"); "System Context Brief" survives only as the original deliverable's title in the back-matter map.
- Poster photo plate closes chapter 14; its sentence was folded into the caption to avoid a two-line orphan page.
Known imperfections: chapter 14 and the back matter have some white space; the decision log and deliverable map tables break across pages; Phase 3 scenario numbers are carried from the team's report, not re-run.
Concurrency note: during this work another process edited `Build/story_build.py` (output folder `Build/work_<name>`, 11 pt, 1.05 in side margins) and added `Build/header_base.tex`, `Build/work_Story`; those were left as found. `PDFs/Story.pdf` and `PDFs/test.pdf` were removed as stale experiments; they can be rebuilt with the build script.

## 5. Build status and what was decided while building (2026-10-12, end of session)

### 5.1 Result
- Final file: `PDFs/The_Breakfast_Paradox_Story_Book.pdf`, 64 pages, 8.5 x 8.5 in, cover + contents + chapters 0 to 14 + back matter (plain words, codes, decision log, map of where each original deliverable lives, sources). 38 distinct figures, none used twice (checked by counting `Assets/` references in `Source/book.md`).
- Rebuild: `Build/join.sh` (joins Source/partA/B/C.md into Source/book.md with blank lines between them; plain `cat` glued the chapter 6 marker onto the last line of part A and broke chapter 6), then `python3 Build/story_build.py Source/book.md PDFs/The_Breakfast_Paradox_Story_Book.pdf` from this folder. The build keeps its work files in `Build/work_<output name>/`, so two builds with different output names do not collide. Edit the three part files, never book.md.
- Checks run on the final PDF: zero em or en dashes; no file names, tool names, "AI", lecture or book mentions; Title/Author/Subject/Creator/Producer blank; no leftover `:::` markup; contents page numbers match the chapter openers.
- Not done: the PDF was reviewed as contact sheets and a few full-size pages, not read line by line. Numbers were spot-checked against the evidence (Kadamba 32,162 bookings, 11,941 scans, 37.1 and 62.9 percent, 26.5 percent in the last quarter hour, Yuktāhār breakfast 17.7 to 40.2 percent); the Phase 3 model numbers were carried over from the team's Phase 3 report, not re-run.

### 5.2 Layout decisions
- Body type 11 pt with 1.05 in side margins (about 75 characters a line). 10.5 pt on a wide measure read as small and long-lined.
- Chapter openers are a colour band plus the chapter title, question and first text on one page (full-page dividers were tried first; they cost 15 pages and left half-empty pages).
- Device boxes (experiment, turning point, we were wrong about, trade-off, plain words, decision) are not allowed to split across pages; a split box left one-line pages.
- Figures are full text width unless they are photos; each figure carries a one-sentence caption that says what to notice.
- Cover: a hundred dots, thirty-seven filled (the share of Kadamba breakfast bookings that are eaten). It echoes the chart in chapter 6.
- Spill pages (one or two lines on a page of their own at a chapter end) were removed by trimming a sentence, not by changing the layout. If text changes, re-check with: `for i in $(seq 1 N); do pdftotext -f $i -l $i FILE - | wc -w; done` and look for pages under about 45 words that are not figure pages.

### 5.3 Figures removed in the last pass (reason)
- The R1 loop picture (dense node-and-arrow, unreadable at book size; the loop is explained in words and the chain figure shows it).
- The Phase 3 "map we handed in" with levers on the chain (dense; the new depth scale and four-places figure replace it).
- A second photo of the Yuktāhār register that sat alone on a page; the books plate in chapter 5 already shows the same register.

### 5.4 Open items and known weaknesses for the next person
- Figure labels inside a few illustrations are small (about 6 pt printed) in the cast, power grid and loop grid figures. They are legible at full size but are the first thing to enlarge if the book is printed.
- Figures made by earlier work and reused (arrival curve, weekday bars, Yuktāhār breakfast against lunch, the two-kitchen timeline, scenario and stress-test charts, projection, prototype lanes) are dense. They carry evidence, so they stay, but each could be redrawn in the same simple style as the f- figures.
- The Phase 3 charts still lack the pass-3 Bakul chip and the "Kadamba only" subtitle. The text says Kadamba only and that Bakul is not sized.
- Where sources disagree the book shows it as open: who heads the dining services body (two names on record), whether Skip Meal reaches Kadamba's kitchen, and whether an operator is paid for booked or served plates.
- The earlier stand-alone rebuilds are unchanged: Phase 2 combined is 79 pages (can be cut to about 50), "8. Workarounds" heading is orphaned at the bottom of a page in Systemic Problem Analysis, one System Map sentence about counting "in weekly blocks" is unconfirmed, and the Reframed Statement assumption table was paraphrased and not re-verified against the register.

## 5. Final status (2026-10-12)
- Built: PDFs/The_Breakfast_Paradox_Story_Book.pdf, 64 square pages (8.5 x 8.5 in), 38 figures each used once (28 new illustrations f-*.png + reused evidence charts and photo plates). About 10,450 words.
- Rebuild: edit Source/partA.md, partB.md or partC.md; run Build/join.sh; run python3 Build/story_build.py Source/book.md PDFs/The_Breakfast_Paradox_Story_Book.pdf. Do not edit book.md.
- Checks passed: zero em/en dashes, no file/tool/AI mentions, blank PDF metadata, every figure used once, headings of every original deliverable traceable through the "Where the original deliverables live" table.
- Known imperfections: small label text inside the cast, power-grid, river and loop-grid illustrations (about 6 to 7 pt printed); some white space in chapter 14 and the back matter; model numbers copied from the team's Phase 3 report, not re-run; Phase 2 stand-alone combined PDF is still 79 pages; one System Map sentence about booking counts "in weekly blocks" is unconfirmed; the Reframed Statement assumption table was paraphrased, not re-verified against the register.
- Open facts shown as open in the book: payment basis (booked vs served plates), who set the four-day close and the cap of five, whether Skip Meal reaches Kadamba's kitchen, who heads the dining services body (two names on record), the base of Kadamba's 5 to 10% waste figure, all Bakul records.
- Suggested next steps if continuing: (1) enlarge text in the four small illustrations; (2) a trim pass on Phase 2 stand-alone PDFs to about 50 pages if wanted; (3) re-run the scenario model to confirm Phase 3 numbers; (4) have a human read chapters 5 to 7 for narrative flow.
