"""Build updated Elementor data for amasirvoyage.com pages.

Reads the untouched backups in ../backups/amasir/*.json and writes
out/<name>.json, the value to store in each post's _elementor_data meta.
"""
import copy, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BK = os.path.join(HERE, '..', 'backups', 'amasir')
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

U = 'https://amasirvoyage.com/wp-content/uploads/2026/10/'
PH = {
    'welcome': (8550, U + 'amasir-guests-marrakech-airport.jpg', 1600, 1200,
                'Amasir Voyage guide with four smiling travellers at Marrakech Menara airport'),
    'dune': (8551, U + 'sunset-jump-sahara-dunes.jpg', 1200, 1600,
             'Amasir Voyage guide jumping on top of a sand dune at sunset in the Moroccan desert'),
    'family': (8552, U + 'family-trip-mountain-viewpoint-morocco.jpg', 1200, 1600,
               'Family of four with their Amasir Voyage guide at a mountain viewpoint in Morocco'),
    'group': (8553, U + 'group-day-trip-morocco.jpg', 590, 787,
              'Group of young travellers smiling together with their guide during a day trip in Morocco'),
    'goodbye': (8554, U + 'family-group-marrakech-airport-departure.jpg', 1600, 738,
                'Two families with their Amasir Voyage guide at Marrakech airport at the end of their trip'),
}
PHONES = [('+212 660 751 249', '+212660751249'), ('+212 666 029 583', '+212666029583')]
EMAIL = 'contact@amasirvoyage.com'
SITE = 'https://amasirvoyage.com'


def load(name):
    with open(os.path.join(BK, name + '.json')) as f:
        return json.load(f)


def save(name, data):
    with open(os.path.join(OUT, name + '.json'), 'w') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))


def find(node, el_id):
    if isinstance(node, list):
        for n in node:
            r = find(n, el_id)
            if r is not None:
                return r
    elif isinstance(node, dict):
        if node.get('id') == el_id:
            return node
        return find(node.get('elements', []), el_id)
    return None


def img(key):
    i, url, w, h, alt = PH[key]
    return {'url': url, 'id': i, 'size': '', 'alt': alt, 'source': 'library'}


def html_widget(el_id, html):
    return {'id': el_id, 'elType': 'widget', 'settings': {'html': html}, 'elements': [], 'widgetType': 'html'}


def section(el_id, html):
    return {'id': el_id, 'elType': 'container',
            'settings': {'content_width': 'full',
                         'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True},
                         'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0', 'isLinked': True}},
            'elements': [html_widget(el_id + 'w', html)], 'isInner': False}


# ---------- shared look: sand paper, polaroids, handwritten notes ----------
CSS_RAW = """@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&display=swap');
.amx{overflow-x:clip;--o:#FF681A;--ink:#1f2430;--ink2:#5b6170;--sand:#faf3ea;--line:#efe2d2;font-size:17px;line-height:1.65;color:var(--ink2)}
.amx *{box-sizing:border-box}
.amx-wrap{max-width:1220px;margin:0 auto;padding:0 15px}
.amx-hand{font-family:'Caveat',cursive;font-weight:700;color:var(--o);font-size:28px;line-height:1;display:inline-block;transform:rotate(-2deg)}
.amx h2{color:var(--ink);font-size:clamp(28px,3.4vw,44px);line-height:1.15;margin:6px 0 14px}
.amx-head{text-align:center;max-width:680px;margin:0 auto 48px}
.amx-head p{margin:0}
.amx-band{position:relative;background:var(--sand);padding:110px 0 120px;overflow:hidden}
.amx-band:before,.amx-band:after{content:'';position:absolute;left:0;right:0;height:14px;background:radial-gradient(circle at 7px -2px,transparent 8px,var(--sand) 8.5px) 0 0/14px 14px repeat-x}
.amx-band:before{top:-1px;transform:scaleY(-1);background:radial-gradient(circle at 7px -2px,transparent 8px,#fff 8.5px) 0 0/14px 14px repeat-x}
.amx-band:after{display:none}
.amx-zz{position:absolute;inset:0;pointer-events:none;opacity:.5;background-image:radial-gradient(var(--line) 1.4px,transparent 1.6px);background-size:22px 22px;-webkit-mask-image:linear-gradient(180deg,#000,transparent 70%);mask-image:linear-gradient(180deg,#000,transparent 70%)}
.amx-wall{position:relative;display:grid;grid-template-columns:repeat(12,1fr);gap:26px;align-items:start}
.amx-pol{margin:0;background:#fff;padding:12px 12px 16px;border-radius:4px;box-shadow:0 1px 2px rgba(0,0,0,.06),0 22px 40px -22px rgba(31,36,48,.45);transform:rotate(var(--r,0deg));transition:transform .45s cubic-bezier(.2,.7,.2,1),box-shadow .45s;position:relative}
.amx-pol:hover{transform:rotate(0) translateY(-6px) scale(1.015);box-shadow:0 1px 2px rgba(0,0,0,.06),0 34px 60px -26px rgba(31,36,48,.55);z-index:3}
.amx-pol img{display:block;width:100%;height:auto;object-fit:cover;border-radius:2px;aspect-ratio:var(--ar,4/3)}
.amx-pol figcaption{font-family:'Caveat',cursive;font-size:23px;line-height:1.15;color:var(--ink);text-align:center;margin-top:10px}
.amx-pol:before{content:'';position:absolute;top:-11px;left:50%;width:92px;height:24px;margin-left:-46px;background:rgba(255,104,26,.22);transform:rotate(var(--t,-3deg));border-radius:2px}
.amx-a{grid-column:1/6;--r:-2.2deg;--ar:4/3}
.amx-b{grid-column:6/9;--r:1.8deg;--ar:3/4;margin-top:46px}
.amx-c{grid-column:9/13;--r:-1.2deg;--ar:3/4;--t:4deg}
.amx-d{grid-column:2/6;--r:1.6deg;--ar:3/4;margin-top:-40px;--t:2deg}
.amx-e{grid-column:6/12;--r:-1.4deg;--ar:16/9;margin-top:10px}
.amx-f{grid-column:3/11;--r:1.2deg;--ar:16/9;margin-top:10px}
.amx-cta{text-align:center;margin-top:56px}
.amx-btn{display:inline-flex;align-items:center;gap:10px;background:var(--o);color:#fff!important;font-weight:700;padding:15px 30px;border-radius:10px;text-decoration:none!important;transition:background .25s,transform .25s}
.amx-btn:hover{background:var(--ink);transform:translateY(-2px)}
.amx-btn.alt{background:transparent;color:var(--ink)!important;border:2px solid var(--ink)}
.amx-btn.alt:hover{background:var(--ink);color:#fff!important}
.amx-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;counter-reset:s}
.amx-step{position:relative;background:#fff;border:1px solid var(--line);border-radius:16px;padding:34px 28px 30px}
.amx-step:before{counter-increment:s;content:counter(s);position:absolute;top:-22px;left:24px;width:44px;height:44px;border-radius:50%;background:var(--o);color:#fff;font-weight:800;font-size:19px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 6px var(--sand)}
.amx-step h3{color:var(--ink);font-size:21px;margin:6px 0 8px}
.amx-step p{margin:0;font-size:16px}
.amx-split{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center}
.amx-split .amx-pol{--r:2deg;max-width:470px;margin-left:auto}
.amx-list{list-style:none;padding:0;margin:18px 0 0}
.amx-list li{position:relative;padding:0 0 12px 34px}
.amx-list li:before{content:'';position:absolute;left:0;top:5px;width:20px;height:20px;border-radius:50%;background:var(--o) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E") center/12px no-repeat}
.amx-list strong{color:var(--ink)}
.amx-reach{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.amx-reach a,.amx-reach div{display:block;background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px 24px;color:var(--ink2);text-decoration:none!important;transition:border-color .2s,transform .2s}
.amx-reach a:hover{border-color:var(--o);transform:translateY(-3px)}
.amx-reach b{display:block;color:var(--ink);font-size:18px;margin-bottom:4px}
@media (max-width:1024px){.amx-split{gap:44px}}
@media (max-width:900px){
 .amx-wall{grid-template-columns:1fr 1fr;gap:22px}
 .amx-a,.amx-e,.amx-f{grid-column:1/3;margin-top:0}
 .amx-b,.amx-c,.amx-d{grid-column:auto;margin-top:0}
 .amx-d{grid-column:1/3;max-width:420px;justify-self:center;width:100%}
 .amx-steps,.amx-reach{grid-template-columns:1fr;gap:34px}
 .amx-reach{gap:16px}
 .amx-split{grid-template-columns:1fr}
 .amx-split .amx-pol{margin:0 auto}
}
@media (max-width:600px){.amx-band{padding:70px 0 80px}.amx-wall{gap:16px}.amx-d{grid-column:auto;max-width:none}.amx-pol{padding:7px 7px 10px}.amx-pol:before{width:60px;margin-left:-30px;height:18px;top:-8px}.amx-pol figcaption{font-size:18px;margin-top:6px}.amx-a .amx-hand,.amx-hand{font-size:25px}}
@media (prefers-reduced-motion:reduce){.amx-pol,.amx-btn{transition:none}}
"""
CSS = ""


def pol(key, cls, caption, eager=False):
    i, url, w, h, alt = PH[key]
    load_attr = '' if eager else " loading='lazy'"
    return ("<figure class='amx-pol %s'><img src='%s' width='%d' height='%d' alt='%s'%s decoding='async'>"
            "<figcaption>%s</figcaption></figure>") % (cls, url, w, h, alt, load_attr, caption)


def wall(title_hand, title, intro, cta):
    return (CSS +
            "<section class='amx amx-band'><div class='amx-zz'></div><div class='amx-wrap'>"
            "<div class='amx-head'><span class='amx-hand'>%s</span><h2>%s</h2><p>%s</p></div>"
            "<div class='amx-wall'>" % (title_hand, title, intro) +
            pol('welcome', 'amx-a', 'First hello at Marrakech airport') +
            pol('dune', 'amx-b', 'Someone always jumps at sunset') +
            pol('family', 'amx-c', 'A family day up in the mountains') +
            pol('group', 'amx-d', 'Group day trip, all smiles') +
            pol('goodbye', 'amx-e', 'The hardest part: goodbye at the airport') +
            "</div>%s</div></section>" % cta)


# ================================ HOME ================================
home = load('home-8276')
hero = find(home, '4917349')['settings']['herotwo_slides']
hero[0].update({'sub_title': 'Private tours from Marrakech',
                'title': 'See Morocco with people who live here',
                'button_text': 'See our tours'})
hero[0]['bg_image']['alt'] = 'Travellers on a private tour with Amasir Voyage in Morocco'
hero[1].update({'sub_title': 'Desert, mountains & coast',
                'title': 'Day trips, desert tours & airport transfers',
                'button_text': 'Plan your trip',
                'link': SITE + '/contact/'})
hero[1]['bg_image']['alt'] = 'Moroccan landscape on an Amasir Voyage day trip'

intro = find(home, '63eec09')['settings']
intro['section_subtitle'] = 'We are Amasir Voyage'
intro['section_title'] = "Morocco, the way we'd show a friend"
intro['section_description'] = (
    "We're a small team of drivers and guides based in Marrakech. A lot of our trips start the same way: "
    "we meet you at arrivals, load the bags, and on the drive into town we talk about what you actually want "
    "to see.\n\n"
    "Some guests want the big loop over the Atlas to the Sahara. Others have one free day and just want to get "
    "out of the medina for a few hours. Either way the trip is private, planned around you, with sensible "
    "driving days and stops wherever there's something worth stopping for.")
find(home, 'bc6118e')['settings']['button_text'] = 'More about us'
about_img = find(home, '0fe6fcb')['settings']
about_img['image'] = img('welcome')
about_img['image_size'] = 'large'
about_img['image_border_radius'] = {'unit': 'px', 'top': '18', 'right': '18', 'bottom': '18', 'left': '18', 'isLinked': True}

tours = find(home, 'c80ba31')['settings']
tours['section_title'] = 'Where we can '
tours['section_title_two'] = 'take you'
tours['section_subtitle'] = 'Our tours'
tours['section_description'] = (
    "Day trips from Marrakech, a couple of nights in the desert, or two weeks across the country. "
    "These are the routes we run most often. If none of them fits, send us your dates and we'll put one together.")
find(home, 'b14944f')['settings']['button_text'] = 'See all tours'

feats = {
    'a089186': ('Comfortable rides', 'Careful drivers who know the roads, and a stop whenever you need one.'),
    'ea2ece7': ('Private, your way', 'Only your group in the car. Want to change the plan halfway? Just say so.'),
    'f212ff9': ('Airport pickups, day or night', "Early flight or late landing, we'll be waiting at arrivals."),
    '6914445': ('Local know-how', "We live here. We'll take you to the places we'd show our own family."),
}
for k, (t, d) in feats.items():
    s = find(home, k)['settings']
    s['title'], s['discription'] = t, d

home_wall = wall('Moments from the road', 'Real trips, real people',
                 "No stock photos here. These are our guests and our team, taken on the road with their phones.",
                 "<div class='amx-cta'><a class='amx-btn' href='%s/contact/'>Plan a trip with us</a></div>" % SITE)
# gallery goes between the tour slider and the feature boxes
idx = next(i for i, n in enumerate(home) if n['id'] == '179e405')
home.insert(idx, section('a7f31c2', home_wall))
save('home', home)

# ================================ ABOUT ================================
about = load('about-8277')
a_img = find(about, '61561ea')['settings']
a_img['image']['alt'] = 'Amasir Voyage guide with travellers in Morocco'
a_img['image_size'] = 'large'
a_img['image_border_radius'] = {'unit': 'px', 'top': '18', 'right': '18', 'bottom': '18', 'left': '18', 'isLinked': True}
at = find(about, '81f4fc0')['settings']
at['section_subtitle'] = 'About Amasir Voyage'
at['section_title'] = 'A small Marrakech team, not a call centre'
at['section_description'] = (
    "Amasir Voyage is a small team based in Marrakech. We run private day trips, multi-day tours and airport "
    "transfers across Morocco.\n\n"
    "Our regular day trips go to Agafay, the Ourika Valley, Imlil, Essaouira and the Ouzoud waterfalls. For "
    "longer trips we head over the Atlas to Merzouga and the Sahara, or north to Chefchaouen and Fes. If you "
    "have your own idea, we're happy to build the trip around it.\n\n"
    "We keep every trip private, plan realistic driving days, and leave a bit of room in the schedule for the "
    "things you only discover once you're here.")

cta = find(about, '567029c')['settings']
cta['section_title'] = 'Why travellers book with us'
cta['section_subtitle'] = (
    "Private trips only, so it's just you and the people you came with. Routes we know well, with honest "
    "timings. Drivers who know the roads and guides who know the stories. And a real person on the other end "
    "when you message us, before the trip and during it.")
cta['cta_img'] = img('family')
cta.pop('section_title_typography_font_size', None)

about_extra = (CSS +
    "<section class='amx amx-band'><div class='amx-zz'></div><div class='amx-wrap'>"
    "<div class='amx-head'><span class='amx-hand'>Simple as that</span><h2>How a trip with us works</h2>"
    "<p>No booking engine maze. You talk to us, we sort it out.</p></div>"
    "<div class='amx-steps'>"
    "<div class='amx-step'><h3>Tell us your plan</h3><p>Dates, how many of you, and roughly what you'd like to see. "
    "A rough idea is fine.</p></div>"
    "<div class='amx-step'><h3>We shape it together</h3><p>We send a day-by-day plan and a price. Change whatever "
    "you like until it feels right.</p></div>"
    "<div class='amx-step'><h3>We pick you up</h3><p>From the airport, your riad or hotel. After that, just enjoy "
    "the ride.</p></div>"
    "</div></div></section>" +
    "<section class='amx' style='padding:110px 0 40px;background:#fff'><div class='amx-wrap'>"
    "<div class='amx-head'><span class='amx-hand'>Our guests</span><h2>A few faces from recent trips</h2>"
    "<p>Families, friends, solo travellers and groups. Every trip ends with a photo, and we'll keep adding them here.</p></div>"
    "<div class='amx-wall'>" +
    pol('welcome', 'amx-a', 'First hello at Marrakech airport') +
    pol('dune', 'amx-b', 'Someone always jumps at sunset') +
    pol('group', 'amx-c', 'Group day trip, all smiles') +
    pol('goodbye', 'amx-f', 'The hardest part: goodbye at the airport') +
    "</div><div class='amx-cta'><a class='amx-btn' href='%s/trip-search-result/'>See our tours</a> "
    "<a class='amx-btn alt' href='%s/contact/'>Ask us anything</a></div></div></section>" % (SITE, SITE))
about.append(section('b3e81d4', about_extra))
save('about', about)

# ================================ CONTACT ================================
contact = load('contact-8279')
find(contact, 'd383d79')['settings']['contactbox_list'] = (
    "<p class=\"contact-box__text\">Lot El Massar N° 1106, 3ème étage</p><p>Marrakech, Morocco</p>")
tel = find(contact, '553451b')['settings']
tel['contactbox_icon'] = 'fas fa-phone-alt'
tel['contactbox_title'] = 'Call or WhatsApp'
tel['contactbox_list'] = ''.join("<p><a href=\"tel:%s\">%s</a></p>" % (n, d) for d, n in PHONES)
em = find(contact, 'c529d2b')['settings']
em['contactbox_icon'] = 'fas fa-envelope'
em['contactbox_list'] = "<p><a href=\"mailto:%s\">%s</a></p>" % (EMAIL, EMAIL)
ct = find(contact, '3857b7b')['settings']
ct['section_subtitle'] = 'Contact us'
ct['section_title'] = 'Tell us about your trip'
ct['section_description'] = (
    "Send us your dates, how many of you are travelling and roughly what you'd like to see. We'll reply with a "
    "plan and a price, with no obligation to book.\n\n"
    "Prefer to talk? Call or message us on the numbers above. Questions about a transfer or a single day trip "
    "are just as welcome as a two-week tour.")
# small human touch above the form
form_box = find(contact, '7cef427')
form_box['elements'].insert(0, html_widget('c6d92e1', CSS +
    "<div class='amx' style='margin:0 auto 46px;max-width:860px'><div class='amx-split' style='gap:40px'>"
    "<div><span class='amx-hand'>See you at arrivals</span>"
    "<ul class='amx-list'><li><strong>Tell us your dates</strong> and how many of you are coming</li>"
    "<li><strong>Private trips only</strong>, just your group</li>"
    "<li><strong>Pickups</strong> from the airport, your riad or hotel</li></ul></div>" +
    pol('welcome', '', 'We meet you right at the exit') +
    "</div></div>"))
save('contact', contact)

# ================================ HEADER ================================
header = load('header-38')
info = find(header, '9000a55')['settings']['infolink_list']
info[1]['info_text'] = PHONES[1][0]
info[1]['info_url'] = 'tel:' + PHONES[1][1]
mob = find(header, 'c837b04')['settings']
mob['logo'] = {'url': SITE + '/wp-content/uploads/2026/08/ChatGPT-Image-6-aout-2026-10_38_41.png',
               'id': 8406, 'size': '', 'alt': 'Amasir Voyage', 'source': 'library'}
mob['logo_link'] = SITE + '/'
srch = find(header, '668d07d')['settings']
srch['placeholder_text'] = 'Search tours...'
save('header', header)

# ================================ FOOTER ================================
footer = load('footer-41')
fc = find(footer, 'fb258db')['settings']
fc['section_title'] = 'Ready when you are'
fc['section_subtitle'] = "Tell us your dates and we'll plan the rest"
fc['sub_title'] = 'Morocco is calling'
fc['button_text'] = 'Our tours'
find(footer, 'e3c8199')['settings']['image']['alt'] = 'Amasir Voyage'
find(footer, 'a353b7b')['settings']['editor'] = (
    "<p class=\"footer-text\">Private tours, day trips and airport transfers from Marrakech, run by a small local team.</p>"
    "<p class=\"footer-text\" style=\"margin-top:14px;line-height:1.9\">"
    + ''.join("<a href=\"tel:%s\">%s</a><br>" % (n, d) for d, n in PHONES)
    + "<a href=\"mailto:%s\">%s</a></p>" % (EMAIL, EMAIL))
for mid in ('da3e3e8', '23a6776'):
    for it in find(footer, mid)['settings']['menu_texts']:
        it['menu_text'] = it['menu_text'].strip()
        it['text_link']['is_external'] = False
        it['text_link']['nofollow'] = False
find(footer, 'db8281b')['settings']['editor'] = "<h4 class=\"widget_title\">Popular Trips</h4>"
find(footer, '10cc01a')['settings']['editor'] = "<h4 class=\"widget_title\">Newsletter</h4>"
find(footer, '0b37e5b')['settings']['editor'] = "<p class=\"form_text\">Seasonal ideas and the odd special offer. No spam, ever.</p>"
cp = find(footer, '8c378e9')['settings']
cp['editor'] = "<p class=\"copyright-text\">© 2026 <a href=\"%s\">Amasir Voyage</a>, Marrakech. All rights reserved.</p>" % SITE
cp.pop('text_color', None)
cp.pop('typography_typography', None)
save('footer', footer)

# ================================ OFF-CANVAS ================================
offc = [{'id': 'fce6937', 'elType': 'container',
         'settings': {'flex_gap': {'column': '0', 'row': '0', 'isLinked': False, 'unit': 'px', 'size': 0},
                      'padding': {'unit': 'px', 'top': '0', 'right': '15', 'bottom': '0', 'left': '15', 'isLinked': False},
                      'content_width': 'full'},
         'elements': [
             {'id': 'd27ea5e', 'elType': 'widget',
              'settings': {'_margin': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '20', 'left': '0', 'isLinked': False},
                           'image_width': {'unit': 'px', 'size': 140, 'sizes': []}},
              'elements': [], 'widgetType': 'travolologo'},
             html_widget('a64ca3a', CSS +
                 "<div class='amx' style='margin-top:26px'>"
                 "<span class='amx-hand'>Say salam</span>"
                 "<p style='margin:10px 0 18px'>Questions about a tour or a transfer? Message us any time.</p>"
                 "<p style='margin:0 0 6px'><b style='color:var(--ink)'>Phone / WhatsApp</b><br>"
                 + '<br>'.join("<a href='tel:%s'>%s</a>" % (n, d) for d, n in PHONES) +
                 "</p><p style='margin:14px 0 22px'><b style='color:var(--ink)'>Email</b><br>"
                 "<a href='mailto:%s'>%s</a></p>" % (EMAIL, EMAIL) +
                 pol('dune', '', 'Sunset in the dunes') +
                 "</div>"),
         ], 'isInner': False}]
save('offcanvas', offc)

import re
mini = re.sub(r'\s*\n\s*', '', CSS_RAW)
with open(os.path.join(OUT, 'custom.css'), 'w') as f:
    f.write(mini)

for n in sorted(os.listdir(OUT)):
    print(n, os.path.getsize(os.path.join(OUT, n)))
