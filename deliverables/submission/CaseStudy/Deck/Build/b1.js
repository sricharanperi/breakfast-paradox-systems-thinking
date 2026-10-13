// Slides 1 to 11: opening, background, approach
const path = require('path');
module.exports = (B, { L, K, FIGS }) => {
  // ---- 1 title
  B[1] = (s) => {
    L.plate(s, 7.8, 3.0, 4.7, { eaten: 37.1, ring: K.onDark2, lw: 3 });
    L.txt(s, 'Why most registered breakfasts go uneaten in the hostel dining halls of IIIT Hyderabad', 0.5, 2.95, 4.4, 0.9, { fontSize: 18, color: K.onDark2 });
    L.txt(s, 'Team Invictus: Sricharan Peri, Prathyusha Kalluri, Neha Susan Manoj', 0.5, 4.0, 4.4, 0.45, { fontSize: 12, color: K.white });
    L.txt(s, 'Systems Thinking and Design PD2.405, Prof. Raman Saxena. September to October 2026', 0.5, 4.55, 4.4, 0.45, { fontSize: 12, color: K.onDark2 });
  };
  // ---- 2 hero: three plates
  B[2] = (s) => {
    const cols = [1.9, 5.0, 8.1];
    L.plate(s, cols[0], 2.45, 1.9, { eaten: 37.1, base: K.red, wedge: K.green, ring: K.onDark2, lw: 2 });
    L.plate(s, cols[1], 2.45, 1.9, { eaten: 28, base: K.red, wedge: K.green, ring: K.onDark2, lw: 2 });
    L.plate(s, cols[2], 2.45, 1.9, { eaten: 56, base: K.greyM, wedge: K.green, band: 89, ring: K.onDark2, lw: 2 });
    L.big(s, '62.9%', cols[0] - 1.4, 3.5, 2.8, 0.8, { color: K.white, size: 40, align: 'center' });
    L.big(s, 'about 72%', cols[1] - 1.4, 3.5, 2.8, 0.8, { color: K.white, size: 40, align: 'center' });
    L.big(s, '56 to 89%', cols[2] - 1.4, 3.5, 2.8, 0.8, { color: K.white, size: 40, align: 'center' });
    ['Kadamba, April 2026, not eaten', 'Yuktāhār, September, not eaten', 'Yuktāhār lunch, eaten'].forEach((t, i) => L.txt(s, t, cols[i] - 1.4, 4.3, 2.8, 0.3, { fontSize: 14, color: K.onDark2, align: 'center' }));
    L.txt(s, 'Green: eaten.  Red: registered and not eaten.', 0.5, 4.8, 5, 0.25, { fontSize: 11, color: K.onDark2 });
    L.tags(s, ['CONFIRMED'], { y: 1.2 });
  };
  // ---- 3 three moves
  B[3] = (s) => {
    const cards = [
      ['teal', 'MdAltRoute', 'Build the missing route', 'Send the records that already exist to the people who set the rules'],
      ['blue', 'MdEvent', 'Open a Sunday skip that removes the charge', 'The one move that lowers what students pay'],
      ['amber', 'MdBalance', 'Calibrate the kitchen’s first batch', 'Buys time and saves food'],
    ];
    cards.forEach((c, i) => {
      const x = 0.5 + i * 3.05;
      L.card(s, x, 1.5, 2.9, 2.55, c[0]);
      L.icon(s, c[1], x + 0.5, 2.05, 0.6, { teal: K.teal, blue: K.blue, amber: K.amber }[c[0]]);
      L.txt(s, c[2], x + 0.2, 2.5, 2.5, 0.7, { fontSize: 16, bold: true });
      L.txt(s, c[3], x + 0.2, 3.25, 2.5, 0.7, { fontSize: 13, color: K.muted });
    });
    L.chip(s, 'QUICK FIX', 7.95, 1.62, 1.3, 0.26, 'amber', { size: 10, bold: true, color: K.amberD });
    L.tags(s, ['PROJECTED'], { y: 4.28, right: 2.4 });
    L.txt(s, 'Replayed on April records: surplus 362 to 91 portions a day', 2.55, 4.26, 6.2, 0.26, { fontSize: 14, bold: true, valign: 'middle' });
    L.txt(s, 'Only the rule change lowers what students pay.', 0.5, 4.7, 8, 0.3, { fontSize: 14, color: K.muted });
  };
  // ---- 4 rules of the system
  B[4] = (s) => {
    const cx = 3.2, cy = 3.0;
    L.plate(s, cx, cy, 1.0, { eaten: 37.1, ring: K.onDark2, lw: 2 });
    const chips = [
      ['Registered for every meal, holidays included', 1.85, 1.45, 2.7],
      ['Charge follows the registration', 4.3, 2.15, 2.3],
      ['Exit: five cancellations a month, four days ahead', 4.3, 3.2, 2.3],
      ['Skip Meal: still charged', 0.5, 3.2, 2.3],
      ['Walk-in pays about 70% more', 0.5, 2.15, 2.3],
    ];
    chips.forEach((c) => {
      const [x, y, w] = [c[1], c[2], c[3]];
      L.line(s, cx, cy, x + w / 2, y + 0.3, { color: K.darkLine, w: 1 });
    });
    L.circ(s, cx, cy, 1.0, K.ink);
    L.plate(s, cx, cy, 1.0, { eaten: 37.1, ring: K.onDark2, lw: 2 });
    chips.forEach((c) => L.chip(s, c[0], c[1], c[2], c[3], 0.55, 'blue', { size: 12 }));
    // class clock
    L.txt(s, 'The breakfast window', 0.5, 4.1, 3, 0.22, { fontSize: 11, color: K.onDark2 });
    L.box(s, 0.5, 4.38, 5.9, 0.16, { fill: K.blue, r: 0.04 });
    const x830 = 0.5 + 5.9 / 2;
    L.line(s, x830, 4.28, x830, 4.64, { color: K.amber, w: 2.5 });
    L.txt(s, '7:30', 0.5, 4.6, 0.8, 0.22, { fontSize: 11, color: K.onDark2 });
    L.txt(s, '8:30 class starts', x830 - 0.7, 4.66, 1.4, 0.22, { fontSize: 11, color: K.amber, bold: true, align: 'center' });
    L.txt(s, '9:30 doors close', 5.0, 4.6, 1.4, 0.22, { fontSize: 11, color: K.onDark2, align: 'right' });
    // portal inset
    L.txt(s, 'Four halls: Kadamba, Palash, Bakul, Yuktāhār.', 6.7, 1.45, 2.8, 0.45, { fontSize: 14, color: K.white });
    s.addImage({ path: path.join(FIGS, 'Figure_2_portal.png'), x: 6.7, y: 2.05, w: 2.8, h: 2.8 * 280 / 702 * 1.0, altText: 'Portal registration dialog with the Skip Meal text' });
    L.box(s, 6.7, 2.05 + 2.8 * 280 / 702 * 0.62, 2.8, 0.34, { line: K.amber, lw: 2, r: 0.04 });
    L.txt(s, 'The portal states it in plain words', 6.7, 3.4, 2.8, 0.5, { fontSize: 12, color: K.amber });
  };
  // ---- 5 restating the problem
  B[5] = (s) => {
    L.box(s, 0.5, 1.4, 4.3, 3.45, { fill: K.greyT, r: 0.08 });
    L.txt(s, 'THE BRIEF’S STORY', 0.7, 1.5, 3.9, 0.22, { fontSize: 10, bold: true, color: K.muted, charSpacing: 2 });
    const chain = [['MdAlarm', 'Alarm at 7:45'], ['MdBedtime', 'Sleep'], ['MdFastfood', 'No breakfast'], ['MdSchedule', 'Hungry at 11:15'], ['MdDelete', 'Food thrown away']];
    chain.forEach((c, i) => {
      const y = 1.9 + i * 0.58;
      L.icon(s, c[0], 1.0, y + 0.2, 0.38, K.grey);
      L.txt(s, c[1], 1.3, y, 1.6, 0.4, { fontSize: 13, valign: 'middle' });
    });
    L.icon(s, 'MdCheckCircle', 3.2, 2.2, 0.34, K.green);
    L.txt(s, 'Late nights lead to missed mornings: confirmed in interviews', 3.5, 1.95, 1.2, 0.95, { fontSize: 10, color: K.green });
    L.icon(s, 'MdHelp', 3.2, 3.5, 0.34, K.greyM);
    L.txt(s, 'Not yet shown: food wasted, costly, the clock is the reason', 3.5, 3.15, 1.2, 1.1, { fontSize: 10, color: K.muted });
    L.line(s, 5.0, 3.1, 5.3, 3.1, { color: K.indigo, w: 2.5, arrow: true });
    const rest = [
      ['Registration misses who eats by about two thirds', 'MdHowToReg'],
      ['Each kitchen applies its own conversion', 'MdRestaurant'],
      ['The records that could fix it reach no rule setter', 'MdLinkOff'],
    ];
    rest.forEach((r, i) => {
      const y = 1.4 + i * 1.12;
      L.card(s, 5.5, y, 4.0, 1.0, 'red');
      L.circ(s, 5.85, y + 0.5, 0.4, K.red);
      L.txt(s, String(i + 1), 5.65, y, 0.4, 1.0, { fontSize: 15, bold: true, color: K.white, align: 'center', valign: 'middle' });
      L.txt(s, r[0], 6.2, y + 0.08, 3.15, 0.9, { fontSize: 14, valign: 'middle' });
    });
    L.txt(s, 'The question moved from why students skip to why the arrangement persists.', 5.5, 4.8, 4.0, 0.4, { fontSize: 12, color: K.muted, italic: true });
  };
  B[6] = (s, d) => L.decisionCard(s, 1, d);
  // ---- 7 plan and timeline (dark)
  B[7] = (s) => {
    const ph = [['Phase 1', 'Describe'], ['Phase 2', 'Model'], ['Phase 3', 'Leverage'], ['Phase 4', 'Design']];
    const wAct = [5, 3, 1, 1];
    const x0 = 0.5, total = 9.0, per = total / 10;
    let a = 0;
    const actX = [];
    ph.forEach((p, i) => {
      const x = x0 + a * per, w = wAct[i] * per - 0.08;
      L.box(s, x, 1.42, w, 0.62, { fill: K.indigoTint, r: 0.06 });
      L.txt(s, (wAct[i] > 2 ? `${p[0]}  ${p[1]}` : `${p[0]}\n${p[1]}`), x + 0.04, 1.42, w - 0.08, 0.62, { fontSize: 11, bold: true, color: K.indigo, valign: 'middle', align: 'center' });
      for (let k = 0; k < wAct[i]; k++) { actX.push(x0 + (a + k) * per + per / 2 - 0.04); }
      a += wAct[i];
    });
    actX.forEach((cx, i) => {
      L.circ(s, cx, 2.38, 0.34, K.blue);
      L.txt(s, String(i + 1), cx - 0.17, 2.21, 0.34, 0.34, { fontSize: 12, bold: true, color: K.white, align: 'center', valign: 'middle' });
    });
    L.txt(s, 'Activities', 0.5, 2.62, 1.2, 0.2, { fontSize: 10, color: K.onDark2 });
    const objActs = [[1], [2], [3], [4], [5], [6], [7, 8], [9], [10]];
    objActs.forEach((as, i) => {
      const xa = actX[as[0] - 1], xb = actX[as[as.length - 1] - 1];
      L.box(s, xa - 0.17, 2.85, xb - xa + 0.34, 0.3, { fill: K.purple, r: 0.15 });
      L.txt(s, String(i + 1), xa - 0.17, 2.85, xb - xa + 0.34, 0.3, { fontSize: 11, bold: true, color: K.white, align: 'center', valign: 'middle' });
    });
    L.txt(s, 'Objectives', 0.5, 3.2, 1.2, 0.2, { fontSize: 10, color: K.onDark2 });
    // timeline
    const tx = (day) => 0.9 + day * 8.2 / 37;
    L.line(s, 0.9, 4.65, 9.1, 4.65, { color: K.onDark2, w: 1.25 });
    [['3 Sep', 0], ['14 Sep', 11], ['26 Sep', 23], ['28 Sep', 25], ['Early Oct', 36]].forEach((t) => {
      L.txt(s, t[0], tx(t[1]) - 0.4, 4.72, 0.8, 0.2, { fontSize: 10, color: K.onDark2, align: 'center' });
    });
    L.box(s, tx(0), 3.55, tx(11) - tx(0), 0.26, { fill: K.blue, r: 0.05 });
    L.txt(s, 'First drafts of phases 1 and 2', tx(0) + 0.08, 3.55, 2.6, 0.26, { fontSize: 10, color: K.white, valign: 'middle' });
    [23, 24, 25].forEach((dd) => L.circ(s, tx(dd), 3.98, 0.17, K.amber));
    L.txt(s, 'Field evidence: 26, 27 and 28 September', tx(25) + 0.2, 3.86, 3.1, 0.24, { fontSize: 10, color: K.amber, bold: true, valign: 'middle' });
    L.box(s, tx(24), 4.2, tx(25) - tx(24), 0.22, { fill: K.red, r: 0.04 });
    L.txt(s, 'Three revision passes through every earlier activity', tx(25) + 0.2, 4.19, 3.5, 0.24, { fontSize: 10, color: K.white, valign: 'middle' });
    L.box(s, tx(25), 4.48, tx(36) - tx(25), 0.14, { fill: K.teal, r: 0.04 });
    L.txt(s, 'Phases 3 and 4 written on the revised evidence', 5.7, 4.97 - 0.02, 3.7, 0.22, { fontSize: 10, color: K.onDark2, align: 'right' });
    L.txt(s, 'Four phases, ten activities, fifteen deliverables, nine objectives', 0.5, 4.95, 5, 0.22, { fontSize: 11, color: K.onDark2 });
  };
  // ---- 8 evidence wall
  B[8] = (s) => {
    const tiles = [
      ['6', 'student voices', 'orange', 'MdSchool'], ['1', 'head of facilities, with a kitchen walkthrough', 'teal', 'MdAccountBalance'], ['3', 'kitchens visited in one day', 'blue', 'MdRestaurant'],
      ['22', 'tables from 26 photographed register pages', 'purple', 'MdMenuBook'], ['32,162', 'Kadamba registrations with scan times', 'purple', 'MdQrCodeScanner'], ['9', 'portal screens', 'blue', 'MdHowToReg'],
    ];
    tiles.forEach((t, i) => {
      const x = 0.5 + (i % 3) * 3.05, y = 1.4 + Math.floor(i / 3) * 1.3;
      L.card(s, x, y, 2.9, 1.18, t[2]);
      L.big(s, t[0], x + 0.15, y + 0.05, 1.3, 0.7, { size: t[0].length > 4 ? 28 : 40, color: { orange: K.orange, teal: K.teal, blue: K.blue, purple: K.purple }[t[2]] });
      L.txt(s, t[1], x + 0.15, y + 0.72, 2.6, 0.42, { fontSize: 12 });
      L.icon(s, t[3], x + 2.4, y + 0.38, 0.4, { orange: K.orange, teal: K.teal, blue: K.blue, purple: K.purple }[t[2]]);
    });
    const halls = [['Kadamba', 'scan records', 'green', null], ['Yuktāhār', 'registers', 'green', null], ['Bakul', 'interview only', 'grey', null], ['Palash', 'candidate, shares Bakul’s off-site kitchen, unconfirmed', 'grey', 'dash']];
    halls.forEach((h, i) => {
      const x = 0.5 + i * 2.28;
      L.chip(s, `${h[0]}: ${h[1]}`, x, 4.1, 2.18, h[0] === 'Palash' ? 0.7 : 0.5, h[2], { size: 12, dash: h[3] });
    });
    L.txt(s, 'Sampling followed access, not chance.', 0.5, 4.95, 5, 0.22, { fontSize: 12, color: K.muted, italic: true });
  };
  B[9] = (s, d) => L.decisionCard(s, 2, d);
  // ---- 10 evidence labels
  B[10] = (s) => {
    const labs = [
      ['CONFIRMED', 'green', 'read off a record, seen on site, or stated alike by independent sources'],
      ['SINGLE-SOURCED', 'grey', 'one person or document, not checked'],
      ['CANDIDATE', 'amber', 'an inference combining sources'],
      ['ASSUMED', 'amber', 'a judgement made to go on'],
      ['PROJECTED', 'indigo', 'arithmetic on real records'],
      ['REASONED', 'purple', 'the team’s expectation of how a group would respond, never their feedback'],
      ['PLANNED', 'teal', 'designed and not carried out'],
    ];
    labs.forEach((l, i) => {
      const row = i < 4 ? 0 : 1, col = i < 4 ? i : i - 4;
      const w = row === 0 ? 2.15 : 2.9;
      const x = 0.5 + col * (w + 0.13), y = 1.45 + row * 1.2;
      const [c] = { green: [K.green], grey: [K.grey], amber: [K.amber], indigo: [K.indigo], purple: [K.purple], teal: [K.teal] }[l[1]];
      L.box(s, x, y, w, 0.3, { fill: l[1] === 'amber' ? K.amberT : c, line: c, r: 0.06 });
      L.txt(s, l[0], x, y, w, 0.3, { fontSize: 11, bold: true, color: l[1] === 'amber' ? K.amberD : K.white, align: 'center', valign: 'middle', charSpacing: 1 });
      L.txt(s, l[2], x, y + 0.36, w, 0.7, { fontSize: 12, color: K.text });
    });
    // two tiny loops
    const y0 = 3.95;
    L.txt(s, 'Loops are drawn closed only when every link is evidenced', 0.5, 3.68, 5.2, 0.22, { fontSize: 12, bold: true });
    const tri = [[1.0, y0 + 0.55], [1.9, y0 + 0.55], [1.45, y0 + 0.05]];
    L.line(s, tri[0][0], tri[0][1], tri[1][0], tri[1][1], { color: K.green, w: 2, arrow: true });
    L.line(s, tri[1][0], tri[1][1], tri[2][0], tri[2][1], { color: K.green, w: 2, arrow: true });
    L.line(s, tri[2][0], tri[2][1], tri[0][0], tri[0][1], { color: K.green, w: 2, arrow: true });
    tri.forEach((p) => L.circ(s, p[0], p[1], 0.16, K.green));
    L.txt(s, 'every link evidenced', 2.1, y0 + 0.2, 1.4, 0.4, { fontSize: 11, color: K.green });
    const ch = [[3.9, y0 + 0.55], [4.6, y0 + 0.25], [5.3, y0 + 0.55]];
    L.line(s, ch[0][0], ch[0][1], ch[1][0], ch[1][1], { color: K.amber, w: 2, arrow: true });
    L.line(s, ch[1][0], ch[1][1], ch[2][0], ch[2][1], { color: K.amber, w: 2, arrow: true });
    L.line(s, ch[2][0], ch[2][1] + 0.12, ch[0][0], ch[0][1] + 0.12, { color: K.amber, w: 2, dash: 'dash', arrow: true });
    ch.forEach((p) => L.circ(s, p[0], p[1], 0.16, K.amber));
    L.txt(s, 'inferred link: dashed', 5.5, y0 + 0.3, 1.5, 0.4, { fontSize: 11, color: K.amberD });
    L.chip(s, 'Scenario replay: 23 days, 8 to 30 April, forecasting from earlier days of the same weekday', 6.9, y0 - 0.05, 2.6, 0.95, 'indigo', { size: 12 });
    L.txt(s, 'These labels appear as tags on later slides.', 0.5, 4.95, 5, 0.22, { fontSize: 12, color: K.muted, italic: true });
  };
  B[11] = (s, d) => L.decisionCard(s, 3, d);
};
