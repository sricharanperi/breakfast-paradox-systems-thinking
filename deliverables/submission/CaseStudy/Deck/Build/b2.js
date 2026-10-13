// Slides 12 to 30: understanding the system
const path = require('path');
module.exports = (B, { pres, L, K, FIGS }) => {
  const WORK = path.join(__dirname, 'work', 'img');
  // ---- 12 boundary (dark opener)
  B[12] = (s) => {
    L.box(s, 0.9, 2.0, 8.2, 2.62, { line: K.onDark2, lw: 1.5, dash: 'dash', r: 0.3 });
    L.txt(s, 'THE BOUNDARY', 1.15, 2.1, 3, 0.2, { fontSize: 10, bold: true, color: K.onDark2, charSpacing: 3 });
    const cards = [['Registration and billing', 'The portal and the counter scan', 'MdHowToReg'], ['Kitchens', 'One caterer per hall', 'MdRestaurant'], ['Governance', 'Rule owners and committees', 'MdAccountBalance']];
    cards.forEach((c, i) => {
      const x = 1.3 + i * 2.7;
      const role = i === 2 ? 'teal' : 'blue';
      L.card(s, x, 2.45, 2.5, 1.15, role);
      L.icon(s, c[2], x + 0.4, 3.02, 0.45, i === 2 ? K.teal : K.blue);
      L.txt(s, c[0], x + 0.78, 2.55, 1.65, 0.45, { fontSize: 13, bold: true });
      L.txt(s, c[1], x + 0.78, 3.0, 1.65, 0.55, { fontSize: 11, color: K.muted });
    });
    L.chip(s, '30 to 50 outsiders and about half the operator’s staff eat from the same pots', 2.2, 3.85, 5.6, 0.5, 'green', { size: 12 });
    L.chip(s, 'Class schedule', 0.5, 1.38, 2.2, 0.42, 'grey', { dash: 'dash', size: 12 });
    L.chip(s, 'Alternatives: outside venues', 7.3, 1.38, 2.2, 0.42, 'grey', { dash: 'dash', size: 12 });
    L.txt(s, 'Lunch and dinner sit outside and serve as the comparison.', 0.5, 4.8, 8, 0.3, { fontSize: 14, color: K.onDark2 });
  };
  // ---- 13 stated vs actual
  B[13] = (s) => {
    L.txt(s, 'STATED DESIGN', 2.3, 1.3, 3, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    L.txt(s, 'ACTUAL MECHANISM', 6.1, 1.3, 3, 0.2, { fontSize: 10, bold: true, color: K.red, charSpacing: 2 });
    const rows = [
      ['What registration records', 'Demand, estimated in advance', 'A default students do not choose, flat across the week', 'MdHowToReg'],
      ['How kitchens plan', 'From the advance count', 'Each operator’s own conversion of the day-before count', 'MdRestaurant'],
      ['Where surplus goes', 'Minimised by planning', 'Reuse, outside diners and staff, held food, the bin', 'MdDelete'],
    ];
    rows.forEach((r, i) => {
      const y = 1.6 + i * 1.12;
      L.icon(s, r[3], 0.78, y + 0.5, 0.5, K.indigo);
      L.txt(s, r[0], 1.15, y, 1.1, 1.0, { fontSize: 12, bold: true, valign: 'middle' });
      L.box(s, 2.3, y, 3.3, 1.0, { fill: K.greyT, r: 0.08 });
      L.txt(s, r[1], 2.45, y, 3.0, 1.0, { fontSize: 14, valign: 'middle', color: K.muted });
      L.line(s, 5.65, y + 0.5, 5.95, y + 0.5, { color: K.indigo, w: 2.5, arrow: true });
      L.card(s, 6.1, y, 3.4, 1.0, 'red');
      L.txt(s, r[2], 6.25, y, 3.1, 1.0, { fontSize: 14, valign: 'middle' });
    });
    L.chip(s, 'Held food is a candidate route', 6.1, 4.95, 2.3, 0.28, 'amber', { size: 10, color: K.amberD });
    L.tags(s, ['CONFIRMED'], { y: 1.0, right: 9.5 });
    L.txt(s, 'The institution’s posters state the aim.', 0.5, 4.95, 4, 0.25, { fontSize: 11, color: K.muted });
  };
  // ---- 14 overstate + missing link
  B[14] = (s) => {
    L.big(s, '2.7 times', 0.5, 1.4, 2.9, 0.75, { size: 40, color: K.red });
    L.txt(s, 'Kadamba', 0.5, 2.15, 2.9, 0.25, { fontSize: 14, color: K.muted });
    L.big(s, '3.5 times', 0.5, 2.6, 2.9, 0.75, { size: 40, color: K.red });
    L.txt(s, 'Yuktāhār', 0.5, 3.35, 2.9, 0.25, { fontSize: 14, color: K.muted });
    L.txt(s, 'registrations against who eats', 0.5, 3.7, 2.9, 0.25, { fontSize: 12, color: K.muted });
    L.card(s, 3.7, 1.45, 2.3, 0.85, 'purple');
    L.icon(s, 'MdQrCodeScanner', 4.05, 1.875, 0.42, K.purple);
    L.txt(s, 'Scan record: who ate and when', 4.4, 1.45, 1.55, 0.85, { fontSize: 12, valign: 'middle' });
    L.card(s, 3.7, 2.5, 2.3, 0.85, 'purple');
    L.icon(s, 'MdMenuBook', 4.05, 2.925, 0.42, K.purple);
    L.txt(s, 'Operators’ registers', 4.4, 2.5, 1.55, 0.85, { fontSize: 12, valign: 'middle' });
    L.card(s, 7.7, 1.85, 1.8, 1.1, 'teal');
    L.icon(s, 'MdAccountBalance', 8.6, 2.2, 0.4, K.teal);
    L.txt(s, 'Registration and billing rules', 7.8, 2.45, 1.6, 0.45, { fontSize: 12, bold: true, align: 'center' });
    L.line(s, 6.0, 1.875, 6.5, 2.35, { color: K.red, w: 1.5, dash: 'dash' });
    L.line(s, 6.0, 2.925, 6.5, 2.45, { color: K.red, w: 1.5, dash: 'dash' });
    L.link(s, 6.5, 2.4, 7.65, 'broken', { label: 'no route' });
    L.chip(s, '20,221 breakfasts billed and not eaten, Kadamba, April 2026', 3.7, 3.7, 5.8, 0.55, 'red', { size: 14, bold: true });
    L.txt(s, 'Operators control quantities, never registration, billing or the menu.', 3.7, 4.45, 5.8, 0.3, { fontSize: 14, color: K.muted });
    L.tags(s, ['CONFIRMED'], { y: 1.13 });
  };
  // ---- 15 stakeholder rings
  B[15] = (s) => {
    const fun = [['17 lenses', 2.7], ['32 candidates', 2.2], ['24 kept', 1.7]];
    fun.forEach((f, i) => {
      const w = f[1], x = 0.5 + (2.7 - w) / 2, y = 1.55 + i * 0.75;
      L.box(s, x, y, w, 0.58, { fill: i === 2 ? K.indigo : K.indigoTint, r: 0.08 });
      L.txt(s, f[0], x, y, w, 0.58, { fontSize: 15, bold: true, color: i === 2 ? K.white : K.indigo, align: 'center', valign: 'middle' });
      if (i < 2) L.line(s, 1.85, y + 0.58, 1.85, y + 0.75, { color: K.indigo, w: 1.5, arrow: true });
    });
    L.chip(s, 'Seven appeared only after operator practice was seen', 0.5, 3.95, 2.7, 0.8, 'amber', { size: 12, color: K.amberD });
    const cx = 5.3, cy = 3.1;
    L.circ(s, cx, cy, 3.5, K.greyT, { line: K.grey, lw: 1, dash: 'dash' });
    L.circ(s, cx, cy, 2.5, K.tealT, { line: K.teal, lw: 1 });
    L.circ(s, cx, cy, 1.5, K.blueT, { line: K.blue, lw: 1 });
    L.circ(s, cx, cy, 0.62, K.orange);
    L.txt(s, 'Students', cx - 0.5, cy - 0.25, 1.0, 0.5, { fontSize: 10, bold: true, color: K.white, align: 'center', valign: 'middle' });
    L.txt(s, '12', cx - 0.4, cy - 1.7, 0.8, 0.3, { fontSize: 16, bold: true, color: K.grey, align: 'center', fontFace: 'Cambria' });
    L.txt(s, '5', cx - 0.4, cy - 1.2, 0.8, 0.3, { fontSize: 16, bold: true, color: K.teal, align: 'center', fontFace: 'Cambria' });
    L.txt(s, '7', cx - 0.4, cy - 0.78, 0.8, 0.3, { fontSize: 16, bold: true, color: K.blue, align: 'center', fontFace: 'Cambria' });
    const leg = [
      ['Primary, 7', K.blue, 'Students, three operators, site management, serving and kitchen staff'],
      ['Secondary, 5', K.teal, 'Mess Committee, Mess Office, dining services team, Warden, Student Parliament mess seats'],
      ['Indirect, 12', K.grey, 'Academic administration, suppliers, non-student diners, Mess Cell, garbage contractor and more'],
    ];
    leg.forEach((l, i) => {
      const y = 1.5 + i * 1.18;
      L.circ(s, 7.35, y + 0.12, 0.18, l[1]);
      L.txt(s, l[0], 7.55, y, 1.9, 0.25, { fontSize: 13, bold: true, color: l[1] });
      L.txt(s, l[2], 7.55, y + 0.28, 1.95, 0.85, { fontSize: 10.5, color: K.text });
    });
    L.txt(s, 'Five governance identities remain unconfirmed and apart.', 3.4, 4.95, 5.5, 0.25, { fontSize: 11, color: K.muted, italic: true });
  };
  B[16] = (s, d) => { L.decisionCard(s, 4, d); L.tags(s, ['OPEN'], { y: 1.13 }); };
  // ---- 17 authority
  B[17] = (s) => {
    const rows = [
      ['Class timing', 'Academic administration', 'CONFIRMED', 'No link to mess governance', 'MdSchedule'],
      ['Registration cut-off and cancellation limit', 'Mess Office; committee sign-off unclear', 'SINGLE-SOURCED', 'One case, December 2024', 'MdEvent'],
      ['Menu', 'Student committee, from operator options', 'CONFIRMED', 'In outline', 'MdRestaurantMenu'],
      ['Quantity, first batch, reuse', 'The operator', 'CONFIRMED', 'At Yuktāhār', 'MdRestaurant'],
      ['Breakfast timing', 'Unknown', 'OPEN', 'About 37 scans a day at or after 9:30', 'MdAccessTime'],
      ['Food safety', 'Facility team, weekly quality control', 'CONFIRMED', 'Nothing covers quantity', 'MdShield'],
    ];
    rows.forEach((r, i) => {
      const y = 1.4 + i * 0.58;
      L.icon(s, r[4], 0.72, y + 0.25, 0.4, K.indigo);
      L.txt(s, r[0], 1.05, y, 2.6, 0.5, { fontSize: 12, bold: true, valign: 'middle' });
      L.line(s, 3.7, y + 0.25, 3.95, y + 0.25, { color: K.greyM, w: 1.5, arrow: true });
      L.chip(s, r[1], 4.0, y + 0.02, 2.75, 0.46, r[2] === 'OPEN' ? 'red' : 'teal', { size: 11, dash: r[2] === 'OPEN' ? 'dash' : undefined });
      const c = L.tagColors[r[2]];
      L.tags(s, [r[2]], { y: y + 0.03, right: 8.55 + 0.0 });
      L.txt(s, r[3], 8.6, y, 0.95, 0.5, { fontSize: 9.5, color: K.muted, valign: 'middle' });
    });
    L.txt(s, 'Nobody has raised the 8:30 overlap with academic administration.', 0.5, 4.95, 8, 0.25, { fontSize: 12, color: K.muted, italic: true });
  };
  // ---- 18 power vs leverage plot
  B[18] = (s) => {
    const px = 1.0, py = 1.4, pw = 5.4, ph = 3.3;
    L.box(s, px, py, pw / 2, ph / 2, { fill: K.indigoTint, r: 0 });
    L.box(s, px + pw / 2, py, pw / 2, ph / 2, { fill: K.tealT, r: 0 });
    L.box(s, px, py + ph / 2, pw / 2, ph / 2, { fill: K.greyT, r: 0 });
    L.box(s, px + pw / 2, py + ph / 2, pw / 2, ph / 2, { fill: K.orangeT, r: 0 });
    L.txt(s, 'Leverage over breakfast waste', px, py + ph + 0.05, pw, 0.22, { fontSize: 11, bold: true, color: K.muted, align: 'center' });
    L.txt(s, 'low', px, py + ph + 0.05, 0.6, 0.22, { fontSize: 10, color: K.muted });
    L.txt(s, 'high', px + pw - 0.6, py + ph + 0.05, 0.6, 0.22, { fontSize: 10, color: K.muted, align: 'right' });
    s.addText('Power over mess decisions', { x: 0.7 - 1.3, y: py + ph / 2 - 0.11, w: 2.6, h: 0.22, rotate: 270, isTextBox: true, margin: 0, fontSize: 11, bold: true, color: K.muted, align: 'center', valign: 'middle' });
    const pts = [
      ['Academic administration', 0.06, 0.9, K.grey, 'r'], ['Facility team and quality control', 0.07, 0.76, K.teal, 'r'],
      ['Heads of the parent and dining services bodies (unconfirmed)', 0.22, 0.58, K.grey, 'dash'], ['Mess Committee, Warden', 0.28, 0.67, K.teal, 'r'],
      ['Mess Office', 0.62, 0.9, K.teal, 'l'], ['Operator: Yuktāhār', 0.62, 0.7, K.blue, 'r'],
      ['Operator: Kadamba', 0.58, 0.4, K.blue, 'r'], ['Operator: Bakul', 0.56, 0.3, K.blue, 'r'],
      ['Mess Cell', 0.66, 0.06, K.orange, 'r'], ['Students collectively', 0.82, 0.15, K.orange, 'l'],
      ['Students individually', 0.04, 0.08, K.orange, 'r'], ['Outside diners, Kadamba staff', 0.06, 0.32, K.green, 'r'],
    ];
    pts.forEach((p) => {
      const cx = px + p[1] * pw, cy = py + (1 - p[2]) * ph;
      const isOp = p[0].startsWith('Operator: K') || p[0].startsWith('Operator: B');
      if (isOp) L.circ(s, cx, cy, 0.34, null, { line: K.red, lw: 2 });
      L.circ(s, cx, cy, 0.18, p[4] === 'dash' ? null : p[3], p[4] === 'dash' ? { line: p[3], lw: 1.25, dash: 'dash' } : {});
      const left = p[4] === 'l';
      L.txt(s, p[0], left ? cx - 2.15 : cx + 0.15, cy - 0.12, 2.0, 0.26, { fontSize: 10, color: K.text, align: left ? 'right' : 'left', valign: 'middle' });
    });
    L.box(s, 6.75, 1.5, 2.75, 1.1, { fill: K.redT, line: K.red, lw: 1, r: 0.08 });
    L.txt(s, 'Most leverage over waste, least rule-making power: the operators', 6.88, 1.5, 2.5, 1.1, { fontSize: 14, bold: true, color: K.red, valign: 'middle' });
    L.txt(s, 'Information-flow leverage, routing records to the rule owner, belongs to nobody.', 6.75, 2.85, 2.75, 1.0, { fontSize: 14 });
    L.txt(s, 'Placement is ordinal and rests on the team’s judgement.', 6.75, 4.1, 2.75, 0.6, { fontSize: 11, color: K.muted, italic: true });
  };
  B[19] = (s, d) => L.decisionCard(s, 5, d);
  // ---- 20 incentives and fork
  B[20] = (s) => {
    L.txt(s, 'WHAT STUDENTS CAN DO', 0.5, 1.35, 4, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    L.chip(s, 'Skip Meal', 0.5, 1.7, 1.5, 0.55, 'blue', { size: 13, bold: true });
    L.line(s, 2.05, 1.975, 2.55, 1.975, { color: K.indigo, w: 2, arrow: true });
    L.icon(s, 'MdWallet', 2.9, 1.975, 0.5, K.grey);
    L.txt(s, 'Rs 0 back', 3.25, 1.7, 1.3, 0.55, { fontSize: 14, bold: true, color: K.red, valign: 'middle' });
    L.chip(s, 'Mess Cell resale', 0.5, 2.5, 1.5, 0.55, 'orange', { size: 13, bold: true });
    L.line(s, 2.05, 2.775, 2.55, 2.775, { color: K.indigo, w: 2, arrow: true });
    L.icon(s, 'MdWallet', 2.9, 2.775, 0.5, K.green);
    L.txt(s, 'value back', 3.25, 2.5, 1.3, 0.55, { fontSize: 14, bold: true, color: K.green, valign: 'middle' });
    L.card(s, 0.5, 3.4, 4.1, 0.75, 'blue');
    L.txt(s, '0 of those who addressed it used Skip Meal for a refund', 0.65, 3.4, 3.8, 0.75, { fontSize: 13, valign: 'middle' });
    L.card(s, 0.5, 4.3, 4.1, 0.55, 'orange');
    L.txt(s, '4 used Mess Cell', 0.65, 4.3, 3.8, 0.55, { fontSize: 13, valign: 'middle' });
    // fork
    L.txt(s, 'WHAT OPERATORS ARE PAID ON', 5.0, 1.35, 4.5, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    L.box(s, 5.6, 1.65, 3.3, 0.6, { fill: K.indigo, r: 0.3 });
    L.txt(s, 'How are operators paid?', 5.6, 1.65, 3.3, 0.6, { fontSize: 14, bold: true, color: K.white, align: 'center', valign: 'middle' });
    L.line(s, 6.6, 2.25, 6.1, 2.75, { color: K.indigo, w: 1.5, arrow: true });
    L.line(s, 7.9, 2.25, 8.4, 2.75, { color: K.indigo, w: 1.5, arrow: true });
    L.card(s, 5.0, 2.8, 2.15, 1.3, 'red', { dash: 'dash' });
    L.txt(s, 'Registered plates: the operator keeps the margin on every no-show', 5.1, 2.8, 1.95, 1.3, { fontSize: 12, valign: 'middle' });
    L.card(s, 7.35, 2.8, 2.15, 1.3, 'red', { dash: 'dash' });
    L.txt(s, 'Served plates: the operator bears the cost of over-cooking', 7.45, 2.8, 1.95, 1.3, { fontSize: 12, valign: 'middle' });
    L.txt(s, 'A remark by Kadamba’s operator suggests this', 5.0, 4.15, 2.15, 0.5, { fontSize: 10.5, color: K.muted });
    L.txt(s, 'Bakul’s manager says this', 7.35, 4.15, 2.15, 0.5, { fontSize: 10.5, color: K.muted });
    L.txt(s, 'No contract has been seen.', 5.0, 4.7, 4.5, 0.3, { fontSize: 14, bold: true, color: K.red });
    L.tags(s, ['OPEN'], { y: 1.13 });
  };
  // ---- 21 three kitchens
  B[21] = (s) => {
    const cols = [
      { n: 'Kadamba', ic: 'MdStairs', role: 'blue', c: K.blue, rows: ['About 70% of registrations, by gram standard', 'Operator management; a supervisor tops up', 'Top-up in 10 to 15 minutes', 'The count is an obligation', 'Scans and the operator’s account'], tag: 'CONFIRMED' },
      { n: 'Yuktāhār', ic: 'MdMenuBook', role: 'teal', c: K.teal, rows: ['No fixed ratio: the matching day in the Wastage Book', 'Storekeeper, coordinator and staff meet daily', 'First half hour projected; re-cook on early run-out', 'Waste is a cost to cut', 'Seen on site; books photographed'], tag: 'CONFIRMED' },
      { n: 'Bakul', ic: 'MdLocalShipping', role: 'orange', c: K.orange, rows: ['70 to 80% by item, reset weekly, floor about 70%', 'The manager alone; cooked about 8 km away', 'Phone call, cook, then a 20 to 40 minute drive', 'A shortage is the failure to avoid', 'The manager’s account; no records'], tag: 'SINGLE-SOURCED' },
    ];
    const labs = ['FIRST BATCH', 'WHO DECIDES', 'CORRECTION IN SERVICE', 'STANCE', 'EVIDENCE'];
    cols.forEach((c, i) => {
      const x = 0.5 + i * 3.05, w = 2.9;
      L.card(s, x, 1.35, w, 3.78, c.role);
      L.icon(s, c.ic, x + 0.4, 1.78, 0.5, c.c);
      L.txt(s, c.n, x + 0.8, 1.45, 1.9, 0.65, { fontSize: 18, bold: true, fontFace: 'Cambria', valign: 'middle' });
      c.rows.forEach((r, k) => {
        const y = 2.12 + k * 0.58;
        L.txt(s, labs[k], x + 0.18, y, w - 0.3, 0.16, { fontSize: 8.5, bold: true, color: c.c, charSpacing: 1 });
        L.txt(s, r, x + 0.18, y + 0.15, w - 0.3, 0.42, { fontSize: 11 });
      });
    });
  };
  // ---- 22 two lanes
  B[22] = (s) => {
    L.txt(s, 'YUKTĀHĀR: A BOOK THAT FEEDS THE NEXT PLAN', 0.5, 1.33, 6, 0.2, { fontSize: 10, bold: true, color: K.teal, charSpacing: 1 });
    const y1 = [['Daily meeting', 'blue'], ['Cook', 'blue'], ['Serve', 'blue'], ['Wastage Book', 'purple']];
    y1.forEach((c, i) => { const x = 0.5 + i * 1.5; L.chip(s, c[0], x, 1.62, 1.28, 0.55, c[1], { size: 12, bold: true }); if (i < 3) L.line(s, x + 1.28, 1.895, x + 1.5, 1.895, { color: K.indigo, w: 1.5, arrow: true }); });
    L.line(s, 5.14, 2.17, 5.14, 2.5, { color: K.purple, w: 2 });
    L.line(s, 5.14, 2.5, 1.14, 2.5, { color: K.purple, w: 2 });
    L.line(s, 1.14, 2.5, 1.14, 2.19, { color: K.purple, w: 2, arrow: true });
    L.txt(s, 'sizes the matching dish about two weeks ahead', 1.4, 2.54, 3.6, 0.25, { fontSize: 11, color: K.purple, bold: true });
    s.addImage({ path: path.join(WORK, 'kitchen_reg.png'), x: 7.7, y: 1.35, w: 1.8, h: 1.8 * 800 / 1440, altText: 'Yuktāhār registers laid out beside the stock' });
    L.txt(s, 'KADAMBA: A DAY THAT ENDS AT THE BIN', 0.5, 3.02, 6, 0.2, { fontSize: 10, bold: true, color: K.blue, charSpacing: 1 });
    L.chip(s, 'Cooking temperature, 72-hour sample, tasting with the facility team', 0.5, 3.3, 5.4, 0.36, 'teal', { size: 11 });
    const k = [['First batch cooked early', 'blue'], ['About 30 portions to outside diners', 'green'], ['Supervisor top-up', 'blue'], ['Service', 'blue'], ['Late door after 9:30', 'blue'], ['The bin', 'red']];
    k.forEach((c, i) => { const x = 0.5 + i * 1.5; L.chip(s, c[0], x, 3.78, 1.32, 0.62, c[1], { size: 11 }); if (i < 5) L.line(s, x + 1.32, 4.09, x + 1.5, 4.09, { color: K.indigo, w: 1.25, arrow: true }); });
    L.link(s, 8.8, 4.72, 1.2, 'broken', { label: 'no record carries the day’s outcome forward' });
    L.txt(s, 'All of Kadamba’s checks come before any sign of turnout.', 6.0, 3.32, 3.5, 0.34, { fontSize: 11, color: K.muted, italic: true });
  };
  B[23] = (s, d) => L.decisionCard(s, 6, d);
  // ---- 24 hero doughnut (dark)
  B[24] = (s) => {
    s.addChart(pres.charts.DOUGHNUT, [{ name: 'April', labels: ['Scanned', 'Not scanned'], values: [37.1, 62.9] }], {
      x: 0.5, y: 1.3, w: 3.9, h: 3.7, holeSize: 66, chartColors: [K.green, K.red], showLegend: false, showValue: false, showPercent: false, showLabel: false, showTitle: false, dataBorder: { pt: 1, color: K.ink },
    });
    L.big(s, '62.9%', 1.35, 2.55, 2.2, 0.8, { color: K.white, size: 40, align: 'center' });
    L.txt(s, 'never scanned', 1.35, 3.3, 2.2, 0.3, { fontSize: 14, color: K.onDark2, align: 'center' });
    const st = [['32,162', 'registrations'], ['11,941', 'scans'], ['20,221', 'billed and not eaten']];
    st.forEach((t, i) => {
      const y = 1.6 + i * 1.05;
      L.big(s, t[0], 5.0, y, 2.6, 0.7, { color: i === 2 ? K.red : K.white, size: 40 });
      L.txt(s, t[1], 7.6, y, 2.0, 0.7, { fontSize: 16, color: K.onDark2, valign: 'middle' });
    });
    L.txt(s, 'Kadamba, 1 to 30 April 2026', 5.0, 4.8, 4.5, 0.25, { fontSize: 12, color: K.onDark2 });
    L.tags(s, ['CONFIRMED'], { y: 1.2 });
  };
  // ---- 25 weekday chart
  B[25] = (s) => {
    const cats = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
    s.addChart(pres.charts.BAR, [{ name: 'Percent eaten', labels: cats, values: [41.1, 42.1, 37.0, 39.5, 37.5, 34.8, 27.3] }], {
      x: 0.5, y: 1.4, w: 6.1, h: 3.5, barDir: 'col', chartColors: [K.blue, K.blue, K.blue, K.blue, K.blue, K.greyM, K.red], showLegend: false, showTitle: false,
      showValue: true, dataLabelFontSize: 12, dataLabelFontFace: '+mn-lt', dataLabelColor: K.text, dataLabelPosition: 'outEnd', dataLabelFormatCode: '0.0',
      valAxisMinVal: 0, valAxisMaxVal: 50, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, catAxisLabelFontSize: 12, catAxisLabelFontFace: '+mn-lt', catAxisLabelColor: K.text, barGapWidthPct: 40,
    });
    L.txt(s, 'Share of registrations eaten, April 2026', 0.5, 4.92, 4, 0.22, { fontSize: 10, color: K.muted });
    L.card(s, 6.9, 1.45, 2.6, 1.0, 'blue');
    L.txt(s, 'Registrations stay flat: about 1,070 a day, Sundays included', 7.0, 1.45, 2.4, 1.0, { fontSize: 12, valign: 'middle' });
    L.chip(s, 'Weekdays 39.3%', 6.9, 2.65, 1.25, 0.5, 'blue', { size: 12, bold: true });
    L.chip(s, 'Weekends 31.1%', 8.25, 2.65, 1.25, 0.5, 'red', { size: 12, bold: true });
    L.txt(s, 'The three lowest days of the month were all Sundays.', 6.9, 3.5, 2.6, 0.8, { fontSize: 14 });
    L.tags(s, ['CONFIRMED'], { y: 1.13 });
  };
  // ---- 26 arrivals (native chart)
  B[26] = (s) => {
    const labs = ['7:00', '7:15', '7:30', '7:45', '8:00', '8:15', '8:30', '8:45', '9:00', '9:15', '9:30', '9:45'];
    const vals = [1.3, 1.3, 9.6, 5.7, 7.3, 8.3, 8.2, 8.9, 13.5, 26.5, 9.1, 0.1];
    const cols = vals.map((v, i) => (i === 9 ? K.red : i === 10 ? K.amber : K.blue));
    s.addChart(pres.charts.BAR, [{ name: 'Share of scans', labels: labs, values: vals }], {
      x: 0.5, y: 1.4, w: 5.9, h: 3.5, barDir: 'col', chartColors: cols, showLegend: false, showTitle: false, showValue: true, dataLabelFontSize: 10, dataLabelFontFace: '+mn-lt', dataLabelColor: K.text,
      dataLabelPosition: 'outEnd', dataLabelFormatCode: '0.0', valAxisMinVal: 0, valAxisMaxVal: 30, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' },
      catAxisLabelFontSize: 10, catAxisLabelFontFace: '+mn-lt', catAxisLabelColor: K.text, barGapWidthPct: 30,
    });
    L.txt(s, 'Share of all 11,941 scans in each fifteen-minute slot, April 2026', 0.5, 4.92, 5.9, 0.22, { fontSize: 10, color: K.muted });
    L.big(s, '26.5%', 6.7, 1.4, 2.8, 0.9, { size: 56, color: K.red });
    L.txt(s, 'of scans between 9:15 and 9:29', 6.7, 2.3, 2.8, 0.5, { fontSize: 14 });
    L.txt(s, 'About 9 a minute at 9:29. 9.2% after 9:30.', 6.7, 2.9, 2.8, 0.6, { fontSize: 13, color: K.muted });
    L.card(s, 6.7, 3.65, 2.8, 1.05, 'amber');
    L.txt(s, 'The operator reckons about 150 in the last ten minutes; the records show about 79', 6.8, 3.65, 2.6, 1.05, { fontSize: 11.5, valign: 'middle', color: K.text });
    L.tags(s, ['CONFIRMED'], { y: 1.13 });
    L.txt(s, 'Kitchens start two hours before the first student arrives.', 6.7, 4.8, 2.8, 0.4, { fontSize: 10.5, color: K.muted, italic: true });
  };
  // ---- 27 lunch control
  B[27] = (s) => {
    const x0 = 2.8, sc = 0.066; // 0..100 -> 6.6 in
    const X = (v) => x0 + v * sc;
    [0, 25, 50, 75, 100].forEach((v) => { L.line(s, X(v), 1.75, X(v), 3.95, { color: 'DDDDDD', w: 0.75 }); L.txt(s, v + '%', X(v) - 0.3, 3.98, 0.6, 0.2, { fontSize: 10, color: K.muted, align: 'center' }); });
    L.txt(s, 'Breakfast, 1 to 20 September', 0.5, 2.15, 2.2, 0.5, { fontSize: 13, bold: true, valign: 'middle' });
    L.box(s, X(17.7), 2.2, X(40.2) - X(17.7), 0.5, { fill: K.red, r: 0.05 });
    L.circ(s, X(28), 2.45, 0.32, K.white, { line: K.red, lw: 2 });
    L.txt(s, 'range 17.7 to 40.2, mean about 28', X(17.7), 2.74, 3.2, 0.25, { fontSize: 12, color: K.red, bold: true });
    L.txt(s, 'Lunch', 0.5, 3.0, 2.2, 0.5, { fontSize: 13, bold: true, valign: 'middle' });
    L.box(s, X(56), 3.05, X(89) - X(56), 0.5, { fill: K.green, r: 0.05 });
    L.txt(s, 'range 56 to 89', X(56), 3.59, 3.2, 0.25, { fontSize: 12, color: K.green, bold: true });
    L.line(s, X(50), 1.6, X(50), 3.95, { color: K.amber, w: 2.5, dash: 'dash' });
    L.txt(s, 'the site head’s belief about breakfast: about 50', X(50) - 1.6, 1.38, 3.2, 0.22, { fontSize: 11, bold: true, color: K.amberD, align: 'center' });
    L.txt(s, 'The site head believed about 50 per cent; his own register says about 28.', 0.5, 4.5, 8.5, 0.35, { fontSize: 16, bold: true });
    L.tags(s, ['CONFIRMED'], { y: 1.13 });
  };
  // ---- 28 first batch vs eaten
  B[28] = (s) => {
    s.addChart(pres.charts.BAR, [{ name: 'Portions a day', labels: ['First batch, about 70% of roughly 1,070', 'Eaten a day'], values: [750, 398] }], {
      x: 0.5, y: 1.35, w: 4.6, h: 2.35, barDir: 'bar', chartColors: [K.red, K.green], showLegend: false, showTitle: false, showValue: true, dataLabelFontSize: 14, dataLabelFontFace: '+mn-lt', dataLabelColor: K.text, dataLabelPosition: 'outEnd',
      valAxisMinVal: 0, valAxisMaxVal: 900, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, catAxisLabelFontSize: 11, catAxisLabelFontFace: '+mn-lt', catAxisLabelColor: K.text, catAxisOrientation: 'maxMin', barGapWidthPct: 45,
    });
    L.chip(s, 'about 3 times what is eaten on a Sunday', 5.4, 1.55, 4.1, 0.55, 'red', { size: 13, bold: true });
    L.card(s, 5.4, 2.3, 4.1, 1.1, 'amber');
    L.icon(s, 'MdWarning', 5.8, 2.85, 0.45, K.amber);
    L.txt(s, 'Idli, puri and bhatura gone by about 9:20', 6.2, 2.3, 3.2, 1.1, { fontSize: 14, valign: 'middle' });
    // timeline strip
    L.txt(s, 'WHAT IS FIXED, AND WHEN', 0.5, 3.8, 4, 0.2, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    L.line(s, 0.7, 4.25, 9.3, 4.25, { color: K.indigo, w: 2 });
    const m = [['About 2 weeks ahead', 'Yuktāhār sizes the dish', 0.9], ['4 days ahead', 'Cancellation closes', 3.0], ['Day before', 'Count closed and converted', 5.1], ['7:30', 'First batch fixed; signals arrive after', 7.2]];
    m.forEach((t) => {
      L.circ(s, t[2] + 0.2, 4.25, 0.18, K.indigo);
      L.txt(s, t[0], t[2] - 0.5, 4.38, 2.0, 0.22, { fontSize: 11, bold: true, color: K.indigo });
      L.txt(s, t[1], t[2] - 0.5, 4.6, 2.0, 0.4, { fontSize: 10.5, color: K.muted });
    });
    L.tags(s, ['CONFIRMED'], { y: 1.13 });
    L.txt(s, 'Only Yuktāhār turns the first half hour into a forecast.', 0.5, 5.02, 6, 0.2, { fontSize: 10, color: K.muted, italic: true });
  };
  // ---- 29 before and after
  B[29] = (s) => {
    const pairs = [
      ['30% unused', '62.9% and about 72%'], ['One passive vendor', 'Three operators, three regimes'], ['A four-day lock is the bottleneck', 'The cooked first batch is'], ['Composting absorbs surplus', 'Outside diners, staff, reheating, the bin'],
      ['Bakul cooks near the airport', 'Bakul’s kitchen is about 8 km away'], ['Six loops close', 'Three close under a strict rule'], ['Cuisine explains low uptake', 'Vegetarian 32.4%, non-vegetarian 48.5%'], ['Friends pull each other in', 'Dropped: six respondents disconfirmed it'],
    ];
    pairs.forEach((p, i) => {
      const x = 0.5 + (i % 4) * 2.28, y = 1.4 + Math.floor(i / 4) * 1.7;
      L.card(s, x, y, 2.18, 1.55, 'indigo');
      L.txt(s, 'WAS', x + 0.14, y + 0.1, 1.0, 0.16, { fontSize: 8.5, bold: true, color: K.muted, charSpacing: 2 });
      L.txt(s, p[0], x + 0.14, y + 0.28, 1.9, 0.5, { fontSize: 12, color: K.muted, strike: 'sngStrike' });
      L.line(s, x + 0.14, y + 0.82, x + 2.04, y + 0.82, { color: K.greyM, w: 0.75 });
      L.txt(s, 'NOW', x + 0.14, y + 0.88, 1.0, 0.16, { fontSize: 8.5, bold: true, color: K.green, charSpacing: 2 });
      L.txt(s, p[1], x + 0.14, y + 1.04, 1.9, 0.5, { fontSize: 12, bold: true });
    });
    L.txt(s, 'Records trusted over recall.', 0.5, 4.88, 6, 0.25, { fontSize: 12, color: K.muted, italic: true });
  };
  // ---- 30 nine findings
  B[30] = (s) => {
    const f = [
      ['Registration is a default, not demand', 'MdHowToReg', 'blue'], ['Each kitchen’s guess is too high', 'MdRestaurant', 'blue'], ['The gap is measured twice and reaches no rule owner', 'MdLinkOff', 'red'],
      ['The cooked first batch is the constraint', 'MdLock', 'red'], ['Shortage and waste share one morning', 'MdAccessTime', 'amber'], ['Class timing has no link to mess governance', 'MdSchedule', 'teal'],
      ['Oversight changes kitchens, not rules', 'MdGavel', 'teal'], ['Surplus is absorbed out of sight, partly by real people', 'MdGroups', 'green'], ['The most requested fix was a longer close', 'MdMoreTime', 'orange'],
    ];
    f.forEach((t, i) => {
      const x = 0.5 + (i % 3) * 3.05, y = 1.4 + Math.floor(i / 3) * 0.98;
      L.tile(s, x, y, 2.9, 0.88, t[2], i + 1, t[0], { size: 12 });
    });
    L.chip(s, 'Not observed: disposal after the close', 0.5, 4.42, 4.4, 0.4, 'grey', { dash: 'dash', size: 12 });
    L.chip(s, 'Not measured: semester-level trends', 5.1, 4.42, 4.4, 0.4, 'grey', { dash: 'dash', size: 12 });
    L.txt(s, 'Next: why the gap holds.', 0.5, 4.95, 4, 0.25, { fontSize: 12, color: K.muted, italic: true });
  };
};
