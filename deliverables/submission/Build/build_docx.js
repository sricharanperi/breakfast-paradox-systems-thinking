// Builds the project documentation as one Word file.
// Usage: node build_docx.js OUT.docx [pages.json]
// pages.json (optional) maps entry keys to printed page numbers for the contents and the lists.
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const D = require('docx');

const SUB = path.resolve(__dirname, '..');
const ROOT = path.resolve(SUB, '..'); // deliverables/
const PROJ = path.resolve(ROOT, '..');
const fpath = (f) => (f.startsWith('deliverables/') ? path.join(PROJ, f) : path.join(ROOT, f));
const SRC = path.join(SUB, 'Source');
const CHECK = process.argv.includes('--check');
const OUT = process.argv[2] && !process.argv[2].startsWith('--') ? process.argv[2] : path.join(SUB, 'Project_Documentation.docx');
const PAGES = process.argv[3] && !process.argv[3].startsWith('--') && fs.existsSync(process.argv[3]) ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : {};
const FIGDIR = path.join(SUB, 'Figures');
const DELAYS = fs.existsSync(path.join(__dirname, 'work', 'delays.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, 'work', 'delays.json'), 'utf8')) : {};

const FONT = 'LM Roman 10';
const FONTB = 'LM Roman 10 Bold';
const FONTI = 'LM Roman 10 Italic';
// Word for Mac ignores embedded bold and italic faces, so each face is embedded as its own family.
function TR(o) {
  o = { ...o };
  if (o.bold) { o.font = FONTB; delete o.bold; delete o.italics; }
  else if (o.italics) { o.font = FONTI; delete o.italics; }
  return new D.TextRun(o);
}
const SIDE = 960;
const TEXTW = 11906 - 2 * SIDE; // A4 (DXA)
const PXW = Math.round(TEXTW / 15); // text width in px at 96 dpi
const BODY = 19;    // 9.5 pt

// ---------------------------------------------------------------- parsing
function smart(s) {
  s = s.replace(/(\w)'(\w)/g, '$1’$2').replace(/'/g, '’');
  let open = true;
  s = s.replace(/"/g, () => { const r = open ? '“' : '”'; open = !open; return r; });
  return s;
}

function parseFile(file) {
  const lines = fs.readFileSync(file, 'utf8').split('\n');
  const blocks = [];
  let i = 0;
  const attrs = (str) => {
    const m = str.match(/\s*\{([^}]*)\}\s*$/);
    if (!m) return [str, {}];
    const a = {};
    m[1].split(/\s+/).forEach((t) => {
      if (t.startsWith('#')) a.id = t.slice(1);
      else if (t.includes('=')) { const [k, v] = t.split('='); a[k] = v; }
    });
    return [str.slice(0, m.index), a];
  };
  while (i < lines.length) {
    const ln = lines[i];
    if (!ln.trim()) { i++; continue; }
    let m;
    if ((m = ln.match(/^(#{1,4}) (.*)$/))) {
      const lvl = m[1].length;
      let [text, a] = attrs(m[2]);
      let appendix = false;
      if (lvl === 1 && text.startsWith('@')) { appendix = true; text = text.slice(1); }
      blocks.push({ t: 'h' + lvl, text: text.trim(), id: a.id, appendix });
      i++; continue;
    }
    if ((m = ln.match(/^!\[(.*)\]\((.*?)\)(\{.*\})?\s*$/))) {
      const [cap, src] = m[1].split('|');
      const a = attrs(' ' + (m[3] || ''))[1];
      blocks.push({ t: 'fig', cap: cap.trim(), src: (src || '').trim(), file: m[2], w: parseFloat(a.w || '100'), id: a.id });
      i++; continue;
    }
    if ((m = ln.match(/^Table: (.*)$/))) {
      const [cap, a] = attrs(m[1]);
      const rows = [];
      i++;
      while (i < lines.length && lines[i].startsWith('|')) {
        if (!/^\|[-| ]+\|$/.test(lines[i])) {
          rows.push(lines[i].replace(/^\||\|$/g, '').split('|').map((c) => c.trim()));
        }
        i++;
      }
      blocks.push({ t: 'table', cap: cap.trim(), id: a.id, cols: (a.cols || '').split(',').map(Number), rows });
      continue;
    }
    if ((m = ln.match(/^Decision: (.*)$/))) {
      blocks.push({ t: 'decision', text: m[1] });
      i++; continue;
    }
    if (ln.startsWith('> ')) {
      const buf = [];
      while (i < lines.length && lines[i].startsWith('> ')) { buf.push(lines[i].slice(2)); i++; }
      blocks.push({ t: 'quote', text: buf.join(' ') });
      continue;
    }
    if (/^\d+\. /.test(ln)) {
      const items = [];
      while (i < lines.length && /^\d+\. /.test(lines[i])) { items.push(lines[i].replace(/^\d+\. /, '')); i++; }
      blocks.push({ t: 'ol', items });
      continue;
    }
    if (/^- /.test(ln)) {
      const items = [];
      while (i < lines.length && /^- /.test(lines[i])) { items.push(lines[i].slice(2)); i++; }
      blocks.push({ t: 'ul', items });
      continue;
    }
    const buf = [];
    while (i < lines.length && lines[i].trim() && !/^(#{1,4} |!\[|Table: |Decision: |> |\d+\. |- )/.test(lines[i])) { buf.push(lines[i]); i++; }
    blocks.push({ t: 'p', text: buf.join(' ') });
  }
  return blocks;
}

const ONLY = (process.argv.find((a) => a.startsWith('--only=')) || '').slice(7);
const files = fs.readdirSync(SRC).filter((f) => /^\d\d-.*\.md$/.test(f) && (!ONLY || f.includes(ONLY))).sort();
let blocks = [];
files.forEach((f) => { blocks = blocks.concat(parseFile(path.join(SRC, f))); });

// ---------------------------------------------------------------- numbering
const labels = {};   // 'fig:key' -> 'Figure 5.1'
let chap = 0, appx = 0, sec = 0, sub = 0, fig = 0, tab = 0, inApp = false;
const letters = 'ABCDEFGH';
const toc = [];      // {key, level, num, title}
const lof = [];
const lot = [];
const figs = [];     // figures to export
var cur = { prefix: 'X' };
blocks.forEach((b) => {
  if (b.t === 'h1') {
    sec = 0; fig = 0; tab = 0;
    if (b.text === 'References') { b.num = ''; b.unnum = true; inApp = false; }
    else if (b.appendix) { inApp = true; b.num = 'Appendix ' + letters[appx]; b.prefix = letters[appx]; appx++; }
    else { chap++; b.num = String(chap); b.prefix = String(chap); }
    b.key = 'h:' + (b.num || b.text);
    if (b.id) labels['ch:' + b.id.replace(/^ch-/, '')] = b.appendix ? b.num : 'Chapter ' + b.num;
    if (b.id) labels['app:' + b.id.replace(/^app-/, '')] = b.num;
    b.curPrefix = b.prefix; cur = b;
    toc.push({ key: b.key, level: 1, num: b.num, title: b.text, appendix: b.appendix, unnum: b.unnum });
  } else if (b.t === 'h2') {
    sec++; sub = 0;
    b.num = (cur.prefix || '') + '.' + sec;
    b.key = 'h:' + b.num;
    if (b.id) labels['sec:' + b.id.replace(/^sec-/, '')] = 'Section ' + b.num;
    toc.push({ key: b.key, level: 2, num: b.num, title: b.text });
  } else if (b.t === 'h3') {
    sub++;
    b.num = (cur.prefix || '') + '.' + sec + '.' + sub;
    b.key = 'h:' + b.num;
    if (b.id) labels['sec:' + b.id.replace(/^sec-/, '')] = 'Section ' + b.num;
    toc.push({ key: b.key, level: 3, num: b.num, title: b.text });
  } else if (b.t === 'fig') {
    fig++; b.num = cur.prefix + '.' + fig; b.key = 'f:' + b.num;
    if (b.id) labels['fig:' + b.id] = 'Figure ' + b.num;
    lof.push({ key: b.key, num: b.num, title: b.cap });
    figs.push(b);
  } else if (b.t === 'table') {
    tab++; b.num = cur.prefix + '.' + tab; b.key = 't:' + b.num;
    if (b.id) labels['tab:' + b.id] = 'Table ' + b.num;
    lot.push({ key: b.key, num: b.num, title: b.cap });
  }
});

const unresolved = [];
function resolve(text) {
  return text.replace(/\[\[(\w+):([\w-]+)\]\]/g, (m, t, k) => {
    const v = labels[t + ':' + k];
    if (!v) { unresolved.push(m); if (!CHECK) throw new Error('Unresolved reference ' + m); return '[?]'; }
    return v;
  });
}

// ---------------------------------------------------------------- inline
function runs(text, o = {}) {
  text = smart(resolve(text));
  const parts = text.split(/(\*\*[^*]+\*\*|\*[^*]+\*)/g).filter((x) => x !== '');
  return parts.map((p) => {
    if (p.startsWith('**')) return new TR({ text: p.slice(2, -2), bold: true, ...o, ...(o.size ? { size: o.size } : {}) });
    if (p.startsWith('*')) return new TR({ text: p.slice(1, -1), italics: true, ...o });
    return new TR({ text: p, ...o });
  });
}

// ---------------------------------------------------------------- image sizes
const seenImg = {};
figs.forEach((f) => {
  const p = fpath(f.file);
  if (!fs.existsSync(p)) { console.log('MISSING IMAGE', f.file); }
  if (seenImg[p]) console.log('DUPLICATE IMAGE', f.file, 'used in Figure', seenImg[p], 'and', f.num);
  seenImg[p] = f.num;
});
if (CHECK) {
  blocks.forEach((b) => {
    [b.text, b.cap, b.src, ...(b.items || []), ...((b.rows || []).flat())].filter(Boolean).forEach((t) => resolve(t));
  });
  console.log('chapters', chap, 'appendices', appx, 'figures', figs.length, 'tables', lot.length, 'unresolved refs', unresolved.length);
  unresolved.forEach((u) => console.log('UNRESOLVED', u));
  blocks.filter((b) => b.t === 'table').forEach((t) => { const n = t.rows[0].length; t.rows.forEach((r, i) => { if (r.length !== n) console.log('TABLE ROW WIDTH', t.num, 'row', i, r.length, 'vs', n); }); if (t.cols.length && t.cols.length !== n) console.log('TABLE COLS', t.num, t.cols.length, 'vs', n); });
  process.exit(0);
}
const imgPaths = figs.map((f) => fpath(f.file));
const dims = JSON.parse(execSync('python3 -c "import sys,json;from PIL import Image;print(json.dumps({p:Image.open(p).size for p in sys.argv[1:]}))" ' + imgPaths.map((p) => JSON.stringify(p)).join(' '), { maxBuffer: 1 << 24 }).toString());

// ---------------------------------------------------------------- renderers
const B = D.BorderStyle;
const NONE = { style: B.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE };

function page(key) { return PAGES[key] !== undefined ? String(PAGES[key]) : '00'; }

function tocLine(e) {
  const o = { font: FONT };
  if (e.level === 1) {
    const bold = true;
    const wide = e.appendix;
    const pos = wide ? 1418 : 567;
    const kids = [];
    if (e.num) kids.push(new TR({ text: e.num, bold, ...o }), new TR({ children: [new D.Tab()], ...o }));
    kids.push(new TR({ text: e.title, bold, ...o }));
    kids.push(new TR({ children: [new D.Tab(), page(e.key)], bold, ...o }));
    return new D.Paragraph({
      spacing: { before: 90, after: 10 },
      indent: e.num ? { left: pos, hanging: pos, right: 0 } : {},
      tabStops: [{ type: D.TabStopType.LEFT, position: pos }, { type: D.TabStopType.RIGHT, position: TEXTW, leader: D.LeaderType.DOT }],
      children: kids,
    });
  }
  if (e.level === 3) {
    return new D.Paragraph({
      spacing: { before: 0, after: 0 },
      indent: { left: 567 + 680 + 900, hanging: 900 },
      tabStops: [{ type: D.TabStopType.LEFT, position: 567 + 680 + 900 }, { type: D.TabStopType.RIGHT, position: TEXTW, leader: D.LeaderType.DOT }],
      children: [
        new TR({ text: e.num, ...{ font: FONT } }), new TR({ children: [new D.Tab()], font: FONT }),
        new TR({ text: smart(e.title), font: FONT }),
        new TR({ children: [new D.Tab(), page(e.key)], font: FONT }),
      ],
    });
  }
  return new D.Paragraph({
    spacing: { before: 0, after: 0 },
    indent: { left: 567 + 680, hanging: 680 },
    tabStops: [{ type: D.TabStopType.LEFT, position: 567 + 680 }, { type: D.TabStopType.RIGHT, position: TEXTW, leader: D.LeaderType.DOT }],
    children: [
      new TR({ text: e.num, ...o }), new TR({ children: [new D.Tab()], ...o }),
      new TR({ text: smart(e.title), ...o }),
      new TR({ children: [new D.Tab(), page(e.key)], ...o }),
    ],
  });
}

const COLW = Math.floor((TEXTW - 360) / 2);
function listLine(kind, e) {
  const o = { font: FONT, size: 18 };
  const lab = kind + ' ' + e.num;
  return new D.Paragraph({
    spacing: { before: 20, after: 0, line: 228 },
    indent: { left: 980, hanging: 980, right: 330 },
    alignment: D.AlignmentType.LEFT,
    tabStops: [{ type: D.TabStopType.LEFT, position: 980 }, { type: D.TabStopType.RIGHT, position: COLW, leader: D.LeaderType.DOT }],
    children: [
      new TR({ text: lab, ...o }), new TR({ children: [new D.Tab()], ...o }),
      new TR({ text: smart(resolve(e.title)), ...o }),
      new TR({ children: [new D.Tab(), page(e.key)], ...o }),
    ],
  });
}

function frontHeading(text, brk = true) {
  return new D.Paragraph({
    style: 'FrontHeading', pageBreakBefore: brk,
    children: [new TR({ text })],
  });
}

function figureBlocks(b) {
  const p = fpath(b.file);
  const [w0, h0] = dims[p];
  let wpx = PXW * b.w * 0.74 / 100;
  let hpx = wpx * h0 / w0;
  const maxH = 440;
  if (hpx > maxH) { wpx = wpx * maxH / hpx; hpx = maxH; }
  const ext = path.extname(p).slice(1).toLowerCase().replace('jpeg', 'jpg');
  const out = [];
  out.push(new D.Paragraph({
    alignment: D.AlignmentType.CENTER, keepNext: true, spacing: { before: 110, after: 50 },
    children: [new D.ImageRun({ type: ext, data: fs.readFileSync(p), transformation: { width: Math.round(wpx), height: Math.round(hpx) }, altText: { title: 'Figure ' + b.num, description: b.cap, name: 'Figure ' + b.num } })],
  }));
  const short = b.cap.length < 100;
  out.push(new D.Paragraph({
    style: 'Caption', alignment: short ? D.AlignmentType.CENTER : D.AlignmentType.JUSTIFIED, keepNext: !!b.src,
    children: [new TR({ text: 'Figure ' + b.num + ': ', bold: true }), ...runs(b.cap)],
  }));
  if (b.src) out.push(new D.Paragraph({ style: 'SourceNote', alignment: D.AlignmentType.CENTER, children: runs(b.src) }));
  return out;
}

function tableBlocks(b) {
  const cols = b.cols.length ? b.cols : b.rows[0].map(() => 100 / b.rows[0].length);
  const sum = cols.reduce((a, c) => a + c, 0);
  let widths = cols.map((c) => Math.round(TEXTW * c / sum));
  widths[widths.length - 1] += TEXTW - widths.reduce((a, c) => a + c, 0);
  const heavy = { style: B.SINGLE, size: 10, color: '000000' };
  const light = { style: B.SINGLE, size: 4, color: '000000' };
  const rows = b.rows.map((r, ri) => {
    const first = ri === 0, last = ri === b.rows.length - 1;
    return new D.TableRow({
      tableHeader: first, cantSplit: true,
      children: r.map((c, ci) => new D.TableCell({
        width: { size: widths[ci], type: D.WidthType.DXA },
        margins: { top: 25, bottom: 25, left: 50, right: 50 },
        borders: { ...noBorders, ...(first ? { top: heavy, bottom: light } : {}), ...(last ? { bottom: heavy } : {}) },
        shading: { type: D.ShadingType.CLEAR, fill: 'FFFFFF', color: 'auto' },
        children: [new D.Paragraph({ style: 'TableText', children: runs(c, first ? { bold: true } : {}) })],
      })),
    });
  });
  return [
    new D.Paragraph({ style: 'TableTitle', keepNext: true, children: [new TR({ text: 'Table ' + b.num + ': ', bold: true }), ...runs(b.cap)] }),
    new D.Table({
      width: { size: TEXTW, type: D.WidthType.DXA }, columnWidths: widths, rows,
      borders: { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE },
    }),
    new D.Paragraph({ spacing: { before: 0, after: 40 }, children: [] }),
  ];
}

function bodyChildren() {
  const out = [];
  let prev = 'h';
  let inRefs = false;
  let pending = [];
  const flush = () => { pending.forEach((p) => out.push(...figureBlocks(p.b))); pending = []; };
  blocks.forEach((b) => {
    if (/^h\d$/.test(b.t) || b.t === 'table') flush();
    if (b.t === 'fig' && DELAYS[b.key] > 0) { pending.push({ b, n: DELAYS[b.key] }); return; }
    if (b.t === 'fig' && pending.length) flush();
    switch (b.t) {
      case 'h1': {
        inRefs = b.text === 'References';
        const kids = [];
        if (b.unnum) kids.push(new TR({ text: b.text }));
        else if (b.appendix) kids.push(new TR({ text: b.num + ': ' + b.text }));
        else kids.push(new TR({ text: b.num }), new TR({ children: [new D.Tab(), b.text] }));
        out.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_1, pageBreakBefore: !['ch-framework', 'ch-synthesis', 'ch-discussion', 'ch-limits', 'ch-conclusion'].includes(b.id), spacing: ['ch-framework', 'ch-synthesis', 'ch-discussion', 'ch-limits', 'ch-conclusion'].includes(b.id) ? { before: 360, after: 260 } : undefined, children: kids }));
        prev = 'h'; break;
      }
      case 'h2':
        out.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_2, children: [new TR({ text: b.num }), new TR({ children: [new D.Tab(), smart(b.text)] })] }));
        prev = 'h'; break;
      case 'h3':
        out.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_3, children: [new TR({ text: b.num }), new TR({ children: [new D.Tab(), smart(b.text)] })] }));
        prev = 'h'; break;
      case 'h4':
        out.push(new D.Paragraph({ style: 'RunIn', children: runs(b.text) }));
        prev = 'h'; break;
      case 'p': {
        if (inRefs) { out.push(new D.Paragraph({ style: 'RefPara', children: runs(b.text) })); prev = 'r'; break; }
        const ind = prev === 'p';
        const isNote = false;
        out.push(new D.Paragraph({ style: ind ? 'BodyIndent' : 'Normal', children: runs(b.text) }));
        prev = 'p'; break;
      }
      case 'decision':
        out.push(new D.Paragraph({ style: 'DecisionBox', children: [new TR({ text: 'Decision. ', bold: true }), ...runs(b.text)] }));
        prev = 'q'; break;
      case 'quote':
        out.push(new D.Paragraph({ style: 'Quote', children: runs(b.text) }));
        prev = 'q'; break;
      case 'ul':
        b.items.forEach((t) => out.push(new D.Paragraph({ style: 'ListPara', numbering: { reference: 'bul', level: 0 }, children: runs(t) })));
        prev = 'l'; break;
      case 'ol': {
        const ref = 'num' + (out.length);
        numberingRefs.push(ref);
        b.items.forEach((t) => out.push(new D.Paragraph({ style: 'ListPara', numbering: { reference: ref, level: 0 }, children: runs(t) })));
        prev = 'l'; break;
      }
      case 'fig': out.push(...figureBlocks(b)); prev = 'f'; break;
      case 'table': out.push(...tableBlocks(b)); prev = 't'; break;
    }
    if (['p', 'ul', 'ol', 'quote', 'decision'].includes(b.t) && pending.length) {
      pending.forEach((p) => { p.n -= 1; });
      const ready = pending.filter((p) => p.n <= 0);
      pending = pending.filter((p) => p.n > 0);
      ready.forEach((p) => { out.push(...figureBlocks(p.b)); prev = 'f'; });
    }
  });
  flush();
  return out;
}
const numberingRefs = [];

// ---------------------------------------------------------------- front matter
const ABSTRACT = [
  'This document records a six-week systems thinking and design project on the breakfast service in the four dining halls of the International Institute of Information Technology, Hyderabad, where students are registered automatically for meals that many of them do not eat. Following a framework of four phases, ten activities and fifteen deliverables, the team defined the system boundary, mapped twenty-four stakeholders, analysed authority and leverage decision by decision, traced the process in three kitchens, and analysed a month of scan records from Kadamba (32,162 breakfast registrations) and twenty days of attendance registers from Yuktāhār.',
  'About 63 per cent of Kadamba’s breakfast registrations in April 2026 and about 72 per cent of Yuktāhār’s in September went unused, while lunch at Yuktāhār ran at 56 to 89 per cent. A strict loop test showed that only three of eighteen suspected feedback mechanisms close with every link evidenced, and all three sit inside a kitchen. The problem was reframed as a stable equilibrium held by three structures: a default registration with a narrow exit, billing at the registration and not at the plate, and a gap that is measured twice and routed to no one who sets the rules.',
  'Twelve leverage points, seven design principles and eight intervention concepts were developed and tested on paper, through a backtest on Kadamba’s records, simulated stakeholder responses and four pass-or-fail gates. The recommendation is to build the missing routes, to change the default through a Sunday skip on a fixed date, and to tune the kitchen alongside, with a pilot on Kadamba’s vegetarian Sunday line. The projections are model results and have not been tested on the campus.',
];
const KEYWORDS = 'systems thinking; causal loop analysis; leverage points; food waste; institutional catering; service design';
const ACK = 'The team thanks the students, the facilities and dining staff, and the caterers’ managers and supervisors who gave their time for interviews and kitchen visits and allowed their records to be photographed, and the course instructors for their guidance. Every person who took part is referred to by role in this document.';

function titlePage() {
  const c = (text, size, o = {}, before = 0, after = 0) => new D.Paragraph({
    alignment: D.AlignmentType.CENTER, spacing: { before, after },
    children: [new TR({ text, size, ...o })],
  });
  return [
    c('International Institute of Information Technology, Hyderabad', 28, {}, 600, 60),
    c('Systems Thinking and Design', 24, { italics: true }, 0, 1500),
    new D.Paragraph({ alignment: D.AlignmentType.CENTER, spacing: { before: 0, after: 0 }, border: { top: { style: B.SINGLE, size: 12, color: '000000', space: 14 } }, children: [new TR({ text: 'The Breakfast Paradox', size: 64, bold: true })] }),
    new D.Paragraph({ alignment: D.AlignmentType.CENTER, spacing: { before: 200, after: 0 }, border: { bottom: { style: B.SINGLE, size: 12, color: '000000', space: 14 } }, children: [new TR({ text: 'A Systems Analysis of Breakfast Registration and Food Waste in the Dining Halls', size: 30 })] }),
    c('Project Documentation', 32, { bold: true }, 900, 1500),
    c('Team Invictus', 28, { bold: true }, 0, 120),
    c('Sricharan Peri', 26, {}, 0, 0),
    c('Prathyusha Kalluri', 26, {}, 0, 0),
    c('Neha', 26, {}, 0, 1500),
    c('October 2026', 26, {}, 0, 0),
  ];
}

function frontChildren() {
  const out = [];
  out.push(frontHeading('Abstract', false));
  ABSTRACT.forEach((t, i) => out.push(new D.Paragraph({ style: i === 0 ? 'Normal' : 'BodyIndent', children: runs(t) })));
  out.push(new D.Paragraph({ spacing: { before: 200 }, alignment: D.AlignmentType.LEFT, children: [new TR({ text: 'Keywords: ', bold: true }), new TR({ text: KEYWORDS, italics: true })] }));
  out.push(new D.Paragraph({ style: 'FrontHeading', spacing: { before: 360, after: 200 }, keepNext: true, children: [new TR({ text: 'Acknowledgements' })] }));
  out.push(new D.Paragraph({ children: runs(ACK) }));
  out.push(frontHeading('Contents'));
  toc.filter((e) => e.level <= 2).forEach((e) => out.push(tocLine(e)));
  return out;
}
function listChildren() {
  const out = [];
  out.push(frontHeading('List of Figures', false));
  lof.forEach((e) => out.push(listLine('Figure', e)));
  out.push(new D.Paragraph({ style: 'FrontHeading', spacing: { before: 360, after: 200 }, keepNext: true, children: [new TR({ text: 'List of Tables' })] }));
  lot.forEach((e) => out.push(listLine('Table', e)));
  return out;
}

// ---------------------------------------------------------------- document
function header() {
  return new D.Header({
    children: [new D.Paragraph({
      tabStops: [{ type: D.TabStopType.RIGHT, position: TEXTW }],
      border: { bottom: { style: B.SINGLE, size: 6, color: '000000', space: 4 } },
      spacing: { after: 0 },
      children: [
        new TR({ text: 'The Breakfast Paradox', italics: true, size: 20 }),
        new TR({ children: [new D.Tab(), 'Team Invictus, IIIT Hyderabad'], italics: true, size: 20 }),
      ],
    })],
  });
}
function footer() {
  return new D.Footer({ children: [new D.Paragraph({ alignment: D.AlignmentType.CENTER, children: [new TR({ children: [D.PageNumber.CURRENT], size: 22 })] })] });
}

const pageProps = (fmt, start) => ({
  size: { width: 11906, height: 16838 },
  margin: { top: 1130, bottom: 1130, left: SIDE, right: SIDE, header: 640, footer: 640 },
  ...(fmt ? { pageNumbers: { ...(start ? { start } : {}), formatType: fmt } } : {}),
});

const body = bodyChildren();
const numberingConfig = [
  { reference: 'bul', levels: [{ level: 0, format: D.LevelFormat.BULLET, text: '•', alignment: D.AlignmentType.LEFT, style: { run: { font: FONT, size: BODY }, paragraph: { indent: { left: 720, hanging: 360 } } } }] },
  ...numberingRefs.map((r) => ({ reference: r, levels: [{ level: 0, format: D.LevelFormat.DECIMAL, text: '%1.', alignment: D.AlignmentType.LEFT, style: { run: { font: FONT, size: BODY }, paragraph: { indent: { left: 720, hanging: 360 } } } }] })),
];

const doc = new D.Document({
  creator: ' ', lastModifiedBy: ' ', title: 'The Breakfast Paradox', description: '',
  fonts: [
    { name: FONT, data: fs.readFileSync(path.join(SUB, 'Fonts', 'LMRoman10-Regular.ttf')) },
    { name: FONTB, data: fs.readFileSync(path.join(SUB, 'Fonts', 'LMRoman10-Bold.ttf')) },
    { name: FONTI, data: fs.readFileSync(path.join(SUB, 'Fonts', 'LMRoman10-Italic.ttf')) },
  ],
  numbering: { config: numberingConfig },
  styles: {
    default: {
      document: { run: { font: FONT, size: BODY }, paragraph: { spacing: { line: 240, after: 20 }, alignment: D.AlignmentType.JUSTIFIED } },
      heading1: { run: { font: FONTB, size: 40, color: '000000' }, paragraph: { spacing: { before: 0, after: 260 }, alignment: D.AlignmentType.LEFT, indent: { left: 720, hanging: 720 }, keepNext: true } },
      heading2: { run: { font: FONTB, size: 28, color: '000000' }, paragraph: { spacing: { before: 220, after: 90 }, alignment: D.AlignmentType.LEFT, indent: { left: 720, hanging: 720 }, keepNext: true } },
      heading3: { run: { font: FONTB, size: 24, color: '000000' }, paragraph: { spacing: { before: 170, after: 60 }, alignment: D.AlignmentType.LEFT, indent: { left: 900, hanging: 900 }, keepNext: true } },
    },
    paragraphStyles: [
      { id: 'BodyIndent', name: 'Body Indent', basedOn: 'Normal', quickFormat: true, paragraph: { indent: { firstLine: 360 } } },
      { id: 'RunIn', name: 'Run In', basedOn: 'Normal', next: 'Normal', run: { font: FONTB }, paragraph: { spacing: { before: 110, after: 30 }, alignment: D.AlignmentType.LEFT, keepNext: true } },
      { id: 'Caption', name: 'Caption', basedOn: 'Normal', run: { size: 20 }, paragraph: { spacing: { before: 40, after: 20 }, indent: { left: 360, right: 360 } } },
      { id: 'SourceNote', name: 'Source Note', basedOn: 'Normal', run: { font: FONTI, size: 18 }, paragraph: { spacing: { before: 0, after: 130 }, indent: { left: 360, right: 360 } } },
      { id: 'TableTitle', name: 'Table Title', basedOn: 'Normal', run: { size: 20 }, paragraph: { spacing: { before: 120, after: 60 }, alignment: D.AlignmentType.LEFT } },
      { id: 'TableText', name: 'Table Text', basedOn: 'Normal', run: { size: 15 }, paragraph: { spacing: { before: 0, after: 0, line: 228 }, alignment: D.AlignmentType.LEFT } },
      { id: 'Quote', name: 'Quote Block', basedOn: 'Normal', run: { font: FONTI }, paragraph: { spacing: { before: 100, after: 140 }, indent: { left: 720, right: 720 } } },
      { id: 'RefPara', name: 'Reference', basedOn: 'Normal', paragraph: { spacing: { after: 120 }, indent: { left: 720, hanging: 720 }, alignment: D.AlignmentType.LEFT } },
      { id: 'DecisionBox', name: 'Decision Box', basedOn: 'Normal', paragraph: { spacing: { before: 100, after: 120 }, indent: { left: 360, right: 200 }, alignment: D.AlignmentType.LEFT, border: { left: { style: B.SINGLE, size: 18, color: '000000', space: 8 } } } },
      { id: 'ListPara', name: 'List Para', basedOn: 'Normal', paragraph: { spacing: { after: 40 } } },
      { id: 'FrontHeading', name: 'Front Heading', basedOn: 'Normal', next: 'Normal', run: { font: FONTB, size: 40 }, paragraph: { alignment: D.AlignmentType.LEFT, spacing: { before: 0, after: 360 }, keepNext: true } },
    ],
  },
  sections: [
    { properties: { page: pageProps() }, children: titlePage() },
    { properties: { page: pageProps(D.NumberFormat.LOWER_ROMAN, 2) }, headers: { default: header() }, footers: { default: footer() }, children: frontChildren() },
    { properties: { type: D.SectionType.NEXT_PAGE, column: { count: 2, space: 360 }, page: pageProps(D.NumberFormat.LOWER_ROMAN) }, headers: { default: header() }, footers: { default: footer() }, children: listChildren() },
    { properties: { page: pageProps(D.NumberFormat.DECIMAL, 1) }, headers: { default: header() }, footers: { default: footer() }, children: body },
  ],
});

D.Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  // export entries for the page-number pass
  fs.writeFileSync(path.join(__dirname, 'entries.json'), JSON.stringify({
    toc, lof, lot,
  }, null, 1));
  // export figure files
  fs.mkdirSync(FIGDIR, { recursive: true });
  fs.readdirSync(FIGDIR).filter((x) => x.startsWith('Figure_')).forEach((x) => fs.unlinkSync(path.join(FIGDIR, x)));
  figs.forEach((f) => {
    const src = fpath(f.file);
    const slug = (f.id || path.basename(f.file, path.extname(f.file))).replace(/[^\w-]+/g, '-');
    const name = 'Figure_' + f.num + '_' + slug + path.extname(f.file);
    fs.copyFileSync(src, path.join(FIGDIR, name));
  });
  console.log('wrote', OUT, buf.length, 'bytes;', figs.length, 'figures;', lot.length, 'tables;', toc.length, 'toc entries');
});
