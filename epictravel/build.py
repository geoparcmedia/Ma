import json, re, os, sys, hashlib
from pages import *

OUT = 'out'; os.makedirs(OUT, exist_ok=True); os.makedirs('preview', exist_ok=True)
def css_min():
    c = open('site.css').read()
    c = re.sub(r'/[*].*?[*]/', '', c, flags=re.S)
    c = re.sub(r'url[(]"(data:[^"]+)"[)]', lambda m: 'url(' + chr(39) + m.group(1).replace(chr(39), '%27') + chr(39) + ')', c)
    c = re.sub(r'\s*\n\s*', '', c)
    assert '"' not in c, c[c.find('"')-60:c.find('"')+60]
    return c
HDR = clean('<style>' + css_min() + '</style>' + header() + JS)
FTR = clean(SPRITE + '<style>.et-book-f .et-btn{line-height:1.3}</style>' + footer())
PAGES = {862: ('home', home()), 69: ('tours', tours_page()), 1247: ('about', about()), 1360: ('contact', contact()), 1334: ('fleet', fleet())}
for t in TOURS:
    PAGES[t['id']] = ('tour-' + t['url'], tour_page(t))

def full(widgets, hid, fid):
    return [('shortcode', '[elementor-template id=%d]' % hid)] + widgets + [('shortcode', '[elementor-template id=%d]' % fid)]

def build(hid, fid):
    sizes = {}
    for pid, (name, w) in PAGES.items():
        data = elementor(full(w, hid, fid), name)
        open(f'{OUT}/{pid}.json', 'w').write(data); sizes[pid] = len(data)
    open(f'{OUT}/header.json', 'w').write(elementor([('html', HDR)], 'hdr'))
    open(f'{OUT}/footer.json', 'w').write(elementor([('html', FTR)], 'ftr'))
    open(f'{OUT}/site.css', 'w').write(open('site.css').read())
    return sizes

# ----- preview with placeholder images (the live site is not reachable from this machine) -----
COL = ['#c9895e', '#7d9aa3', '#b5552f', '#d1a47b', '#2f4f7a', '#a3765a', '#5c828f', '#c7a46b']
def ph(m):
    h = int(hashlib.md5(m.group(0).encode()).hexdigest(), 16)
    a, b = COL[h % 8], COL[(h // 8) % 8]
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' width='800' height='600'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='" + a + "'/><stop offset='1' stop-color='" + b + "'/></linearGradient></defs>"
           "<rect width='800' height='600' fill='url(%23g)'/><path d='M0 600 L220 380 L360 470 L560 300 L800 520 L800 600Z' fill='rgba(0,0,0,.18)'/><circle cx='620' cy='150' r='60' fill='rgba(255,255,255,.35)'/></svg>")
    return 'data:image/svg+xml,' + svg.replace('#', '%23').replace("'", '%27').replace('<', '%3C').replace('>', '%3E').replace(' ', '%20')
def preview(name, widgets):
    html = ''.join(c if t == 'html' else "<div style='padding:40px;text-align:center;background:#fff;color:#999;font:14px sans-serif'>[" + c + "]</div>" for t, c in widgets)
    html = HDR + html + FTR
    html = re.sub(r"https://epictravelmorocco\.com/wp-content/uploads/[^'\" ,)]+\.(?:jpe?g|png|webp)", ph, html)
    html = html.replace("srcset='data", "srcset='data")
    doc = ("<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
           "<link href='https://fonts.googleapis.com/css2?family=Philosopher:wght@400;700&display=swap' rel='stylesheet'><style>body{margin:0}</style></head><body>" + html + "</body></html>")
    open('preview/' + name + '.html', 'w').write(doc)

if __name__ == '__main__':
    hid, fid = (int(x) for x in (sys.argv[1:3] if len(sys.argv) > 2 else (0, 0)))
    s = build(hid, fid)
    for pid, (name, w) in PAGES.items():
        preview(name, w)
    print('pages', len(s), 'total KB', sum(s.values()) // 1024, {k: v // 1024 for k, v in s.items()})
    print('header', len(HDR), 'footer', len(FTR), 'css', len(open('site.css').read()))
