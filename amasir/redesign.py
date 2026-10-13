"""Full redesign of amasirvoyage.com (header, footer, Home, About, Contact, Activities).

Writes out2/<name>.json (values for each post's _elementor_data meta) and
out2/custom.css (the site's Additional CSS, post 7424). Also writes
preview/<page>.html for local screenshots.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out2')
PRE = os.path.join(HERE, 'preview')
os.makedirs(OUT, exist_ok=True)
os.makedirs(PRE, exist_ok=True)

S = 'https://amasirvoyage.com'
UP = S + '/wp-content/uploads/'
LOGO = UP + '2026/08/ChatGPT-Image-6-aout-2026-10_38_41.png'
WA_NUM = '212660751249'
WA = 'https://wa.me/' + WA_NUM + '?text=' + 'Hello%20Amasir%20Voyage%2C%20I%27d%20like%20to%20plan%20a%20trip'
PHONES = [('+212 660 751 249', '+212660751249'), ('+212 666 029 583', '+212666029583')]
EMAIL = 'contact@amasirvoyage.com'

G = {  # our guest photos (Oct 2026 uploads)
    'welcome': (UP + '2026/10/amasir-guests-marrakech-airport.jpg', 1600, 1200, 'Amasir Voyage guide with four smiling travellers at Marrakech Menara airport'),
    'dune': (UP + '2026/10/sunset-jump-sahara-dunes.jpg', 1200, 1600, 'Amasir Voyage guide jumping on top of a sand dune at sunset'),
    'family': (UP + '2026/10/family-trip-mountain-viewpoint-morocco.jpg', 1200, 1600, 'Family of four with their Amasir Voyage guide at a mountain viewpoint'),
    'group': (UP + '2026/10/group-day-trip-morocco.jpg', 590, 787, 'Group of young travellers smiling with their guide on a day trip'),
    'goodbye': (UP + '2026/10/family-group-marrakech-airport-departure.jpg', 1600, 738, 'Two families with their Amasir Voyage guide at Marrakech airport'),
}
HERO_HOME = UP + '2026/08/WhatsApp-Image-2026-08-06-at-11.25.07-AM.jpeg'
HERO_ABOUT = UP + '2026/08/WhatsApp-Image-2026-08-06-at-11.25.06-AM2-1.jpeg'


def u(path):
    return UP + '2026/08/' + path


# (title, slug, full image, card image, chip, description)
DAY = [
    ('Agafay Desert Day Trip', 'agafay-desert-day-trip', u('buggy-tour-agafay-desert-view-1536x864-1.jpg'), u('buggy-tour-agafay-desert-view-1536x864-1-705x540.jpg'), 'Day trip',
     'The stony desert just outside Marrakech, with the Atlas on the horizon. Optional camel or quad, then sunset and dinner at a camp.'),
    ('Imlil & High Atlas Mountains', 'imlil-high-atlas-mountains-day-trip', u('images.jpg'), u('images.jpg'), 'Day trip',
     'Berber villages, walnut terraces and the foot of Toubkal, about an hour and a half from the city.'),
    ('Ouzoud Waterfalls', 'ouzoud-waterfalls-day-trip', u('sf26aalgw5y00sc66eqk.jpg'), u('sf26aalgw5y00sc66eqk-705x469.jpg'), 'Day trip',
     'The big falls in the Middle Atlas, olive groves on the way down and the local macaques.'),
    ('Essaouira from Marrakech', 'essaouira-day-trip-from-marrakech', u('WhatsApp-Image-2026-08-06-at-9.05.03-PM.jpeg'), u('WhatsApp-Image-2026-08-06-at-9.05.03-PM-705x540.jpeg'), 'Day trip',
     'Blue boats, the old ramparts and grilled fish by the port, on the Atlantic coast.'),
    ('Ourika Valley', 'ourika-valley-day-trip-from-marrakech', u('WhatsApp-Image-2026-08-06-at-9.07.24-PM1.jpeg'), u('WhatsApp-Image-2026-08-06-at-9.07.24-PM1-705x540.jpeg'), 'Day trip',
     'A green river valley in the Atlas foothills. An easy first day out of the city.'),
]
TOURS = [
    ('3-Day Merzouga Desert Adventure', '3-day-merzouga-desert-adventure', u('pexels-mographe-30254941.jpg'), u('pexels-mographe-30254941-705x540.jpg'), '3 days',
     'Over the Atlas and down the valleys to the Erg Chebbi dunes, with a night in a desert camp.'),
    ('Blue City to Sahara', 'blue-city-to-sahara', u('pexels-alaritammsalu-37064558-scaled.jpg'), u('pexels-alaritammsalu-37064558-705x540.jpg'), '4 days',
     'From Tangier through Chefchaouen and Fes to Merzouga, then Todra, Dades and Ait Ben Haddou to Marrakech.'),
    ('5-Day Sahara Trekking', '5-day-sahara-trekking-adventure', u('pexels-tom-d-arby-3904203-68076461-scaled.jpg'), u('pexels-tom-d-arby-3904203-68076461-705x540.jpg'), '5 days',
     'Walking days in the desert, camels for the bags and nights under a lot of stars.'),
    ('8-Day Desert & Coast', '8-day-morocco-desert-coast-escape', u('WhatsApp-Image-2026-08-06-at-9.10.12-PM.jpeg'), u('WhatsApp-Image-2026-08-06-at-9.10.12-PM-705x540.jpeg'), '8 days',
     'Sahara dunes, kasbahs and gorges, finishing with a few slow days on the Atlantic.'),
    ('15-Day Grand Morocco', '15-day-grand-morocco-discovery', u('pexels-the-trvlr-5614643-scaled.jpg'), u('pexels-the-trvlr-5614643-705x540.jpg'), '15 days',
     'The whole country in one trip: imperial cities, the mountains, the desert and the coast.'),
]
ACTS = [
    ('Hot Air Balloon at Sunrise', 'marrakech-hot-air-balloon-adventure', u('pexels-leos-37736075-scaled.jpg'), u('pexels-leos-37736075-600x810.jpg'),
     'An early start and a quiet hour above the plains as the sun comes up over the Atlas.'),
    ('Agafay Dinner & Live Show', 'agafay-desert-dinner-live-show', u('WhatsApp-Image-2026-08-07-at-1.02.52-AM.jpeg'), u('WhatsApp-Image-2026-08-07-at-1.02.52-AM-600x810.jpeg'),
     'Sunset in the desert, a Moroccan dinner and music around the fire.'),
    ('Quad Biking', 'quad-biking', u('WhatsApp-Image-2026-08-07-at-1.02.51-AM2.jpeg'), u('WhatsApp-Image-2026-08-07-at-1.02.51-AM2-600x810.jpeg'),
     'A couple of hours on desert tracks just outside the city.'),
    ('Dromedary Ride', 'dromedary-ride', u('WhatsApp-Image-2026-08-07-at-1.02.51-AM1.jpeg'), u('WhatsApp-Image-2026-08-07-at-1.02.51-AM1-600x810.jpeg'),
     'A slow ride at golden hour. Good with kids, and the best photos of the day.'),
]

# ---------------- icons ----------------
def ic(p, fill=False):
    a = "fill='currentColor'" if fill else "fill='none' stroke='currentColor' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'"
    return "<svg viewBox='0 0 24 24' %s aria-hidden='true'>%s</svg>" % (a, p)

I_WA = ic("<path d='M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.8 2.3 1 2.5c.1.2 1.6 2.5 4 3.5 1.5.6 2 .7 2.8.6.4-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.4-.2z'/>", True)
I_PH = ic("<path d='M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z'/>")
I_ML = ic("<rect x='3' y='5' width='18' height='14' rx='2'/><path d='m3 7 9 6 9-6'/>")
I_PIN = ic("<path d='M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z'/><circle cx='12' cy='9.5' r='2.5'/>")
I_CAR = ic("<path d='M5 17h14M3 13l2-5.5A2 2 0 0 1 6.9 6h10.2a2 2 0 0 1 1.9 1.5L21 13v4h-2'/><path d='M5 17H3v-4h18'/><circle cx='7.5' cy='17' r='1.8'/><circle cx='16.5' cy='17' r='1.8'/>")
I_USR = ic("<circle cx='9' cy='8' r='3.5'/><path d='M2.5 20a6.5 6.5 0 0 1 13 0'/><path d='M16 4.5a3.5 3.5 0 0 1 0 7M18.5 20a6.5 6.5 0 0 0-3-5.5'/>")
I_PLN = ic("<path d='M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z'/>")
I_MAP = ic("<path d='M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2z'/><path d='M9 4v14M15 6v14'/>")
I_CHAT = ic("<path d='M21 12a8 8 0 0 1-11.6 7.2L4 21l1.8-5.4A8 8 0 1 1 21 12z'/>")

STAMP = ("<div class='am-stamp' aria-hidden='true'><svg viewBox='0 0 136 136'><defs><path id='amc' d='M68 68m-50 0a50 50 0 1 1 100 0a50 50 0 1 1-100 0'/></defs>"
         "<text font-family='Inter,sans-serif' font-size='11.5' font-weight='600' letter-spacing='3.2' fill='%s'><textPath href='#amc'>PRIVATE TOURS &#183; MARRAKECH &#183; MOROCCO &#183; </textPath></text></svg><b>&#10022;</b></div>")


def hero_bg(src, alt):
    return "<div class='am-hero-bg'>%s</div>" % img_tag(src, alt, eager=True)


def img_tag(src, alt, w=None, h=None, full=None, eager=False, cls=''):
    a = " width='%d' height='%d'" % (w, h) if w else ''
    f = " data-full='%s' onerror='this.onerror=null;this.src=this.dataset.full'" % full if full and full != src else ''
    l = " fetchpriority='high'" if eager else " loading='lazy'"
    c = " class='%s'" % cls if cls else ''
    return "<img src='%s' alt='%s'%s%s%s decoding='async'%s>" % (src, alt, a, l, f, c)


def trip_card(t, dark=False):
    title, slug, full, card, chip, desc = t
    return ("<a class='am-trip' href='%s/trip/%s/'><div class='am-trip-i'>%s<span class='am-chip'>%s</span></div>"
            "<div class='am-trip-b'><h3>%s</h3><p>%s</p><span class='am-go'>See the trip</span></div></a>") % (
        S, slug, img_tag(card, title, full=full), chip, title.replace('&', '&amp;'), desc)


def act_card(a):
    title, slug, full, card, desc = a
    return ("<a class='am-act' href='%s/trip/%s/'><div class='am-act-i'>%s</div><h3>%s</h3><p>%s</p><span class='am-go'>Details</span></a>") % (
        S, slug, img_tag(card, title, full=full), title.replace('&', '&amp;'), desc)


def pol(key, cls, cap):
    src, w, h, alt = G[key]
    return "<figure class='am-pol %s'>%s<figcaption>%s</figcaption></figure>" % (cls, img_tag(src, alt, w, h), cap)


def wall(keys):
    caps = {'welcome': 'First hello at Marrakech airport', 'dune': 'Someone always jumps at sunset',
            'family': 'A family day up in the mountains', 'group': 'Group day trip, all smiles',
            'goodbye': 'The hardest part: goodbye at the airport'}
    return "<div class='am-wall'>" + ''.join(pol(k, c, caps[k]) for k, c in keys) + "</div>"


def cta(title, text):
    return ("<section class='am am-sec am-sec--white' style='padding-top:40px'><div class='am-w'><div class='am-cta'>"
            "<div><span class='am-hand'>Yalla, let's plan it</span><h2>%s</h2></div>"
            "<div class='am-btns'><a class='am-btn am-btn--white' href='%s' target='_blank' rel='noopener'>%s WhatsApp us</a>"
            "<a class='am-btn am-btn--ghost' href='%s/contact/'>Send a message</a></div></div></div></section>") % (title, WA, I_WA, S)


def steps():
    return ("<section class='am am-sec am-sec--white'><div class='am-w'><div class='am-sh'><div><span class='am-eb'>How it works</span>"
            "<h2>Booking is a <em>conversation</em>, not a form</h2></div><p>No booking engine maze and no surprises on the day. You talk to us, we sort the rest.</p></div>"
            "<div class='am-steps'>"
            "<div class='am-step'><b>01</b><h3>Tell us your plan</h3><p>Dates, how many of you, and roughly what you'd like to see. A rough idea is plenty.</p></div>"
            "<div class='am-step'><b>02</b><h3>We shape it together</h3><p>We send a day-by-day plan and a price. Change anything until it feels right.</p></div>"
            "<div class='am-step'><b>03</b><h3>We pick you up</h3><p>At the airport, your riad or your hotel. From there, just enjoy the road.</p></div>"
            "</div></div></section>")


# ================================ HEADER ================================
NAV = [('Home', '/'), ('Day trips', '/#day-trips'), ('Tours', '/#tours'), ('Activities', '/activities/'), ('About', '/about/'), ('Contact', '/contact/')]
nav_links = ''.join("<a href='%s%s'>%s</a>" % (S, h, t) for t, h in NAV)
panel_links = ''.join("<a class='amh-l' href='%s%s'>%s<span>&#8594;</span></a>" % (S, h, t) for t, h in NAV)
H_TOP = ("<div class='amh-top'><div class='am-w'><span class='amh-tagline'>Private tours, day trips &amp; airport transfers from Marrakech</span>"
         "<div><a href='mailto:%s'>%s</a><a href='tel:%s'>%s</a></div></div></div>") % (EMAIL, EMAIL, PHONES[0][1], PHONES[0][0])
H_BRAND = ("<div class='amh-brand'><a class='amh-logo' href='%s/' aria-label='Amasir Voyage home'><img src='%s' alt='Amasir Voyage' width='1657' height='949'></a></div>") % (S, LOGO)
H_NAV = "<nav class='amh-nav' aria-label='Main menu'>%s</nav>" % nav_links
H_ACT = ("<div class='amh-act'><a class='am-btn amh-wa' href='%s' target='_blank' rel='noopener' aria-label='WhatsApp Amasir Voyage'>%s<span>WhatsApp</span></a>"
         "<button type='button' class='amh-burger' aria-label='Open menu' aria-expanded='false'><i></i><i></i><i></i></button></div>"
         "<div class='amh-ov'></div><nav class='amh-panel' aria-label='Mobile menu'><div class='amh-ph'><img src='%s' alt='Amasir Voyage'>"
         "<button type='button' class='amh-x' aria-label='Close menu'><i></i><i></i></button></div>%s"
         "<div class='amh-pc'><a class='am-btn amh-wa' href='%s' target='_blank' rel='noopener'>%s WhatsApp %s</a>"
         "<a class='am-btn am-btn--line' href='mailto:%s'>%s %s</a><small>We usually answer the same day.</small></div></nav>"
         "<script>(function(){var d=document,r=d.documentElement,b=d.querySelector('.amh-burger');if(!b)return;"
         "function t(o){r.classList.toggle('amh-open',o);b.setAttribute('aria-expanded',o?'true':'false')}"
         "b.addEventListener('click',function(){t(true)});d.querySelector('.amh-x').addEventListener('click',function(){t(false)});"
         "d.querySelector('.amh-ov').addEventListener('click',function(){t(false)});d.querySelectorAll('.amh-l').forEach(function(a){a.addEventListener('click',function(){t(false)})});"
         "d.addEventListener('keydown',function(e){if(e.key==='Escape')t(false)});"
         "var p=location.pathname;d.querySelectorAll('.amh-nav a,.amh-l').forEach(function(a){var h=a.getAttribute('href').replace('%s','');if(h===p||(h.length>1&&h.charAt(1)!=='#'&&p.indexOf(h)===0))a.classList.add('on')})})();</script>"
         ) % (WA, I_WA, LOGO, panel_links, WA, I_WA, PHONES[0][0], EMAIL, I_ML, EMAIL, S)
H_ACT = H_ACT.replace("We usually answer the same day.", "Call us: " + PHONES[1][0])


def w_html(el_id, html, cls=''):
    s = {'html': html}
    if cls:
        s['_css_classes'] = cls
    return {'id': el_id, 'elType': 'widget', 'settings': s, 'elements': [], 'widgetType': 'html'}


def w_short(el_id, code, cls=''):
    s = {'shortcode': code}
    if cls:
        s['_css_classes'] = cls
    return {'id': el_id, 'elType': 'widget', 'settings': s, 'elements': [], 'widgetType': 'shortcode'}


Z = {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
GAP0 = {'unit': 'px', 'size': 0, 'column': '0', 'row': '0', 'isLinked': True}


def con(el_id, elements, cls='', row=False, inner=False):
    s = {'content_width': 'full', 'padding': Z, 'margin': Z, 'flex_gap': GAP0}
    if row:
        s.update({'flex_direction': 'row', 'flex_align_items': 'center', 'flex_justify_content': 'space-between', 'flex_wrap': 'nowrap'})
    if cls:
        s['css_classes'] = cls
    return {'id': el_id, 'elType': 'container', 'settings': s, 'elements': elements, 'isInner': inner}


header = [
    con('ah00001', [w_html('ah0001w', H_TOP)]),
    con('ah00002', [con('ah00003', [
        w_html('ah0002w', H_BRAND),
        w_html('ah0003w', H_NAV, 'amh-navw'),
        w_short('ah0004w', '[gtranslate]', 'amh-lang'),
        w_html('ah0005w', H_ACT),
    ], 'amh-row', row=True, inner=True)], 'amh-bg'),
]

# ================================ FOOTER ================================
popular = [DAY[0], DAY[3], TOURS[0], TOURS[1], TOURS[4]]
F = ("<footer class='amf'><div class='am-w'><div class='amf-g'>"
     "<div><a class='amf-logo' href='%s/'><img src='%s' alt='Amasir Voyage' width='1657' height='949' loading='lazy'></a>"
     "<p class='amf-big'>Private trips across Morocco, run by a small team <em>from Marrakech</em>.</p>"
     "<a class='am-btn amh-wa' href='%s' target='_blank' rel='noopener'>%s WhatsApp us</a></div>"
     "<div><h4>Explore</h4><ul>%s</ul></div>"
     "<div><h4>Popular trips</h4><ul>%s</ul></div>"
     "<div><h4>Get in touch</h4><ul class='amf-c'>"
     "<li>%s<span><a href='tel:%s'>%s</a><br><a href='tel:%s'>%s</a></span></li>"
     "<li>%s<a href='mailto:%s'>%s</a></li>"
     "<li>%s<span>Lot El Massar N&#176; 1106, 3&#232;me &#233;tage<br>Marrakech, Morocco</span></li></ul></div>"
     "</div><div class='amf-bot'><span>&#169; 2026 Amasir Voyage, Marrakech. All rights reserved.</span><span class='amf-dev'>By <a href='https://www.majdoulinean.com' target='_blank' rel='noopener'>majdoulinean</a></span></div></div></footer>"
     ) % (S, LOGO, WA, I_WA,
          ''.join("<li><a href='%s%s'>%s</a></li>" % (S, h, t) for t, h in NAV[1:] + [('All trips', '/trip-search-result/')]),
          ''.join("<li><a href='%s/trip/%s/'>%s</a></li>" % (S, t[1], t[0].replace('&', '&amp;')) for t in popular),
          I_PH, PHONES[0][1], PHONES[0][0], PHONES[1][1], PHONES[1][0], I_ML, EMAIL, EMAIL, I_PIN)
footer = [con('af00001', [w_html('af0001w', F)])]

# ================================ HOME ================================
KEYS = {  # extra words people type when looking for a trip
    'agafay-desert-day-trip': 'agafay desert camel quad sunset dinner camp',
    'imlil-high-atlas-mountains-day-trip': 'imlil atlas mountains toubkal berber villages hiking',
    'ouzoud-waterfalls-day-trip': 'ouzoud waterfalls cascades monkeys macaques',
    'essaouira-day-trip-from-marrakech': 'essaouira coast ocean beach port mogador',
    'ourika-valley-day-trip-from-marrakech': 'ourika valley river atlas setti fatma',
    '3-day-merzouga-desert-adventure': 'merzouga sahara desert erg chebbi camel camp dunes 3 days',
    'blue-city-to-sahara': 'chefchaouen blue city tangier fes sahara merzouga 4 days',
    '5-day-sahara-trekking-adventure': 'sahara desert trekking walking camel 5 days',
    '8-day-morocco-desert-coast-escape': 'desert coast sahara essaouira kasbah 8 days',
    '15-day-grand-morocco-discovery': 'grand tour imperial cities fes rabat chefchaouen sahara 15 days',
    'marrakech-hot-air-balloon-adventure': 'hot air balloon sunrise montgolfiere',
    'agafay-desert-dinner-live-show': 'agafay dinner show music evening',
    'quad-biking': 'quad atv buggy palmeraie',
    'dromedary-ride': 'dromedary camel ride sunset',
}
SDATA = ([{'t': t[0], 'u': S + '/trip/' + t[1] + '/', 'c': t[4], 'k': KEYS[t[1]]} for t in DAY + TOURS]
         + [{'t': a[0], 'u': S + '/trip/' + a[1] + '/', 'c': 'Activity', 'k': KEYS[a[1]]} for a in ACTS])
I_SRCH = ic("<circle cx='11' cy='11' r='7'/><path d='m20 20-3.5-3.5'/>")
SEARCH = ("<form class='am-search' role='search' autocomplete='off'><label>%s"
          "<input type='search' placeholder='Where to? Agafay, Merzouga, Essaouira...' aria-label='Search a trip'>"
          "<button type='submit'>Search</button></label><ul class='am-sr' hidden></ul></form>"
          "<script>(function(){var T=%s,f=document.querySelector('.am-search');if(!f)return;"
          "var i=f.querySelector('input'),l=f.querySelector('.am-sr'),r=[];"
          "function n(x){return x.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}"
          "function e(x){return x.replace(/&/g,'&amp;').replace(/</g,'&lt;')}"
          "function show(){var q=n(i.value.trim());if(!q){l.hidden=true;return}"
          "var w=q.split(/\\s+/);r=T.filter(function(t){var h=n(t.t+' '+t.k);return w.every(function(x){return h.indexOf(x)>-1})});"
          "l.innerHTML=r.length?r.slice(0,8).map(function(t,j){return '<li><a href=\"'+t.u+'\"'+(j?'':' class=\"on\"')+'>'+e(t.t)+'<small>'+e(t.c)+'</small></a></li>'}).join('')"
          ":'<li class=\"am-none\">No trip with that name yet. <a href=\"%s\" target=\"_blank\" rel=\"noopener\">Ask us on WhatsApp</a>, we can plan it.</li>';l.hidden=false}"
          "i.addEventListener('input',show);i.addEventListener('focus',show);"
          "f.addEventListener('submit',function(ev){ev.preventDefault();show();if(r.length)location.href=r[0].u});"
          "document.addEventListener('click',function(ev){if(!f.contains(ev.target))l.hidden=true});"
          "i.addEventListener('keydown',function(ev){if(ev.key==='Escape')l.hidden=true})})();</script>"
          ) % (I_SRCH, json.dumps(SDATA, ensure_ascii=False), WA)
k = lambda title, n, href, img, full, text: (
    "<a class='am-kind' href='%s'>%s<div class='am-kind-b'><span class='am-kind-n'>%s</span><h3>%s</h3><p>%s</p><span class='am-go'>Show me</span></div></a>"
    % (href, img_tag(img, title, full=full), n, title, text))
H1 = ("<section class='am am-hero'>%s<div class='am-hero-note'>your trip could<br>start right here<svg viewBox='0 0 70 60' fill='none' stroke='currentColor' stroke-width='2.2' stroke-linecap='round'><path d='M60 4C48 20 30 30 12 46'/><path d='M10 30 11 47 27 45'/></svg></div>"
      "<div class='am-w'><span class='am-eb'>Amasir Voyage &#183; Marrakech</span>"
      "<h1>Morocco, shown by people who <em>live here</em></h1>"
      "<p class='am-hero-lead'>Private day trips, desert tours and airport pickups from Marrakech. Small team, local drivers and guides, and plans built around you.</p>"
      "%s<div class='am-btns' style='margin-top:18px'><a class='am-btn am-btn--terra' href='#day-trips'>Browse our trips</a><a class='am-btn am-btn--ghost' href='%s' target='_blank' rel='noopener'>%s Ask us on WhatsApp</a></div>"
      "</div></section>") % (hero_bg(HERO_HOME, 'Travellers in the Moroccan desert on an Amasir Voyage trip'), SEARCH, WA, I_WA)
H2 = ("<section class='am am-sec'><div class='am-w'><div class='am-sh'><div><span class='am-eb'>Where to start</span><h2>Pick the <em>kind</em> of trip you have time for</h2></div>"
      "<p>One free day, a few nights in the desert or the whole country. Choose a starting point and we'll adjust the details with you.</p></div><div class='am-kinds'>"
      + k('Day trips', '5 trips', '#day-trips', u('buggy-tour-agafay-desert-view-1536x864-1-600x810.jpg'), u('buggy-tour-agafay-desert-view-1536x864-1.jpg'), 'Out of Marrakech in the morning, back for dinner.')
      + k('Multi-day tours', '5 tours', '#tours', u('pexels-mographe-30254941-600x810.jpg'), u('pexels-mographe-30254941.jpg'), 'Mountains, kasbahs and nights in the Sahara.')
      + k('Activities', '4 activities', S + '/activities/', u('pexels-leos-37736075-600x810.jpg'), u('pexels-leos-37736075-scaled.jpg'), 'Balloons at sunrise, quads, camels and dinner shows.')
      + "</div></div></section>")
src, w, h, alt = G['welcome']
H3 = ("<section class='am am-sec am-sec--white'><div class='am-w am-split'>"
      "<div class='am-arch'>%s%s</div>"
      "<div class='am-tx'><span class='am-eb'>We are Amasir Voyage</span><h2>Morocco, the way we'd show <em>a friend</em></h2>"
      "<p>We're a small team of drivers and guides based in Marrakech. A lot of our trips start the same way: we meet you at arrivals, load the bags, and on the drive into town we talk about what you actually want to see.</p>"
      "<p>Some guests want the big loop over the Atlas to the Sahara. Others have one free day and just want to get out of the medina for a few hours. Either way the trip is private, planned around you, with sensible driving days and stops wherever there's something worth stopping for.</p>"
      "<span class='am-sign'>&#8212; the Amasir team</span>"
      "<div class='am-btns' style='margin-top:30px'><a class='am-btn am-btn--line' href='%s/about/'>More about us</a></div></div>"
      "</div></section>") % (img_tag(src, alt, w, h), STAMP % '#221C17', S)
H4 = ("<section class='am am-sec am-sec--sand' id='day-trips'><div class='am-w'><div class='am-sh'><div><span class='am-eb'>Day trips from Marrakech</span>"
      "<h2>Out in the morning, <em>back for dinner</em></h2></div><p>Pickup from your riad or hotel, a private car and driver, and the day at your pace.</p></div>"
      "<div class='am-trips'>" + ''.join(trip_card(t) for t in DAY) + "</div></div></section>")
H5 = ("<section class='am am-sec am-sec--ink' id='tours'><div class='am-w'><div class='am-sh'><div><span class='am-eb'>Multi-day tours</span>"
      "<h2>A few nights <em>further out</em></h2></div><p>Over the Atlas to the dunes, north to the blue city, or the whole country. Every itinerary can be stretched, shortened or reshuffled.</p></div>"
      "<div class='am-trips'>" + ''.join(trip_card(t) for t in TOURS) + "</div>"
      "<div class='am-more-row'><a class='am-btn am-btn--ghost' href='%s/trip-search-result/'>See all trips</a></div></div></section>") % S
H6 = ("<section class='am am-sec'><div class='am-w'><div class='am-sh am-sh--c'><span class='am-hand'>Moments from the road</span>"
      "<h2>Real trips, <em>real people</em></h2><p>No stock photos here. These are our guests and our team, taken on the road with their phones.</p></div>"
      + wall([('welcome', 'am-pa'), ('dune', 'am-pb'), ('family', 'am-pc'), ('group', 'am-pd'), ('goodbye', 'am-pe')]) + "</div></section>")
H7 = ("<section class='am am-sec am-sec--sand'><div class='am-w'><div class='am-sh'><div><span class='am-eb'>Activities</span><h2>Got a free <em>afternoon</em>?</h2></div>"
      "<p>Short experiences around Marrakech. Book one on its own or add it to a day trip.</p></div>"
      "<div class='am-acts'>" + ''.join(act_card(a) for a in ACTS) + "</div></div></section>")
home_html = [H1, H2, H3, H4, H5, H6, H7, steps(), cta("Tell us your dates. <em>We'll do the rest.</em>",
             "A quick message is enough to start: when you arrive, how many of you, and what you'd love to see.")]
home = [con('am0home', [w_html('amh%02dw' % i, x) for i, x in enumerate(home_html)])]

# ================================ ABOUT ================================
A1 = ("<section class='am am-hero am-hero--sm'>%s<div class='am-w'><span class='am-eb'>About us</span>"
      "<h1>A small Marrakech team, <em>not a call centre</em></h1>"
      "<p class='am-hero-lead'>Drivers and guides who live here, planning private trips we'd be happy to take our own families on.</p></div></section>") % hero_bg(HERO_ABOUT, 'Amasir Voyage guide with travellers in Morocco')
src, w, h, alt = G['family']
A2 = ("<section class='am am-sec am-sec--white'><div class='am-w am-split'>"
      "<div class='am-tx'><span class='am-eb'>Our story, in short</span><h2>Trips built around <em>people</em>, not packages</h2>"
      "<p>Amasir Voyage is a small team based in Marrakech. We run private day trips, multi-day tours and airport transfers across Morocco.</p>"
      "<p>Our regular day trips go to Agafay, the Ourika Valley, Imlil, Essaouira and the Ouzoud waterfalls. For longer trips we head over the Atlas to Merzouga and the Sahara, or north to Chefchaouen and Fes. If you have your own idea, we're happy to build the trip around it.</p>"
      "<p>We keep every trip private, plan realistic driving days, and leave a bit of room in the schedule for the things you only discover once you're here.</p>"
      "<span class='am-sign'>Marhaba, and see you soon</span></div>"
      "<div class='am-arch' style='margin-left:auto'>%s%s</div></div></section>") % (img_tag(src, alt, w, h), STAMP % '#221C17')
val = lambda icon, t, d: "<div class='am-val'><i>%s</i><h3>%s</h3><p>%s</p></div>" % (icon, t, d)
A3 = ("<section class='am am-sec am-sec--sand'><div class='am-w'><div class='am-sh'><div><span class='am-eb'>Why travellers book with us</span>"
      "<h2>The small things that make a <em>good trip</em></h2></div><p>Nothing fancy. Just the way we think a trip in Morocco should be run.</p></div><div class='am-vals'>"
      + val(I_USR, 'Private, always', "It's just you and the people you came with. No strangers, no fixed group schedule.")
      + val(I_MAP, 'Routes we know well', 'Honest driving times, good stops and the right place for lunch.')
      + val(I_CAR, 'Careful drivers', 'Comfortable cars and drivers who know the mountain roads.')
      + val(I_CHAT, 'A real person to talk to', 'Message us before the trip and during it. Plans change, and that is fine.')
      + "</div></div></section>")
A4 = ("<section class='am am-sec'><div class='am-w'><div class='am-sh am-sh--c'><span class='am-hand'>Our guests</span>"
      "<h2>A few faces from <em>recent trips</em></h2><p>Families, friends, solo travellers and groups. Every trip ends with a photo, and we'll keep adding them here.</p></div>"
      + wall([('welcome', 'am-pa'), ('dune', 'am-pb'), ('group', 'am-pc'), ('goodbye', 'am-pf')]) + "</div></section>")
about = [con('am0abou', [w_html('ama%02dw' % i, x) for i, x in enumerate([A1, A2, A3, A4, steps(),
         cta('Have a trip <em>in mind?</em>', "Tell us what you're thinking, even if it's just a rough idea. We'll come back with a plan.")])])]

# ================================ CONTACT ================================
src, w, h, alt = G['welcome']
C1 = ("<section class='am am-hero am-hero--sm'>%s<div class='am-w'><span class='am-eb'>Contact</span>"
      "<h1>Tell us about <em>your trip</em></h1>"
      "<p class='am-hero-lead'>Your dates, how many of you, and roughly what you'd like to see. We'll reply with a plan and a price, with no obligation to book.</p></div></section>") % hero_bg(src, alt)
cc = lambda cls, href, icon, t, d: ("<a class='am-cc %s' href='%s'%s><i>%s</i><span><b>%s</b>%s</span></a>" % (cls, href, " target='_blank' rel='noopener'" if href.startswith('http') else '', icon, t, d))
C_LEFT = ("<div class='am'><span class='am-eb'>Reach us directly</span><h2 style='font-size:clamp(30px,3vw,40px);margin-bottom:24px'>The quickest way is <em>WhatsApp</em></h2>"
          "<div class='am-cards'>"
          + cc('am-cc--wa', WA, I_WA, 'WhatsApp', PHONES[0][0])
          + cc('', 'tel:' + PHONES[1][1], I_PH, 'Call us', PHONES[1][0] + ' &#183; ' + PHONES[0][0])
          + cc('', 'mailto:' + EMAIL, I_ML, 'Email', EMAIL)
          + "<div class='am-cc'><i>%s</i><span><b>Office</b>Lot El Massar N&#176; 1106, 3&#232;me &#233;tage, Marrakech</span></div>" % I_PIN
          + "</div><div class='am-map'><iframe title='Amasir Voyage office in Marrakech' loading='lazy' referrerpolicy='no-referrer-when-downgrade' src='https://www.google.com/maps?q=El%20Massar%2C%20Marrakech%2C%20Morocco&amp;output=embed'></iframe></div></div>")
C_FORM_H = ("<div class='am'><span class='am-eb'>Or write to us</span><h2 style='font-size:clamp(30px,3vw,40px);margin-bottom:10px'>Send a message</h2>"
            "<p style='margin-bottom:26px'>Questions about a transfer or a single day trip are just as welcome as a two-week tour.</p></div>")
contact = [con('am0cont', [
    w_html('amc00w', C1),
    w_html('amc01w', "<div class='am' style='height:110px;background:var(--am-paper)'></div>"),
    con('amc0grd', [
        con('amc0lft', [w_html('amc02w', C_LEFT)], inner=True),
        con('amc0rgt', [w_html('amc03w', C_FORM_H), w_short('amc04w', '[contact-form-7 id="4de6ca8" title="Contact Form"]')], 'amc-form', inner=True),
    ], 'amc-grid', inner=True),
    w_html('amc05w', cta('Prefer to <em>just talk?</em>', 'Send us a WhatsApp message and a real person from the team will answer.')),
], 'amc-wrap')]

# ================================ ACTIVITIES ================================
X1 = ("<section class='am am-hero am-hero--sm'>%s<div class='am-w'><span class='am-eb'>Activities</span>"
      "<h1>Short adventures <em>around Marrakech</em></h1>"
      "<p class='am-hero-lead'>A few hours is enough. Book one on its own, or add it to any of our day trips.</p></div></section>") % hero_bg(u('pexels-leos-37736075-scaled.jpg'), 'Hot air balloons at sunrise near Marrakech')
X2 = ("<section class='am am-sec'><div class='am-w'><div class='am-acts am-acts--big'>"
      + ''.join(("<a class='am-act' href='%s/trip/%s/'><div class='am-act-i'>%s</div><div><span class='am-eb'>Activity</span><h3>%s</h3><p>%s</p><span class='am-go'>See details</span></div></a>")
                % (S, a[1], img_tag(a[3], a[0], full=a[2]), a[0].replace('&', '&amp;'), a[4]) for a in ACTS)
      + "</div></div></section>")
activities = [con('am0acti', [w_html('amx%02dw' % i, x) for i, x in enumerate([X1, X2,
              cta('Want to <em>combine</em> a few?', "Balloon in the morning, Agafay at sunset? Tell us what you like and we'll fit it into one day.")])])]


# ================================ write ================================
def save(name, data):
    with open(os.path.join(OUT, name + '.json'), 'w') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    s = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('\\', '\\\\')
    with open(os.path.join(OUT, name + '.slashed.json'), 'w') as f:
        f.write(s)


for n, d in [('header', header), ('footer', footer), ('home', home), ('about', about), ('contact', contact), ('activities', activities)]:
    save(n, d)

css = open(os.path.join(HERE, 'design.css')).read()
imp_end = css.index("');") + 3
body = re.sub(r'/\*.*?\*/', '', css[imp_end:], flags=re.S)
body = re.sub(r'\s*\n\s*', '', body)
with open(os.path.join(OUT, 'custom.css'), 'w') as f:
    f.write(css[:imp_end] + '\n\n.blog-style6, .blog-style7{\n\tpadding:0;\n}\n\n/* Amasir Voyage design (am-*) */\n' + body)


# ---------- local preview ----------
def htmls(n, acc):
    if isinstance(n, list):
        for x in n:
            htmls(x, acc)
    elif isinstance(n, dict):
        wc = n.get('settings', {}).get('_css_classes', '') if isinstance(n.get('settings'), dict) else ''
        if n.get('widgetType') == 'html':
            acc.append("<div class='elementor-element %s'>%s</div>" % (wc, n['settings']['html']))
        elif n.get('widgetType') == 'shortcode':
            acc.append("<div class='elementor-element %s' style='padding:10px;border:2px dashed #ccc;font:13px monospace'>%s</div>" % (wc, n['settings']['shortcode']))
        inner = htmls(n.get('elements', []), [])
        cls = n.get('settings', {}).get('css_classes') or n.get('settings', {}).get('_css_classes') if isinstance(n.get('settings'), dict) else ''
        if n.get('elType') == 'container' and cls:
            acc.append("<div class='%s'>%s</div>" % (cls, ''.join(inner)))
        elif n.get('elType') == 'container':
            acc.extend(inner)
        else:
            acc.extend(inner)
    return acc


def local(s):
    for key, (src, *_r) in G.items():
        s = s.replace(src, '../../media/amasir/' + src.rsplit('/', 1)[1])
    return s


for n, d in [('home', home), ('about', about), ('contact', contact), ('activities', activities)]:
    page = ("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>"
            "<style>" + css + "body{margin:0}img[src*='amasirvoyage.com']{background:linear-gradient(135deg,#d9b48f,#a8573a)}</style><body>"
            + ''.join(htmls(header, [])) + ''.join(htmls(d, [])) + ''.join(htmls(footer, [])) + "</body>")
    with open(os.path.join(PRE, n + '.html'), 'w') as f:
        f.write(local(page))

for n in sorted(os.listdir(OUT)):
    print(n, os.path.getsize(os.path.join(OUT, n)))
