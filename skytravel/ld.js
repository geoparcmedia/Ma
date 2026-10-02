const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage(); const errs=[]; p.on('pageerror', e => errs.push(e.message));
 for (const id of process.argv.slice(2)) { await p.goto('file://' + process.cwd() + '/preview/' + id + '.html');
  const ld = await p.evaluate(() => { const s=document.querySelector('script[type="application/ld+json"]'); const j=JSON.parse(s.text); return j['@graph'][0].name + ' | items=' + j['@graph'][0].itinerary.numberOfItems; });
  const h1 = await p.$$eval('h1', a => a.length); console.log(id, ld, 'h1=', h1); }
 console.log('errors', errs); await b.close(); })();
