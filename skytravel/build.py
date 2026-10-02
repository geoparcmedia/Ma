"""Build Morocco Sky Travel program pages (Elementor data + SEO fields).

python3 build.py            -> writes out/<id>.json (payload for wp_update_post) and preview/<id>.html
Shared CSS lives in style.css and is published once as WordPress "Additional CSS".
"""
import json, os, re, hashlib, html, urllib.parse
from tours import TOURS

SITE = 'https://moroccoskytravel.com'
WA = '212667307641'
PHONE = '+212 667 307 641'
EMAIL = 'moroccoskytravel@gmail.com'
FORM = '[contact-form-7 id=389]'
LIST = {'multi': ('Destinations', SITE + '/our-destinations/'), 'day': ('Day Trips', SITE + '/destinations-copy/')}

def typo(s):
    """Typographic apostrophes/quotes so the HTML never needs a straight quote in text."""
    s = s.replace("'", '’')
    s = re.sub(r'"([^"]*)"', '“\\1”', s)
    return s

def esc(s):
    return html.escape(typo(s), quote=False)

def eid(*k):
    return hashlib.md5('|'.join(map(str, k)).encode()).hexdigest()[:7]

IC = {
 'clock': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='9'/><path d='M12 7v5l3 2'/></svg>",
 'pin': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z'/><circle cx='12' cy='10' r='2.5'/></svg>",
 'flag': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M5 21V4h11l-1.5 4L16 12H5'/></svg>",
 'car': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M5 16h14M6 16l1.5-6h9L18 16M5 16v3h2v-3M17 16v3h2v-3'/><circle cx='8' cy='13.5' r='.6'/><circle cx='16' cy='13.5' r='.6'/></svg>",
 'wa': "<svg viewBox='0 0 24 24' fill='currentColor'><path d='M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z'/></svg>",
 'mail': "<svg viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><rect x='3' y='5' width='18' height='14' rx='2'/><path d='M3 7l9 6 9-6'/></svg>",
}

def wa_link(msg):
    return 'https://wa.me/%s?text=%s' % (WA, urllib.parse.quote(msg))

def dur(t):
    return ('%d days' % t['days']) if t['kind'] == 'multi' else 'Full day'

def badge(t):
    return ('%d days' % t['days']) if t['kind'] == 'multi' else 'Day trip'

def card(t, h='h3'):
    return ("<a class='mst-tc' href='%s/%s/' data-start='%s'><div class='im'><img src='%s' alt='%s' loading='lazy' width='640' height='480'><span class='badge'>%s</span></div>"
            "<div class='tx'><%s>%s</%s><span class='rt'>%s</span><p>%s</p><span class='go'>View itinerary →</span></div></a>") % (
        SITE, t['url'], t['start'], t['img'], esc(t['alt']), badge(t), h, esc(t['card']), h,
        esc('From ' + t['start'] + (' · ' + t['hours'] if t['kind'] == 'day' else '')), esc(t['lead']))

def related(t):
    pool = [x for x in TOURS if x['id'] != t['id'] and x['kind'] == t['kind']]
    if t['kind'] == 'multi':
        pool.sort(key=lambda x: (x['start'] != t['start'], abs(x['days'] - t['days'])))
    return pool[:3]

def jsonld(t):
    lst, lurl = LIST[t['kind']]
    url = '%s/%s/' % (SITE, t['url'])
    if t['kind'] == 'multi':
        nums = t.get('daynums') or ['Day %d' % (i + 1) for i in range(len(t['it']))]
        items = [{'@type': 'ListItem', 'position': i + 1, 'name': '%s: %s' % (nums[i], a)} for i, (a, b) in enumerate(t['it'])]
    else:
        items = [{'@type': 'ListItem', 'position': i + 1, 'name': '%s %s' % (a, b)} for i, (a, b, c) in enumerate(t['steps'])]
    data = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'TouristTrip', '@id': url + '#trip', 'name': t['title'], 'description': t['desc'], 'url': url, 'image': t['img'],
         'touristType': 'Private tour', 'itinerary': {'@type': 'ItemList', 'numberOfItems': len(items), 'itemListElement': items},
         'provider': {'@type': 'TravelAgency', '@id': SITE + '/#agency', 'name': 'Morocco Sky Travel', 'url': SITE + '/', 'telephone': '+212667307641', 'email': EMAIL,
                      'address': {'@type': 'PostalAddress', 'addressLocality': 'Fes', 'addressCountry': 'MA'}}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': lst, 'item': lurl},
            {'@type': 'ListItem', 'position': 3, 'name': t['title'], 'item': url}]}]}
    return ldscript(data)

def jsv(v):
    """JS literal with single-quoted strings only, so the page JSON never needs a backslash."""
    if isinstance(v, dict):
        return '{' + ','.join("'%s':%s" % (k, jsv(x)) for k, x in v.items()) + '}'
    if isinstance(v, list):
        return '[' + ','.join(jsv(x) for x in v) + ']'
    if isinstance(v, (int, float)):
        return str(v)
    v = typo(str(v)).replace('<', '&lt;')
    assert "'" not in v and '\\' not in v and '\n' not in v, v
    return "'" + v + "'"

def ldscript(data):
    return ("<script>(function(){var s=document.createElement('script');s.type='application/ld+json';s.text=JSON.stringify(%s);document.head.appendChild(s)})()</script>" % jsv(data))

def intro(t):
    if t['id'] == 2847:
        return 'This 7-day trek starts with a transfer from Marrakech to Mhamid by minibus or 4x4, then continues on foot and by camel with your nomad team all the way to the dunes of Erg Chagaga.'
    if t['kind'] == 'multi':
        same = t['start'] == t['end']
        return 'This private %d-day tour %s, with your own driver and a vehicle reserved for your group from the first day to the last.' % (
            t['days'], ('starts and ends in %s' % t['start']) if same else ('starts in %s and ends in %s' % (t['start'], t['end'])))
    return 'A private full-day trip with pick-up and drop-off at your hotel or riad in %s, travelling in an air-conditioned vehicle with your own driver.' % t['start']

def top(t):
    lst, lurl = LIST[t['kind']]
    wa = wa_link('Hello Morocco Sky Travel, I am interested in the tour: %s' % t['title'])
    facts = [('clock', 'Duration', dur(t) if t['kind'] == 'multi' else t['hours']), ('pin', 'Starts in', t['start']), ('flag', 'Ends in', t['end']), ('car', 'Tour type', 'Private tour')]
    h = ["<div class='mst'>",
         "<header class='mst-hero' style='background-image:url(%s)'><div class='mst-wrap'>" % t['img'],
         "<nav class='mst-crumbs' aria-label='Breadcrumb'><a href='%s/'>Home</a><span>/</span><a href='%s'>%s</a><span>/</span>%s</nav>" % (SITE, lurl, lst, esc(t['card'])),
         "<span class='mst-eyebrow'>%s</span>" % ('Private tour · %d days' % t['days'] if t['kind'] == 'multi' else 'Private day trip from ' + t['start']),
         '<h1>%s</h1>' % esc(t['title']),
         "<p class='mst-lead'>%s</p>" % esc(t['lead']),
         "<div class='mst-hero-ctas'><a class='mst-btn mst-btn--gold' href='#book'>Request this tour</a><a class='mst-btn mst-btn--ghost' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> WhatsApp us</a></div>" % wa,
         '</div></header>',
         "<div class='mst-wrap mst-facts'><ul>" + ''.join("<li><span class='ic'><i class='i-%s'></i></span><span><small>%s</small><b>%s</b></span></li>" % (i, a, esc(b)) for i, a, b in facts) + '</ul></div>',
         "<div class='mst-wrap mst-body'><div class='mst-grid'><main>",
         "<section class='mst-sec'><span class='mst-eyebrow'>Overview</span><h2>About this %s</h2><p>%s</p>%s</section>" % (
             'tour' if t['kind'] == 'multi' else 'day trip', esc(intro(t)), '<p>%s</p>' % esc(t.get('outro') or t['desc'])),
         "<section class='mst-sec'><span class='mst-eyebrow'>Highlights</span><h2>What you will see</h2><ul class='mst-hl'>" + ''.join('<li>%s</li>' % esc(x) for x in t['hl']) + '</ul></section>']
    if t['kind'] == 'multi':
        nums = t.get('daynums') or ['Day %d' % (i + 1) for i in range(len(t['it']))]
        h.append("<section class='mst-sec' id='itinerary'><div class='mst-it-head'><div><span class='mst-eyebrow'>Itinerary</span><h2>Day-by-day itinerary</h2></div>"
                 "<button type='button' class='mst-toggle' onclick='var d=this.closest(&quot;section&quot;).querySelectorAll(&quot;details&quot;),o=this.dataset.o!=&quot;1&quot;;d.forEach(function(x){x.open=o});this.dataset.o=o?&quot;1&quot;:&quot;0&quot;;this.textContent=o?&quot;Collapse all days&quot;:&quot;Expand all days&quot;'>Expand all days</button></div><div class='mst-days'>")
        for i, (a, b) in enumerate(t['it']):
            h.append("<details class='mst-day'%s><summary><span class='dn'>%s</span><h3>%s</h3></summary><div class='bd'><p>%s</p></div></details>" % (' open' if i == 0 else '', nums[i], esc(a), esc(b)))
        h.append('</div></section>')
    else:
        h.append("<section class='mst-sec' id='itinerary'><span class='mst-eyebrow'>Itinerary</span><h2>How the day goes</h2><ol class='mst-steps'>")
        for a, b, c in t['steps']:
            h.append("<li><span class='t'>%s</span><div><h3>%s</h3><p>%s</p></div></li>" % (esc(a), esc(b), esc(c)))
        h.append('</ol></section>')
        h.append("<section class='mst-sec'><span class='mst-eyebrow'>Good to know</span><h2>What’s included</h2><div class='mst-ie'><div class='in'><h3>Included</h3><ul>%s</ul></div><div class='ex'><h3>Not included</h3><ul>%s</ul></div></div></section>" % (
            ''.join('<li>%s</li>' % esc(x) for x in t['inc']), ''.join('<li>%s</li>' % esc(x) for x in t['exc'])))
    h.append("<p class='mst-note'>Every tour is private and can be adapted to your dates, pace and interests. Tell us what you would like to change and we will tailor it for you.</p>")
    h.append('</main>')
    h.append("<aside class='mst-side'><div class='mst-card'><div class='mst-card-top'><small>Private tour</small><b>%s</b><span>%s · from %s</span></div>"
             "<div class='mst-card-bd'><a class='mst-btn mst-btn--gold' href='#book'>Request this tour</a><a class='mst-btn mst-btn--wa' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> Chat on WhatsApp</a>"
             "<a class='mst-btn mst-btn--line' href='mailto:%s?subject=%s'><i class='i-mail'></i> Email us</a>"
             "<ul class='mst-trust'><li>Family-run company with Saharan roots in Zagora</li><li>Over seven years of experience in Moroccan tourism</li><li>Private transport and local guides</li><li>Itinerary tailored to you</li></ul></div>"
             "<div class='mst-card-ft'>Prefer to call? <a href='tel:+212667307641'>%s</a></div></div></aside>" % (
                 esc(t['card']), dur(t) if t['kind'] == 'multi' else t['hours'], t['start'], wa, EMAIL, urllib.parse.quote('Tour request: ' + t['title']), PHONE))
    h.append('</div></div></div>')
    return ''.join(h)

def book_head(t=None, title='Request this tour', text=None):
    text = text or "Send us your dates and group size. We will reply with a tailored itinerary and a personal quote. No payment is needed to ask."
    return "<div class='mst mst-book-in'><span class='mst-eyebrow'>Free quote</span><h2>%s</h2><p>%s</p></div>" % (esc(title), esc(text))

def bottom(t):
    rel = related(t)
    lst, lurl = LIST[t['kind']]
    return ("<div class='mst'><section class='mst-wrap mst-related'><span class='mst-eyebrow'>You may also like</span><h2>More %s</h2><div class='mst-cards'>%s</div>"
            "<p style='text-align:center;margin-top:30px'><a class='mst-btn mst-btn--line' href='%s'>See all %s</a></p></section></div>%s") % (
        'tours' if t['kind'] == 'multi' else 'day trips', ''.join(card(x) for x in rel), lurl, lst.lower(), jsonld(t))

def container(cid, widgets, extra=None):
    s = {'content_width': 'full', 'flex_direction': 'column', 'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0'},
         'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}}
    if extra: s.update(extra)
    return {'id': cid, 'elType': 'container', 'settings': s, 'elements': widgets, 'isInner': False}

def w_html(wid, code):
    return {'id': wid, 'elType': 'widget', 'settings': {'html': code}, 'elements': [], 'widgetType': 'html'}

def w_sc(wid, code):
    return {'id': wid, 'elType': 'widget', 'settings': {'shortcode': code}, 'elements': [], 'widgetType': 'shortcode'}

def book_container(key, head):
    return container(eid(key, 'c2'), [w_html(eid(key, 'w2'), head), w_sc(eid(key, 'w3'), FORM)],
                     {'css_classes': 'mst-book', '_element_id': 'book', 'padding': {'unit': 'px', 'top': '72', 'right': '20', 'bottom': '72', 'left': '20', 'isLinked': False},
                      'flex_gap': {'unit': 'px', 'size': 28, 'column': '28', 'row': '28'}})

def elementor(t):
    k = t['id']
    return [container(eid(k, 'c1'), [w_html(eid(k, 'w1'), top(t))]),
            book_container(k, book_head(t)),
            container(eid(k, 'c3'), [w_html(eid(k, 'w4'), bottom(t))])]

def plain(t):
    """post_content fallback (search, excerpts): clean semantic text only."""
    p = ['<p>%s</p>' % esc(t['lead'])]
    if t['kind'] == 'multi':
        nums = t.get('daynums') or ['Day %d' % (i + 1) for i in range(len(t['it']))]
        p += ['<h3>%s: %s</h3>' % (nums[i], esc(a)) for i, (a, b) in enumerate(t['it'])]
    else:
        p += ['<h3>%s – %s</h3><p>%s</p>' % (esc(a), esc(b), esc(c)) for a, b, c in t['steps']]
    return ''.join(p)

def nobs(s):
    # wp_unslash() is a no-op only when the JSON has no backslash at all
    assert '\\' not in s, s[s.index('\\') - 80:s.index('\\') + 20]
    return s

def addslashes(s):
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('"', '\\"')

def seo_title(t):
    s = '%s | Morocco Sky Travel' % t['title']
    return s if len(s) <= 62 else t['title']

def payload(t, edata, content):
    return {'ID': t['id'],
            'fields': {'post_title': t['title'], 'post_content': content, 'post_excerpt': t['desc']},
            'meta_input': {'_elementor_data': nobs(json.dumps(edata, ensure_ascii=False, separators=(',', ':'))),
                           '_elementor_edit_mode': 'builder', '_wp_page_template': 'elementor_header_footer',
                           'site-post-title': 'disabled', 'ast-title-bar-display': 'disabled', 'ast-featured-img': 'disabled',
                           'rank_math_title': seo_title(t), 'rank_math_description': t['desc'], 'rank_math_focus_keyword': t['kw']}}

def preview(name, body, css):
    os.makedirs('preview', exist_ok=True)
    open('preview/%s.html' % name, 'w').write(
        "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<style>body{margin:0;background:#fff}.hdr{height:90px;background:#F0D6B3}.ftr{height:200px;background:#010000}" + css + '</style></head><body><div class=hdr></div>' + body + '<div class=ftr></div></body></html>')

if __name__ == '__main__':
    os.makedirs('out', exist_ok=True)
    css = open('style.css').read()
    for t in TOURS:
        ed = elementor(t)
        json.dump(payload(t, ed, plain(t)), open('out/%d.json' % t['id'], 'w'), ensure_ascii=False)
        form = "<form class='wpcf7-form'><div class='mst-f'><label>Full name <em>*</em><span class='wpcf7-form-control-wrap'><input type='text' placeholder='Your full name'></span></label><label>Email <em>*</em><span class='wpcf7-form-control-wrap'><input type='email' placeholder='you@example.com'></span></label><label class='full'>Message<span class='wpcf7-form-control-wrap'><textarea></textarea></span></label><div class='full'><input class='wpcf7-submit' type='submit' value='Send my request'></div></div></form>"
        body = ed[0]['elements'][0]['settings']['html'] + "<div class='mst-book' id='book'>" + ed[1]['elements'][0]['settings']['html'] + "<div class='mst-formbox'><div class='wpcf7'>" + form + '</div></div></div>' + ed[2]['elements'][0]['settings']['html']
        preview(str(t['id']), body, css)
        assert '\\' not in ed[0]['elements'][0]['settings']['html'], t['id']
    print('built', len(TOURS))
