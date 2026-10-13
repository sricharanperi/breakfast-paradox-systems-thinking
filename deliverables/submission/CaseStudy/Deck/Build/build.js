// Builds The Breakfast Paradox presentation.
// Usage: node build.js [OUT.pptx]
const fs = require('fs');
const path = require('path');
const { K, SECTIONS, W, H, THEME, loadIcons, makeLib, pptxgen } = require('./lib');
const SKILL = '/Users/perisricharan/.claude/skills/synced/639d251c-b7f1-490c-9a9e-4f6969b8ef19_ca26e898-02d8-40f1-bdf1-2895265d7862/pptx/scripts/apply_theme.js';
const { applyTheme } = require(SKILL);

const DECK = path.resolve(__dirname, '..');
const OUT = process.argv[2] || path.join(DECK, 'The_Breakfast_Paradox.pptx');
const FIGS = path.resolve(DECK, '..', 'Figures');

// ------------------------------------------------------------ parse the blueprint
const bp = fs.readFileSync(path.join(DECK, 'BLUEPRINT.md'), 'utf8');
const parts = bp.split(/^### Slide /m).slice(1);
const data = {};
parts.forEach((blk) => {
  const head = blk.split('\n')[0];
  const key = head.split('|')[0].trim();
  const d = { key };
  blk.split('\n').forEach((ln) => {
    const m = ln.match(/^- ([A-Za-z\- ]+?)( \(chip\))?: (.*)$/);
    if (!m) return;
    const f = m[1].trim().toLowerCase();
    const v = m[3].trim();
    if (f === 'title') d.title = v;
    else if (f === 'message') d.message = v;
    else if (f === 'notes') d.notes = v;
    else if (f === 'decision') d.decision = v;
    else if (f === 'alternatives') d.alternatives = v;
    else if (f === 'reason') d.reason = v;
    else if (f === 'trade-off') d.tradeoff = v;
    else if (f === 'proof line') d.proof = v;
    else if (f === 'content') d.content = v;
    else if (f === 'on-slide text') d.onslide = v;
  });
  data[key] = d;
});

const sectionOf = (n) => (n <= 3 ? 0 : n <= 6 ? 1 : n <= 11 ? 2 : n <= 30 ? 3 : n <= 41 ? 4 : n <= 46 ? 5 : n <= 60 ? 6 : n === 61 ? 7 : n <= 63 ? 8 : n === 64 ? 9 : 10);
const DARK = new Set([1, 2, 4, 7, 12, 24, 31, 40, 42, 47, 61, 62, 64, 65]);

const ICONS = ['MdHowToReg', 'MdReceiptLong', 'MdQrCodeScanner', 'MdMenuBook', 'MdRestaurant', 'MdDelete', 'MdSchedule', 'MdEvent', 'MdSchool', 'MdEngineering',
  'MdAccountBalance', 'MdAltRoute', 'MdLinkOff', 'MdCheckCircle', 'MdHelp', 'MdWarning', 'MdPayments', 'MdBarChart', 'MdAutorenew', 'MdStairs', 'MdBlock',
  'MdLock', 'MdHandshake', 'MdGroups', 'MdTune', 'MdBalance', 'MdSwapHoriz', 'MdInsights', 'MdLocalShipping', 'MdPerson', 'MdPeople', 'MdSettings', 'MdStorefront',
  'MdAlarm', 'MdBedtime', 'MdFastfood', 'MdSearch', 'MdTimeline', 'MdFactCheck', 'MdRule', 'MdSensors', 'MdMoreTime', 'MdCancel', 'MdArrowForward', 'MdTrendingDown',
  'MdNotificationsActive', 'MdVisibility', 'MdVisibilityOff', 'MdShield', 'MdForum', 'MdGavel', 'MdAssignment', 'MdLoop', 'MdWaterDrop', 'MdLocalDining', 'MdRecycling',
  'MdRestaurantMenu', 'MdHistory', 'MdFlag', 'MdLightbulb', 'MdStar', 'MdClose', 'MdDoneAll', 'MdPlayArrow', 'MdStop', 'MdCalendarMonth', 'MdScale', 'MdMenu', 'MdAccessTime',
  'MdTrackChanges', 'MdPsychology', 'MdFilterAlt', 'MdAccountTree', 'MdHub', 'MdPriorityHigh', 'MdTouchApp', 'MdSwapVert', 'MdOutlinedFlag', 'MdReportProblem', 'MdSell', 'MdWallet'];

(async () => {
  await loadIcons(ICONS);
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_16x9';
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = ' '; pres.author = ' '; pres.subject = ' ';
  const L = makeLib(pres);

  // layouts: light and dark, one per section (the section name sits in the footer)
  const mk = (name, dark) => pres.defineSlideMaster({
    title: name,
    background: { color: dark ? K.ink : K.paper },
    objects: [{ placeholder: { options: { name: 'title', type: 'title', x: 0.5, y: 0.34, w: 9.0, h: 0.8, fontSize: 24, bold: true, fontFace: 'Cambria', color: dark ? K.white : K.text, align: 'left', valign: 'top', margin: 0 }, text: '' } }],
    slideNumber: { x: 9.0, y: 5.22, w: 0.5, h: 0.3, fontSize: 10, color: dark ? K.onDark2 : K.muted, align: 'right', fontFace: 'Calibri' },
  });
  mk('LIGHT', false); mk('DARK', true);
  pres.defineSlideMaster({ title: 'TITLE', background: { color: K.ink }, objects: [{ placeholder: { options: { name: 'title', type: 'title', x: 0.5, y: 1.35, w: 5.2, h: 1.5, fontSize: 44, bold: true, fontFace: 'Cambria', color: K.white, align: 'left', valign: 'top', margin: 0 }, text: '' } }], slideNumber: { x: 9.0, y: 5.22, w: 0.5, h: 0.3, fontSize: 10, color: K.onDark2, align: 'right', fontFace: 'Calibri' } });
  pres.defineSlideMaster({ title: 'APP', background: { color: K.paper }, objects: [{ placeholder: { options: { name: 'title', type: 'title', x: 0.5, y: 0.34, w: 9.0, h: 0.7, fontSize: 24, bold: true, fontFace: 'Cambria', color: K.text, align: 'left', valign: 'top', margin: 0 }, text: '' } }], slideNumber: { x: 9.0, y: 5.22, w: 0.5, h: 0.3, fontSize: 10, color: K.muted, align: 'right', fontFace: 'Calibri' } });

  const footer = (s, sec, dark) => {
    const on = dark ? K.white : K.indigo, off = dark ? K.darkLine : K.greyM;
    for (let i = 0; i < 10; i++) {
      const cx = 0.555 + i * 0.2;
      const past = sec > 0 && i + 1 < sec, cur = i + 1 === sec;
      if (cur) { L.circ(s, cx, 5.375, 0.16, on); L.circ(s, cx, 5.375, 0.24, null, { line: on, lw: 0.75 }); }
      else if (past) L.circ(s, cx, 5.375, 0.11, on);
      else L.circ(s, cx, 5.375, 0.11, null, { line: off, lw: 0.75 });
    }
    if (sec > 0) L.txt(s, `${sec} ${SECTIONS[sec - 1]}`, 2.75, 5.26, 5.5, 0.24, { fontSize: 10, color: dark ? K.onDark2 : K.muted, valign: 'middle' });
  };

  const ctx = { pres, L, K, data, FIGS, H, W };
  const B = {};
  require('./b1')(B, ctx); require('./b2')(B, ctx); require('./b3')(B, ctx); require('./b4')(B, ctx);

  let lastSec = -1;
  const sectionNames = ['Opening', ...SECTIONS];
  for (let n = 1; n <= 65; n++) {
    const sec = sectionOf(n);
    if (sec !== lastSec) { pres.addSection({ title: sectionNames[sec] }); lastSec = sec; }
    const dark = DARK.has(n);
    const s = pres.addSlide({ masterName: n === 1 ? 'TITLE' : (dark ? 'DARK' : 'LIGHT'), sectionTitle: sectionNames[sec] });
    const d = data[String(n)];
    if (!d) throw new Error('no data for slide ' + n);
    s.addText(d.title, { placeholder: 'title' });
    footer(s, sec, dark);
    if (B[n]) B[n](s, d, dark); else console.log('NO BUILDER', n);
    s.addNotes(`${d.message || ''} ${d.notes || ''}`.trim());
  }
  pres.addSection({ title: 'Appendix' });
  data.A1.title = 'Nine research objectives and the activities that addressed them';
  data.A1b = { title: 'Sources of evidence and their main limits', content: data.A1.content };
  for (const k of ['A1', 'A1b', 'A2', 'A3', 'A4']) {
    const s = pres.addSlide({ masterName: 'APP', sectionTitle: 'Appendix' });
    const d = data[k];
    s.addText(d.title, { placeholder: 'title' });
    L.txt(s, 'For reading, not presented live', 0.5, 5.26, 4, 0.24, { fontSize: 10, color: K.muted, valign: 'middle' });
    if (B[k]) B[k](s, d, false);
    s.addNotes(d.content || '');
  }
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  // the default master carries an en dash as a level-2 bullet character; replace it so no dash exists anywhere in the file
  const JSZip = require('jszip');
  const zip = await JSZip.loadAsync(fs.readFileSync(OUT));
  for (const name of Object.keys(zip.files)) {
    if (/^ppt\/slideMasters\/.*\.xml$/.test(name)) {
      const x = await zip.file(name).async('string');
      zip.file(name, x.replace(/char="[\u2013\u2014]"/g, 'char="\u2022"'));
    }
  }
  fs.writeFileSync(OUT, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
  console.log('wrote', OUT);
})().catch((e) => { console.error(e); process.exit(1); });
