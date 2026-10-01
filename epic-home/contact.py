"""Epic Travel Morocco – Contact page (ID 1360, /contact-2/), same style as the home page.

python3 contact.py -> contact-1360.json (value of _elementor_data) and preview-contact.html
Header and footer come from the site-wide footer template (footer.py).
"""
import json, os, hashlib
import build as B

HERE = os.path.dirname(os.path.abspath(__file__))
SITE, U, ic = B.SITE, B.U, B.ic
FORM = "[contact-form-7 id='f402750' title='Main Contact']"
MAP = 'https://maps.google.com/maps?q=Gueliz%2C%20Marrakech%2C%20Morocco&z=14&output=embed'

CSS = """
.etc{--teal:#5c828f;--sand:#d1a47b;--sand2:#b98a5e;--ink:#05181f;--cream:#fff9f0;--mut:#5e6b70;
 --fh:'Marcellus',Georgia,serif;--fb:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;font-family:var(--fb);color:var(--ink);font-size:17px;line-height:1.7}
.etc *,.etc *:before,.etc *:after{box-sizing:border-box}
.etc h1,.etc h2,.etc h3{font-family:var(--fh);font-weight:400;line-height:1.15;margin:0;color:inherit;text-transform:none;letter-spacing:.01em}
.etc p{margin:0 0 1em}
.etc a{text-decoration:none!important}
.etc-wrap{max-width:1240px;margin:0 auto;padding:0 24px}
.etc .etm-i{width:24px;height:24px;flex:none;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.etc-eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:13px;font-weight:600;letter-spacing:.24em;text-transform:uppercase;color:var(--sand);margin-bottom:14px}
.etc-eyebrow:before,.etc-eyebrow:after{content:'';width:16px;height:16px;background:currentColor;clip-path:polygon(50% 0,61% 29%,93% 22%,71% 50%,93% 78%,61% 71%,50% 100%,39% 71%,7% 78%,29% 50%,7% 22%,39% 29%)}
.etc-hero{position:relative;min-height:440px;display:flex;align-items:flex-end;color:#fff;background:var(--ink) url(HERO) center/cover}
.etc-hero:before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,24,31,.35),rgba(5,24,31,.85))}
.etc-hero .etc-wrap{position:relative;padding:120px 24px 64px;width:100%}
.etc-hero h1{font-size:clamp(40px,6vw,72px);color:#fff}
.etc-hero p{max-width:620px;margin:18px 0 0;font-size:clamp(17px,1.6vw,20px);color:rgba(255,255,255,.85)}
.etc-band{height:10px;background:var(--zb);background-size:10px 10px}
.etc-cards{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:-50px;position:relative;z-index:2}
.etc-card{display:flex;flex-direction:column;gap:6px;padding:26px 24px;background:#fff;border-radius:18px;box-shadow:0 18px 40px rgba(5,24,31,.1);color:var(--ink)!important;transition:transform .2s}
a.etc-card:hover{transform:translateY(-4px)}
.etc-card .etm-i{width:44px;height:44px;padding:10px;border-radius:12px;background:var(--ink);color:var(--sand);margin-bottom:12px}
.etc-card small{font-size:12.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--sand2)}
.etc-card b{font-weight:600;font-size:16.5px;line-height:1.5;overflow-wrap:anywhere}
.etc-main{background:var(--cream);padding:70px 0 90px}
.etc-grid{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(30px,5vw,70px);align-items:start}
.etc-intro h2{font-size:clamp(34px,4.4vw,52px);margin-bottom:16px}
.etc-intro p{color:var(--mut)}
.etc-list{list-style:none;margin:22px 0 30px;padding:0;display:grid;gap:12px}
.etc-list li{display:flex;gap:12px;align-items:flex-start;font-weight:500}
.etc-list li:before{content:'';width:14px;height:14px;margin-top:6px;flex:none;background:var(--sand);clip-path:polygon(50% 0,61% 29%,93% 22%,71% 50%,93% 78%,61% 71%,50% 100%,39% 71%,7% 78%,29% 50%,7% 22%,39% 29%)}
.etc-map{border-radius:18px;overflow:hidden;border:6px solid #fff;box-shadow:0 18px 40px rgba(5,24,31,.1)}
.etc-map iframe{display:block;width:100%;height:320px;border:0}
.etc-form-box{background:#fff;border-radius:22px;padding:34px 34px 20px;box-shadow:0 24px 60px rgba(5,24,31,.1)}
.etc-form-box h3{font-size:28px;margin-bottom:6px}
.etc-form-box p{color:var(--mut);margin:0}
"""

# the Contact Form 7 widget sits in the right column; these rules style it
FORM_CSS = """
.etc-form{background:#fff;border-radius:0 0 22px 22px;padding:10px 34px 34px;margin-top:-6px;box-shadow:0 24px 60px rgba(5,24,31,.1);box-sizing:border-box;font-family:'Jost',system-ui,sans-serif}
.etc-form form p{margin:0 0 14px}.etc-form *{box-sizing:border-box;max-width:100%}
.etc-form label{display:block;font-size:14px;font-weight:600;color:#5e6b70}
.etc-form br{display:none}
.etc-form input[type=text],.etc-form input[type=email],.etc-form input[type=tel],.etc-form input[type=date],.etc-form input[type=number],.etc-form select,.etc-form textarea{
 width:100%;margin-top:6px;padding:14px 16px;border:1px solid #e4ddd2;border-radius:12px;background:#fbf8f3;color:#05181f;font:400 16px/1.4 'Jost',system-ui,sans-serif;transition:border-color .2s,box-shadow .2s}
.etc-form textarea{min-height:140px;resize:vertical}
.etc-form input:focus,.etc-form select:focus,.etc-form textarea:focus{outline:none;border-color:#d1a47b;box-shadow:0 0 0 3px rgba(209,164,123,.25);background:#fff}
.etc-form input[type=submit],.etc-form button[type=submit]{width:100%;height:54px;border:0;border-radius:999px;background:#05181f;color:#fff;font:600 16px 'Jost',system-ui,sans-serif;letter-spacing:.04em;cursor:pointer;transition:background .2s}
.etc-form input[type=submit]:hover{background:#3f6572}
.etc-form .wpcf7-spinner{position:absolute}
@media (max-width:1024px){.etc-cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:860px){.etc-grid{grid-template-columns:1fr}}
@media (max-width:600px){.etc{font-size:16px}.etc-wrap{padding:0 18px}.etc-cards{grid-template-columns:1fr;margin-top:-36px}.etc-form-box{padding:26px 22px 14px}.etc-form{padding:8px 22px 26px}.etc-hero .etc-wrap{padding:110px 18px 56px}}
"""


def left_html():
    cards = ('<div class="etc-cards">'
             '<a class="etc-card" href="tel:' + B.PHONE1 + '">' + ic('phone') + '<small>Morocco</small><b>' + B.PHONE1_T + '</b></a>'
             '<a class="etc-card" href="tel:' + B.PHONE2 + '">' + ic('phone') + '<small>Canada / USA</small><b>' + B.PHONE2_T + '</b></a>'
             '<a class="etc-card" href="mailto:' + B.EMAIL + '">' + ic('mail') + '<small>Email</small><b>' + B.EMAIL + '</b></a>'
             '<div class="etc-card">' + ic('map') + '<small>Office</small><b>Gueliz, Marrakech 22000, Morocco</b></div></div>')
    return (B.FONTS + '<style>' + ' '.join((CSS.replace('HERO', U + '2025/11/pexels-zakariahanif-12214734-scaled.jpg') + FORM_CSS).split()) + '</style>'
            '<script>' + B.ZJS + '</script>'
            '<div class="etc"><section class="etc-hero"><div class="etc-wrap"><span class="etc-eyebrow">Contact us</span>'
            '<h1>Let’s start planning</h1>'
            '<p>Don’t hesitate to reach out, whether it’s a fully crafted itinerary or just a question about one of our tours. '
            'Your Moroccan adventure starts here.</p></div></section><div class="etc-band"></div>'
            '<div class="etc-wrap">' + cards + '</div></div>')


def intro_html():
    return ('<div class="etc etc-intro"><span class="etc-eyebrow" style="color:#b98a5e">Get in touch</span>'
            '<h2>We’d love to hear from you</h2>'
            '<p>Whether you’re ready for a tailored Moroccan adventure, have questions about one of our tours, or just want to explore options, we’re here to help.</p>'
            '<ul class="etc-list"><li>Reply within 24 hours</li><li>Private tours, adapted to your dates and pace</li>'
            '<li>Local team based in Marrakech</li></ul>'
            '<div class="etc-map"><iframe src="' + MAP + '" loading="lazy" title="Epic Travel Morocco, Gueliz, Marrakech" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div>')


def form_head_html():
    return ('<div class="etc"><div class="etc-form-box"><h3>Send us a message</h3>'
            '<p>Tell us your dates, group size and the places you’d like to see.</p></div></div>')


def noq(h):
    h = h.replace('"', "'")
    assert '"' not in h and '\\' not in h
    return h


def eid(s):
    return hashlib.md5(s.encode()).hexdigest()[:7]


PAD0 = {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}


def w(kind, content, key, extra=None):
    st = {'html': content} if kind == 'html' else {'shortcode': content}
    st.update(extra or {})
    return {'id': eid(key), 'elType': 'widget', 'settings': st, 'elements': [], 'widgetType': kind}


data = [
    {'id': eid('etc-top'), 'elType': 'container', 'isInner': False,
     'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': PAD0,
                  'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0'}},
     'elements': [w('html', noq(left_html()), 'etc-w1')]},
    {'id': eid('etc-main'), 'elType': 'container', 'isInner': False,
     'settings': {'content_width': 'full', 'flex_direction': 'column', 'css_classes': 'etc-main', 'background_background': 'classic',
                  'background_color': '#FFF9F0', 'padding': {'unit': 'px', 'top': '70', 'right': '24', 'bottom': '90', 'left': '24', 'isLinked': False}},
     'elements': [{'id': eid('etc-grid'), 'elType': 'container', 'isInner': True,
                   'settings': {'content_width': 'boxed', 'boxed_width': {'unit': 'px', 'size': 1192, 'sizes': []},
                                'container_type': 'grid', 'grid_columns_grid': {'unit': 'fr', 'size': 2, 'sizes': []},
                                'grid_columns_grid_tablet': {'unit': 'fr', 'size': 1, 'sizes': []},
                                'grid_gaps': {'column': '60', 'row': '40', 'isLinked': False, 'unit': 'px'}, 'grid_align_items': 'start', 'padding': PAD0},
                   'elements': [
                       {'id': eid('etc-col1'), 'elType': 'container', 'isInner': True,
                        'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': PAD0},
                        'elements': [w('html', noq(intro_html()), 'etc-w2')]},
                       {'id': eid('etc-col2'), 'elType': 'container', 'isInner': True,
                        'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': PAD0,
                                     'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0'}},
                        'elements': [w('html', noq(form_head_html()), 'etc-w3'), w('shortcode', FORM, 'etc-w4', {'_css_classes': 'etc-form'})]},
                   ]}]},
]
s = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
assert '\\' not in s
open(os.path.join(HERE, 'contact-1360.json'), 'w').write(s)
print('contact-1360.json', len(s))

fake_form = ("<div class='etc-form'><form><p><label>Your name<input type='text'></label></p><p><label>Your email<input type='email'></label></p>"
             "<p><label>Subject<input type='text'></label></p><p><label>Your message<textarea></textarea></label></p><p><input type='submit' value='Submit'></p></form></div>")
page = ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'
        + left_html() + '<div style="background:#FFF9F0;padding:70px 24px 90px"><div style="max-width:1192px;margin:auto;display:grid;'
        'grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:40px 60px;align-items:start"><div>' + intro_html() + '</div><div>'
        + form_head_html() + fake_form + '</div></div></div></body></html>')
open(os.path.join(HERE, 'preview-contact.html'), 'w').write(page)
