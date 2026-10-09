"""Compact variant of build.py for sending through the WordPress connector.

Same page and texts as build.py, but card, button and icon styling is done by the page
stylesheet (classes aim2-*) so each widget only carries its content (text, image, link).
Everything stays editable in Elementor; style controls set there override the stylesheet.
Writes home-en-lite.json and home-fr-lite.json.
"""
import json
import os

import build as B

HERE = os.path.dirname(os.path.abspath(__file__))
_n = [0]


def eid():
    _n[0] += 1
    return '%07x' % (0xa100000 + _n[0])


def w(kind, s, cls='', anim=None):
    if cls:
        s['_css_classes'] = cls
    if anim is not None:
        s['_animation'] = 'fadeInUp'
        if anim:
            s['_animation_delay'] = anim
    return {'id': eid(), 'elType': 'widget', 'settings': s, 'widgetType': kind}


def h(text, tag='h2', cls='', anim=None, link=''):
    s = {'title': text, 'header_size': tag}
    if link:
        s['link'] = {'url': link}
    return w('heading', s, cls, anim)


def p(html, cls='', anim=None):
    return w('text-editor', {'editor': '<p>%s</p>' % html}, cls, anim)


def btn(label, link, cls='aim2-btn', icon=None, anim=None):
    s = {'text': label, 'link': {'url': link}}
    if icon:
        s['selected_icon'] = {'value': icon, 'library': 'fa-brands' if icon.startswith('fab') else 'fa-solid'}
        s['icon_indent'] = {'unit': 'px', 'size': 8}
    return w('button', s, cls, anim)


def img(url, alt, cls='', link=''):
    s = {'image': {'url': url, 'id': '', 'alt': alt}, 'image_size': 'full'}
    if link:
        s.update(link_to='custom', link={'url': link})
    return w('image', s, cls)


def ilist(items, icon):
    return w('icon-list', {'icon_list': [{'_id': eid(), 'text': t, 'selected_icon': {'value': i or icon, 'library': 'fa-solid'}}
                                         for t, i in items]})


def col(els, size=100, cls='', **s):
    s['_column_size'] = size
    if cls:
        s['css_classes'] = cls
    return {'id': eid(), 'elType': 'column', 'settings': s, 'elements': els, 'isInner': False}


def sec(cols, cls='', el_id='', **s):
    s.setdefault('gap', 'no')
    s['css_classes'] = ('aim2 ' + cls).strip()
    s['stretch_section'] = 'section-stretched'
    if el_id:
        s['_element_id'] = el_id
    return {'id': eid(), 'elType': 'section', 'settings': s, 'elements': cols, 'isInner': False}


def head(k, title, sub='', align='center'):
    els = [h(k, 'p', 'aim2-k', 0), h(title, 'h2', '', 100)]
    if sub:
        els.append(p(sub, 'aim2-sub', 200))
    return els


STYLE = B.STYLE.replace('</style>', (
    '.elementor-section.aim2>.elementor-container{max-width:1180px}'
    '.elementor-section.aim2-narrow>.elementor-container{max-width:780px}'
    '.aim2{padding:90px 20px}'
    '.aim2-top{padding-bottom:30px}.aim2-tight{padding-top:0}.aim2-nb{padding-bottom:0}'
    '.aim2-cream{background:#F7F5F0}.aim2-white{background:#fff}.aim2-navy{background:#0F1F4D}'
    '.aim2-center{text-align:center}'
    '.aim2 .elementor-heading-title,.aim2 .elementor-heading-title a{color:#14182B}'
    '.aim2-sub,.aim2 .elementor-widget-text-editor{color:#4B5068}'
    '.aim2-navy .elementor-heading-title{color:#fff}'
    '.aim2-navy .aim2-card .elementor-heading-title{color:#14182B}'
    '.aim2-navy .aim2-sub{color:#C9D2EA}'
    '.aim2 .aim2-k .elementor-heading-title{color:#E0A526}'
    '.aim2 .elementor-icon-box-title,.aim2 .elementor-icon-box-title a{color:#14182B}'
    '.aim2 .elementor-icon-box-description{color:#4B5068}'
    '.aim2 .elementor-icon-box-icon .elementor-icon{color:#1E3A8A;fill:#1E3A8A}'
    '.aim2 .elementor-icon-list-text{color:#14182B}'
    '.aim2 .elementor-icon-list-icon i{color:#1E3A8A}.aim2 .elementor-icon-list-icon svg{fill:#1E3A8A}'
    '.aim2 .elementor-tab-title a,.aim2 .elementor-tab-title{color:#14182B}'
    '.aim2 .elementor-tab-content{color:#4B5068;background:#fff}'
    '.aim2 .elementor-accordion-icon i{color:#E0A526}'
    '.aim2 .elementor-button{border-radius:6px;padding:15px 28px;background:#1E3A8A;color:#fff}'
    '.aim2 .elementor-button:hover{background:#152C6B;color:#fff}'
    '.aim2 .aim2-gold .elementor-button{background:#E0A526;color:#14182B}'
    '.aim2 .aim2-gold .elementor-button:hover{background:#fff;color:#14182B}'
    '.aim2 .aim2-ghost .elementor-button{background:transparent;color:#fff;box-shadow:inset 0 0 0 1px #fff}'
    '.aim2 .aim2-ghost .elementor-button:hover{background:#fff;color:#14182B}'
    '.aim2 .aim2-inline{width:auto;display:inline-block;margin-right:12px;margin-bottom:10px}'
    '.aim2-card>.elementor-widget-wrap{background:#fff;border-radius:10px;box-shadow:0 10px 30px rgba(15,31,77,.08);overflow:hidden;align-content:flex-start}'
    '.aim2 .aim2-card{padding:0 12px 24px}'
    '.aim2-card .elementor-widget:not(.elementor-widget-image){padding:0 24px}'
    '.aim2-card .elementor-widget-heading:first-of-type{margin-top:0}'
    '.aim2-card .elementor-widget-button{margin-top:auto;padding-bottom:24px!important}'
    '.aim2-card h3.elementor-heading-title{margin-top:18px}'
    '.aim2-svc>.elementor-widget-wrap{padding:26px 22px!important;text-align:center}'
    '.aim2-svc .elementor-icon{color:#1E3A8A;font-size:30px}'
    '.aim2-veh-img{padding:20px 20px 0!important}'
    '.aim2-veh-img img{height:200px!important;width:100%;object-fit:contain;background:#F7F5F0;border-radius:8px}'
    '.aim2-card-img img{height:220px!important;width:100%;object-fit:cover}'
    '.aim2-card .elementor-icon-list-icon i{color:#1E3A8A}'
    '.aim2-why .elementor-icon-list-icon i{color:#E0A526;font-size:18px}.aim2-why .elementor-icon-list-icon svg{fill:#E0A526}'
    '.aim2-why .elementor-icon-list-item{padding:6px 0}'
    '.aim2-badge{position:absolute!important;top:14px;left:14px;width:auto!important;padding:0!important;z-index:2}'
    '.aim2-badge .elementor-heading-title{white-space:nowrap;background:#E0A526;color:#0F1F4D!important;border-radius:20px;padding:6px 12px}'
    '.aim2-price .elementor-heading-title{font-family:Inter,sans-serif;font-size:13px;color:#4B5068;letter-spacing:0}'
    '.aim2-price strong{font-size:22px;color:#1E3A8A}'
    '.aim2 .aim2-link .elementor-button{background:transparent;color:#1E3A8A;padding:0}'
    '.aim2 .aim2-link .elementor-button:hover{background:transparent;color:#1E3A8A;text-decoration:underline}'
    '.aim2-num{text-align:center}.aim2-num .elementor-heading-title{display:inline-block;background:#E0A526;color:#0F1F4D;border-radius:50%;width:56px;height:56px;line-height:56px}'
    '.aim2-step>.elementor-widget-wrap{text-align:center;padding:10px 20px}'
    '.aim2-round img{border-radius:14px;height:480px!important;width:100%;object-fit:cover}'
    '.aim2-hero{min-height:90vh;display:flex;align-items:center;padding:110px 20px;position:relative}'
    '.aim2-hero .elementor-heading-title,.aim2-hero .elementor-widget-text-editor{color:#fff}'
    '.aim2-hero .aim2-lead{color:#E3E8F5}'
    '.aim2-cta{background:linear-gradient(120deg,#0F1F4D,#1E3A8A);padding:70px 20px}'
    '.aim2-cta .elementor-heading-title{color:#fff}.aim2-cta .elementor-widget-text-editor{color:#C9D2EA}'
    '.aim2-cta a{color:#fff}'
    '.aim2 .elementor-accordion-item{border-color:#E3E6EF;margin-bottom:10px;border-radius:8px;overflow:hidden}'
    '.aim2 .elementor-tab-title{background:#F7F5F0;padding:20px 24px}'
    '.aim2 .elementor-tab-title .elementor-accordion-icon{color:#E0A526}'
    '.aim2 .elementor-tab-title.elementor-active a{color:#1E3A8A}'
    '.aim2-k.aim2-badge .elementor-heading-title{color:#0F1F4D}'
    '@media(max-width:1024px){.aim2-hero{min-height:auto}}'
    '@media(max-width:767px){.aim2{padding:60px 16px}.aim2-round img{height:260px!important}.aim2-cta .elementor-column{text-align:left}}'
    '</style>'))


def build(lang):
    t = B.T[lang]
    wa = B.WA + t['wa_text']
    out = []
    # Hero: video background with overlay (kept as Elementor settings so it stays editable)
    out.append(sec([col([
        h(t['eyebrow'], 'p', 'aim2-k', 0),
        h(t['h1'], 'h1', '', 150),
        p(t['lead'], 'aim2-lead', 300),
        btn(t['quote'], wa, 'aim2-gold aim2-inline', 'fab fa-whatsapp', 450),
        btn(t['fleet_btn'], '#fleet', 'aim2-ghost aim2-inline', None, 450),
        h('<span style=\'opacity:.8\'>%s :</span> <a href=\'tel:+212662667975\'><strong>%s</strong></a> · 7/7' % (t['call'], B.PHONE),
          'p', 'aim2-call', 550),
    ], 70), col([], 30)], 'aim2-hero',
        background_background='video', background_video_link=B.UP + '2026/05/tourisme-voyage-travelmorocco-touristbus-marrakechmedina.mp4',
        background_play_on_mobile='yes', background_video_fallback={'url': B.media(1894), 'id': ''},
        background_overlay_background='gradient', background_overlay_color='rgba(15,31,77,0.92)',
        background_overlay_color_b='rgba(15,31,77,0.35)', background_overlay_gradient_angle={'unit': 'deg', 'size': 90}))
    # Services
    out.append(sec([col(head(t['services_k'], t['services_h'], t['services_s']))], 'aim2-cream aim2-narrow aim2-top aim2-center'))
    out.append(sec([col([w('icon-box', {'selected_icon': {'value': i, 'library': 'fa-solid'}, 'title_text': a, 'description_text': d,
                                        'title_size': 'h3'}, anim=k * 80)], 20, 'aim2-card aim2-svc')
                    for k, (i, a, d) in enumerate(t['services'])], 'aim2-cream aim2-tight'))
    # Fleet
    out.append(sec([col(head(t['fleet_k'], t['fleet_h'], t['fleet_s']))], 'aim2-navy aim2-narrow aim2-top aim2-center', 'fleet'))
    out.append(sec([col([
        img(B.UP + im, name, 'aim2-veh-img'),
        h(name, 'h3'),
        ilist([(pax, 'fas fa-user-friends'), (bags, 'fas fa-suitcase-rolling'), (t['ideal'] + ': ' + ideal, 'fas fa-check-circle')], ''),
        btn(t['vq'], wa + name.replace(' ', '%20')),
    ], 25, 'aim2-card', _animation='fadeInUp', _animation_delay=k * 100) for k, (im, name, pax, bags, ideal) in enumerate(t['fleet'])],
        'aim2-navy aim2-tight aim2-top'))
    out.append(sec([col([btn(t['fleet_all'], B.page_link(t['fleet_page']), 'aim2-ghost')], 100, 'aim2-center')], 'aim2-navy aim2-tight'))
    # Excursions with our vehicles
    out.append(sec([col(head(t['exc_k'], t['exc_h'], t['exc_s']))], 'aim2-cream aim2-narrow aim2-top aim2-center'))
    cards = []
    for k, (pid, mid, title, dur, price) in enumerate(t['trips']):
        url = B.page_link(pid)
        badge = t['badge_multi'] if dur.endswith('d') else t['badge_day']
        cards.append(col([
            img(B.media(mid), title, 'aim2-card-img', url),
            h(badge + ' · ' + t['days'][dur], 'p', 'aim2-k aim2-badge'),
            h(title, 'h3', link=url),
            h('%s <strong>€%d</strong> %s' % (t['from_'], price + B.PRICE_UPLIFT, t['per']), 'p', 'aim2-price'),
            btn(t['details'] + ' →', url, 'aim2-link'),
        ], 33, 'aim2-card', _animation='fadeInUp', _animation_delay=(k % 3) * 100))
    out.append(sec(cards[:3], 'aim2-cream aim2-tight aim2-nb'))
    out.append(sec(cards[3:], 'aim2-cream aim2-tight'))
    # Why us
    out.append(sec([
        col([img(B.media(1891), 'Aït Ben Haddou', 'aim2-round')], 50, padding={'unit': 'px', 'top': '0', 'right': '30', 'bottom': '20', 'left': '0'}),
        col([h(t['why_k'], 'p', 'aim2-k'), h(t['why_h']), p(t['why_p']), ilist([(x, '') for x in t['why']], 'fas fa-check-circle'),
             btn(t['quote'], wa, 'aim2-btn', 'fab fa-whatsapp')], 50, 'aim2-why', content_position='center'),
    ], 'aim2-white'))
    # Steps
    out.append(sec([col(head(t['steps_k'], t['steps_h']))], 'aim2-cream aim2-narrow aim2-top aim2-center'))
    out.append(sec([col([h(n, 'div', 'aim2-num'), h(a, 'h3', 'aim2-center'), p(d, 'aim2-center')], 33, 'aim2-step',
                        _animation='fadeInUp', _animation_delay=k * 120) for k, (n, a, d) in enumerate(t['steps'])], 'aim2-cream aim2-tight'))
    # FAQ
    out.append(sec([col(head(t['faq_k'], t['faq_h']) + [w('accordion', {
        'tabs': [{'_id': eid(), 'tab_title': q, 'tab_content': '<p>%s</p>' % a} for q, a in t['faq']],
        'selected_icon': {'value': 'fas fa-plus', 'library': 'fa-solid'},
        'selected_active_icon': {'value': 'fas fa-minus', 'library': 'fa-solid'}})])], 'aim2-white aim2-narrow aim2-center'))
    # Contact band + stylesheet
    out.append(sec([
        col([h(t['cta_h']), p(t['cta_p'])], 55, content_position='center'),
        col([btn(t['quote'], wa, 'aim2-gold aim2-inline', 'fab fa-whatsapp'), btn(t['email_btn'], 'mailto:' + B.EMAIL, 'aim2-ghost aim2-inline'),
             h('<a href=\'tel:+212662667975\'>%s</a> · <a href=\'mailto:%s\'>%s</a>' % (B.PHONE, B.EMAIL, B.EMAIL), 'p', 'aim2-price'),
             w('html', {'html': STYLE})], 45, content_position='center'),
    ], 'aim2-cta', 'contact'))
    return out


if __name__ == '__main__':
    for lang in ('en', 'fr'):
        data = json.dumps(build(lang), ensure_ascii=False, separators=(',', ':'))
        assert '\\' not in data and '"' not in json.dumps(STYLE)[1:-1].replace('\\"', '')
        with open(os.path.join(HERE, 'home-%s-lite.json' % lang), 'w') as f:
            f.write(data)
        print(lang, len(data), 'bytes')
