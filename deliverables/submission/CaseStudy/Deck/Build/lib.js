// Shared helpers for the Breakfast Paradox deck (10 x 5.625 in).
const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');
const React = require('react');
const RDS = require('react-dom/server');
const sharp = require('sharp');
const MD = require('react-icons/md');

const K = {
  ink: '0E1440', indigo: '1A237E', indigoTint: 'E8EAF6', paper: 'FAF8F4', text: '1F2430', muted: '616161',
  onDark: 'FFFFFF', onDark2: 'B8BFE6', darkLine: '6B74A8',
  orange: 'E65100', orangeT: 'FFF3E0',
  blue: '1565C0', blueT: 'E3F2FD',
  teal: '00695C', tealT: 'E0F2F1',
  purple: '6A1B9A', purpleT: 'F3E5F5',
  grey: '616161', greyT: 'F2F2F2', greyM: '9AA3B5',
  red: 'C62828', redT: 'FDECEA',
  amber: 'F57F17', amberT: 'FFF8E1', amberD: '8D4A00',
  green: '2E7D32', greenT: 'E8F5E9',
  white: 'FFFFFF',
};
const ROLE = {
  orange: [K.orange, K.orangeT], blue: [K.blue, K.blueT], teal: [K.teal, K.tealT], purple: [K.purple, K.purpleT],
  grey: [K.grey, K.greyT], red: [K.red, K.redT], amber: [K.amber, K.amberT], green: [K.green, K.greenT], indigo: [K.indigo, K.indigoTint],
};
const SECTIONS = ['Background', 'Approach', 'Understanding the system', 'Modelling the system', 'Finding where to intervene',
  'Designing and testing interventions', 'What the findings mean for the institution', 'Limitations and open questions', 'Reflections', 'Questions for discussion'];
const W = 10, H = 5.625;

const THEME = {
  name: 'Breakfast Paradox', headFontFace: 'Cambria', bodyFontFace: 'Calibri',
  colors: { dk1: '1F2430', lt1: 'FAF8F4', dk2: '0E1440', lt2: 'E8EAF6', accent1: 'E65100', accent2: '1565C0', accent3: '00695C', accent4: '6A1B9A', accent5: 'C62828', accent6: '2E7D32', hlink: '1A237E', folHlink: 'F57F17' },
};

// ------------------------------------------------------------------ icons
const iconCache = {};
async function loadIcons(names) {
  for (const n of names) {
    if (!MD[n]) throw new Error('Unknown icon ' + n);
    const svg = RDS.renderToStaticMarkup(React.createElement(MD[n], { color: '#FFFFFF', size: '256' }));
    const buf = await sharp(Buffer.from(svg)).resize(256, 256).png().toBuffer();
    iconCache[n] = 'image/png;base64,' + buf.toString('base64');
    const svg2 = RDS.renderToStaticMarkup(React.createElement(MD[n], { color: '#1F2430', size: '256' }));
    iconCache[n + ':dark'] = 'image/png;base64,' + (await sharp(Buffer.from(svg2)).resize(256, 256).png().toBuffer()).toString('base64');
  }
}

function makeLib(pres) {
  const L = {};
  L.pres = pres;
  const shp = pres.shapes;

  L.txt = (s, text, x, y, w, h, o = {}) => {
    s.addText(text, { x, y, w, h, isTextBox: true, margin: 0, fontSize: 14, color: K.text, valign: 'top', align: 'left', ...o });
  };
  L.box = (s, x, y, w, h, o = {}) => {
    const r = o.r === undefined ? 0.08 : o.r;
    const opt = { x, y, w, h };
    if (o.fill) opt.fill = { color: o.fill, ...(o.transparency ? { transparency: o.transparency } : {}) }; else opt.fill = { type: 'none' };
    if (o.line) opt.line = { color: o.line, width: o.lw || 1, ...(o.dash ? { dashType: o.dash } : {}) }; else opt.line = { type: 'none' };
    if (r > 0) { opt.rectRadius = r; s.addShape(shp.ROUNDED_RECTANGLE, opt); } else s.addShape(shp.RECTANGLE, opt);
  };
  // card with a role colour: tint fill and 1pt border
  L.card = (s, x, y, w, h, role, o = {}) => {
    const [c, t] = ROLE[role];
    L.box(s, x, y, w, h, { fill: o.fill || t, line: o.noLine ? null : (o.line || c), lw: o.lw || 1, dash: o.dash, r: o.r === undefined ? 0.08 : o.r });
  };
  L.circ = (s, cx, cy, d, fill, o = {}) => {
    const opt = { x: cx - d / 2, y: cy - d / 2, w: d, h: d };
    opt.fill = fill ? { color: fill } : { type: 'none' };
    opt.line = o.line ? { color: o.line, width: o.lw || 1, ...(o.dash ? { dashType: o.dash } : {}) } : { type: 'none' };
    s.addShape(shp.OVAL, opt);
  };
  L.icon = (s, name, cx, cy, d, fill) => {
    L.circ(s, cx, cy, d, fill);
    const g = d * 0.6;
    s.addImage({ data: iconCache[name], x: cx - g / 2, y: cy - g / 2, w: g, h: g, altText: name.replace(/^Md/, '') });
  };
  L.iconBare = (s, name, cx, cy, g, dark = true) => {
    s.addImage({ data: iconCache[dark ? name + ':dark' : name], x: cx - g / 2, y: cy - g / 2, w: g, h: g, altText: name.replace(/^Md/, '') });
  };
  // straight line or arrow from (x1,y1) to (x2,y2)
  L.line = (s, x1, y1, x2, y2, o = {}) => {
    const x = Math.min(x1, x2), y = Math.min(y1, y2), w = Math.abs(x2 - x1), h = Math.abs(y2 - y1);
    const opt = { x, y, w, h, line: { color: o.color || K.text, width: o.w || 1.5, ...(o.dash ? { dashType: o.dash } : {}), ...(o.arrow ? { endArrowType: 'triangle' } : {}), ...(o.arrowStart ? { beginArrowType: 'triangle' } : {}) } };
    if ((x2 < x1) !== (y2 < y1) && w > 0 && h > 0) opt.flipV = true;
    if (x2 < x1 && y2 < y1) { opt.flipH = true; opt.flipV = true; }
    if (x2 < x1 && y2 >= y1) { opt.flipH = true; opt.flipV = false; }
    if (x2 >= x1 && y2 < y1) { opt.flipH = false; opt.flipV = true; }
    if (x2 >= x1 && y2 >= y1) { opt.flipH = false; opt.flipV = false; }
    s.addShape(shp.LINE, opt);
  };
  L.tagColors = {
    CONFIRMED: { fill: K.green, color: K.white }, 'SINGLE-SOURCED': { fill: K.grey, color: K.white },
    CANDIDATE: { fill: K.amberT, color: K.amberD, line: K.amber }, ASSUMED: { fill: null, color: K.amberD, line: K.amber },
    PROJECTED: { fill: K.indigo, color: K.white }, REASONED: { fill: K.purple, color: K.white }, PLANNED: { fill: K.teal, color: K.white },
    OPEN: { fill: null, color: K.red, line: K.red },
  };
  // evidence tags, right-aligned in the content zone; kinds is an array of words
  L.tags = (s, kinds, o = {}) => {
    const y = o.y === undefined ? 1.13 : o.y;
    let x = (o.right || 9.5);
    [...kinds].reverse().forEach((k) => {
      const c = L.tagColors[k];
      const w = 0.34 + k.length * 0.075;
      x -= w;
      const opt = { x, y, w, h: 0.22, rectRadius: 0.05, fill: c.fill ? { color: c.fill } : { type: 'none' }, line: c.line ? { color: c.line, width: 1 } : { type: 'none' } };
      s.addShape(shp.ROUNDED_RECTANGLE, opt);
      L.txt(s, k, x, y, w, 0.22, { fontSize: 9, bold: true, color: c.color, align: 'center', valign: 'middle', charSpacing: 1 });
      x -= 0.08;
    });
  };
  // role chip: small rounded rectangle with centred text
  L.chip = (s, text, x, y, w, h, role, o = {}) => {
    const [c, t] = ROLE[role];
    L.box(s, x, y, w, h, { fill: o.solid ? c : t, line: c, lw: o.lw || 1, dash: o.dash, r: o.r === undefined ? 0.06 : o.r });
    L.txt(s, text, x + 0.07, y, w - 0.14, h, { fontSize: o.size || 12, color: o.solid ? K.white : (o.color || K.text), valign: 'middle', align: o.align || 'center', bold: o.bold, ...(o.extra || {}) });
  };
  L.big = (s, text, x, y, w, h, o = {}) => {
    L.txt(s, text, x, y, w, h, { fontFace: 'Cambria', bold: true, fontSize: o.size || 54, color: o.color || K.text, valign: o.valign || 'middle', align: o.align || 'left', ...(o.extra || {}) });
  };
  // the plate: wedge for the eaten share, empty ring for the rest
  L.plate = (s, cx, cy, d, o = {}) => {
    const eaten = o.eaten === undefined ? 37.1 : o.eaten;
    const ringColor = o.ring || K.onDark2;
    s.addShape(shp.OVAL, { x: cx - d / 2, y: cy - d / 2, w: d, h: d, fill: o.base ? { color: o.base } : { type: 'none' }, line: { color: ringColor, width: o.lw || 3 } });
    if (o.band) s.addShape(shp.PIE, { x: cx - d / 2, y: cy - d / 2, w: d, h: d, fill: { color: o.wedge || K.orange, transparency: 55 }, line: { type: 'none' }, angleRange: [270, (270 + o.band * 3.6) % 360] });
    const start = 270, end = (270 + eaten * 3.6) % 360;
    s.addShape(shp.PIE, { x: cx - d / 2, y: cy - d / 2, w: d, h: d, fill: { color: o.wedge || K.orange }, line: { type: 'none' }, angleRange: [start, end] });
  };
  // the missing link: an arrow from x1 to x2 at height y that stops short, with a gap and a broken-link icon.
  // state 'broken' or 'solid'
  L.link = (s, x1, y, x2, state = 'broken', o = {}) => {
    const col = o.color || K.red;
    if (state === 'solid') {
      L.line(s, x1, y, x2, y, { color: o.solidColor || K.green, w: 3, arrow: true });
      if (o.label) L.txt(s, o.label, x1, y - 0.3, x2 - x1, 0.26, { fontSize: 12, bold: true, color: o.labelColor || K.green, align: 'center' });
      return;
    }
    const gap = 0.5, mid = (x1 + x2) / 2;
    L.line(s, x1, y, mid - gap / 2, y, { color: col, w: 2.5, dash: 'dash' });
    L.line(s, mid + gap / 2, y, x2, y, { color: col, w: 2.5, dash: 'dash', arrow: true });
    L.icon(s, 'MdLinkOff', mid, y, 0.34, col);
    if (o.label) L.txt(s, o.label, mid - 0.9, y + 0.24, 1.8, 0.24, { fontSize: 11, color: o.labelColor || col, align: 'center', bold: true });
  };
  L.decisionCard = (s, n, d, proofRole = 'indigo') => {
    // tracker
    for (let i = 1; i <= 13; i++) {
      const cx = 9.5 - (13 - i) * 0.16 - 0.05;
      L.circ(s, cx, 0.17, 0.1, i === n ? K.indigo : null, { line: K.indigo, lw: 0.75 });
    }
    L.txt(s, `Decision ${n} of 13`, 0.5, 0.1, 3, 0.2, { fontSize: 10, bold: true, color: K.indigo, charSpacing: 1 });
    // left panel
    L.box(s, 0.5, 1.4, 3.2, 3.4, { fill: K.indigo, r: 0.08 });
    L.txt(s, 'DECISION', 0.7, 1.6, 2.8, 0.25, { fontSize: 11, bold: true, color: K.onDark2, charSpacing: 3 });
    L.txt(s, d.decision, 0.7, 1.95, 2.8, 1.9, { fontSize: 18, bold: true, color: K.white, fontFace: 'Cambria' });
    L.txt(s, String(n), 0.7, 3.85, 1.2, 0.85, { fontSize: 54, bold: true, color: '3949AB', fontFace: 'Cambria', valign: 'bottom' });
    const rows = [
      ['ALTERNATIVES', d.alternatives, 'MdSwapHoriz', K.grey, K.greyT, K.text],
      ['REASON', d.reason, 'MdCheckCircle', K.green, K.greenT, K.text],
      ['TRADE-OFF', d.tradeoff, 'MdBalance', K.amber, K.amberT, K.text],
    ];
    rows.forEach((r, i) => {
      const y = 1.4 + i * 1.07;
      L.box(s, 3.95, y, 5.55, 0.95, { fill: r[4], r: 0.08 });
      L.icon(s, r[2], 4.3, y + 0.475, 0.5, r[3]);
      L.txt(s, r[0], 4.7, y + 0.1, 4.6, 0.2, { fontSize: 10, bold: true, color: r[0] === 'TRADE-OFF' ? K.amberD : K.muted, charSpacing: 2 });
      L.txt(s, r[1], 4.7, y + 0.31, 4.65, 0.6, { fontSize: 13, color: r[5], valign: 'top' });
    });
    if (d.proof) {
      L.icon(s, 'MdInsights', 4.18, 4.88, 0.28, K.indigo);
      L.txt(s, d.proof, 4.45, 4.76, 5.05, 0.25, { fontSize: 12, color: K.text, valign: 'middle', italic: true });
    }
  };
  // numbered tile: coloured number circle, short text
  L.tile = (s, x, y, w, h, role, num, text, o = {}) => {
    L.card(s, x, y, w, h, role, o);
    const [c] = ROLE[role];
    if (o.icon) L.icon(s, o.icon, x + 0.38, y + h / 2, 0.44, c);
    else if (num !== null && num !== undefined) { L.circ(s, x + 0.34, y + h / 2, 0.4, c); L.txt(s, String(num), x + 0.14, y, 0.4, h, { fontSize: 14, bold: true, color: K.white, align: 'center', valign: 'middle' }); }
    L.txt(s, text, x + (o.icon || (num !== null && num !== undefined) ? 0.7 : 0.14), y + 0.05, w - (o.icon || (num !== null && num !== undefined) ? 0.82 : 0.28), h - 0.1, { fontSize: o.size || 12, valign: 'middle', color: o.color || K.text });
  };
  return L;
}

module.exports = { K, ROLE, SECTIONS, W, H, THEME, loadIcons, makeLib, pptxgen };
