import json, re, hashlib, sys
sys.path.insert(0, '.')
from tours import tours_html, schema
from anim import SCENE, STATS, CSS, JS_EARLY, JS, add_bikes, add_reveal, SPRITE
body1 = None

style = open('style.html').read()
body1 = open('body1.html').read().replace('HERO2SCENE', "<div class='wgm-hero2 h2a' aria-hidden='true'><b>From the Atlas to the Sahara</b><span>Mountains · Oases · Berber villages · Desert dunes</span></div><div class='wgm-hero2 h2b' aria-hidden='true'><b>Ride the Dust – Live the Adventure</b><span>Guided gravel bike tours with local experts</span></div><div class='wgm-cue' aria-hidden='true'></div>" + SCENE).replace('STATSBAND', STATS)
style = style.replace('</style>', CSS + '</style>') + JS_EARLY + SPRITE
part3 = open('part3.html').read()
part5 = open('part5.html').read().replace('</div>\n', '', 0)
# part5 ends with the closing </div> of the old .wgm wrapper; drop it
part5 = part5.rsplit('</div>', 1)[0]

FAQ = re.findall(r'<details[^>]*><summary>(.*?)</summary><p>(.*?)</p></details>', part3)
faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in FAQ]}

weather_js = ("<script>window.addEventListener('load',function(){setTimeout(function(){var d=document,s=d.createElement('script');"
              "s.id='weatherwidget-io-js';s.src='https://weatherwidget.io/js/widget.min.js';d.body.appendChild(s);},1500);});</script>")

reviews_head = ('<section class="wgm-sec" style="padding-top:0;padding-bottom:24px"><div class="wgm-wrap"><div class="wgm-head" style="margin-bottom:0">'
                '<span class="wgm-eyebrow">Reviews</span><h2>What Our Travelers Say</h2>'
                '<p>Read real reviews from riders and hikers who explored Morocco with us on Tripadvisor.</p></div></div></section>')

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
    return ('<script>(function(){[' + ','.join(jsval(o) for o in objs) + '].forEach(function(o){var s=document.createElement(\'script\');'
            's.type=\'application/ld+json\';s.text=JSON.stringify(o);document.head.appendChild(s);});})();</script>')


W = lambda s: '<div class="wgm">' + s + '</div>'
widgets = [
    ('html', style + W(body1)),
    ('html', W(tours_html())),
    ('html', W(part3) + weather_js),
    ('html', W(reviews_head)),
    ('shortcode', '[trustindex no-registration=tripadvisor]'),
    ('html', W(part5) + JS + ldjs([json.loads(schema()[35:-9]), faq_ld])),
]


def eid(s):
    return hashlib.md5(s.encode()).hexdigest()[:7]


els = []
for i, (t, c) in enumerate(widgets):
    c = c.replace('\n', ' ')
    if t == 'html':
        c = re.sub(r'(<script type="application/ld\+json">.*?</script>)|="([^"\']*)"', lambda m: m.group(1) or "='" + m.group(2) + "'", c, flags=re.S)
        c = add_reveal(add_bikes(c))
    st = {'html': c} if t == 'html' else {'shortcode': c}
    els.append({"id": eid('w%d' % i), "elType": "widget", "settings": st, "elements": [], "widgetType": t})
data = [{"id": "a1b2c3d", "elType": "section",
         "settings": {"layout": "full_width", "stretch_section": "section-stretched", "gap": "no",
                      "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}},
         "elements": [{"id": "e4f5a6b", "elType": "column",
                       "settings": {"_column_size": 100, "_inline_size": None, "space_between_widgets": 0,
                                    "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}},
                       "elements": els, "isInner": False}], "isInner": False}]
out = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
open('home_new_elementor.json', 'w').write(out)
open('home_send.txt', 'w').write(out.replace('\\', '\\\\'))
print('elementor json', len(out), 'backslashes', out.count('\\'))

# preview
def ph(m):
    u = m.group(0)
    h = int(hashlib.md5(u.encode()).hexdigest()[:6], 16)
    return 'https://ph.local/%06x' % h
page = ''.join(e['settings']['html'] if e['widgetType'] == 'html' else '<div style="height:260px;background:#eee;display:flex;align-items:center;justify-content:center;font:20px sans-serif;color:#888">[Tripadvisor reviews widget]</div>' for e in els)
page = page.replace(' loading="lazy"','')
page = re.sub(r"https://wegravelmorocco\.com/wp-content/uploads/[^\"' ,]+", ph, page)
html = ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<style>body{margin:0;font-family:Poppins,Arial,sans-serif}.hdr{height:120px;background:#313041;color:#fff;display:flex;align-items:center;padding:0 30px;font:bold 20px sans-serif}</style></head>'
        '<body><div class="hdr">[site header]</div><div style="overflow:hidden">' + page + '</div></body></html>')
open('preview.html', 'w').write(html)
