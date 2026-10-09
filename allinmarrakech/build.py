"""All in Marrakech homepage (EN + FR) as native Elementor widgets.

Brand: tourist transport company – Majorelle blue, gold accent, Montserrat/Inter.
Writes home-en.json and home-fr.json (the `_elementor_data` value of each page).
Run: python3 build.py
"""
import json
import os

import elementor_helpers as E
from elementor_helpers import (box, px, typo, widget, heading, kicker, text, button, image, para, anim, icon_box,
                               spacer, column, section, bg, bg_image)

HERE = os.path.dirname(os.path.abspath(__file__))
BLUE, NAVY, GOLD, CREAM, INK, MUTED, WHITE = '#1E3A8A', '#0F1F4D', '#E0A526', '#F7F5F0', '#14182B', '#4B5068', '#FFFFFF'
UP = 'https://allinmarrakech.com/wp-content/uploads/'
WA = 'https://wa.me/212662667975?text='
PHONE = '+212 662 667 975'
EMAIL = 'allinmarrakechtravel@gmail.com'
PRICE_UPLIFT = 20  # € added to the current site prices


def page_link(page_id):
    return 'https://allinmarrakech.com/?page_id=%d' % page_id


def gold_button(label, link, **extra):
    s = dict(background_color=GOLD, button_text_color=INK, button_background_hover_color=WHITE, hover_color=INK)
    s.update(extra)
    return button(label, link, **s)


def white_outline(label, link, **extra):
    s = dict(outline=True, border_color=WHITE, button_text_color=WHITE, button_background_hover_color=WHITE, hover_color=INK)
    s.update(extra)
    return button(label, link, **s)


def head_block(eyebrow, title, sub, dark=False, align='center'):
    els = [
        kicker(eyebrow, GOLD, align, **anim()),
        heading(title, 40, color=WHITE if dark else INK, align=align, mobile=28, **anim(100)),
    ]
    if sub:
        els.append(text('<p>%s</p>' % sub, 16, '#C9D2EA' if dark else MUTED, align, **anim(200)))
    return els


# Small finishing touches the Elementor UI has no control for (kept in an HTML widget so it travels with the page).
STYLE = ('<style>'
         '.aim2-card{transition:transform .3s ease,box-shadow .3s ease}'
         '.aim2-card:hover{transform:translateY(-6px)}'
         '.aim2-card>.elementor-widget-wrap{overflow:hidden}'
         '.aim2-card-img a{display:block;overflow:hidden}'
         '.aim2-card-img img{transition:transform .6s ease}'
         '.aim2-card:hover .aim2-card-img img{transform:scale(1.06)}'
         '.aim2-veh-img img{object-fit:contain!important;background:#F7F5F0;border-radius:8px}'
         '.aim2-badge{z-index:2}'
         '.aim2-round img{border-radius:14px}'
         '.aim2-link .elementor-button{border:0!important;padding-left:0!important;padding-right:0!important;background:transparent!important;color:#1E3A8A!important}'
         '.aim2-link .elementor-button:hover{text-decoration:underline}'
         '</style>')


T = {
    'en': dict(
        eyebrow='Tourist transport company · Marrakech',
        h1='Your private transport across Morocco',
        lead='Airport transfers, private driver, excursions and group transport – with our own vehicles and professional drivers, 7 days a week.',
        quote='Get a quote on WhatsApp', fleet_btn='See our fleet', call='Call us',
        services_k='What we do', services_h='Transport for every journey',
        services_s='From one traveller to a group of 84, we have the right vehicle and the right driver.',
        services=[
            ('fas fa-plane-arrival', 'Airport transfers', 'Marrakech, Casablanca, Agadir and Fes airports. We follow your flight.'),
            ('fas fa-route', 'City-to-city transfers', 'Essaouira, Agadir, Casablanca, Fes… door to door, no stress.'),
            ('fas fa-user-tie', 'Private driver', 'A vehicle and driver at your disposal by the hour or by the day.'),
            ('fas fa-mountain', 'Excursions with driver', 'We drive you to the Atlas, the desert and the big cities.'),
            ('fas fa-users', 'Groups & events', 'Minibuses and coaches for groups, congresses and weddings.'),
        ],
        fleet_k='Our fleet', fleet_h='Modern, air-conditioned vehicles',
        fleet_s='Clean, comfortable and driven by experienced drivers. Choose the size that fits your group.',
        fleet=[
            ('2026/05/Gemini_Generated_Image_gkvc6sgkvc6sgkvc.png', 'Mercedes E-Class', '1 – 3 passengers', '2 suitcases', 'Business & airport transfers'),
            ('2026/05/Gemini_Generated_Image_3thgsl3thgsl3thg.png', 'Mercedes V-Class', '1 – 7 passengers', '6 suitcases', 'Families & small groups'),
            ('2026/05/pp.png', 'Mercedes Sprinter', '8 – 18 passengers', '15 suitcases', 'Groups & excursions'),
            ('2026/05/Gemini_Generated_Image_dr180udr180udr18.png', 'Tourist coach', '19 – 84 passengers', 'Large luggage hold', 'Big groups & events'),
        ],
        ideal='Ideal for', vq='Get a quote', fleet_all='Transfers & fleet',
        exc_k='Excursions with our vehicles', exc_h='We drive you there',
        exc_s='Your private vehicle and driver for the day, from your riad and back. Prices are per vehicle, for 1 to 4 travellers.',
        per='per vehicle', from_='From', details='View details',
        badge_day='Day trip', badge_multi='Multi-day',
        why_k='Why All in Marrakech', why_h='A local transport company you can trust',
        why_p='We are a Marrakech-based tourist transport company. We know every road, we plan with you, and we answer your messages ourselves.',
        why=['Private vehicles only – no shared buses', 'Price agreed before you travel', 'Experienced, careful drivers',
             'Available 7 days a week, at any hour', 'Help on WhatsApp before and during your trip'],
        steps_k='How it works', steps_h='Book your transport in 3 steps',
        steps=[('1', 'Send your request', 'Dates, number of people, pick-up and destination – by WhatsApp or email.'),
               ('2', 'Receive your price', 'We reply quickly with a clear price and the right vehicle for your group.'),
               ('3', 'Your driver picks you up', 'On time, at the airport, your hotel or your riad. Enjoy the ride.')],
        faq_k='FAQ', faq_h='Frequently asked questions',
        faq=[('Are your transfers and excursions private?', 'Yes. Only you and your group travel in the vehicle, with your own driver.'),
             ('What is included in the price?', 'The air-conditioned vehicle, the driver, fuel and tolls, and pick-up at your hotel or riad. Meals, entrance tickets and accommodation are not included unless agreed.'),
             ('Do you do airport transfers at night?', 'Yes, we work 7 days a week and at any hour. Send us your flight number and we follow your arrival.'),
             ('Can we change the itinerary?', 'Of course. Add stops, change the times or build your own route – just tell us.'),
             ('How do I book and pay?', 'Send us your request on WhatsApp or by email. We reply with the price and the payment options; your booking is confirmed once you accept.')],
        cta_h='Need a driver in Morocco?', cta_p='Tell us where and when – we reply with a clear price.',
        email_btn='Email us',
        days={'day': 'Full day', 'half': 'Half day', '2d': '2 days', '3d': '3 days', '5d': '5 days'},
        trips=[(1927, 1897, 'Agafay Desert at Sunset', 'half', 80), (1930, 1898, 'Ourika Valley & Waterfalls', 'day', 90),
               (1931, 1899, 'Imlil & Toubkal Valley', 'day', 110), (1934, 1900, 'Casablanca from Marrakech', 'day', 155),
               (1935, 1891, 'Aït Ben Haddou & Ouarzazate', 'day', 155), (1922, 1892, 'Merzouga Desert via the Dades Gorges', '3d', 470)],
        fleet_page=1939, wa_text='Hello%20All%20in%20Marrakech%2C%20I%20would%20like%20a%20quote%20for%3A%20',
    ),
    'fr': dict(
        eyebrow='Transport touristique · Marrakech',
        h1='Votre transport privé partout au Maroc',
        lead='Transferts aéroport, chauffeur privé, excursions et transport de groupes – avec nos propres véhicules et des chauffeurs professionnels, 7 jours sur 7.',
        quote='Devis sur WhatsApp', fleet_btn='Voir notre flotte', call='Appelez-nous',
        services_k='Nos services', services_h='Un transport pour chaque trajet',
        services_s='D’un voyageur à un groupe de 84 personnes, nous avons le bon véhicule et le bon chauffeur.',
        services=[
            ('fas fa-plane-arrival', 'Transferts aéroport', 'Aéroports de Marrakech, Casablanca, Agadir et Fès. Nous suivons votre vol.'),
            ('fas fa-route', 'Transferts entre villes', 'Essaouira, Agadir, Casablanca, Fès… de porte à porte, sans stress.'),
            ('fas fa-user-tie', 'Chauffeur privé', 'Un véhicule et un chauffeur à votre disposition à l’heure ou à la journée.'),
            ('fas fa-mountain', 'Excursions avec chauffeur', 'Nous vous conduisons dans l’Atlas, le désert et les grandes villes.'),
            ('fas fa-users', 'Groupes & événements', 'Minibus et autocars pour groupes, congrès et mariages.'),
        ],
        fleet_k='Notre flotte', fleet_h='Des véhicules modernes et climatisés',
        fleet_s='Propres, confortables et conduits par des chauffeurs expérimentés. Choisissez la taille adaptée à votre groupe.',
        fleet=[
            ('2026/05/Gemini_Generated_Image_gkvc6sgkvc6sgkvc.png', 'Mercedes Classe E', '1 – 3 passagers', '2 valises', 'Affaires & transferts aéroport'),
            ('2026/05/Gemini_Generated_Image_3thgsl3thgsl3thg.png', 'Mercedes Classe V', '1 – 7 passagers', '6 valises', 'Familles & petits groupes'),
            ('2026/05/pp.png', 'Mercedes Sprinter', '8 – 18 passagers', '15 valises', 'Groupes & excursions'),
            ('2026/05/Gemini_Generated_Image_dr180udr180udr18.png', 'Autocar de tourisme', '19 – 84 passagers', 'Grande soute à bagages', 'Grands groupes & événements'),
        ],
        ideal='Idéal pour', vq='Demander un devis', fleet_all='Transferts & flotte',
        exc_k='Excursions avec nos véhicules', exc_h='Nous vous y conduisons',
        exc_s='Votre véhicule privé avec chauffeur pour la journée, depuis votre riad et retour. Prix par véhicule, de 1 à 4 voyageurs.',
        per='par véhicule', from_='À partir de', details='Voir le détail',
        badge_day='Excursion', badge_multi='Circuit',
        why_k='Pourquoi All in Marrakech', why_h='Une société de transport locale de confiance',
        why_p='Nous sommes une société de transport touristique basée à Marrakech. Nous connaissons chaque route, nous préparons le trajet avec vous et nous répondons nous-mêmes à vos messages.',
        why=['Véhicules privés uniquement – pas de bus partagé', 'Prix fixé avant le départ', 'Chauffeurs expérimentés et prudents',
             'Disponibles 7 jours sur 7, à toute heure', 'Assistance WhatsApp avant et pendant le voyage'],
        steps_k='Comment ça marche', steps_h='Réservez votre transport en 3 étapes',
        steps=[('1', 'Envoyez votre demande', 'Dates, nombre de personnes, lieu de prise en charge et destination – par WhatsApp ou e-mail.'),
               ('2', 'Recevez votre prix', 'Nous répondons rapidement avec un prix clair et le véhicule adapté à votre groupe.'),
               ('3', 'Votre chauffeur vous attend', 'À l’heure, à l’aéroport, à votre hôtel ou à votre riad. Profitez du trajet.')],
        faq_k='FAQ', faq_h='Questions fréquentes',
        faq=[('Vos transferts et excursions sont-ils privés ?', 'Oui. Seuls vous et votre groupe voyagez dans le véhicule, avec votre propre chauffeur.'),
             ('Que comprend le prix ?', 'Le véhicule climatisé, le chauffeur, le carburant et les péages, ainsi que la prise en charge à votre hôtel ou riad. Repas, entrées et hébergement non inclus sauf accord.'),
             ('Faites-vous des transferts aéroport la nuit ?', 'Oui, nous travaillons 7 jours sur 7 et à toute heure. Envoyez-nous votre numéro de vol, nous suivons votre arrivée.'),
             ('Peut-on modifier l’itinéraire ?', 'Bien sûr. Ajoutez des arrêts, changez les horaires ou créez votre propre trajet – dites-le-nous.'),
             ('Comment réserver et payer ?', 'Envoyez votre demande sur WhatsApp ou par e-mail. Nous répondons avec le prix et les moyens de paiement ; la réservation est confirmée dès votre accord.')],
        cta_h='Besoin d’un chauffeur au Maroc ?', cta_p='Dites-nous où et quand – nous répondons avec un prix clair.',
        email_btn='Écrivez-nous',
        days={'day': 'Journée', 'half': 'Demi-journée', '2d': '2 jours', '3d': '3 jours', '5d': '5 jours'},
        trips=[(1949, 1897, 'Désert d’Agafay au coucher du soleil', 'half', 80), (1952, 1898, 'Vallée de l’Ourika & cascades', 'day', 90),
               (1953, 1899, 'Imlil & vallée du Toubkal', 'day', 110), (1956, 1900, 'Casablanca depuis Marrakech', 'day', 155),
               (1957, 1891, 'Aït Ben Haddou & Ouarzazate', 'day', 155), (1944, 1892, 'Désert de Merzouga par les gorges du Dadès', '3d', 470)],
        fleet_page=1961, wa_text='Bonjour%20All%20in%20Marrakech%2C%20je%20souhaite%20un%20devis%20pour%20%3A%20',
    ),
}

MEDIA = {1897: 'Agafay_Desert_Morocco_20250125_1802_7284.jpg', 1898: 'Ourika_Valley.jpg', 1899: 'Imlil_village_High_Atlas_Mountains.jpg',
         1900: 'Sunrise_in_Casablanca_with_Hassan_II_Mosque.jpg', 1891: 'Kasbah_-_Ait_Ben_Haddou_-_Morocco_-_panoramio.jpg',
         1892: 'Erg_Chebbi_Dunes_Camel_LL.jpg', 1894: 'Jemaa_el-Fnaa_Marrakech_at_sunset.jpg'}


def media(mid):
    return UP + '2026/10/' + MEDIA[mid]


CARD = dict(background_background='classic', background_color=WHITE, padding=box(0, 0, 0, 0), border_radius=box(10, 10, 10, 10),
            margin=box(0, 12, 24, 12), margin_tablet=box(0, 8, 16, 8), margin_mobile=box(0, 0, 20, 0),
            box_shadow_box_shadow_type='yes',
            box_shadow_box_shadow={'horizontal': 0, 'vertical': 10, 'blur': 30, 'spread': 0, 'color': 'rgba(15,31,77,0.08)'})
PAD = box(0, 24, 0, 24)


def vehicle_card(t, img, name, pax, bags, ideal, delay):
    return column([
        image(UP + img, height=200, alt=name, _css_classes='aim2-veh-img', _padding=box(20, 20, 0, 20)),
        heading(name, 20, 'h3', INK, _padding=box(16, 24, 0, 24)),
        widget('icon-list', dict(
            icon_list=[{'_id': E.eid(), 'text': pax, 'selected_icon': {'value': 'fas fa-user-friends', 'library': 'fa-solid'}},
                       {'_id': E.eid(), 'text': bags, 'selected_icon': {'value': 'fas fa-suitcase-rolling', 'library': 'fa-solid'}},
                       {'_id': E.eid(), 'text': t['ideal'] + ': ' + ideal, 'selected_icon': {'value': 'fas fa-check-circle', 'library': 'fa-solid'}}],
            icon_color=BLUE, icon_size=px(14), text_color=MUTED, space_between=px(8), text_indent=px(10),
            _padding=PAD, **typo(14, '400', prefix='icon_typography'))),
        button(t['vq'], WA + t['wa_text'] + name.replace(' ', '%20'), _element_width='auto', _margin=box(6, 0, 26, 24),
               background_color=BLUE),
    ], 25, **CARD, css_classes='aim2-card', **anim(delay))


def trip_card(t, page_id, mid, title, dur, price, delay):
    url = page_link(page_id)
    badge = t['badge_multi'] if dur.endswith('d') else t['badge_day']
    return column([
        image(media(mid), url, 220, title, _css_classes='aim2-card-img'),
        kicker(badge + ' · ' + t['days'][dur], NAVY, _position='absolute', _offset_x=px(14), _offset_y=px(14), _element_width='auto',
               _background_background='classic', _background_color=GOLD, _padding=box(6, 12, 6, 12), _border_radius=box(20, 20, 20, 20),
               _css_classes='aim2-badge'),
        heading(title, 19, 'h3', INK, link=url, _padding=box(20, 24, 0, 24)),
        para('<span style=\'font-size:12px;color:#4B5068\'>%s</span> <strong style=\'font-size:22px;color:#1E3A8A\'>€%d</strong> '
             '<span style=\'font-size:12px;color:#4B5068\'>%s</span>' % (t['from_'], price + PRICE_UPLIFT, t['per']), 14, INK,
             _padding=box(0, 24, 0, 24)),
        button(t['details'] + ' →', url, outline=True, _element_width='auto', _margin=box(0, 0, 24, 24), _css_classes='aim2-link'),
    ], 33, **CARD, css_classes='aim2-card', **anim(delay))


def build(lang):
    t = T[lang]
    wa = WA + t['wa_text']
    hero = section([column([
        kicker(t['eyebrow'], GOLD, **anim()),
        heading(t['h1'], 58, 'h1', WHITE, mobile=36, **anim(150)),
        text('<p>%s</p>' % t['lead'], 18, '#E3E8F5', **anim(300)),
        gold_button(t['quote'], wa, _element_width='auto', selected_icon={'value': 'fab fa-whatsapp', 'library': 'fa-brands'},
                    icon_indent=px(8), **anim(450)),
        white_outline(t['fleet_btn'], '#fleet', _element_width='auto', _margin=box(0, 0, 0, 12), **anim(450)),
        para('<span style=\'opacity:.8\'>%s :</span> <a href=\'tel:+212662667975\' style=\'color:#fff\'><strong>%s</strong></a> · 7/7'
             % (t['call'], PHONE), 15, WHITE, _margin=box(18, 0, 0, 0), **anim(550)),
    ], 70), column([], 30)], height='min-height', custom_height=px(90, 'vh'), content_position='middle',
        padding=box(110, 20, 110, 20), background_background='video',
        background_video_link=UP + '2026/05/tourisme-voyage-travelmorocco-touristbus-marrakechmedina.mp4',
        background_play_on_mobile='yes', background_video_fallback={'url': media(1894), 'id': ''},
        background_overlay_background='gradient', background_overlay_color='rgba(15,31,77,0.92)',
        background_overlay_color_b='rgba(15,31,77,0.35)', background_overlay_gradient_angle={'unit': 'deg', 'size': 90, 'sizes': []})

    services = [section([column(head_block(t['services_k'], t['services_h'], t['services_s']))], width=760,
                        padding=box(90, 20, 30, 20), **bg(CREAM)),
                section([column([icon_box(i, h, d, k * 80)], 20, background_background='classic', background_color=WHITE,
                                 padding=box(26, 22, 26, 22), margin=box(0, 8, 16, 8), border_radius=box(10, 10, 10, 10),
                                 css_classes='aim2-card') for k, (i, h, d) in enumerate(t['services'])],
                        gap='no', padding=box(0, 20, 90, 20), **bg(CREAM))]
    for s in services[1]['elements']:
        for w in s['elements']:
            w['settings'].update(position='top', primary_color=BLUE, icon_size=px(30), title_text_color=INK)

    fleet = [section([column(head_block(t['fleet_k'], t['fleet_h'], t['fleet_s'], dark=True))], width=760,
                     padding=box(90, 20, 30, 20), _element_id='fleet', **bg(NAVY)),
             section([vehicle_card(t, *v, delay=k * 100) for k, v in enumerate(t['fleet'])], gap='no', padding=box(0, 20, 30, 20), **bg(NAVY)),
             section([column([white_outline(t['fleet_all'], page_link(t['fleet_page']), align='center')])], padding=box(0, 20, 90, 20), **bg(NAVY))]

    trips = [section([column(head_block(t['exc_k'], t['exc_h'], t['exc_s']))], width=760, padding=box(90, 20, 30, 20), **bg(CREAM))]
    for row in (t['trips'][:3], t['trips'][3:]):
        trips.append(section([trip_card(t, *tr, delay=k * 100) for k, tr in enumerate(row)], gap='no', padding=box(0, 20, 0, 20), **bg(CREAM)))
    trips[-1]['settings']['padding'] = box(0, 20, 80, 20)

    why = section([
        column([image(media(1891), height=480, alt='Aït Ben Haddou', height_mobile=px(260), _css_classes='aim2-round')], 50,
               padding=box(0, 20, 0, 0), padding_mobile=box(0, 0, 20, 0), **anim()),
        column([
            kicker(t['why_k'], GOLD),
            heading(t['why_h'], 36, mobile=28),
            text('<p>%s</p>' % t['why_p'], 16),
            widget('icon-list', dict(
                icon_list=[{'_id': E.eid(), 'text': w, 'selected_icon': {'value': 'fas fa-check-circle', 'library': 'fa-solid'}} for w in t['why']],
                icon_color=GOLD, icon_size=px(18), text_color=INK, space_between=px(12), text_indent=px(12),
                **typo(15, '500', prefix='icon_typography'))),
            spacer(6),
            button(t['quote'], wa, background_color=BLUE, selected_icon={'value': 'fab fa-whatsapp', 'library': 'fa-brands'}, icon_indent=px(8)),
        ], 50, content_position='center', padding=box(10, 10, 10, 40), padding_mobile=box(0, 0, 0, 0), **anim(150)),
    ], padding=box(100, 20, 100, 20), **bg(WHITE))

    steps = [section([column(head_block(t['steps_k'], t['steps_h'], ''))], width=760, padding=box(90, 20, 20, 20), **bg(CREAM)),
             section([column([
                 heading(n, 22, 'div', NAVY, 'center', _element_width='auto', _background_background='classic', _background_color=GOLD,
                         _padding=box(14, 22, 14, 22), _border_radius=box(50, 50, 50, 50)),
                 heading(h, 19, 'h3', INK, 'center', _margin=box(14, 0, 0, 0)),
                 text('<p>%s</p>' % d, 15, align='center'),
             ], 33, align='center', padding=box(10, 20, 10, 20), **anim(k * 120)) for k, (n, h, d) in enumerate(t['steps'])],
                 padding=box(0, 20, 90, 20), **bg(CREAM))]

    faq = [section([column(head_block(t['faq_k'], t['faq_h'], ''))], width=760, padding=box(90, 20, 20, 20), **bg(WHITE)),
           section([column([widget('accordion', dict(
               tabs=[{'_id': E.eid(), 'tab_title': q, 'tab_content': '<p>%s</p>' % a} for q, a in t['faq']],
               selected_icon={'value': 'fas fa-plus', 'library': 'fa-solid'},
               selected_active_icon={'value': 'fas fa-minus', 'library': 'fa-solid'},
               border_color='#E3E6EF', title_background=CREAM, title_color=INK, tab_active_color=BLUE,
               icon_color=GOLD, icon_active_color=GOLD, content_background_color=WHITE, content_color=MUTED,
               title_padding=box(20, 24, 20, 24), content_padding=box(18, 24, 20, 24),
               **typo(16, '600', prefix='title_typography', family=E.HEAD_FONT),
               **typo(15, '400', line=1.7, prefix='content_typography'), **anim()))])],
               width=860, padding=box(0, 20, 90, 20), **bg(WHITE))]

    cta = section([
        column([
            heading(t['cta_h'], 36, color=WHITE, mobile=28),
            text('<p>%s</p>' % t['cta_p'], 17, '#C9D2EA'),
        ], 55, content_position='center', **anim()),
        column([
            gold_button(t['quote'], wa, _element_width='auto', selected_icon={'value': 'fab fa-whatsapp', 'library': 'fa-brands'},
                        icon_indent=px(8)),
            white_outline(t['email_btn'], 'mailto:' + EMAIL, _element_width='auto', _margin=box(0, 0, 0, 12)),
            para('<a href=\'tel:+212662667975\' style=\'color:#fff\'>%s</a> · <a href=\'mailto:%s\' style=\'color:#fff\'>%s</a>'
                 % (PHONE, EMAIL, EMAIL), 14, '#C9D2EA', align='right', align_mobile='left', _margin=box(16, 0, 0, 0)),
        ], 45, content_position='center', align='flex-end', align_mobile='flex-start', **anim(150)),
    ], padding=box(70, 20, 70, 20), _element_id='contact',
        background_background='gradient', background_color=NAVY, background_color_b=BLUE,
        background_gradient_angle={'unit': 'deg', 'size': 120, 'sizes': []})

    cta['elements'][0]['elements'].append(widget('html', {'html': STYLE}))
    return [hero] + services + fleet + trips + [why] + steps + faq + [cta]


for lang in ('en', 'fr'):
    data = json.dumps(build(lang), ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in data, 'backslash would be stripped by WordPress meta unslashing'
    with open(os.path.join(HERE, 'home-%s.json' % lang), 'w') as f:
        f.write(data)
    print(lang, len(data), 'bytes')
