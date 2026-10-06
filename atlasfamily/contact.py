"""Contact page (8279): contact cards + Contact Form 7 (id 4de6ca8) + map, in the Atlas Family style."""
import json
from home import CSS, container, html, eid, WA, TREKS
from brand import EXTRA

C_CSS = ("<style>.afc-grid{display:grid;grid-template-columns:1fr 1.25fr;gap:40px;align-items:start}"
 ".afc-cards{display:grid;gap:14px}.afc-card{display:flex;gap:16px;align-items:center;background:#fff;border:1px solid #eadcc8;border-radius:16px;padding:18px 20px;text-decoration:none;color:var(--ink);transition:transform .2s,box-shadow .2s}"
 "a.afc-card:hover{transform:translateY(-3px);box-shadow:0 16px 34px -20px rgba(0,0,0,.35)}"
 ".afc-ic{flex:0 0 50px;width:50px;height:50px;border-radius:50%;display:grid;place-items:center;font-size:22px;background:var(--sand);color:var(--o)}"
 ".afc-card small{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);font-weight:600}.afc-card b{font-size:17px;font-weight:600}"
 ".afc-card.wa .afc-ic{background:#1f9d55;color:#fff}"
 ".afc-note{background:var(--sand);border-radius:16px;padding:20px 22px;margin-top:6px;color:var(--mut);font-size:15px}"
 ".afc-form-head{background:#2a2017;color:#fff;border-radius:20px 20px 0 0;padding:26px 30px}.afc-form-head h2{color:#fff;font-size:28px;margin:0 0 6px}.afc-form-head p{margin:0;color:rgba(255,255,255,.8)}"
 "</style>")
FORM_CSS = ("<style>.afc-form,.afc-form *{box-sizing:border-box}.afc-form{background:#fff;border:1px solid #eadcc8;border-top:0;border-radius:0 0 20px 20px;padding:26px 30px 30px;box-shadow:0 24px 50px -30px rgba(0,0,0,.35)}"
 ".afc-form .wpcf7 p{margin:0 0 14px}.afc-form .wpcf7 br{display:none}"
 ".afc-form input[type=text],.afc-form input[type=email],.afc-form input[type=tel],.afc-form textarea{box-sizing:border-box;width:100%;border:1px solid #dcc9ae;border-radius:12px;padding:14px 16px;font-size:16px;background:#fffdf9;color:#1c1c1c;outline:0;box-shadow:none;margin:0}"
 ".afc-form textarea{height:150px;resize:vertical}.afc-form input:focus,.afc-form textarea:focus{border-color:#b8432b;box-shadow:0 0 0 4px rgba(184,67,43,.15)}"
 ".afc-form .wpcf7-submit{width:100%;padding:16px 24px!important;font-size:16px!important;cursor:pointer}"
 ".afc-form .wpcf7-response-output{border-radius:12px;margin:14px 0 0!important}</style>")

def left():
    cards = [('wa', '✆', 'WhatsApp (fastest)', '+212 703 501 612', WA),
             ('', '☎', 'Phone', '+212 703 501 612', 'tel:+212703501612'),
             ('', '☎', 'Phone 2', '+212 700 174 513', 'tel:+212700174513'),
             ('', '✉', 'Email', 'aelmahdizaki@gmail.com', 'mailto:aelmahdizaki@gmail.com'),
             ('', '⌂', 'Office', 'Gueliz, Marrakech 22000, Morocco', None)]
    out = ''
    for cls, ic, lab, val, url in cards:
        inner = "<span class='afc-ic'>%s</span><span><small>%s</small><b>%s</b></span>" % (ic, lab, val)
        out += ("<a class='afc-card %s' href='%s'%s>%s</a>" % (cls, url, " target='_blank' rel='noopener'" if url.startswith('http') else '', inner)) if url else "<div class='afc-card'>%s</div>" % inner
    return out

def head():
    return (CSS + EXTRA + C_CSS + FORM_CSS + "<div class='afh'><section class='afh-sec' style='padding-bottom:40px'><div class='afh-w'><div class='afh-head' style='margin-bottom:0'>"
            "<span class='afh-k'>Contact us</span><h2>Let’s plan your adventure together</h2>"
            "<p>Tell us about your dream trek in Morocco: dates, group size, and what you would love to see. Mehdi and the family will get back to you personally.</p></div></div></section></div>")

def cards():
    return ("<div class='afh'><div class='afc-cards'>" + left() +
            "<div class='afc-note'><b>Good to know:</b> all our treks can be adapted. Tell us your level and your interests, and we will suggest the right route for you.</div></div></div>")

def form_head():
    return "<div class='afh'><div class='afc-form-head'><h2>Send us a message</h2><p>We usually answer on WhatsApp or by email.</p></div></div>"

def bottom():
    return ("<div class='afh'><div class='afh-rug' style='margin-top:70px'></div>"
            "<section class='afh-sec' style='padding:60px 0 80px'><div class='afh-w afh-more'>"
            "<span class='afh-k'>Prefer to talk?</span><h2>Chat with us on WhatsApp</h2><p>Questions about a trek, the best season or what to bring? Send us a message and we will help.</p>"
            "<p class='afh-sign'>Mehdi &amp; the Atlas family</p>"
            "<div class='afh-btns'><a class='afh-b afh-b--p' href='%s' target='_blank' rel='noopener'>WhatsApp us</a>"
            "<a class='afh-b afh-b--l' href='%s'>See our treks</a></div></div></section></div>") % (WA, TREKS)

def inner(cid, els, extra):
    c = container(cid, els, extra); c['isInner'] = True; return c

def build():
    k = 'contact'
    form = {'id': eid(k, 'form'), 'elType': 'widget', 'widgetType': 'shortcode', 'elements': [],
            'settings': {'shortcode': "[contact-form-7 id='4de6ca8' title='Contact Form']", '_css_classes': 'afc-form'}}
    pad0 = {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
    row = container(eid(k, 'row'), [
        inner(eid(k, 'l'), [html(eid(k, 'wl'), cards())], {'width': {'unit': '%', 'size': 42, 'sizes': []}, 'width_mobile': {'unit': '%', 'size': 100, 'sizes': []}, 'padding': pad0}),
        inner(eid(k, 'r'), [html(eid(k, 'wr'), form_head()), form], {'width': {'unit': '%', 'size': 58, 'sizes': []}, 'width_mobile': {'unit': '%', 'size': 100, 'sizes': []}, 'padding': pad0})],
        {'content_width': 'boxed', 'boxed_width': {'unit': 'px', 'size': 1200, 'sizes': []}, 'flex_direction': 'row', 'flex_direction_mobile': 'column', 'flex_wrap': 'nowrap',
         'flex_gap': {'unit': 'px', 'size': 40, 'column': '40', 'row': '40'}, 'padding': {'unit': 'px', 'top': '0', 'right': '20', 'bottom': '0', 'left': '20', 'isLinked': False}})
    return [container(eid(k, 'c1'), [html(eid(k, 'w1'), head())]), row, container(eid(k, 'c3'), [html(eid(k, 'w3'), bottom())])]

if __name__ == '__main__':
    ed = build()
    s = json.dumps(ed, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s
    open('contact_elementor.json', 'w').write(s)
    fake = "<div class='wpcf7'><form><p><input type='text' placeholder='Enter Your First Name'></p><p><input type='text' placeholder='Enter Your Last Name'></p><p><input type='email' placeholder='Your Email'></p><p><input type='tel' placeholder='Phone No'></p><p><textarea placeholder='Write Your Comment'></textarea></p><p><input class='wpcf7-submit' type='submit' value='Send Message'></p></form></div>"
    open('contact_preview.html', 'w').write("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><body style='margin:0;font-family:system-ui'><style>.r{max-width:1200px;margin:0 auto;padding:0 20px;display:flex;gap:40px}.r>div:first-child{width:42%}.r>div:last-child{width:58%}@media(max-width:767px){.r{flex-direction:column}.r>div{width:100%!important}}</style>"
        + head() + "<div class='r'><div>" + cards() + "</div><div>" + form_head() + "<div class='afc-form'>" + fake + "</div></div></div>" + bottom())
    print(len(s))
