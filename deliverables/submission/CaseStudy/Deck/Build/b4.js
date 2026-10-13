// Slides 47 to 65 and the appendix
module.exports = (B, { pres, L, K }) => {
  const HEXRED = 'FF8A80';
  // ---- 47 eight concepts (dark opener)
  B[47] = (s) => {
    const c = [
      ['A', 'The Breakfast Ledger', 'LP1, LP7', 'Fundamental', 'teal'], ['B', 'The Kitchen Learning Kit', 'LP3, LP4, LP5', 'Quick fix', 'amber'], ['C', 'The Crest Plan', 'LP6', 'Quick fix, with B', 'amber'], ['D', 'The Sunday Exit', 'LP2', 'Fundamental, week 6', 'teal'],
      ['E', 'The Operator Menu Slot', 'LP8', 'Fundamental, one loop only', 'teal'], ['F', 'Billed at Consumption', 'LP10', 'Held behind the payment basis', 'grey'], ['G', 'Ratio Cut to 50 Percent', 'no lever', 'Foil', 'red'], ['H', 'The Shared Reading', 'LP11, LP12', 'Fundamental, in the bundle', 'teal'],
    ];
    c.forEach((t, i) => {
      const x = 0.5 + (i % 4) * 2.28, y = 1.4 + Math.floor(i / 4) * 1.7;
      const foil = t[0] === 'G';
      L.card(s, x, y, 2.18, 1.55, t[4] === 'teal' ? 'teal' : t[4], { dash: foil ? 'dash' : undefined });
      const col = { teal: K.teal, amber: K.amber, grey: K.grey, red: K.red }[t[4]];
      L.circ(s, x + 0.32, y + 0.34, 0.4, col);
      L.txt(s, t[0], x + 0.12, y + 0.14, 0.4, 0.4, { fontSize: 15, bold: true, color: K.white, align: 'center', valign: 'middle' });
      L.txt(s, t[1], x + 0.62, y + 0.1, 1.5, 0.5, { fontSize: 12.5, bold: true, valign: 'middle' });
      L.txt(s, t[2], x + 0.14, y + 0.72, 1.9, 0.25, { fontSize: 11, color: K.muted });
      L.chip(s, t[3], x + 0.14, y + 1.05, 1.9, 0.36, t[4], { size: 10, bold: true, color: t[4] === 'amber' ? K.amberD : undefined });
    });
    L.txt(s, 'Prototype: the bundle across one breakfast, on paper.', 0.5, 4.88, 8, 0.28, { fontSize: 14, color: K.onDark2 });
  };
  // ---- 48 ledger and plan card
  B[48] = (s) => {
    L.txt(s, 'SATURDAY EVENING: THE PLAN CARD', 0.5, 1.35, 5, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    const steps = [['164', 'expected eaters'], ['54.7%', 'share in by 9:15'], ['1.5', 'cover'], ['134', 'first batch']];
    steps.forEach((t, i) => {
      const x = 0.5 + i * 1.35;
      L.card(s, x, 1.6, 1.2, 0.95, i === 3 ? 'teal' : 'blue');
      L.big(s, t[0], x, 1.62, 1.2, 0.55, { size: 24, color: i === 3 ? K.teal : K.blue, align: 'center' });
      L.txt(s, t[1], x, 2.18, 1.2, 0.3, { fontSize: 10.5, color: K.muted, align: 'center' });
      if (i < 3) L.txt(s, i === 2 ? '=' : '×', x + 1.18, 1.75, 0.2, 0.4, { fontSize: 16, bold: true, color: K.indigo, align: 'center' });
    });
    L.txt(s, 'AT 9:00: THE LATE BATCH', 0.5, 2.78, 5, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    const rule = [['62', 'diners so far'], ['39.4%', 'usual share by 9:00'], ['173', 'projected, with 10%'], ['39', 'late batch']];
    rule.forEach((t, i) => {
      const x = 0.5 + i * 1.35;
      L.card(s, x, 3.03, 1.2, 0.95, i === 3 ? 'amber' : 'purple');
      L.big(s, t[0], x, 3.05, 1.2, 0.55, { size: 24, color: i === 3 ? K.amberD : K.purple, align: 'center' });
      L.txt(s, t[1], x, 3.6, 1.2, 0.34, { fontSize: 10, color: K.muted, align: 'center' });
    });
    L.txt(s, 'Portions cooked against the 179 who ate (projected)', 0.5, 4.15, 5.2, 0.2, { fontSize: 10.5, bold: true });
    [['Baseline, 70% of 817', 572, K.red], ['Refined: first batch plus late batch', 173, K.indigo], ['Eaten (scans)', 179, K.green]].forEach((b, i) => {
      const y = 4.4 + i * 0.26;
      L.box(s, 2.7, y, b[1] / 572 * 2.6, 0.2, { fill: b[2], r: 0.03 });
      L.txt(s, b[0], 0.5, y, 2.15, 0.2, { fontSize: 10, valign: 'middle' });
      L.txt(s, String(b[1]), 2.75 + b[1] / 572 * 2.6, y, 0.5, 0.2, { fontSize: 10, bold: true, valign: 'middle' });
    });
    // ledger
    L.card(s, 5.95, 1.4, 3.55, 3.3, 'purple');
    L.icon(s, 'MdAssignment', 6.35, 1.82, 0.5, K.purple);
    L.txt(s, 'The weekly ledger', 6.75, 1.55, 2.6, 0.55, { fontSize: 14, bold: true, valign: 'middle' });
    L.txt(s, 'Kadamba vegetarian line, Sunday 19 April 2026', 6.15, 2.2, 3.2, 0.4, { fontSize: 11.5, color: K.muted });
    L.txt(s, '817 registered   179 eaten', 6.15, 2.65, 3.2, 0.3, { fontSize: 14 });
    L.txt(s, '638 charged and not eaten, at Rs 48', 6.15, 2.98, 3.3, 0.3, { fontSize: 14 });
    L.big(s, 'Rs 30,624', 6.1, 3.3, 3.3, 0.8, { size: 40, color: K.red });
    L.txt(s, '817 minus 179 equals 638; 638 times Rs 48 equals Rs 30,624', 6.15, 4.12, 3.25, 0.5, { fontSize: 10.5, color: K.muted });
    L.txt(s, 'Sunday skip: one control, open until 8 pm on Saturday.', 5.95, 4.8, 3.55, 0.35, { fontSize: 12, color: K.muted, italic: true });
    L.tags(s, ['PROJECTED'], { y: 1.13 });
  };
  // ---- 49 backtest chart
  B[49] = (s) => {
    const labs = ['Baseline: 70% of registrations, one batch (759 cooked)', 'Ratio cut to 50% (542 cooked)', 'Calibrated to forecast plus 10%, one batch (440)', 'Calibrated plus late batch at 9:00 (485)'];
    s.addChart(pres.charts.BAR, [
      { name: 'Surplus a day', labels: labs, values: [362, 150, 60, 91] },
      { name: 'Short a day', labels: labs, values: [0, 4.5, 16.8, 2.6] },
    ], {
      x: 0.5, y: 1.35, w: 9.0, h: 2.85, barDir: 'col', barGrouping: 'clustered', chartColors: [K.indigo, K.red], showLegend: true, legendPos: 't', legendFontSize: 11, legendFontFace: '+mn-lt', legendColor: K.text, showTitle: false,
      showValue: true, dataLabelFontSize: 11, dataLabelFontFace: '+mn-lt', dataLabelColor: K.text, dataLabelPosition: 'outEnd', dataLabelFormatCode: 'General', valAxisMinVal: 0, valAxisMaxVal: 420, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' },
      catAxisLabelFontSize: 10.5, catAxisLabelFontFace: '+mn-lt', catAxisLabelColor: K.text, barGapWidthPct: 60,
    });
    L.box(s, 7.0, 1.7, 2.45, 2.5, { line: K.indigo, lw: 2, dash: 'dash', r: 0.1 });
    L.txt(s, 'LINE-DAYS SHORT, OF 46', 0.5, 4.3, 3, 0.2, { fontSize: 9.5, bold: true, color: K.muted, charSpacing: 1 });
    ['0', '7', '16', '7'].forEach((v, i) => L.chip(s, v, 0.55 + i * 2.2, 4.52, 1.6, 0.34, i === 3 ? 'indigo' : 'grey', { size: 13, bold: true }));
    L.txt(s, 'Replay of 23 April days, both lines. Three backtest Sundays: baseline about 563 vegetarian portions for about 190 eaten; refined design about 233.', 0.5, 4.93, 9.0, 0.28, { fontSize: 10.5, color: K.muted });
    L.tags(s, ['PROJECTED'], { y: 1.13 });
  };
  B[50] = (s, d) => { L.decisionCard(s, 10, d); L.tags(s, ['PROJECTED'], { y: 1.13 }); };
  // ---- 51 student side
  B[51] = (s) => {
    L.big(s, 'Rs 10.58 lakh', 0.5, 1.4, 3.8, 0.9, { size: 40, color: K.red });
    L.txt(s, 'estimated charged for 20,221 uneaten breakfasts at Kadamba in April, at posted rates', 0.5, 2.3, 3.6, 0.8, { fontSize: 13, color: K.muted });
    L.txt(s, 'A skip that returns nothing changes nothing.', 0.5, 3.7, 3.6, 0.6, { fontSize: 14, bold: true });
    const x0 = 4.7, sc = 0.84;
    L.txt(s, 'REDUCTION IN THE APRIL CHARGE, RS LAKH', 4.5, 1.35, 5, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 1 });
    [0, 1, 2, 3, 4, 5].forEach((v) => { L.line(s, x0 + v * sc, 1.75, x0 + v * sc, 4.35, { color: 'DDDDDD', w: 0.75 }); L.txt(s, String(v), x0 + v * sc - 0.2, 4.38, 0.4, 0.2, { fontSize: 10, color: K.muted, align: 'center' }); });
    L.txt(s, 'Kitchen rules', 4.5, 1.85, 4.5, 0.25, { fontSize: 13, bold: true });
    L.circ(s, x0, 2.4, 0.2, K.grey); L.txt(s, 'Rs 0', x0 + 0.2, 2.28, 1, 0.25, { fontSize: 13, bold: true, color: K.grey });
    L.txt(s, 'Sunday skip at 25 to 50% uptake', 4.5, 2.75, 4.8, 0.25, { fontSize: 13, bold: true });
    L.box(s, x0 + 0.40 * sc, 3.1, 0.40 * sc, 0.3, { fill: K.blue, r: 0.04 }); L.txt(s, 'Rs 0.40 to 0.80', x0 + 0.9 * sc + 0.1, 3.1, 2, 0.3, { fontSize: 13, bold: true, color: K.blue, valign: 'middle' });
    L.txt(s, 'Every-day skip', 4.5, 3.55, 4.5, 0.25, { fontSize: 13, bold: true });
    L.box(s, x0 + 2.65 * sc, 3.9, (5.29 - 2.65) * sc, 0.3, { fill: K.green, r: 0.04 }); L.txt(s, 'Rs 2.65 to 5.29', x0 + 2.65 * sc, 3.9, (5.29 - 2.65) * sc, 0.3, { fontSize: 13, bold: true, color: K.white, align: 'center', valign: 'middle' });
    L.tags(s, ['PROJECTED', 'ASSUMED'], { y: 1.13 });
  };
  // ---- 52 gates and scores
  B[52] = (s) => {
    const g = [['G1', 'Absorbers that protect someone are kept', 'MdShield'], ['G2', 'The food-safety sequence stays intact', 'MdFactCheck'], ['G3', 'Aims at structure, blames no one, waits on no reversing unknown', 'MdTrackChanges'], ['G4', 'A quick fix is paired with a fundamental fix on a fixed date', 'MdEvent']];
    g.forEach((t, i) => {
      const y = 1.4 + i * 0.86;
      L.card(s, 0.5, y, 3.5, 0.76, 'indigo');
      L.icon(s, t[2], 0.9, y + 0.38, 0.44, K.indigo);
      L.txt(s, [{ text: t[0] + '  ', options: { bold: true, color: K.indigo } }, { text: t[1], options: {} }], 1.3, y, 2.65, 0.76, { fontSize: 11.5, valign: 'middle' });
    });
    L.txt(s, 'Scored 0 to 4 on nine criteria, weights out of 400.', 0.5, 4.88, 3.6, 0.3, { fontSize: 11, color: K.muted, italic: true });
    const items = [['Re-sequenced bundle (passes)', 79, 1], ['First-draft bundle (fails G4)', 79, 0], ['A Breakfast Ledger', 68, 1], ['H Shared Reading', 65, 1], ['F Billed at consumption (fails G3, held)', 63, 0], ['C Crest Plan alone (fails G4)', 63, 0],
      ['D Sunday skip, ratio kept', 60, 1], ['E Operator Menu Slot', 60, 1], ['B Kitchen Kit alone (fails G4)', 58, 0], ['D every-day skip', 50, 1], ['D Sunday opt-in, first draft', 50, 1], ['G Ratio cut to 50% (fails G1)', 48, 0]];
    s.addChart(pres.charts.BAR, [{ name: 'Score', labels: items.map((i) => i[0]), values: items.map((i) => i[1]) }], {
      x: 4.2, y: 1.3, w: 5.3, h: 3.7, barDir: 'bar', chartColors: items.map((i) => (i[2] ? K.blue : K.greyM)), showLegend: false, showTitle: false, showValue: true, dataLabelFontSize: 10, dataLabelFontFace: '+mn-lt', dataLabelColor: K.text, dataLabelPosition: 'outEnd',
      valAxisMinVal: 0, valAxisMaxVal: 100, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, catAxisLabelFontSize: 10, catAxisLabelFontFace: '+mn-lt', catAxisLabelColor: K.text, catAxisOrientation: 'maxMin', barGapWidthPct: 35,
    });
    L.tags(s, ['PROJECTED'], { y: 1.13 });
  };
  B[53] = (s, d) => L.decisionCard(s, 11, d);
  // ---- 54 opposition and ratchet
  B[54] = (s) => {
    const o = ['The Kadamba operator would oppose the Sunday exit if paid on registered plates', 'Bakul’s operator would resist any run-out risk', 'Outside diners and staff are harmed only if the allowance is left unnamed'];
    L.txt(s, 'WHERE OPPOSITION IS EXPECTED', 0.5, 1.4, 4.3, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    o.forEach((t, i) => {
      const y = 1.7 + i * 0.9;
      L.card(s, 0.5, y, 4.3, 0.8, 'red');
      L.icon(s, ['MdEngineering', 'MdLocalShipping', 'MdGroups'][i], 0.9, y + 0.4, 0.44, K.red);
      L.txt(s, t, 1.3, y, 3.4, 0.8, { fontSize: 11.5, valign: 'middle' });
    });
    L.txt(s, 'THE LIKELIEST SIDE EFFECT: THE HEDGE RATCHET', 5.2, 1.4, 4.3, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 1 });
    const n = [['A run-out is loud, a surplus is silent', 5.2, 1.75], ['One complaint after a cut', 7.4, 2.55], ['Batch returns to its old size', 5.2, 3.35]];
    n.forEach((t) => { L.card(s, t[1], t[2], 2.1, 0.7, 'amber', { dash: 'dash' }); L.txt(s, t[0], t[1] + 0.08, t[2], 1.94, 0.7, { fontSize: 11, valign: 'middle', align: 'center' }); });
    L.line(s, 7.3, 2.1, 8.2, 2.55, { color: K.amber, w: 2, arrow: true });
    L.line(s, 8.2, 3.25, 7.3, 3.7, { color: K.amber, w: 2, arrow: true });
    L.line(s, 5.2 + 1.05, 3.35, 6.25, 2.5, { color: K.amber, w: 2, dash: 'dash', arrow: true });
    ['Judge results over months', 'Record every run-out', 'Keep the late batch and the raw reserve', 'Name the allowance; note exam weeks'].forEach((t, i) => L.chip(s, t, 0.5 + i * 2.28, 4.45, 2.18, 0.5, 'green', { size: 10.5 }));
    L.txt(s, 'Twelve groups, reasoned from stated positions; none consulted.', 0.5, 5.0, 6, 0.22, { fontSize: 10.5, color: K.muted, italic: true });
    L.tags(s, ['REASONED', 'CANDIDATE'], { y: 1.13 });
  };
  // ---- 55 the three parts, link built
  B[55] = (s) => {
    L.card(s, 0.5, 1.4, 2.4, 0.8, 'purple');
    L.icon(s, 'MdQrCodeScanner', 0.9, 1.8, 0.42, K.purple);
    L.txt(s, 'Records', 1.25, 1.4, 1.6, 0.8, { fontSize: 14, bold: true, valign: 'middle' });
    L.card(s, 7.1, 1.4, 2.4, 0.8, 'teal');
    L.icon(s, 'MdAccountBalance', 7.5, 1.8, 0.42, K.teal);
    L.txt(s, 'Rule setters', 7.85, 1.4, 1.6, 0.8, { fontSize: 14, bold: true, valign: 'middle' });
    L.line(s, 2.95, 1.8, 7.05, 1.8, { color: K.green, w: 3.5, arrow: true });
    L.txt(s, 'weekly ledger, read jointly with operators and the dining services body', 3.0, 1.38, 4.0, 0.38, { fontSize: 11.5, bold: true, color: K.green, align: 'center' });
    const m = [['The route', 'Build the weekly ledger of booked, cooked and eaten for each hall', 'teal', 'MdAltRoute'], ['The exit', 'Open the Sunday skip; take the payment-basis question to the rule owner at the same time', 'blue', 'MdEvent'], ['The kitchen', 'Plan card, daily sheet and a late batch', 'amber', 'MdTune']];
    m.forEach((c, i) => {
      const x = 0.5 + i * 3.05;
      L.card(s, x, 2.45, 2.9, 1.35, c[2]);
      L.icon(s, c[3], x + 0.4, 2.85, 0.46, { teal: K.teal, blue: K.blue, amber: K.amber }[c[2]]);
      L.txt(s, c[0], x + 0.78, 2.5, 1.5, 0.7, { fontSize: 14, bold: true, valign: 'middle' });
      L.txt(s, c[1], x + 0.15, 3.18, 2.65, 0.6, { fontSize: 10.5 });
    });
    L.chip(s, 'QUICK FIX', 8.05, 3.45, 1.25, 0.24, 'amber', { size: 9, bold: true, color: K.amberD });
    // thirteen actions
    L.txt(s, 'THIRTEEN ACTIONS, BY WHO CAN FINISH THEM', 0.5, 3.98, 6, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 1 });
    const grp = [[2, K.orange, 'The team alone: ledger, cards and sheet; co-design tests'], [4, K.blue, 'Convene or support'], [6, K.teal, 'Carried as evidenced proposals'], [1, K.indigo, 'Must complete: handover by week 20']];
    let k = 0;
    grp.forEach((g) => { for (let i = 0; i < g[0]; i++) { L.circ(s, 0.7 + k * 0.42, 4.42, 0.32, g[1]); k++; } });
    let ly = 4.2;
    grp.forEach((g) => { L.circ(s, 7.3, ly + 0.08, 0.14, g[1]); L.txt(s, `${g[0]}  ${g[2]}`, 7.5, ly, 2.1, 0.2, { fontSize: 9.5, valign: 'middle' }); ly += 0.22; });
    L.txt(s, 'The Kadamba supervisor decides on the batches; only the rule owner can open the Sunday exit.', 0.5, 4.78, 8, 0.28, { fontSize: 12, color: K.muted, italic: true });
  };
  // ---- 56 twenty weeks
  B[56] = (s) => {
    const x0 = 1.8, wk = 0.385, X = (w) => x0 + w * wk;
    [[0, 4, K.green, 'Stage 1'], [5, 8, K.blue, 'Stage 2'], [9, 20, K.purple, 'Stage 3']].forEach((st) => {
      L.box(s, X(st[0]), 1.35, X(st[1] + (st[1] === 20 ? 0 : 1)) - X(st[0]) - 0.03, 0.26, { fill: st[2], r: 0.05 });
      L.txt(s, `${st[3]}  weeks ${st[0]} to ${st[1]}`, X(st[0]), 1.35, X(st[1] + (st[1] === 20 ? 0 : 1)) - X(st[0]) - 0.03, 0.26, { fontSize: 9.5, bold: true, color: K.white, align: 'center', valign: 'middle' });
    });
    [0, 4, 8, 12, 16, 20].forEach((w) => L.txt(s, String(w), X(w) - 0.2, 1.62, 0.4, 0.18, { fontSize: 9.5, color: K.muted, align: 'center' }));
    const lanes = [
      ['Fundamental fix', 1.85, 'teal', [[0, 4, 'Ledger, charge line, co-design tests'], [5.5, 10, 'Sunday skip proposed at week 6, in force about week 10'], [10.2, 20, 'Every-day skip decision at week 14; operator forum; menu notes']]],
      ['Quick fix', 2.45, 'amber', [[0, 4, 'Cards and sheet drafted with the supervisor'], [5, 10, 'Sunday vegetarian pilot: card, allowance, 9:00 batch, sheet'], [10.2, 20, 'Every day, both lines; Yuktāhār re-anchors']]],
      ['Handover', 3.05, 'grey', [[10.2, 20, 'Week 16 the dining services body compiles with the team; week 18 alone; week 20 the team steps back']]],
      ['Held until facts are known', 3.55, 'red', [[0, 20, 'Billing and payment basis (LP10); a named owner (LP9); Bakul once it has records']]],
    ];
    lanes.forEach((ln) => {
      L.txt(s, ln[0], 0.5, ln[1], 1.25, 0.5, { fontSize: 10, bold: true, valign: 'middle', color: ln[2] === 'amber' ? K.amberD : K.text });
      ln[3].forEach((it) => {
        const h = ln[0] === 'Held until facts are known' ? 0.4 : ln[0] === 'Handover' ? 0.42 : 0.54;
        L.card(s, X(it[0]), ln[1], X(it[1]) - X(it[0]) - 0.04, h, ln[2], { dash: ln[2] === 'red' ? 'dash' : undefined });
        L.txt(s, it[2], X(it[0]) + 0.06, ln[1], X(it[1]) - X(it[0]) - 0.16, h, { fontSize: 9.5, valign: 'middle' });
      });
    });
    [[4, 'joint reading'], [6, 'DP1'], [10, 'skip in force'], [14, 'DP2'], [20, 'team steps back']].forEach((m) => {
      L.circ(s, X(m[0]), 4.07, 0.16, K.red);
      L.txt(s, m[1], m[0] === 20 ? 8.3 : X(m[0]) - 0.6, 4.14, m[0] === 20 ? 1.2 : 1.2, 0.18, { fontSize: 9, color: K.red, bold: true, align: m[0] === 20 ? 'right' : 'center' });
    });
    const dp = [['DP1, week 6', 'Goes ahead on this date; if declined, the charge line goes to the escalation forum'], ['DP2, week 14', 'Sunday uptake at least 25% and no Sunday over 10 short; under 10%, retest the wording'], ['DP3, after a term of DP2', 'Opt-in on the lowest-turnout days'], ['DP4, payment basis known', 'Bill on consumption or pay on served plates']];
    dp.forEach((d, i) => {
      const x = 0.5 + i * 2.28;
      L.box(s, x, 4.4, 2.18, 0.78, { fill: K.indigoTint, r: 0.06 });
      L.txt(s, d[0], x + 0.08, 4.42, 2.05, 0.18, { fontSize: 9.5, bold: true, color: K.indigo });
      L.txt(s, d[1], x + 0.08, 4.6, 2.05, 0.56, { fontSize: 9 });
    });
    L.tags(s, ['PLANNED'], { y: 1.0, right: 9.5 });
  };
  B[57] = (s, d) => { L.decisionCard(s, 12, d); L.tags(s, ['PROJECTED', 'ASSUMED'], { y: 1.13 }); };
  // ---- 58 pilot conditions
  B[58] = (s) => {
    L.box(s, 0.5, 1.4, 4.2, 3.35, { fill: K.greenT, r: 0.08 });
    L.txt(s, 'SUCCESS', 0.7, 1.5, 3.5, 0.2, { fontSize: 10, bold: true, color: K.green, charSpacing: 2 });
    L.txt(s, 'Sunday vegetarian surplus, portions', 0.7, 1.75, 3.8, 0.25, { fontSize: 12, bold: true });
    L.box(s, 0.7, 2.08, 3.0, 0.3, { fill: K.red, r: 0.04 }); L.txt(s, 'about 370 now', 0.8, 2.08, 2.8, 0.3, { fontSize: 11, color: K.white, bold: true, valign: 'middle' });
    L.box(s, 0.7, 2.45, 0.8, 0.3, { fill: K.green, r: 0.04 }); L.txt(s, 'under 100 (model about 45)', 1.6, 2.45, 2.6, 0.3, { fontSize: 11, bold: true, color: K.green, valign: 'middle' });
    ['No Sunday more than 10 short', 'Run-outs no more frequent than on comparison days', 'Every allowance meal served', 'Grams and taste hold; every safety step recorded'].forEach((t, i) => {
      const y = 2.95 + i * 0.44;
      L.icon(s, 'MdCheckCircle', 0.9, y + 0.17, 0.3, K.green);
      L.txt(s, t, 1.15, y, 3.4, 0.36, { fontSize: 11.5, valign: 'middle' });
    });
    L.txt(s, 'STOP CONDITIONS', 5.0, 1.45, 4.5, 0.2, { fontSize: 10, bold: true, color: K.red, charSpacing: 2 });
    ['Shortage beyond one top-up on two Sundays running', 'The late batch fails twice', 'Any allowance meal missed', 'Grams below standard', 'Any figure used against staff', 'Consent withdrawn'].forEach((t, i) => {
      const x = 5.0 + (i % 2) * 2.3, y = 1.75 + Math.floor(i / 2) * 1.0;
      L.card(s, x, y, 2.2, 0.9, 'red');
      L.icon(s, 'MdStop', x + 0.32, y + 0.45, 0.36, K.red);
      L.txt(s, t, x + 0.62, y, 1.52, 0.9, { fontSize: 11, valign: 'middle' });
    });
    L.txt(s, 'Judged at week 16 against Sunday non-vegetarian, Saturday vegetarian and earlier Sundays. Run by the Kadamba supervisor.', 0.5, 4.85, 9, 0.35, { fontSize: 11.5, color: K.muted });
    L.tags(s, ['PLANNED'], { y: 1.13 });
  };
  B[59] = (s, d) => L.decisionCard(s, 13, d);
  // ---- 60 projected response
  B[60] = (s) => {
    L.txt(s, 'FIRST-BATCH SURPLUS AT KADAMBA, PORTIONS A DAY', 0.5, 1.4, 6, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 1 });
    const x0 = 2.0, sc = 7.3 / 500;
    [0, 100, 200, 300, 400, 500].forEach((v) => { L.line(s, x0 + v * sc, 1.9, x0 + v * sc, 2.95, { color: 'DDDDDD', w: 0.75 }); L.txt(s, String(v), x0 + v * sc - 0.2, 2.97, 0.4, 0.18, { fontSize: 9.5, color: K.muted, align: 'center' }); });
    L.txt(s, 'Now', 0.5, 1.95, 1.4, 0.4, { fontSize: 13, bold: true, valign: 'middle' });
    L.box(s, x0 + 254 * sc, 1.98, (471 - 254) * sc, 0.34, { fill: K.red, r: 0.04 }); L.txt(s, '254 to 471', x0 + 254 * sc, 1.98, (471 - 254) * sc, 0.34, { fontSize: 12, bold: true, color: K.white, align: 'center', valign: 'middle' });
    L.txt(s, 'After about four months', 0.5, 2.45, 1.45, 0.4, { fontSize: 11.5, bold: true, valign: 'middle' });
    L.box(s, x0 + 69 * sc, 2.48, (120 - 69) * sc, 0.34, { fill: K.green, r: 0.04 }); L.txt(s, 'about 69 to 120', x0 + 120 * sc + 0.1, 2.48, 2, 0.34, { fontSize: 12, bold: true, color: K.green, valign: 'middle' });
    L.txt(s, 'WEEKLY CHARGE FOR UNEATEN BREAKFASTS, RS LAKH', 0.5, 3.35, 6, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 1 });
    const y0 = 3.6, sc2 = 7.3 / 3.0;
    [0, 1, 2, 3].forEach((v) => { L.line(s, x0 + v * sc2, y0 + 0.05, x0 + v * sc2, y0 + 1.05, { color: 'DDDDDD', w: 0.75 }); L.txt(s, String(v), x0 + v * sc2 - 0.2, y0 + 1.07, 0.4, 0.18, { fontSize: 9.5, color: K.muted, align: 'center' }); });
    L.txt(s, 'Now', 0.5, y0 + 0.08, 1.4, 0.26, { fontSize: 12, bold: true });
    L.box(s, x0, y0 + 0.1, 2.47 * sc2, 0.24, { fill: K.red, r: 0.04 }); L.txt(s, 'about 2.47', x0 + 0.1, y0 + 0.1, 2, 0.24, { fontSize: 11, bold: true, color: K.white, valign: 'middle' });
    L.txt(s, 'Sunday skip', 0.5, y0 + 0.4, 1.4, 0.26, { fontSize: 12, bold: true });
    L.box(s, x0 + 2.27 * sc2, y0 + 0.42, (2.37 - 2.27) * sc2, 0.24, { fill: K.blue, r: 0.04 }); L.txt(s, '2.27 to 2.37', x0 + 2.37 * sc2 + 0.08, y0 + 0.42, 1.5, 0.24, { fontSize: 11, bold: true, color: K.blue, valign: 'middle' });
    L.txt(s, 'Every-day skip', 0.5, y0 + 0.72, 1.4, 0.26, { fontSize: 12, bold: true });
    L.box(s, x0 + 1.23 * sc2, y0 + 0.74, (1.85 - 1.23) * sc2, 0.24, { fill: K.green, r: 0.04 }); L.txt(s, '1.23 to 1.85', x0 + 1.85 * sc2 + 0.08, y0 + 0.74, 1.5, 0.24, { fontSize: 11, bold: true, color: K.green, valign: 'middle' });
    L.txt(s, 'Surplus starts to fall with the Sunday pilot; the charge moves only when the skip comes into force. Not tested on campus.', 0.5, 4.95, 9, 0.25, { fontSize: 11, color: K.muted, italic: true });
    L.tags(s, ['PROJECTED', 'ASSUMED'], { y: 1.13 });
  };
  // ---- 61 what it means (dark opener)
  B[61] = (s) => {
    L.plate(s, 1.2, 2.3, 1.1, { eaten: 37.1, ring: K.onDark2, lw: 2 }); L.txt(s, 'Kadamba', 0.5, 2.9, 1.4, 0.25, { fontSize: 12, color: K.white, align: 'center', bold: true });
    L.plate(s, 2.7, 2.3, 1.1, { eaten: 28, ring: K.onDark2, lw: 2 }); L.txt(s, 'Yuktāhār', 2.0, 2.9, 1.4, 0.25, { fontSize: 12, color: K.white, align: 'center', bold: true });
    L.txt(s, 'Share the rules, differ in kitchen practice, and show the same wide gap', 0.5, 3.3, 2.9, 0.7, { fontSize: 12, color: K.onDark2 });
    L.card(s, 3.8, 1.5, 2.6, 0.8, 'red');
    L.txt(s, 'Centre: no correction', 3.8, 1.5, 2.6, 0.8, { fontSize: 14, bold: true, align: 'center', valign: 'middle' });
    L.card(s, 3.8, 3.2, 2.6, 0.8, 'green');
    L.txt(s, 'Kitchen: local loops that work', 3.8, 3.2, 2.6, 0.8, { fontSize: 14, bold: true, align: 'center', valign: 'middle' });
    L.line(s, 5.1, 3.2, 5.1, 2.9, { color: HEXRED, w: 2.5, dash: 'dash' });
    L.icon(s, 'MdLinkOff', 5.1, 2.65, 0.34, K.red);
    L.line(s, 5.1, 2.4, 5.1, 2.32, { color: HEXRED, w: 2.5, dash: 'dash', arrow: true });
    const ins = [['MdLoop', 'Every working loop sits inside a kitchen'], ['MdVisibilityOff', 'A quick fix can make the central problem harder to see'], ['MdAccountTree', 'No office owns the chain from registration to bin']];
    ins.forEach((t, i) => {
      const y = 1.5 + i * 0.95;
      L.icon(s, t[0], 7.0, y + 0.3, 0.5, K.indigo);
      L.txt(s, t[1], 7.4, y, 2.1, 0.7, { fontSize: 12.5, color: K.white, valign: 'middle' });
    });
    L.txt(s, 'The first step costs a weekly sheet and a meeting.', 0.5, 4.7, 8, 0.3, { fontSize: 14, color: K.onDark2 });
  };
  // ---- 62 limits (dark)
  B[62] = (s) => {
    const t = [['6', 'students: six people are not a population'], ['1', 'visit per kitchen: operators describe their own practice'], ['2', 'record sets, two halls, two months; Bakul has none'], ['1', 'hall’s scans feed the model: shocks are assumed'], ['0', 'co-design tests run: responses are reasoned, no one consulted']];
    t.forEach((c, i) => {
      const x = 0.5 + i * 1.82;
      L.card(s, x, 1.45, 1.72, 1.85, 'indigo');
      L.big(s, c[0], x, 1.5, 1.72, 0.8, { size: 44, color: K.indigo, align: 'center' });
      L.txt(s, c[1], x + 0.1, 2.3, 1.52, 0.95, { fontSize: 11, align: 'center' });
    });
    ['The loop test is strict by design: three describes the evidence', 'Scoring weights are the team’s judgement', 'Halls differ in five ways beyond the planning rule', 'Interviewers were peers of the respondents'].forEach((c, i) => {
      L.chip(s, c, 0.5 + (i % 2) * 4.55, 3.55 + Math.floor(i / 2) * 0.55, 4.45, 0.46, 'grey', { size: 11, dash: 'dash' });
    });
    L.txt(s, 'Disposal after the close and a live breakfast were not observed.', 0.5, 4.8, 8, 0.28, { fontSize: 14, color: K.onDark2 });
  };
  // ---- 63 open conflicts
  B[63] = (s) => {
    const c = [['1', 'Who heads the dining services body', 'Two different people are on record'], ['2', 'Whether Skip Meal lowers the count Kadamba cooks from', 'The institution says yes; the portal says staff are told; the operator says it cooks on registrations'], ['3', 'Whether operators are paid on registered or served plates', 'The one that matters most']];
    c.forEach((t, i) => {
      const x = 0.5 + i * 3.05;
      L.card(s, x, 1.4, 2.9, 1.75, 'red');
      L.circ(s, x + 0.35, 1.78, 0.4, K.red); L.txt(s, t[0], x + 0.15, 1.58, 0.4, 0.4, { fontSize: 14, bold: true, color: K.white, align: 'center', valign: 'middle' });
      L.txt(s, t[1], x + 0.7, 1.5, 2.1, 0.6, { fontSize: 12.5, bold: true, valign: 'middle' });
      L.txt(s, t[2], x + 0.15, 2.2, 2.65, 0.9, { fontSize: 11 });
    });
    const q = [['Payment basis', 'contracts or the dining services body'], ['Skip Meal count', 'the dining services body'], ['Sunday skip uptake', 'students'], ['Late batch landing by 9:15', 'operators'], ['What Kadamba’s 5 to 10% waste is a percentage of', 'operators'], ['Who set the four-day close and the cap of five', 'the institution and its contracts'], ['Who heads the dining services body', 'the dining services body'], ['Whether the April pattern holds in other months and halls', 'scan exports not yet obtained']];
    q.forEach((t, i) => {
      const x = 0.5 + (i % 2) * 4.55, y = 3.3 + Math.floor(i / 2) * 0.42;
      L.box(s, x, y, 4.45, 0.37, { fill: K.greyT, r: 0.05 });
      L.txt(s, [{ text: t[0], options: { bold: true } }, { text: '  ' + t[1], options: { color: K.muted } }], x + 0.1, y, 4.3, 0.37, { fontSize: 10, valign: 'middle' });
    });
    L.tags(s, ['OPEN'], { y: 1.13 });
    L.txt(s, 'The case does not choose between them.', 0.5, 5.02, 5, 0.22, { fontSize: 10.5, color: K.muted, italic: true });
  };
  // ---- 64 reflections (dark)
  B[64] = (s) => {
    const cols = [['What worked', 'green', ['Saying how sure we were from the first document', 'Treating each operator as its own system', 'Keeping a foil in every test']],
      ['What we would change', 'amber', ['Go to the kitchens first and ask for the records sooner', 'Be slower to name a fix and an owner', 'Notice we built the burden-shifting pattern into our own plan']],
      ['Next steps', 'blue', ['Obtain the missing records, including Bakul’s item-level record', 'Settle each operator’s payment basis', 'Run the co-design tests, the pilot and a test of Sunday skip uptake; then extend to lunch and dinner']]];
    cols.forEach((c, i) => {
      const x = 0.5 + i * 3.05;
      L.card(s, x, 1.4, 2.9, 2.85, c[1]);
      L.txt(s, c[0], x + 0.15, 1.5, 2.6, 0.35, { fontSize: 15, bold: true, fontFace: 'Cambria' });
      c[2].forEach((t, k) => {
        const y = 1.95 + k * 0.76;
        L.circ(s, x + 0.3, y + 0.17, 0.12, { green: K.green, amber: K.amber, blue: K.blue }[c[1]]);
        L.txt(s, t, x + 0.5, y, 2.3, 0.72, { fontSize: 11 });
      });
    });
    L.card(s, 0.5, 4.45, 1.5, 0.6, 'purple'); L.txt(s, 'Records', 0.5, 4.45, 1.5, 0.6, { fontSize: 13, bold: true, align: 'center', valign: 'middle' });
    L.line(s, 2.05, 4.75, 3.35, 4.75, { color: K.green, w: 3.5, arrow: true });
    L.card(s, 3.4, 4.45, 1.5, 0.6, 'teal'); L.txt(s, 'Rule setters', 3.4, 4.45, 1.5, 0.6, { fontSize: 13, bold: true, align: 'center', valign: 'middle' });
    L.txt(s, 'The records existed all along.', 5.2, 4.45, 4.3, 0.6, { fontSize: 18, bold: true, fontFace: 'Cambria', color: K.white, valign: 'middle' });
  };
  // ---- 65 questions (dark)
  B[65] = (s) => {
    const q = [['MdPsychology', 'Why do people hold a belief above their own record, and how do you present a number so it is used, not feared?'], ['MdVolumeUp', 'Why did menu fatigue reach the rule setters while a larger, quiet gap did not?'],
      ['MdBalance', 'Should the team propose a kitchen bundle that leaves bills untouched?'], ['MdHelp', 'Billing on attendance ran twice and was switched off: which of three explanations would you test first?'],
      ['MdGavel', 'How do you propose a rule whose fairness depends on a fact you cannot get?'], ['MdBlock', 'Where in your own work would a deliberately weak concept be useful?']];
    q.forEach((t, i) => {
      const x = 0.5 + (i % 3) * 3.05, y = 1.4 + Math.floor(i / 3) * 1.55;
      L.card(s, x, y, 2.9, 1.42, 'indigo');
      L.circ(s, x + 0.3, y + 0.3, 0.38, K.indigo); L.txt(s, String(i + 1), x + 0.11, y + 0.11, 0.38, 0.38, { fontSize: 13, bold: true, color: K.white, align: 'center', valign: 'middle' });
      L.txt(s, t[1], x + 0.15, y + 0.58, 2.62, 0.82, { fontSize: 11 });
    });
    L.plate(s, 8.95, 4.75, 0.75, { eaten: 37.1, ring: K.onDark2, lw: 1.5 });
    L.txt(s, 'Team Invictus. Thank you.', 0.5, 4.7, 6, 0.4, { fontSize: 18, bold: true, color: K.white, fontFace: 'Cambria' });
    L.txt(s, 'Sricharan Peri, Prathyusha Kalluri, Neha Susan Manoj', 0.5, 5.02, 6, 0.22, { fontSize: 11, color: K.onDark2 });
  };

  // ------------------------------------------------------------ appendix
  const tbl = (s, rows, x, y, w, colW, size = 10) => {
    const body = rows.map((r, ri) => r.map((c) => ({ text: c, options: { bold: ri === 0, fill: ri === 0 ? { color: K.indigoTint } : { color: ri % 2 ? 'FFFFFF' : 'F6F6F9' }, color: K.text, fontSize: size, valign: 'middle' } })));
    s.addTable(body, { x, y, w, colW, border: { type: 'solid', pt: 0.5, color: 'C9CDE0' }, margin: [0.04, 0.07, 0.04, 0.07], fontFace: 'Calibri', autoPage: false });
  };
  B.A1 = (s) => {
    tbl(s, [['No.', 'Objective', 'Activity', 'Phase'],
      ['1', 'Fix the boundary and separate visible symptoms from underlying issues', '1', '1'], ['2', 'Identify the people and bodies in the system and what each needs', '2', '1'], ['3', 'Establish who holds authority, power and leverage over each decision', '3', '1'],
      ['4', 'Trace how a registration becomes cooked food', '4', '1'], ['5', 'Measure behaviour over a morning, a week and a month', '5', '1'], ['6', 'Build a model and test which feedback mechanisms close', '6', '2'],
      ['7', 'Trace events to structures and beliefs, and reframe the problem', '7 and 8', '2'], ['8', 'Find where change could act and what any change must protect', '9', '3'], ['9', 'Design, test and evaluate interventions', '10', '4']], 0.5, 1.2, 9.0, [0.6, 6.4, 1.2, 0.8], 11);
  };
  B.A1b = (s) => {
    tbl(s, [['Source', 'What it gave', 'Main limit'],
      ['A team member’s own account, 3 September', 'The system and a student’s mornings', 'One person, who is also a stakeholder'], ['Nine portal screens', 'Registration dialog, capacities, rates and charges', 'Each screen shows one day'],
      ['Five student interviews, 6 September', 'Two daily eaters and three skippers', 'Four or five distinct people'], ['Head of facilities, 13 September, with a walkthrough of Kadamba’s kitchen and four posters', 'Governance, menu rotation, stock, waste and food safety', 'One respondent; posters state intent'],
      ['Operator visits to three kitchens, 26 September, and a first-hand account, 27 September', 'Ordering, registers, rules of thumb and surplus routes', 'Operators describe their own practice'], ['Yuktāhār’s books and registers, 26 September', '26 photographs, turned into 22 tables', 'Some breakfast rows partly hidden by a hand'],
      ['Kadamba scan export, April 2026', 'Every breakfast registration with its scan time', 'One hall, one meal, one month']], 0.5, 1.2, 9.0, [3.6, 3.0, 2.4], 11);
  };
  B.A2 = (s) => {
    tbl(s, [['Lever', 'What it is', 'Place', 'Can a student team act on it?'],
      ['LP1', 'Build the missing routes from records to rule owners', '6', 'Yes: high to prototype, medium to deliver'], ['LP2', 'Change the breakfast default and its exit', '5', 'Propose only; the rule owner decides'],
      ['LP3', 'Make surplus a cost in the operator’s goal', '3', 'Low to medium; operator management'], ['LP4', 'An operator forum that runs its own trials', '4', 'Medium; operators, with the dining services body convening'],
      ['LP5', 'A record-calibrated first batch and a daily record', '6, 8', 'Operator decides; high at Yuktāhār, medium at Kadamba, unsizeable at Bakul'], ['LP6', 'Crest-aware top-up and a staged late batch', '6, 10', 'Operator decides; high at Kadamba, low at Bakul'],
      ['LP7', 'A cost trigger on the oversight line', '8', 'Medium, after LP1'], ['LP8', 'Operator voice in the menu', '6', 'Medium; the menu committee'], ['LP9', 'A named owner of booked, cooked and eaten', '5', 'Held; low'],
      ['LP10', 'What a booking costs: billing at consumption', '5', 'Held; low'], ['LP11', 'Test the governing mental models', '2', 'Medium; each belief’s holder'], ['LP12', 'Change the goal actually sought', '3', 'Low to medium; the parent and dining services bodies']], 0.5, 1.15, 9.0, [0.7, 3.7, 0.7, 3.9], 10);
    L.txt(s, 'The ladder on slide 42 shows additional places for LP3, LP5, LP7 and LP8 and is the authority for the chip positions.', 0.5, 4.95, 9, 0.25, { fontSize: 10, color: K.muted, italic: true });
  };
  B.A3 = (s) => {
    tbl(s, [['Decision point', 'When', 'Rule, and what happens if the evidence goes the other way'],
      ['DP1 Sunday skip', 'Week 6; in force about week 10', 'Goes ahead on this date; if declined, the Sunday charge line goes to the escalation forum'],
      ['DP2 Every-day skip', 'Week 14; from about week 16', 'Sunday uptake at least 25 per cent and no Sunday more than 10 short; if uptake is under 10 per cent, the wording is retested'],
      ['DP3 Default matched to intent', 'After a term of DP2', 'Opt-in on the lowest-turnout days; if uptake is low and the charge stable, the skip and default stay'],
      ['DP4 Billing and payment', 'Once the payment basis is known', 'Billing at consumption or payment on served plates; if plates are registered and there is no rate agreement, billing stays and the skip carries the students']], 0.5, 1.3, 9.0, [2.2, 2.2, 4.6], 12);
    L.txt(s, 'The thresholds are the team’s judgement.', 0.5, 4.85, 6, 0.25, { fontSize: 11, color: K.muted, italic: true });
  };
  B.A4 = (s) => {
    tbl(s, [['Question', 'Who could answer it'],
      ['What a plate counts for in each operator’s monthly payment; no contract has been seen', 'The institution’s contracts or the dining services body'], ['Whether Skip Meal lowers the count that Kadamba cooks from', 'The dining services body'],
      ['How many students would take a Sunday skip (assumed 25 to 50% of no-shows, tested from 10 to 75)', 'The students'], ['Whether a late batch cooked at 9:00 can land by about 9:15 without delaying service at the crest', 'The operators'],
      ['What Kadamba’s stated 5 to 10% waste figure is a percentage of', 'The operators'], ['Who set the four-day close and the limit of five cancellations', 'The institution and its contracts'], ['Who heads the dining services body', 'The dining services body'],
      ['Whether the April pattern holds in other months and at the halls without records', 'Scan exports not yet obtained']], 0.5, 1.2, 9.0, [6.2, 2.8], 11);
  };
};
