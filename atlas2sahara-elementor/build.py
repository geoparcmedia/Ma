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
FONT = 'Helvetica'
WIDTH = 1040

_n = [0]


def eid():
    _n[0] += 1
    return hashlib.md5(('a2s%d' % _n[0]).encode()).hexdigest()[:7]


def box(t=0, r=0, b=0, l=0, unit='px'):
    return {'unit': unit, 'top': str(t), 'right': str(r), 'bottom': str(b), 'left': str(l), 'isLinked': False}


def px(v, unit='px'):
    return {'unit': unit, 'size': v, 'sizes': []}


def typo(size, weight='400', style='', spacing=None, transform='', line=None, mobile=None, prefix='typography'):
    s = {prefix + '_typography': 'custom', prefix + '_font_family': FONT, prefix + '_font_size': px(size), prefix + '_font_weight': weight}
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
    s.update(typo(size, weight, line=1.2, mobile=mobile))
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
    ('atlas-to-sahara-gravel-ride', 'Atlas to Sahara Gravel Ride', '8 days', 'Guided', '€1,190', 'riders-card.jpg',
     'Ride from the snow-capped High Atlas down through the Draa Valley palm groves to the dunes of Merzouga.'),
    ('toubkal-summit-trek', 'Toubkal Summit Trek', '4 days', 'Guided', '€420', 'camels-card.jpg',
     'Climb North Africa\'s highest peak (4,167 m) through Berber villages and walnut-shaded valleys.'),
    ('merzouga-dunes-camel-trek', 'Merzouga Dunes & Camel Trek', '3 days', 'Guided', '€290', 'camels-card.jpg',
     'Camel caravans, a starlit camp in Erg Chebbi and sunrise from the top of the dunes.'),
    ('agafay-atlas-foothills-e-bike-day', 'Agafay & Atlas Foothills E-Bike Day', '1 day', 'Guided', '€95', 'cyclist-card.jpg',
     'An easy e-bike day from Marrakech into the stony Agafay desert and the first Atlas villages.'),
    ('mgoun-valleys-self-guided-walk', 'M\'Goun Valleys Self-Guided Walk', '6 days', 'Self-guided', '€640', 'camels-card.jpg',
     'Walk inn to inn through the Happy Valley of Aït Bouguemez with GPS routes and luggage transfers.'),
    ('zagora-desert-overland', 'Zagora Desert Overland', '5 days', 'Guided', '€560', 'culture-card.jpg',
     'Follow the Draa river south to Zagora and the quieter dunes of Erg Chegaga by 4x4.'),
]

STORIES = [
    ('from-the-atlas-to-the-sahara-what-to-expect', 'From the Atlas to the Sahara: What to Expect', 'camels-card.jpg',
     'Mountain passes, kasbahs, palm valleys and the dunes of Merzouga – a guide to Morocco\'s most spectacular journey.'),
    ('a-taste-of-morocco-dishes-to-try-on-your-trip', 'A Taste of Morocco: Dishes to Try on Your Trip', 'culture-card.jpg',
     'From slow-cooked tagine to Berber bread baked in the sand, here is what to look forward to after a long day outdoors.'),
    ('riding-the-palmeraie-gravel-biking-around-marrakech', 'Riding the Palmeraie: Gravel Biking Around Marrakech', 'cyclist-card.jpg',
     'Dusty tracks, thousands of palm trees and a sunset you will not forget – our favourite easy ride from the city.'),
]

PAD_X = box(0, 22, 0, 22)


def tour_card(slug, title, days, style, price, img, excerpt):
    url = '{TOUR:%s}' % slug
    return column([
        image(IMG + img, url, 210, title, _css_classes='a2s-card-img'),
        kicker(style + ' tour', ACCENT, _position='absolute', _offset_x=px(14), _offset_y=px(14),
               _element_width='auto', _background_background='classic', _background_color=CREAM,
               _padding=box(5, 10, 5, 10), _css_classes='a2s-badge'),
        kicker(days, INK, _padding=box(22, 22, 0, 22)),
        heading(title, 19, 'h3', link=url, _padding=PAD_X),
        text('<p>%s</p>' % excerpt, 13, _padding=PAD_X),
        text('<p>From %s <small>pp</small></p>' % price, 13, INK, _padding=PAD_X),
        button('Book', '{HOME}/#contact', _element_width='auto', _margin=box(0, 0, 24, 22)),
        button('Info ›', url, outline=True, _element_width='auto', _margin=box(0, 0, 24, 14), _css_classes='a2s-link-btn'),
    ], 33, **bg(CARD), padding=box(0, 0, 0, 0), css_classes='a2s-card')


def story_card(slug, title, img, excerpt):
    url = '{POST:%s}' % slug
    return column([
        image(IMG + img, url, 210, title, _css_classes='a2s-card-img'),
        kicker('Our stories', MUTED, _padding=box(22, 22, 0, 22)),
        heading(title, 19, 'h3', link=url, _padding=PAD_X),
        text('<p>%s</p>' % excerpt, 13, _padding=PAD_X),
        button('Read ›', url, outline=True, _element_width='auto', _margin=box(0, 0, 24, 22), _css_classes='a2s-link-btn'),
    ], 33, **bg(CARD), padding=box(0, 0, 0, 0), css_classes='a2s-card')


def review_col():
    return column([
        text('<p><em>“Paste a real review from one of your guests here – for example from Google or TripAdvisor.”</em></p>',
             14, INK, 'center'),
        text('<p>Tour name</p>', 12, '#9AA48C', 'center', _margin=box(0, 0, 0, 0)),
        heading('Guest name', 12, 'p', align='center', weight='600'),
    ], 33, padding=box(10, 10, 10, 10))


def split(img, img_alt, title, html, link, reverse=False):
    media = column([image(IMG + img, height=400, alt=img_alt)], 50, padding=box(0, 0, 0, 0))
    words = column([
        heading(title, 30, mobile=24),
        text(html, 14),
        button('Learn more', link),
    ], 50, **bg(BG), padding=box(42, 40, 42, 40), padding_mobile=box(30, 22, 30, 22), content_position='center')
    cols = [words, media] if reverse else [media, words]
    extra = {'reverse_order_mobile': 'reverse-mobile'} if reverse else {}
    return section(cols, gap='no', padding=box(0 if reverse else 40, 20, 40 if reverse else 12, 20), **bg(CARD), **extra)


page = [
    # Hero
    section([column([
        heading('Bike Tours & Desert Adventures in Morocco', 54, 'h1', '#FFFFFF', 'center', mobile=34),
        text('<p><em>Ride through palm groves, cross the High Atlas, walk with camel caravans into the Sahara and share mint tea '
             'in Berber villages – all with local guides who call this land home.</em></p>'
             '<p><em>Welcome to Morocco, from the Atlas mountains to the Sahara desert.</em></p>', 16, '#FFFFFF', 'center'),
        button('View our tours', '#tours', 'center'),
    ])], width=760, height='min-height', custom_height=px(88, 'vh'), content_position='middle',
        padding=box(80, 20, 80, 20), **bg_image('{THEME}/assets/img/riders.jpg', 0.38)),
    # Sage strip
    section([
        column([kicker('Atlas2Sahara')], 30, content_position='center'),
        column([text('<p>Guided &amp; self-guided tours · Local Moroccan guides · Small groups · Tailor-made trips</p>', 13,
                     align='right', align_mobile='left', _margin=box(0, 0, 0, 0))], 70, content_position='center'),
    ], width=None, padding=box(14, 30, 14, 30), **bg(SAGE)),
    # Tours
    dict(title_block('Our Most Popular Biking and Desert Tours',
                     'Experience the best of Morocco\'s outdoors with Atlas2Sahara\'s favourite biking, hiking and desert trips.'),
         ),
    section([tour_card(*t) for t in TOURS[:3]], gap='extended', padding=box(0, 20, 20, 20), **bg(BG)),
    section([tour_card(*t) for t in TOURS[3:]], gap='extended', padding=box(10, 20, 80, 20), **bg(BG)),
    # Why
    split('cyclist.jpg', 'Cycling through the palm groves near Marrakech', 'Why Cycling in Morocco?',
          '<p>Cycling in Morocco offers a <strong>captivating</strong> and <strong>diverse experience</strong> for riders of '
          '<strong>all levels</strong>, from easy palm-grove loops to epic mountain passes.</p>'
          '<p>Sitting at <em>the gateway to Africa</em>, Morocco packs <strong>snow-capped peaks, desert tracks and green oases</strong> '
          'into a single trip, with quiet roads and a warm welcome in every village.</p>'
          '<p>From the <strong>Palmeraie of Marrakech</strong> to the <strong>passes of the High Atlas</strong>, here\'s why we think '
          'cycling in Morocco is a must-try.</p>', '{TYPE:biking}'),
    split('camels.jpg', 'Camel caravan walking towards the Sahara dunes', 'Why the Sahara Desert?',
          '<p>For those who love exploring on foot, the Sahara offers an experience that is as <strong>peaceful</strong> as it is '
          '<strong>unforgettable</strong>. Walk beside camel caravans across stony plains towards dunes that glow orange at sunset.</p>'
          '<p>From <strong>starlit desert camps</strong> to <strong>ancient kasbahs and oases</strong>, nomadic culture and endless '
          'silence make the desert a place you will want to return to.</p>', '{TYPE:desert}', reverse=True),
    # Custom holidays
    title_block('Your Custom Holidays',
                'Every trip is a personal chapter in your story. Tell us your dates, pace and interests and we will build '
                'the Moroccan journey you have in mind.', button('Contact us', '{CONTACT}', 'center')),
    section([column([
        image(IMG + name + '-square.jpg', link, 320, label),
        heading(label, 14, 'h3', '#FFFFFF', _position='absolute', _offset_x=px(18), _offset_orientation_v='end',
                _offset_y_end=px(16), _element_width='auto', _css_classes='a2s-tile-label',
                **typo(14, '700', spacing=2, transform='uppercase', prefix='typography')),
    ], 33, css_classes='a2s-tile') for name, label, link in [
        ('riders', 'Cycling', '{TYPE:biking}'), ('camels', 'Desert', '{TYPE:desert}'), ('culture', 'Culture', '{TYPE:hiking}')]],
        gap='extended', padding=box(0, 20, 80, 20), _element_id='contact', **bg(BG)),
    # About
    section([column([section([
        column([
            kicker('Local guides, Moroccan hospitality, real adventures'),
            heading('About us', 26),
            text('<p>We craft biking, hiking and desert journeys across Morocco for travellers who want more than a postcard.</p>', 14, INK),
            button('Learn more', '{CONTACT}'),
        ], 50),
        column([text('<p>By partnering with local families, guesthouses and desert camps, we create authentic adventures that also '
                     'support the communities we travel through.</p>', 14, INK)], 50),
    ], inner=True, width=None, gap='extended')], background_background='classic', background_color='rgba(245,244,242,0.72)',
        padding=box(50, 20, 50, 20))], padding=box(40, 20, 40, 20), _element_id='about',
        **bg_image('{THEME}/assets/img/camels.jpg')),
    # Reviews
    title_block('Loved By Our Guests', 'Here\'s what some of our guests have said about their Moroccan adventures.'),
    section([review_col(), review_col(), review_col()], gap='extended', padding=box(0, 20, 80, 20), _element_id='reviews', **bg(BG)),
    # Banner
    section([column([spacer(10)])], width=None, height='min-height', custom_height=px(440), custom_height_mobile=px(260),
            **bg_image('{THEME}/assets/img/cyclist.jpg')),
    # Stories
    title_block('Our Stories', 'Where stories come to life. Explore our travel notes and get inspired.'),
    section([story_card(*s) for s in STORIES], gap='extended', padding=box(0, 20, 80, 20), _element_id='stories', **bg(BG)),
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
