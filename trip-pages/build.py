"""Build the new tour page layout for the 10 WP Travel Engine trips.

The layout is stored as the trip's post_content (one wp:html block). WP Travel
Engine prints post_content above its tabs, inside the main column, next to the
booking sidebar. The CSS in the block hides the old tabs, so the page shows:
key facts, overview, highlights, route map, day-by-day itinerary, what's
included, and a booking card that is moved into the sidebar.

Text comes from ../seo-content/trips_new.json, routes from routes.py.
Run: python3 build.py  ->  out/<id>.html (block) and preview/<id>.html
"""
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'homepage-redesign'))
from routes import P, R
from tours import CYCLING, TREKKING

TRIPS = json.load(open(os.path.join(HERE, '..', 'seo-content', 'trips_new.json')))
SLUG = {3755: 'morocco-cycling-tour', 3723: 'caravan-road-gravel-bike-tour', 3761: 'morocco-hike-and-bike-tour',
        3727: 'hike-and-bike-morocco-tour', 3656: 'hiking-in-bougmaz-valleykigdom-of-berbers',
        3627: 'toubkal-ascent-essaouira-city-4167-m-13671-ft', 3621: 'edge-of-the-sahara-desert-trek',
        3616: 'climb-mount-toubkal-4167-m-13671-ft', 3611: 'classic-toubkal-mountain-trek',
        3606: 'climb-mount-mgoun4071m-13356-ft'}
SHARED_REF = int(open(os.path.join(HERE, 'shared-ref.txt')).read()) if os.path.exists(os.path.join(HERE, 'shared-ref.txt')) else 0
PRICE = {c[0].strip('/'): c[6] for c in CYCLING + TREKKING}
WA = 'https://wa.me/212660435569'
MAIL = 'mailto:marouanguide@yahoo.fr?subject='
CONTACT = 'https://wegravelmorocco.com/contact-us/'

e = lambda s: html.escape(s, quote=True)

# ---------- icons (24x24 stroke icons) ----------
IC = {
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    'gauge': '<path d="M4 18a8 8 0 1 1 16 0"/><path d="M12 18l4-6"/>',
    'cal': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    'users': '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M16 4.5a3 3 0 0 1 0 6M21 20c0-2.7-1.6-5-4-5.7"/>',
    'pin': '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    'bike': '<circle cx="6" cy="16" r="3.5"/><circle cx="18" cy="16" r="3.5"/><path d="M6 16l4-8h5l3 8M10 8l3 8h-7M14 5h2.5"/>',
    'boot': '<path d="M13 4l1 5 4 2 3 1v4H4V4z"/><path d="M4 20h17M8 9h3M8 12h4"/>',
    'car': '<path d="M3 16v-4l2-5h14l2 5v4z"/><circle cx="7" cy="16.5" r="1.8"/><circle cx="17" cy="16.5" r="1.8"/><path d="M3 12h18"/>',
    'bed': '<path d="M3 18V7M3 13h18v5M21 13a3 3 0 0 0-3-3h-7v3"/><circle cx="7" cy="10.5" r="1.8"/>',
    'food': '<path d="M5 3v8a2 2 0 0 0 2 2v8M9 3v8M7 3v6M17 21V3c-2 1-3 4-3 8h3"/>',
    'mtn': '<path d="M2 20l7-12 4 6 3-4 6 10z"/><path d="M8 10l1.5 1.5L11 10"/>',
    'check': '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    'x': '<path d="M6 6l12 12M18 6L6 18"/>',
    'star': '<path d="M12 3l2.6 5.6 6 .7-4.5 4.1 1.2 6L12 16.5 6.7 19.4l1.2-6L3.4 9.3l6-.7z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    'map': '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    'age': '<circle cx="12" cy="7" r="3.5"/><path d="M5 21c0-3.9 3.1-7 7-7s7 3.1 7 7"/>',
    'tag': '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
    'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
    'chev': '<path d="M6 9l6 6 6-6"/>',
    'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>',
    'chat': '<path d="M4 5h16v11H9l-5 4z"/>',
}
WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2c0 1.3.9 2.5 1.1 2.7.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>')


def ic(name, cls='wgt-i'):
    return '<svg class="%s" aria-hidden="true"><use href="#wgt-%s"/></svg>' % (cls, name)


WA_PATH = WA_SVG[WA_SVG.index('<path'):WA_SVG.index('</svg>')]
WA_SVG = '<svg class="wgt-f" aria-hidden="true"><use href="#wgt-wa"/></svg>'


def sprite():
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">' +
            ''.join('<symbol id="wgt-%s" viewBox="0 0 24 24">%s</symbol>' % (k, v) for k, v in IC.items()) +
            '<symbol id="wgt-wa" viewBox="0 0 24 24">' + WA_PATH + '</symbol></svg>')


# ---------- data helpers ----------
def text_of(block):
    return re.findall(r'<p>(.*?)</p>', block, re.S)


def overview(s):
    tc = s['tab_content']['1_wpeditor']
    paras = [p for p in text_of(tc) if not p.startswith('<strong>Trip details')]
    facts = [(k.strip().rstrip(':'), v.strip()) for k, v in re.findall(r'<li><strong>([^<]*)</strong>\s*([^<]*)</li>', tc)]
    return paras, facts


DAYF = {'Accommodation': 'bed', 'Meals': 'food', 'Cycling distance': 'bike', 'Walking': 'boot', 'Drive': 'car',
        'Elevation': 'mtn', 'Level': 'gauge'}
DAYORDER = ['Cycling distance', 'Walking', 'Elevation', 'Drive', 'Accommodation', 'Meals', 'Level']


def day(s, k):
    c = s['itinerary']['itinerary_content'][k]
    ps = text_of(c)
    body, facts, note = [], {}, ''
    for p in ps:
        pairs = re.findall(r'<strong>([^<]+?):</strong>\s*([^<]*?)(?=<br>|$)', p)
        if pairs and p.startswith('<strong>'):
            for a, b in pairs:
                if a == 'Note':
                    note = b.strip()
                else:
                    facts[a] = b.strip()
        else:
            body.append(p)
    # a "Note:" can also sit inside the text paragraph
    for i, p in enumerate(body):
        m = re.search(r'<strong>Note:</strong>\s*(.*)$', p)
        if m:
            note = re.sub('<[^>]+>', '', m.group(1)).strip()
            body[i] = re.sub(r'(<br\s*/?>\s*)+$', '', p[:m.start()].strip())
    return body, facts, note


def modes(tid):
    used = set()
    for d in R[tid][1]:
        for m, _ in d:
            used.add(m)
    return used


def route_json(tid, s):
    start, days = R[tid]
    titles = s['itinerary']['itinerary_title']
    cur = start
    out = []
    for i, legs in enumerate(days, 1):
        L = []
        for m, pts in legs:
            names = [cur] + pts
            L.append({'m': m, 'p': [list(P[n]) for n in names],
                      'n': [n for n in pts if n[0].isupper()]})
            cur = pts[-1]
        out.append({'d': i, 't': titles[str(i)], 'l': L, 'end': cur, 'at': list(P[cur])})
    return {'start': start, 'at': list(P[start]), 'days': out}


# ---------- sections ----------
def key_facts(facts, days):
    f = dict(facts)
    act = f.get('Bike') or f.get('Type of travel') or ''
    items = [
        ('clock', 'Duration', f.get('Duration', '%d days' % days)),
        ('gauge', 'Level', f.get('Grade', '')),
        ('cal', 'Best time', f.get('Best time to visit', '')),
        ('users', 'Group size', f.get('Group size', '')),
        ('pin', 'Start / finish', f.get('Start / finish', '')),
        ('bike' if 'Bike' in f else 'boot', 'Bike' if 'Bike' in f else 'Travel style', act),
    ]
    return ('<div class="wgt-facts">' + ''.join(
        '<div class="wgt-fact">%s<div><span>%s</span><b>%s</b></div></div>' % (ic(i), e(l), e(v))
        for i, l, v in items if v) + '</div>')


def nav():
    links = [('overview', 'Overview'), ('highlights', 'Highlights'), ('route', 'Route map'),
             ('itinerary', 'Itinerary'), ('included', 'What’s included'), ('book', 'Book')]
    return ('<nav class="wgt-nav" aria-label="Tour sections"><div class="wgt-nav-in">' +
            ''.join('<a href="#wgt-%s">%s</a>' % (a, t) for a, t in links) + '</div></nav>')


def head(eyebrow, title, anchor, extra=''):
    return ('<div class="wgt-h" id="wgt-%s"><span class="wgt-eyebrow">%s</span><h2>%s</h2>%s</div>'
            % (anchor, eyebrow, title, extra))


def sec_overview(paras, facts):
    skip = {'Duration', 'Grade', 'Best time to visit', 'Group size', 'Start / finish', 'Bike', 'Type of travel'}
    icons = {'Tour name': 'tag', 'Recommended age': 'age', 'Accommodation': 'bed'}
    rest = [(k, v) for k, v in facts if k not in skip]
    lead = '<p class="wgt-lead">%s</p>' % paras[0] if paras else ''
    more = ''.join('<p>%s</p>' % p for p in paras[1:])
    dl = ''.join('<div>%s<dt>%s</dt><dd>%s</dd></div>' % (ic(icons.get(k, 'check')), e(k), e(v)) for k, v in rest)
    return ('<section class="wgt-sec">' + head('The tour', 'Tour overview', 'overview') + lead + more +
            '<dl class="wgt-dl">' + dl + '</dl></section>')


def sec_highlights(s):
    hl = [h['highlight_text'] for h in s['trip_highlights']]
    return ('<section class="wgt-sec">' + head('Why you’ll love it', 'Highlights', 'highlights') +
            '<ul class="wgt-hl">' + ''.join('<li><span>%s</span>%s</li>' % (ic('star'), e(h)) for h in hl) +
            '</ul></section>')


def sec_map(tid, rj):
    used = modes(tid)
    lg = [('ride', 'Cycling'), ('hike', 'Hiking'), ('drive', 'Transfer by vehicle')]
    legend = ''.join('<span class="wgt-lg wgt-lg-%s"><i></i>%s</span>' % (m, t) for m, t in lg if m in used)
    legend += '<span class="wgt-lg wgt-lg-stop"><i></i>Overnight stop</span>'
    # the ordered list of overnight places, also useful without JavaScript
    stops = [rj['start']]
    for d in rj['days']:
        if d['end'] != stops[-1]:
            stops.append(d['end'])
    chain = '<ol class="wgt-chain">' + ''.join('<li>%s</li>' % e(x) for x in stops) + '</ol>'
    data = json.dumps(rj, ensure_ascii=False, separators=(',', ':'))
    return ('<section class="wgt-sec">' + head('Where you’ll go', 'Route map', 'route') +
            '<div class="wgt-legend">' + legend + '</div>'
            '<div class="wgt-map-wrap"><div class="wgt-map" id="wgt-map" role="region" aria-label="Map of the tour route">' +
            '<div class="wgt-map-ph">' + ic('map') + '<span>Loading map…</span></div></div></div>'
            '<p class="wgt-note">The line shows the approximate route. Tap a day in the itinerary to zoom in on it.</p>' +
            chain + '<script type="application/json" id="wgt-data">' + data.replace('</', '<\\/') + '</script></section>')


def sec_itinerary(s, rj):
    titles = s['itinerary']['itinerary_title']
    rows = []
    for k in sorted(titles, key=int):
        body, facts, note = day(s, k)
        d = rj['days'][int(k) - 1]
        ms = [l['m'] for l in d['l']]
        kind = 'ride' if 'ride' in ms else 'hike' if 'hike' in ms else 'drive' if ms else 'rest'
        chips = ''.join('<span class="wgt-chip">%s<em>%s</em> %s</span>' % (ic(DAYF[f]), e(f.replace('Cycling distance', 'Cycling')), e(facts[f]))
                        for f in DAYORDER if f in facts)
        mini = []
        for f in ('Cycling distance', 'Walking'):
            if f in facts:
                mini.append('<span>%s%s</span>' % (ic(DAYF[f]), e(facts[f])))
        txt = ''.join('<p>%s</p>' % p for p in body)
        if note:
            txt += '<p class="wgt-daynote"><b>Note:</b> %s</p>' % e(note)
        btn = ('<button type="button" class="wgt-onmap" data-day="%s">%sShow on map</button>' % (k, ic('map'))) if d['l'] else ''
        rows.append(
            '<details class="wgt-day wgt-k-%s"%s><summary><span class="wgt-dn"><small>Day</small>%s</span>'
            '<span class="wgt-dt"><b>%s</b><span class="wgt-mini">%s</span></span>%s</summary>'
            '<div class="wgt-db">%s<div class="wgt-chips">%s</div>%s</div></details>'
            % (kind, ' open' if k == '1' else '', k, e(titles[k]), ''.join(mini), ic('chev', 'wgt-i wgt-chev'), txt, chips, btn))
    tools = '<button type="button" class="wgt-expand" aria-pressed="false">Expand all days</button>'
    return ('<section class="wgt-sec">' + head('Day by day', 'Itinerary', 'itinerary', tools) +
            '<div class="wgt-days">' + ''.join(rows) + '</div></section>')


def sec_included(s):
    inc = [x for x in s['cost']['cost_includes'].split('\n') if x.strip()]
    exc = [x for x in s['cost']['cost_excludes'].split('\n') if x.strip()]
    col = lambda cls, t, icon, xs: ('<div class="wgt-inc %s"><h3>%s</h3><ul>%s</ul></div>' % (
        cls, t, ''.join('<li>%s<span>%s</span></li>' % (ic(icon), e(x)) for x in xs)))
    return ('<section class="wgt-sec">' + head('Price details', 'What’s included', 'included') +
            '<div class="wgt-incs">' + col('wgt-yes', 'Included', 'check', inc) + col('wgt-no', 'Not included', 'x', exc) +
            '</div></section>')


def cta(price, verb, mail):
    return ('<section class="wgt-cta" id="wgt-book"><div><span class="wgt-eyebrow">Ready to %s?</span>'
            '<h2>Book this tour or ask us anything</h2>'
            '<p>Send us your dates on WhatsApp or by email. Our team in Marrakech replies within 24 hours '
            'and can adapt the tour to your group, level and dates.</p></div>'
            '<div class="wgt-cta-b"><div class="wgt-price"><small>From</small><b>%s €</b><small>per person</small></div>'
            '<a class="wgt-btn wgt-btn-wa" href="%s" target="_blank" rel="noopener">%sWhatsApp us</a>'
            '<a class="wgt-btn wgt-btn-l" href="%s">%sEmail us</a></div></section>'
            % (verb, price, WA, WA_SVG, mail, ic('mail')))


def aside(price, facts, days, mail):
    f = dict(facts)
    rows = [('clock', f.get('Duration', '%d days' % days)), ('gauge', f.get('Grade', '')),
            ('users', f.get('Group size', '')), ('pin', 'Start / finish: ' + f.get('Start / finish', 'Marrakech'))]
    return ('<aside class="wgt-aside" aria-label="Book this tour"><div class="wgt-aside-top"><small>From</small>'
            '<b>%s €</b><small>per person</small></div><ul>%s</ul>'
            '<a class="wgt-btn wgt-btn-wa" href="%s" target="_blank" rel="noopener">%sWhatsApp +212 660 435 569</a>'
            '<a class="wgt-btn wgt-btn-l" href="%s">%sEmail us</a>'
            '<div class="wgt-trust"><span>%sLocal guides from Morocco</span><span>%sReply within 24 hours</span>'
            '<span>%sPrivate dates on request</span></div></aside>'
            % (price, ''.join('<li>%s%s</li>' % (ic(i), e(v)) for i, v in rows if v), WA, WA_SVG, mail, ic('mail'),
               ic('shield'), ic('chat'), ic('cal')))


def mbar(price):
    return ('<div class="wgt-mbar"><div><small>From</small><b>%s €</b></div>'
            '<a class="wgt-btn wgt-btn-wa" href="%s" target="_blank" rel="noopener">%sBook on WhatsApp</a></div>' % (price, WA, WA_SVG))


CSS = open(os.path.join(HERE, 'style.css')).read()
JS = open(os.path.join(HERE, 'script.js')).read()
FONTS = ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700'
         '&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">')


def minify_css(c):
    c = re.sub(r'/\*.*?\*/', '', c, flags=re.S)
    c = re.sub(r'\s+', ' ', c)
    c = re.sub(r'\s*([{};,>])\s*', r'\1', c)
    return c.replace(';}', '}').strip()


def minify_js(j):
    j = re.sub(r'^\s*//.*$', '', j, flags=re.M)
    return re.sub(r'\n\s*', '\n', j).strip()


def build(tid):
    t = TRIPS[str(tid)]
    s = t['setting']
    paras, facts = overview(s)
    ndays = len(s['itinerary']['itinerary_title'])
    price = PRICE[SLUG[tid]]
    rj = route_json(tid, s)
    from urllib.parse import quote
    mail = MAIL + quote('Booking request: ' + t['title'])
    verb = 'ride' if 'ride' in modes(tid) else 'walk'
    body = ('<div class="wgt">' + key_facts(facts, ndays) + nav() + sec_overview(paras, facts) + sec_highlights(s) +
            sec_map(tid, rj) + sec_itinerary(s, rj) + sec_included(s) + cta(price, verb, mail) + aside(price, facts, ndays, mail) +
            mbar(price) + '</div>')
    assert '\n\n' not in body
    return '<!-- wp:block {"ref":%s} /-->\n\n<!-- wp:html -->\n' % SHARED_REF + body + '\n<!-- /wp:html -->', body


def shared():
    """CSS, script and icons used by every tour page (stored once as a synced pattern)."""
    out = FONTS + '<style>' + minify_css(CSS) + '</style>' + sprite() + '<script>' + minify_js(JS) + '</script>'
    assert '\n\n' not in out
    return '<!-- wp:html -->\n' + out + '\n<!-- /wp:html -->', out


def preview(tid, inner):
    """Rough copy of the WP Travel Engine page frame, to check the layout locally."""
    t = TRIPS[str(tid)]
    return ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><style>body{margin:0;font-family:Arial,sans-serif;color:#333}'
            '.hdr{height:86px;background:#313041}.ban{height:340px;background:#8a6b4f linear-gradient(135deg,#b5835a,#4b3a2c)}'
            '.trip-content-area{max-width:1200px;margin:0 auto;padding:0 15px}.row{display:flex;gap:30px;align-items:flex-start}'
            '#primary{flex:1;min-width:0}#secondary{width:360px;flex:none}'
            '.wpte-bf-outer{border:1px solid #ddd;padding:20px;background:#fff}.wpte-bf-btn{display:block;background:#E77717;color:#fff;padding:14px;text-align:center}'
            '@media(max-width:991px){.row{flex-direction:column;align-items:stretch}#secondary{width:100%%}}'
            '#tabs-container{padding:40px;background:#fdd}</style></head><body class="single-trip">'
            '<div class="hdr"></div><div class="ban"></div><div id="wp-travel-trip-wrapper" class="trip-content-area"><div class="row">'
            '<div id="primary" class="content-area"><main class="site-main"><article class="trip-post">'
            '<header class="entry-header"><h1 class="entry-title">%s</h1><span class="wte-title-duration"><span class="duration">%d</span> <span class="days">Days</span></span></header>'
            '<div class="entry-content"><div class="trip-post-content">%s</div>'
            '<div id="tabs-container">OLD TABS (hidden on the site)</div></div></article></main></div>'
            '<div id="secondary" class="widget-area"><div class="wpte-bf-outer"><div class="wpte-bf-price">From <b>€%s</b></div>'
            '<a class="wpte-bf-btn" href="#">Check Availability</a></div></div></div></div><div class="hdr"></div></body></html>'
            % (e(t['title']), e(t['title']), len(t['setting']['itinerary']['itinerary_title']), inner, PRICE[SLUG[tid]]))


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    os.makedirs(os.path.join(HERE, 'preview'), exist_ok=True)
    sblock, sinner = shared()
    open(os.path.join(HERE, 'out', 'shared.html'), 'w').write(sblock)
    print('shared', len(sblock))
    for tid in R:
        block, inner = build(tid)
        open(os.path.join(HERE, 'out', '%d.html' % tid), 'w').write(block)
        open(os.path.join(HERE, 'preview', '%d.html' % tid), 'w').write(preview(tid, sinner + inner))
        print(tid, len(block))
