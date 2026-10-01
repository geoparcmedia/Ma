const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const [name, mode] = process.argv.slice(2);
  const [w, h] = mode === 'm' ? [390, 844] : [1440, 900];
  const p = await b.newPage({ viewport: { width: w, height: h } });
  await p.route(/fonts\.(googleapis|gstatic)|maps\.google/, r => r.abort());
  await p.goto('file://' + process.cwd() + '/preview/' + name + '.html');
  await p.evaluate(() => document.querySelectorAll('.et-rv').forEach(e => e.classList.add('in')));
  const H = await p.evaluate(() => document.documentElement.scrollHeight);
  let k = 0;
  for (let y = 0; y < H; y += h) {
    await p.evaluate(y => window.scrollTo(0, y), y);
    await p.waitForTimeout(150);
    await p.screenshot({ path: `shots/${name}-${mode}-${k++}.png` });
  }
  console.log(name, mode, H, k);
  await b.close();
})();
