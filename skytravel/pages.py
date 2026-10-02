"""Listing and contact pages (Destinations, Day Trips, Book, Contact) in the same design system."""
import json, os
from tours import TOURS, U
from build import (SITE, WA, PHONE, EMAIL, esc, eid, card, container, w_html, w_sc, book_container,
                   book_head, ldscript, nobs, preview, wa_link)

WHY = [('Local experts', 'Friendly, knowledgeable guides who share authentic insights and stories throughout your journey.'),
       ('Tailor-made itineraries', 'Every tour is private and flexible: we adapt the route, pace and hotels to you.'),
       ('Comfortable transport', 'Reliable private transport with your own driver for the whole trip.'),
       ('Hand-picked stays', 'Hotels, riads and desert camps booked for you for a smooth, comfortable trip.'),
       ('Desert roots', 'A family company whose story began with camel journeys in the sands of Zagora.'),
       ('Seven years of experience', 'Over seven years organising trips across Morocco for travellers from all over the world.')]

def hero(img, eyebrow, h1, lead, crumbs, ctas=True):
    c = "<nav class='mst-crumbs' aria-label='Breadcrumb'><a href='%s/'>Home</a><span>/</span>%s</nav>" % (SITE, esc(crumbs))
    b = ("<div class='mst-hero-ctas'><a class='mst-btn mst-btn--gold' href='#book'>Plan my trip</a>"
         "<a class='mst-btn mst-btn--ghost' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> WhatsApp us</a></div>") % wa_link(
        'Hello Morocco Sky Travel, I would like help planning a trip to Morocco.') if ctas else ''
    return ("<header class='mst-hero' style='background-image:url(%s)'><div class='mst-wrap'>%s<span class='mst-eyebrow'>%s</span>"
            "<h1>%s</h1><p class='mst-lead'>%s</p>%s</div></header>") % (img, c, esc(eyebrow), esc(h1), esc(lead), b)

def why():
    return ("<section class='mst-wrap'><div class='mst-intro'><span class='mst-eyebrow'>Why travel with us</span><h2>Morocco, the way locals know it</h2></div>"
            "<div class='mst-why'>" + ''.join('<div><h3>%s</h3><p>%s</p></div>' % (esc(a), esc(b)) for a, b in WHY) + '</div></section>')

def cta(img, title, text, link, label):
    return ("<div class='mst-wrap'><div class='mst-cta' style='background-image:url(%s)'><div><h2>%s</h2><p>%s</p></div>"
            "<div class='acts'><a class='mst-btn mst-btn--gold' href='%s'>%s</a></div></div></div>") % (img, esc(title), esc(text), link, esc(label))

def itemlist(name, url, items):
    return ldscript({'@context': 'https://schema.org', '@graph': [
        {'@type': 'ItemList', 'name': name, 'url': url, 'numberOfItems': len(items),
         'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': '%s/%s/' % (SITE, t['url']), 'name': t['title']} for i, t in enumerate(items)]},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': name, 'item': url}]}]})

FILTER_JS = ("<script>(function(){var f=document.querySelector('.mst-filter');if(!f)return;f.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;"
             "f.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});var v=b.dataset.f;"
             "document.querySelectorAll('.mst-list .mst-tc').forEach(function(c){c.style.display=(v==='all'||c.dataset.start===v)?'':'none'})})})()</script>")

def destinations():
    multi = sorted([t for t in TOURS if t['kind'] == 'multi'], key=lambda t: (t['days'], t['start']))
    starts = []
    for t in multi:
        if t['start'] not in starts: starts.append(t['start'])
    url = SITE + '/our-destinations/'
    top = ("<div class='mst'>" + hero(U + '2025/11/pexels-droosmo-3088563-scaled.jpg', 'Private tours across Morocco', 'Morocco Tours & Desert Trips',
           'Sahara nights, imperial cities, Atlas villages and the Atlantic coast: choose a ready-made itinerary or let us tailor one for you.', 'Destinations') +
           "<section class='mst-wrap mst-list'><div class='mst-intro'><span class='mst-eyebrow'>Our tours</span><h2>Choose your journey</h2>"
           "<p>%s</p></div>" % esc('Discover the magic of Morocco through carefully crafted journeys designed to immerse you in the country’s beauty, culture and authentic experiences. Each tour reflects a different facet of Morocco, from golden dunes and imperial cities to coastal escapes and mountain adventures.') +
           "<div class='mst-filter' role='group' aria-label='Filter tours by starting city'><button type='button' data-f='all' aria-pressed='true'>All tours</button>" +
           ''.join("<button type='button' data-f='%s' aria-pressed='false'>From %s</button>" % (s, s) for s in starts) + '</div>'
           "<div class='mst-cards'>" + ''.join(card(t) for t in multi) + '</div></section>' +
           cta(U + '2025/11/quad-biking-in-agafay-desert-with-lunch-camel-ride-pool-3228139.jpg', 'Only have a day?',
               'Discover our private day trips from Marrakech: Atlas valleys, waterfalls, the Agafay desert and Essaouira.', SITE + '/destinations-copy/', 'See day trips') +
           why() + '</div>' + FILTER_JS + itemlist('Morocco Tours & Desert Trips', url, multi))
    head = book_head(title='Plan your tailor-made trip', text='Tell us your dates, starting city and what you would love to see. We will design a private itinerary and send you a personal quote.')
    ed = [container(eid(332, 'c1'), [w_html(eid(332, 'w1'), top)]), book_container(332, head)]
    return dict(ID=332, title='Morocco Tours & Desert Trips', ed=ed,
                content='<p>Private Morocco tours and desert trips from Marrakech, Fes, Casablanca, Agadir and Tangier.</p>' + ''.join('<h3>%s</h3>' % esc(t['title']) for t in multi),
                excerpt='Private Morocco tours from 2 to 15 days: Sahara desert trips, imperial cities, Atlas Mountains and the Atlantic coast, from Marrakech, Fes and more.',
                seo='Morocco Tours & Desert Trips | Morocco Sky Travel', kw='Morocco tours')

def daytrips():
    days = [t for t in TOURS if t['kind'] == 'day']
    url = SITE + '/destinations-copy/'
    top = ("<div class='mst'>" + hero(U + '2024/10/WhatsApp-Image-2024-10-28-at-12.15.31-PM-1.jpeg', 'Private day trips', 'Day Trips from Marrakech',
           'Waterfalls, Berber villages, desert sunsets and the Atlantic coast, with private transport from your hotel or riad.', 'Day Trips') +
           "<section class='mst-wrap mst-list'><div class='mst-intro'><span class='mst-eyebrow'>Popular day trips</span><h2>Top day excursions</h2>"
           "<p>%s</p></div>" % esc('Explore Morocco’s most captivating places on a private day excursion. Whether you want coastal relaxation, cultural discovery, mountain adventure or a taste of the desert, each trip combines comfort, authenticity and unforgettable memories, ideal for travellers of all ages.') +
           "<div class='mst-cards'>" + ''.join(card(t) for t in days) + '</div></section>' +
           cta(U + '2025/11/pexels-zakariahanif-12214734-2-scaled.jpg', 'Want to sleep in the Sahara?',
               'Our multi-day tours take you to the Erg Chebbi and Erg Chagaga dunes, with nights in desert camps.', SITE + '/our-destinations/', 'See all tours') +
           '</div>' + itemlist('Day Trips from Marrakech', url, days))
    head = book_head(title='Book your day trip', text='Send us your date, hotel and group size. We will confirm availability and send you a personal quote.')
    ed = [container(eid(353, 'c1'), [w_html(eid(353, 'w1'), top)]), book_container(353, head)]
    return dict(ID=353, title='Day Trips from Marrakech', ed=ed,
                content='<p>Private day trips from Marrakech.</p>' + ''.join('<h3>%s</h3>' % esc(t['title']) for t in days),
                excerpt='Private day trips from Marrakech: Imlil and the Atlas, Ourika Valley, Ouzoud waterfalls, Agafay desert, Essaouira and Ouarzazate.',
                seo='Day Trips from Marrakech | Morocco Sky Travel', kw='day trips from Marrakech')

def contact_cards():
    items = [("<a href='%s' target='_blank' rel='noopener'>" % wa_link('Hello Morocco Sky Travel, I would like some information about a trip.'), 'WhatsApp', PHONE, '</a>'),
             ("<a href='mailto:%s'>" % EMAIL, 'Email', EMAIL, '</a>'),
             ("<a href='tel:+212667307641'>", 'Phone', PHONE, '</a>'),
             ('<div>', 'Office', 'Fez, Morocco – Sais', '</div>')]
    return "<div class='mst-wrap'><div class='mst-contact'>" + ''.join('%s<small>%s</small><b>%s</b>%s' % (a, esc(b), esc(c), d) for a, b, c, d in items) + '</div></div>'

def contact_page(pid, img, eyebrow, h1, lead, crumbs, title, text, extra=None):
    top = "<div class='mst'>" + hero(img, eyebrow, h1, lead, crumbs, ctas=False) + contact_cards() + '</div>'
    head = book_head(title=title, text=text)
    ed = [container(eid(pid, 'c1'), [w_html(eid(pid, 'w1'), top)]), book_container(pid, head)]
    if extra: ed.append(extra)
    return ed

def contact():
    # keep the existing Google map widget from the old page (address: Fes)
    gmap = container(eid(380, 'c4'), [{'id': eid(380, 'w9'), 'elType': 'widget', 'widgetType': 'google_maps', 'elements': [],
                                       'settings': {'address': 'Fes, Morocco', 'zoom': {'unit': 'px', 'size': 12, 'sizes': []}, 'height': {'unit': 'px', 'size': 380, 'sizes': []}}}])
    ed = contact_page(380, U + '2024/10/WhatsApp-Image-2024-10-28-at-12.15.31-PM.jpeg', 'Contact', 'Contact Morocco Sky Travel',
                      'Planning a trip or just have a question? Our team is here to help you explore Morocco’s cities, mountains and deserts.', 'Contact',
                      'Send us a message', 'Tell us about your plans and we will get back to you with ideas, availability and a personal quote.', gmap)
    return dict(ID=380, title='Contact Us', ed=ed, content='<p>Contact Morocco Sky Travel by WhatsApp, phone or email: +212 667 307 641, moroccoskytravel@gmail.com. Office in Fez, Morocco.</p>',
                excerpt='Contact Morocco Sky Travel to plan your private Morocco tour: WhatsApp and phone +212 667 307 641, email moroccoskytravel@gmail.com.',
                seo='Contact Us | Morocco Sky Travel', kw='Morocco Sky Travel contact')

def book():
    ed = contact_page(393, U + '2025/11/pexels-taryn-elliott-4973655-scaled.jpg', 'Book your trip', 'Book Your Morocco Trip',
                      'Send us your request and we will design your private itinerary, with a personal quote and no obligation.', 'Book',
                      'Request your trip', 'Choose a tour from our website or describe your dream trip. We reply with a tailored itinerary and price.')
    return dict(ID=393, title='Book Your Morocco Trip', ed=ed, content='<p>Request a private Morocco tour or day trip. We reply with a tailored itinerary and a personal quote.</p>',
                excerpt='Request your private Morocco tour or day trip with Morocco Sky Travel. Tell us your dates and group size and receive a tailored itinerary and quote.',
                seo='Book Your Morocco Trip | Morocco Sky Travel', kw='book Morocco tour')

def payload(p):
    return {'ID': p['ID'], 'fields': {'post_title': p['title'], 'post_content': p['content'], 'post_excerpt': p['excerpt']},
            'meta_input': {'_elementor_data': nobs(json.dumps(p['ed'], ensure_ascii=False, separators=(',', ':'))),
                           '_elementor_edit_mode': 'builder', '_wp_page_template': 'elementor_header_footer',
                           'site-post-title': 'disabled', 'ast-title-bar-display': 'disabled', 'ast-featured-img': 'disabled',
                           'rank_math_title': p['seo'], 'rank_math_description': p['excerpt'], 'rank_math_focus_keyword': p['kw']}}

if __name__ == '__main__':
    css = open('style.css').read()
    form = "<form class='wpcf7-form'><div class='mst-f'><label>Full name <em>*</em><span class='wpcf7-form-control-wrap'><input type='text'></span></label><label>Email <em>*</em><span class='wpcf7-form-control-wrap'><input type='email'></span></label><div class='full'><input class='wpcf7-submit' type='submit' value='Send my request'></div></div></form>"
    for p in (destinations(), daytrips(), contact(), book()):
        json.dump(payload(p), open('out/%d.json' % p['ID'], 'w'), ensure_ascii=False)
        body = p['ed'][0]['elements'][0]['settings']['html'] + "<div class='mst-book' id='book'>" + p['ed'][1]['elements'][0]['settings']['html'] + "<div class='mst-formbox'><div class='wpcf7'>" + form + '</div></div></div>'
        preview(str(p['ID']), body, css)
    print('ok')
