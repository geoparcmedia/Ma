from common import *
from images import GALLERY, gal, FLEET, FLEET_ORIG

U = B + '2025/11/'

# ---------- home ----------
def home():
    featured = [BY_ID[i] for i in (3353, 3339, 3359, 3351, 3331, 3390)]
    marquee = ''.join('<span>' + w + '</span><i>✦</i>' for w in ['Plan smarter', 'Travel better', 'Epic Travel Morocco', 'Imperial cities', 'Atlas Mountains', 'Sahara dunes'])
    why = [('favorite-location-1.svg', 'Authentic Local Experience', 'Our native guides reveal the real Morocco — its traditions, hidden gems, and warm hospitality.'),
           ('casablanca.svg', 'Customized Tours', 'Whether you seek adventure, culture, or relaxation, we design tailor-made itineraries to match your style.'),
           ('protection.svg', 'Sustainable Tourism', 'We partner with local communities and eco-friendly lodges to protect Morocco’s beauty and culture.'),
           ('hotel.svg', 'Comfort & Safety', 'Travel with modern vehicles, hand-picked accommodations, and dedicated 24/7 support.')]
    whyh = ''.join("<div class='et-rv'><span class='ic'><img src='" + U + f + "' width='38' height='38' alt='' loading='lazy'></span><h3>" + t + "</h3><p>" + d + "</p></div>" for f, t, d in why)
    galh = ''.join("<a href='" + o + "' target='_blank' rel='noopener' class='et-rv' aria-label='Open photo " + str(n + 1) + "'><img src='" + c + "' width='600' height='810' alt='Epic Travel Morocco travellers – photo " + str(n + 1) + "' loading='lazy' decoding='async' data-o='" + o + "' onerror=etF(this)></a>" for n, (c, o) in enumerate(map(gal, GALLERY)))
    body = (
        hero('hero1', 'Epic Travel Morocco', 'Where Every Journey Becomes an Epic Story',
             'Private tours across Morocco — from the blue streets of Chefchaouen and the medinas of Fes to the golden dunes of the Sahara — planned by a local team in Marrakech.',
             "<a class='et-btn' href='" + SITE + "/destination/'>Explore our tours " + ICON['arrow'] + "</a><a class='et-btn et-btn-w' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "Plan with us on WhatsApp</a>", small=False)
        + "<div class='et'><div class='et-wrap'><div class='et-facts'><div><b>15</b><span>ready-made itineraries</span></div><div><b>3–15</b><span>days, every tour private</span></div>"
          "<div><b>4×4 · Van · Bus</b><span>our own fleet with driver</span></div><div><b>24/7</b><span>support during your trip</span></div></div></div></div>"
        + "<section class='et et-sec'><div class='et-wrap et-split'><div class='et-archimg et-rv'>" + img('taryn', 'Traveller in a Moroccan medina', w=600, h=750)
        + "<div class='et-badge'><b>Marrakech</b><span>our home base — local drivers &amp; guides who know every road</span></div></div>"
          "<div class='et-rv'><span class='et-eye'>Welcome</span><h2>Welcome to Epic Travel Morocco</h2>"
          "<p style='font-size:19px;color:var(--et-navy)'>Your gateway to the magic, history, and vibrant culture of Morocco.</p>"
          "<p>We craft journeys that take you to the heart of Morocco’s most captivating destinations — a blend of adventure, discovery, and cultural immersion, shaped around your dates, pace and style.</p>"
          "<ul class='et-list'><li>Imperial cities: Fes, Meknes, Rabat and Marrakech</li><li>Camel treks and nights under the stars in Merzouga and Erg Chigaga</li><li>Kasbahs, gorges and palm oases of the south</li><li>Chefchaouen, the blue pearl of the Rif</li></ul>"
          "<div class='et-ctas'><a class='et-btn et-btn-o' href='" + SITE + "/about-us/'>About us</a><a class='et-btn' href='" + SITE + "/destination/'>Explore more " + ICON['arrow'] + "</a></div></div></div></section>"
        + "<div class='et et-mq' aria-hidden='true'><div>" + marquee + "</div><div>" + marquee + "</div></div>"
        + "<section class='et et-sec et-pat'><div class='et-wrap'><div class='et-head'>" + ORN + "<span class='et-eye'>Popular destinations</span><h2>Our most-loved Morocco tours</h2>"
          "<p>Every program is private and can be adjusted — start date, pace, hotels and stops.</p></div><div class='et-grid'>"
        + ''.join(card(t) for t in featured) + "</div><div class='et-center'><a class='et-btn et-btn-o' href='" + SITE + "/destination/'>See all 15 tours " + ICON['arrow'] + "</a></div></div></section>"
        + "<section class='et et-sec et-dark'><div class='et-wrap'><div class='et-head'><span class='et-eye'>Epic Travel Morocco</span><h2>Why travel with us</h2>"
          "<p>A small local team, our own vehicles and drivers, and itineraries built around you.</p></div><div class='et-why'>" + whyh + "</div></div><div class='et-band' style='position:absolute;left:0;right:0;bottom:0'></div></section>"
        + "<section class='et et-sec'><div class='et-wrap'><div class='et-head'>" + ORN + "<span class='et-eye'>Gallery</span><h2>From our adventures</h2><p>Real moments from our travellers on the road with us.</p></div>"
          "<div class='et-gal'>" + galh + "</div></div></section>"
        + "<section class='et et-sec et-cream' style='padding-bottom:30px'><div class='et-wrap'><div class='et-head' style='margin-bottom:10px'><span class='et-eye'>Reviews</span><h2>Hear it from our happy travellers</h2></div></div></section>"
    )
    after = cta('Let’s plan your Moroccan adventure', 'Tell us your dates and what you dream of seeing — we reply within 24 hours with a route and a price.')
    org = {"@context": "https://schema.org", "@type": "TravelAgency", "name": "Epic Travel Morocco", "url": SITE + "/", "logo": LOGO, "email": EMAIL,
           "telephone": "+212661292596", "address": {"@type": "PostalAddress", "addressLocality": "Marrakech", "postalCode": "22000", "streetAddress": "Gueliz", "addressCountry": "MA"},
           "sameAs": [FB, IG, TA]}
    return [('html', clean(body)), ('shortcode', '[trustindex no-registration=tripadvisor]'), ('html', clean(after + ldjs([org])))]

# ---------- tours list ----------
def tours_page():
    chips = [('all', 'All tours'), ('short', '3–5 days'), ('desert', 'Sahara desert'), ('imperial', 'Imperial cities'), ('north', 'Chefchaouen & the north'), ('coast', 'Coast'), ('grand', 'Grand tours 10+ days')]
    chh = ''.join("<button type='button' class='et-chip" + (' on' if k == 'all' else '') + "' data-f='" + k + "'>" + n + "</button>" for k, n in chips)
    order = sorted(TOURS, key=lambda t: t['days'])
    cards = ''.join(card(t, " data-g='" + GROUP[t['id']] + "'") for t in order)
    js = ("<script>(function(){var c=document.querySelectorAll('.et-chip'),k=document.querySelectorAll('.et-grid .et-card');"
          "function f(v){c.forEach(function(b){b.classList.toggle('on',b.getAttribute('data-f')===v)});k.forEach(function(a){a.classList.toggle('et-hide',v!=='all'&&(' '+a.getAttribute('data-g')+' ').indexOf(' '+v+' ')<0);a.classList.add('in')})}"
          "c.forEach(function(b){b.addEventListener('click',function(){f(b.getAttribute('data-f'))})});"
          "var m=location.hash.replace('#',''),ok=0;c.forEach(function(b){if(b.getAttribute('data-f')===m)ok=1});if(ok)f(m)})();</script>")
    body = (hero('hero2', 'Morocco tours', 'Find your Morocco journey',
                 'Fifteen private itineraries from 3 to 15 days — desert escapes from Marrakech, the imperial cities, the blue north and grand tours of the whole country.',
                 "<a class='et-btn' href='#et-list'>Browse the tours " + ICON['arrow'] + "</a><a class='et-btn et-btn-w' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "Ask for a custom tour</a>",
                 crumb="<div class='et-crumb'><a href='" + SITE + "/'>Home</a> / Tours</div>")
            + "<section class='et et-sec et-pat' id='et-list'><div class='et-wrap'><div class='et-head'>" + ORN + "<span class='et-eye'>Our programs</span><h2>All Morocco tours</h2>"
              "<p>Pick a style or a length. Every tour starts on the date you choose, with your own driver.</p></div><div class='et-chips'>" + chh + "</div>"
              "<div class='et-grid'>" + cards + "</div></div></section>"
            + cta('Didn’t find the perfect route?', 'We build private tours of any length — tell us your dates, the places you want to see and your travel style.') + js)
    items = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": n + 1, "url": turl(t), "name": t['name']} for n, t in enumerate(order)]}
    return [('html', clean(body + ldjs([items])))]

# ---------- single tour ----------
def para(text):
    out, ul = [], []
    for block in text.split('\n\n'):
        lines = block.split('\n')
        if lines[0].startswith('► '):
            out.append('<h4>' + lines[0][2:] + '</h4>' + ''.join('<p>' + l + '</p>' for l in lines[1:]))
            continue
        items = [l[2:] for l in lines if l.startswith('- ')]
        rest = [l for l in lines if not l.startswith('- ')]
        if rest:
            out.append('<p>' + '<br>'.join(rest) + '</p>')
        if items:
            out.append('<ul>' + ''.join('<li>' + i + '</li>' for i in items) + '</ul>')
    return ''.join(out)

def tour_page(t):
    days = []
    n = 0
    for d in t['plan']:
        if len(d) == 3:
            label, title, text = d
            n = int(re.findall(r'\d+', label)[-1])
            node = re.findall(r'\d+', label)[0]
        else:
            n += 1
            label, (title, text) = 'Day %d' % n, d
            node = str(n)
        days.append("<details class='et-day et-rv'" + (' open' if not days else '') + "><summary><span class='et-node'>" + node + "</span><small>" + label + "</small><b>" + title.replace(' | ', ' · ') + "</b></summary>"
                    "<div class='et-day-b'>" + para(text) + "</div></details>")
    note = t.get('note', 'Every itinerary can be adapted — start date, number of days, hotels and stops.')
    msg = ('Hello Epic Travel Morocco, I am interested in ' + ('' if t['name'].startswith('The ') else 'the ') + t['name'] + ' (' + str(t['days']) + ' days). ').replace(' ', '%20').replace('&', 'and').replace('’', '').replace('–', '-')
    others = [x for x in TOURS if x['id'] != t['id']]
    rel = sorted(others, key=lambda x: (len(set(GROUP[x['id']].split()) & set(GROUP[t['id']].split())) * -10 + abs(x['days'] - t['days'])))[:3]
    stops_h = ''.join('<span>' + s + '</span>' for s in stops(t))
    nights = t['days'] - 1
    body = (hero(TIMG[t['id']], t['kind'] + ' · ' + str(t['days']) + ' days', t['name'], t['intro'],
                 "<a class='et-btn' href='#et-iti'>See the day-by-day plan " + ICON['arrow'] + "</a><a class='et-btn et-btn-w et-btn-wa' href='" + WA + "?text=" + msg + "' target='_blank' rel='noopener'>" + ICON['wa'] + "Book on WhatsApp</a>",
                 crumb="<div class='et-crumb'><a href='" + SITE + "/'>Home</a> / <a href='" + SITE + "/destination/'>Tours</a> / " + t['name'] + "</div>")
            + "<div class='et'><div class='et-wrap'><div class='et-facts'><div><b>" + str(t['days']) + " days</b><span>" + str(nights) + " nights</span></div>"
              "<div><b>" + t['start'] + "</b><span>starting point</span></div><div><b>" + t['end'] + "</b><span>end of the tour</span></div>"
              "<div><b>Private</b><span>your own driver &amp; vehicle</span></div></div></div></div>"
            + "<section class='et et-sec' id='et-iti'><div class='et-wrap et-tour'><div>"
              "<h3 style='font-size:20px'>Route</h3><div class='et-stops'>" + stops_h + "</div>"
              "<div class='et-iti-h'><div><span class='et-eye'>Itinerary</span><h2>Day by day</h2></div><button type='button' class='et-tog' data-o='0'>Open all days</button></div>"
              "<div class='et-iti'>" + ''.join(days) + "</div>"
              "<div class='et-note'>" + ICON['info'] + "<div><b>Tailor-made:</b> " + note + " Tell us your dates and we send you a detailed quote.</div></div></div>"
              "<aside class='et-side'><div class='et-book'><div class='et-book-h et-dark'><h3>Book this tour</h3><p>Free quote within 24 hours — no payment to ask.</p></div>"
              "<ul><li><span>Duration</span><b>" + str(t['days']) + " days / " + str(nights) + " nights</b></li><li><span>Start</span><b>" + t['start'] + "</b></li>"
              "<li><span>End</span><b>" + t['end'] + "</b></li><li><span>Style</span><b>" + t['kind'] + "</b></li><li><span>Type</span><b>Private tour</b></li></ul>"
              "<div class='et-book-f'><a class='et-btn et-btn-wa' href='" + WA + "?text=" + msg + "' target='_blank' rel='noopener'>" + ICON['wa'] + "Book on WhatsApp</a>"
              "<a class='et-btn et-btn-o' href='mailto:" + EMAIL + "?subject=" + t['name'].replace(' ', '%20').replace('&', 'and').replace('’', '').replace('–', '-') + "'>" + ICON['mail'] + "Email us</a>"
              "<a class='et-btn' href='" + SITE + "/contact-2/'>Send a request</a><small>WhatsApp " + PHONE_MA + " · Tel " + PHONE_CA + "</small></div></div></aside></div></section>"
            + "<section class='et et-sec et-pat'><div class='et-wrap'><div class='et-head'>" + ORN + "<span class='et-eye'>You may also like</span><h2>More Morocco tours</h2></div>"
              "<div class='et-grid'>" + ''.join(card(x) for x in rel) + "</div><div class='et-center'><a class='et-btn et-btn-o' href='" + SITE + "/destination/'>All tours " + ICON['arrow'] + "</a></div></div></section>"
            + cta('Make this tour yours', 'Change the start city, add a night in the desert or a day in Essaouira — we adapt every program to you.'))
    js = ("<script>(function(){var b=document.querySelector('.et-tog'),d=document.querySelectorAll('.et-day');if(!b)return;"
          "b.addEventListener('click',function(){var o=b.getAttribute('data-o')!=='1';d.forEach(function(x){x.open=o});b.setAttribute('data-o',o?'1':'0');b.textContent=o?'Close all days':'Open all days'})})();</script>")
    ld = {"@context": "https://schema.org", "@type": "TouristTrip", "name": t['name'], "description": t['intro'], "url": turl(t), "image": IMG[TIMG[t['id']]]['orig'],
          "touristType": t['kind'], "provider": {"@type": "TravelAgency", "name": "Epic Travel Morocco", "url": SITE + "/"}}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Tours", "item": SITE + "/destination/"},
        {"@type": "ListItem", "position": 3, "name": t['name'], "item": turl(t)}]}
    return [('html', clean(body + js + ldjs([ld, crumbs])))]

# ---------- about ----------
def about():
    blocks = [('team', 'Who We Are', 'We are a team of passionate travelers and Morocco enthusiasts who are dedicated to sharing the best of what this incredible country has to offer. With years of experience in the travel industry and a deep understanding of Morocco’s hidden treasures, we pride ourselves on creating tailor-made experiences that are as unique as our clients.'),
              ('reyyan', 'Our Offerings', 'At Epic Travel Morocco, we specialize in personalized travel experiences that highlight the diversity and richness of Moroccan culture. Whether you’re looking for a luxurious escape, an adventure-filled journey, or a cultural immersion, we customize every itinerary to meet your needs and exceed your expectations.'),
              ('kasbah', 'Our Story', 'Epic Travel Morocco began with a simple idea: to offer travelers a more meaningful way to experience Morocco. Our founders, experienced globetrotters with a deep connection to Morocco, saw the need for travel experiences that are authentic, enriching, and truly epic. Today, we are proud to be a leading travel company, known for our personalized approach and commitment to quality.')]
    bh = ''.join("<article class='et-card et-rv' style='text-align:left'><div class='et-card-img' style='aspect-ratio:4/3.6'>" + img(k, h, w=600, h=540) + "</div>"
                 "<div class='et-card-b' style='text-align:left'><span class='et-kind'>0" + str(n + 1) + "</span><h3>" + h + "</h3><p style='color:var(--et-muted);margin:0'>" + p + "</p></div></article>" for n, (k, h, p) in enumerate(blocks))
    body = (hero('kasbah', 'About us', 'Your epic Moroccan adventure awaits', 'A local team crafting journeys to the heart of Morocco’s most captivating destinations.',
                 crumb="<div class='et-crumb'><a href='" + SITE + "/'>Home</a> / About us</div>")
            + "<section class='et et-sec'><div class='et-wrap et-split'><div class='et-archimg et-rv'>" + img('piotr', 'Moroccan landscape', w=600, h=750)
            + "<div class='et-badge'><b>15</b><span>itineraries across Morocco, all private</span></div></div><div class='et-rv'><span class='et-eye'>About us</span><h2>Travel should be adventure, discovery and culture</h2>"
              "<p>At Epic Travel Morocco, we’re passionate about one thing: crafting journeys that take you to the heart of Morocco’s most captivating destinations. Our company was founded on the belief that travel should be a blend of adventure, discovery, and cultural immersion, and we’ve made it our mission to deliver that experience to every traveler who journeys with us.</p>"
              "<div class='et-ctas'><a class='et-btn' href='" + SITE + "/destination/'>Explore more " + ICON['arrow'] + "</a><a class='et-btn et-btn-o' href='" + SITE + "/fleet/'>Our fleet</a></div></div></div></section>"
            + "<section class='et et-sec et-pat'><div class='et-wrap'><div class='et-head'>" + ORN + "<span class='et-eye'>Epic Travel Morocco</span><h2>Who we are</h2></div><div class='et-cards3'>" + bh + "</div></div></section>"
            + cta('Ready to discover Morocco with us?', 'Tell us how you like to travel and we will design a route around you.'))
    return [('html', clean(body))]

# ---------- contact ----------
def contact():
    infos = [('pin', 'Address', 'Gueliz, Marrakech 22000, Morocco', 'https://maps.google.com/?q=Gueliz+Marrakech'),
             ('phone', 'Phone', PHONE_MA + '<br>' + PHONE_CA, 'tel:+212661292596'),
             ('mail', 'Email', EMAIL, 'mailto:' + EMAIL)]
    ih = ''.join("<a class='et-info et-rv' href='" + u + "'" + (" target='_blank' rel='noopener'" if u.startswith('http') else '') + "><span class='ic'>" + ICON[i] + "</span><h3>" + h + "</h3><p style='margin:0'>" + t + "</p></a>" for i, h, t, u in infos)
    top = (hero('marrakech', 'Contact us', 'Let’s start planning',
                'Don’t hesitate to reach out — whether it’s a fully-crafted itinerary or just a question about one of our tours, we’re ready to help. Your Moroccan adventure starts here.',
                "<a class='et-btn et-btn-wa' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "WhatsApp " + PHONE_MA + "</a><a class='et-btn et-btn-w' href='#et-form'>Send a message</a>",
                crumb="<div class='et-crumb'><a href='" + SITE + "/'>Home</a> / Contact</div>")
           + "<section class='et et-sec et-pat'><div class='et-wrap'><div class='et-cards3'>" + ih + "</div></div></section>"
           + "<section class='et et-sec' id='et-form' style='padding:20px 0 34px'><div class='et-wrap'><div class='et-head' style='margin-bottom:0'><span class='et-eye'>Get in touch</span><h2>We’d love to hear from you</h2>"
             "<p>Whether you’re ready to embark on a tailored Moroccan adventure, have questions about one of our tours, or just want to explore options — we’re here. We reply within 24 hours.</p></div></div></section>"
             "<style>.elementor-widget-shortcode .wpcf7{max-width:780px;margin:0 auto;background:#fff;border-radius:22px;padding:36px;box-shadow:0 18px 40px -18px rgba(11,37,71,.35);border-top:4px solid #d1a47b;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif}"
             ".wpcf7 input:not([type=submit]):not([type=checkbox]),.wpcf7 textarea,.wpcf7 select{width:100%;border:1.5px solid #f4ead9;border-radius:12px;padding:13px 15px;font-size:16px;background:#fbf6ee;color:#26313f}"
             ".wpcf7 input:focus,.wpcf7 textarea:focus{outline:0;border-color:#d1a47b;background:#fff}.wpcf7 textarea{min-height:140px}.wpcf7 p{margin:0 0 14px}"
             ".wpcf7 input[type=submit]{background:#b5552f;color:#fff;border:0;border-radius:999px;padding:15px 34px;font-weight:700;font-size:15px;cursor:pointer}.wpcf7 input[type=submit]:hover{background:#9d4524}"
             "@media (max-width:600px){.elementor-widget-shortcode .wpcf7{margin:0 14px;padding:24px 18px}}</style>")
    bottom = ("<section class='et et-sec' style='padding-top:60px'><div class='et-wrap'><iframe class='et-map et-rv' style='height:420px' loading='lazy' title='Epic Travel Morocco – Marrakech' src='https://maps.google.com/maps?q=Gueliz%20Marrakech&amp;t=m&amp;z=12&amp;output=embed'></iframe></div></section>"
              + cta('Prefer to chat?', 'Send us a WhatsApp message — it’s the fastest way to plan your trip with our team.').replace("href='" + SITE + "/contact-2/'>Send a request", "href='mailto:" + EMAIL + "'>Email us"))
    return [('html', clean(top)), ('shortcode', '[contact-form-7 id=f402750]'), ('html', clean(bottom))]

# ---------- fleet ----------
def fleet():
    veh = [('van', 'Mercedes Mini Van', '2 to 7 passengers', 'Ideal for small groups and families, providing a comfortable and private travel option.'),
           ('suv', 'Toyota Prado SUV', '4×4 for adventure', 'For adventurous souls, our SUVs are perfect for exploring Morocco’s diverse and challenging terrains.'),
           ('sprinter', 'Mercedes Sprinter Minibus', '8 to 17 passengers', 'Perfect for medium-sized groups, offering a spacious and relaxing ride while exploring Morocco’s diverse and challenging terrains.'),
           ('bus', 'Big Buses', '18 to 48 passengers', 'Suitable for large groups, ensuring everyone travels together comfortably.')]
    vh = ''.join("<article class='et-rv'><div class='im'><img src='" + (FLEET_ORIG[k] if k == 'bus' else FLEET[k]) + "' width='768' height='600' alt='" + n + " – Epic Travel Morocco' loading='lazy' decoding='async' data-o='" + FLEET_ORIG[k] + "' onerror=etF(this)></div>"
                 "<div class='bd'><span class='et-cap'>" + ICON['users'] + c + "</span><h3>" + n + "</h3><p style='color:var(--et-muted);margin:0'>" + d + "</p></div></article>" for k, n, c, d in veh)
    body = (hero('journey', 'Our fleet', 'Car rental with driver', 'Tailored travel transport service in Morocco — comfortable vehicles and professional drivers for every group size.',
                 "<a class='et-btn et-btn-wa' href='" + WA + "' target='_blank' rel='noopener'>" + ICON['wa'] + "Book a driver</a>",
                 crumb="<div class='et-crumb'><a href='" + SITE + "/'>Home</a> / Our fleet</div>")
            + "<section class='et et-sec'><div class='et-wrap'><div class='et-head'>" + ORN + "<span class='et-eye'>Comfort &amp; safety</span><h2>Experience Morocco in comfort</h2>"
              "<p>Our top-quality transportation services and diverse fleet are designed to meet all your travel needs — from the elegant Mercedes Vito mini vans to the rugged Toyota Prado SUVs, Sprinter minibuses and big buses for groups.</p></div>"
              "<div class='et-veh'>" + vh + "</div></div></section>"
            + "<section class='et et-sec et-dark'><div class='et-wrap et-split'><div class='et-rv'><span class='et-eye'>Professional drivers</span><h2>Medinas, mountain passes and desert tracks</h2>"
              "<p>Each vehicle is meticulously maintained for a smooth and enjoyable ride, while our professional drivers ensure a safe and seamless journey. Whether you’re navigating the historic medinas, crossing the majestic Atlas Mountains, or venturing into the Sahara Desert, you travel in safety and comfort.</p>"
              "<p>Contact us for reliable and personalized services that cater to all your travel needs.</p></div>"
              "<div class='et-archimg et-rv'>" + img('dunes-camel', 'Driving to the Sahara dunes', w=600, h=750) + "</div></div><div class='et-band' style='position:absolute;left:0;right:0;bottom:0'></div></section>"
            + cta('Need a driver for your trip?', 'Airport transfers, day trips or a full tour — tell us your plan and group size.'))
    return [('html', clean(body))]

def page_data(widgets, seed):
    return elementor(widgets, seed)
