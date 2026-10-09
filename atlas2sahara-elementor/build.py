"""Build the Atlas2Sahara homepage as native Elementor widgets.

Outputs:
  ../atlas2sahara-theme/inc/elementor-home.json  – used by the theme to create the
      Elementor "Home" page (tokens {THEME}, {HOME}, {TOUR:slug}, {POST:slug}, {TYPE:slug}
      are replaced with real URLs on the site).
  atlas2sahara-home-template.json – same page as an Elementor template file
      (Templates → Saved Templates → Import) with absolute atlas2sahara.com URLs.
"""
import hashlib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

INK, MUTED, BG, CARD, BTN, SAGE, CREAM, ACCENT = '#1B1F1C', '#4A4F4B', '#F5F4F2', '#C1C4C0', '#0F1913', '#C3CBB4', '#ECDDCB', '#C0723F'
FONT = 'Inter'
HEAD_FONT = 'Archivo'
WIDTH = 1040

_n = [0]


def eid():
    _n[0] += 1
    return hashlib.md5(('a2s%d' % _n[0]).encode()).hexdigest()[:7]


def box(t=0, r=0, b=0, l=0, unit='px'):
    return {'unit': unit, 'top': str(t), 'right': str(r), 'bottom': str(b), 'left': str(l), 'isLinked': False}


def px(v, unit='px'):
    return {'unit': unit, 'size': v, 'sizes': []}


def typo(size, weight='400', style='', spacing=None, transform='', line=None, mobile=None, prefix='typography', family=None):
    s = {prefix + '_typography': 'custom', prefix + '_font_family': family or FONT, prefix + '_font_size': px(size), prefix + '_font_weight': weight}
    if mobile:
        s[prefix + '_font_size_mobile'] = px(mobile)
    if style:
        s[prefix + '_font_style'] = style
    if spacing is not None:
        s[prefix + '_letter_spacing'] = px(spacing)
    if transform:
        s[prefix + '_text_transform'] = transform
    if line:
        s[prefix + '_line_height'] = px(line, 'em')
    return s


def widget(kind, settings):
    return {'id': eid(), 'elType': 'widget', 'settings': settings, 'elements': [], 'widgetType': kind}


def heading(text, size=36, tag='h2', color=INK, align='', weight='700', link='', mobile=None, **extra):
    s = {'title': text, 'header_size': tag, 'title_color': color}
    s.update(typo(size, weight, line=1.15, mobile=mobile, family=HEAD_FONT, spacing=-0.5 if size >= 24 else None))
    if align:
        s['align'] = align
    if link:
        s['link'] = {'url': link, 'is_external': '', 'nofollow': ''}
    s.update(extra)
    return widget('heading', s)


def kicker(text, color=INK, align='', **extra):
    s = {'title': text, 'header_size': 'p', 'title_color': color}
    s.update(typo(11, '700', spacing=2, transform='uppercase'))
    if align:
        s['align'] = align
    s.update(extra)
    return widget('heading', s)


def text(html, size=15, color=MUTED, align='', style='', **extra):
    s = {'editor': html, 'text_color': color}
    s.update(typo(size, '400', style=style, line=1.6))
    if align:
        s['align'] = align
    s.update(extra)
    return widget('text-editor', s)


def button(label, link, align='', outline=False, **extra):
    s = {
        'text': label,
        'link': {'url': link, 'is_external': '', 'nofollow': ''},
        'background_color': 'rgba(0,0,0,0)' if outline else BTN,
        'button_text_color': INK if outline else '#FFFFFF',
        'button_background_hover_color': BTN if outline else '#2A3A2F',
        'hover_color': '#FFFFFF',
        'border_radius': box(2, 2, 2, 2),
        'text_padding': box(14, 30, 14, 30),
    }
    if outline:
        s.update({'border_border': 'solid', 'border_width': box(1, 1, 1, 1), 'border_color': INK})
    s.update(typo(11, '700', spacing=2.2, transform='uppercase'))
    if align:
        s['align'] = align
    s.update(extra)
    return widget('button', s)


def image(src, link='', height=None, alt='', **extra):
    s = {'image': {'url': src, 'id': '', 'alt': alt, 'source': 'library'}, 'image_size': 'full', 'width': px(100, '%')}
    if height:
        s.update({'height': px(height), 'object-fit': 'cover'})
    if link:
        s.update({'link_to': 'custom', 'link': {'url': link, 'is_external': '', 'nofollow': ''}})
    s.update(extra)
    return widget('image', s)


def para(html, size=13, color=MUTED, **extra):
    """Paragraph as a Heading widget (tag p): keeps its padding with Elementor's optimized markup."""
    s = {'title': html, 'header_size': 'p', 'title_color': color}
    s.update(typo(size, '400', line=1.6))
    s.update(extra)
    return widget('heading', s)


def anim(delay=0, kind='fadeInUp'):
    s = {'_animation': kind, 'animation_duration': 'normal'}
    if delay:
        s['_animation_delay'] = delay
    return s


def icon_box(icon, title, desc, delay=0):
    s = {'selected_icon': {'value': icon, 'library': 'fa-solid'}, 'title_text': title, 'description_text': desc,
         'position': 'left', 'title_size': 'h3', 'primary_color': ACCENT, 'icon_size': px(26), 'icon_space': px(14),
         'title_color': INK, 'description_color': MUTED, 'title_bottom_space': px(4)}
    s.update(typo(15, '700', prefix='title_typography', family=HEAD_FONT))
    s.update(typo(13, '400', line=1.5, prefix='description_typography'))
    s.update(anim(delay))
    return widget('icon-box', s)


def icon_list(items, color=INK):
    s = {'icon_list': [{'_id': eid(), 'text': t, 'selected_icon': {'value': 'fas fa-check', 'library': 'fa-solid'}} for t in items],
         'icon_color': ACCENT, 'icon_size': px(13), 'text_color': color, 'space_between': px(8), 'text_indent': px(10)}
    s.update(typo(14, '500', prefix='icon_typography'))
    return widget('icon-list', s)


def spacer(h):
    return widget('spacer', {'space': px(h)})


def column(elements, size=100, **settings):
    s = {'_column_size': size, '_inline_size': None}
    s.update(settings)
    return {'id': eid(), 'elType': 'column', 'settings': s, 'elements': elements, 'isInner': False}


def section(columns, inner=False, width=WIDTH, gap='default', **settings):
    s = {'gap': gap}
    if width:
        s['content_width'] = px(width)
    else:
        s['layout'] = 'full_width'
    if not inner:
        s['stretch_section'] = 'section-stretched'
    s.update(settings)
    for c in columns:
        c['isInner'] = inner
    return {'id': eid(), 'elType': 'section', 'settings': s, 'elements': columns, 'isInner': inner}


def bg(color):
    return {'background_background': 'classic', 'background_color': color}


def bg_image(src, overlay=None):
    s = {'background_background': 'classic', 'background_image': {'url': src, 'id': '', 'source': 'library'},
         'background_position': 'center center', 'background_size': 'cover', 'background_repeat': 'no-repeat'}
    if overlay is not None:
        s.update({'background_overlay_background': 'classic', 'background_overlay_color': '#000000',
                  'background_overlay_opacity': px(overlay)})
    return s


def title_block(title, subtitle, extra=None):
    els = [heading(title, 36, align='center', mobile=28),
           text('<p><em>%s</em></p>' % subtitle, 14, align='center', _margin=box(0, 0, 0, 0))]
    if extra:
        els.append(extra)
    return section([column(els)], width=640, padding=box(80, 20, 30, 20), **bg(BG))


IMG = '{THEME}/assets/img/'

TOURS = [
    ('atlas-to-sahara-gravel-ride', 'Atlas to Sahara Gravel Ride', '8 days', 'Guided', '€1,190', 'riders-card.jpg', 'Moderate',
     'Ride from the snow-capped High Atlas down through the Draa Valley palm groves to the dunes of Merzouga.'),
    ('toubkal-summit-trek', 'Toubkal Summit Trek', '4 days', 'Guided', '€420', 'camels-card.jpg', 'Challenging',
     'Climb North Africa\'s highest peak (4,167 m) through Berber villages and walnut-shaded valleys.'),
    ('merzouga-dunes-camel-trek', 'Merzouga Dunes & Camel Trek', '3 days', 'Guided', '€290', 'camels-card.jpg', 'Easy',
     'Camel caravans, a starlit camp in Erg Chebbi and sunrise from the top of the dunes.'),
    ('agafay-atlas-foothills-e-bike-day', 'Agafay & Atlas Foothills E-Bike Day', '1 day', 'Guided', '€95', 'cyclist-card.jpg', 'Easy',
     'An easy e-bike day from Marrakech into the stony Agafay desert and the first Atlas villages.'),
    ('mgoun-valleys-self-guided-walk', 'M\'Goun Valleys Self-Guided Walk', '6 days', 'Self-guided', '€640', 'camels-card.jpg', 'Moderate',
     'Walk inn to inn through the Happy Valley of Aït Bouguemez with GPS routes and luggage transfers.'),
    ('zagora-desert-overland', 'Zagora Desert Overland', '5 days', 'Guided', '€560', 'culture-card.jpg', 'Easy',
     'Follow the Draa river south to Zagora and the quieter dunes of Erg Chegaga by 4x4.'),
]

STORIES = [
    ('from-the-atlas-to-the-sahara-what-to-expect', 'From the Atlas to the Sahara: What to Expect', 'camels-card.jpg', 'Travel guide',
     'Mountain passes, kasbahs, palm valleys and the dunes of Merzouga – a guide to Morocco\'s most spectacular journey.'),
    ('a-taste-of-morocco-dishes-to-try-on-your-trip', 'A Taste of Morocco: Dishes to Try on Your Trip', 'culture-card.jpg', 'Food & culture',
     'From slow-cooked tagine to Berber bread baked in the sand, here is what to look forward to after a long day outdoors.'),
    ('riding-the-palmeraie-gravel-biking-around-marrakech', 'Riding the Palmeraie: Gravel Biking Around Marrakech', 'cyclist-card.jpg', 'Cycling',
     'Dusty tracks, thousands of palm trees and a sunset you will not forget – our favourite easy ride from the city.'),
]

FAQ = [
    ('When is the best time to visit?',
     'Spring (March to May) and autumn (September to November) bring mild days in the mountains and comfortable temperatures in the desert. '
     'Winter is great for the Sahara and Marrakech; summer is best for the High Atlas.'),
    ('How fit do I need to be?',
     'Every tour has a difficulty level. Easy trips suit anyone who is active; moderate and challenging trips need regular riding or hiking. '
     'Tell us about your experience and we will recommend the right trip.'),
    ('Can you tailor a trip for us?',
     'Yes. Dates, pace, accommodation and activities can all be adapted, and we can combine biking, hiking and the desert in one journey.'),
    ('Guided or self-guided – what is the difference?',
     'On guided tours a local guide is with you every day. On self-guided tours you travel at your own pace with GPS routes, a route book, '
     'luggage transfers and our support by phone.'),
    ('How do I book?',
     'Send us your dates and the tour you like. We reply within 24 hours with availability and a detailed proposal.'),
]

CARD_PAD = box(0, 24, 0, 24)
GUTTER = dict(margin=box(0, 12, 0, 12), margin_tablet=box(0, 8, 0, 8), margin_mobile=box(0, 0, 24, 0))
CARD_COL = dict(background_background='classic', background_color=CARD, padding=box(0, 0, 0, 0), css_classes='a2s-card',
                border_radius=box(4, 4, 4, 4), **GUTTER)


def tour_card(slug, title, days, style, price, img, level, excerpt, delay=0):
    url = '{TOUR:%s}' % slug
    return column([
        image(IMG + img, url, 220, title, _css_classes='a2s-card-img'),
        kicker(style + ' tour', ACCENT, _position='absolute', _offset_x=px(14), _offset_y=px(14),
               _element_width='auto', _background_background='classic', _background_color=CREAM,
               _padding=box(5, 10, 5, 10), _css_classes='a2s-badge'),
        kicker(days + '  ·  ' + level, INK, _padding=box(22, 24, 0, 24)),
        heading(title, 20, 'h3', link=url, _padding=CARD_PAD),
        para(excerpt, 13.5, _padding=box(0, 24, 4, 24)),
        para('From <strong>%s</strong> <small>pp</small>' % price, 14, INK, _padding=box(0, 24, 0, 24)),
        button('Book', '{HOME}/#contact', _element_width='auto', _margin=box(8, 0, 26, 24)),
        button('Info ›', url, outline=True, _element_width='auto', _margin=box(8, 0, 26, 18), _css_classes='a2s-link-btn'),
    ], 33, **CARD_COL, **anim(delay))


def story_card(slug, title, img, tag, excerpt, delay=0):
    url = '{POST:%s}' % slug
    return column([
        image(IMG + img, url, 220, title, _css_classes='a2s-card-img'),
        kicker(tag, ACCENT, _padding=box(22, 24, 0, 24)),
        heading(title, 20, 'h3', link=url, _padding=CARD_PAD),
        para(excerpt, 13.5, _padding=box(0, 24, 0, 24)),
        button('Read ›', url, outline=True, _element_width='auto', _margin=box(4, 0, 24, 24), _css_classes='a2s-link-btn'),
    ], 33, **CARD_COL, **anim(delay))


def review_col(delay=0):
    return column([
        heading('“', 72, 'div', '#D9D6CF', 'center', _margin=box(0, 0, -30, 0)),
        para('<em>Paste a real review from one of your guests here – for example from Google or TripAdvisor.</em>', 15, INK,
             align='center'),
        para('Tour name', 12, '#9AA48C', align='center', _margin=box(6, 0, 0, 0)),
        heading('Guest name', 13, 'p', align='center', weight='600'),
    ], 33, padding=box(10, 16, 10, 16), **anim(delay))


def split(img, img_alt, title, html, bullets, link, reverse=False):
    media = column([image(IMG + img, height=460, alt=img_alt, height_mobile=px(260))], 50, padding=box(0, 0, 0, 0))
    words = column([
        kicker('Why travel with us', ACCENT),
        heading(title, 32, mobile=26),
        text(html, 15),
        icon_list(bullets),
        spacer(8),
        button('Learn more', link),
    ], 50, **bg(BG), padding=box(50, 48, 50, 48), padding_mobile=box(34, 22, 34, 22), content_position='center', **anim(150))
    cols = [words, media] if reverse else [media, words]
    extra = {'reverse_order_mobile': 'reverse-mobile'} if reverse else {}
    return section(cols, gap='no', padding=box(0 if reverse else 60, 20, 60 if reverse else 14, 20), **bg(CARD), **extra)


def tile(name, label, desc, link, delay):
    return column([
        spacer(170),
        heading(label, 24, 'h3', '#FFFFFF', link=link),
        para(desc, 14, '#F1EEE8'),
        button('Explore ›', link, outline=True, _css_classes='a2s-link-btn a2s-link-light'),
    ], 33, padding=box(26, 26, 18, 26), content_position='bottom', css_classes='a2s-tile', border_radius=box(4, 4, 4, 4), **GUTTER,
        **bg_image(IMG + name + '-square.jpg'), **anim(delay))


def title_block(title, subtitle, eyebrow='', extra=None, padding_top=96):
    els = []
    if eyebrow:
        els.append(kicker(eyebrow, ACCENT, 'center'))
    els += [heading(title, 40, align='center', mobile=30),
            text('<p>%s</p>' % subtitle, 16, align='center', _margin=box(0, 0, 0, 0))]
    if extra:
        els.append(extra)
    return section([column(els, **anim())], width=680, padding=box(padding_top, 20, 40, 20), **bg(BG))


page = [
    # Hero
    section([column([
        kicker('Morocco  ·  High Atlas  ·  Sahara', '#F3D9BF', 'center', **anim()),
        heading('Bike Tours & Desert Adventures in Morocco', 64, 'h1', '#FFFFFF', 'center', mobile=38, **anim(150)),
        text('<p>Ride through palm groves, cross the High Atlas, walk with camel caravans into the Sahara and share mint tea '
             'in Berber villages – with local guides who call this land home.</p>', 18, '#FFFFFF', 'center', **anim(300)),
        button('View our tours', '#tours', _element_width='auto', **anim(450)),
        button('Plan a custom trip', '{CONTACT}', outline=True, _element_width='auto', border_color='#FFFFFF',
               button_text_color='#FFFFFF', button_background_hover_color='#FFFFFF', hover_color=INK,
               _margin=box(0, 0, 0, 12), **anim(450)),
    ], align='center', css_classes='a2s-hero-col')], width=820, height='min-height', custom_height=px(92, 'vh'), content_position='middle',
        padding=box(90, 20, 90, 20), **bg_image('{THEME}/assets/img/riders.jpg', 0.42)),
    # Feature strip
    section([column([icon_box(i, t, d, k * 100)], 25) for k, (i, t, d) in enumerate([
        ('fas fa-user-friends', 'Local guides', 'Moroccan experts who know every trail.'),
        ('fas fa-route', 'Tested routes', 'Rides and walks we do ourselves.'),
        ('fas fa-shuttle-van', 'Full support', 'Luggage transfers and backup vehicle.'),
        ('fas fa-sliders-h', 'Tailor-made', 'Your dates, your pace, your trip.'),
    ])], padding=box(30, 20, 30, 20), **bg(SAGE)),
    # Tours
    title_block('Our Most Popular Biking and Desert Tours',
                'Experience the best of Morocco\'s outdoors with our favourite biking, hiking and desert trips.', 'Featured tours'),
    section([tour_card(*t, delay=k * 120) for k, t in enumerate(TOURS[:3])], gap='no', padding=box(0, 20, 12, 20), **bg(BG)),
    section([tour_card(*t, delay=k * 120) for k, t in enumerate(TOURS[3:])], gap='no', padding=box(12, 20, 96, 20), **bg(BG)),
    # Why
    split('cyclist.jpg', 'Cycling through the palm groves near Marrakech', 'Why Cycling in Morocco?',
          '<p>Cycling in Morocco is a <strong>diverse experience</strong> for riders of <strong>all levels</strong> – from easy '
          'palm-grove loops to epic mountain passes, with quiet roads and a warm welcome in every village.</p>',
          ['Snow-capped peaks, desert tracks and oases in one trip', 'Quality gravel, road and e-bikes',
           'Support vehicle on guided rides'], '{TYPE:biking}'),
    split('camels.jpg', 'Camel caravan walking towards the Sahara dunes', 'Why the Sahara Desert?',
          '<p>Walk beside camel caravans across stony plains towards dunes that glow orange at sunset. The Sahara is as '
          '<strong>peaceful</strong> as it is <strong>unforgettable</strong>.</p>',
          ['Nights in starlit desert camps', 'Ancient kasbahs and palm oases', 'Nomadic culture and endless silence'],
          '{TYPE:desert}', reverse=True),
    # Custom holidays
    title_block('Your Custom Holidays',
                'Every trip is a personal chapter in your story. Tell us your dates, pace and interests and we will build '
                'the Moroccan journey you have in mind.', 'Made for you', button('Contact us', '{CONTACT}', 'center')),
    section([tile('riders', 'Cycling', 'Gravel, road and e-bike adventures.', '{TYPE:biking}', 0),
             tile('camels', 'Desert', 'Camel treks and Sahara camps.', '{TYPE:desert}', 120),
             tile('culture', 'Culture', 'Music, food and Berber villages.', '{TYPE:hiking}', 240)],
            gap='no', padding=box(0, 20, 96, 20), _element_id='contact', **bg(BG)),
    # About
    section([column([section([
        column([
            kicker('Local guides · Moroccan hospitality', ACCENT),
            heading('About us', 34),
            text('<p>We craft biking, hiking and desert journeys across Morocco for travellers who want more than a postcard.</p>', 16, INK),
            button('Learn more', '{CONTACT}'),
        ], 50),
        column([text('<p>By partnering with local families, guesthouses and desert camps, we create authentic adventures that also '
                     'support the communities we travel through.</p>', 16, INK)], 50, content_position='center'),
    ], inner=True, width=None, gap='extended')], background_background='classic', background_color='rgba(245,244,242,0.86)',
        padding=box(60, 30, 60, 30), border_radius=box(4, 4, 4, 4), **anim())],
        padding=box(90, 20, 90, 20), _element_id='about', **bg_image('{THEME}/assets/img/camels.jpg')),
    # Reviews
    title_block('Loved By Our Guests', 'Here\'s what some of our guests have said about their Moroccan adventures.', 'Reviews'),
    section([review_col(0), review_col(120), review_col(240)], gap='extended', padding=box(0, 20, 96, 20), _element_id='reviews', **bg(BG)),
    # Banner
    section([column([spacer(10)])], width=None, height='min-height', custom_height=px(460), custom_height_mobile=px(260),
            **bg_image('{THEME}/assets/img/cyclist.jpg')),
    # FAQ
    title_block('Good to Know', 'Answers to the questions our guests ask most often.', 'FAQ'),
    section([column([widget('accordion', dict(
        tabs=[{'_id': eid(), 'tab_title': q, 'tab_content': '<p>%s</p>' % a} for q, a in FAQ],
        selected_icon={'value': 'fas fa-plus', 'library': 'fa-solid'},
        selected_active_icon={'value': 'fas fa-minus', 'library': 'fa-solid'},
        border_color='#D9D6CF', title_background='#FFFFFF', title_color=INK, tab_active_color=ACCENT,
        icon_color=ACCENT, icon_active_color=ACCENT, content_background_color='#FFFFFF', content_color=MUTED,
        title_padding=box(20, 24, 20, 24), content_padding=box(0, 24, 22, 24),
        **typo(16, '600', prefix='title_typography', family=HEAD_FONT),
        **typo(14, '400', line=1.7, prefix='content_typography'), **anim()))], 100)],
        width=820, padding=box(0, 20, 96, 20), _element_id='faq', **bg(BG)),
    # Stories
    title_block('Our Stories', 'Where stories come to life. Explore our travel notes and get inspired.', 'Journal', padding_top=0),
    section([story_card(*s, delay=k * 120) for k, s in enumerate(STORIES)], gap='no', padding=box(0, 20, 96, 20),
            _element_id='stories', **bg(BG)),
    # Call to action
    section([
        column([
            kicker('Ready when you are', '#F3D9BF'),
            heading('Let\'s plan your Moroccan adventure', 36, color='#FFFFFF', mobile=28),
            text('<p>Tell us your dates and interests – we reply within 24 hours with a free, no-obligation proposal.</p>', 16, '#D9DDD6'),
        ], 66, content_position='center', **anim()),
        column([
            button('Get in touch', '{CONTACT}', 'right', align_mobile='left', background_color=ACCENT,
                   button_background_hover_color='#FFFFFF', hover_color=INK, **anim(150)),
        ], 34, content_position='center'),
    ], padding=box(70, 20, 70, 20), **bg(BTN)),
]
page[0]['settings']['_element_id'] = 'top-hero'
page[3]['settings']['_element_id'] = 'tours'

data = json.dumps(page, ensure_ascii=False, separators=(',', ':'))
assert all(tok in data for tok in ('{THEME}', '{TOUR:', '{POST:', '{TYPE:', '{HOME}', '{CONTACT}'))
with open(os.path.join(HERE, '..', 'atlas2sahara-theme', 'inc', 'elementor-home.json'), 'w') as f:
    f.write(data)

SITE = 'https://atlas2sahara.com'
absolute = data.replace('{THEME}', SITE + '/wp-content/themes/atlas2sahara').replace('{HOME}', SITE).replace('{CONTACT}', SITE + '/#contact')
absolute = re.sub(r'\{TOUR:([a-z0-9-]+)\}', SITE + r'/tour/\1/', absolute)
absolute = re.sub(r'\{POST:([a-z0-9-]+)\}', SITE + r'/\1/', absolute)
absolute = re.sub(r'\{TYPE:([a-z0-9-]+)\}', SITE + r'/tours/type/\1/', absolute)
template = {'version': '0.4', 'title': 'Atlas2Sahara Home', 'type': 'page',
            'page_settings': {'hide_title': 'yes', 'template': 'elementor_header_footer'},
            'content': json.loads(absolute)}
with open(os.path.join(HERE, 'atlas2sahara-home-template.json'), 'w') as f:
    json.dump(template, f, ensure_ascii=False, indent=1)
print('elements:', _n[0], 'bytes:', len(data))
