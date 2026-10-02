const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const [name, w, h] of process.argv.slice(2).map(a => a.split(':'))) {
    const [id, vw] = [name, +w];
    const p = await b.newPage({ viewport: { width: vw, height: +h } });
    await p.goto('file://' + process.cwd() + '/preview/' + id + '.html');
    await p.waitForTimeout(300);
    await p.screenshot({ path: `preview/${id}-${vw}.png`, fullPage: true });
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    console.log(id, vw, 'scrollWidth', sw);
    await p.close();
  }
  await b.close();
})();
