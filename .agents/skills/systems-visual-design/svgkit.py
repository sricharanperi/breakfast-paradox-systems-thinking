import math, subprocess, os

_HERE = os.path.dirname(os.path.abspath(__file__))
ICON_DEFS = open(os.path.join(_HERE, "icon-defs.svg")).read()

PALETTE = {
    "users": ("#e65100", "#fff3e0"),
    "tech":  ("#1565c0", "#e3f2fd"),
    "biz":   ("#00695c", "#e0f2f1"),
    "soc":   ("#6a1b9a", "#f3e5f5"),
    "hub":   ("#1a237e", None),
    "green": ("#2e7d32", "#e8f5e9"),
    "red":   ("#c62828", "#fdecea"),
    "amber": ("#f57f17", "#fff8e1"),
    "teal":  ("#00838f", "#e0f7fa"),
    "grey":  ("#616161", "#f5f5f5"),
    "pink":  ("#ad1457", "#fce4ec"),
}

def chip(cx, cy, icon, line1, line2, color, w=240, h=78, icon_r=17, fill="white", text_color="#1b1b1b"):
    left = cx - w/2
    text_x = left + icon_r*2 + 18
    badge_cx = left + icon_r + 10
    out = f'<g><rect x="{left:.1f}" y="{cy-h/2:.1f}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{color}" stroke-width="2.6"/>'
    out += f'<circle cx="{badge_cx:.1f}" cy="{cy:.1f}" r="{icon_r}" fill="{color}"/>'
    out += f'<use href="#{icon}" x="{badge_cx-11:.1f}" y="{cy-11:.1f}" width="22" height="22" fill="white"/>'
    out += f'<text x="{text_x:.1f}" y="{cy-6:.1f}" font-family="Helvetica,Arial,sans-serif" font-size="12.5" font-weight="700" fill="{text_color}">{line1}</text>'
    if line2:
        out += f'<text x="{text_x:.1f}" y="{cy+12:.1f}" font-family="Helvetica,Arial,sans-serif" font-size="11" fill="#3a3a3a">{line2}</text>'
    out += '</g>'
    return out

def label_box(mx, my, label, color, bg="white"):
    lw = len(label)*6.6+16
    out = f'<rect x="{mx-lw/2:.1f}" y="{my-13:.1f}" width="{lw:.1f}" height="24" rx="7" fill="{bg}" stroke="{color}" stroke-width="1.4"/>'
    out += f'<text x="{mx:.1f}" y="{my+4:.1f}" text-anchor="middle" font-family="Helvetica,Arial,sans-serif" font-size="12" font-weight="700" fill="#222">{label}</text>'
    return out

def straight_arrow(x1, y1, x2, y2, color, label="", width=7, dash=None):
    mx, my = (x1+x2)/2, (y1+y2)/2
    dash_attr = f'stroke-dasharray="{dash}"' if dash else ""
    out = f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}" {dash_attr} marker-end="url(#arrow-{color.replace("#","")})"/>'
    if label:
        out += label_box(mx, my, label, color)
    return out

def curved_arrow(x1, y1, x2, y2, color, label="", bend=0.28, width=4.5, dash=None, sign=None, t=0.32):
    mx, my = (x1+x2)/2, (y1+y2)/2
    dx, dy = x2-x1, y2-y1
    nx, ny = -dy, dx
    norm = math.hypot(nx, ny) or 1
    nx, ny = nx/norm, ny/norm
    cxp, cyp = mx + nx*norm*bend, my + ny*norm*bend
    dash_attr = f'stroke-dasharray="{dash}"' if dash else ""
    out = f'<path d="M {x1:.1f} {y1:.1f} Q {cxp:.1f} {cyp:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{width}" {dash_attr} marker-end="url(#arrow-{color.replace("#","")})"/>'
    # anchor sign/label at parameter t along the quadratic bezier (biased toward the
    # source node) so edges sharing an endpoint don't stack their labels on each other
    it = 1-t
    tx = it*it*x1 + 2*it*t*cxp + t*t*x2
    ty = it*it*y1 + 2*it*t*cyp + t*t*y2
    if sign:
        out += f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="13" fill="{color}"/><text x="{tx:.1f}" y="{ty+5:.1f}" text-anchor="middle" font-size="15" font-weight="900" fill="white">{sign}</text>'
    if label:
        lx = tx + 22 + len(label)*3.3
        out += label_box(lx, ty, label, color)
    return out

def marker_defs(colors):
    out = []
    for c in colors:
        cid = c.replace('#', '')
        out.append(f'<marker id="arrow-{cid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>')
    return "\n".join(out)

def wrap_svg(w, h, body, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Helvetica,Arial,sans-serif">
    {ICON_DEFS}
    <defs>{extra_defs}</defs>
    <rect width="{w}" height="{h}" fill="#fbfbfd"/>
    {body}
    </svg>'''

def render(svg_content, out_png, w, h, scale=2):
    html_path = out_png.replace(".png", ".html")
    with open(html_path, "w") as f:
        f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;padding:0;background:#fbfbfd;}}</style></head><body>{svg_content}</body></html>')
    subprocess.run([
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless", "--disable-gpu",
        f"--screenshot={out_png}",
        f"--window-size={w},{h}",
        f"--force-device-scale-factor={scale}",
        "--default-background-color=FFFFFFFF",
        f"file://{html_path}"
    ], capture_output=True)
    print("rendered", out_png, os.path.getsize(out_png), "bytes")
