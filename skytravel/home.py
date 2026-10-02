"""Homepage (479), header (308) and footer (316) in the Morocco Sky Travel design system."""
import json
from tours import TOURS, U
from build import (SITE, WA, PHONE, EMAIL, esc, eid, card, container, w_html, w_sc, book_container,
                   book_head, ldscript, nobs, wa_link)
from pages import WHY

LOGO = U + '2024/10/LOGO-COLEU.png'
LOGO_W = U + '2024/10/BLN.png'
BY = {t['id']: t for t in TOURS}
NAV = [('Home', '/'), ('Tours', '/our-destinations/'), ('Day Trips', '/destinations-copy/'), ('About', '/elementor-366/'), ('Contact', '/contact-us/')]
SOCIAL = [('Facebook', 'https://m.facebook.com/p/Moroccoskytravel-100063598419420/'),
          ('Instagram', 'https://www.instagram.com/moroccoskytravel/'),
          ('Snapchat', 'https://snapchat.com/t/V3WuOytE')]

def header():
    links = ''.join("<a href='%s%s'>%s</a>" % (SITE, u, n) for n, u in NAV)
    js = ("<script>(function(){var p=location.pathname;document.querySelectorAll('.msh-nav a').forEach(function(a){var h=new URL(a.href).pathname;"
          "if(h===p||(h!=='/'&&p.indexOf(h)===0))a.classList.add('on')});"
          "var b=document.querySelector('.msh-burger'),n=document.getElementById('msh-nav');if(b&&n)b.addEventListener('click',function(){var o=n.classList.toggle('open');"
          "b.setAttribute('aria-expanded',o?'true':'false')})})()</script>")
    return ("<div class='mst msh'><div class='msh-in'><a class='msh-logo' href='%s/' aria-label='Morocco Sky Travel home'><img src='%s' alt='Morocco Sky Travel' height='56'></a>"
            "<nav class='msh-nav' id='msh-nav' aria-label='Main menu'>%s<a class='msh-m' href='%s/book/'>Book your trip</a></nav>"
            "<div class='msh-act'><a class='msh-wa' href='%s' target='_blank' rel='noopener' aria-label='WhatsApp'><i class='i-wa'></i><span>%s</span></a>"
            "<a class='mst-btn mst-btn--gold msh-cta' href='%s/book/'>Book your trip</a>"
            "<button type='button' class='msh-burger' aria-label='Menu' aria-expanded='false' aria-controls='msh-nav'><span></span><span></span><span></span></button></div></div></div>%s") % (
        SITE, LOGO, links, SITE, wa_link('Hello Morocco Sky Travel, I would like some information about a trip.'), PHONE, SITE, js)

def footer():
    tours = [BY[i] for i in (2805, 2794, 2771, 2847, 2814, 2829)]
    col_t = ''.join("<li><a href='%s/%s/'>%s</a></li>" % (SITE, t['url'], esc(t['card'])) for t in tours)
    col_c = ''.join("<li><a href='%s%s'>%s</a></li>" % (SITE, u, n) for n, u in NAV + [('Book your trip', '/book/')])
    soc = ''.join("<a href='%s' target='_blank' rel='noopener'>%s</a>" % (u, n) for n, u in SOCIAL)
    return ("<footer class='mst msf'><div class='mst-wrap msf-grid'>"
            "<div class='msf-brand'><img src='%s' alt='Morocco Sky Travel' height='64' loading='lazy'><p>%s</p><div class='msf-soc'>%s</div></div>"
            "<div><h3>Popular tours</h3><ul>%s</ul></div><div><h3>Company</h3><ul>%s</ul></div>"
            "<div><h3>Contact</h3><ul class='msf-ct'><li><a href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> %s</a></li>"
            "<li><a href='mailto:%s'><i class='i-mail'></i> %s</a></li><li><a href='tel:+212667307641'><i class='i-phone'></i> Call us: %s</a></li>"
            "<li><span><i class='i-pin'></i> Fez, Morocco – Sais</span></li></ul></div></div>"
            "<div class='mst-wrap msf-bot'><span>© <span class='msf-y'>2026</span> Morocco Sky Travel. All rights reserved.</span><a href='%s/our-destinations/'>Private Morocco tours &amp; desert trips</a></div></footer>"
            "<script>document.querySelectorAll('.msf-y').forEach(function(e){e.textContent=new Date().getFullYear()})</script>") % (
        LOGO_W, esc('Join us at Morocco Sky Travel and let us guide you through the enchanting landscapes and vibrant cultures of Morocco. Your adventure awaits!'),
        soc, col_t, col_c, wa_link('Hello Morocco Sky Travel, I would like some information about a trip.'), PHONE, EMAIL, EMAIL, PHONE, SITE)

SERVICES = [('i-car', 'Tours around Morocco by car', 'Explore the landscapes and cultural heritage of Morocco with private, expertly guided road trips, from bustling cities to quiet coastal towns.'),
            ('i-flag', 'Desert tours by camel', 'Ride across the golden dunes of the Sahara and spend nights under a sky full of stars in traditional desert camps.'),
            ('i-pin', 'Trekking in the Atlas Mountains', 'Discover the rugged beauty of the Atlas with guided treks for every level, from first-time hikers to experienced walkers.')]
DEST = [('Marrakech', U + '2025/11/pexels-reyyan-505450018-33429795-1-scaled.jpg'), ('Merzouga', U + '2025/11/pexels-vlasceanu-19190946-scaled.jpg'),
        ('Fes', U + '2025/11/pexels-artem-yellow-422929671-15188458-1-scaled.jpg'), ('Casablanca', U + '2025/11/pexels-taryn-elliott-3889986-1-scaled.jpg')]

def home_top():
    feat = [BY[i] for i in (2805, 2794, 2771, 2847, 2814, 2829)]
    days = [BY[i] for i in (2947, 2943, 2934)]
    hero = ("<header class='mst-hero mst-hero--home' style='background-image:url(%s)'><div class='mst-wrap'><span class='mst-eyebrow'>Private tours · Sahara · Atlas · Imperial cities</span>"
            "<h1>Private Morocco Tours &amp; Sahara Desert Trips</h1><p class='mst-lead'>Travel smarter, travel better. Tailor-made journeys through Morocco’s imperial cities, mountains and deserts, with a family-run local team and your own private driver.</p>"
            "<div class='mst-hero-ctas'><a class='mst-btn mst-btn--gold' href='%s/our-destinations/'>Explore our tours</a><a class='mst-btn mst-btn--ghost' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> WhatsApp us</a></div>"
            "<ul class='mst-stats'><li><b>7+</b><span>years of experience</span></li><li><b>20+</b><span>ready-made itineraries</span></li><li><b>100%%</b><span>private &amp; tailor-made</span></li></ul></div></header>") % (
        U + '2025/11/pexels-taryn-elliott-4253829-scaled.jpg', SITE, wa_link('Hello Morocco Sky Travel, I would like help planning a trip to Morocco.'))
    svc = ("<section class='mst-wrap mst-band'><div class='mst-intro'><span class='mst-eyebrow'>What we offer</span><h2>Journeys designed around you</h2>"
           "<p>Morocco Sky Travel creates private trips across Morocco. Our knowledge and passion for the country’s beauty and culture make every journey personal and unforgettable.</p></div>"
           "<div class='mst-svc'>" + ''.join("<div><span class='ic'><i class='%s'></i></span><h3>%s</h3><p>%s</p></div>" % (i, esc(a), esc(b)) for i, a, b in SERVICES) + '</div></section>')
    tours = ("<section class='mst-wrap mst-band'><div class='mst-intro'><span class='mst-eyebrow'>Most popular</span><h2>Our best-loved tours</h2>"
             "<p>Desert nights, mountain villages and imperial cities: start from one of our favourite itineraries and we will adapt it to you.</p></div>"
             "<div class='mst-cards'>" + ''.join(card(t) for t in feat) + "</div><p class='mst-more'><a class='mst-btn mst-btn--dark' href='%s/our-destinations/'>See all tours</a></p></section>") % SITE
    dest = ("<section class='mst-band mst-band--sand'><div class='mst-wrap'><div class='mst-intro'><span class='mst-eyebrow'>Key destinations</span><h2>From the medinas to the dunes</h2>"
            "<p>We cover Morocco’s most iconic and diverse regions, with journeys across all the major cities and breathtaking landscapes.</p></div><div class='mst-dest'>" +
            ''.join("<a href='%s/our-destinations/' style='background-image:url(%s)'><span>%s</span></a>" % (SITE, img, n) for n, img in DEST) + '</div></div></section>')
    about = ("<section class='mst-wrap mst-band'><div class='mst-split'><div class='mst-split-im' style='background-image:url(%s)' role='img' aria-label='Morocco Sky Travel team in the desert'></div>"
             "<div><span class='mst-eyebrow'>About us</span><h2>A family story that began in the sands of Zagora</h2>"
             "<p>Our journey began generations ago with a grandfather who guided travellers across the dunes by camel. Today we carry on that family legacy, with over seven years of experience creating private trips across Morocco.</p>"
             "<p>We blend our Berber heritage with modern comfort, so you can ride across the Sahara, wander through vibrant medinas and discover the Atlas with people who call this land home.</p>"
             "<a class='mst-btn mst-btn--line' href='%s/elementor-366/'>Read our story</a></div></div></section>") % (U + '2024/10/WhatsApp-Image-2024-10-28-at-12.15.31-PM.jpeg', SITE)
    why = ("<section class='mst-wrap mst-band'><div class='mst-intro'><span class='mst-eyebrow'>Why travel with us</span><h2>Authentic, comfortable, local</h2></div><div class='mst-why'>" +
           ''.join('<div><h3>%s</h3><p>%s</p></div>' % (esc(a), esc(b)) for a, b in WHY) + '</div></section>')
    dtrip = ("<section class='mst-wrap mst-band'><div class='mst-intro'><span class='mst-eyebrow'>Short on time?</span><h2>Day trips from Marrakech</h2></div>"
             "<div class='mst-cards'>" + ''.join(card(t) for t in days) + "</div><p class='mst-more'><a class='mst-btn mst-btn--line' href='%s/destinations-copy/'>See all day trips</a></p></section>") % SITE
    ld = ldscript({'@context': 'https://schema.org', '@type': 'TravelAgency', '@id': SITE + '/#agency', 'name': 'Morocco Sky Travel', 'url': SITE + '/',
                   'logo': LOGO, 'image': U + '2025/11/pexels-taryn-elliott-4253829-scaled.jpg', 'telephone': '+212667307641', 'email': EMAIL,
                   'description': 'Family-run travel company offering private Morocco tours, Sahara desert trips and day trips.',
                   'address': {'@type': 'PostalAddress', 'addressLocality': 'Fes', 'addressCountry': 'MA'}, 'sameAs': [u for n, u in SOCIAL]})
    return "<div class='mst'>" + hero + svc + tours + dest + about + why + dtrip + '</div>' + ld

def reviews_head():
    return ("<div class='mst mst-intro' style='margin-bottom:0'><span class='mst-eyebrow'>Testimonials</span><h2>What our travellers say</h2>"
            "<p>Our clients’ satisfaction is our top priority. We are proud to be highly rated on Tripadvisor, where travellers share their experiences with Morocco Sky Travel.</p></div>")

def home():
    k = 479
    rev = container(eid(k, 'c5'), [w_html(eid(k, 'w5'), reviews_head()), w_sc(eid(k, 'w6'), '[trustindex no-registration=tripadvisor]')],
                    {'css_classes': 'mst-rev', 'padding': {'unit': 'px', 'top': '24', 'right': '20', 'bottom': '72', 'left': '20', 'isLinked': False},
                     'flex_gap': {'unit': 'px', 'size': 20, 'column': '20', 'row': '20'}})
    head = book_head(title='Plan your trip with us', text='Tell us your dates, group size and the places you dream of. We will design a private itinerary and send you a personal quote.')
    return [container(eid(k, 'c1'), [w_html(eid(k, 'w1'), home_top())]), rev, book_container(k, head)]

def payload_raw(pid, ed, extra=None):
    m = {'_elementor_data': nobs(json.dumps(ed, ensure_ascii=False, separators=(',', ':')))}
    if extra: m.update(extra)
    return {'ID': pid, 'meta_input': m}

if __name__ == '__main__':
    from build import preview
    css = open('style.css').read()
    hd, ft = header(), footer()
    hed = [container(eid(308, 'c1'), [w_html(eid(308, 'w1'), hd)])]
    fed = [container(eid(316, 'c1'), [w_html(eid(316, 'w1'), ft)])]
    hm = home()
    json.dump(payload_raw(308, hed), open('out/308.json', 'w'), ensure_ascii=False)
    json.dump(payload_raw(316, fed), open('out/316.json', 'w'), ensure_ascii=False)
    json.dump({'ID': 479, 'fields': {'post_title': 'Home'}, 'meta_input': payload_raw(479, hm, {
        '_elementor_edit_mode': 'builder', '_wp_page_template': 'elementor_header_footer', 'site-post-title': 'disabled',
        'ast-title-bar-display': 'disabled', 'ast-featured-img': 'disabled'})['meta_input']}, open('out/479.json', 'w'), ensure_ascii=False)
    body = hm[0]['elements'][0]['settings']['html'] + "<div class='mst-rev' style='padding:24px 20px 72px'>" + reviews_head() + "<div style='height:200px;background:#eee;max-width:1180px;margin:20px auto'>Tripadvisor widget</div></div>"
    open('preview/home.html', 'w').write("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{margin:0}" + css + '</style></head><body>' + hd + body + ft + '</body></html>')
    print('ok', [len(json.dumps(x)) for x in (hed, fed, hm)])
