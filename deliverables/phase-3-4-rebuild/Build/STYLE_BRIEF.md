# Rebuild brief (Phase 2 and Phase 3/4): read before writing

Goal: a mid-length, high-quality rebuild of one deliverable. Not a summary, not a copy. Keep the analysis, cut the repetition.

## Sections
- Keep EVERY `#` and `##` heading of the source file, verbatim and in the same order. You may add `###` or new `##` sections where the content needs them. Never drop or rename an original heading.
- Keep the YAML title/subtitle block of the source.

## Length
- Target the word count given in your task (roughly a quarter to a half of the source, depending on deliverable). Quality over mechanical cutting: remove duplication first, then verbose prose, then low-value tables rows. Do not delete findings, numbers, loop/chain/lever IDs, or confidence labels that carry a distinct fact.

## Kill repetition (the main complaint)
- Every fact has ONE home section in the document. Elsewhere refer to it in a few words ("the Yuktāhār loop above"), never restate its numbers.
- The source repeats the same figures (37.1%, 62.9%, 70% batch, 26.5% crest, 30 to 50 outside diners, five cancellations, Raju/Giri, plate basis, Skip Meal conflict, no composting, Bakul floor) in many sections. State each once, in the section where it belongs, and cut it from the others.
- Drop inline "(Revised: ...)" and "earlier version said ..." narration. Corrections are collected in one table at the end of the whole phase document by the coordinator. If you find a first-version claim that was overturned, list it in a comment-free file `Source/<yourfile>_corrections.txt`, one line each (old claim -> current fact).
- No restating the heading in the first sentence. No end-of-section summary sentences. No "this section shows".

## Voice (humanizer rules, applied for real)
- Plain, direct, human sentences. Vary length. Say the point once. Active voice where it shows who acts.
- Zero em or en dashes. No "not X but Y", "rather than" contrasts used as rhetoric, no forced triads, no one-line moral closers, no signposting ("importantly", "it is worth noting"), no AI words (additionally, crucial, pivotal, robust, landscape, holistic, nuanced, underscore, foster, leverage as a verb, highlight as a verb, comprehensive).
- Use "is/are/has", not "serves as/stands as". No bold label on every list item; bold only real structure.
- Keep the project's confidence labels in prose: confirmed, single-sourced, candidate, assumed (Phase 3 also projected, simulated, planned). Keep them where a claim is made, once per claim, not on every clause.
- People by role only (no staff first names). Spellings: Yuktāhār, Palash, Kadamba, Bakul. Where sources disagree (who heads CDS, whether Skip Meal reaches the Kadamba kitchen, the plate basis for payment) show it as open, once.
- Never mention files, folders, scripts, tools, lectures, books or "the brief" inside the text. The grader gets only the PDF.
- Do not invent facts or numbers. Check any number you keep against the evidence briefs / records if in doubt (research/primary-research/*, Observation images/Extracted Data/*).

## Illustrations (compulsory)
- Aim for one visual per ~600 to 900 words of final text, placed next to the text that introduces it, each with a short italic caption written as `![Caption.](Assets/name.png){width=NN%}`.
- Reuse these ready, current images (in Assets/): diagram8-crowd-curve, d18/d19/d20 charts, d9-exception-paths, d10-loop-r1, d11-loop-b1, d14-power-flow-network, d15/d16 swimlanes, d17-food-safety-sequence, d21-two-kitchen-daily-timeline, d22-planning-horizon-ladder, d23-kadamba-command-chain, d24-bakul-offsite-loop, and photo plates plate-*.jpg (registers, books, kitchen, posters, staff). Phase 3/4 folder also has the six Phase 3 charts and the leverage and prototype diagrams.
- Do NOT reuse any old PNG from deliverables/phase-2/assets or phase-3/assets other than those already copied (they are stale).
- Generate NEW diagrams for your deliverable with the local kit: `Assets/gen/p1kit.py` (Canvas, node, edge, pill, zone, flag, legend, render; icons in icon-defs.svg; see Phase 1 generators in ../phase-1-rebuild/Assets/gen/gen_p1_*.py for usage patterns). Put your generator at `Assets/gen/gen_<name>.py`, give each PNG a unique prefix (given in your task) so parallel workers do not collide. Render, then LOOK at every PNG (Read it): no overlapping labels, nothing clipped, arrows land on boxes, text inside boxes. Fix and re-render until clean. Keep canvases about 1200 px wide, fonts at least 12 px.
- Diagrams must match the text: loops must close with +/- signs; dashed for unconfirmed; use loop IDs L1..L17, L3b.

## Build and check
- Build your PDF: `python3 Build/build.py Source/<file>.md PDFs/<Title>.pdf` from the folder root (Phase 2: deliverables/phase-2-rebuild or deliverables/phase-3-4-rebuild). Read a contact sheet or a few pages at low resolution to catch layout problems (tables running off the page, empty pages, figures too small). Tables with long text: give the separator row proportional dash widths.
- Run `python3 /Users/Shared/Files\ From\ e.localized/PDM/Sem3/Systems\ Thinking/Project/.claude/skills/ai-humanizer/scripts/check_preservation.py <source_md> <your_md>`; it must report no missing headings or IDs. Review the numbers it lists as missing: restore any that carried a distinct fact.
- Run: `pdftotext PDF - | grep -c '—'` must be 0.

## Report back (under 120 words)
Word count before/after, page count, number of figures (new/reused), any facts you could not verify, any first-version corrections file written. Do not paste the document.
