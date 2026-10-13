"""Diagram kit for the Phase 1 rebuild: boxes, nodes, edges, wrapped text, headless-Chrome render."""
import math, os, subprocess, html

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.dirname(HERE)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ICON_DEFS = open(os.path.join(HERE, "icon-defs.svg")).read()

# (stroke, tint)
C = {
    "users": ("#e65100", "#fff3e0"), "tech": ("#1565c0", "#e3f2fd"), "biz": ("#00695c", "#e0f2f1"),
    "soc": ("#6a1b9a", "#f3e5f5"), "ext": ("#616161", "#f2f2f2"), "red": ("#c62828", "#fdecea"),
    "amber": ("#e08600", "#fff8e1"), "green": ("#2e7d32", "#e8f5e9"), "pink": ("#ad1457", "#fce4ec"),
    "teal": ("#00838f", "#e0f7fa"), "navy": ("#1a237e", "#e8eaf6"), "slate": ("#37474f", "#eceff1"),
}
FONT = "Helvetica Neue,Helvetica,Arial,sans-serif"

def esc(s): return html.escape(str(s), quote=False)

def tw(s, fs, bold=False):
    return len(s) * fs * (0.56 if bold else 0.52)

def wrap(s, maxw, fs, bold=False):
    words, lines, cur = str(s).split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(t, fs, bold) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

class Canvas:
    def __init__(self, w, h, title=None, subtitle=None):
        self.w, self.h = w, h
        self.parts, self.colors = [], set()
        if title:
            self.parts.append(f'<text x="28" y="40" font-size="26" font-weight="800" fill="#0d47a1">{esc(title)}</text>')
        if subtitle:
            self.parts.append(f'<text x="28" y="64" font-size="15" fill="#555">{esc(subtitle)}</text>')
    def add(self, s): self.parts.append(s)
    def use_color(self, c): self.colors.add(c)

    def text(self, x, y, s, fs=15, bold=False, color="#1b1b1b", anchor="start", italic=False, width=None, lh=1.25):
        lines = wrap(s, width, fs, bold) if width else [s]
        out = []
        for i, ln in enumerate(lines):
            out.append(f'<text x="{x:.1f}" y="{y + i*fs*lh:.1f}" font-size="{fs}" font-weight="{700 if bold else 400}" '
                       f'fill="{color}" text-anchor="{anchor}" {"font-style=italic" if italic else ""}>{esc(ln)}</text>')
        self.add("".join(out))
        return len(lines) * fs * lh

    def zone(self, x, y, w, h, label, key, fs=15, opacity=0.55):
        s, f = C[key]
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{f}" fill-opacity="{opacity}" stroke="{s}" stroke-width="1.6" stroke-dasharray="7 5"/>')
        if label:
            self.add(f'<text x="{x+16}" y="{y+24}" font-size="{fs}" font-weight="800" fill="{s}">{esc(label)}</text>')

    def node(self, x, y, w, h, title, sub=None, key="tech", icon=None, dashed=False, fs=15, sfs=13, fill=None, bold_title=True, tcolor="#1b1b1b"):
        """x,y = top-left. Returns a Node."""
        s, f = C[key]
        dash = 'stroke-dasharray="7 5"' if dashed else ""
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill or "white"}" stroke="{s}" stroke-width="2.4" {dash}/>')
        tx = x + 12
        if icon:
            r = 17
            self.add(f'<circle cx="{x+r+9}" cy="{y+h/2}" r="{r}" fill="{s}"/>'
                     f'<use href="#{icon}" x="{x+r+9-11}" y="{y+h/2-11}" width="22" height="22" fill="white"/>')
            tx = x + 2*r + 22
        avail = x + w - 10 - tx
        tl = wrap(title, avail, fs, True)
        sl = wrap(sub, avail, sfs) if sub else []
        total = len(tl) * fs * 1.22 + len(sl) * sfs * 1.25 + (3 if sl else 0)
        yy = y + (h - total) / 2 + fs * 0.95
        for ln in tl:
            self.add(f'<text x="{tx:.1f}" y="{yy:.1f}" font-size="{fs}" font-weight="{700 if bold_title else 500}" fill="{tcolor}">{esc(ln)}</text>')
            yy += fs * 1.22
        yy += 3 - fs * 0.22 + sfs * 0.2
        for ln in sl:
            self.add(f'<text x="{tx:.1f}" y="{yy:.1f}" font-size="{sfs}" fill="#3a3a3a">{esc(ln)}</text>')
            yy += sfs * 1.25
        return Node(x, y, w, h)

    def pill(self, cx, cy, s, key="tech", fs=13, w=None, dashed=False):
        st, f = C[key]
        ww = w or tw(s, fs, True) + 22
        dash = 'stroke-dasharray="5 4"' if dashed else ""
        self.add(f'<rect x="{cx-ww/2:.1f}" y="{cy-fs*0.95:.1f}" width="{ww:.1f}" height="{fs*1.9:.1f}" rx="{fs*0.95:.1f}" fill="{f}" stroke="{st}" stroke-width="1.6" {dash}/>'
                 f'<text x="{cx:.1f}" y="{cy+fs*0.36:.1f}" font-size="{fs}" font-weight="700" fill="{st}" text-anchor="middle">{esc(s)}</text>')

    def badge(self, cx, cy, s, color, r=13, fs=14):
        self.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/><text x="{cx}" y="{cy+fs*0.36:.1f}" font-size="{fs}" font-weight="800" fill="white" text-anchor="middle">{esc(s)}</text>')

    def flag(self, x, y, s, key="red", w=240, fs=12.5):
        st, f = C[key]
        lines = wrap(s, w - 44, fs, True)
        h = max(32, len(lines) * fs * 1.25 + 14)
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h:.1f}" rx="9" fill="white" stroke="{st}" stroke-width="2"/>'
                 f'<circle cx="{x+20}" cy="{y+h/2:.1f}" r="12" fill="{st}"/><use href="#ic-warning" x="{x+10}" y="{y+h/2-10:.1f}" width="20" height="20" fill="white"/>')
        for i, ln in enumerate(lines):
            self.add(f'<text x="{x+40}" y="{y+ (h-len(lines)*fs*1.25)/2 + fs*0.95 + i*fs*1.25:.1f}" font-size="{fs}" font-weight="700" fill="{st}">{esc(ln)}</text>')
        return h

    def edge(self, a, b, color="#37474f", label=None, dash=None, width=3, bend=0, sign=None, lfs=12, t=0.5, a_pt=None, b_pt=None, lpos=None):
        """Edge between Nodes (or (x,y) points). Straight if bend==0 else quadratic curve."""
        self.use_color(color)
        pa = a_pt or (a.edge_toward(b.cx, b.cy) if hasattr(a, "cx") else a)
        pb = b_pt or (b.edge_toward(a.cx, a.cy) if hasattr(b, "cx") else b)
        x1, y1 = pa; x2, y2 = pb
        mx, my = (x1+x2)/2, (y1+y2)/2
        dx, dy = x2-x1, y2-y1
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy/L, dx/L
        cx_, cy_ = mx + nx*bend*L, my + ny*bend*L
        dash_attr = f'stroke-dasharray="{dash}"' if dash else ""
        if bend:
            self.add(f'<path d="M {x1:.1f} {y1:.1f} Q {cx_:.1f} {cy_:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{width}" {dash_attr} marker-end="url(#ar-{color[1:]})"/>')
            it = 1 - t
            lx, ly = it*it*x1 + 2*it*t*cx_ + t*t*x2, it*it*y1 + 2*it*t*cy_ + t*t*y2
        else:
            self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" stroke-width="{width}" {dash_attr} marker-end="url(#ar-{color[1:]})"/>')
            lx, ly = x1 + dx*t, y1 + dy*t
        if lpos: lx, ly = lpos
        if sign:
            self.badge(lx, ly, sign, color)
        elif label:
            lw = tw(label, lfs, True) + 14
            self.add(f'<rect x="{lx-lw/2:.1f}" y="{ly-lfs*0.95:.1f}" width="{lw:.1f}" height="{lfs*1.8:.1f}" rx="6" fill="white" fill-opacity="0.96" stroke="{color}" stroke-width="1.2"/>'
                     f'<text x="{lx:.1f}" y="{ly+lfs*0.36:.1f}" font-size="{lfs}" font-weight="700" fill="#222" text-anchor="middle">{esc(label)}</text>')

    def legend(self, x, y, items, title=None, fs=12.5):
        h = 14 + (22 if title else 0) + len(items) * 21 + 6
        w = max(tw(l, fs) for _, l, *_ in items) + 70
        self.add(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{h}" rx="9" fill="white" stroke="#bbb" stroke-width="1.2"/>')
        yy = y + 20
        if title:
            self.add(f'<text x="{x+12}" y="{yy}" font-size="{fs}" font-weight="800" fill="#222">{esc(title)}</text>'); yy += 22
        for it in items:
            col, label = it[0], it[1]
            style = it[2] if len(it) > 2 else "box"
            if style == "dash":
                self.add(f'<line x1="{x+12}" y1="{yy-4}" x2="{x+38}" y2="{yy-4}" stroke="{col}" stroke-width="3" stroke-dasharray="6 4"/>')
            elif style == "line":
                self.add(f'<line x1="{x+12}" y1="{yy-4}" x2="{x+38}" y2="{yy-4}" stroke="{col}" stroke-width="3"/>')
            else:
                self.add(f'<rect x="{x+12}" y="{yy-12}" width="26" height="14" rx="3" fill="{col}"/>')
            self.add(f'<text x="{x+46}" y="{yy}" font-size="{fs}" fill="#333">{esc(label)}</text>')
            yy += 21
        return w, h

    def svg(self):
        cols = sorted(self.colors | {"#37474f"})
        marks = "".join(f'<marker id="ar-{c[1:]}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>' for c in cols)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" font-family="{FONT}">'
                f'{ICON_DEFS}<defs>{marks}</defs><rect width="{self.w}" height="{self.h}" fill="white"/>{"".join(self.parts)}</svg>')

    def render(self, name, scale=2):
        out_png = os.path.join(ASSETS, name)
        html_path = os.path.join("/tmp", "p1_" + name.replace("/", "_") + ".html") if False else out_png.replace(".png", ".html")
        with open(html_path, "w") as f:
            f.write(f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:white}}</style></head><body>{self.svg()}</body></html>')
        subprocess.run([CHROME, "--headless", "--disable-gpu", f"--screenshot={out_png}", f"--window-size={self.w},{self.h}",
                        f"--force-device-scale-factor={scale}", "--default-background-color=FFFFFFFF", f"file://{html_path}"],
                       capture_output=True)
        os.remove(html_path)
        print("rendered", name, os.path.getsize(out_png))

class Node:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.cx, self.cy = x + w/2, y + h/2
    def edge_toward(self, tx, ty, pad=3):
        dx, dy = tx - self.cx, ty - self.cy
        if dx == 0 and dy == 0: return (self.cx, self.cy)
        sx = (self.w/2 + pad) / abs(dx) if dx else 1e9
        sy = (self.h/2 + pad) / abs(dy) if dy else 1e9
        s = min(sx, sy)
        return (self.cx + dx*s, self.cy + dy*s)
    def top(self): return (self.cx, self.y - 3)
    def bottom(self): return (self.cx, self.y + self.h + 3)
    def left(self): return (self.x - 3, self.cy)
    def right(self): return (self.x + self.w + 3, self.cy)
