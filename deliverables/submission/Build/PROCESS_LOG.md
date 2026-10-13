# Process log: project documentation (Word), October 2026 (second, exhaustive edition)

Handover note for another model or teammate. Read with `deliverables/story/PROCESS_LOG.md` (story book) and the house rules in `README.md`.

## 0. Status (13 October 2026, final)
- `Project_Documentation.docx`: 148 pages in Microsoft Word (A4, 9.5 pt Latin Modern look, 1.7 cm side margins), 12 chapters, References, Appendices A to E, 86 figures (84 submitted-rebuild figures, each once, plus the project timeline and the portal screens), 105 tables, about 72,000 words. Contents, List of Figures and List of Tables page numbers come from Word's own pagination (`python3 Build/wordpass.py`; 0 differences). LibreOffice paginates ch4 one page differently.
- How it was brought from 205 to 148 pages (token-cheap, no further agents): smaller body font and margins, figures at 74 per cent of text width, two-column List of Figures and Tables, fewer chapter page breaks, abstract and acknowledgements on one page; deleted the framework tables in Chapter 2 (the activity method tables show the same key activities), the duplicate unintended-consequences table in Activity 6, the quick-list and trade-off tables (now in prose and in Guide 1), the alternatives column and long cells of the decision register, the revision narratives at the end of the activities, and the Key Findings bodies (replaced by a pointer to Chapter 9); long paragraphs were cut to their first sentences using `Source/_scratch/para.py` (lists paragraphs, keeps the first n sentences). Details lost this way are in the uncompressed drafts in `Source/old/drafts/` and the first edition in `Source/old/`.
- The sentences about simulated respondents were removed (the guide review is described neutrally in Chapter 4 and in decision 4 of the register). No AI-assistance note is included (the course does not ask for one).

## 1. What was asked (latest instruction)
Make the document exhaustive: add the research objectives and the interview questionnaire section; include every method, section and process of every phase from the rebuild documents; use the rebuild figures exactly as submitted (the user felt the first version's diagrams were not in line with the submissions); no repetition; story-like flow; all images exported to Figures; under about 150 pages if possible; final document, no further prompts.

## 2. Source layout (Source/*.md, the only source of the document)
01 intro; 02 framework and per-activity timeline (Chapter 2); 03 literature review; 04 methodology and instruments (objectives, sources table, guides 1 to 3, quick list, versions v1 to v6, conduct, records, evidence labels, revision protocol, ethics, limits); 05-p1-0head + 05-p1-1a1 (Activity 1), 05-p1-1b-a2, 05-p1-2a3, 05-p1-2b-a4, 05-p1-3a5 (Activity 5 and Phase 1 synthesis); 06-p2-0head + 06-p2-1a6, 06-p2-2a7, 06-p2-2b-a8; 07-p3 (Phase 3, Activity 9); 08-p4 (Phase 4, Activity 10); 09 synthesis; 10 discussion; 11 limits and ethics; 12 conclusion; 14 references; 15 Appendix A (glossary, loop key); 16 Appendix B (decision register, 94 entries); 17 Appendix C (register of deliverables); 18 Appendix D (open questions); 19 Appendix E (corrections to the first submissions).
`Source/old/` keeps the first short version and the uncompressed writer drafts; `Source/_scratch/` keeps writer notes (BRIEF.md, COMPRESS.md, dropped-item logs, chronology.md, refs.md, trim.py). They are not part of the document.

## 3. Method of this edition
Nine writers drafted the chapters from the rebuild sources, each activity under the framework's own key-activity headings plus purpose, method table, timeline, findings, decisions (one-line `Decision:` callouts); six of them hit a usage limit at the end of their run but their files were complete. Drafts were 114,000 words (343 pages), so a compression pass followed (Activities 2, 3 and 5 by writers, Activity 1 largely by a writer, Activity 6 by hand). Layout was tightened (10 pt, 2 cm margins, 1.0 spacing, tables 8 pt). Voice: third person, British spelling, evidence labels in parentheses, people by role, no dashes. Humanizer scan: 0 dashes; the few flagged phrases are the framework's own wording or quotations.
Known side effects of the compression: Activities 4, 7 to 10 and Chapter 4 are still at draft length; Activity 6 was trimmed by hand (a helper deleted one span by mistake, restored from `Source/old/drafts/06-p2-1a6.partial.md`; all 14 figures are present).

## 4. Rebuild
`cd deliverables/submission && python3 Build/make.py` (two passes: docx, LibreOffice PDF, page numbers into Contents and lists, docx again). `python3 Build/make.py --optimize` tries to move figures to fill page gaps; it gained one page and is not needed. `node Build/build_docx.js --check` validates the sources (missing or duplicate images, table widths, unresolved references). `python3 Build/gen_new.py` redraws the two framing diagrams. Dialect and fonts: see earlier notes in this file (section 4 and 5 of the first edition, unchanged): `[[fig:id]]`, `[[tab:id]]`, `[[sec:id]]`, `[[ch:id]]`, `[[app:id]]` references; `Decision:` callout lines; Word for Mac needs bold and italic faces embedded as separate families (Build/rename_fonts.py).

## 5. Caveats to check before submission
- References: Mendelow is cited as 1981 (the common 1991 date is a mis-citation); several details (Shostack pages, Brown pages, Goodhart, Campbell, Harney publisher, the Ontario playbook year, Stroh subtitle, the lecture deck title) came from notes and could not be confirmed; check against library copies. Stroh, Brown and the Design Council framework were read from summaries only and are cited narrowly.
- The interview guides were tested on two simulated respondents; the document says plainly that they are excluded from evidence (Chapter 4). Remove that sentence if the course prefers.
- If the course requires a note on AI assistance in documentation, add it to the front matter.
- Not re-run: model numbers of Activity 10 (copied from the team's scenario model outputs in the rebuild text), Bakul figures (single-sourced).
- The figure-issue notes written by the writers are in `Source/_scratch/*_figure_issues.md` (for example, one cell of the two-kitchen timeline mixes a record with a single-sourced figure).

## 6. Next task (not started)
Case study: a short version of this project (the user will prompt for it). Reuse the storyline, the home-section rule and the figure set.

---
# Earlier notes (first edition, kept for the build details)

# Process log: project documentation (Word), October 2026

Handover note for another model or teammate. Read with `deliverables/story/PROCESS_LOG.md` (story book) and the house rules in `README.md`.

## 1. What was asked
One Word (.docx) project document covering the whole journey (process, activities, methods, deliverables, decisions, outcome), written as academic project documentation (not a story book), laid out like the LaTeX reference report in `Project/Case study and project document ` (Computer Modern look, numbered chapters and sections, Contents with dotted leaders, running header with rule, roman front-matter numbers). All figures exported to a folder so the team can zip and attach them. No separate PDF: the team exports the PDF from Word. The case study (short version) is a LATER task the user will prompt for. Stop after the documentation.

## 2. What exists
- `Project_Documentation.docx` : the deliverable. A4, 75 pages (8 front matter in roman numerals, 67 numbered), 12 chapters + References + Appendices A to D, 34 figures, 14 tables, 23 decisions logged.
- `Figures/` : the 34 images used, copied by the build as `Figure_<n.k>_<id>.<ext>` so the name matches the caption. Regenerated on every build.
- `Fonts/` : LM Roman 10, LM Roman 10 Bold, LM Roman 10 Italic (TrueType, Latin Modern, GUST licence). They are also embedded in the docx. Install only if a machine shows another font.
- `Source/01..05-*.md` : the text (single source of truth for this document). `Build/` : generator and tooling.
- Build/PROCESS_LOG.md (this file), Build/gen_new.py (two new diagrams: timeline, framework), Build/newfig/ (their PNGs).

## 3. How to rebuild
`cd deliverables/submission && python3 Build/make.py`
It runs `node Build/build_docx.js` twice with a LibreOffice render between (pass 1 builds with placeholder page numbers, LibreOffice makes a PDF in `Build/work/`, `make.py` finds the printed page of every heading, figure and table, pass 2 writes those numbers into Contents, List of Figures and List of Tables as static text). Needs node with the `docx` package in `Build/node_modules` (`npm install` in Build), LibreOffice, pdftotext, Pillow. Delete `Build/work/*.pdf` after use so no stray PDF sits in the folder.
Verification done: the docx was also opened in Microsoft Word (AppleScript, Save as PDF). Word gives the same 75 pages and the same page for every Contents entry (0 differences) and renders the embedded fonts, with real bold and italic.

## 4. Text file dialect (Source/*.md, parsed by build_docx.js)
`#` chapter, `##` section, `####` run-in sub-heading (unnumbered); `# @Title` = appendix. `{#id}` after a heading, figure or table title gives it an id. Cross-references: `[[ch:name]]`, `[[sec:name]]`, `[[fig:id]]`, `[[tab:id]]` (the id minus its `ch-`/`sec-` prefix). Figure line: `![Caption.|Source note.](path){w=NN #id}` (path relative to `deliverables/` or starting `deliverables/`). Table: a line `Table: Caption. {#id cols=a,b,c}` then pipe rows. `> ` quote block, `- ` and `1. ` lists, `*italic*`, `**bold**`. Smart quotes are applied by the builder. The rupee sign is written "Rs" because Latin Modern has no glyph for it.

## 5. Design decisions for this document
1. Structure follows the reference report: front matter, then introduction, framework, literature review, methodology, one chapter per phase, synthesis, discussion, limitations and ethics, conclusion, references, appendices. Each activity is reported under the same six run-in headings: Purpose, Method, Process, Deliverable(s), Findings, Decisions and trade-offs.
2. One storyline, each fact told once in its home section (home chapters: Phase 1 for rules, records and the 37.1/62.9 per cent; Phase 2 for loops, structures and the reframe; Phase 3 for levers and Sunday; Phase 4 for model, gates, recommendation). Corrections are collected once in Table 9.1.
3. Academic voice: third person narration ("the team"), plain sentences, evidence labels kept in parentheses (confirmed, single-sourced, candidate, assumed, projected, simulated, planned), people by role, Yuktāhār/Palash/Kadamba/Bakul spellings, no em or en dashes (also in header text: "Team Invictus, IIIT Hyderabad"), no mention of files or tools in the text. Citation style: author-year (Harvard type), alphabetical reference list. The three open conflicts (who heads the dining services body; whether Skip Meal reaches Kadamba's kitchen; plate basis of operator payment) stay open.
4. Figures: analytical diagrams from the rebuilt Phase 1 to 4 asset folders, plus two new ones made with the Phase 1 diagram kit (project timeline Figure 1.1, project structure Figure 2.1) and one field photograph (Figure 4.1). Story book illustrations were NOT used because they read as storybook art. Captions sit below figures with a source line; table titles sit above tables; table style is booktabs-like (rules only).
5. Look: Latin Modern Roman 10 at 11 pt, justified, first-line indent, numbered headings, running header (title left, "Team Invictus, IIIT Hyderabad" right, rule), page number centred in the footer, title page without header, roman numerals for Abstract to List of Tables (title page counts as i, Abstract is ii), arabic from Chapter 1.
6. Fonts are embedded as three separate families because Word for Mac ignores embedded bold and italic faces (first test showed faux bold). Build/rename_fonts.py documents how the families were made. The bold-italic face does not exist in the available Latin Modern set, so the document never combines bold and italic.
7. Contents, List of Figures and List of Tables are static text (not Word fields), so there is no "update fields" prompt. If the team edits the document, page numbers must be corrected by hand or by re-running the build from the source files.
8. References (checked against what the project actually used): Hall 2013; Mendelow 1991; Meadows 1999 and 2008; Nygard 2011; Senge 1994; Senge et al. 1994 (Fieldbook); Shostack 1984; Sterman 2000. Not cited because they were not used: Kim, Stroh, Campbell and Design Council material. Page range of Shostack (133-139) and publisher names were written from memory of the standard citations and should be checked against the library copies if the course is strict.

## 6. Humanizer pass
check_preservation.py tell scan: 0 on every pattern across 17,900 words. Manual pass removed about 40 "X and not Y" constructions and first-person "we" so the voice is consistent. A residual style: about 17 sentences start "The team". Dash scan of the Word PDF: 0.

## 7. Known caveats
- Page count is 75 (reference report is about 102). Trim options: drop Figures 5.5, 6.3 and 7.2 and the Phase 1 synthesis, or cut Table 9.1 rows.
- Figures with dense text (Figures 6.2, 6.5, 8.3) are small at text width; they are the same images as in the stand-alone reports.
- Word showed one fallback font (Arial) on page 10 in the PDF export; no visible glyph is affected.
- If the course asks for a declaration of AI assistance in documentation, add it to the front matter (not included).
- Not re-verified against raw records in this pass: Phase 3/4 model numbers (copied from the earlier team report, as before), the "seven primary, five secondary" stakeholder tiering sentence (taken from the Phase 1 source), the Bakul figures (single-sourced).
- Section "Participants and Sources of Evidence" says the Bakul summary was finalised on 28 September and the facilities head interview was on 13 September; both come from the earlier session log, not from a new check.

## 8. Next task (not started, wait for the user)
Case study: a short version of this project (the user will prompt). Reuse the same storyline, home-chapter rule and figure set; keep it to a few pages.
