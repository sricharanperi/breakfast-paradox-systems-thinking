# Phase 1 rebuild (new submission set)

The original Phase 1 files in `../phase-1/` are untouched.

- `PDFs/` : the five deliverables, the consolidated report, and `Invictus_Phase1_Complete.pdf` (cover, contents table and bookmarks, then all six in order).
- `Source/` : the markdown each PDF is built from. Edit here, never the PDF.
- `Assets/` : diagrams and photo plates. `Assets/gen/*.py` regenerate every diagram; charts read the raw CSVs under `Observation images/Extracted Data/`.
- `Build/` : `bundle.py` rebuilds everything (`python3 Build/bundle.py`); `check_headings.py` confirms every heading of the original submission survives; `skeleton_original.json` is the locked heading list.
