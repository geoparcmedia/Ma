const { chromium } = require('playwright');
const pal=[['#c9773b','#5b2f17'],['#e0b27a','#8a5a1c'],['#7a8fa6','#2f3b4a'],['#d99a5b','#3a2a1c'],['#b7c29a','#4d5a33'],['#e7c8a0','#a0522d']];
(async () => {
  const b = await chromium.launch();
  for (const w of [1366, 390]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    let i=0;
    await p.route(/moroccoskytravel\.com\/wp-content/, r => { const [a,c]=pal[i++%pal.length];
      r.fulfill({contentType:'image/svg+xml',body:`<svg xmlns='http://www.w3.org/2000/svg' width='1200' height='800'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='${a}'/><stop offset='1' stop-color='${c}'/></linearGradient></defs><rect width='1200' height='800' fill='url(#g)'/><path d='M0 560 Q300 420 600 540 T1200 500 V800 H0Z' fill='${c}' opacity='.6'/></svg>`})});
    await p.route(/fonts\.(googleapis|gstatic)/, r => r.abort());
    await p.goto('file://' + process.cwd() + '/preview/'+(process.env.PG||'home')+'.html');
    await p.waitForTimeout(600);
    await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60))}window.scrollTo(0,0)});
    await p.waitForTimeout(1600);
    const H=await p.evaluate(()=>document.documentElement.scrollHeight);const step=w>500?1400:1800;for(let y=0,k=0;y<H;y+=step,k++){await p.screenshot({path:`preview/${process.env.PG||'home'}-${w}-${k}.png`,fullPage:true,clip:{x:0,y,width:w,height:Math.min(step,H-y)}})}
    console.log(w, await p.evaluate(() => document.documentElement.scrollWidth));
    await p.close();
  }
  await b.close();
})();
