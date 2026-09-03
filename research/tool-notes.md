# Open-source tools survey (2026-09-01)

Verified via `git ls-remote` before cloning — all real repos, not hallucinated.

## Vendored into `tools/` (static HTML, no build step — just open `index.html` in a browser)

| Tool | Path | What it's for | License |
|---|---|---|---|
| Loopy (Nicky Case) | `tools/loopy/index.html` | Sketch causal loop diagrams by hand, simulate them live (nodes pulse/grow based on +/- links) | Public domain |
| CLD Editor (schucan, Loopy-derived) | `tools/cld-editor/index.html` | Lighter-weight CLD sketching, same idea as Loopy | See `tools/cld-editor/LICENSE*` in repo |
| Stakeholder Map (izzi-ink) | `tools/stakeholder-map/index.html` | Power-interest matrix + network graph, saves to browser local storage | MIT |

Use these if you want to hand-sketch/iterate on a CLD or stakeholder map interactively as a group,
outside of what I generate as Mermaid artifacts. They don't share data with each other or with me —
if you build something good in one of these, describe it back to me (or export/screenshot it) so I
can fold it into the deliverable write-up.

## Vendored into `research/` (reference material, not software)

| Repo | Path | What it is |
|---|---|---|
| Ontario govt Service Design Playbook | `research/service-design-playbook/` | Markdown crash course in service design methods — journey maps, service blueprints, research synthesis |
| HPI dt@it Toolbox | `research/dt-worksheets/` | 12 worksheets for running design thinking activities in a team |

## Considered, not vendored

- **MunGell/insightmaker** — full system-dynamics + agent-based modeling engine. Real and active but
  it's a proper web app (needs its own server), overkill for a 4-week qualitative CLD exercise. Link:
  github.com/MunGell/insightmaker — worth a look only if the team wants to *quantitatively simulate*
  the CLD (stocks/flows) rather than just diagram it.
- **gschema/awesome-service-design**, **SDXorg/SD-Tools**, **open-design-kit/opendesignkit** — curated
  link-lists / activity indexes, not standalone content worth cloning.
- Empathy maps, journey maps, 5 Whys, fishbone diagrams — no credible standalone open-source *tools*
  exist for these; they're templates/methods, not software. Handled directly by the
  `systems-design-toolkit` skill instead (markdown templates + Mermaid rendering).

## Claude Code plugin — checked, NOT installed

`fakoli/systems-thinking-plugin` (marketplace name `systems-thinking`, MIT, v0.3.0) is a real,
installable Claude Code plugin. Inspected its manifest and skills before deciding: despite the name,
it's built for **infrastructure/architecture decisions** (vendor doc risk extraction, dependency
mapping for network/cloud architecture) — not the qualitative, stakeholder/CLD-style systems thinking
this project needs. It also installs `UserPromptSubmit` and `Stop` hooks that would run on every
message in any project once enabled, and requires `uv`/`jq` as dependencies. Given the domain mismatch
and the always-on hook overhead, I skipped installing it. Reconsider only if a later phase of this
project turns into actual infra/vendor-evaluation work.
