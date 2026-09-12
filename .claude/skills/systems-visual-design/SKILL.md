# Systems Visual Design — colorful, icon-based diagrams (not Mermaid)

Use this skill for **every diagram, map, or graph produced for this project** from now on, whenever a visual is called for. It replaces the earlier default of generating Mermaid flowcharts, which the user explicitly rejected as "clearly AI"-looking, in favor of hand-built, colorful, icon-rich vector illustrations closer to how the course's own "System Mapping Example" slide (Lecture 7-8, a Blinkit app-ecosystem diagram) looks: a radial hub-and-spoke layout, soft colored zone blobs, flat icon badges, curved labeled arrows.

**Read this whole file before building a diagram.** It is short. Skipping it and reaching for Mermaid again is the one mistake this skill exists to prevent.

## Important limitation — read this first

**There is no text-to-image generation model available in this environment.** Claude Code cannot call DALL-E, Midjourney, Stable Diffusion, or anything similar. "Image generation" in this project means: **hand-authored SVG, composed programmatically in Python, rasterized to PNG via a headless-Chrome screenshot.** This produces clean, precise, fully-controlled vector illustrations — not photorealistic or generatively-varied images. That is the right tool for systems diagrams anyway (crisp text, exact colors, reproducible), but do not imply to the user that actual generative image AI is being invoked. If a request genuinely calls for illustrative/photographic imagery this toolkit cannot produce, say so rather than quietly substituting a vector diagram and hoping it passes.

## The render pipeline

1. Compose the diagram as an SVG string (via the Python helpers below, or hand-written).
2. Wrap it in a minimal HTML file (`<!doctype html><body>{svg}</body>`).
3. Screenshot it with headless Chrome at 2x device-scale-factor for print-quality resolution:
   ```
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
     --screenshot="out.png" --window-size=<W>,<H> --force-device-scale-factor=2 \
     --default-background-color=FFFFFFFF "file:///path/to/file.html"
   ```
   (Stderr will print several harmless `CVDisplayLinkCreateWithCGDisplay` / `task_policy_set` warnings on macOS — ignore them; check the actual PNG was written.)
4. **Always render and read the resulting PNG before calling a diagram done** — the same verification discipline as the docx→PDF pipeline (see `MASTER_CONTEXT.md` Section 5.5). Layout bugs (collisions, off-canvas content, missing labels) are common on the first pass of any new diagram and are only caught by looking.
5. Alternative tools checked and **not available** in this environment: `rsvg-convert`, `inkscape`, `resvg`, any local Chromium/headless-shell binary, `cairosvg` (needs a native `libcairo` this machine doesn't have — don't `brew install` it without asking first). Google Chrome.app + `--headless --screenshot` is the confirmed-working path.

## `svgkit.py` — the shared component library

Lives at `.claude/skills/systems-visual-design/svgkit.py`, alongside `icon-defs.svg` (a set of hand-drawn flat icon `<symbol>`s — person, people, gear, phone, QR, chat bubble, coin, clock, warning triangle, briefcase, building, cooking pot, toggle switch, calendar-with-X, shield, bowl, broken-link — extend this file with more `<symbol>`s as new diagrams need new icons, following the existing `viewBox="-16 -16 32 32"` convention so they drop into `chip()` at a consistent scale).

Import it from any diagram-generator script:
```python
import sys
sys.path.insert(0, "/absolute/path/to/.claude/skills/systems-visual-design")
from svgkit import chip, straight_arrow, curved_arrow, marker_defs, wrap_svg, render, label_box, PALETTE
```

Key functions:
- **`chip(cx, cy, icon, line1, line2, color, w=240, h=78)`** — the basic node: a rounded rectangle, a colored circular icon badge on the left, two lines of text. This is the workhorse for every diagram type (system maps, blueprints, CLD nodes).
- **`straight_arrow(x1, y1, x2, y2, color, label="")`** — a straight labeled edge with an arrowhead. Use for direct/hub-spoke connections.
- **`curved_arrow(x1, y1, x2, y2, color, label="", bend=0.28, sign=None, dash=None)`** — a quadratic-bezier edge. `sign="+"` or `sign="-"` draws a small colored polarity badge partway along the curve — this is what makes a **Causal Loop Diagram** (CLD) correct: every causal link needs a polarity sign, and a loop must actually close (the last edge's target must be the first edge's source) to legitimately call it "Reinforcing" or "Balancing." `dash="8 6"` renders a broken/dashed link — use this to mark a mechanism that was *designed* but doesn't actually fire in practice (confirmed by evidence), consistent with this project's "don't overstate what's confirmed" discipline.
- **`marker_defs(colors)`** — generates the arrowhead `<marker>` defs for a list of colors; call once per diagram with every color used.
- **`wrap_svg(w, h, body, extra_defs="")`** / **`render(svg, out_png, w, h, scale=2)`** — top-level assembly and rasterization.

**A real bug to avoid repeating:** in `curved_arrow`, the sign/label anchor point must be computed along the actual bezier curve at a parameter biased toward the *source* node (`t≈0.32`), not at the straight-line midpoint. Two edges that share an endpoint (very common in triangular/polygonal loop diagrams) will otherwise place their labels almost exactly on top of each other, and whichever is drawn later silently hides the other's text — a real defect hit and fixed while building the CLDs for Task 6 (see `MASTER_CONTEXT.md`'s mistakes log). Always visually confirm every edge's label/sign is legible and not overlapping another one.

**Sizing `bend` correctly (another real bug):** `bend` is a *fraction of the edge's own length*, applied along the perpendicular to that edge. For a long, nearly-horizontal or nearly-vertical edge, the perpendicular direction is nearly vertical (or horizontal) — so a `bend` value that looks like a gentle arc on a short, steep edge becomes a huge absolute pixel displacement on a long, flat one, easily enough to push the curve off the canvas entirely. This actually happened building the Power/Information Flow Network diagram (three "no formal channel" arrows shot off the top of the page). **Rule of thumb:** pick `bend` from the arc height you actually want in pixels, divided by the edge's length — don't reuse the same `bend` number across edges of very different length or orientation. Always render and look, especially near the canvas edges.

**Routing around an obstacle: change `bend`, never the endpoint.** If a straight or lightly-curved connector would pass through another node, the fix is to increase `bend` (which only moves the bezier control point) — never to nudge the edge's actual `x2,y2` endpoint to "dodge" the obstacle, since that just moves where the arrowhead lands, potentially straight past the intended target and off the canvas. This was hit and fixed while adding intra-zone connections to the System Map's category diagram.

**Labels need room.** A label box is roughly `len(label)*6.6 + 16` px wide. Don't put one on a `curved_arrow` between two chips that are closer together than that — it will render on top of, and obscure, whichever chip is nearest. Either give the two nodes more spacing, or (usually simpler) leave that specific short connection unlabeled — the line itself already communicates "these are related"; not every edge needs text.

## Layout patterns, by diagram type

| Diagram type | Pattern | Example built this way |
|---|---|---|
| **System Map / category map** (Users, Technology, Business, Social-Environmental — the Lecture 6 "System Mapping Sprint" framework) | Radial hub-and-spoke: one central circle (the system), four soft-colored ellipse "zones" around it (top/right/bottom/left), each zone holding 4-5 `chip()` nodes, connected to the hub by one thick labeled arrow per zone. | `deliverables/phase-2/assets/diagram3-mapping-sprint-quadrants.png` (+ its generator `gen_diagram3.py`) |
| **System Map / process flow** (actors, process steps, resources, constraints) | Horizontal pipeline of `chip()` nodes left-to-right for the process; a governance row above with dashed vertical connectors down into the pipeline; a decision-branch row below for outcomes; small "flag" callout boxes (colored circle + warning icon + short text) pinned near the node they annotate, for bottlenecks/tensions — this is the "rich picture" flavor (annotated, not just a clean flowchart) without needing literal Checkland cartoon notation. | `diagram1-system-map.png` / `gen_diagram1.py` |
| **Relationship / power network** (who talks to whom, what flows, where a channel doesn't exist) | Not a pipeline — nodes placed by role (a cluster for governance, one large actor node, a commercial/vendor node, an informal-channel cluster), edges color-coded by relationship *type* (formal authority, material flow, feedback, informal economy, "no channel confirmed") rather than by source node, each with its own legend entry. Read the exact node/edge list back out of any prior version's source before rebuilding, so nothing is dropped or invented in translation. | `diagram9-power-flow-network.png` / `gen_pfn.py` |
| **Causal Loop Diagram (CLD)** | Nodes placed on a circle (`n` nodes at `360/n` degree intervals — see `loop_diagram()` in `gen_clds.py`, a small reusable function worth copying into new CLD scripts), edges as `curved_arrow` with `sign` on every link, `dash` on any link that's designed-but-not-firing. Title states the loop's letter (R1, B1, ...) and one-line confirmed/candidate status. | `diagram4`–`diagram7` in `deliverables/phase-2/assets/` |
| **Service Blueprint** (frontstage/backstage/support-process swimlanes across a timeline) | Column headers = time stages; horizontal lanes = Physical Evidence / Frontstage / Line of Visibility (a dashed red rule) / Backstage / Support Processes; `chip()` nodes in a grid, thin vertical connectors between lanes in the same column, thin horizontal flow arrows within a lane. A genuinely useful *addition* to this project's method set (not previously used) — see `MASTER_CONTEXT.md` D-20. | `diagram8-service-blueprint.png` / `gen_blueprint.py` |

## Color palette (consistent across every diagram in this project)

| Category | Stroke / accent | Fill tint |
|---|---|---|
| Users / Students / student decisions | `#e65100` (orange) | `#fff3e0` |
| Technology / Process | `#1565c0` (blue) | `#e3f2fd` |
| Business / Governance | `#00695c` (teal) | `#e0f2f1` |
| Social-Environmental / Feedback | `#6a1b9a` (purple) | `#f3e5f5` |
| External (outside the system boundary) | `#616161` (grey) | `#f0f0f0` / `#fafafa` |
| Bottleneck / broken link / warning | `#c62828` (red) | `#fdecea` |
| Tension (weaker than a hard bottleneck) | `#f57f17` (amber) | `#fff8e1` |
| Confirmed-vs-candidate contrast (e.g. R2's evidenced vs. hypothesized links) | green `#2e7d32` (confirmed) vs. pink `#ad1457` (candidate) | `#e8f5e9` / `#fce4ec` |
| Hub / central system node | radial gradient `#5c6bc0 → #1a237e`, white text | — |

Keep new diagrams inside this palette unless a new category genuinely doesn't fit one of the above — consistency across the whole document is part of what makes it look designed rather than ad hoc.

## Workflow when asked to build or update a diagram

1. Check whether an existing `gen_*.py` script already covers this diagram or a close relative — copy and adapt rather than starting from a blank SVG.
2. Plan node/zone coordinates on paper (or in a comment) before writing the loop that emits `chip()` calls — most of the real bugs in this pipeline so far have been spacing/collision issues (icon mis-centered inside its badge, chip text overflowing its box, two zones' node stacks colliding), not conceptual ones. Generous spacing and short (≤26-char) label lines avoid nearly all of them.
3. Render, then **read the PNG** — check every label is inside its box, every arrow's label is legible and not overlapping another, nothing is clipped by the canvas edge, and (for a CLD) that the loop actually closes and every link has a visible polarity sign.
4. Save the finished `.py` generator alongside its `.png` output in the same `assets/` folder the diagram belongs to (mirrors how this project already keeps Mermaid `.mmd` sources next to their `.png` renders — same idea, different source format).
5. Reference the `.png` from the deliverable's markdown exactly as any other image.
