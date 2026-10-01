"""Shared 'chic Moroccan' design system for the inner pages of epictravelmorocco.com.

Modern editorial layout (Cormorant Garamond + Jost, ink / gold / paper) with a light Moroccan touch:
arched image frames, khatam (8-point star) ornaments and a faint rosette watermark in the dark sections.
Every page script (contact.py, about.py, fleet.py, tours.py, footer.py) imports this module.
Elementor meta cannot hold double quotes or backslashes, so all markup goes through noq().
"""
import hashlib, math
import build as B

SITE, U = B.SITE, B.U

FONTS = ("<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
         "<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap'>")


def _star(cx, cy, r1, r2, n=8, rot=0.0):
    pts = []
    for i in range(2 * n):
        r = r1 if i % 2 == 0 else r2
        t = math.pi * i / n + rot
        pts.append('%.1f,%.1f' % (cx + r * math.sin(t), cy - r * math.cos(t)))
    return ' '.join(pts)


def star(cls='ch-star'):
    """Small khatam star icon (line art)."""
    return ('<svg class="%s" viewBox="0 0 24 24" aria-hidden="true"><polygon points="%s"/><circle cx="12" cy="12" r="2.2"/></svg>'
            % (cls, _star(12, 12, 10.5, 6.2)))


def rosette(cls='ch-ros'):
    """Large line-art Moroccan rosette, used as a faint watermark."""
    p = []
    p.append('<rect x="45" y="45" width="110" height="110"/>')
    p.append('<rect x="45" y="45" width="110" height="110" transform="rotate(45 100 100)"/>')
    p.append('<circle cx="100" cy="100" r="92"/><circle cx="100" cy="100" r="78"/><circle cx="100" cy="100" r="22"/>')
    p.append('<polygon points="%s"/>' % _star(100, 100, 66, 40, 8, math.pi / 8))
    p.append('<polygon points="%s"/>' % _star(100, 100, 36, 24, 8))
    for k in range(16):
        t = math.pi * k / 8
        p.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (100 + 22 * math.sin(t), 100 - 22 * math.cos(t), 100 + 78 * math.sin(t), 100 - 78 * math.cos(t)))
    return '<svg class="%s" viewBox="0 0 200 200" aria-hidden="true">%s</svg>' % (cls, ''.join(p))


def orn(extra=''):
    """Divider: hairline, star, hairline."""
    return '<div class="ch-orn %s"><span></span>%s<span></span></div>' % (extra, star())


def kicker(text, light=False):
    return '<span class="ch-k%s">%s%s</span>' % (' ch-k-l' if light else '', star(), text)


CSS = """
.ch{--ink:#0d1a1f;--ink2:#132830;--gold:#b98a5e;--gold2:#d1a47b;--line:rgba(13,26,31,.13);--mut:#66717a;--paper:#f7f3ec;--paper2:#efe7da;
 --fh:'Cormorant Garamond',Georgia,serif;--fb:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;
 font-family:var(--fb);font-weight:300;color:var(--ink);font-size:17px;line-height:1.75;-webkit-font-smoothing:antialiased}
.ch *,.ch *:before,.ch *:after{box-sizing:border-box}
.ch h1,.ch h2,.ch h3,.ch h4{font-family:var(--fh);font-weight:400;line-height:1.06;margin:0;color:inherit;text-transform:none;letter-spacing:-.01em}
.ch em{font-style:italic;color:var(--gold)}
.ch p{margin:0 0 1em}
.ch a{text-decoration:none!important;color:inherit}
.ch img{display:block;max-width:100%}
.ch-w{max-width:1240px;margin:0 auto;padding:0 28px}
.ch-star{width:14px;height:14px;flex:none;fill:none;stroke:currentColor;stroke-width:1.3}
.ch-k{display:inline-flex;align-items:center;gap:12px;font-size:11.5px;font-weight:500;letter-spacing:.32em;text-transform:uppercase;color:var(--gold);margin-bottom:24px}
.ch-k-l{color:var(--gold2)}
.ch-orn{display:flex;align-items:center;justify-content:center;gap:16px;color:var(--gold);margin:0 auto 26px;max-width:260px}
.ch-orn span{flex:1;height:1px;background:currentColor;opacity:.5}
.ch-orn .ch-star{width:18px;height:18px}
.ch-ros{position:absolute;width:520px;height:520px;fill:none;stroke:var(--gold2);stroke-width:.55;opacity:.13;pointer-events:none}
.ch-btn{display:inline-flex;align-items:center;gap:14px;padding:19px 40px;border:1px solid var(--ink);background:var(--ink);color:#fff!important;font:500 12px var(--fb);letter-spacing:.3em;text-transform:uppercase;transition:background .35s,color .35s,border-color .35s}
.ch-btn:hover{background:transparent;color:var(--ink)!important}
.ch-btn-g{border-color:var(--gold2);background:transparent;color:#fff!important}
.ch-btn-g:hover{background:var(--gold2);color:var(--ink)!important}
.ch-link{display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;padding-bottom:6px;border-bottom:1px solid var(--gold)}
/* arched frames: the Moroccan window */
.ch-arch{position:relative;border-radius:999px 999px 0 0;overflow:hidden;background:var(--paper2)}
.ch-arch img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s}
.ch-archf{position:relative;padding:12px}
.ch-archf:before{content:'';position:absolute;inset:0;border:1px solid var(--gold);border-radius:999px 999px 0 0;opacity:.55;pointer-events:none}
/* page hero */
.ch-hero{position:relative;overflow:hidden;padding-top:90px;background:var(--ink);color:#efe8de}
.ch-hero .ch-ros{right:-150px;top:-130px}
.ch-hero-g{position:relative;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(30px,6vw,90px);align-items:end}
.ch-hero-t{padding-bottom:110px}
.ch-hero h1{font-size:clamp(48px,6.4vw,96px);color:#fff}
.ch-hero p{max-width:470px;margin:30px 0 40px;color:rgba(239,232,222,.72)}
.ch-hero .ch-arch{height:clamp(380px,46vw,600px)}
.ch-hero-act{display:flex;flex-wrap:wrap;gap:14px 30px;align-items:center}
.ch-hero-act a:not(.ch-btn){color:#fff;font-size:12px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;padding-bottom:6px;border-bottom:1px solid var(--gold2)}
/* sections */
.ch-s{padding:clamp(80px,10vw,130px) 0}
.ch-paper{background:var(--paper)}
.ch-h2{font-size:clamp(40px,4.8vw,66px);margin-bottom:24px}
.ch-lead{font-family:var(--fh);font-size:clamp(22px,2.2vw,28px);line-height:1.5;color:var(--ink)}
.ch-mut{color:var(--mut)}
.ch-center{text-align:center}
.ch-center p{margin-left:auto;margin-right:auto}
/* dark call to action */
.ch-cta{position:relative;overflow:hidden;background:var(--ink2);color:#efe8de;text-align:center;padding:clamp(80px,9vw,120px) 0}
.ch-cta .ch-ros{left:50%;top:50%;width:640px;height:640px;margin:-320px 0 0 -320px;opacity:.09}
.ch-cta h2{position:relative;font-size:clamp(40px,5vw,70px);color:#fff;margin-bottom:20px}
.ch-cta p{position:relative;max-width:540px;margin:0 auto 38px;color:rgba(239,232,222,.7)}
.ch-cta .ch-orn{color:var(--gold2)}
.ch-cta-act{position:relative;display:flex;justify-content:center;flex-wrap:wrap;gap:14px}
@media (max-width:900px){.ch-hero{padding-top:56px}.ch-hero-g{grid-template-columns:1fr;gap:0}.ch-hero-t{padding-bottom:50px}.ch-hero .ch-arch{height:420px;max-width:520px;width:100%;margin:0 auto}.ch-hero .ch-ros{width:380px;height:380px;right:-160px;top:-120px}}
@media (max-width:600px){.ch{font-size:16px}.ch-w{padding:0 22px}.ch-hero .ch-arch{height:360px}.ch-btn{padding:17px 30px}}
"""


def style(extra_css=''):
    return FONTS + '<style>' + ' '.join((CSS + extra_css).split()) + '</style>'


def hero(k, title, text, img, actions, alt):
    return ('<section class="ch-hero">' + rosette() + '<div class="ch-w ch-hero-g"><div class="ch-hero-t">' + kicker(k, True)
            + '<h1>' + title + '</h1><p>' + text + '</p><div class="ch-hero-act">' + actions + '</div></div>'
            '<div class="ch-archf"><div class="ch-arch"><img src="' + img + '" alt="' + alt + '"></div></div></div></section>')


def cta(title='Ready to plan <em>your journey?</em>',
        text='Tell us your dates and the places you dream of. We design a private itinerary around you.'):
    return ('<section class="ch-cta">' + rosette() + '<div class="ch-w">' + orn() + '<h2>' + title + '</h2><p>' + text + '</p>'
            '<div class="ch-cta-act"><a class="ch-btn ch-btn-g" href="' + SITE + '/contact-2/">Plan my trip</a>'
            '<a class="ch-btn ch-btn-g" href="https://wa.me/' + B.PHONE1.lstrip('+') + '">WhatsApp</a></div></div></section>')


def noq(h):
    h = h.replace('"', "'")
    assert '"' not in h and '\\' not in h
    return h


def eid(s):
    return hashlib.md5(s.encode()).hexdigest()[:7]


PAD0 = {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
GAP0 = {'unit': 'px', 'size': 0, 'column': '0', 'row': '0'}


def widget(kind, content, key, extra=None):
    st = {'html': content} if kind == 'html' else {'shortcode': content}
    st.update(extra or {})
    return {'id': eid(key), 'elType': 'widget', 'settings': st, 'elements': [], 'widgetType': kind}


def html_page(key, html):
    """Whole page as one full-width container holding one html widget."""
    return [{'id': eid(key), 'elType': 'container', 'isInner': False,
             'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': PAD0, 'flex_gap': GAP0},
             'elements': [widget('html', noq(html), key + '-w')]}]


def preview(body, title='Preview'):
    """Stand-alone preview page: the global header and footer from footer.py around the page body."""
    import footer as F
    return ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + title + '</title></head>'
            '<body class="page" style="margin:0">' + body + F.preview_footer() + '</body></html>')
