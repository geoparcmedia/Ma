import json, re, hashlib, sys
sys.path.insert(0,'.')
from tours import CYCLING, TREKKING, card
from anim2 import add_bikes, SPRITE
U='https://wegravelmorocco.com/wp-content/uploads/2025/10/'
BASE=open('style.html').read().replace('<style>','').replace('</style>','')
CSS=BASE+"""
.wgp-hero{position:relative;min-height:62vh;display:flex;align-items:flex-end;color:#fff;overflow:hidden;background:#1b1a22}
.wgp-hero>img{position:absolute;inset:0;width:100%!important;height:100%!important;max-width:none!important;object-fit:cover}
.wgp-hero:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,10,15,.25),rgba(10,10,15,.75))}
.wgp-hero .wgm-wrap{position:relative;z-index:2;width:100%;padding-top:120px;padding-bottom:56px}
.wgp-hero h1{color:#fff!important;font-size:clamp(34px,5vw,62px)!important;line-height:1.08!important;margin:0 0 16px!important;max-width:820px}
.wgp-hero p{color:rgba(255,255,255,.9)!important;max-width:720px;font-size:clamp(16px,1.4vw,18.5px);margin:0!important}
.wgp-hero .wgm-eyebrow{color:#ffb56b}
.wgp-count{display:inline-block;margin-top:22px;padding:8px 16px;border-radius:999px;background:rgba(255,255,255,.12);backdrop-filter:blur(6px);font-size:14px;font-weight:600}
.wgp-list{padding:64px 0 30px}
.wgp-cta{background:var(--ink2);color:#fff;padding:64px 0;text-align:center}
.wgp-cta h2{color:#fff!important}.wgp-cta p{color:rgba(255,255,255,.8)!important;max-width:620px;margin:0 auto 26px!important}
.wgp-cta .wgm-ctas{justify-content:center}
.wgp-wa{background:#25D366;color:#fff!important}.wgp-wa:hover{background:#1ebe5a}
.wgm-js .wgm-rv{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s ease}.wgm-js .wgm-rv.in{opacity:1;transform:none}
.wgm-card-img img{transition:transform .8s cubic-bezier(.2,.7,.2,1)}.wgm-card:hover .wgm-card-img img{transform:scale(1.06)}
.wgm-btn{position:relative;overflow:hidden}.wgm-bk{position:absolute;left:14px;top:50%;width:30px;margin-top:-10px;opacity:0;transform:translateX(-60px);transition:transform .45s cubic-bezier(.2,.7,.2,1),opacity .3s;display:block;line-height:0}.wgm-bk svg{width:30px;height:20px}.wgm-btn:hover{padding-left:54px}.wgm-btn:hover .wgm-bk{opacity:1;transform:none}
@media (max-width:767px){.wgp-hero{min-height:52vh}.wgp-hero .wgm-wrap{padding-top:90px;padding-bottom:36px}.wgp-list{padding:40px 0 10px}.wgm-bk{display:none}.wgm-btn:hover{padding-left:28px}}
@media (prefers-reduced-motion:reduce){.wgm-js .wgm-rv{opacity:1;transform:none;transition:none}}
"""
JS=("<script>(function(){var d=document;var r=d.querySelectorAll('.wgm-rv');"
    "if(!('IntersectionObserver' in window)){r.forEach(function(e){e.classList.add('in')});return}"
    "var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');o.unobserve(e.target)}})},{rootMargin:'0px 0px -6% 0px'});"
    "r.forEach(function(e){o.observe(e)});setTimeout(function(){r.forEach(function(e){e.classList.add('in')})},3500)})();</script>")
CTA=("<section class='wgp-cta'><div class='wgm-wrap'><h2>Not sure which tour to choose?</h2>"
     "<p>Tell us your dates, level and ideas – our local team will suggest the best route or build a private tour for you. We reply within 24 hours.</p>"
     "<div class='wgm-ctas'><a class='wgm-btn wgp-wa' href='https://wa.me/212660435569' target='_blank' rel='noopener'>WhatsApp +212 660 435 569</a>"
     "<a class='wgm-btn wgm-btn-o' href='https://wegravelmorocco.com/contact-us/'>Contact Us</a></div></div></section>")

def page(hero_img, hero_alt, eyebrow, h1, intro, count, tours, extra='', grid='wgm-grid'):
    cards=''.join(card(*c) for c in tours)
    body=("<section class='wgp-hero'><img src='"+hero_img+"' alt='"+hero_alt+"' fetchpriority='high' decoding='async'>"
          "<div class='wgm-wrap'><span class='wgm-eyebrow'>"+eyebrow+"</span><h1>"+h1+"</h1><p>"+intro+"</p><span class='wgp-count'>"+count+"</span></div></section>"
          "<section class='wgp-list'><div class='wgm-wrap'><div class='"+grid+"'>"+cards+"</div>"+extra+"</div></section>"+CTA)
    html="<style>"+CSS+"</style><script>document.documentElement.classList.add('wgm-js')</script>"+SPRITE+"<div class='wgm'>"+body+"</div>"+JS
    html=html.replace('\n',' ')
    html=re.sub(r'="([^"\']*)"', lambda m:"='"+m.group(1)+"'", html)
    html=add_bikes(html)
    for cls in ['wgm-card','wgm-custom']:
        html=re.sub(r"class='(%s)'"%cls, r"class='\1 wgm-rv'", html)
    return html

def elementor(html, seed):
    h=lambda s:hashlib.md5((seed+s).encode()).hexdigest()[:7]
    data=[{"id":h('s'),"elType":"section","settings":{"layout":"full_width","stretch_section":"section-stretched","gap":"no","padding":{"unit":"px","top":"0","right":"0","bottom":"0","left":"0","isLinked":True}},
           "elements":[{"id":h('c'),"elType":"column","settings":{"_column_size":100,"_inline_size":None,"padding":{"unit":"px","top":"0","right":"0","bottom":"0","left":"0","isLinked":True}},
           "elements":[{"id":h('w'),"elType":"widget","settings":{"html":html},"elements":[],"widgetType":"html"}],"isInner":False}],"isInner":False}]
    return json.dumps(data,ensure_ascii=False,separators=(',',':'))

custom=("<a class='wgm-custom' href='https://wegravelmorocco.com/contact-us/'><img src='"+U+"atlas-p-580x450.png' width='580' height='450' alt='Mountain bike tour in the Atlas Mountains of Morocco' loading='lazy' decoding='async'>"
        "<div><span class='wgm-tag'>On request · 7 days · from 800 €</span><h3>Morocco Mountain Bike Tour</h3><p>A private mountain bike adventure in the High Atlas, or any custom route you dream of – any length, any level. We build the tour around your pace and dates.</p>"
        "<span class='wgm-btn wgm-btn-o'>Ask Us for a Custom Tour</span></div></a>")
cyc=page(U+'5431730073238630289-1024x683.jpg','Guided cycling tour in the Atlas Mountains of Morocco','Bike in Morocco',
         'Explore Cycling Adventures in the Atlas Mountains',
         'Discover the best cycling in Morocco with We Gravel Morocco. Our guided bike tours take you through breathtaking landscapes, from the rugged Atlas Mountains to the Sahara Desert. Whether you’re a beginner or an experienced cyclist, we offer tailored adventures that combine exploration, culture and unforgettable experiences.',
         '5 cycling &amp; gravel bike tours', CYCLING, custom, 'wgm-grid wgm-grid4')
trk=page(U+'pianchette-top-7989881_1920-1024x768.jpg','Trekking in the High Atlas Mountains of Morocco','We Gravel Morocco',
         'Your Gateway to Trekking Adventures in Morocco',
         'Trekking in Morocco is more than just walking – it’s an immersive journey through ancient Berber villages, panoramic mountain passes and hidden oasis trails. Join our local mountain guides to hike scenic routes, enjoy local hospitality and experience Morocco like never before.',
         '6 guided treks', TREKKING)
for name,html,seed in [('cycling',cyc,'cyc'),('trekking',trk,'trk')]:
    out=elementor(html,seed)
    open(name+'_elementor.json','w').write(out)
    print(name, len(out), out.count('\\'), out.count('"'))
    prev=re.sub(r"https://wegravelmorocco\.com/wp-content/uploads/[^\"' ,]+","https://ph.local/x",html)
    open(name+'_prev.html','w').write("<!doctype html><html><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><style>body{margin:0;font-family:Arial,sans-serif}</style></head><body><div style='height:86px;background:#313041'></div>"+prev+"</body></html>")
