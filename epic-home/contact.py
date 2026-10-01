"""Epic Travel Morocco – Contact page (ID 1360, /contact-2/), chic Moroccan style (see chic.py).

python3 contact.py -> contact-1360.json (value of _elementor_data) and preview-contact.html
Header and footer come from the site-wide footer template (footer.py).
"""
import json, os
import build as B
import chic as C

HERE = os.path.dirname(os.path.abspath(__file__))
FORM = "[contact-form-7 id='f402750' title='Main Contact']"
MAP = 'https://maps.google.com/maps?q=Gueliz%2C%20Marrakech%2C%20Morocco&z=14&output=embed'
HERO = C.U + '2025/11/pexels-zakariahanif-12214734-scaled.jpg'

CSS = """
.etc-info{background:var(--paper)}
.etc-info-g{max-width:1240px;margin:0 auto;display:grid;grid-template-columns:repeat(4,minmax(0,1fr))}
.etc-info-g>*{display:block;padding:46px 32px;border-left:1px solid var(--line);transition:background .3s}
.etc-info-g>*:first-child{border-left:0}
.etc-info-g a:hover{background:#fff}
.etc-info small{display:block;font-size:11px;font-weight:500;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:12px}
.etc-info b{display:block;font-family:var(--fh);font-weight:400;font-size:24px;line-height:1.3;overflow-wrap:anywhere}
.etc-info b.etc-sm{font-size:clamp(17px,1.45vw,21px);overflow-wrap:normal;padding-top:4px}
.etc-head p{color:var(--mut);max-width:460px;margin-bottom:40px}
.etc-side{position:relative}
.etc-side .ch-archf{margin-bottom:0}
.etc-map{height:460px}
.etc-map iframe{display:block;width:100%;height:100%;border:0;filter:grayscale(1) sepia(.18) contrast(1.02)}
.etc-side-t{background:var(--paper);padding:38px 40px 42px;margin:0 12px}
.etc-side-t h3{font-size:30px;margin-bottom:16px}
.etc-side-t dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:10px 28px;font-size:15px}
.etc-side-t dt{font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);padding-top:4px}
.etc-side-t dd{margin:0;overflow-wrap:anywhere}
.etc-form{font-family:'Jost',system-ui,sans-serif;font-weight:300}
.etc-form *{box-sizing:border-box;max-width:100%}
.etc-form form p{margin:0 0 30px}
.etc-form label{display:block;font-size:11px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:#66717a}
.etc-form br{display:none}
.etc-form input[type=text],.etc-form input[type=email],.etc-form input[type=tel],.etc-form input[type=date],.etc-form input[type=number],.etc-form select,.etc-form textarea{
 width:100%;margin-top:4px;padding:12px 0;border:0;border-bottom:1px solid rgba(13,26,31,.2);border-radius:0;background:transparent;color:#0d1a1f;
 font:400 19px/1.4 'Cormorant Garamond',Georgia,serif;box-shadow:none;transition:border-color .3s}
.etc-form textarea{min-height:110px;height:110px;resize:vertical}
.etc-form input:focus,.etc-form select:focus,.etc-form textarea:focus{outline:none;border-bottom-color:#b98a5e;box-shadow:none;background:transparent}
.etc-form input[type=submit],.etc-form button[type=submit]{width:auto;height:auto;padding:20px 54px;border:1px solid #0d1a1f;border-radius:0;background:#0d1a1f;color:#fff;
 font:500 12px 'Jost',system-ui,sans-serif;letter-spacing:.3em;text-transform:uppercase;cursor:pointer;transition:background .35s,color .35s}
.etc-form input[type=submit]:hover,.etc-form button[type=submit]:hover{background:transparent;color:#0d1a1f}
.etc-form .wpcf7-spinner{position:absolute}
.etc-form .wpcf7-not-valid-tip{font-size:13px;margin-top:6px}
@media (max-width:1024px){.etc-info-g{grid-template-columns:repeat(2,minmax(0,1fr))}.etc-info-g>*:nth-child(3){border-left:0}.etc-info-g>*:nth-child(n+3){border-top:1px solid var(--line)}}
@media (max-width:600px){.etc-info-g{grid-template-columns:1fr}.etc-info-g>*{border-left:0!important;border-top:1px solid var(--line);padding:28px 22px}.etc-info-g>*:first-child{border-top:0}.etc-side-t{padding:28px 22px 32px}.etc-map{height:340px}}
"""


def top_html():
    info = ('<div class="etc-info"><div class="etc-info-g">'
            '<a href="tel:' + B.PHONE1 + '"><small>Morocco</small><b>' + B.PHONE1_T + '</b></a>'
            '<a href="tel:' + B.PHONE2 + '"><small>Canada &amp; USA</small><b>' + B.PHONE2_T + '</b></a>'
            '<a href="mailto:' + B.EMAIL + '"><small>Write to us</small><b class="etc-sm">' + B.EMAIL + '</b></a>'
            '<div><small>Visit us</small><b>Gueliz, Marrakech</b></div></div></div>')
    acts = ('<a class="ch-btn ch-btn-g" href="https://wa.me/' + B.PHONE1.lstrip('+') + '">WhatsApp</a>'
            '<a href="mailto:' + B.EMAIL + '">Email us</a>')
    return (C.style(CSS) + '<div class="ch">'
            + C.hero('Contact', 'Let’s craft your<br><em>Moroccan journey</em>',
                     'A fully tailored itinerary or a simple question about one of our tours. Our team in Marrakech answers every message personally.',
                     HERO, acts, 'Private tour vehicle in Marrakech')
            + info + '</div>')


def form_head_html():
    return ('<div class="ch etc-head">' + C.kicker('Enquiry') + '<h2 class="ch-h2">Tell us about<br><em>your trip</em></h2>'
            '<p>Share your dates, the size of your group and the places you dream of. We will come back to you with a personal proposal.</p></div>')


def side_html():
    return ('<div class="ch etc-side"><div class="ch-archf"><div class="ch-arch etc-map"><iframe src="' + MAP + '" loading="lazy" '
            'title="Epic Travel Morocco, Gueliz, Marrakech" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div>'
            '<div class="etc-side-t"><h3>Our office</h3><dl>'
            '<dt>Address</dt><dd>Gueliz, Marrakech 22000, Morocco</dd>'
            '<dt>Phone</dt><dd><a href="tel:' + B.PHONE1 + '">' + B.PHONE1_T + '</a></dd>'
            '<dt>Email</dt><dd><a href="mailto:' + B.EMAIL + '">' + B.EMAIL + '</a></dd></dl></div></div>')


W = C.widget
data = [
    {'id': C.eid('etc-top'), 'elType': 'container', 'isInner': False,
     'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': C.PAD0, 'flex_gap': C.GAP0},
     'elements': [W('html', C.noq(top_html()), 'etc-w1')]},
    {'id': C.eid('etc-main'), 'elType': 'container', 'isInner': False,
     'settings': {'content_width': 'full', 'flex_direction': 'column', 'css_classes': 'etc-main', 'background_background': 'classic',
                  'background_color': '#FFFFFF', 'padding': {'unit': 'px', 'top': '110', 'right': '24', 'bottom': '110', 'left': '24', 'isLinked': False},
                  'padding_mobile': {'unit': 'px', 'top': '64', 'right': '20', 'bottom': '70', 'left': '20', 'isLinked': False}},
     'elements': [{'id': C.eid('etc-grid'), 'elType': 'container', 'isInner': True,
                   'settings': {'content_width': 'boxed', 'boxed_width': {'unit': 'px', 'size': 1184, 'sizes': []},
                                'container_type': 'grid', 'grid_columns_grid': {'unit': 'fr', 'size': 2, 'sizes': []},
                                'grid_columns_grid_tablet': {'unit': 'fr', 'size': 1, 'sizes': []},
                                'grid_gaps': {'column': '90', 'row': '60', 'isLinked': False, 'unit': 'px'}, 'grid_align_items': 'start', 'padding': C.PAD0},
                   'elements': [
                       {'id': C.eid('etc-col1'), 'elType': 'container', 'isInner': True,
                        'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': C.PAD0, 'flex_gap': C.GAP0},
                        'elements': [W('html', C.noq(form_head_html()), 'etc-w3'), W('shortcode', FORM, 'etc-w4', {'_css_classes': 'etc-form'})]},
                       {'id': C.eid('etc-col2'), 'elType': 'container', 'isInner': True,
                        'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': C.PAD0},
                        'elements': [W('html', C.noq(side_html()), 'etc-w2')]},
                   ]}]},
]

if __name__ == '__main__':
    s = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s
    open(os.path.join(HERE, 'contact-1360.json'), 'w').write(s)
    print('contact-1360.json', len(s))
    fake_form = ("<div class='etc-form'><form><p><label>Your name<input type='text'></label></p><p><label>Your email<input type='email'></label></p>"
                 "<p><label>Subject<input type='text'></label></p><p><label>Your message<textarea></textarea></label></p><p><input type='submit' value='Send enquiry'></p></form></div>")
    body = (top_html() + '<div style="background:#fff;padding:110px 24px"><div style="max-width:1184px;margin:auto;display:grid;'
            'grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:60px 90px;align-items:start"><div>' + form_head_html() + fake_form + '</div><div>'
            + side_html() + '</div></div></div>')
    open(os.path.join(HERE, 'preview-contact.html'), 'w').write(C.preview(body, 'Contact'))
