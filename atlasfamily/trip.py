"""Single trek template (WPTE Single Trip Template, posts 24 & 4394).

Removes the 700px photo carousel and empty sections, recolours to the brand,
adds a compact title band and a WhatsApp help box under the booking card.
"""
import json

SRC = 'backups/trip-template4394-elementor.json'
WA = ('https://wa.me/212703501612?text=Hello%20Atlas%20Family%20Adventure%2C%20'
      'I%20would%20like%20information%20about%20this%20trek.')

DROP_WIDGETS = {'wte-trip-ratings', 'wte-map', 'wte-faqs', 'wte-fixed-starting-date',
                'wte-trip-review-form', 'wte-trip-reviews'}
DROP_HEADINGS = {'Official Trek Map', 'Our Customer Reviews'}

CSS = (
    "<style>"
    ".single-trip .breadcumb-wrapper,.single-trip .vs-breadcumb,.single-trip .breadcrumb-wrapper{display:none!important}"
    ".aft-band{background:#faf3ea;border-bottom:1px solid #eadcc8;font-family:Poppins,system-ui,sans-serif}"
    ".aft-band .in{max-width:1240px;margin:0 auto;padding:22px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}"
    ".aft-band .k{font-family:Caveat,cursive;font-size:24px;color:#b8432b;line-height:1}"
    ".aft-band .k:before{content:'ⵣ';font-family:system-ui,sans-serif;font-size:.75em;margin-right:8px}"
    ".aft-band a.back{color:#2a2017;font-weight:600;font-size:14.5px;text-decoration:none;border:1px solid #e3d3bd;border-radius:999px;padding:9px 18px;background:#fff}"
    ".aft-band a.back:hover{color:#fff;background:#b8432b;border-color:#b8432b}"
    ".aft-wrap{font-family:Poppins,system-ui,sans-serif;color:#4a3f35}"
    ".aft-wrap h1,.aft-wrap h2,.aft-wrap h3,.aft-wrap h4,.aft-wrap .elementor-heading-title{font-family:Poppins,system-ui,sans-serif!important;color:#2a2017!important;letter-spacing:-.01em}"
    ".aft-wrap h1{font-size:clamp(28px,3.4vw,40px)!important;line-height:1.2!important;font-weight:700!important;margin:0!important}"
    ".aft-wrap .elementor-heading-title{font-size:26px!important;font-weight:700!important}"
    ".aft-wrap a{color:#b8432b}"
    ".aft-wrap [style*='1A84EE'],.aft-wrap [style*='1a84ee']{background-color:#b8432b!important;border-color:#b8432b!important}"
    ".aft-wrap i,.aft-wrap svg{color:#b8432b}"
    ".aft-wrap img{max-width:100%;height:auto}"
    ".aft-wrap .elementor-divider-separator{border-color:#eadcc8!important}"
    ".aft-main{border-radius:18px!important;border-color:#eadcc8!important;box-shadow:0 20px 50px -35px rgba(42,32,23,.35)}"
    ".aft-side .wpte-booking-area,.aft-side [class*=booking]{border-radius:18px!important}"
    ".aft-help{margin-top:22px;background:#2a2017;color:rgba(255,255,255,.82);border-radius:18px;padding:24px;font-family:Poppins,system-ui,sans-serif;font-size:14.5px;line-height:1.6}"
    ".aft-help .k{font-family:Caveat,cursive;font-size:26px;color:#f2c9a0;line-height:1;margin:0 0 8px}"
    ".aft-help b{color:#fff;display:block;font-size:17px;margin-bottom:6px}"
    ".aft-help a.afg-btn{display:flex;justify-content:center;margin-top:16px;background:#b8432b;color:#fff;padding:12px 18px;border-radius:999px;font-weight:600;text-decoration:none}"
    ".aft-help a.afg-btn:hover{background:#fff;color:#2a2017}"
    ".aft-help a.mail{color:#f2c9a0}"
    "@media (min-width:1025px){.aft-side{position:sticky!important;top:20px;align-self:flex-start}}"
    "@media (max-width:1024px){.aft-cols{flex-direction:column!important}.aft-cols>.e-con{width:100%!important;--width:100%!important}}"
    "@media (max-width:640px){.aft-main{--padding-top:18px;--padding-right:16px;--padding-bottom:18px;--padding-left:16px}}"
    "</style>"
)

BAND = (
    CSS +
    "<div class='aft-band'><div class='in'><span class='k'>Trek with a local family</span>"
    "<a class='back' href='https://atlasfamilyadventure.com/index.php/trip/'>← All treks</a></div></div>"
)

HELP = (
    "<div class='aft-help'><p class='k'>Need help choosing?</p>"
    "<b>Talk to Mehdi directly</b>"
    "Private departures on the dates you choose, small groups and local guides from the Atlas."
    "<a class='afg-btn' href='" + WA + "' target='_blank' rel='noopener'>Ask on WhatsApp</a>"
    "<p style='margin:12px 0 0;text-align:center'><a class='mail' href='mailto:aelmahdizaki@gmail.com'>aelmahdizaki@gmail.com</a></p></div>"
)


def recolor(o):
    if isinstance(o, dict):
        return {k: recolor(v) for k, v in o.items()}
    if isinstance(o, list):
        return [recolor(v) for v in o]
    if isinstance(o, str):
        if o.upper() == '#1A84EE':
            return '#b8432b'
        if o == 'Amiri':
            return 'Poppins'
        if o == '#00C004':
            return '#b8432b'
    return o


def keep(el):
    if el.get('widgetType') in DROP_WIDGETS:
        return False
    if el.get('widgetType') == 'heading' and el['settings'].get('title') in DROP_HEADINGS:
        return False
    return True


def clean(els):
    out = []
    for el in els:
        if not keep(el):
            continue
        el['elements'] = clean(el.get('elements', []))
        # drop containers left empty
        if el['elType'] == 'container' and not el['elements']:
            continue
        out.append(el)
    # collapse consecutive / trailing dividers
    res = []
    for el in out:
        if el.get('widgetType') == 'divider' and (not res or res[-1].get('widgetType') == 'divider'):
            continue
        res.append(el)
    while res and res[-1].get('widgetType') == 'divider':
        res.pop()
    return res


def build():
    tpl = json.load(open(SRC))
    tpl = recolor(tpl)
    # 1) replace the absolute breadcrumb overlay + 700px carousel with a compact band
    hero = tpl[0]
    hero['elements'] = [{'id': 'af7b001', 'elType': 'widget', 'widgetType': 'html',
                         'settings': {'html': BAND}, 'elements': []}]
    # 2) main row
    row = tpl[1]
    row['settings']['css_classes'] = 'aft-wrap aft-cols'
    row['settings']['boxed_width'] = {'unit': 'px', 'size': 1240, 'sizes': []}
    row['settings']['padding'] = {'unit': 'px', 'top': '40', 'right': '20', 'bottom': '60', 'left': '20', 'isLinked': False}
    main, side = row['elements']
    main['settings']['css_classes'] = 'aft-main'
    main['settings']['border_radius'] = {'unit': 'px', 'top': '18', 'right': '18', 'bottom': '18', 'left': '18', 'isLinked': True}
    main['settings']['border_color'] = '#EADCC8'
    main['settings']['padding'] = {'unit': 'px', 'top': '32', 'right': '32', 'bottom': '32', 'left': '32', 'isLinked': True}
    main['elements'] = clean(main['elements'])
    # title block: duration badge no longer absolute over the title
    for el in main['elements']:
        if el['elType'] == 'container' and any(e.get('widgetType') == 'wte-title' for e in el['elements']):
            el['settings']['padding'] = {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}
            el['settings']['flex_direction'] = 'column'
            el['settings']['flex_align_items'] = 'flex-start'
            for e in el['elements']:
                if e.get('widgetType') == 'wte-duration':
                    for k in ('_position', '_offset_orientation_h', '_offset_y'):
                        e['settings'].pop(k, None)
                    e['settings']['duration_bg_color'] = '#b8432b'
                if e.get('widgetType') == 'wte-title':
                    e['settings']['title_color'] = '#2a2017'
                    e['settings']['title_typography_font_weight'] = '700'
    side['settings']['css_classes'] = 'aft-side'
    side['elements'].append({'id': 'af7b002', 'elType': 'widget', 'widgetType': 'html',
                             'settings': {'html': HELP}, 'elements': []})
    return tpl


if __name__ == '__main__':
    tpl = build()
    s = json.dumps(tpl, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s, 'backslash in JSON'
    assert '"' not in BAND + HELP
    open('trip_elementor.json', 'w').write(s)
    print(len(s))
    for el in tpl[1]['elements'][0]['elements']:
        print(' ', el['elType'], el.get('widgetType') or '', (el['settings'].get('title') or '')[:40],
              [e.get('widgetType') or e['elType'] for e in el.get('elements', [])])
