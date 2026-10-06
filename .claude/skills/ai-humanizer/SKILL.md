---
name: ai-humanizer
description: |
  DEFAULT for every Word document (.docx) or PDF the user asks Claude to make, export, render or edit, and for any report, submission, deliverable or write-up headed for one. Also use whenever the user says a document "looks AI-generated", asks to "humanize" it, or asks to make text sound human-written. Rewrites the prose so it reads as a person wrote it and makes it somewhat shorter, while keeping EVERY section, heading, table, figure, number, name, date, ID and claim. It trims only the AI-sounding words and sentences, then verifies with a script that no information was lost.
---

# AI Humanizer (documents and PDFs)

Make a document read as if a careful person wrote it, and make it a bit shorter, **without removing any section or any information**. It applies by default to every .docx and PDF, before the final render.

## The contract (never break it)

1. **Keep every section.** Same headings, same order, same numbering, same tables, same figures and captions (captions may be tightened). Never merge, drop or rename a section unless the user asks.
2. **Keep every piece of information.** Every number, percentage, currency amount, date, time, name, place, ID (LP1, IP14, L17, Table 3), confidence label (confirmed / single-sourced / candidate / assumed / projected / simulated / planned), finding, caveat, condition and recommendation survives. Rewording is fine; losing a fact is not.
3. **Add nothing.** No new facts, numbers, sources, examples or claims. If a sentence needs a detail you do not have, write a simpler sentence.
4. **Cut only what reads as AI.** Shorten the passages that carry the tells below. Leave plain, working sentences alone. The target is about **10–20% fewer words overall**, taken almost entirely from the flagged passages, and never by deleting content.
5. **Tables, data, code, file paths, formulas and quotations stay exactly as they are.** Humanize table prose cells only if they contain full sentences with tells, and keep every value.

## How to work

1. **Get an editable source.** Work on the markdown, .docx or LaTeX source, never on the PDF text itself, then re-render. If only a PDF exists, rebuild a faithful source first (text, headings, tables, figures, captions) and check it against the rendered pages. See "PDF-only documents" below.
2. **Take a baseline:** `python3 scripts/check_preservation.py before.md` prints the section list, fact inventory and tell counts.
3. **Mark the tells** in each section, strongest first (catalogue below). Look at paragraph shape too: a section whose every paragraph ends with a moral, or whose every list item has a bold label, is one tell at a larger scale.
4. **Rewrite section by section.** For each flagged passage, say the point once, directly, in plain words. Vary sentence length. Prefer *is / are / has* over *serves as / stands as / features*. Use active voice where it shows who acts. Keep the document's voice: academic and plain for reports, with no chattiness and no invented opinions.
5. **Verify:** `python3 scripts/check_preservation.py before.md after.md`. It must report every heading present, and no lost numbers or IDs. Any "missing" item must be put back, unless it was a pure duplicate inside the same paragraph and still appears there. Re-read the flagged sections once more for the tells that survive rewrites most often: not-X-but-Y contrasts, one-line closers, triads, dashes, bold labels.
6. **Render and look.** Re-render the .docx/PDF with the project's normal pipeline, view pages as images, and check tables and figures are intact.
7. **Report briefly:** words before and after, the sections trimmed most, and confirmation that the checker passed.

## Catalogue of tells (strongest first)

Act on one sighting of A-group tells. B–E tells need company in the same passage.

### A. Staging instead of stating
- **Not X but Y.** "not just / not only / rather than / isn't X, it's Y", or split across sentences ("This does not mean X. It means Y."). State the point. Keep a contrast only when both halves carry information or the negative corrects a belief the reader really holds.
- **One-line closers and morals.** A final sentence that restates the paragraph or names what an example showed ("This is why...", "That is the point.", "The lesson is clear."). Cut, unless it adds a new fact.
- **Sayings that sound deep.** "at its core", "the real question is", "the heart of the matter", "X is the architecture of Y". Replace with the specific claim.
- **Staged run-ups and signposting.** "Let us now turn to", "It is worth noting that", "Importantly,", "Crucially,", "Notably,", "In other words,", "Put simply,". Delete the run-up and start with the point.
- **Arguing with no one.** "This is not to say...", "To be clear...", "One might think...". Remove the defence; keep any real claim.

### B. Rhythm by rule
- **Forced triads.** Three items or three parallel sentences when the meaning has two or four. Keep real lists.
- **Dashes everywhere.** No em or en dashes in running prose. Use a period, comma, colon or parentheses.
- **Same sentence openings.** Several sentences in a row starting "This...", "The...", "It...". Merge or reorder.
- **Stacked qualifiers.** "could potentially", "may arguably". Keep one qualifier that the evidence supports. Never remove the project's confidence labels.
- **Over-uniform paragraphs.** Every paragraph the same length and shape. Vary it.

### C. Inflation
- **AI words:** additionally, align with, bolster, crucial, delve, deep dive, enhance, foster, garner, highlight (verb), holistic, interplay, intricate, key (adjective), landscape (abstract), leverage (verb, outside the technical "leverage point"), meticulous, navigate (figurative), nuanced, pivotal, robust (figurative), seamless, showcase, streamline, tapestry, testament, underscore, vital, vibrant, comprehensive, multifaceted, paramount, synergy, empower, unlock, realm, ever-evolving.
- **Inflated significance:** "plays a pivotal role", "marks a turning point", "sets the stage", "a step in the right direction". Keep the fact; drop the significance.
- **Shallow -ing riders:** ", highlighting / underscoring / ensuring / reflecting / fostering ...". Cut the rider or make it a sentence with a real claim.
- **Avoiding is/has:** "serves as", "stands as", "functions as", "boasts", "features". Use is / has.
- **Vague association:** "associated with", "linked to", "in connection with", when the source says how. Name the relationship.

### D. Formatting by rule
- **Bold labels on every list item** ("**Evidence:** ..."), and bold scattered through prose for emphasis. Remove the decoration. Turn a labelled list into prose when the labels add nothing. Keep the bold that marks real document structure (deliverable labels, table headers).
- **Title Case Headings Everywhere.** Keep the document's existing heading style if it is a required format (e.g. framework wording). Otherwise use sentence case.
- **Emojis, arrows (→) and decorative symbols** in prose.

### E. Leftovers
- **Chatbot residue:** "I hope this helps", "Certainly", "Here is...", "Let me know". Remove.
- **Writing about the document instead of its subject:** "This section explains...", "The table below shows...", "This document is organised as follows...", "as discussed above". Cut, unless the reader truly needs the pointer.
- **A heading repeated in the first sentence.** Remove the echo.
- **Summaries of what was just said:** "In summary", "Overall", "In conclusion" paragraphs that add nothing. Shorten them to the one new point, or cut them if the section's required structure does not need them. Never cut a required "Key findings" or "Conclusion" section; tighten it.

## When not to act
- Quotations, titles, proper names, the required framework wording in headings, defined technical terms (e.g. "leverage point", "balancing loop"), and any labels the user's project requires.
- Plain sentences with no tells. Human writing is uneven. Do not rewrite for the sake of it.
- A deliberate stylistic choice the user has asked for.

## PDF-only documents
When the user supplies only a PDF (e.g. exported from Pages or Word) and wants it humanized:
1. Extract text per page (`pdftotext -layout`), and extract figures (`pdfimages -png`) and page images (`pdftoppm`) for checking.
2. Repair broken ligatures: `fi`, `fl`, `ff`, `ffi` often drop out as gaps ("con rmed", " ows"). `scripts/fix_ligatures.py` repairs them against a word list.
3. Rebuild the document as markdown with the same title block, heading hierarchy and numbering, tables, figures in place, and captions. Check it page by page against the page images before editing.
4. Humanize the markdown, verify it with the checker, then render to PDF (and .docx if useful) in a clean layout close to the original. Keep the original file untouched and give the new one a clear name.
5. Split long documents into chunks at section boundaries (about 3,000 to 5,000 words each). Rebuild, humanize and verify each chunk, then stitch the chunks and run the checker on the whole document.
6. When rendering with pandoc, turn off implicit figures (`-f gfm-implicit_figures`) if captions are written as separate lines. Otherwise every caption prints twice. Scan the rendered text for repeated caption lines, and remove a duplicate only when the original also printed it twice by mistake.
7. Realistic shortening: a report dense with tables, numbers and confidence labels usually shrinks only 5 to 10 percent without losing facts. Say so, rather than cutting facts to hit a number.

## Scripts
- `scripts/check_preservation.py BEFORE [AFTER]`: section list, fact inventory (numbers, percentages, currency, IDs, confidence labels), tell counts per section, and word counts. With two files it reports missing headings or facts, the change in word count, and the tell counts before and after. Exits non-zero if a heading or ID is missing.
- `scripts/fix_ligatures.py IN OUT`: repairs dropped ligatures in extracted PDF text.

## Credit
The tell catalogue adapts the MIT-licensed "humanizer" skill (github.com/blader/humanizer), which is based on Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup). This skill adds the document contract, the shortening rule, the PDF workflow and the preservation checker.
