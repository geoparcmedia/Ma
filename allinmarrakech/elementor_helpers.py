"""Elementor JSON helpers (sections, columns and native widgets), shared by the page builders."""
import hashlib

INK, MUTED, BG, CARD, BTN, SAGE, CREAM, ACCENT = '#14182B', '#4B5068', '#F7F5F0', '#FFFFFF', '#1E3A8A', '#E8ECF7', '#FBEFD3', '#E0A526'
FONT = 'Inter'
HEAD_FONT = 'Montserrat'
WIDTH = 1180
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
        'button_background_hover_color': BTN if outline else '#152C6B',
        'hover_color': '#FFFFFF',
        'border_radius': box(6, 6, 6, 6),
        'text_padding': box(15, 28, 15, 28),
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


