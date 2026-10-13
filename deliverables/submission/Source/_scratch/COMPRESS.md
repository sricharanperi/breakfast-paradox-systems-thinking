# Compression brief (read fully; binding)

Context: one Word document, "The Breakfast Paradox: project documentation" (Team Invictus, IIIT Hyderabad), is built from markdown files in `deliverables/submission/Source/`. The drafts are accurate and complete but far too long: the whole document must come down to about 150 pages, so each file must be cut to roughly 45 to 55 per cent of its present words. You edit ONE file (named in your task) in place, rewriting it to the target word count (see `wc -w`; include table text; stay within plus or minus 10 per cent). Nobody else edits your file. The text is written in a dialect; keep it valid.

## What must survive (exhaustiveness is the user's top priority)
- Every `##` and `###` heading with its `{#id}` (the ids are referenced from other files; do not rename or delete them). You may merge or drop `####` run-in headings.
- Every figure line `![...](path){w=.. #id}`: keep the file path, the id and a short caption plus source note (captions may be shortened to one sentence). Never drop a figure.
- Every table id that is referenced from another file: before deleting or renaming a table, grep the other files in `Source/` for `[[tab:<id>]]` and `[[fig:<id>]]`. Tables may be merged, trimmed to fewer rows or columns, or turned into prose if shorter, but their facts survive.
- Every method and process step (what the team did, in order, and why), every framework key activity, every number, ID (L1..L17, LP1..LP12, IP1..IP14, P1..P7, concepts A..H), evidence label in parentheses, named open conflict, caveat and finding. Findings are stated once.
- Every `Decision:` callout (one line each; merge two only when they say the same thing).
- Stakeholder, mechanism, lever and similar lists and registers stay complete (shorten the wording of cells, not the number of entries).

## What to cut
- Repetition: any fact stated twice in the file, any restatement of a headline number or of a fact whose home is another activity (the home map is in `_scratch/BRIEF.md` section 4; refer by `[[sec:aN]]` in a clause instead).
- Story of revisions: keep at most two sentences per activity on what changed after later evidence (corrections live in Appendix E, decisions in Appendix B).
- Verbose table cells, long lead-in and closing paragraphs, "Purpose, Approach and Timeline" prose beyond: purpose in two sentences, the method table, evidence in one sentence, dates and passes in two to three sentences. "Key Findings" sections shrink to a short list of one-line findings with pointers.
- Quotations longer than a clause, adjectives, hedging that does not carry an evidence label, "the team found that" runs, meta-comments about the document.
- Prefer a compact table to three paragraphs of enumeration when the content is a list of parallel items; prefer prose to a table when a table has one or two rows.

## Style (unchanged)
British spelling; third person ("the team"); plain sentences; no dashes of any kind (use comma, colon, parentheses, "to" for ranges); no "not X but Y" or "and not Y" tags, forced triads, moral closers, signposting, AI words (additionally, crucial, pivotal, robust, landscape, holistic, nuanced, underscore, foster, comprehensive); evidence labels in parentheses once per claim; people by role (no staff first names); Rs, "per cent"; never mention files, tools, AI, "the brief", "markdown", "the PDF". Open conflicts stay open (who heads the dining services body; whether Skip Meal reaches Kadamba's kitchen; plate basis of operator payment).

## Process and output
1. Read your whole file and `_scratch/BRIEF.md` (sections 2 and 4). 2. Plan the cut: list what is duplicated or low value. 3. Write the new file with the Write tool (complete replacement; the original is backed up in `Source/old/drafts/`). 4. Check: `wc -w <file>`; `cd ../../Build && node build_docx.js --check --only=<part of file name>` must show no missing or duplicate images, no table width problems, and no unresolved `fig:` or `tab:` references (unresolved `sec:` and `ch:` and `app:` to other files are fine). `grep -c` for the characters em dash, en dash and the percent sign must be 0 in prose (write "per cent"). 5. Append to `_scratch/<tag>_dropped.md` one line per substantive item you removed (fact or step, in 10 words). 6. Final reply under 80 words: final word count, figures kept, anything important that you could not fit.
Do not build the Word file. Do not edit other files.
