"""Sahara Desert Tours (8776) as an Elementor page: full width (no theme sidebar) + other treks grid."""
import json, re
import sahara
from home import container, html, eid

def build():
    full = sahara.page().replace('\n', '')
    css, body = full.split('</style>', 1)
    css += '.afs{max-width:1200px;margin:0 auto;padding:60px 20px 0}.afs-more{max-width:1200px;margin:0 auto;padding:0 20px}</style>'
    cta_i = body.index("<section class='afs-cta'")
    top, cta = body[:cta_i] + '</div>', "<div class='afs' style='padding-top:30px;padding-bottom:70px'>" + body[cta_i:]
    head = ("<div class='afs-more'><div class='afs-h' style='margin-top:10px'><span class='afs-k'>More adventures</span><h2>More treks with Atlas Family</h2>"
            "<p>Explore all our treks in the High Atlas, M’Goun, Jebel Saghro and the Sahara.</p></div></div>")
    trips = {'id': eid('sah', 'trips'), 'elType': 'widget', 'widgetType': 'wptravelengine-trips', 'elements': [],
             'settings': {'layout': 'grid', 'cardlayout': '3', 'showDescription': '', 'durationType': 'both', 'showReviews': 'yes', 'showViewMoreButton': 'yes',
                          'viewMoreButtonText': 'View Details', 'showFeaturedRibbon': '', 'showDiscount': '',
                          'button_border_radius': {'unit': 'px', 'top': '10', 'right': '10', 'bottom': '10', 'left': '10', 'isLinked': True}, 'button_bg_hover_color': '#d93a06'}}
    return [container(eid('sah', 'c1'), [html(eid('sah', 'w1'), css + top + head)]),
            container(eid('sah', 'c2'), [trips], {'content_width': 'boxed', 'boxed_width': {'unit': 'px', 'size': 1200, 'sizes': []},
                                                 'padding': {'unit': 'px', 'top': '0', 'right': '20', 'bottom': '0', 'left': '20', 'isLinked': False}}),
            container(eid('sah', 'c3'), [html(eid('sah', 'w3'), cta)])]

if __name__ == '__main__':
    s = json.dumps(build(), ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s
    open('sahara_elementor.json', 'w').write(s)
    print(len(s))
