import json, hashlib, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from images import IMG, LOGO, B
from tours_a import TOURS_A
from tours_b import TOURS_B
from tours_c import TOURS_C
from tours_d import TOURS_D
from tours_e import TOURS_E

SITE = 'https://epictravelmorocco.com'
TOURS = TOURS_A + TOURS_B + TOURS_C + TOURS_D + TOURS_E
BY_ID = {t['id']: t for t in TOURS}
# tour id -> image key
TIMG = {3353: 'sahara-exp', 3403: 'north-south', 3400: 'midelt', 3396: 'coast-desert', 3393: 'dunes-camel',
        3390: 'marrakech', 3362: 'historic', 3361: 'chefchaouen-trip', 3359: 'ifrane', 3351: 'magic',
        3346: 'odyssey', 3341: 'journey', 3339: 'kasbah', 3338: 'north', 3331: 'authentic'}
# filter groups used by the tours page
GROUP = {3353: 'desert short', 3393: 'desert short', 3339: 'desert short', 3396: 'desert coast',
         3390: 'city coast', 3362: 'imperial', 3338: 'imperial north', 3361: 'north desert', 3341: 'imperial desert short',
         3359: 'imperial desert', 3351: 'imperial desert', 3403: 'grand north desert coast', 3400: 'grand north desert',
         3331: 'grand imperial desert', 3346: 'grand north desert coast'}

PHONE_MA = '+212 661 292 596'
PHONE_CA = '+1 579 484 7707'
WA = 'https://wa.me/212661292596'
EMAIL = 'epictravelmorocco@gmail.com'
FB = 'https://web.facebook.com/epictravelmorocco'
IG = 'https://www.instagram.com/epictravelmorocco/'
TA = 'https://www.tripadvisor.com/Attraction_Review-g293734-d25394757-Reviews-Epic_Travel_Morocco-Marrakech_Marrakech_Safi.html'

def turl(t):
    return SITE + '/all-tour/' + t['url'] + '/'

ICON_SRC = {
 'wa': "<svg viewBox='0 0 24 24' fill='currentColor' aria-hidden='true'><path d='M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.8 2.3 1 2.5c.1.2 1.6 2.5 4 3.5 1.5.6 2 .7 2.8.6.4-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.4-.2z'/></svg>",
 'mail': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true'><rect x='3' y='5' width='18' height='14' rx='2'/><path d='m3 7 9 6 9-6'/></svg>",
 'phone': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true'><path d='M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z'/></svg>",
 'pin': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true'><path d='M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z'/><circle cx='12' cy='10' r='3'/></svg>",
 'arrow': "<svg viewBox='0 0 24 24' width='16' height='16' fill='none' stroke='currentColor' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true'><path d='M5 12h14M13 6l6 6-6 6'/></svg>",
 'star': "<svg viewBox='0 0 24 24' fill='currentColor' aria-hidden='true'><path d='M12 1l3.2 4.4 5.3-.9-.9 5.3L24 12l-4.4 3.2.9 5.3-5.3-.9L12 23l-3.2-4.4-5.3.9.9-5.3L0 12l4.4-3.2-.9-5.3 5.3.9z'/></svg>",
 'users': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' aria-hidden='true'><path d='M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2'/><circle cx='9' cy='7' r='4'/><path d='M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8'/></svg>",
 'info': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' aria-hidden='true'><circle cx='12' cy='12' r='10'/><path d='M12 16v-4M12 8h.01'/></svg>",
 'fb': "<svg viewBox='0 0 24 24' fill='currentColor' aria-hidden='true'><path d='M14 8h3V4h-3a4 4 0 0 0-4 4v2H8v4h2v8h4v-8h3l1-4h-4V8z'/></svg>",
 'ig': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' aria-hidden='true'><rect x='3' y='3' width='18' height='18' rx='5'/><circle cx='12' cy='12' r='4'/><circle cx='17.5' cy='6.5' r='1' fill='currentColor'/></svg>",
 'ta': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' aria-hidden='true'><circle cx='7' cy='13' r='4'/><circle cx='17' cy='13' r='4'/><circle cx='7' cy='13' r='1' fill='currentColor'/><circle cx='17' cy='13' r='1' fill='currentColor'/><path d='M3 8.5C5.5 6.5 8.6 5.5 12 5.5s6.5 1 9 3M12 5.5 12 8'/></svg>",
}

import re as _re
def _sym(k, svg):
    attrs = _re.match(r"<svg ([^>]*)>", svg).group(1)
    attrs = _re.sub(r"\s(aria-hidden|width|height)='[^']*'", '', ' ' + attrs).strip()
    inner = svg[svg.index('>') + 1:-6]
    return "<symbol id='et-i-" + k + "' " + attrs + ">" + inner + "</symbol>"
SPRITE = "<svg width='0' height='0' style='position:absolute' aria-hidden='true'>" + ''.join(_sym(k, v) for k, v in ICON_SRC.items()) + "</svg>"
ICON = {k: "<svg aria-hidden='true'" + (" width='16' height='16'" if k == 'arrow' else '') + "><use href='#et-i-" + k + "'/></svg>" for k in ICON_SRC}
ORN = "<div class='et-orn'>" + ICON['star'] + "</div>"

NAV = [('Home', SITE + '/'), ('Tours', SITE + '/destination/'), ('Our Fleet', SITE + '/fleet/'),
       ('About Us', SITE + '/about-us/'), ('Contact', SITE + '/contact-2/')]

def logo():
    return ("<a class='et-logo' href='" + SITE + "/' aria-label='Epic Travel Morocco – home'><img src='" + LOGO +
            "' width='63' height='48' alt='Epic Travel Morocco logo'><b>Epic Travel<small>Morocco</small></b></a>")

def header():
    links = ''.join("<a href='" + u + "'>" + n + "</a>" for n, u in NAV)
    return (SPRITE + "<header class='et et-h' id='et-h'><div class='et-band'></div><div class='et-h-in'>" + logo() +
            "<nav class='et-nav' aria-label='Main menu'>" + links + "</nav>"
            "<div class='et-h-cta'><a class='et-btn et-btn-wa' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "WhatsApp</a>"
            "<button type='button' class='et-burger' aria-label='Open menu' aria-expanded='false'><i></i><i></i><i></i></button></div></div>"
            "<div class='et-ov'></div><div class='et-panel' role='dialog' aria-label='Menu'><button type='button' class='et-x' aria-label='Close menu'>×</button>"
            + logo().replace("class='et-logo'", "class='et-logo' style='align-self:flex-start;box-shadow:none'") +
            "<nav>" + links + "</nav>"
            "<a class='et-btn et-btn-wa' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "WhatsApp " + PHONE_MA + "</a>"
            "<a class='et-btn et-btn-o' href='mailto:" + EMAIL + "'>" + ICON['mail'] + "Email us</a></div></header>")

JS = ("<script>window.etF=function(i){var o=i.getAttribute('data-o');if(o&&i.src!==o){i.removeAttribute('data-o');var p=i.parentNode;if(p&&p.tagName==='PICTURE')p.querySelectorAll('source').forEach(function(x){x.remove()});i.src=o}};(function(){var d=document,h=d.getElementById('et-h');if(!h)return;d.documentElement.classList.add('et-js');"
      "var p=location.pathname.replace(/[/]+$/,'')||'/';h.querySelectorAll('a').forEach(function(a){try{var q=new URL(a.href).pathname.replace(/[/]+$/,'')||'/';if(q===p&&!a.classList.contains('et-btn'))a.classList.add('on')}catch(e){}});"
      "var s=function(){h.classList.toggle('sc',scrollY>40||d.body.classList.contains('et-solid'))};s();addEventListener('scroll',s,{passive:true});"
      "var b=h.querySelector('.et-burger'),o=function(v){h.classList.toggle('et-open',v);b.setAttribute('aria-expanded',v);d.body.style.overflow=v?'hidden':''};"
      "b.addEventListener('click',function(){o(true)});h.querySelector('.et-x').addEventListener('click',function(){o(false)});h.querySelector('.et-ov').addEventListener('click',function(){o(false)});"
      "addEventListener('keydown',function(e){if(e.key==='Escape')o(false)});"
      "var r=d.querySelectorAll('.et-rv');if(!('IntersectionObserver' in window)){r.forEach(function(e){e.classList.add('in')});return}"
      "var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});"
      "r.forEach(function(e){io.observe(e)});setTimeout(function(){r.forEach(function(e){e.classList.add('in')})},4000)})();</script>")

def footer():
    tours = ''.join("<li><a href='" + turl(BY_ID[i]) + "'>" + BY_ID[i]['name'] + "</a></li>" for i in (3353, 3339, 3359, 3351, 3331, 3346))
    links = ''.join("<li><a href='" + u + "'>" + n + "</a></li>" for n, u in NAV)
    return ("<footer class='et et-f et-dark'><div class='et-wrap'><div class='et-f-g'>"
            "<div>" + logo() + "<p>Private tours and transport across Morocco – imperial cities, Atlas Mountains, Sahara dunes and the Atlantic coast, with local drivers and guides who know every road.</p>"
            "<div class='et-soc'><a href='" + FB + "' target='_blank' rel='noopener' aria-label='Facebook'>" + ICON['fb'] + "</a>"
            "<a href='" + IG + "' target='_blank' rel='noopener' aria-label='Instagram'>" + ICON['ig'] + "</a>"
            "<a href='" + TA + "' target='_blank' rel='noopener' aria-label='Tripadvisor'>" + ICON['ta'] + "</a></div></div>"
            "<div><h4>Popular tours</h4><ul>" + tours + "</ul></div>"
            "<div><h4>Quick links</h4><ul>" + links + "</ul></div>"
            "<div><h4>Say hello</h4><ul><li><a href='mailto:" + EMAIL + "'>" + EMAIL + "</a></li>"
            "<li><a href='tel:+212661292596'>" + PHONE_MA + " (WhatsApp)</a></li><li><a href='tel:+15794847707'>" + PHONE_CA + "</a></li>"
            "<li>Gueliz, Marrakech 22000, Morocco</li></ul>"
            "<a class='et-btn et-btn-wa' style='margin-top:20px' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "Chat on WhatsApp</a></div>"
            "</div><div class='et-f-b'><span>© 2025 Epic Travel Morocco. All rights reserved.</span>"
            "<span><a href='" + SITE + "/terms-and-conditions/'>Terms &amp; Conditions</a></span></div></div><div class='et-band'></div></footer>")

ROUTE = {
 3353: ['Marrakech', 'Tizi n’Tichka', 'Ouarzazate', 'Dades Gorges', 'Todra Gorges', 'Merzouga', 'Rissani', 'Draa Valley', 'Ait Benhaddou'],
 3403: ['Tangier', 'Chefchaouen', 'Volubilis', 'Meknes', 'Fes', 'Midelt', 'Merzouga', 'Todra Gorge', 'Dades Valley', 'Ait Benhaddou', 'Marrakech', 'Essaouira'],
 3400: ['Casablanca', 'Rabat', 'Chefchaouen', 'Volubilis', 'Meknes', 'Fes', 'Ifrane', 'Midelt', 'Merzouga', 'Todra Gorge', 'Dades Valley', 'Ouarzazate', 'Ait Benhaddou', 'Marrakech'],
 3396: ['Marrakech', 'Ait Benhaddou', 'Draa Valley', 'Zagora', 'Erg Chigaga', 'Lac Iriki', 'Taroudant', 'Agadir', 'Essaouira'],
 3393: ['Marrakech', 'Ait Benhaddou', 'Ouarzazate', 'Dades', 'Todra Gorge', 'Erfoud', 'Erg Chebbi', 'Nkob'],
 3390: ['Marrakech', 'Majorelle Garden', 'Anima Garden', 'Essaouira', 'Ourika Valley'],
 3362: ['Casablanca', 'Rabat', 'Meknes', 'Fes', 'Volubilis', 'Moulay Idriss', 'Beni Mellal', 'Marrakech'],
 3361: ['Tangier', 'Chefchaouen', 'Volubilis', 'Fes', 'Ifrane', 'Merzouga', 'Todra Gorge', 'Dades Valley', 'Ait Benhaddou', 'Marrakech'],
 3359: ['Casablanca', 'Rabat', 'Volubilis', 'Fes', 'Ifrane', 'Merzouga', 'Rissani', 'Todra Gorge', 'Dades', 'Ait Benhaddou', 'Marrakech'],
 3351: ['Casablanca', 'Rabat', 'Chefchaouen', 'Volubilis', 'Meknes', 'Fes', 'Ifrane', 'Merzouga', 'Todra Gorge', 'Dades Valley', 'Ait Benhaddou', 'Marrakech'],
 3346: ['Casablanca or Tangier', 'Chefchaouen', 'Volubilis', 'Fes', 'Ifrane', 'Erfoud', 'Merzouga', 'Skoura', 'Ait Benhaddou', 'Telouet', 'Marrakech', 'Essaouira', 'El Jadida'],
 3341: ['Casablanca', 'Rabat', 'Chefchaouen', 'Fes', 'Ifrane', 'Merzouga', 'Dades', 'Ouarzazate', 'Marrakech'],
 3339: ['Marrakech', 'Ouarzazate', 'Roses Valley', 'Dades Gorges', 'Todra Gorges', 'Merzouga', 'Rissani', 'Draa Valley', 'Ait Benhaddou'],
 3338: ['Casablanca', 'Rabat', 'Tangier', 'Chefchaouen', 'Fes', 'Volubilis'],
 3331: ['Casablanca', 'Rabat', 'Fes', 'Volubilis', 'Meknes', 'Merzouga', 'Todra Gorge', 'Dades', 'Ait Benhaddou', 'Marrakech'],
}

def stops(t):
    return ROUTE[t['id']]

def route_short(t):
    s = stops(t)
    return ' · '.join(s[:4]) + (' …' if len(s) > 4 else '')

def img(key, alt, cls='', size='card', lazy=True, w=600, h=810):
    i = IMG[key]
    return ("<img src='" + i[size] + "' width='" + str(w) + "' height='" + str(h) + "' alt='" + alt + "'" +
            (" class='" + cls + "'" if cls else '') + (" loading='lazy'" if lazy else " fetchpriority='high'") +
            " decoding='async' data-o='" + i['orig'] + "' onerror=etF(this)>")

def card(t, extra=''):
    return ("<a class='et-card et-rv' href='" + turl(t) + "'" + extra + "><div class='et-card-img'>" + img(TIMG[t['id']], t['name'] + ' – Morocco tour') +
            "<span class='et-days'><b>" + str(t['days']) + "</b> days · from " + t['start'].split(' or ')[0] + "</span></div>"
            "<div class='et-card-b'><span class='et-kind'>" + t['kind'] + "</span><h3>" + t['name'] + "</h3>"
            "<p class='et-route'>" + route_short(t) + "</p><span class='et-more'>View the program " + ICON['arrow'] + "</span></div></a>")

def hero(key, eyebrow, h1, lead, ctas='', small=True, crumb=''):
    i = IMG[key]
    return ("<section class='et et-hero" + (' et-hero-s' if small else '') + "'><picture><source media='(max-width:700px)' srcset='" + i['card'] + "'>"
            "<img src='" + i['wide'] + "' alt='' fetchpriority='high' decoding='async' data-o='" + i['orig'] + "' onerror=etF(this)></picture>"
            "<span class='et-arch-o'></span><div class='et-wrap'>" + crumb + "<span class='et-eye'>" + eyebrow + "</span><h1>" + h1 + "</h1>"
            + ("<p class='lead'>" + lead + "</p>" if lead else '') + (("<div class='et-ctas'>" + ctas + "</div>") if ctas else '') + "</div></section>")

def cta(title, text):
    return ("<section class='et et-sec' style='padding-top:0'><div class='et-wrap'><div class='et-cta et-dark et-rv'><div><span class='et-eye'>Tailor-made</span><h2>" + title + "</h2><p>" + text + "</p></div>"
            "<div class='et-ctas'><a class='et-btn et-btn-wa' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "WhatsApp us</a>"
            "<a class='et-btn et-btn-w' href='" + SITE + "/contact-2/'>Send a request</a></div></div></div></section>")

def jsval(v):
    if isinstance(v, dict):
        return '{' + ','.join(jsval(k) + ':' + jsval(x) for k, x in v.items()) + '}'
    if isinstance(v, list):
        return '[' + ','.join(jsval(x) for x in v) + ']'
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    assert "'" not in s and '\\' not in s and '"' not in s, s
    return "'" + s + "'"

def ldjs(objs):
    return ("<script>(function(){[" + ','.join(jsval(o) for o in objs) + "].forEach(function(o){var s=document.createElement('script');"
            "s.type='application/ld+json';s.text=JSON.stringify(o);document.head.appendChild(s);});})();</script>")

def clean(html):
    html = re.sub(r'\s*\n\s*', ' ', html)
    assert '"' not in html and '\\' not in html, html[max(0, html.find('"') - 80):html.find('"') + 80]
    return html

def elementor(widgets, seed):
    h = lambda s: hashlib.md5((seed + s).encode()).hexdigest()[:7]
    els = []
    for i, (t, c) in enumerate(widgets):
        st = {'html': c} if t == 'html' else {'shortcode': c}
        els.append({"id": h('w%d' % i), "elType": "widget", "settings": st, "elements": [], "widgetType": t})
    z = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
    data = [{"id": h('c'), "elType": "container", "settings": {"content_width": "full", "flex_direction": "column", "padding": z, "margin": z,
             "flex_gap": {"unit": "px", "size": 0, "column": "0", "row": "0", "isLinked": True}}, "elements": els, "isInner": False}]
    out = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in out, [m.start() for m in re.finditer(r'\\\\', out)][:5]
    return out
