"""Clean rebuild of the Atlas Family Adventure homepage (page 8276), keeping the owner's own text, photos,
the WP Travel Engine trips slider and the Tripadvisor reviews shortcode."""
import json, hashlib
from brand import EXTRA, PEAKS
U = 'https://atlasfamilyadventure.com/wp-content/uploads/2026/09/'
S = 'https://atlasfamilyadventure.com/index.php'
WA = 'https://wa.me/212703501612?text=Hello%20Atlas%20Family%20Adventure%2C%20I%20would%20like%20information%20about%20a%20trek.'
TREKS = S + '/trip/'
SAHARA = S + '/sahara-desert-tours/'
CONTACT = S + '/contact/'
eid = lambda *k: hashlib.md5('|'.join(map(str, k)).encode()).hexdigest()[:7]

CSS = ("<style>.afh{--o:#ff4911;--od:#d93a06;--ink:#1c1c1c;--mut:#5c5c5c;--sand:#faf3ea;color:var(--ink);font-size:16px;line-height:1.7}"
".afh *{box-sizing:border-box}.afh h1,.afh h2,.afh h3{margin:0;line-height:1.15;color:var(--ink)}.afh p{margin:0 0 14px}"
".afh-w{max-width:1200px;margin:0 auto;padding:0 20px}.afh-sec{padding:90px 0}.afh-sand{background:var(--sand)}"
".afh-k{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--o);margin-bottom:12px}"
".afh a.afh-b{display:inline-flex;align-items:center;justify-content:center;padding:14px 26px;border-radius:999px;font-weight:700;text-decoration:none;border:2px solid var(--o);transition:all .2s;line-height:1.2}"
".afh a.afh-b--p{background:var(--o);color:#fff}.afh a.afh-b--p:hover{background:var(--od);border-color:var(--od)}"
".afh a.afh-b--g{border-color:rgba(255,255,255,.8);color:#fff;background:rgba(255,255,255,.08)}.afh a.afh-b--g:hover{background:#fff;color:var(--ink)}"
".afh a.afh-b--l{color:var(--o);background:#fff}.afh a.afh-b--l:hover{background:var(--o);color:#fff}.afh-btns{display:flex;flex-wrap:wrap;gap:12px}"
".afh-hero{position:relative;min-height:88vh;display:flex;align-items:center;background:#3a2a1c center/cover;color:#fff;padding:120px 0}"
".afh-hero:before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,10,5,.78),rgba(15,10,5,.35))}"
".afh-hero .afh-w{position:relative;width:100%}.afh-hero .afh-k{color:#ffd2bd}"
".afh-hero h1{color:#fff;font-size:clamp(38px,5.6vw,72px);max-width:820px;margin-bottom:20px}"
".afh-hero p{font-size:clamp(17px,1.6vw,20px);max-width:620px;color:rgba(255,255,255,.92);margin-bottom:30px}"
".afh-split{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}.afh-split h2{font-size:clamp(30px,3.4vw,44px);margin-bottom:20px}"
".afh-split p{color:var(--mut);font-size:16.5px}.afh-pics{display:grid;grid-template-columns:1fr 1fr;gap:14px}"
".afh-pics span{display:block;border-radius:18px;background:#c9a77c center/cover;min-height:440px}.afh-pics span+span{margin-top:60px}"
".afh-head{text-align:center;max-width:700px;margin:0 auto 40px}.afh-head h2{font-size:clamp(28px,3vw,40px);margin-bottom:10px}.afh-head p{color:var(--mut);margin:0}"
".afh-reg{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}"
".afh-reg a{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:380px;border-radius:18px;overflow:hidden;padding:26px;background:#3a2a1c center/cover;color:#fff;text-decoration:none;transition:transform .25s}"
".afh-reg a:before{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.8))}.afh-reg a>*{position:relative}"
".afh-reg a:hover{transform:translateY(-4px)}.afh-reg h3{color:#fff;font-size:26px;margin-bottom:6px}.afh-reg p{margin:0;color:rgba(255,255,255,.88);font-size:15px}"
".afh-reg i{font-style:normal;font-weight:700;color:#ffd2bd;margin-top:10px;font-size:15px}"
".afh-why{position:relative;background:#2a2017 center/cover;color:#fff;padding:100px 0}.afh-why:before{content:'';position:absolute;inset:0;background:rgba(20,14,8,.78)}"
".afh-why .afh-w{position:relative}.afh-why h2{color:#fff}.afh-why .afh-head p{color:rgba(255,255,255,.8)}"
".afh-why ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:18px}"
".afh-why li{margin:0;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);border-radius:16px;padding:24px 24px 24px 64px;position:relative;font-size:16.5px}"
".afh-why li:before{content:'';position:absolute;left:22px;top:24px;width:26px;height:26px;border-radius:50%;background:var(--o) url(data:image/svg+xml,%3Csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20viewBox=%270%200%2024%2024%27%20fill=%27none%27%20stroke=%27%23fff%27%20stroke-width=%273%27%20stroke-linecap=%27round%27%20stroke-linejoin=%27round%27%3E%3Cpath%20d=%27M5%2012l5%205L20%207%27/%3E%3C/svg%3E) center/14px no-repeat}"
".afh-more{text-align:center;max-width:760px;margin:0 auto}.afh-more h2{font-size:clamp(28px,3vw,40px);margin-bottom:16px}.afh-more p{color:var(--mut);font-size:17px}"
".afh-more .afh-btns{justify-content:center;margin-top:24px}.afh-c{text-align:center;margin-top:30px}"
"@media (max-width:900px){.afh-sec{padding:64px 0}.afh-split,.afh-reg,.afh-why ul{grid-template-columns:1fr}.afh-split{gap:34px}.afh-pics span{min-height:260px}.afh-pics span+span{margin-top:30px}.afh-reg a{min-height:280px}.afh-hero{min-height:auto;padding:100px 0}}"
"</style>")

INTRO = ["Morocco is more than beautiful landscapes. It’s the people you meet, the stories you hear, the meals you share, and the memories you create along the way.",
         "At Atlas Family Adventure, we invite you to discover the Morocco we grew up in. From the High Atlas Mountains to the Sahara Desert, we organize hiking trips and cultural journeys that take you beyond the usual tourist routes.",
         "Whether you’re trekking through remote Amazigh villages, climbing Mount M’Goun, exploring the volcanic landscapes of Jebel Saghro, or spending a night under the stars in the Sahara, every trip is led by local people who know these places by heart.",
         "We work with our families, friends, muleteers, cooks, and drivers to create authentic experiences where you can slow down, enjoy nature, and experience the real Morocco."]
WHY = ['Local guides born and raised in the Atlas Mountains.', 'Small groups and private tailor-made adventures.', 'Authentic trekking and cultural experiences.',
       'Traditional Moroccan meals prepared by our local cook.', 'Responsible tourism that supports local communities.', 'Flexible itineraries designed around your interests.']
REG = [('High Atlas & M’Goun', 'Aït Bougmez, the M’Goun summit (4,071 m), its gorges and the Rose Valley.', U + 'CVJR2258.jpg', TREKS),
       ('Jebel Saghro', 'Volcanic mountains and wide valleys between the Atlas and the desert.', U + 'WhatsApp-Image-2026-09-20-at-11.17.35-7.jpeg', TREKS),
       ('Sahara Desert', 'Dunes, palm groves and remote camps in the Draa Valley.', U + 'IMG_3545.jpeg', SAHARA)]

def top():
    hero = ("<section class='afh-hero' style='background-image:url(%sWhatsApp-Image-2026-09-22-at-04.52.07-scaled.jpeg)'><div class='afh-w'>"
            "<span class='afh-k'>Atlas Family Adventure</span><h1>Discover the Real Morocco, Beyond the Usual Routes</h1>"
            "<p>Hiking trips and cultural journeys from the High Atlas Mountains to the Sahara Desert, led by local people who know these places by heart.</p>"
            "<div class='afh-btns'><a class='afh-b afh-b--p' href='%s'>Our Treks</a><a class='afh-b afh-b--g' href='%s' target='_blank' rel='noopener'>WhatsApp us</a></div></div>" + PEAKS % ('#ffffff', '#ffffff') + "</section><div class='afh-rug'></div>") % (U, TREKS, WA)
    intro = ("<section class='afh-sec'><div class='afh-w afh-split'><div><span class='afh-k'>Atlas Family Adventure</span><h2>Morocco, Beyond the Journey</h2>"
             + ''.join('<p>%s</p>' % p for p in INTRO) +
             "<div class='afh-btns' style='margin-top:20px'><a class='afh-b afh-b--p' href='%s/about/'>About us</a></div></div>"
             "<div class='afh-pics'><span style='background-image:url(%sIMG_3118-scaled.jpeg)'></span><span style='background-image:url(%sIMG_1195-scaled.jpeg)'></span></div></div></section>") % (S, U, U)
    return CSS + EXTRA + "<div class='afh'>" + hero + intro + "<div class='afh-sand' style='padding-top:90px'><div class='afh-w afh-head'><span class='afh-k'>Our treks</span><h2>Trekking adventures in Morocco</h2><p>Mountain and desert treks with our local team.</p></div></div></div>"

def mid():
    btn = "<div class='afh afh-sand'><div class='afh-c' style='margin-top:0;padding:10px 0 90px'><a class='afh-b afh-b--p' href='%s'>View all treks</a></div></div>" % TREKS
    return btn

def rest():
    reg = ("<section class='afh-sec'><div class='afh-w'><div class='afh-head'><span class='afh-k'>Where we trek</span><h2>From the mountains to the desert</h2></div><div class='afh-reg'>"
           + ''.join("<a href='%s' style='background-image:url(%s)'><h3>%s</h3><p>%s</p><i>Discover →</i></a>" % (u, img, t, d) for t, d, img, u in REG) + '</div></div></section>')
    why = ("<section class='afh-why' style='background-image:url(%sIMG_1195-scaled.jpeg)'><div class='afh-w'><div class='afh-head'><span class='afh-k'>Why us</span>"
           "<h2>Why Travel With Atlas Family Adventure?</h2></div><ul>" + ''.join('<li>%s</li>' % w for w in WHY) + '</ul></div></section>') % U
    more = ("<section class='afh-sec'><div class='afh-w afh-more'><span class='afh-k'>More than a holiday</span><h2>We look forward to welcoming you to our home</h2>"
            "<p>For us, every trek is a chance to meet new people, exchange cultures, and create lasting memories together. We don’t just guide you through Morocco, we share our way of life with you.</p>"
            "<p>Our goal is simple: to make you feel welcome and to share the places we are proud to call home.</p><p class='afh-sign'>Mehdi &amp; the Atlas family</p>"
            "<div class='afh-btns'><a class='afh-b afh-b--p' href='%s'>Contact us</a><a class='afh-b afh-b--l' href='%s' target='_blank' rel='noopener'>WhatsApp</a></div></div></section>") % (CONTACT, WA)
    return "<div class='afh'>" + reg + why + more + "<div class='afh-rug' style='margin-bottom:60px'></div><div class='afh-head' style='margin-bottom:10px'><span class='afh-k'>Testimonials</span><h2>Words From Our Guests</h2></div></div>"

def container(cid, els, extra=None):
    s = {'content_width': 'full', 'flex_direction': 'column', 'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0'},
         'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '0', 'left': '0', 'isLinked': True}}
    if extra: s.update(extra)
    return {'id': cid, 'elType': 'container', 'settings': s, 'elements': els, 'isInner': False}
html = lambda i, c: {'id': i, 'elType': 'widget', 'settings': {'html': c}, 'elements': [], 'widgetType': 'html'}

def build():
    k = 'afhome'
    trips = {'id': '469e833', 'elType': 'widget', 'widgetType': 'wptravelengine-trips', 'elements': [],
             'settings': {'layout': 'slider', 'cardlayout': '3', 'showDescription': '', 'durationType': 'both', 'showReviews': 'yes', 'showViewMoreButton': 'yes',
                          'viewMoreButtonText': 'View Details', 'showFeaturedRibbon': '', 'showDiscount': '', 'slider.arrow': 'yes', 'slider.pagination': '',
                          'slider.slidesPerViewDesktop_tablet': 2, 'slider.slidesPerViewDesktop_mobile': 1,
                          'button_border_radius': {'unit': 'px', 'top': '10', 'right': '10', 'bottom': '10', 'left': '10', 'isLinked': True}, 'button_bg_hover_color': '#d93a06'}}
    rev = {'id': eid(k, 'sc'), 'elType': 'widget', 'settings': {'shortcode': '[trustindex no-registration=tripadvisor]'}, 'elements': [], 'widgetType': 'shortcode'}
    return [container(eid(k, 'c1'), [html(eid(k, 'w1'), top())]),
            container(eid(k, 'c2'), [trips], {'content_width': 'boxed', 'boxed_width': {'unit': 'px', 'size': 1200, 'sizes': []}, 'background_background': 'classic', 'background_color': '#faf3ea',
                                             'padding': {'unit': 'px', 'top': '0', 'right': '20', 'bottom': '20', 'left': '20', 'isLinked': False}}),
            container(eid(k, 'c3'), [html(eid(k, 'w3'), mid()), html(eid(k, 'w4'), rest()), rev],
                      {'padding': {'unit': 'px', 'top': '0', 'right': '0', 'bottom': '80', 'left': '0', 'isLinked': False}})]

if __name__ == '__main__':
    ed = build()
    s = json.dumps(ed, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s, s[s.index('\\') - 80:s.index('\\') + 20]
    open('home_elementor.json', 'w').write(s)
    body = top() + "<div style='max-width:1200px;margin:0 auto;height:420px;background:#faf3ea;display:grid;place-items:center'>[trips slider]</div>" + mid() + rest() + "<div style='height:200px;background:#eee;max-width:1200px;margin:0 auto'>[reviews]</div>"
    open('home_preview.html', 'w').write("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><body style='margin:0;font-family:system-ui'>" + body)
    print(len(s))
