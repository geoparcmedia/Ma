import re, sys, hashlib
css = open('style.css').read()
form = open('out/manifest.json') and ''
FORM = ('<form class="wpcf7-form"><div class="aim-row"><p><label>Full name *<input></label></p><p><label>Email *<input></label></p></div>'
        '<div class="aim-row"><p><label>WhatsApp / phone *<input></label></p><p><label>Travel date<input type="date"></label></p></div>'
        '<div class="aim-row"><p><label>Trip or service<input id="aim-trip"></label></p><p><label>Number of travellers<input value="2"></label></p></div>'
        '<p><label>Your message<textarea></textarea></label></p><input type="submit" value="Send my request"></form>')
def ph(m):
    u = m.group(1)
    h = int(hashlib.md5(u.encode()).hexdigest()[:6], 16)
    col = ['#b98b5e','#8a6a4f','#c49a6c','#6f8a8f','#a0522d','#d2a679','#7d6e5c'][h % 7]
    name = u.rsplit('/',1)[-1][:28]
    svg = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='1600' height='1000'><rect width='100%25' height='100%25' fill='" + col.replace('#','%23') + "'/><text x='50%25' y='50%25' fill='white' font-size='40' text-anchor='middle' font-family='sans-serif'>" + name + "</text></svg>"
    return 'src="' + svg + '"'
for f in sys.argv[1:]:
    h = open('out/%s.html' % f).read()
    lang = 'fr' if '"ref":0' in h and ('lang="fr"' in h) else 'en'
    parts = re.split(r'<!-- wp:block \{"ref":0\} /-->', h)
    order = ['header','book','footer'] if len(parts)==4 else ['header','footer']
    h = parts[0]
    for k, rest in zip(order, parts[1:]):
        h += open('out/blocks/%s-%s.html' % (k, lang)).read() + rest
    h = h.replace('<!-- wp:html -->','').replace('<!-- /wp:html -->','')
    h = re.sub(r'\[contact-form-7 id="\d+"\]', FORM, h)
    h = re.sub(r'src="(https://allinmarrakech[^"]+)"', ph, h)
    css2 = css.split('\n',1)[1]  # drop google font import (blocked)
    open('/tmp/claude-0/-home-user-Ma/4b23bc68-9921-52be-82c2-a849c89279b5/scratchpad/pv_%s.html' % f, 'w').write(
        '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>' + css2 + '</style></head><body class="page-template-elementor_canvas">' + h + '</body></html>')
