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
/* hero entrance */
.wgm-hero-in>*{animation:wgmUp 1s cubic-bezier(.2,.7,.2,1) both}
.wgm-hero-in>:nth-child(2){animation-delay:.12s}.wgm-hero-in>:nth-child(3){animation-delay:.24s}.wgm-hero-in>:nth-child(4){animation-delay:.36s}.wgm-hero-in>:nth-child(5){animation-delay:.48s}
@keyframes wgmUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}
.wgm-hero{perspective:1200px}
.wgm-hero:after{z-index:1;opacity:var(--ov,1);background:linear-gradient(90deg,rgba(12,14,20,.55) 0%,rgba(12,14,20,.25) 45%,rgba(12,14,20,0) 75%),linear-gradient(180deg,rgba(12,14,20,.25) 0%,rgba(12,14,20,0) 30%,rgba(12,14,20,0) 60%,rgba(12,14,20,.45) 100%)!important}
.wgm .wgm-slide{filter:saturate(1.18) contrast(1.05) brightness(1.05)}
.wgm-hero h1,.wgm-hero p,.wgm-hero .wgm-eyebrow,.wgm-trust{text-shadow:0 2px 18px rgba(0,0,0,.55)}
.wgm-slides{position:absolute;inset:-3%;will-change:transform;transform:scale(1.08)}
.wgm-sl{position:absolute;inset:0;overflow:hidden;will-change:transform}
.wgm-sl+.wgm-sl{clip-path:circle(0px at 50% 58%)}
.wgm .wgm-slide{position:absolute;inset:0;width:100%;height:100%;max-width:none;object-fit:cover;animation:wgmKB 18s ease-in-out infinite alternate}
.wgm-sl:nth-child(2) .wgm-slide{animation-name:wgmKB2;animation-duration:22s}
.wgm-sl:nth-child(3) .wgm-slide{animation-duration:20s;animation-direction:alternate-reverse}
@keyframes wgmKB{from{transform:scale(1.02) translate(0,0)}to{transform:scale(1.16) translate(-2%,-1.5%)}}
@keyframes wgmKB2{from{transform:scale(1.14) translate(2%,1%)}to{transform:scale(1.02) translate(-1%,0)}}
.wgm-ring{z-index:3;position:absolute;left:50%;top:58%;width:0;height:0;border-radius:50%;pointer-events:none;opacity:0;transform:translate(-50%,-50%);box-shadow:0 0 0 4px #E77717,0 0 60px 14px rgba(231,119,23,.75),inset 0 0 50px 10px rgba(231,119,23,.6)}
.wgm-fx{position:absolute;inset:0;width:100%;height:100%;z-index:2;mix-blend-mode:screen;pointer-events:none}
.wgm-hero-in>h1.wgm-h1s{animation:none}
.wgm-hero h1 .wgm-w{color:inherit}.wgm-w{display:inline-block;animation:wgmFlip 1s cubic-bezier(.2,.7,.2,1) both;transform-origin:50% 100%}
@keyframes wgmFlip{from{opacity:0;transform:perspective(700px) rotateX(-90deg) translateY(40px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}
.wgm-idx{position:absolute;right:30px;top:50%;z-index:3;transform:translateY(-50%);display:flex;flex-direction:column;gap:20px;color:rgba(255,255,255,.5);font-size:12px;letter-spacing:.18em;text-transform:uppercase;font-weight:700}
.wgm-idx i{font-style:normal;display:flex;align-items:center;gap:10px;justify-content:flex-end;transition:color .4s,transform .4s}
.wgm-idx i:after{content:'';width:18px;height:2px;background:currentColor;transition:width .4s}
.wgm-idx b{font-size:15px}
.wgm-idx i.on{color:#fff;transform:translateX(-6px)}
.wgm-idx i.on b{color:#E77717}.wgm-idx i.on:after{width:42px;background:#E77717}
.wgm-hero .wgm-wrap{z-index:3}
.wgm-hero{padding-bottom:120px}
.wgm-pin{position:relative}
.wgm-pin>.wgm-hero{position:relative;height:100vh;min-height:620px;max-height:1100px}
.wgm-pin.pinned{height:300vh}
.wgm-pin.pinned>.wgm-hero{position:sticky;top:0;max-height:none}
.wgm-hero2{will-change:transform,opacity,filter;position:absolute;left:0;right:0;top:30%;z-index:3;text-align:center;color:#fff;opacity:0;pointer-events:none;padding:0 20px}
.wgm-hero2 b{display:block;font-size:clamp(34px,6vw,84px);font-weight:800;line-height:1.05;letter-spacing:-.02em;text-shadow:0 10px 40px rgba(0,0,0,.4)}
.wgm-hero2 span{display:inline-block;margin-top:14px;font-size:clamp(15px,1.4vw,19px);letter-spacing:.2em;text-transform:uppercase;color:#ffb56b;font-weight:700}
.wgm-cue{position:absolute;left:50%;bottom:150px;z-index:3;width:26px;height:42px;margin-left:-13px;border:2px solid rgba(255,255,255,.8);border-radius:14px}
.wgm-cue:after{content:'';position:absolute;left:50%;top:8px;width:4px;height:8px;margin-left:-2px;border-radius:2px;background:#fff;animation:wgmCue 1.6s ease-in-out infinite}
@keyframes wgmCue{0%{opacity:0;transform:translateY(0)}40%{opacity:1}100%{opacity:0;transform:translateY(14px)}}
/* scene */
.wgm-scene{position:absolute;left:0;right:0;bottom:-1px;height:220px;z-index:2;pointer-events:none;overflow:hidden}
.wgm-m{position:absolute;left:0;bottom:0;width:100%;height:100%;will-change:transform}
.wgm-m.m1{height:100%}.wgm-m.m2{height:75%}.wgm-m.m3{height:40%}
.wgm-road{position:absolute;left:0;right:0;bottom:62px;height:0;border-top:3px dashed rgba(231,119,23,.55)}
.wgm-rider{position:absolute;left:0;bottom:60px;width:100px;color:var(--o);transform:translateX(6vw);will-change:transform}
.wgm-rider .wh,.wgm-rider svg,.wgm-dust{animation-play-state:paused}
.wgm-rider.moving .wh,.wgm-rider.moving svg,.wgm-rider.moving .wgm-dust{animation-play-state:running}
.wgm-dust{opacity:0}.wgm-rider.moving .wgm-dust{opacity:1}
.wgm-rider svg{display:block;animation:wgmBump .35s ease-in-out infinite alternate;filter:drop-shadow(0 6px 8px rgba(0,0,0,.35))}
@keyframes wgmBump{from{transform:translateY(0) rotate(0)}to{transform:translateY(-2px) rotate(-1.5deg)}}
.wgm .wh{transform-box:fill-box;transform-origin:center;animation:wgmSpin .5s linear infinite}
@keyframes wgmSpin{to{transform:rotate(360deg)}}
.wgm-dust{position:absolute;left:0;bottom:4px;width:10px;height:10px;border-radius:50%;background:rgba(214,170,120,.8);animation:wgmDust 1s ease-out infinite}
.wgm-dust:nth-child(2){animation-delay:.33s;width:7px;height:7px}.wgm-dust:nth-child(3){animation-delay:.66s;width:12px;height:12px}
@keyframes wgmDust{from{opacity:.9;transform:translate(0,0) scale(.6)}to{opacity:0;transform:translate(-38px,-14px) scale(1.8)}}
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
@media (max-width:767px) and (max-height:800px){.wgm-trust{display:none}}
@media (max-width:1100px){.wgm-idx{display:none}}
@media (max-width:767px){.wgm-pin>.wgm-hero{height:auto;min-height:0;max-height:none}.wgm-hero2{display:none}.wgm-hero p{font-size:15.5px;line-height:1.6}.wgm-hero h1{font-size:34px}.wgm-cue{display:none}.wgm-hero .wgm-wrap{padding-top:40px!important}.wgm-trust{margin-top:24px}.wgm-scene{height:130px}.wgm-road{bottom:36px}.wgm-rider{bottom:34px;width:64px}.wgm-hero{padding-bottom:90px}.wgm-stats-in{grid-template-columns:1fr 1fr;padding:22px 12px}.wgm-stats-in>div:nth-child(2){border-right:0}.wgm-btn:hover{padding-left:28px}.wgm-bk{display:none}}
@media (prefers-reduced-motion:reduce){.wgm *,.wgm *:before,.wgm *:after{animation:none!important;transition:none!important}.wgm-js .wgm-rv{opacity:1;transform:none}.wgm-rider,.wgm-cue,.wgm-hero2,.wgm-fx,.wgm-ring,.wgm-idx{display:none}.wgm-sl+.wgm-sl{display:none}.wgm-pin.pinned{height:auto}.wgm-pin.pinned>.wgm-hero{position:relative}}
"""

JS_EARLY = SPRITE_PLACE = None
JS_EARLY = "<script>document.documentElement.classList.add('wgm-js');setTimeout(function(){var e=document.querySelectorAll('.wgm-rv');for(var i=0;i<e.length;i++)e[i].classList.add('in')},4000);</script>"

JS = ("<script>(function(){var d=document,w=window,rm=w.matchMedia('(prefers-reduced-motion: reduce)').matches;"
      "var rv=d.querySelectorAll('.wgm-rv');if('IntersectionObserver' in w){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});rv.forEach(function(el){io.observe(el)})}else{rv.forEach(function(el){el.classList.add('in')})}"
      "var cs=d.querySelectorAll('.wgm-count');function run(el){var to=+el.getAttribute('data-to'),t0=null;if(rm){el.textContent=to;return}function st(t){if(!t0)t0=t;var p=Math.min((t-t0)/1600,1);el.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(st)}requestAnimationFrame(st)}"
      "if('IntersectionObserver' in w){var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);io2.unobserve(e.target)}})});cs.forEach(function(el){el.textContent='0';io2.observe(el)})}"
      "if(!rm&&w.matchMedia('(hover: hover) and (pointer: fine)').matches){d.querySelectorAll('.wgm-card,.wgm-val').forEach(function(c){c.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform='perspective(900px) rotateY('+(x*12)+'deg) rotateX('+(-y*12)+'deg) translateY(-6px)';c.style.setProperty('--mx',(x+.5)*100+'%');c.style.setProperty('--my',(y+.5)*100+'%')});c.addEventListener('pointerleave',function(){c.style.transform=''})})}"
      "var pin=d.querySelector('.wgm-pin'),hero=pin&&pin.querySelector('.wgm-hero'),sw=hero&&hero.querySelector('.wgm-slides'),sl=hero?hero.querySelectorAll('.wgm-sl'):[],ring=hero&&hero.querySelector('.wgm-ring'),ix=d.querySelectorAll('.wgm-idx i'),ms=d.querySelectorAll('.wgm-m'),hi=d.querySelector('.wgm-hero-in'),ha=d.querySelector('.h2a'),hb=d.querySelector('.h2b'),cue=d.querySelector('.wgm-cue'),rd=d.querySelector('.wgm-rider'),tk=false,to=null,pinned=false,act=-1,fxb=0,mx=0,my=0,cx0=0,cy0=0,ml=false;"
      "function cl(x){return Math.min(Math.max(x,0),1)}function band(p,a,b,c,e){return cl((p-a)/(b-a))*cl((e-p)/(e-c))}function ez(t){return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}"
      "var auto=w.innerWidth<768;if(pin&&!rm&&!auto&&w.CSS&&CSS.supports('overflow','clip')){for(var el=pin.parentElement;el&&el!==d.documentElement;el=el.parentElement){var cs2=getComputedStyle(el);if(cs2.overflowX==='hidden'||cs2.overflowY==='hidden'||cs2.overflowX==='auto'||cs2.overflowY==='auto'){el.style.overflow='clip'}}pin.classList.add('pinned');pinned=true}"
      "function px(){tk=false;if(!hero)return;var vh=w.innerHeight,vw=w.innerWidth,H=hero.offsetHeight,p,shift=0;"
      "if(pinned){var pr=pin.getBoundingClientRect(),hr=hero.getBoundingClientRect();if(pr.top<-20&&pr.bottom>vh+20&&Math.abs(hr.top)>20){pin.classList.remove('pinned');pinned=false;return px()}p=cl(-pr.top/(pin.offsetHeight-vh))}else{p=cl(-hero.getBoundingClientRect().top/H);shift=p*H}"
      "if(sw)sw.style.transform='translate3d('+(cx0*-26)+'px,'+(shift*0.45+cy0*-18)+'px,0) scale('+(1.08-0.04*p)+') rotateY('+(cx0*5)+'deg) rotateX('+(cy0*-4)+'deg)';"
      "if(sl.length>2&&sw&&!auto){var W=sw.offsetWidth,SH=sw.offsetHeight,Rm=Math.sqrt(W*W/4+SH*SH*0.3364)+30,t1=ez(cl((p-0.2)/0.2)),t2=ez(cl((p-0.54)/0.2)),ts=[1,t1,t2],rg=0,rt=0;"
      "for(var k=0;k<3;k++){var tin=ts[k],tout=k<2?ts[k+1]:0,s=(k?1.35-0.35*tin:1)*(1+0.3*tout);sl[k].style.transform='scale('+s+')';if(k){sl[k].style.clipPath=tin>=1?'none':'circle('+(tin*Rm)+'px at 50% 58%)';if(tin>0&&tin<1){rg=tin;rt=tin*Rm}}}"
      "if(ring){ring.style.opacity=Math.sin(rg*Math.PI);ring.style.width=ring.style.height=(2*rt)+'px'}"
      "var a2=p<0.32?0:p<0.66?1:2;if(a2!==act){act=a2;for(var n=0;n<ix.length;n++)ix[n].classList.toggle('on',n===a2)}}"
      "ms.forEach(function(m,i){m.style.transform='translate3d(0,'+(p*[70,35,0][i])+'px,0)'});"
      "if(rd)rd.style.transform='translateX('+(vw*0.06+p*(vw*0.94-40))+'px)';"
      "if(hi){hi.style.opacity=cl(1-p*4);hi.style.transform='translate3d('+(cx0*14)+'px,'+(shift*0.3-p*80+cy0*10)+'px,0)'}"
      "[[ha,0.34,0.42,0.52,0.58],[hb,0.7,0.78,1.1,1.2]].forEach(function(x){if(!x[0])return;var q=band(p,x[1],x[2],x[3],x[4]);x[0].style.opacity=q;x[0].style.filter=q<1?'blur('+((1-q)*10)+'px)':'none';x[0].style.transform='translate3d('+(cx0*-10)+'px,'+(shift*0.5+(1-q)*40)+'px,0) scale('+(0.92+0.08*q)+')'});"
      "if(cue)cue.style.opacity=cl(1-p*8);hero.style.setProperty('--ov',1-0.6*cl(p*4))}"
      "function ml2(){cx0+=(mx-cx0)*0.08;cy0+=(my-cy0)*0.08;px();if(Math.abs(mx-cx0)+Math.abs(my-cy0)>0.002){requestAnimationFrame(ml2)}else{ml=false}}"
      "if(hero&&!rm&&w.matchMedia('(hover: hover) and (pointer: fine)').matches){hero.addEventListener('pointermove',function(e){var r=hero.getBoundingClientRect();mx=(e.clientX-r.left)/r.width-.5;my=(e.clientY-r.top)/r.height-.5;if(!ml){ml=true;requestAnimationFrame(ml2)}});hero.addEventListener('pointerleave',function(){mx=0;my=0;if(!ml){ml=true;requestAnimationFrame(ml2)}})}"
      "var cv=hero&&hero.querySelector('.wgm-fx');if(cv&&cv.getContext&&!rm){var g=cv.getContext('2d'),P=[],N=w.innerWidth<768?22:55,vis=true,dpr=Math.min(w.devicePixelRatio||1,1.5);"
      "function sz(){cv.width=cv.offsetWidth*dpr;cv.height=cv.offsetHeight*dpr}sz();w.addEventListener('resize',sz);"
      "for(var q0=0;q0<N;q0++)P.push({x:Math.random(),y:Math.random(),r:.6+Math.random()*2.2,s:.2+Math.random()*.8,a:.25+Math.random()*.55,o:Math.random()*6.3});"
      "if('IntersectionObserver' in w)new IntersectionObserver(function(e){vis=e[0].isIntersecting}).observe(hero);"
      "function fr(t){requestAnimationFrame(fr);if(!vis||d.hidden)return;var W=cv.width,H=cv.height;g.clearRect(0,0,W,H);fxb*=.94;P.forEach(function(q){q.x+=q.s*(1+fxb)*0.0009;q.y-=q.s*0.0004*(1+fxb*.5)-Math.sin(t/1500+q.o)*0.0003;if(q.x>1.02){q.x=-.02;q.y=Math.random()}if(q.y<-.02)q.y=1.02;g.beginPath();g.arc(q.x*W,q.y*H,q.r*dpr,0,6.283);g.fillStyle='rgba(255,196,130,'+(q.a*(.6+.4*Math.sin(t/700+q.o)))+')';g.fill()})}requestAnimationFrame(fr)}"
"if(auto&&!rm&&sl.length>2&&sw){var cur=0;function show(n){var el=sl[n],pv=sl[cur],t0=null,W=sw.offsetWidth,SH=sw.offsetHeight,Rm=Math.sqrt(W*W/4+SH*SH*0.3364)+30;for(var i=0;i<sl.length;i++){sl[i].style.zIndex=i===n?2:(i===cur?1:0)}el.style.clipPath='circle(0px at 50% 58%)';"
      "function st(t){if(!t0)t0=t;var k=Math.min((t-t0)/1400,1),e=ez(k);el.style.clipPath=k>=1?'none':'circle('+(e*Rm)+'px at 50% 58%)';el.style.transform='scale('+(1.3-0.3*e)+')';pv.style.transform='scale('+(1+0.25*e)+')';if(ring){ring.style.opacity=k<1?Math.sin(e*Math.PI):0;ring.style.width=ring.style.height=(2*e*Rm)+'px'}if(k<1){requestAnimationFrame(st)}else{pv.style.transform='';cur=n}}requestAnimationFrame(st)}"
      "setInterval(function(){if(!d.hidden)show((cur+1)%sl.length)},5000)}"
"if(!rm){w.addEventListener('scroll',function(){fxb=Math.min(fxb+0.5,6);if(rd){rd.classList.add('moving');clearTimeout(to);to=setTimeout(function(){rd.classList.remove('moving')},160)}if(!tk){tk=true;requestAnimationFrame(px)}},{passive:true});w.addEventListener('resize',px);px()}})();</script>")


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
