// Builds the case study as one Word file.
// Usage: node build_case.js OUT.docx [pages.json]
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const D = require('docx');

const CS = path.resolve(__dirname, '..');           // CaseStudy/
const SUB = path.resolve(CS, '..');                 // submission/
const WORK = path.join(__dirname, 'work');
const OUT = process.argv[2] || path.join(CS, 'Breakfast_Paradox_Case_Study.docx');
const PAGES = process.argv[3] && fs.existsSync(process.argv[3]) ? JSON.parse(fs.readFileSync(process.argv[3], 'utf8')) : {};
const FIGDIR = path.join(CS, 'Figures');

const FONT = 'LM Roman 10';
const FONTB = 'LM Roman 10 Bold';
const FONTI = 'LM Roman 10 Italic';
function TR(o) {
  o = { ...o };
  if (o.bold) { o.font = FONTB; delete o.bold; delete o.italics; }
  else if (o.italics) { o.font = FONTI; delete o.italics; }
  else if (!o.font) o.font = FONT;
  return new D.TextRun(o);
}
const SIDE = 1304;                      // 23 mm
const TEXTW = 11906 - 2 * SIDE;         // 9072 DXA
const PXW = Math.round(TEXTW / 15);
const BODY = 21;                        // 10.5 pt

function smart(s) {
  s = s.replace(/(\w)'(\w)/g, '$1’$2').replace(/'/g, '’');
  let open = true;
  s = s.replace(/"/g, () => { const r = open ? '“' : '”'; open = !open; return r; });
  return s;
}
function runs(text, o = {}) {
  text = smart(text);
  const parts = text.split(/(\*\*[^*]+\*\*|\*[^*]+\*)/g).filter((x) => x !== '');
  return parts.map((p) => {
    if (p.startsWith('**')) return new TR({ text: p.slice(2, -2), bold: true, ...o });
    if (p.startsWith('*')) return new TR({ text: p.slice(1, -1), italics: true, ...o });
    return new TR({ text: p, ...o });
  });
}

// ---------------------------------------------------------------- parse
function attrs(str) {
  const m = str.match(/\s*\{([^}]*)\}\s*$/);
  if (!m) return [str, {}];
  const a = {};
  m[1].split(/\s+/).forEach((t) => {
    if (t.startsWith('#')) a.id = t.slice(1);
    else if (t.includes('=')) { const [k, v] = t.split('='); a[k] = v; }
  });
  return [str.slice(0, m.index), a];
}
const lines = fs.readFileSync(path.join(CS, 'Source', 'case2.md'), 'utf8').split('\n');
const blocks = [];
for (let i = 0; i < lines.length;) {
  const ln = lines[i];
  let m;
  if (!ln.trim()) { i++; continue; }
  if (ln.startsWith('::: facts')) {
    const rows = []; i++;
    while (i < lines.length && !lines[i].startsWith(':::')) { rows.push(lines[i].split(' | ')); i++; }
    i++; blocks.push({ t: 'facts', rows }); continue;
  }
  if ((m = ln.match(/^::: decision (.*)$/))) {
    const rows = []; i++;
    while (i < lines.length && !lines[i].startsWith(':::')) { rows.push(lines[i].split(' | ')); i++; }
    i++; blocks.push({ t: 'decision', title: m[1].trim(), rows }); continue;
  }
  if (ln.startsWith('Contents:')) { blocks.push({ t: 'contents' }); i++; continue; }
  if (ln.startsWith('End: ')) { blocks.push({ t: 'end', text: ln.slice(5) }); i++; continue; }
  if ((m = ln.match(/^(##|###) (.*)$/))) { const [text, a] = attrs(m[2]); blocks.push({ t: m[1] === '##' ? 'h2' : 'h3', text: text.trim(), id: a.id }); i++; continue; }
  if ((m = ln.match(/^!\[(.*)\]\((.*?)\)(\{.*\})?\s*$/))) {
    const a = attrs(' ' + (m[3] || ''))[1];
    blocks.push({ t: 'fig', cap: m[1].trim(), file: m[2], w: parseFloat(a.w || '100'), crop: a.crop, id: a.id }); i++; continue;
  }
  if ((m = ln.match(/^Table: (.*)$/))) {
    const [cap, a] = attrs(m[1]); const rows = []; i++;
    while (i < lines.length && lines[i].startsWith('|')) { rows.push(lines[i].replace(/^\||\|$/g, '').split('|').map((c) => c.trim())); i++; }
    blocks.push({ t: 'table', cap: cap.trim(), id: a.id, cols: (a.cols || '').split(',').map(Number), rows }); continue;
  }
  if (ln.startsWith('> ')) {
    const buf = [];
    while (i < lines.length && lines[i].startsWith('> ')) { buf.push(lines[i].slice(2)); i++; }
    blocks.push({ t: 'quote', text: buf.join(' ') }); continue;
  }
  if (/^\d+\. /.test(ln)) {
    const items = [];
    while (i < lines.length && /^\d+\. /.test(lines[i])) { items.push(lines[i].replace(/^\d+\. /, '')); i++; }
    blocks.push({ t: 'ol', items }); continue;
  }
  const buf = [];
  while (i < lines.length && lines[i].trim() && !/^(##|###) |^!\[|^Table: |^End: |^::: |^Contents:|^> |^\d+\. /.test(lines[i])) { buf.push(lines[i]); i++; }
  blocks.push({ t: 'p', text: buf.join(' ') });
}

// numbering
let sec = 0, sub = 0, fig = 0, tab = 0, dec = 0;
const entries = [];   // for the page pass
const tocList = [], decList = [];
blocks.forEach((b) => {
  if (b.t === 'h2') {
    if (b.text === 'Summary') { b.num = ''; b.key = 'h:summary'; return; }
    sec++; sub = 0; b.num = String(sec); b.key = 'h:' + b.num;
    entries.push({ key: b.key, kind: 'h', num: b.num, title: b.text }); tocList.push({ key: b.key, level: 1, num: b.num, title: b.text });
  }
  if (b.t === 'h3') {
    sub++; b.num = sec + '.' + sub; b.key = 'h:' + b.num;
    entries.push({ key: b.key, kind: 'h', num: b.num, title: b.text }); tocList.push({ key: b.key, level: 2, num: b.num, title: b.text });
  }
  if (b.t === 'fig') { fig++; b.num = String(fig); entries.push({ key: 'f:' + fig, kind: 'f', num: b.num }); }
  if (b.t === 'table') { tab++; b.num = String(tab); entries.push({ key: 't:' + tab, kind: 't', num: b.num }); }
  if (b.t === 'decision') { dec++; b.num = String(dec); b.key = 'd:' + dec; entries.push({ key: b.key, kind: 'd', num: b.num, title: b.title }); decList.push({ key: b.key, num: b.num, title: b.title }); }
});
function page(key) { return PAGES[key] !== undefined ? String(PAGES[key]) : '0'; }

// ---------------------------------------------------------------- images
const imgOf = (b) => (b.crop ? path.join(WORK, 'img', b.crop + '.png') : path.join(SUB, b.file));
const figs = blocks.filter((b) => b.t === 'fig');
const seen = {};
figs.forEach((f) => {
  if (!fs.existsSync(imgOf(f))) { console.log('MISSING IMAGE', imgOf(f)); process.exit(1); }
  if (seen[imgOf(f)]) console.log('DUPLICATE IMAGE', f.file);
  seen[imgOf(f)] = 1;
});
const dims = JSON.parse(execSync('python3 -c "import sys,json;from PIL import Image;print(json.dumps({p:Image.open(p).size for p in sys.argv[1:]}))" ' + figs.map((f) => JSON.stringify(imgOf(f))).join(' '), { maxBuffer: 1 << 24 }).toString());

// ---------------------------------------------------------------- renderers
const B = D.BorderStyle;
const NONE = { style: B.NONE, size: 0, color: 'FFFFFF' };
const noBorders = { top: NONE, bottom: NONE, left: NONE, right: NONE };
const heavy = { style: B.SINGLE, size: 10, color: '000000' };
const light = { style: B.SINGLE, size: 4, color: '000000' };
const grey = { style: B.SINGLE, size: 4, color: '808080' };

function factsBlock(b) {
  const lw = 1500;
  const rows = b.rows.map((r, ri) => new D.TableRow({
    cantSplit: true,
    children: [
      new D.TableCell({ width: { size: lw, type: D.WidthType.DXA }, margins: { top: 45, bottom: 45, left: 0, right: 100 }, borders: { ...noBorders, ...(ri === 0 ? { top: heavy } : {}), ...(ri === b.rows.length - 1 ? { bottom: heavy } : {}) },
        children: [new D.Paragraph({ style: 'FactText', children: [new TR({ text: r[0].toUpperCase(), bold: true, size: 16 })] })] }),
      new D.TableCell({ width: { size: TEXTW - lw, type: D.WidthType.DXA }, margins: { top: 45, bottom: 45, left: 100, right: 0 }, borders: { ...noBorders, ...(ri === 0 ? { top: heavy } : {}), ...(ri === b.rows.length - 1 ? { bottom: heavy } : {}) },
        children: [new D.Paragraph({ style: 'FactText', children: runs(r[1]) })] }),
    ],
  }));
  return [new D.Table({ width: { size: TEXTW, type: D.WidthType.DXA }, columnWidths: [lw, TEXTW - lw], rows, borders: { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE } }),
    new D.Paragraph({ spacing: { before: 0, after: 80 }, children: [] })];
}

function decisionBlock(b) {
  const lw = 1350;
  const n = b.rows.length;
  const head = new D.TableRow({ cantSplit: true, children: [new D.TableCell({
    columnSpan: 2, width: { size: TEXTW, type: D.WidthType.DXA }, margins: { top: 60, bottom: 60, left: 110, right: 110 },
    shading: { type: D.ShadingType.CLEAR, fill: 'E8E8E8', color: 'auto' },
    borders: { top: heavy, bottom: grey, left: grey, right: grey },
    children: [new D.Paragraph({ style: 'DecText', keepNext: true, children: [new TR({ text: 'DECISION ' + b.num, bold: true, size: 16, characterSpacing: 10 }), new TR({ text: '   ' }), new TR({ text: smart('Decision: ' + b.title), bold: true })] })],
  })] });
  const rows = b.rows.map((r, ri) => new D.TableRow({ cantSplit: true, children: [
    new D.TableCell({ width: { size: lw, type: D.WidthType.DXA }, margins: { top: 40, bottom: 40, left: 110, right: 60 },
      borders: { top: NONE, bottom: ri === n - 1 ? heavy : NONE, left: grey, right: NONE },
      children: [new D.Paragraph({ style: 'DecText', keepNext: ri % 2 === 0 && ri < n - 1, children: [new TR({ text: r[0], bold: true })] })] }),
    new D.TableCell({ width: { size: TEXTW - lw, type: D.WidthType.DXA }, margins: { top: 40, bottom: 40, left: 60, right: 110 },
      borders: { top: NONE, bottom: ri === n - 1 ? heavy : NONE, left: NONE, right: grey },
      children: [new D.Paragraph({ style: 'DecText', keepNext: ri % 2 === 0 && ri < n - 1, children: runs(r[1]) })] }),
  ] }));
  return [new D.Paragraph({ spacing: { before: 60, after: 0 }, keepNext: true, children: [] }),
    new D.Table({ width: { size: TEXTW, type: D.WidthType.DXA }, columnWidths: [lw, TEXTW - lw], rows: [head, ...rows], borders: { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE } }),
    new D.Paragraph({ spacing: { before: 0, after: 140 }, children: [] })];
}

function figureBlocks(b) {
  const p = imgOf(b);
  const [w0, h0] = dims[p];
  let wpx = PXW * b.w / 100;
  let hpx = wpx * h0 / w0;
  const maxH = 400;
  if (hpx > maxH) { wpx = wpx * maxH / hpx; hpx = maxH; }
  const ext = path.extname(p).slice(1).toLowerCase().replace('jpeg', 'jpg');
  return [
    new D.Paragraph({ alignment: D.AlignmentType.CENTER, keepNext: true, spacing: { before: 140, after: 60 },
      children: [new D.ImageRun({ type: ext, data: fs.readFileSync(p), transformation: { width: Math.round(wpx), height: Math.round(hpx) }, altText: { title: 'Figure ' + b.num, description: b.cap, name: 'Figure ' + b.num } })] }),
    new D.Paragraph({ style: 'Caption', alignment: b.cap.length < 110 ? D.AlignmentType.CENTER : D.AlignmentType.JUSTIFIED,
      children: [new TR({ text: 'Figure ' + b.num + '. ', bold: true }), ...runs(b.cap)] }),
  ];
}

function tableBlocks(b) {
  const cols = b.cols.length ? b.cols : b.rows[0].map(() => 100 / b.rows[0].length);
  const sum = cols.reduce((a, c) => a + c, 0);
  const widths = cols.map((c) => Math.round(TEXTW * c / sum));
  widths[widths.length - 1] += TEXTW - widths.reduce((a, c) => a + c, 0);
  const rows = b.rows.map((r, ri) => {
    const first = ri === 0, last = ri === b.rows.length - 1;
    return new D.TableRow({
      tableHeader: first, cantSplit: true,
      children: r.map((c, ci) => new D.TableCell({
        width: { size: widths[ci], type: D.WidthType.DXA },
        margins: { top: 45, bottom: 45, left: 70, right: 70 },
        borders: { ...noBorders, ...(first ? { top: heavy, bottom: light } : {}), ...(last ? { bottom: heavy } : {}) },
        children: [new D.Paragraph({ style: 'TableText', keepNext: !last && b.rows.length <= 6, children: runs(c, first ? { bold: true } : {}) })],
      })),
    });
  });
  return [
    new D.Paragraph({ style: 'TableTitle', keepNext: true, children: [new TR({ text: 'Table ' + b.num + '. ', bold: true }), ...runs(b.cap)] }),
    new D.Table({ width: { size: TEXTW, type: D.WidthType.DXA }, columnWidths: widths, rows, borders: { top: NONE, bottom: NONE, left: NONE, right: NONE, insideHorizontal: NONE, insideVertical: NONE } }),
    new D.Paragraph({ spacing: { before: 0, after: 100 }, children: [] }),
  ];
}

function contentsBlocks() {
  const out = [new D.Paragraph({ style: 'FrontHeading', pageBreakBefore: true, children: [new TR({ text: 'Contents', bold: true })] })];
  tocList.forEach((e) => {
    const l1 = e.level === 1;
    const pos = l1 ? 520 : 1180;
    out.push(new D.Paragraph({
      alignment: D.AlignmentType.LEFT,
      spacing: { before: l1 ? 60 : 0, after: 0, line: 232 },
      indent: { left: pos, hanging: l1 ? 520 : 660 },
      tabStops: [{ type: D.TabStopType.LEFT, position: pos }, { type: D.TabStopType.RIGHT, position: TEXTW, leader: D.LeaderType.DOT }],
      children: [new TR({ text: e.num, bold: l1, size: 20 }), new TR({ children: [new D.Tab()], size: 20 }), new TR({ text: smart(e.title), bold: l1, size: 20 }), new TR({ children: [new D.Tab(), page(e.key)], bold: l1, size: 20 })],
    }));
  });
  out.push(new D.Paragraph({ style: 'FrontHeading', pageBreakBefore: true, children: [new TR({ text: 'Key decisions', bold: true })] }));
  decList.forEach((e) => {
    out.push(new D.Paragraph({
      alignment: D.AlignmentType.LEFT, spacing: { before: 0, after: 0, line: 232 },
      indent: { left: 520, hanging: 520 },
      tabStops: [{ type: D.TabStopType.LEFT, position: 520 }, { type: D.TabStopType.RIGHT, position: TEXTW, leader: D.LeaderType.DOT }],
      children: [new TR({ text: e.num, size: 20 }), new TR({ children: [new D.Tab()], size: 20 }), new TR({ text: smart(e.title), size: 20 }), new TR({ children: [new D.Tab(), page(e.key)], size: 20 })],
    }));
  });
  const first = (c) => c.split(/\.\s/)[0].replace(/\.$/, '');
  out.push(new D.Paragraph({ style: 'FrontSub', keepNext: true, children: [new TR({ text: 'Figures', bold: true })] }));
  blocks.filter((b) => b.t === 'fig').forEach((b) => out.push(listLine('Figure ' + b.num, first(b.cap), page('f:' + b.num))));
  return out;
}
function listLine(lab, title, pg) {
  return new D.Paragraph({
    alignment: D.AlignmentType.LEFT, spacing: { before: 0, after: 0, line: 232 },
    indent: { left: 1100, hanging: 1100 },
    tabStops: [{ type: D.TabStopType.LEFT, position: 1100 }, { type: D.TabStopType.RIGHT, position: TEXTW, leader: D.LeaderType.DOT }],
    children: [new TR({ text: lab, size: 20 }), new TR({ children: [new D.Tab()], size: 20 }), new TR({ text: smart(title), size: 20 }), new TR({ children: [new D.Tab(), pg], size: 20 })],
  });
}

const numberingRefs = [];
function bodyChildren() {
  const out = [];
  let prev = 'h';
  let firstSec = true;
  blocks.forEach((b) => {
    switch (b.t) {
      case 'facts': out.push(...factsBlock(b)); prev = 'x'; break;
      case 'contents': out.push(...contentsBlocks()); prev = 'x'; break;
      case 'end': out.push(new D.Paragraph({ style: 'EndNote', children: runs(b.text) })); prev = 'x'; break;
      case 'h2':
        if (b.text === 'Summary') {
          out.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_2, spacing: { before: 120, after: 100 }, indent: { left: 0, hanging: 0 }, children: [new TR({ text: 'Summary' })] }));
        } else {
          out.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_2, pageBreakBefore: firstSec, children: [new TR({ text: b.num }), new TR({ children: [new D.Tab(), smart(b.text)] })] }));
          firstSec = false;
        }
        prev = 'h'; break;
      case 'h3':
        out.push(new D.Paragraph({ heading: D.HeadingLevel.HEADING_3, children: [new TR({ text: b.num }), new TR({ children: [new D.Tab(), smart(b.text)] })] }));
        prev = 'h'; break;
      case 'p': out.push(new D.Paragraph({ style: prev === 'p' ? 'BodyIndent' : 'Normal', children: runs(b.text) })); prev = 'p'; break;
      case 'quote': out.push(new D.Paragraph({ style: 'Quote', children: runs(b.text) })); prev = 'q'; break;
      case 'decision': out.push(...decisionBlock(b)); prev = 'q'; break;
      case 'ol': {
        const ref = 'num' + out.length; numberingRefs.push(ref);
        b.items.forEach((t) => out.push(new D.Paragraph({ style: 'ListPara', numbering: { reference: ref, level: 0 }, children: runs(t) })));
        prev = 'l'; break;
      }
      case 'fig': out.push(...figureBlocks(b)); prev = 'f'; break;
      case 'table': out.push(...tableBlocks(b)); prev = 't'; break;
    }
  });
  return out;
}

function titleBlock() {
  return [
    new D.Paragraph({ alignment: D.AlignmentType.LEFT, spacing: { before: 0, after: 100 }, children: [new TR({ text: 'CASE STUDY, SYSTEMS THINKING AND DESIGN, IIIT HYDERABAD, SEPTEMBER TO OCTOBER 2026', size: 17, characterSpacing: 20 })] }),
    new D.Paragraph({ alignment: D.AlignmentType.LEFT, spacing: { before: 0, after: 60 }, children: [new TR({ text: 'The Breakfast Paradox', bold: true, size: 56 })] }),
    new D.Paragraph({ alignment: D.AlignmentType.LEFT, spacing: { before: 0, after: 200, line: 276 }, children: [new TR({ text: 'A systems study of breakfast registration and food waste in the hostel dining halls', italics: true, size: 28 })] }),
  ];
}

function hdr(side) {
  return new D.Header({ children: [new D.Paragraph({
    alignment: side === 'r' ? D.AlignmentType.RIGHT : D.AlignmentType.LEFT,
    border: { bottom: { style: B.SINGLE, size: 4, color: '000000', space: 4 } }, spacing: { after: 0 },
    children: [new TR({ text: side === 'r' ? 'CASE STUDY, IIIT HYDERABAD' : 'THE BREAKFAST PARADOX', size: 17, characterSpacing: 10 })],
  })] });
}
const emptyHdr = () => new D.Header({ children: [new D.Paragraph({ children: [] })] });
const ftr = () => new D.Footer({ children: [new D.Paragraph({ alignment: D.AlignmentType.CENTER, children: [new TR({ children: [D.PageNumber.CURRENT], size: 18 })] })] });

const body = [...titleBlock(), ...bodyChildren()];
const numberingConfig = numberingRefs.map((r) => ({ reference: r, levels: [{ level: 0, format: D.LevelFormat.DECIMAL, text: '%1.', alignment: D.AlignmentType.LEFT, style: { run: { font: FONT, size: BODY }, paragraph: { indent: { left: 500, hanging: 360 } } } }] }));

const doc = new D.Document({
  creator: ' ', lastModifiedBy: ' ', title: ' ', description: ' ',
  evenAndOddHeaderFooter: true,
  fonts: [
    { name: FONT, data: fs.readFileSync(path.join(SUB, 'Fonts', 'LMRoman10-Regular.ttf')) },
    { name: FONTB, data: fs.readFileSync(path.join(SUB, 'Fonts', 'LMRoman10-Bold.ttf')) },
    { name: FONTI, data: fs.readFileSync(path.join(SUB, 'Fonts', 'LMRoman10-Italic.ttf')) },
  ],
  numbering: { config: numberingConfig },
  styles: {
    default: {
      document: { run: { font: FONT, size: BODY }, paragraph: { spacing: { line: 264, after: 0 }, alignment: D.AlignmentType.JUSTIFIED } },
      heading2: { run: { font: FONTB, size: 30, color: '000000' }, paragraph: { spacing: { before: 360, after: 140 }, alignment: D.AlignmentType.LEFT, indent: { left: 560, hanging: 560 }, keepNext: true } },
      heading3: { run: { font: FONTB, size: 24, color: '000000' }, paragraph: { spacing: { before: 240, after: 90 }, alignment: D.AlignmentType.LEFT, indent: { left: 560, hanging: 560 }, keepNext: true } },
    },
    paragraphStyles: [
      { id: 'BodyIndent', name: 'Body Indent', basedOn: 'Normal', quickFormat: true, paragraph: { indent: { firstLine: 300 } } },
      { id: 'Caption', name: 'Caption', basedOn: 'Normal', run: { size: 19 }, paragraph: { spacing: { before: 20, after: 200, line: 252 }, indent: { left: 300, right: 300 } } },
      { id: 'TableTitle', name: 'Table Title', basedOn: 'Normal', run: { size: 19 }, paragraph: { spacing: { before: 160, after: 80 }, alignment: D.AlignmentType.LEFT } },
      { id: 'TableText', name: 'Table Text', basedOn: 'Normal', run: { size: 18 }, paragraph: { spacing: { before: 0, after: 0, line: 240 }, alignment: D.AlignmentType.LEFT } },
      { id: 'FactText', name: 'Fact Text', basedOn: 'Normal', run: { size: 19 }, paragraph: { spacing: { before: 0, after: 0, line: 252 }, alignment: D.AlignmentType.LEFT } },
      { id: 'DecText', name: 'Decision Text', basedOn: 'Normal', run: { size: 19 }, paragraph: { spacing: { before: 0, after: 0, line: 250 }, alignment: D.AlignmentType.LEFT } },
      { id: 'Quote', name: 'Quote Block', basedOn: 'Normal', run: { font: FONTI }, paragraph: { spacing: { before: 100, after: 140 }, indent: { left: 700, right: 500 }, border: { left: { style: B.SINGLE, size: 8, color: '000000', space: 10 } } } },
      { id: 'ListPara', name: 'List Para', basedOn: 'Normal', paragraph: { spacing: { after: 80 } } },
      { id: 'EndNote', name: 'End Note', basedOn: 'Normal', run: { font: FONTI, size: 19 }, paragraph: { spacing: { before: 240, after: 0 }, alignment: D.AlignmentType.LEFT } },
      { id: 'FrontHeading', name: 'Front Heading', basedOn: 'Normal', next: 'Normal', run: { font: FONTB, size: 30 }, paragraph: { alignment: D.AlignmentType.LEFT, spacing: { before: 0, after: 200 }, keepNext: true } },
      { id: 'FrontSub', name: 'Front Subheading', basedOn: 'Normal', next: 'Normal', run: { font: FONTB, size: 26 }, paragraph: { alignment: D.AlignmentType.LEFT, spacing: { before: 200, after: 60 }, keepNext: true } },
    ],
  },
  sections: [{
    properties: {
      titlePage: true,
      page: { size: { width: 11906, height: 16838 }, margin: { top: 1417, bottom: 1500, left: SIDE, right: SIDE, header: 700, footer: 700 }, pageNumbers: { start: 1, formatType: D.NumberFormat.DECIMAL } },
    },
    headers: { first: emptyHdr(), default: hdr('r'), even: hdr('l') },
    footers: { first: ftr(), default: ftr(), even: ftr() },
    children: body,
  }],
});

D.Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT, buf);
  fs.writeFileSync(path.join(__dirname, 'entries.json'), JSON.stringify(entries, null, 1));
  fs.mkdirSync(FIGDIR, { recursive: true });
  fs.readdirSync(FIGDIR).filter((x) => x.startsWith('Figure_')).forEach((x) => fs.unlinkSync(path.join(FIGDIR, x)));
  figs.forEach((f) => {
    const src = imgOf(f);
    const slug = (f.id || 'fig').replace(/^f-/, '').replace(/[^\w-]+/g, '-');
    fs.copyFileSync(src, path.join(FIGDIR, 'Figure_' + f.num + '_' + slug + path.extname(src)));
  });
  console.log('wrote', OUT, buf.length, 'bytes;', figs.length, 'figures;', tab, 'tables;', sec, 'sections;', dec, 'decisions');
});
