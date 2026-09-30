"""Homepage hero - design A: full-screen photo, centered title, 'find my tour' bar.
Single quotes only, no backslashes."""
U9 = 'https://wegravelmorocco.com/wp-content/uploads/2026/09/'
T = 'https://wegravelmorocco.com/'


def hero_html():
    return ("<section class='wga'>"
            "<picture class='wga-bg'><source media='(max-width:767px)' srcset='" + U9 + "gravel-bike-group-high-atlas-morocco-600x810.jpg'>"
            "<img src='" + U9 + "gravel-bike-group-high-atlas-morocco.jpg' alt='Small group gravel bike tour on a dirt road in the High Atlas Mountains, Morocco' fetchpriority='high' decoding='async'></picture>"
            "<div class='wga-in'>"
            "<span class='wga-eb'>Gravel · Cycling · Trekking</span>"
            "<h1>Gravel Bike Tours in <span>Morocco</span></h1>"
            "<p class='wga-p'>Ride the Atlas. Reach the Sahara. Guided gravel bike &amp; trekking tours in small groups with licensed local guides.</p>"
            "<div class='wga-ctas'><a class='wgm-btn wgm-btn-o' href='" + T + "cycling/'>Explore Cycling Tours</a>"
            "<a class='wgm-btn wgm-btn-w' href='" + T + "trekking/'>Trekking Tours</a></div>"
            "</div>"
            "<form class='wga-find' action='" + T + "cycling/' method='get' onsubmit='return false'>"
            "<label><small>Activity</small><select name='a' aria-label='Activity'>"
            "<option value='cycling/'>Cycling</option>"
            "<option value='trekking/'>Trekking</option></select></label>"
            "<label><small>Duration</small><select name='d' aria-label='Duration'>"
            "<option value=''>Any length</option><option value='short'>2–4 days</option><option value=''>6–8 days</option></select></label>"
            "<label class='wga-when'><small>When</small><select name='w' aria-label='When'>"
            "<option>Any month</option><option>Spring (Mar–May)</option><option>Summer (Jun–Aug)</option><option>Autumn (Sep–Nov)</option><option>Winter (Dec–Feb)</option></select></label>"
            "<button type='submit'>Find my tour <span aria-hidden='true'>→</span></button>"
            "</form>"
            "</section>")


CSS = """
.wga{position:relative;height:100vh;height:100svh;min-height:680px;max-height:1100px;overflow:hidden;background:#1b1a22;color:#fff;display:flex;align-items:center;justify-content:center;text-align:center}
.wga-bg,.wga-bg img{position:absolute;inset:0;width:100%!important;height:100%!important;max-width:none!important}
.wga-bg img{object-fit:cover;object-position:50% 62%;animation:wgaKB 16s ease-out both}
@keyframes wgaKB{from{transform:scale(1.12)}to{transform:scale(1)}}
.wga:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,15,.55) 0%,rgba(10,10,15,.2) 35%,rgba(10,10,15,.25) 60%,rgba(10,10,15,.7) 100%);pointer-events:none}
.wga-in{position:relative;z-index:2;max-width:980px;padding:40px 24px 120px}
.wga-eb{display:inline-block;padding:9px 18px;border:1px solid rgba(255,255,255,.5);border-radius:999px;font-size:13px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;margin-bottom:24px;backdrop-filter:blur(6px);background:rgba(255,255,255,.06)}
.wga h1{color:#fff!important;font-size:clamp(42px,7vw,96px)!important;line-height:1.02!important;font-weight:800;letter-spacing:-.025em;margin:0 0 22px!important;text-shadow:0 6px 40px rgba(0,0,0,.35)}
.wga h1 span{color:#E77717}
.wga-p{font-size:clamp(16px,1.5vw,20px)!important;color:rgba(255,255,255,.92)!important;max-width:660px;margin:0 auto 34px!important;line-height:1.6}
.wga-ctas{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.wga-in>*{animation:wgaUp 1s cubic-bezier(.2,.7,.2,1) both}
.wga-in>:nth-child(2){animation-delay:.12s}.wga-in>:nth-child(3){animation-delay:.24s}.wga-in>:nth-child(4){animation-delay:.36s}
@keyframes wgaUp{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}
.wga-find{position:absolute;z-index:3;left:50%;bottom:44px;transform:translateX(-50%);display:flex;width:min(900px,92vw);background:#fff;border-radius:18px;box-shadow:0 30px 60px -20px rgba(0,0,0,.55);overflow:hidden;text-align:left;margin:0;animation:wgaUp2 1s .5s cubic-bezier(.2,.7,.2,1) both}
@keyframes wgaUp2{from{opacity:0;transform:translate(-50%,30px)}to{opacity:1;transform:translate(-50%,0)}}
.wga-find label{flex:1;display:block;padding:14px 22px 12px;border-right:1px solid #eee;margin:0;cursor:pointer}
.wga-find small{display:block;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#E77717;font-weight:700;margin-bottom:2px}
.wga-find select{width:100%;border:0!important;background:transparent!important;font-family:inherit;font-weight:600;font-size:15.5px;line-height:1.4;color:#1d2330;padding:0!important;height:auto!important;box-shadow:none!important;outline:0;cursor:pointer;-webkit-appearance:none;appearance:none}
.wga-find button{flex:none;border:0;background:#E77717;color:#fff;font-family:inherit;font-weight:700;font-size:16px;padding:0 32px;cursor:pointer;transition:background .2s;border-radius:0}
.wga-find button:hover{background:#c9620c}
@media (max-width:1024px){.wga{height:calc(100vh - 64px);height:calc(100svh - 64px);min-height:620px;max-height:none}}
@media (max-width:767px){
.wga{align-items:flex-start;min-height:640px}
.wga-in{padding:56px 18px 0}
.wga h1{font-size:40px!important}
.wga-p{font-size:15.5px!important;margin-bottom:24px!important}
.wga-ctas .wgm-btn{width:100%;justify-content:center}
.wga-find{flex-wrap:wrap;bottom:18px;border-radius:16px}
.wga-find label{flex:1 1 50%;padding:11px 14px}.wga-find .wga-when{display:none}
.wga-find button{flex:1 1 100%;padding:15px}
}
@media (max-height:700px) and (min-width:768px){.wga-in{padding-bottom:140px}.wga h1{font-size:64px!important}}
/* stats band under the hero */
.wgm-stats{padding:34px 0 10px!important}
.wgm-stats-in b span{font-size:inherit!important;color:inherit!important}
/* header overlay on the homepage (desktop header only) */
@media (min-width:1025px){
body.home .header-builder-frontend .header-builder-inner{position:absolute!important;top:0;left:0;right:0;width:100%}
body.home .gv-sticky-wrapper:not(.is-fixed)>.elementor-section{background:transparent!important;box-shadow:none!important}
body.home .header-builder-inner{background:linear-gradient(180deg,rgba(10,10,16,.6),rgba(10,10,16,0))}
}
@media (prefers-reduced-motion:reduce){.wga-bg img,.wga-in>*,.wga-find{animation:none}}
"""

JS = ("<script>(function(){var f=document.querySelector('.wga-find');if(!f)return;f.addEventListener('submit',function(e){e.preventDefault();"
      "var a=f.querySelector('[name=a]').value,d=f.querySelector('[name=d]').value;"
      "if(a==='trekking/'&&d==='short'){a='trip/classic-toubkal-mountain-trek/'}"
      "window.location.href='https://wegravelmorocco.com/'+a})})();</script>")
