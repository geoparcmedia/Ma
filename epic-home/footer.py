"""Epic Travel Morocco – site-wide footer + header (Elementor footer templates).

python3 footer.py -> footer-3433.json (main footer template: new footer, and the new header on every page)
                     copyright-3436.json (copyright bar template)
                     preview-inner.html (an inner page with the global header and footer)
The home page (build.py) has its own header; this script adds the same header on all other pages.
"""
import json, os, hashlib
import build as B  # reuses texts, icons, colours and the zellij script (build.py also rebuilds the home page)

HERE = os.path.dirname(os.path.abspath(__file__))
SITE, U, ic = B.SITE, B.U, B.ic
FB = 'https://web.facebook.com/epictravelmorocco'
IG = 'https://www.instagram.com/epictravelmorocco/'
TA = 'https://www.tripadvisor.com/Attraction_Review-g293734-d25394757-Reviews-Epic_Travel_Morocco-Marrakech_Marrakech_Safi.html'

SOC = {
    'fb': '<path fill="currentColor" stroke="none" d="M13.5 21v-7.5H16l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21z"/>',
    'ig': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".9" fill="currentColor" stroke="none"/>',
    'ta': '<circle cx="7.5" cy="13" r="3.2"/><circle cx="16.5" cy="13" r="3.2"/><circle cx="7.5" cy="13" r=".9" fill="currentColor"/><circle cx="16.5" cy="13" r=".9" fill="currentColor"/><path d="M3 8.5h18M4.3 8.5 3 7M19.7 8.5 21 7M12 8.5c-1.5-1.4-3.4-2-6-2M12 8.5c1.5-1.4 3.4-2 6-2M12 16.5l-1.2-1.8M12 16.5l1.2-1.8"/>',
}


def soc(n):
    return '<svg class="etm-i" viewBox="0 0 24 24" aria-hidden="true">' + SOC[n] + '</svg>'


CSS = """
.etf{--teal:#5c828f;--sand:#d1a47b;--sand2:#b98a5e;--ink:#05181f;--fh:'Marcellus',Georgia,serif;--fb:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;
 font-family:var(--fb);color:rgba(255,255,255,.75);background:var(--ink);font-size:15.5px;line-height:1.7}
.etf *,.etf *:before,.etf *:after{box-sizing:border-box}
.etf a{color:rgba(255,255,255,.8)!important;text-decoration:none!important;transition:color .2s}
.etf a:hover{color:var(--sand)!important}
.etf-band{height:10px;background:var(--zb);background-size:10px 10px}
.etf-wrap{max-width:1240px;margin:0 auto;padding:0 24px}
.etf-grid{display:grid;grid-template-columns:1.3fr 1fr 1.1fr 1.3fr;gap:40px;padding:70px 0 50px}
.etf-logo img{max-height:70px;width:auto;margin-bottom:18px}
.etf-logo span{font:400 26px/1 var(--fh);color:#fff}
.etf p{margin:0 0 16px;max-width:320px}
.etf h4{margin:0 0 18px;font:400 21px/1.2 var(--fh);color:#fff;letter-spacing:.02em}
.etf h4:after{content:'';display:block;width:34px;height:2px;margin-top:12px;background:var(--sand)}
.etf ul{list-style:none;margin:0;padding:0}
.etf li{margin:0 0 10px}
.etf li:before{display:none}
.etf-soc{display:flex;gap:10px}
.etf-soc a{display:grid;place-items:center;width:42px;height:42px;border-radius:50%;border:1px solid rgba(255,255,255,.2)}
.etf-soc a:hover{border-color:var(--sand);background:rgba(209,164,123,.12)}
.etf-i{display:flex;gap:12px;align-items:flex-start;margin-bottom:14px}
.etf .etm-i{width:20px;height:20px;flex:none;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.etf-i .etm-i{color:var(--sand);margin-top:3px}
.etf-news-in{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;padding-top:30px;border-top:1px solid rgba(255,255,255,.1)}
.etf-news-in h4{margin:0}
.etf-news-in h4:after{display:none}
.etf-news-in p{margin:4px 0 0;max-width:none;font-size:14.5px}
.etf-news-form{background:#05181f;padding:14px 24px 44px}
.etf-news-form .elementor-widget-container,.etf-news-form .elementor-shortcode{max-width:1192px;margin:0 auto}
.etf-news-form form{display:flex;gap:8px;flex-wrap:wrap;margin:0;max-width:480px}
.etf-news-form form p{margin:0;flex:1;min-width:0}
.etf-news-form br{display:none}
.etf-news-form input[type=email],.etf-news-form input[type=text]{width:100%;height:48px;padding:0 18px;border-radius:999px;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.06);color:#fff;font:400 15px system-ui}
.etf-news-form input[type=submit],.etf-news-form button{height:48px;padding:0 24px;border:0;border-radius:999px;background:#d1a47b;color:#05181f;font:600 15px system-ui;cursor:pointer}
.etf-news-form .wpcf7-response-output{color:#fff;flex-basis:100%}
.etf-news-form .wpcf7-spinner{display:none}
.etf-bottom{border-top:1px solid rgba(255,255,255,.1)}
.etf-bottom .etf-wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:22px 24px;font-size:14px;color:rgba(255,255,255,.6)}
@media (max-width:1024px){.etf-grid{grid-template-columns:1fr 1fr}}
@media (max-width:760px){.etf-news-in{flex-direction:column;align-items:flex-start}.etf-news-form{padding:12px 18px 36px}}
@media (max-width:600px){.etf-grid{grid-template-columns:1fr;gap:34px;padding:56px 0 40px}}
/* spacer under the fixed header on inner pages */
.etm-spacer{height:84px;background:#05181f}
@media (max-width:900px){.etm-spacer{height:70px}}
"""

HEADER_CSS = B.CSS[B.CSS.index('/* header */'):B.CSS.index('.etm-hero ~ *')]
BASE_CSS = """.etm-top,.etm-drawer{--sand:#d1a47b;--ink:#05181f;--fh:'Marcellus',Georgia,serif;--fb:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-family:var(--fb);line-height:1.7}
.etm-top *,.etm-drawer *{box-sizing:border-box}.etm-top a,.etm-drawer a{text-decoration:none!important}
.etm-top .etm-wrap{max-width:1240px;margin:0 auto;padding:0 24px}
.etm-i{width:22px;height:22px;flex:none;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.etm-top .etm-btn,.etm-drawer .etm-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border-radius:999px;background:#d1a47b;color:#05181f!important;font-weight:600;letter-spacing:.04em;transition:transform .2s,background .2s}
.etm-top .etm-btn:hover{background:#e0b88f;transform:translateY(-2px)}"""

TOURS = [('Sahara Desert Experience', 'sahara-desert-experience'), ('Majestic Kasbah & Desert', 'majestic-kasbah-and-desert-adventure'),
         ('Highlights of Morocco', 'highlights-of-morocco'), ('The Magic of Morocco', 'the-magic-of-morocco'),
         ('Moroccan Odyssey', 'moroccan-odyssey-15-day-grand-tour')]


def header_markup():
    menu = ''.join('<a href="%s">%s</a>' % (u, t) for t, u in B.NAV)
    return ('<header class="etm etm-top solid" id="etm-top"><div class="etm-wrap etm-top-in">'
            '<a class="etm-logo" href="' + SITE + '/" aria-label="Epic Travel Morocco"><img src="' + B.LOGO + '" alt="Epic Travel Morocco"></a>'
            '<nav class="etm-menu" aria-label="Main menu">' + menu + '</nav>'
            '<div class="etm-top-cta"><a class="etm-top-tel" href="tel:' + B.PHONE1 + '">' + ic('phone') + B.PHONE1_T + '</a>'
            '<a class="etm-btn" href="' + SITE + '/contact-2/">Plan my trip</a></div>'
            '<button class="etm-burger" type="button" aria-expanded="false" aria-controls="etm-drawer" aria-label="Menu"><span></span><span></span></button>'
            '</div></header>'
            '<div class="etm etm-drawer" id="etm-drawer">' + ''.join('<a href="%s">%s</a>' % (u, t) for t, u in B.NAV) +
            '<a class="etm-btn" href="' + SITE + '/contact-2/">Plan my trip</a>'
            '<a class="etm-top-tel" href="tel:' + B.PHONE1 + '">' + ic('phone') + B.PHONE1_T + '</a></div>')


# the header lives in a <template> and is only used on pages that do not already have one (the home page does)
JS = """<script>(function(){var d=document,W=window;function ready(f){if(d.readyState!=='loading')f();else d.addEventListener('DOMContentLoaded',f)}
ready(function(){if(d.querySelector('.etm-hero')||d.getElementById('etm-top'))return;var t=d.getElementById('etm-header-tpl');if(!t)return;
var box=d.createElement('div');box.innerHTML=t.innerHTML;var top=box.querySelector('.etm-top'),dr=box.querySelector('.etm-drawer'),bg=top.querySelector('.etm-burger');
var sp=d.createElement('div');sp.className='etm-spacer';d.body.insertBefore(sp,d.body.firstChild);d.body.appendChild(top);d.body.appendChild(dr);
var path=location.pathname.replace(/[/]+$/,'')||'/';top.querySelectorAll('.etm-menu a').forEach(function(a){var p=a.pathname.replace(/[/]+$/,'')||'/';if(p===path)a.classList.add('cur')});
bg.addEventListener('click',function(){var o=!dr.classList.contains('open');dr.classList.toggle('open',o);bg.setAttribute('aria-expanded',o);d.documentElement.style.overflow=o?'hidden':''});
dr.addEventListener('click',function(e){if(e.target.closest('a')){dr.classList.remove('open');bg.setAttribute('aria-expanded','false');d.documentElement.style.overflow=''}});
var hide=function(){var cand=[].slice.call(d.querySelectorAll('header,nav,div,section')).filter(function(el){
if(el===top||top.contains(el)||el===dr||dr.contains(el)||el===sp||el.closest('.etm,.etf')||el.querySelector('.etm,.etf,footer')||el.closest('footer')||el.closest('.elementor-location-footer'))return false;
var rc=el.getBoundingClientRect();if(rc.top+W.pageYOffset>320)return false;
return el.querySelector('a[href*=destination]')&&el.querySelector('a[href*=contact],a[href*=about]')});
cand.filter(function(el){return !cand.some(function(o){return o!==el&&o.contains(el)})}).forEach(function(el){el.style.setProperty('display','none','important')})};
hide();W.addEventListener('load',hide)});})();</script>""".replace('\n', '')


def footer_html():
    links = ''.join('<li><a href="%s">%s</a></li>' % (u, t) for t, u in B.NAV)
    tours = ''.join('<li><a href="%s/all-tour/%s/">%s</a></li>' % (SITE, s, t) for t, s in TOURS)
    return (B.FONTS + '<style>' + ' '.join((BASE_CSS + HEADER_CSS + CSS).split()) + '</style><script>' + B.ZJS + '</script>'
            '<template id="etm-header-tpl">' + header_markup() + '</template>'
            '<footer class="etf" role="contentinfo"><div class="etf-band"></div><div class="etf-wrap"><div class="etf-grid">'
            '<div><a class="etf-logo" href="' + SITE + '/"><img src="' + B.LOGO + '" alt="Epic Travel Morocco"></a>'
            '<p>Private tours across Morocco with local guides, from Marrakech to the Sahara, the Atlas and the imperial cities.</p>'
            '<div class="etf-soc"><a href="' + FB + '" target="_blank" rel="noopener" aria-label="Facebook">' + soc('fb') + '</a>'
            '<a href="' + IG + '" target="_blank" rel="noopener" aria-label="Instagram">' + soc('ig') + '</a>'
            '<a href="' + TA + '" target="_blank" rel="noopener" aria-label="Tripadvisor">' + soc('ta') + '</a></div></div>'
            '<div><h4>Quick links</h4><ul>' + links + '</ul></div>'
            '<div><h4>Popular tours</h4><ul>' + tours + '<li><a href="' + SITE + '/destination/">All tours →</a></li></ul></div>'
            '<div><h4>Say hello</h4>'
            '<div class="etf-i">' + ic('mail') + '<a href="mailto:' + B.EMAIL + '">' + B.EMAIL + '</a></div>'
            '<div class="etf-i">' + ic('phone') + '<div><a href="tel:' + B.PHONE1 + '">' + B.PHONE1_T + '</a><br><a href="tel:' + B.PHONE2 + '">' + B.PHONE2_T + '</a></div></div>'
            '<div class="etf-i">' + ic('map') + '<span>Gueliz, Marrakech 22000, Morocco</span></div></div>'
            '</div><div class="etf-news-in"><div><h4>Subscribe to our newsletter</h4><p>Travel ideas and new tours, once in a while.</p></div></div>'
            '</div></footer>' + JS)


def copyright_html():
    return ('<div class="etf"><div class="etf-bottom"><div class="etf-wrap"><span>© 2025 Epic Travel Morocco. All rights reserved.</span>'
            '<span>Private tours from Marrakech</span></div></div></div>')


def noq(h):
    h = h.replace('"', "'")
    assert '"' not in h and '\\' not in h
    return h


def eid(s):
    return hashlib.md5(s.encode()).hexdigest()[:7]


def doc(widgets, key):
    els = []
    for k, (t, c, extra) in enumerate(widgets):
        st = {'html': c} if t == 'html' else {'shortcode': c}
        st.update(extra)
        els.append({'id': eid('%s%d' % (key, k)), 'elType': 'widget', 'settings': st, 'elements': [], 'widgetType': t})
    return [{'id': eid(key), 'elType': 'container',
             'settings': {'content_width': 'full', 'flex_direction': 'column', 'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0'},
                          'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}},
             'elements': els, 'isInner': False}]


main = doc([('html', noq(footer_html()), {}),
            ('shortcode', "[contact-form-7 id='a4499c9' title='footer email']", {'_css_classes': 'etf-news-form'})], 'etf-main')
copy = doc([('html', noq(copyright_html()), {})], 'etf-copy')
for name, d in (('footer-3433.json', main), ('copyright-3436.json', copy)):
    s = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s, name
    open(os.path.join(HERE, name), 'w').write(s)
    print(name, len(s))

# preview: a fake inner page with an old theme header, content, then the footer templates
fake = ('<header class="theme-header" style="background:#fff;padding:24px;font:16px sans-serif"><b>OLD HEADER</b> '
        '<a href="/destination/">Destination</a> <a href="/contact-2/">Contact</a></header>'
        '<div style="padding:90px 24px;background:#f4efe6;font:18px sans-serif"><h1 style="font:40px Georgia">About us</h1><p>Page content…</p></div>')
news = ('<div class="elementor-element etf-news-form"><div class="elementor-widget-container"><form><p><input type="email" placeholder="Your email"></p>'
        '<p><input type="submit" value="Subscribe"></p></form></div></div>')
page = ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'
        + fake + main[0]['elements'][0]['settings']['html'] + news + copy[0]['elements'][0]['settings']['html'] + '</body></html>')
open(os.path.join(HERE, 'preview-inner.html'), 'w').write(page)
