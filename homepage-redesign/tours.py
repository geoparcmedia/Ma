U = "https://wegravelmorocco.com/wp-content/uploads/2025/10/"
T = "https://wegravelmorocco.com/trip/"
CYCLING = [
    ("caravan-road-gravel-bike-tour/", "5431893337830453311-580x450.jpg", "Gravel Bike", "Caravan Road Gravel Bike Tour",
     "Skoura oasis, Rose Valley, Dades Gorges, Saghro Mountain and the Draa Valley on ancient caravan tracks.", "8 days · Moderate", 1100),
    ("morocco-cycling-tour/", "5431893337830453207-580x450.jpg", "Mountain / Gravel", "Morocco Cycling Tour: Atlas to Sahara",
     "Cross the Atlas, ride the Draa palm groves and camp under the stars in the Chegaga dunes.", "8 days · Moderate", 1100),
    ("hike-and-bike-morocco-tour/", "5431893337830453213-580x450.jpg", "Hike &amp; Bike", "Toubkal Summit &amp; Agafay by Bike",
     "Climb Toubkal (4167 m), then cycle through Ouirgane and the rocky Agafay desert.", "8 days · Challenging", 1050),
    ("morocco-hike-and-bike-tour/", "5431893337830453245-580x450.jpg", "Hike &amp; Bike", "Happy Valley, Lake &amp; Ouzoud Waterfall",
     "Hike the Happy Valley, then ride the M’Goun Geopark to Bin El Ouidane lake and Ouzoud.", "8 days · Easy to moderate", 1050),
]
TREKKING = [
    ("classic-toubkal-mountain-trek/", "5431893337830453170-580x450.jpg", "Trekking", "Classic Toubkal Trek",
     "Marrakech to the summit of Toubkal (4167 m), the highest peak in North Africa.", "3 days · Moderate to hard", 380),
    ("climb-mount-toubkal-4167-m-13671-ft/", "la-vallee-de-latlas-et-le-mont-toubkal-au-maroc-boerez-benjamin-40758-580x450.jpg", "Trekking", "Berber Villages &amp; Toubkal Peak",
     "Tamsoult valley, Agulzim pass and the Toubkal summit, with a guided tour of Marrakech.", "6 days · Moderate to hard", 600),
    ("climb-mount-mgoun4071m-13356-ft/", "pianchette-top-7989881_1920-1-580x450.jpg", "Trekking", "Happy Valley &amp; M’Goun Summit",
     "Climb M’Goun (4071 m), the second highest peak in North Africa, on old nomad paths.", "8 days · Moderate to hard", 950),
    ("hiking-in-bougmaz-valleykigdom-of-berbers/", "Vue-panoramique-sur-la-vallee-dait-bouguemez-2-scaled-1-580x450.jpg", "Trekking", "Bougmaz Valley: Kingdom of the Berbers",
     "Five easy hiking days village to village in the Happy Valley, with Ouzoud Waterfall.", "8 days · Easy", 890),
    ("edge-of-the-sahara-desert-trek/", "fullsizeoutput_1d1-580x450.jpeg", "Desert Trek", "Sahara Desert Trek",
     "Walk with camels across the dunes of M’hamid El Ghizlan and sleep in desert camps.", "8 days · Easy", 1050),
    ("toubkal-ascent-essaouira-city-4167-m-13671-ft/", "citadelle_essaouira-scaled-1-580x450.jpg", "Trek &amp; Relax", "Toubkal Challenge &amp; Essaouira",
     "A 3-day Toubkal ascent followed by relaxing days in the seaside town of Essaouira.", "7 days · Moderate to hard", 680),
]


def card(slug, img, tag, title, desc, meta, price):
    return (f'<a class="wgm-card" href="{T}{slug}">'
            f'<div class="wgm-card-img"><img src="{U}{img}" width="580" height="450" alt="{title} – We Gravel Morocco" loading="lazy" decoding="async"><span class="wgm-tag">{tag}</span></div>'
            f'<div class="wgm-card-b"><h3>{title}</h3><p>{desc}</p>'
            f'<div class="wgm-meta"><span>{meta}</span><span>from <b>{price} €</b></span></div></div></a>\n')


def tours_html():
    h = ['<section class="wgm-sec" id="tours"><div class="wgm-wrap">',
         '<div class="wgm-head"><span class="wgm-eyebrow">Our tours</span><h2>Guided Cycling &amp; Trekking Tours in Morocco</h2>',
         '<p>Small-group and private departures from Marrakech. All tours include local guides, accommodation, most meals and transport.</p></div>',
         '<div class="wgm-tours"><div class="wgm-tabs"><h3>Cycling &amp; Gravel Bike Tours</h3><a href="https://wegravelmorocco.com/cycling/">All cycling tours →</a></div><div class="wgm-grid wgm-grid4">']
    h += [card(*c) for c in CYCLING]
    h.append('</div><a class="wgm-custom" href="https://wegravelmorocco.com/contact-us/"><img src="' + U + 'DSC01041-2-scaled-1-580x450.jpg" width="580" height="450" alt="Custom gravel bike tour in Morocco" loading="lazy" decoding="async"><div><span class="wgm-tag">Tailor-made</span><h3>Your Custom Bike Tour</h3><p>Already have a route or challenge in mind? We build a private tour around your pace, level and dates – any length, any level.</p><span class="wgm-btn wgm-btn-o">Ask Us for a Custom Tour</span></div></a>\n')
    h.append('</div>')
    h.append('<div class="wgm-tours"><div class="wgm-tabs"><h3>Trekking &amp; Hiking Tours</h3><a href="https://wegravelmorocco.com/trekking/">All trekking tours →</a></div><div class="wgm-grid">')
    h += [card(*c) for c in TREKKING]
    h.append('</div></div></div></section>\n')
    return ''.join(h)


def schema():
    import json
    items = []
    for i, c in enumerate(CYCLING + TREKKING, 1):
        items.append({"@type": "ListItem", "position": i, "item": {
            "@type": "TouristTrip", "name": c[3].replace('&amp;', '&'), "description": c[4],
            "url": T + c[0], "image": U + c[1],
            "offers": {"@type": "Offer", "price": str(c[6]), "priceCurrency": "EUR", "url": T + c[0]}}})
    data = {"@context": "https://schema.org", "@graph": [
        {"@type": "TravelAgency", "@id": "https://wegravelmorocco.com/#agency", "name": "We Gravel Morocco",
         "url": "https://wegravelmorocco.com/", "logo": "https://wegravelmorocco.com/wp-content/uploads/2021/10/ww.png",
         "image": "https://wegravelmorocco.com/wp-content/uploads/2025/10/5431893337830453212-1024x683.jpg",
         "description": "Local tour operator in Marrakech and Azilal offering guided gravel bike, cycling and trekking tours across Morocco.",
         "telephone": "+212660435569", "email": "marouanguide@yahoo.fr", "priceRange": "€€",
         "address": {"@type": "PostalAddress", "addressLocality": "Marrakech", "addressCountry": "MA"},
         "areaServed": "Morocco",
         "sameAs": ["https://www.instagram.com/wegravel_morocco/", "https://www.tripadvisor.com/Attraction_Review-g293734-d32697051-Reviews-Wegravelmorocco-Marrakech_Marrakech_Safi.html"]},
        {"@type": "ItemList", "name": "Guided tours in Morocco", "itemListElement": items}]}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '</script>'
