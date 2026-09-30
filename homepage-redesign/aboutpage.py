import json, re, sys
sys.path.insert(0,'.')
from listpages import CSS as LCSS, JS, elementor
U='https://wegravelmorocco.com/wp-content/uploads/'
CSS=LCSS+"""
.wga-hero{min-height:56vh}
.wga-hero h1{margin-bottom:10px!important}
.wga-crumb{font-size:14px;font-weight:600;color:rgba(255,255,255,.8)}.wga-crumb a{color:#ffb56b!important}
.wga-intro{padding:96px 0}
.wga-ph{position:relative}
.wga-ph img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:18px;box-shadow:0 30px 60px -28px rgba(29,35,48,.55)}
.wga-ph:before{content:'';position:absolute;left:-18px;top:-18px;width:55%;height:55%;border-radius:18px;background:repeating-linear-gradient(45deg,var(--o) 0 2px,transparent 2px 12px);opacity:.35;z-index:-1}
.wga-ph:after{content:'';position:absolute;right:-16px;bottom:-16px;width:40%;height:40%;border:3px solid var(--o);border-radius:18px;z-index:-1}
.wga-tx h2{font-size:clamp(28px,3.2vw,40px)!important}
.wga-tx p{font-size:17px}
.wga-tx p strong{color:var(--ink)}
.wga-list{list-style:none;padding:0;margin:8px 0 26px;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.wga-list li{display:flex;align-items:center;gap:10px;padding:11px 14px;background:var(--sand);border:1px solid var(--line);border-radius:12px;font-size:15px;line-height:1.3;transition:transform .2s,border-color .2s,background .2s}
.wga-list li:hover{transform:translateY(-2px);border-color:var(--o);background:#fff}
.wga-list li:before{content:'';flex:none;width:26px;height:26px;border-radius:50%;background:var(--o) url(data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%2024%2024%27%20fill%3D%27none%27%20stroke%3D%27white%27%20stroke-width%3D%273%27%20stroke-linecap%3D%27round%27%20stroke-linejoin%3D%27round%27%3E%3Cpolyline%20points%3D%2720%206%209%2017%204%2012%27%2F%3E%3C%2Fsvg%3E) center/14px no-repeat}
.wga-list strong{color:var(--ink)}
.wga-people{padding:10px 0 0;text-align:center}
.wga-people h2{margin:0!important}
.wga-people h2:after{content:'';display:block;width:64px;height:4px;border-radius:4px;background:var(--o);margin:18px auto 0}
.wga-bio{margin-top:56px;background:var(--o) ;color:#fff;position:relative;overflow:hidden;padding:96px 0}
.wga-bio:before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 85% 20%,rgba(255,255,255,.18),transparent 45%),radial-gradient(circle at 10% 90%,rgba(0,0,0,.14),transparent 50%)}
.wga-bio .wgm-wrap{position:relative}
.wga-bio .wgm-eyebrow{color:#fff;opacity:.9}
.wga-bio h2{color:#fff!important}
.wga-bio p{color:rgba(255,255,255,.95)!important;font-size:17px}
.wga-bio-ph{position:relative}
.wga-bio-ph img{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:18px;border:6px solid rgba(255,255,255,.9);box-shadow:0 30px 60px -25px rgba(0,0,0,.5);transform:rotate(1.5deg);transition:transform .5s}
.wga-bio-ph:hover img{transform:rotate(0)}
.wga-bio-ph figcaption{position:absolute;left:18px;bottom:-18px;background:#fff;color:var(--ink);font-weight:800;font-size:15px;padding:10px 16px;border-radius:12px;box-shadow:0 12px 30px -12px rgba(0,0,0,.4)}
.wga-team{padding:96px 0;background:var(--sand)}
.wga-tgrid{display:grid;grid-template-columns:1fr 1fr;gap:32px;max-width:1000px;margin:0 auto}
.wga-m{background:#fff;border-radius:20px;overflow:hidden;border:1px solid var(--line);box-shadow:0 18px 40px -28px rgba(29,35,48,.4);transition:transform .35s,box-shadow .35s;display:flex;flex-direction:column}
.wga-m:hover{transform:translateY(-6px);box-shadow:0 30px 60px -30px rgba(29,35,48,.55)}
.wga-m-img{overflow:hidden;aspect-ratio:1/1;background:#eee}
.wga-m-img img{width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.wga-m:hover .wga-m-img img{transform:scale(1.05)}
.wga-m-b{padding:26px 28px 30px}
.wga-m h3{color:var(--o)!important;font-size:22px!important;letter-spacing:.04em!important;margin:0 0 4px!important}
.wga-role{display:inline-block;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--ink2);background:var(--sand);padding:6px 12px;border-radius:999px;margin-bottom:14px}
.wga-m p{margin:0!important;font-size:16px}
@media (max-width:1024px){.wga-intro .wgm-split,.wga-bio .wgm-split{gap:48px}}
@media (max-width:900px){.wga-intro .wgm-split,.wga-bio .wgm-split{grid-template-columns:1fr}.wga-ph{max-width:520px;margin:0 auto}.wga-bio .wgm-split>:first-child{order:2}}
@media (max-width:767px){.wga-hero{min-height:42vh}.wga-intro,.wga-bio,.wga-team{padding:60px 0}.wga-list{grid-template-columns:1fr}.wga-tgrid{grid-template-columns:1fr;gap:24px}.wga-ph:before,.wga-ph:after{display:none}.wga-bio{margin-top:40px}.wga-bio-ph img{transform:none}}
"""
items=['Gravel Bike Tours','Mountain Bike Tours','Road Bike Tours','Electric Bike Tours','Trekking in the Atlas Mountains','Trekking in the Sahara Desert','Morocco Imperial Cities Cultural Tours','Desert Tours from Marrakech or Fes']
lis=''.join("<li><strong>%s</strong></li>"%i for i in items)
def member(img,alt,name,role,desc):
    return ("<article class='wga-m wgm-rv'><div class='wga-m-img'><img src='"+img+"' width='600' height='600' alt='"+alt+"' loading='lazy' decoding='async'></div>"
            "<div class='wga-m-b'><h3>"+name+"</h3><span class='wga-role'>"+role+"</span><p>"+desc+"</p></div></article>")
body=(
"<section class='wgp-hero wga-hero'><img src='"+U+"2025/11/fullsizeoutput_1ccb.jpeg' alt='Road bike tour in Morocco with We Gravel Morocco' fetchpriority='high' decoding='async'>"
"<div class='wgm-wrap'><h1>About us</h1><span class='wga-crumb'><a href='https://wegravelmorocco.com/'>Home Page</a> / About us</span></div></section>"
"<section class='wga-intro'><div class='wgm-wrap wgm-split'>"
"<figure class='wga-ph wgm-rv' style='margin:0'><img src='"+U+"2025/11/fullsizeoutput_1cd0-790x1024.jpeg' width='790' height='1024' alt='We Gravel Morocco guide in the Atlas Mountains' loading='lazy' decoding='async'></figure>"
"<div class='wga-tx wgm-rv'><span class='wgm-eyebrow'>We Gravel Morocco</span><h2>Authentic Adventure Tours &amp; Local Guiding Expertise</h2>"
"<p>We Gravel Morocco is a local tour operator based in both <strong>Marrakech</strong> and <strong>Azilal</strong>, specializing in authentic adventure travel across Morocco. We design <strong>professional itineraries</strong> tailored to every traveler’s needs, whether you are a solo adventurer, a couple, a family, or a small group of explorers.</p>"
"<p>We offer unforgettable experiences including:</p><ul class='wga-list'>"+lis+"</ul>"
"<p>With a deep passion for adventure and local culture, We Gravel Morocco crafts journeys that immerse travelers in the <strong>true soul of Morocco</strong> — from high Atlas trails to golden Sahara dunes, through Berber villages and imperial cities.</p></div></div></section>"
"<section class='wga-people'><div class='wgm-wrap wgm-rv'><h2>The People Behind We Gravel Morocco</h2></div></section>"
"<section class='wga-bio'><div class='wgm-wrap wgm-split'>"
"<div class='wgm-rv'><span class='wgm-eyebrow'>Biography</span><h2>The Story Behind We Gravel Morocco</h2>"
"<p>Marouane Bargaz, born and raised in the Atlas Mountains in a Berber family, is the passionate founder of We Gravel Morocco. From a young age, Marouane’s adventurous spirit led him to explore the stunning landscapes of his homeland. In 2010, alongside his best friends, he decided to pursue formal training at the School of Mountain Guides (CFAMM) in the Bougmez Valley.</p>"
"<p>Marouane also spent several years living in Marrakech, where he pursued higher education. His experiences have given him a profound appreciation for sharing his enthusiasm for travel and adventure with like-minded explorers.</p>"
"<p>Marouane feels fortunate to have the opportunity to introduce travelers to the hidden gems of Morocco, consistently finding fun and unique adventures throughout the country he calls home.</p></div>"
"<figure class='wga-bio-ph wgm-rv' style='margin:0'><img src='"+U+"2025/10/IMG-20231101-WA0000-1024x682.jpg' width='1024' height='682' alt='Marouane Bargaz, founder of We Gravel Morocco' loading='lazy' decoding='async'><figcaption>Marouane Bargaz</figcaption></figure>"
"</div></section>"
"<section class='wga-team'><div class='wgm-wrap'><div class='wga-tgrid'>"
+member(U+"2025/10/WhatsApp-Image-2025-08-15-at-5.51ddd-600x600.png","Rachid Ouabass, We Gravel Morocco guide","RACHID OUABASS","Wilderness Guide &amp; Logistics","The soul of the company, a wilderness guide by profession and a passionate walker and leisure cyclist. He often works behind the scenes and takes care of accommodation and transportation, and he occasionally guides too.")
+member(U+"2025/10/WhatsApp-Image-2025-08-15-at-5.51-600x600.png","Mustapha Ouattar, We Gravel Morocco guide","MUSTAPHA OUATTAR","Wilderness Guide","Mustapha has been involved in tourism all his life. A wilderness guide by profession and a passionate walker and leisure cyclist, he was born in the Happy Valley, has a superb knowledge of the back roads of Morocco and is very passionate about his job.")
+"</div></div></section>")
html="<style>"+CSS+"</style><script>document.documentElement.classList.add('wgm-js')</script><div class='wgm'>"+body+"</div>"+JS
html=html.replace('\n',' ')
out=elementor(html,'about')
open('about_elementor.json','w').write(out)
print(len(out), out.count('\\\\'), html.count('"'))
prev=re.sub(r"https://wegravelmorocco\.com/wp-content/uploads/[^\"' ,]+","https://ph.local/x",html)
open('about_prev.html','w').write("<!doctype html><html><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><style>body{margin:0;font-family:Arial,sans-serif}</style></head><body><div style='height:86px;background:#313041'></div>"+prev+"</body></html>")
