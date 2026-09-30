"""Animation layer for the homepage: CSS, hero scene, stats band, button bikes, JS.
Everything uses single quotes only (no double quotes / backslashes) so it stores cleanly."""
import re

BIKE = ("<svg viewBox='0 0 44 28' fill='none' stroke='currentColor' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true'>"
        "<g class='wh'><circle cx='9' cy='19' r='7'/><path d='M9 13v12M3 19h12'/></g>"
        "<g class='wh'><circle cx='35' cy='19' r='7'/><path d='M35 13v12M29 19h12'/></g>"
        "<path d='M9 19l7-11h14l5 11M16 8l4 11h-11M20 19l10-11M13 8h6M30 8l2-3h3'/></svg>")

RIDER = ("<svg viewBox='0 -24 46 52' fill='none' stroke='currentColor' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'>"
         "<g class='wh'><circle cx='9' cy='19' r='7.5'/><path d='M9 12.5v13M2.5 19h13'/></g>"
         "<g class='wh'><circle cx='36' cy='19' r='7.5'/><path d='M36 12.5v13M29.5 19h13'/></g>"
         "<path d='M9 19l7-11h14l6 11M16 8l4 11h-11M20 19l10-11M13 8h6M30 8l2-3h3'/>"
         "<path d='M17 6l8-13 8 10M25-7l-1 7 5 4-6 9M16 7l6 1 4 8' stroke='#fff'/>"
         "<circle cx='28' cy='-13' r='3.6' fill='#fff' stroke='none'/>"
         "<path d='M24.5-15.5c2-3 6-3 8 0' stroke='#E77717' stroke-width='3'/></svg>")

M = "<svg class='wgm-m {c}' viewBox='0 0 1440 220' preserveAspectRatio='none'><path d='{d}' fill='{f}'/></svg>"
SCENE = ("<div class='wgm-scene' aria-hidden='true'>"
         + M.format(c='m1', f='rgba(255,255,255,.08)', d='M0 220V120l110-40 90 30 150-80 120 60 110-30 170 70 150-90 130 60 140-50 130 40 140-30v150z')
         + M.format(c='m2', f='rgba(231,119,23,.22)', d='M0 220V160l140-30 120 25 160-55 150 50 120-20 170 45 160-60 150 45 150-25 120 20v65z')
         + M.format(c='m3', f='#fff', d='M0 220v-48c120-10 240-14 360-8s240 10 360 4 240-12 360-8 240 8 360 4v56z')
         + "<div class='wgm-road'></div><div class='wgm-rider'><i class='wgm-dust'></i><i class='wgm-dust'></i><i class='wgm-dust'></i>" + RIDER + "</div></div>")

STATS = ("<section class='wgm-stats'><div class='wgm-wrap'><div class='wgm-stats-in'>"
         "<div class='wgm-rv'><b><span class='wgm-count' data-to='10'>10</span></b><span>Guided tours</span></div>"
         "<div class='wgm-rv'><b><span class='wgm-count' data-to='4167'>4167</span> m</b><span>Highest summit – Toubkal</span></div>"
         "<div class='wgm-rv'><b>2–16</b><span>Travelers per group</span></div>"
         "<div class='wgm-rv'><b><span class='wgm-count' data-to='24'>24</span> h</b><span>Reply to your request</span></div>"
         "</div></div></section>")

CSS = """
.wgm-js .wgm-rv{opacity:0;transform:translateY(34px);transition:opacity .8s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1)}
.wgm-js .wgm-rv.in{opacity:1;transform:none}
.wgm-grid>.wgm-rv:nth-child(2),.wgm-vals>.wgm-rv:nth-child(2),.wgm-stats-in>.wgm-rv:nth-child(2){transition-delay:.1s}
.wgm-grid>.wgm-rv:nth-child(3),.wgm-vals>.wgm-rv:nth-child(3),.wgm-stats-in>.wgm-rv:nth-child(3){transition-delay:.2s}
.wgm-grid>.wgm-rv:nth-child(4),.wgm-vals>.wgm-rv:nth-child(4),.wgm-stats-in>.wgm-rv:nth-child(4){transition-delay:.3s}
.wgm-grid>.wgm-rv:nth-child(5){transition-delay:.4s}.wgm-grid>.wgm-rv:nth-child(6){transition-delay:.5s}
.wgm .wh{transform-box:fill-box;transform-origin:center;animation:wgmSpin .5s linear infinite}
@keyframes wgmSpin{to{transform:rotate(360deg)}}
/* stats */
.wgm-stats{padding:10px 0 20px}
.wgm-stats-in{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;background:#fff;border:1px solid var(--line);border-radius:18px;padding:28px 20px;box-shadow:0 30px 60px -40px rgba(29,35,48,.45)}
.wgm-stats-in>div{text-align:center;border-right:1px solid var(--line)}
.wgm-stats-in>div:last-child{border-right:0}
.wgm-stats-in b{display:block;font-size:clamp(30px,3.4vw,44px);line-height:1.1;color:var(--o);font-weight:800}
.wgm-stats-in span{font-size:14.5px;color:var(--mut)}
/* buttons with bike */
.wgm-btn{position:relative;overflow:hidden;transition:padding .35s cubic-bezier(.2,.7,.2,1),transform .15s,background .2s,color .2s}
.wgm-bk{position:absolute;left:14px;top:50%;width:30px;margin-top:-10px;opacity:0;transform:translateX(-60px);transition:transform .45s cubic-bezier(.2,.7,.2,1),opacity .3s;display:block;line-height:0}
.wgm-bk svg{width:30px;height:20px}
.wgm-bk .wh{animation-play-state:paused}
.wgm-btn:hover{padding-left:54px}
.wgm-btn:hover .wgm-bk{opacity:1;transform:none}
.wgm-btn:hover .wgm-bk .wh{animation-play-state:running}
/* 3D cards */
.wgm-card,.wgm-val{transform-style:preserve-3d;will-change:transform}
.wgm-card{transition:transform .25s ease-out,box-shadow .25s,opacity .8s}
.wgm-card:after{content:'';position:absolute;inset:0;border-radius:inherit;pointer-events:none;background:radial-gradient(420px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.35),transparent 45%);opacity:0;transition:opacity .3s}
.wgm-card{position:relative}
.wgm-card:hover:after{opacity:1}
.wgm-card-img img{transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.wgm-card:hover .wgm-card-img img{transform:scale(1.08)}
.wgm-card:hover .wgm-tag{background:var(--o)}
.wgm-val{transition:transform .25s ease-out,box-shadow .25s,opacity .8s}
.wgm-val:hover{box-shadow:0 26px 40px -26px rgba(29,35,48,.45)}
.wgm-val:hover svg{animation:wgmPop .6s ease}
@keyframes wgmPop{40%{transform:scale(1.18) rotate(-6deg)}}
.wgm-media img{transition:transform 1s cubic-bezier(.2,.7,.2,1)}
.wgm-media:hover img{transform:scale(1.05)}

@media (max-width:767px){.wgm-stats-in{grid-template-columns:1fr 1fr;padding:22px 12px}.wgm-stats-in>div:nth-child(2){border-right:0}.wgm-btn:hover{padding-left:28px}.wgm-bk{display:none}}
"""

JS_EARLY = SPRITE_PLACE = None
JS_EARLY = "<script>document.documentElement.classList.add('wgm-js');setTimeout(function(){var e=document.querySelectorAll('.wgm-rv');for(var i=0;i<e.length;i++)e[i].classList.add('in')},4000);</script>"

JS = ("<script>(function(){var d=document,w=window,rm=w.matchMedia('(prefers-reduced-motion: reduce)').matches;"
      "var rv=d.querySelectorAll('.wgm-rv');if('IntersectionObserver' in w){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});rv.forEach(function(el){io.observe(el)})}else{rv.forEach(function(el){el.classList.add('in')})}"
      "var cs=d.querySelectorAll('.wgm-count');function run(el){var to=+el.getAttribute('data-to'),t0=null;if(rm){el.textContent=to;return}function st(t){if(!t0)t0=t;var p=Math.min((t-t0)/1600,1);el.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(st)}requestAnimationFrame(st)}"
      "if('IntersectionObserver' in w){var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);io2.unobserve(e.target)}})});cs.forEach(function(el){el.textContent='0';io2.observe(el)})}"
      "if(!rm&&w.matchMedia('(hover: hover) and (pointer: fine)').matches){d.querySelectorAll('.wgm-card,.wgm-val').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform='perspective(900px) rotateY('+(x*12)+'deg) rotateX('+(-y*12)+'deg) translateY(-6px)';c.style.setProperty('--mx',(x+.5)*100+'%');c.style.setProperty('--my',(y+.5)*100+'%')});c.addEventListener('pointerleave',function(){c.style.transform=''})})}"
      "})();</script>")


SPRITE = ("<svg width='0' height='0' style='position:absolute' aria-hidden='true'><symbol id='wgm-b' viewBox='0 0 44 28'>"
          + BIKE[BIKE.index('>') + 1:-6] + "</symbol></svg>")
BTN_BIKE = ("<i class='wgm-bk'><svg viewBox='0 0 44 28' fill='none' stroke='currentColor' stroke-width='2.4' "
            "stroke-linecap='round' stroke-linejoin='round'><use href='#wgm-b'/></svg></i>")


def add_bikes(html):
    return re.sub(r"(<(?:a|span) class='wgm-btn[^']*'[^>]*>)", lambda m: m.group(1) + BTN_BIKE, html)


def add_reveal(html):
    for cls in ['wgm-head', 'wgm-val', 'wgm-card', 'wgm-media', 'wgm-custom', 'wgm-tabs', 'wgm-box']:
        html = re.sub(r"class='(%s)'" % cls, r"class='\1 wgm-rv'", html)
    html = re.sub(r"<details", "<details class='wgm-rv'", html)
    return html

SPLIT = ("<script>(function(){var d=document,h=d.querySelector('.wgm-hero h1');if(!h||!d.documentElement.classList.contains('wgm-js'))return;var n=0;"
         "function sp(el){[].slice.call(el.childNodes).forEach(function(c){if(c.nodeType===3){var f=d.createDocumentFragment();c.textContent.split(' ').forEach(function(wd,i,a){if(wd){var s=d.createElement('span');s.className='wgm-w';s.style.animationDelay=(0.15+n++*0.1)+'s';s.textContent=wd;f.appendChild(s)}if(i<a.length-1)f.appendChild(d.createTextNode(' '))});el.replaceChild(f,c)}else if(c.nodeType===1)sp(c)})}"
         "sp(h);h.classList.add('wgm-h1s')})();</script>")
