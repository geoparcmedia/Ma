"""Adds the site-wide header/footer block (footer.py -> chrome-widget.html) to the site.

The Contact page holds the full block; every other page and tour gets a tiny loader that copies it from /contact-2/.

The Travelor theme does not render the footer widget area nor Elementor footer templates, so the block lives
inside every page. python3 embed.py -> deploy/<name>.json (values of _elementor_data, ready to upload).
Tour pages (classic content) get a tiny loader instead (deploy/tour-loader.html) that copies the block from /contact-2/.
"""
import json, os
import chic as C

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = [('home-3648', 'elementor-data.json'), ('contact-1360', 'contact-1360.json'), ('about-1247', 'about-1247.json'),
         ('fleet-1334', 'fleet-1334.json'), ('tours-69', 'tours-69.json')]

LOADER = ("<script>(function(){var d=document;if(d.querySelector('.chw'))return;"
          "fetch('/contact-2/',{credentials:'same-origin'}).then(function(r){return r.text()}).then(function(t){"
          "if(d.querySelector('.chw'))return;var w=new DOMParser().parseFromString(t,'text/html').querySelector('.chw');if(!w)return;"
          "var box=d.importNode(w,true),ss=[].slice.call(box.querySelectorAll('script'));ss.forEach(function(s){s.remove()});"
          "d.body.appendChild(box);ss.forEach(function(s){var n=d.createElement('script');n.text=s.text;d.body.appendChild(n)})})})();</script>")
chrome = open(os.path.join(HERE, 'chrome-widget.html')).read()
os.makedirs(os.path.join(HERE, 'deploy'), exist_ok=True)
for name, src in PAGES:
    data = json.load(open(os.path.join(HERE, src)))
    data = [el for el in data if el.get('id') != C.eid('chrome-' + name)]
    data.append({'id': C.eid('chrome-' + name), 'elType': 'container', 'isInner': False,
                 'settings': {'content_width': 'full', 'flex_direction': 'column', 'padding': C.PAD0, 'flex_gap': C.GAP0},
                 'elements': [C.widget('html', chrome if name == 'contact-1360' else LOADER, 'chrome-w-' + name)]})
    s = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s
    open(os.path.join(HERE, 'deploy', name + '.json'), 'w').write(s)
    print(name, len(s))

open(os.path.join(HERE, 'deploy', 'tour-loader.html'), 'w').write(LOADER)
print('loader', len(LOADER))
