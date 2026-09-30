"""New homepage hero (option C): full-screen photo slider with thumbnails.
Single quotes only, no backslashes (stored via wp_update_post_meta)."""
U9 = 'https://wegravelmorocco.com/wp-content/uploads/2026/09/'
U12 = 'https://wegravelmorocco.com/wp-content/uploads/2025/12/'
SLIDES = [
    # desktop src, mobile src, thumb, label, alt, object-position desktop
    (U9 + 'gravel-bike-group-high-atlas-morocco.jpg', U9 + 'gravel-bike-group-high-atlas-morocco-600x810.jpg',
     U9 + 'gravel-bike-group-high-atlas-morocco-410x250.jpg', 'High Atlas trails',
     'Small group gravel bike tour on a dirt road in the High Atlas Mountains, Morocco', '50% 62%'),
    (U9 + 'gravel-bike-sunset-atlas-morocco.jpg', U9 + 'gravel-bike-sunset-atlas-morocco-600x810.jpg',
     U9 + 'gravel-bike-sunset-atlas-morocco-410x250.jpg', 'Sunset rides',
     'Two cyclists riding a rocky ridge at sunset in the Atlas Mountains, Morocco', '50% 72%'),
    (U12 + 'GRAVEL-MOROCCO-BIKE-1024x684.png', U12 + 'GRAVEL-MOROCCO-BIKE-768x513.png',
     U12 + 'GRAVEL-MOROCCO-BIKE-768x513.png', 'Gravel roads',
     'Gravel bike tour in the Atlas Mountains of Morocco', '50% 50%'),
    (U9 + 'bike-tour-4x4-support-morocco.jpg', U9 + 'bike-tour-4x4-support-morocco-600x810.jpg',
     U9 + 'bike-tour-4x4-support-morocco-410x250.jpg', 'Daily 4x4 support',
     'Toyota 4x4 support vehicle with bikes on the roof for a guided bike tour in Morocco', '50% 45%'),
]


def hero_html():
    sl, th = [], []
    for i, (d, m, t, label, alt, pos) in enumerate(SLIDES):
        eager = "fetchpriority='high' loading='eager'" if i == 0 else "loading='lazy'"
        sl.append("<div class='wgx-s%s' data-i='%d'><picture><source media='(max-width:767px)' srcset='%s'>"
                  "<img src='%s' alt='%s' decoding='async' %s style='object-position:%s'></picture></div>"
                  % (' on' if i == 0 else '', i, m, d, alt, eager, pos))
        th.append("<button type='button' class='wgx-t%s' data-i='%d' aria-label='Show photo: %s'><img src='%s' alt='' loading='lazy'><span>%s</span><i></i></button>"
                  % (' on' if i == 0 else '', i, label, t, label))
    return ("<section class='wgx' aria-label='We Gravel Morocco – gravel bike tours'>"
            "<div class='wgx-slides'>" + ''.join(sl) + "</div>"
            "<div class='wgx-in'><div class='wgx-wrap'>"
            "<p class='wgx-eb'><b class='wgx-n'>01</b> / 0%d — <span class='wgx-l'>%s</span></p>" % (len(SLIDES), SLIDES[0][3]) +
            "<h1>Gravel Bike Tours in <span>Morocco</span></h1>"
            "<p class='wgx-p'>Small groups, licensed local guides and daily 4x4 support – ride the Atlas Mountains all the way to the Sahara.</p>"
            "<div class='wgx-ctas'><a class='wgm-btn wgm-btn-o' href='https://wegravelmorocco.com/cycling/'>Explore Cycling Tours</a>"
            "<a class='wgm-btn wgm-btn-w' href='https://wegravelmorocco.com/trekking/'>Trekking Tours</a></div>"
            "<ul class='wgx-trust'><li>Licensed local guides</li><li>Groups of 2–16</li><li>Tailor-made tours</li></ul>"
            "</div></div>"
            "<div class='wgx-nav'>" + ''.join(th) + "</div>"
            "</section>")


CSS = """
.wgx{position:relative;height:100vh;height:100svh;min-height:640px;max-height:1080px;overflow:hidden;background:#1b1a22;color:#fff}
.wgx-slides,.wgx-s{position:absolute;inset:0}
.wgx-s{opacity:0;transition:opacity 1.2s ease;z-index:0}
.wgx-s.on{opacity:1;z-index:1}
.wgx-s img{position:absolute;inset:0;width:100%!important;height:100%!important;max-width:none!important;object-fit:cover;transform:scale(1.02)}
.wgx-s.on img{animation:wgxKB 9s ease-out both}
@keyframes wgxKB{from{transform:scale(1.14)}to{transform:scale(1.02)}}
.wgx:after{content:'';position:absolute;inset:0;z-index:2;pointer-events:none;background:linear-gradient(180deg,rgba(12,12,18,.55) 0%,rgba(12,12,18,.05) 30%,rgba(12,12,18,.05) 50%,rgba(12,12,18,.7) 100%),linear-gradient(90deg,rgba(12,12,18,.55) 0%,rgba(12,12,18,0) 60%)}
.wgx-in{position:absolute;inset:0;z-index:3;display:flex;align-items:flex-end;padding-bottom:150px}
.wgx-wrap{width:100%;max-width:1240px;margin:0 auto;padding:0 32px}
.wgx-eb{margin:0 0 14px!important;font-size:13px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:#fff!important;opacity:.9}
.wgx-eb b{color:#E77717}
.wgx h1{color:#fff!important;font-size:clamp(40px,6.2vw,86px)!important;line-height:1.02!important;font-weight:800;letter-spacing:-.025em;margin:0 0 18px!important;max-width:760px;text-shadow:0 4px 30px rgba(0,0,0,.35)}
.wgx h1 span{color:#E77717}
.wgx-p{font-size:clamp(16px,1.4vw,19px)!important;color:rgba(255,255,255,.9)!important;max-width:560px;margin:0 0 30px!important;line-height:1.6}
.wgx-ctas{display:flex;flex-wrap:wrap;gap:14px}
.wgx-trust{display:flex;flex-wrap:wrap;gap:8px 22px;list-style:none;margin:26px 0 0!important;padding:0!important}
.wgx-trust li{display:flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:rgba(255,255,255,.92)}
.wgx-trust li:before{content:'';width:7px;height:7px;border-radius:50%;background:#E77717}
.wgx-in .wgx-wrap>*{animation:wgxUp .9s cubic-bezier(.2,.7,.2,1) both}
.wgx-in .wgx-wrap>:nth-child(2){animation-delay:.1s}.wgx-in .wgx-wrap>:nth-child(3){animation-delay:.2s}.wgx-in .wgx-wrap>:nth-child(4){animation-delay:.3s}.wgx-in .wgx-wrap>:nth-child(5){animation-delay:.4s}
@keyframes wgxUp{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}
.wgx-nav{position:absolute;z-index:4;right:32px;bottom:40px;display:flex;gap:12px}
.wgx-t{position:relative;width:150px;padding:0;border:0;border-radius:12px;overflow:hidden;cursor:pointer;background:rgba(255,255,255,.1);backdrop-filter:blur(6px);color:#fff;text-align:left;font:600 12.5px/1.2 inherit;transition:transform .3s,opacity .3s;opacity:.7}
.wgx-t:hover{opacity:1;transform:translateY(-3px)}
.wgx-t.on{opacity:1}
.wgx-t img{display:block;width:100%!important;height:78px!important;object-fit:cover}
.wgx-t span{display:block;padding:8px 10px 10px}
.wgx-t i{position:absolute;left:0;bottom:0;height:3px;width:0;background:#E77717}
.wgx-t.on i{animation:wgxBar 6s linear forwards}
.wgx.paused .wgx-t.on i{animation-play-state:paused}
@keyframes wgxBar{to{width:100%}}
@media (max-width:1100px){.wgx-in{padding-bottom:90px}.wgx-nav{left:0;right:0;bottom:34px;justify-content:center;gap:8px}.wgx-t{width:40px;height:4px;border-radius:2px;background:rgba(255,255,255,.35);opacity:1;backdrop-filter:none}.wgx-t img,.wgx-t span{display:none!important}.wgx-t i{height:100%}}
@media (max-width:1024px){.wgx{height:calc(100vh - 64px);height:calc(100svh - 64px);min-height:560px;max-height:none}}
@media (max-width:767px){
.wgx{min-height:600px}
.wgx:after{background:linear-gradient(180deg,rgba(12,12,18,.25) 0%,rgba(12,12,18,.1) 30%,rgba(12,12,18,.78) 72%,rgba(12,12,18,.9) 100%)}
.wgx-in{padding-bottom:84px}.wgx-wrap{padding:0 18px}
.wgx h1{font-size:38px!important}
.wgx-p{font-size:15.5px!important;margin-bottom:22px!important}
.wgx-ctas .wgm-btn{width:100%;justify-content:center}
.wgx-trust{display:none}
.wgx-nav{left:0;right:0;bottom:30px;justify-content:center;gap:8px}
.wgx-t{width:34px;height:4px;border-radius:2px;background:rgba(255,255,255,.35);opacity:1;backdrop-filter:none}
.wgx-t img,.wgx-t span{display:none!important}
.wgx-t i{height:100%}
}
/* stats band under the hero */
.wgm-stats{padding:34px 0 10px!important}
.wgm-stats-in b span{font-size:inherit!important;color:inherit!important}
/* header overlay on the homepage (desktop header only) */
@media (min-width:1025px){
body.home .header-builder-frontend .header-builder-inner{position:absolute!important;top:0;left:0;right:0;width:100%}
body.home .header-builder-frontend .elementor-element-35ff7978,body.home .header-builder-frontend .elementor-element-35ff7978:not(.elementor-motion-effects-element-type-background){background:transparent!important}
body.home .gv-sticky-wrapper:not(.is-fixed)>.elementor-section{background:transparent!important;box-shadow:none!important}
body.home .header-builder-inner{background:linear-gradient(180deg,rgba(10,10,16,.6),rgba(10,10,16,0))}
}
@media (prefers-reduced-motion:reduce){.wgx-s.on img,.wgx-in .wgx-wrap>*{animation:none}.wgx-s{transition:none}}
"""

JS = ("<script>(function(){var d=document,h=d.querySelector('.wgx');if(!h)return;var s=h.querySelectorAll('.wgx-s'),t=h.querySelectorAll('.wgx-t'),n=h.querySelector('.wgx-n'),l=h.querySelector('.wgx-l'),i=0,tm=null,"
      "rm=window.matchMedia('(prefers-reduced-motion: reduce)').matches,lab=[];for(var k=0;k<t.length;k++){lab.push(t[k].querySelector('span').textContent)}"
      "function go(j){if(j===i)return;s[i].classList.remove('on');t[i].classList.remove('on');i=(j+s.length)%s.length;var im=s[i].querySelector('img');if(im.loading==='lazy'){im.loading='eager'}"
      "s[i].classList.add('on');t[i].classList.add('on');if(n)n.textContent='0'+(i+1);if(l)l.textContent=lab[i];start()}"
      "function start(){clearTimeout(tm);t[i].classList.remove('on');void t[i].offsetWidth;t[i].classList.add('on');if(!rm)tm=setTimeout(function(){go(i+1)},6000)}"
      "for(var k2=0;k2<t.length;k2++){t[k2].addEventListener('click',function(){go(+this.getAttribute('data-i'))})}"
      "var x0=null;h.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});h.addEventListener('touchend',function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>50)go(dx<0?i+1:i-1);x0=null},{passive:true});"
      "var nv=h.querySelector('.wgx-nav');nv.addEventListener('mouseenter',function(){clearTimeout(tm);h.classList.add('paused')});nv.addEventListener('mouseleave',function(){h.classList.remove('paused');start()});"
      "d.addEventListener('visibilitychange',function(){if(d.hidden){clearTimeout(tm)}else{start()}});"
      "setTimeout(function(){for(var k3=1;k3<s.length;k3++){var m=s[k3].querySelector('img');m.loading='eager'}},2500);start()})();</script>")
