// Slides 31 to 46: modelling the system and finding where to intervene
module.exports = (B, { pres, L, K }) => {
  const chainX = (i) => 0.5 + i * 1.84;
  const chainNodes = [
    ['Standing booking, flat all week', 'blue'], ['Ratio, about 70%', 'blue'], ['First batch: can be topped up, never reduced', 'red'],
    ['Crest in the last quarter hour, 9:15 to 9:30', 'amber'], ['Shortage and surplus on the same morning', 'red'],
  ];
  // ---- 31 bottleneck (dark opener, build 1 of 3)
  B[31] = (s) => {
    chainNodes.forEach((c, i) => {
      L.card(s, chainX(i), 1.45, 1.65, 1.1, c[1], { lw: i === 2 ? 3.5 : 1 });
      L.txt(s, c[0], chainX(i) + 0.1, 1.45, 1.45, 1.1, { fontSize: 12, bold: i === 2, valign: 'middle', align: 'center' });
      if (i < 4) L.line(s, chainX(i) + 1.65, 2.0, chainX(i + 1), 2.0, { color: K.onDark2, w: 2, arrow: true });
    });
    L.txt(s, 'THE BOTTLENECK', chainX(2), 2.62, 1.65, 0.2, { fontSize: 9.5, bold: true, color: '#FF8A80'.slice(1), align: 'center', charSpacing: 2 });
    L.card(s, 0.5, 3.75, 2.1, 0.95, 'purple');
    L.icon(s, 'MdQrCodeScanner', 0.95, 4.225, 0.42, K.purple);
    L.txt(s, 'Scans and books', 1.3, 3.75, 1.25, 0.95, { fontSize: 12, bold: true, valign: 'middle' });
    L.line(s, chainX(2) + 0.82, 2.85, chainX(2) + 0.82, 3.3, { color: K.onDark2, w: 1.5, dash: 'dash' });
    L.line(s, chainX(2) + 0.82, 3.3, 1.55, 3.3, { color: K.onDark2, w: 1.5, dash: 'dash' });
    L.line(s, 1.55, 3.3, 1.55, 3.72, { color: K.onDark2, w: 1.5, dash: 'dash', arrow: true });
    L.card(s, 7.4, 3.75, 2.1, 0.95, 'teal');
    L.icon(s, 'MdAccountBalance', 7.85, 4.225, 0.42, K.teal);
    L.txt(s, 'Who decides', 8.2, 3.75, 1.25, 0.95, { fontSize: 12, bold: true, valign: 'middle' });
    L.link(s, 2.65, 4.225, 7.35, 'broken', { color: '#FF8A80'.slice(1), label: 'no route' });
    L.txt(s, 'The gap is recorded in the kitchen and goes no further.', 0.5, 4.9, 8, 0.28, { fontSize: 14, color: K.onDark2 });
  };
  // ---- 32 eight absorbers (build 2 of 3)
  B[32] = (s) => {
    chainNodes.forEach((c, i) => {
      L.box(s, chainX(i), 1.38, 1.65, 0.5, { fill: K.greyT, line: i === 2 ? K.red : K.greyM, lw: i === 2 ? 2 : 0.75, r: 0.06 });
      L.txt(s, c[0], chainX(i) + 0.06, 1.38, 1.53, 0.5, { fontSize: 9.5, color: K.muted, valign: 'middle', align: 'center' });
    });
    L.chip(s, 'PROTECTS NO ONE', chainX(2) + 0.1, 1.93, 1.45, 0.2, 'red', { size: 9, bold: true });
    const abs = [
      ['Resale on Mess Cell', 'MdSell', 'orange'], ['Operator top-ups and discount', 'MdTune', 'teal'], ['Reuse at Yuktāhār', 'MdRecycling', 'green'], ['Outside diners and Kadamba staff', 'MdGroups', 'green'],
      ['Held and reheated food', 'MdHistory', 'amber'], ['Late-door service', 'MdMoreTime', 'blue'], ['Outside venues', 'MdStorefront', 'grey'], ['The bin', 'MdDelete', 'red'],
    ];
    L.txt(s, 'WHERE THE SURPLUS GOES BEFORE ANY RULE SETTER SEES IT', 0.5, 2.3, 8, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    abs.forEach((a, i) => {
      const x = 0.5 + (i % 4) * 2.28, y = 2.6 + Math.floor(i / 4) * 1.15;
      const col = { orange: K.orange, teal: K.teal, green: K.green, amber: K.amber, blue: K.blue, grey: K.grey, red: K.red }[a[2]];
      L.card(s, x, y, 2.18, 1.0, a[2], { dash: a[0].startsWith('Held') ? 'dash' : undefined });
      L.icon(s, a[1], x + 0.38, y + 0.5, 0.46, col);
      L.txt(s, a[0], x + 0.72, y + 0.05, 1.4, 0.9, { fontSize: 12, valign: 'middle' });
      if (a[0] === 'Held and reheated food' || a[0] === 'The bin') L.chip(s, 'PROTECTS NO ONE', x + 0.6, y + 0.8, 1.5, 0.2, 'red', { size: 9, bold: true });
    });
    L.txt(s, 'Most absorbers feed real people.', 0.5, 4.95, 5, 0.25, { fontSize: 12, color: K.muted, italic: true });
  };
  // ---- 33 eighteen mechanisms
  B[33] = (s) => {
    const groups = [
      ['Closed, every link evidenced', K.green, 'green', false, [['L4', 'Menu rotation governance'], ['L11', 'Wastage Book learning at Yuktāhār'], ['L12', 'Counter top-up, upward only']]],
      ['Candidate loops, closing link assumed', K.purple, 'purple', true, [['L1', 'Resale safety net'], ['L3b', 'Kadamba demand lock-in'], ['L9', 'Waste absorption'], ['L15', 'Soft close'], ['L17', 'Kitchen competence shifts the burden']]],
      ['Chains that do not close', K.amber, 'amber', false, [['L13', 'Standing booking to fixed-ratio surplus (core)'], ['L14', 'Closing rush to just-in-case batch'], ['L2', 'Skip Meal'], ['L5', 'Menu transparency'], ['L6', 'Shock relaxation'], ['L7', 'Late-night workload to skip']]],
      ['Contraindicated, unresolved, absent or static', K.red, 'red', false, [['L3', 'Capacity redistribution'], ['L8', 'Vendor discipline'], ['L16', 'Operator waste to menu'], ['L10', 'Measured but unrouted']]],
    ];
    groups.forEach((g, gi) => {
      const y = 1.35 + gi * 0.9;
      L.txt(s, g[0].toUpperCase(), 0.5, y, 6, 0.18, { fontSize: 9, bold: true, color: g[1] === K.amber ? K.amberD : g[1], charSpacing: 1.5 });
      const n = g[4].length, w = n >= 6 ? 1.43 : n === 5 ? 1.76 : n === 4 ? 2.14 : 2.9, gap = n >= 6 ? 0.084 : 0.14;
      g[4].forEach((t, i) => {
        const x = 0.5 + i * (w + gap);
        const core = t[0] === 'L13' || t[0] === 'L10';
        L.card(s, x, y + 0.22, w, 0.6, g[2], { dash: g[3] ? 'dash' : undefined, lw: core ? 2.5 : 1 });
        L.txt(s, [{ text: t[0] + '  ', options: { bold: true, color: g[1] === K.amber ? K.amberD : g[1] } }, { text: t[1], options: { color: K.text } }], x + 0.08, y + 0.22, w - 0.16, 0.6, { fontSize: 10.5, valign: 'middle' });
      });
    });
    L.txt(s, 'Every working loop corrects the kitchen. None corrects the booking.', 0.5, 4.98, 8, 0.25, { fontSize: 12, bold: true });
  };
  B[34] = (s, d) => L.decisionCard(s, 7, d);
  // ---- 35 two models
  B[35] = (s) => {
    L.box(s, 0.5, 1.4, 4.2, 3.0, { fill: K.greyT, r: 0.08 });
    L.txt(s, 'BILL THE BOOKING', 0.7, 1.5, 3.8, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    L.txt(s, 'The model in force', 0.7, 1.72, 3.8, 0.3, { fontSize: 16, bold: true });
    L.chip(s, 'Standing booking', 0.7, 2.2, 1.7, 0.5, 'blue', { size: 12 });
    L.line(s, 2.4, 2.45, 2.75, 2.45, { color: K.indigo, w: 2, arrow: true });
    L.chip(s, 'A charge', 2.75, 2.2, 1.7, 0.5, 'red', { size: 12 });
    L.card(s, 0.7, 3.05, 3.75, 1.1, 'red');
    L.txt(s, 'Sunday 6 September, Yuktāhār: 267 registered, 50 ate', 0.85, 3.05, 3.45, 1.1, { fontSize: 14, bold: true, valign: 'middle' });
    L.box(s, 5.0, 1.4, 4.5, 3.0, { fill: K.greenT, r: 0.08 });
    L.txt(s, 'BILL ATTENDANCE', 5.2, 1.5, 4.1, 0.2, { fontSize: 10, bold: true, color: K.green, charSpacing: 2 });
    L.txt(s, 'Run twice', 5.2, 1.72, 4.1, 0.3, { fontSize: 16, bold: true });
    L.card(s, 5.2, 2.15, 4.1, 1.0, 'green');
    L.icon(s, 'MdWaterDrop', 5.6, 2.65, 0.45, K.green);
    L.txt(s, 'Gas shortage: one item at the same price, cancellation cap raised from five to ten, registration no longer compulsory', 5.95, 2.15, 3.3, 1.0, { fontSize: 11, valign: 'middle' });
    L.card(s, 5.2, 3.3, 4.1, 0.95, 'green', { dash: 'dash' });
    L.icon(s, 'MdEvent', 5.6, 3.775, 0.45, K.green);
    L.txt(s, 'Holidays and long weekends: students walked in and scanned, nobody who neither registered nor came was charged. This part is disputed.', 5.95, 3.3, 3.3, 0.95, { fontSize: 10.5, valign: 'middle' });
    L.box(s, 0.5, 4.55, 9.0, 0.42, { fill: K.red, r: 0.06 });
    L.txt(s, 'Switched off when the trigger passed, with no review. Why it was dropped is unchecked.', 0.6, 4.55, 8.8, 0.42, { fontSize: 14, bold: true, color: K.white, valign: 'middle', align: 'center' });
    L.tags(s, ['SINGLE-SOURCED'], { y: 1.13 });
  };
  // ---- 36 causes and conditions
  B[36] = (s) => {
    const c = ['A standing default with a narrow, early exit', 'Billing fires at the booking, not at consumption', 'The gap is measured but unrouted'];
    c.forEach((t, i) => {
      const x = 0.5 + i * 3.05;
      L.card(s, x, 1.4, 2.9, 1.15, 'red');
      L.circ(s, x + 0.35, 1.97, 0.42, K.red);
      L.txt(s, String(i + 1), x + 0.14, 1.76, 0.42, 0.42, { fontSize: 15, bold: true, color: K.white, align: 'center', valign: 'middle' });
      L.txt(s, t, x + 0.68, 1.45, 2.15, 1.05, { fontSize: 13, bold: true, valign: 'middle' });
      L.line(s, x + 1.45, 2.55, x + 1.45, 2.85, { color: K.red, w: 1.5, arrow: true });
    });
    L.txt(s, 'THREE STRUCTURAL CAUSES', 5.4, 1.12, 4.1, 0.2, { fontSize: 9.5, bold: true, color: K.red, charSpacing: 2, align: 'right' });
    L.box(s, 0.5, 2.9, 9.0, 0.62, { fill: K.amberT, line: K.amber, r: 0.08 });
    L.txt(s, [{ text: 'Condition 1   ', options: { bold: true, color: K.amberD } }, { text: 'Action follows loudness', options: {} }], 0.7, 2.9, 8.6, 0.62, { fontSize: 14, valign: 'middle' });
    L.box(s, 0.5, 3.6, 9.0, 0.62, { fill: K.amberT, line: K.amber, r: 0.08 });
    L.txt(s, [{ text: 'Condition 2   ', options: { bold: true, color: K.amberD } }, { text: 'Absorption takes up each consequence before authority sees it', options: {} }], 0.7, 3.6, 8.6, 0.62, { fontSize: 14, valign: 'middle' });
    L.card(s, 0.5, 4.3, 9.0, 0.55, 'grey');
    L.txt(s, 'The uncalibrated conversion ratio, three regimes: not a root cause, but the most actionable', 0.7, 4.3, 8.6, 0.55, { fontSize: 13, valign: 'middle', color: K.muted });
    L.txt(s, 'Menu fatigue was loud and got fixed. The registration gap is quiet.', 0.5, 4.95, 8, 0.25, { fontSize: 12, color: K.muted, italic: true });
  };
  B[37] = (s, d) => L.decisionCard(s, 8, d);
  // ---- 38 five assumptions
  B[38] = (s) => {
    const rows = [
      ['Students not showing up is the problem', 'A symptom, and partly no problem: one respondent fasts by choice', 'amber'],
      ['Students are careless or irrational', 'Fails: most never choose the booking, and the exit is narrow and early', 'red'],
      ['Nobody has solved this', 'Fails: attendance-tracked billing ran twice', 'red'],
      ['Nobody knows how big the gap is', 'Fails: it is measured in at least three places', 'red'],
      ['This is one problem', 'Fails: three structural causes plus one thing that is no problem', 'red'],
    ];
    rows.forEach((r, i) => {
      const y = 1.4 + i * 0.7;
      L.box(s, 0.5, y, 3.7, 0.6, { fill: K.greyT, r: 0.08 });
      L.txt(s, r[0], 0.65, y, 3.4, 0.6, { fontSize: 13, valign: 'middle', color: K.muted });
      L.line(s, 4.25, y + 0.3, 4.6, y + 0.3, { color: K.indigo, w: 2, arrow: true });
      L.icon(s, r[2] === 'amber' ? 'MdHelp' : 'MdClose', 4.95, y + 0.3, 0.4, r[2] === 'amber' ? K.amber : K.red);
      L.card(s, 5.3, y, 4.2, 0.6, r[2]);
      L.txt(s, r[1], 5.42, y, 3.95, 0.6, { fontSize: 12, valign: 'middle' });
    });
    L.txt(s, 'Challenged before any reframing was accepted.', 0.5, 4.95, 6, 0.25, { fontSize: 12, color: K.muted, italic: true });
  };
  // ---- 39 framings matrix
  B[39] = (s) => {
    const cols = ['Explains why breakfast and not lunch', 'Explains why it persists unseen', 'Reaches the booking', 'Fits the evidence'];
    const rows = [
      ['More registered students attend', 'EEEE'], ['Registration as a truer signal of intent', 'EEHE'], ['Kitchens forecast better', 'EEEH'], ['Every operator runs like Yuktāhār', 'EHEH'],
      ['Why breakfast fails when lunch works', 'FEHF'], ['Who should own the gap', 'EHHH'], ['The reframing: a stable equilibrium', 'FFFF'],
    ];
    const x0 = 4.4, cw = 1.28;
    cols.forEach((c, i) => L.txt(s, c, x0 + i * cw, 1.3, cw - 0.08, 0.5, { fontSize: 10.5, bold: true, color: K.muted, align: 'center', valign: 'bottom' }));
    rows.forEach((r, i) => {
      const y = 1.9 + i * 0.44;
      if (i === 6) L.box(s, 0.5, y - 0.03, 9.0, 0.44, { fill: K.greenT, line: K.green, r: 0.06 });
      L.txt(s, r[0], 0.65, y, 3.7, 0.38, { fontSize: 12.5, valign: 'middle', bold: i === 6 });
      [...r[1]].forEach((m, k) => {
        const cx = x0 + k * cw + (cw - 0.08) / 2, cy = y + 0.19, d = 0.26;
        if (m === 'F') L.circ(s, cx, cy, d, K.green);
        else if (m === 'E') L.circ(s, cx, cy, d, null, { line: K.green, lw: 1.5 });
        else { L.circ(s, cx, cy, d, null, { line: K.green, lw: 1.5 }); s.addShape(pres.shapes.PIE, { x: cx - d / 2, y: cy - d / 2, w: d, h: d, fill: { color: K.green }, line: { type: 'none' }, angleRange: [270, 90] }); }
      });
    });
    L.txt(s, 'Full circle passes. Half partly. Empty fails.', 0.5, 5.0, 6, 0.22, { fontSize: 11, color: K.muted, italic: true });
  };
  // ---- 40 equilibrium (dark hero)
  B[40] = (s) => {
    L.card(s, 3.9, 1.38, 2.2, 0.55, 'purple');
    L.txt(s, 'Rule setters', 3.9, 1.38, 2.2, 0.55, { fontSize: 13, bold: true, align: 'center', valign: 'middle' });
    L.line(s, 5.0, 2.35, 5.0, 1.95, { color: '#FF8A80'.slice(1), w: 1.5, dash: 'dash', arrow: true });
    L.txt(s, 'only loud complaints arrive', 3.0, 2.0, 1.9, 0.3, { fontSize: 10.5, color: 'FF8A80', align: 'right' });
    const forces = ['Default booking, narrow exit', 'Billing at the booking', 'Gap measured, not routed'];
    forces.forEach((f, i) => {
      const y = 1.75 + i * 0.75;
      L.card(s, 0.5, y, 2.4, 0.62, 'red');
      L.txt(s, f, 0.6, y, 2.2, 0.62, { fontSize: 12, bold: true, valign: 'middle' });
      L.line(s, 2.9, y + 0.31, 4.4, 2.95, { color: K.onDark2, w: 1.5, arrow: true });
    });
    L.circ(s, 5.0, 2.95, 1.2, K.indigo, { line: K.onDark2, lw: 2 });
    L.txt(s, 'The gap', 4.4, 2.5, 1.2, 0.9, { fontSize: 15, bold: true, color: K.white, align: 'center', valign: 'middle' });
    const abs = ['Resale on Mess Cell', 'Operator top-ups', 'Reuse', 'Outside diners and staff', 'Held and reheated food', 'Late-door service', 'Outside venues', 'The bin'];
    abs.forEach((a, i) => {
      const x = 6.55 + (i % 2) * 1.5, y = 1.55 + Math.floor(i / 2) * 0.55;
      L.chip(s, a, x, y, 1.42, 0.46, i === 7 ? 'red' : i === 4 ? 'amber' : 'green', { size: 10, dash: i === 4 ? 'dash' : undefined });
    });
    L.line(s, 5.6, 2.95, 6.45, 2.95, { color: K.onDark2, w: 1.5, arrow: true });
    L.txt(s, 'EIGHT ABSORBERS', 6.55, 1.3, 3, 0.2, { fontSize: 9.5, color: K.onDark2, bold: true, charSpacing: 2 });
    L.line(s, 0.5, 4.12, 9.5, 4.12, { color: 'FF8A80', w: 2, dash: 'dash' });
    L.txt(s, 'The kitchen door: nothing the kitchens learn crosses upward', 2.2, 3.88, 5.6, 0.2, { fontSize: 10.5, bold: true, color: '#FF8A80'.slice(1), align: 'center' });
    L.card(s, 0.5, 4.3, 4.4, 0.78, 'green');
    L.txt(s, 'Yuktāhār: blame-free weighing, a matching-week lookup, daily discussion; waste fell between August and December', 0.6, 4.3, 4.2, 0.78, { fontSize: 10.5, valign: 'middle' });
    L.card(s, 5.1, 4.3, 4.4, 0.78, 'green');
    L.txt(s, 'Bakul and Kadamba: weekly adjustment down only to a floor; one recorded adjustment at Kadamba and no outcome record', 5.2, 4.3, 4.2, 0.78, { fontSize: 10.5, valign: 'middle' });
  };
  // ---- 41 design opportunity
  B[41] = (s) => {
    L.card(s, 0.5, 1.4, 1.6, 2.6, 'purple');
    L.icon(s, 'MdQrCodeScanner', 1.3, 2.15, 0.6, K.purple);
    L.txt(s, 'The records that already exist', 0.6, 2.6, 1.4, 0.9, { fontSize: 13, bold: true, align: 'center' });
    L.card(s, 3.7, 1.4, 2.3, 0.85, 'blue');
    L.txt(s, 'The kitchen decision that fixes how much is cooked', 3.8, 1.4, 2.1, 0.85, { fontSize: 12, valign: 'middle' });
    L.card(s, 3.7, 3.15, 2.3, 0.85, 'teal');
    L.txt(s, 'A decision about registration and billing', 3.8, 3.15, 2.1, 0.85, { fontSize: 12, valign: 'middle' });
    L.link(s, 2.15, 1.825, 3.65, 'broken');
    L.link(s, 2.15, 3.575, 3.65, 'broken');
    [['Does a plate for payment mean served or registered?', 0.5], ['Who set the four-day lead and the cap of five cancellations?', 3.35]].forEach((g) => {
      L.card(s, g[1], 4.2, 2.75, 0.75, 'amber', { dash: 'dash' });
      L.icon(s, 'MdHelp', g[1] + 0.32, 4.575, 0.36, K.amber);
      L.txt(s, g[0], g[1] + 0.6, 4.2, 2.1, 0.75, { fontSize: 11, valign: 'middle' });
    });
    const ip = [['The kitchen, where a registration becomes a cooked quantity', 'blue'], ['The registration and billing rules', 'teal'], ['The ownership gap', 'grey'], ['The attention mechanism: a cost trigger beside the complaint trigger, the cheapest by far', 'purple']];
    ip.forEach((p, i) => {
      const y = 1.4 + i * 0.9;
      L.tile(s, 6.3, y, 3.2, 0.8, p[1], i + 1, p[0], { size: 11 });
    });
    L.txt(s, 'Four places to intervene', 6.3, 5.0, 3.2, 0.22, { fontSize: 10, bold: true, color: K.muted });
  };
  // ---- 42 ladder (dark opener)
  B[42] = (s) => {
    const names = ['Transcend paradigms', 'Mindset or paradigm', 'Goals of the system', 'Power to self-organise', 'Rules of the system', 'Information flows', 'Gain of reinforcing loops', 'Strength of balancing loops', 'Length of delays', 'Stocks and flows structure', 'Buffer sizes', 'Parameters and numbers'];
    const fills = ['3949AB', '4452B5', '5C6BC0', '7986CB', '9FA8DA', 'B8BFE6', 'C5CAE9', 'D3D8EE', 'DDE0F0', 'E8EAF6', 'EEF0F9', 'F3F4FA'];
    const chips = {
      2: [['LP11', 'purple']], 3: [['LP12', 'purple'], ['LP3 goal', 'teal']], 4: [['LP4', 'teal']],
      5: [['LP2', 'blue'], ['LP9', 'purple', 1], ['LP10', 'purple', 1], ['LP7 rule', 'blue'], ['LP8 slot', 'blue']],
      6: [['LP1', 'red'], ['LP5', 'teal'], ['LP6', 'teal'], ['LP8', 'blue']], 8: [['LP3 target', 'teal'], ['LP5', 'teal'], ['LP7', 'blue']], 10: [['LP6 late batch', 'teal']],
    };
    const empty = { 1: 'no lever', 7: 'no lever', 9: 'not claimed', 11: 'settings inside a deeper lever only', 12: 'settings inside a deeper lever only' };
    names.forEach((n, i) => {
      const y = 1.32 + i * 0.295;
      L.box(s, 0.5, y, 3.2, 0.26, { fill: fills[i], r: 0.04 });
      L.txt(s, `${i + 1}  ${n}`, 0.6, y, 3.0, 0.26, { fontSize: 11, bold: i < 5, color: i < 5 ? K.white : K.ink, valign: 'middle' });
      const cs = chips[i + 1];
      if (cs) {
        let x = 3.9;
        cs.forEach((c) => {
          const w = 0.3 + c[0].length * 0.075;
          L.chip(s, c[0], x, y + 0.01, w, 0.24, c[1], { size: 10, dash: c[2] ? 'dash' : undefined, r: 0.05 });
          x += w + 0.08;
        });
      } else L.txt(s, empty[i + 1], 3.9, y, 4.5, 0.26, { fontSize: 10.5, color: K.onDark2, italic: true, valign: 'middle' });
    });
    L.txt(s, 'Place 1 is the deepest.', 7.0, 1.32, 2.5, 0.25, { fontSize: 12, color: K.onDark2, bold: true, align: 'right' });
    const key = [['red', 'the route'], ['teal', 'operator levers'], ['blue', 'rule owner levers'], ['purple', 'beliefs and goals']];
    key.forEach((k, i) => L.chip(s, k[1], 6.3 + (i % 2) * 1.65, 4.25 + Math.floor(i / 2) * 0.38, 1.55, 0.3, k[0], { size: 10 }));
    L.txt(s, 'Dashed: held until the payment basis is known', 6.3, 5.02, 3.2, 0.2, { fontSize: 9.5, color: K.onDark2 });
  };
  B[43] = (s, d) => L.decisionCard(s, 9, d);
  // ---- 44 archetype
  B[44] = (s) => {
    L.card(s, 3.75, 2.55, 2.5, 0.85, 'red', { lw: 2 });
    L.txt(s, 'Surplus and run-outs: the symptom', 3.85, 2.55, 2.3, 0.85, { fontSize: 13, bold: true, align: 'center', valign: 'middle' });
    L.card(s, 0.5, 1.4, 3.0, 0.95, 'amber');
    L.icon(s, 'MdTune', 0.95, 1.875, 0.5, K.amber);
    L.txt(s, 'Quick fix: calibrated batch and top-up (LP5, LP6)', 1.3, 1.4, 2.15, 0.95, { fontSize: 12, bold: true, valign: 'middle' });
    L.chip(s, 'QUICK FIX', 0.6, 1.2, 0.9, 0.22, 'amber', { size: 9, bold: true, color: K.amberD });
    L.line(s, 3.5, 2.1, 4.3, 2.55, { color: K.amber, w: 2.5, arrow: true });
    L.txt(s, 'relief within minutes or weeks', 3.55, 1.85, 2.2, 0.24, { fontSize: 11, color: K.amberD, bold: true });
    L.card(s, 6.4, 3.9, 3.1, 1.0, 'teal');
    L.icon(s, 'MdAltRoute', 6.85, 4.4, 0.5, K.teal);
    L.txt(s, 'Fundamental fix: route, default, beliefs, goal (LP1, LP2, LP11, LP12, LP10 once released)', 7.2, 3.9, 2.25, 1.0, { fontSize: 10.5, valign: 'middle' });
    L.line(s, 6.25, 3.2, 7.2, 3.9, { color: K.teal, w: 2.5, arrow: true });
    L.txt(s, 'long delay', 7.25, 3.45, 1.4, 0.22, { fontSize: 11, color: K.teal, bold: true });
    L.line(s, 3.5, 1.65, 8.0, 1.65, { color: K.amber, w: 2, dash: 'dash' });
    L.line(s, 8.0, 1.65, 8.0, 3.85, { color: K.amber, w: 2, dash: 'dash', arrow: true });
    L.txt(s, 'eases pressure on those who could fix the cause (assumed)', 3.6, 1.34, 4.5, 0.24, { fontSize: 11, color: K.amberD, bold: true, align: 'center' });
    L.chip(s, 'Resale replaced Skip Meal', 0.5, 3.85, 2.7, 0.42, 'grey', { size: 11 });
    L.chip(s, 'Attendance billing reverted', 0.5, 4.35, 2.7, 0.42, 'grey', { size: 11 });
    L.tags(s, ['CANDIDATE', 'ASSUMED'], { y: 1.13 });
    L.txt(s, 'LP5 and LP6 are labelled the quick fix throughout.', 3.4, 4.95, 6, 0.25, { fontSize: 12, color: K.muted, italic: true });
  };
  // ---- 45 seven principles
  B[45] = (s) => {
    const p = ['Route before you measure, and route on paper', 'Measure without blame, and judge over months', 'Change the default, goal and belief, not the people', 'Act on the first batch the day before; in the morning only top up',
      'Feed the absorbers by plan; target only the over-cooked batch, repeated reheating and the bin', 'Judge success by cooked against eaten, run-outs and food quality, not turnout', 'Treat measures as diagnostic and plural, never a single target'];
    const cols = ['blue', 'purple', 'orange', 'teal', 'green', 'blue', 'purple'];
    p.forEach((t, i) => {
      const x = 0.5 + (i % 4) * 2.28, y = 1.4 + Math.floor(i / 4) * 1.5;
      L.card(s, x, y, 2.18, 1.38, cols[i]);
      const c = { blue: K.blue, purple: K.purple, orange: K.orange, teal: K.teal, green: K.green }[cols[i]];
      L.circ(s, x + 0.3, y + 0.3, 0.38, c);
      L.txt(s, String(i + 1), x + 0.11, y + 0.11, 0.38, 0.38, { fontSize: 13, bold: true, color: K.white, align: 'center', valign: 'middle' });
      L.txt(s, t, x + 0.12, y + 0.55, 1.95, 0.8, { fontSize: 11 });
    });
    L.card(s, 7.34, 2.9, 2.16, 1.38, 'amber', { dash: 'dash' });
    L.txt(s, 'Added in revision: a figure used against its recorder stops being recorded honestly', 7.46, 2.9, 1.95, 1.38, { fontSize: 11, valign: 'middle', color: K.amberD });
    L.box(s, 0.5, 4.38, 9.0, 0.6, { fill: K.indigo, r: 0.08 });
    L.txt(s, 'Design objective: registration matches intent, the kitchen cooks to expected eaters, and the cost of any gap reaches the rule setters', 0.7, 4.38, 8.6, 0.6, { fontSize: 12.5, bold: true, color: K.white, valign: 'middle' });
  };
  // ---- 46 Sunday slice
  B[46] = (s) => {
    s.addChart(pres.charts.BAR, [{ name: 'Multiple', labels: ['Tuesday', 'Sunday'], values: [1.9, 3.1] }], {
      x: 0.5, y: 1.55, w: 4.3, h: 3.0, barDir: 'col', chartColors: [K.blue, K.red], showLegend: false, showTitle: false, showValue: true, dataLabelFontSize: 16, dataLabelFontFace: '+mn-lt', dataLabelColor: K.text, dataLabelPosition: 'outEnd', dataLabelFormatCode: '0.0',
      valAxisMinVal: 0, valAxisMaxVal: 4, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, catAxisLabelFontSize: 13, catAxisLabelFontFace: '+mn-lt', catAxisLabelColor: K.text, barGapWidthPct: 60,
    });
    L.txt(s, 'A 70% vegetarian batch, as a multiple of those who eat', 0.5, 4.6, 4.3, 0.4, { fontSize: 11, color: K.muted });
    L.txt(s, 'THREE LEVERS MEET ON SUNDAY', 5.2, 1.4, 4.3, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    [['LP2', 'Default and exit', 'blue'], ['LP5', 'Calibrated batch', 'teal'], ['LP6', 'Late batch', 'teal']].forEach((l, i) => {
      const y = 1.72 + i * 0.62;
      L.chip(s, l[0], 5.2, y, 0.8, 0.5, l[2], { solid: true, size: 13, bold: true });
      L.txt(s, l[1], 6.15, y, 3.3, 0.5, { fontSize: 14, valign: 'middle' });
    });
    L.card(s, 5.2, 3.75, 2.05, 0.65, 'teal'); L.txt(s, 'Kadamba: fixed ratio', 5.3, 3.75, 1.85, 0.65, { fontSize: 11.5, valign: 'middle', align: 'center' });
    L.card(s, 7.45, 3.75, 2.05, 0.65, 'teal'); L.txt(s, 'Yuktāhār: plans from records, weighs without blame', 7.5, 3.75, 1.95, 0.65, { fontSize: 10.5, valign: 'middle', align: 'center' });
    L.txt(s, 'Same registration and billing. A learning practice is possible under current rules.', 5.2, 4.5, 4.3, 0.45, { fontSize: 12, color: K.muted, italic: true });
    L.tags(s, ['CONFIRMED'], { y: 1.13 });
  };
};
