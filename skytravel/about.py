"""About page (366) in the Sahara homepage style (.msx classes)."""
import json
from tours import TOURS, U
from build import SITE, EMAIL, esc, eid, container, w_html, book_container, book_head, ldscript, wa_link
from pages import payload
from home import DUNE, HOME_JS, header, footer, BY

PID = 366
HERO = U + '2025/11/pexels-zakariahanif-12214734-1-scaled.jpg'
P1, P2, P3 = (U + '2024/10/WhatsApp-Image-2024-10-28-at-12.15.%s-PM.jpeg' % n for n in ('30', '31', '32'))
P4 = U + '2025/11/preview-344cbe563516fd0a1b68aa90b684cb15af3e278f525cab66b7d61e2e9d9ee822.jpg'
WA = wa_link('Hello Morocco Sky Travel, I would like help planning a trip to Morocco.')

TIMELINE = [('Roots', 'A grandfather on camelback',
             'Generations ago, our grandfather, a Berber from Zagora, guided travellers across the dunes by camel. The Sahara was not a backdrop for him: it was home, full of stories and traditions.'),
            ('Growth', 'Desert journeys, family-led',
             'Our uncle carried on the tradition and turned our camel treks into real immersive experiences, where hospitality, culture and nature meet under starry desert skies.'),
            ('Today', 'All of Morocco, one family',
             'We now organise private journeys across the whole country, from imperial cities to the Atlas and the coast, while our roots stay firmly in the desert.')]
VALUES = [('i-pin', 'Local, for real', 'We live here. Our guides, drivers and partners are people we know and trust, from Fes to Zagora.'),
          ('i-clock', 'Your trip, your pace', 'Every tour is private. We adapt the route, the hotels and the rhythm of each day to you.'),
          ('i-flag', 'Berber hospitality', 'We welcome you the way we would welcome our own guests: warmly, simply, and always with time for a glass of mint tea.')]

def about_top():
    hero = ("<header class='msx-hero msx-hero--page'><div class='msx-hero-bg' style='background-image:url(%s)'></div><div class='mst-wrap msx-hero-in'>"
            "<nav class='mst-crumbs' aria-label='Breadcrumb'><a href='%s/'>Home</a><span>/</span>About us</nav>"
            "<span class='msx-place'>Zagora <i></i> Sahara <i></i> Fes</span>"
            "<h1>About Morocco Sky Travel <em>A family story from the desert</em></h1>"
            "<p class='msx-lead'>From the sands of Zagora to travellers all over the world: we are a Moroccan family sharing the country we love, one private journey at a time.</p></div>"
            + DUNE % ('msx-dune', '#fffaf2', '#fffaf2') + "</header>") % (HERO, SITE)
    story = ("<section class='msx-sec'><div class='mst-wrap msx-about'><div class='rv'><span class='mst-eyebrow'>Our story</span>"
             "<h2>From the sands of Zagora to the digital age</h2>"
             "<p>Nestled in the south of Morocco, at the gates of the Sahara, our travel company is more than a business: it is a family legacy. "
             "Our story begins in Zagora, where the golden sands and ancient Berber traditions shaped who we are.</p>"
             "<p>Today we welcome travellers from every corner of the world, with the same simple idea our grandfather had: treat every guest like family, and show them the real Morocco.</p>"
             "<ul class='msx-ticks'><li>Family-run since the beginning</li><li>Berber roots in Zagora</li><li>Private tours only</li><li>Based in Fes</li></ul></div>"
             "<div class='msx-pics rv'><span class='p1' style='background-image:url(%s)' role='img' aria-label='The Morocco Sky Travel family in the Sahara'></span>"
             "<span class='p2' style='background-image:url(%s)'></span><span class='msx-seal'><b>7+</b>years of private tours</span></div></div></section>") % (P1, P2)
    tl = ("<section class='msx-sec msx-sec--sand'><div class='mst-wrap'><div class='msx-head rv'><span class='mst-eyebrow'>Three generations</span>"
          "<h2>A legacy of desert journeys</h2></div><ol class='msx-tl'>" +
          ''.join("<li class='rv'><span class='k'>%s</span><h3>%s</h3><p>%s</p></li>" % (k, esc(a), esc(b)) for k, a, b in TIMELINE) + '</ol></div></section>')
    band = ("<section class='msx-band' style='background-image:url(%s)'><div class='mst-wrap msx-band-in rv'><blockquote>“Welcome to Morocco, <em>where our story and your adventure begin.</em>”"
            "<cite>The Morocco Sky Travel family</cite></blockquote><ul class='msx-num'>"
            "<li><b data-n='7' data-s='+'>7+</b><span>years of experience</span></li><li><b data-n='3'>3</b><span>generations in the desert</span></li>"
            "<li><b data-n='21'>21</b><span>ready-made itineraries</span></li><li><b data-n='100' data-s='%%'>100%%</b><span>private tours</span></li></ul></div></section>") % BY[2805]['img']
    modern = ("<section class='msx-sec'><div class='mst-wrap msx-about msx-about--rev'><div class='msx-pics rv'><span class='p1' style='background-image:url(%s)' role='img' aria-label='Travellers with Morocco Sky Travel'></span>"
              "<span class='p2' style='background-image:url(%s)'></span></div><div class='rv'><span class='mst-eyebrow'>Embracing modernity</span>"
              "<h2>Desert roots, modern comfort</h2>"
              "<p>We have grown far beyond our first camel treks. Today we offer a full range of journeys across Morocco: desert trips, imperial cities, mountain treks and coastal escapes, with comfortable vehicles and hand-picked riads and camps.</p>"
              "<p>Technology lets us talk with you before you even land: plan your trip on WhatsApp, follow our journeys on social media, and get a personal itinerary in your inbox. The welcome, though, stays the same as it always was.</p>"
              "<a class='mst-btn mst-btn--dark' href='%s/our-destinations/'>Discover our tours</a></div></div></section>") % (P3, P4, SITE)
    vals = ("<section class='msx-sec msx-sec--sand'><div class='mst-wrap'><div class='msx-head rv'><span class='mst-eyebrow'>What we believe</span><h2>How we travel</h2></div><div class='msx-why'>" +
            ''.join("<div class='rv'><span class='ic'><i class='%s'></i></span><h3>%s</h3><p>%s</p></div>" % (i, esc(a), esc(b)) for i, a, b in VALUES) + '</div></div></section>')
    gal = ("<section class='msx-sec msx-sec--tight'><div class='mst-wrap'><div class='msx-head rv'><span class='mst-eyebrow'>On the road</span><h2>Moments from our journeys</h2></div>"
           "<div class='msx-gal rv'>" + ''.join("<span style='background-image:url(%s)' role='img' aria-label='%s'></span>" % (u, a) for u, a in (
               (P1, 'Our team in the Sahara'), (BY[2847]['img'], 'Camel trek in the dunes'), (P3, 'Travellers with Morocco Sky Travel'),
               (BY[2809]['img'], 'Ait Benhaddou kasbah'), (P2, 'Desert camp evening'))) + '</div></div></section>')
    welcome = ("<section class='msx-sec'><div class='mst-wrap'><div class='msx-cta' style='background-image:url(%s)'><div><span class='mst-eyebrow'>Welcoming you to Morocco</span>"
               "<h2>Ride the Sahara, wander the medinas, travel with family</h2><p>Whether you dream of a camel ride at sunset, the souks of Marrakech or the blue streets of Chefchaouen, we will design the journey with you.</p></div>"
               "<div class='acts'><a class='mst-btn mst-btn--gold' href='#book'>Plan my trip</a><a class='mst-btn mst-btn--ghost' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> WhatsApp us</a></div></div></div></section>") % (HERO, WA)
    ld = ldscript({'@context': 'https://schema.org', '@type': 'AboutPage', 'name': 'About Morocco Sky Travel', 'url': SITE + '/elementor-366/',
                   'about': {'@id': SITE + '/#agency'}, 'breadcrumb': {'@type': 'BreadcrumbList', 'itemListElement': [
                       {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
                       {'@type': 'ListItem', 'position': 2, 'name': 'About us', 'item': SITE + '/elementor-366/'}]}})
    return "<div class='mst msx'>" + hero + story + tl + band + modern + vals + gal + welcome + '</div>' + HOME_JS + ld

def about():
    head = book_head(title='Start planning with our family', text='Tell us your dates and what you would love to see. We reply with a free, personal itinerary.')
    ed = [container(eid(PID, 'c1'), [w_html(eid(PID, 'w1'), about_top())]), book_container(PID, head)]
    content = ('<h2>From the sands of Zagora to the digital age</h2><p>Morocco Sky Travel is a family-run travel company with Berber roots in Zagora, '
               'at the gates of the Sahara. Our grandfather guided travellers across the dunes by camel; today we organise private tours, desert trips '
               'and tailor-made journeys across Morocco.</p><h2>Desert roots, modern comfort</h2><p>Private drivers, hand-picked riads and desert camps, '
               'and itineraries designed around you.</p>')
    return dict(ID=PID, title='About Us', ed=ed, content=content,
                excerpt='Morocco Sky Travel is a family-run travel company with Saharan roots in Zagora, offering private tours, desert trips and tailor-made journeys across Morocco.',
                seo='About Us | Morocco Sky Travel, a Family from the Sahara', kw='Morocco Sky Travel')

if __name__ == '__main__':
    p = about()
    json.dump(payload(p), open('out/366.json', 'w'), ensure_ascii=False)
    css = open('style.css').read()
    body = p['ed'][0]['elements'][0]['settings']['html'] + "<div class='mst-book' id='book'>" + p['ed'][1]['elements'][0]['settings']['html'] + "<div class='mst-formbox'><div class='wpcf7'>form</div></div></div>"
    open('preview/about.html', 'w').write("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{margin:0}" + css + '</style></head><body>' + header() + body + footer() + '</body></html>')
    print('ok', len(json.dumps(p['ed'])))
