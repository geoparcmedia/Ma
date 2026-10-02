"""Homepage (479), header (308) and footer (316) in the Morocco Sky Travel design system."""
import json
from tours import TOURS, U
from build import (SITE, WA, PHONE, EMAIL, esc, eid, card, container, w_html, w_sc, book_container,
                   book_head, ldscript, nobs, wa_link)
from pages import WHY

LOGO = U + '2024/10/LOGO-COLEU.png'
LOGO_W = U + '2024/10/BLN.png'
BY = {t['id']: t for t in TOURS}
FONTS = ("<link rel='preconnect' href='https://fonts.googleapis.com'><link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>"
         "<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500..800;1,6..96,500..700&family=Inter:wght@400;500;600;700&display=swap'>")
NAV = [('Home', '/'), ('Tours', '/our-destinations/'), ('Day Trips', '/destinations-copy/'), ('About', '/elementor-366/'), ('Contact', '/contact-us/')]
SOCIAL = [('Facebook', 'https://m.facebook.com/p/Moroccoskytravel-100063598419420/'),
          ('Instagram', 'https://www.instagram.com/moroccoskytravel/'),
          ('Snapchat', 'https://snapchat.com/t/V3WuOytE')]

MEGA = [('Desert tours', (2805, 2771, 2789, 2847, 2800)), ('Grand tours', (2814, 2784, 2839, 2834, 2829)), ('Day trips from Marrakech', (2947, 2943, 2934, 2926, 2960))]
DUNE = ("<svg class='%s' viewBox='0 0 1440 90' preserveAspectRatio='none' aria-hidden='true'><path d='M0 62C160 30 300 18 470 40s300 52 480 30 330-60 490-38V90H0z' fill='%s'/>"
        "<path d='M0 78c200-26 380-30 560-12s360 30 520 8 260-28 360-20V90H0z' fill='%s' opacity='.55'/></svg>")
WA_HI = 'Hello Morocco Sky Travel, I would like some information about a trip.'

def header():
    mega = ''.join("<div><h4>%s</h4>%s</div>" % (n, ''.join("<a href='%s/%s/'>%s</a>" % (SITE, BY[i]['url'], esc(BY[i]['card'])) for i in ids)) for n, ids in MEGA)
    mega += ("<a class='mh-feat' href='%s/book/' style='background-image:url(%s)'><span>Can’t decide?</span><b>Let us design your trip</b><i>Free quote →</i></a>") % (SITE, BY[2847]['img'])
    soc = ''.join("<a href='%s' target='_blank' rel='noopener' aria-label='%s'><i class='i-%s'></i></a>" % (u, n, n[:2].lower()) for n, u in SOCIAL)
    js = ("<script>(function(){var h=document.querySelector('.mh');if(!h)return;var p=location.pathname;"
          "h.querySelectorAll('.mh-nav>a,.mh-nav .mh-dt').forEach(function(a){var q=new URL(a.href).pathname;if(q===p||(q!=='/'&&p.indexOf(q)===0))a.classList.add('on')});"
          "var b=h.querySelector('.mh-burger'),n=h.querySelector('.mh-nav');b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false')});"
          "var x=h.querySelector('.mh-x'),d=h.querySelector('.mh-dd');x.addEventListener('click',function(){var o=d.classList.toggle('open');x.setAttribute('aria-expanded',o?'true':'false')});"
          "var s=function(){h.classList.toggle('mh-s',window.scrollY>30)};s();window.addEventListener('scroll',s,{passive:true})})()</script>")
    return (FONTS + "<div class='mst mh'><div class='mh-top'><div class='mh-w'><div class='mh-tl'>"
            "<a href='tel:+212667307641'><i class='i-phone'></i>%s</a><a href='mailto:%s'><i class='i-mail'></i>%s</a><span><i class='i-pin'></i>Based in Fes · Private tours across Morocco</span></div>"
            "<div class='mh-soc'>%s</div></div></div>"
            "<div class='mh-bar'><div class='mh-w'><a class='mh-logo' href='%s/' aria-label='Morocco Sky Travel home'><img src='%s' alt='Morocco Sky Travel' height='58'></a>"
            "<nav class='mh-nav' aria-label='Main menu'><a href='%s/'>Home</a>"
            "<div class='mh-dd'><a class='mh-dt' href='%s/our-destinations/'>Tours</a><button type='button' class='mh-x' aria-label='Show tours' aria-expanded='false'></button><div class='mh-mega'>%s</div></div>"
            "<a href='%s/destinations-copy/'>Day Trips</a><a href='%s/elementor-366/'>About</a><a href='%s/contact-us/'>Contact</a>"
            "<a class='mh-m mst-btn mst-btn--gold' href='%s/book/'>Book your trip</a></nav>"
            "<div class='mh-act'><a class='mh-wa' href='%s' target='_blank' rel='noopener' aria-label='WhatsApp us'><i class='i-wa'></i></a>"
            "<a class='mst-btn mst-btn--gold mh-cta' href='%s/book/'>Book your trip</a>"
            "<button type='button' class='mh-burger' aria-label='Menu' aria-expanded='false'><span></span><span></span><span></span></button></div></div></div></div>%s") % (
        PHONE, EMAIL, EMAIL, soc, SITE, LOGO, SITE, SITE, mega, SITE, SITE, SITE, SITE, wa_link(WA_HI), SITE, js)

def footer():
    col = lambda ids: ''.join("<li><a href='%s/%s/'>%s</a></li>" % (SITE, BY[i]['url'], esc(BY[i]['card'])) for i in ids)
    soc = ''.join("<a href='%s' target='_blank' rel='noopener' aria-label='%s'><i class='i-%s'></i></a>" % (u, n, n[:2].lower()) for n, u in SOCIAL)
    return ("<footer class='mst mf'>" + DUNE % ('mf-dune', '#2a170b', '#2a170b') +
            "<div class='mst-wrap mf-cta'><div><span class='mst-eyebrow'>Your trip, your way</span><h2>Ready to sleep under the Sahara stars?</h2>"
            "<p>Tell us your dates and wishes. Our family team replies with a free, personal itinerary.</p></div>"
            "<div class='acts'><a class='mst-btn mst-btn--gold' href='%s/book/'>Plan my trip</a><a class='mst-btn mst-btn--wa' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> WhatsApp</a></div></div>"
            "<div class='mst-wrap mf-grid'><div class='mf-brand'><img src='%s' alt='Morocco Sky Travel' height='70' loading='lazy'>"
            "<p>A family-run Moroccan travel company. From the dunes of the Sahara to the medinas of Fes and Marrakech, we create private journeys with heart.</p><div class='mf-soc'>%s</div></div>"
            "<div><h3>Tours</h3><ul>%s<li><a class='mf-all' href='%s/our-destinations/'>All tours →</a></li></ul></div>"
            "<div><h3>Day trips</h3><ul>%s<li><a class='mf-all' href='%s/destinations-copy/'>All day trips →</a></li></ul></div>"
            "<div><h3>Contact us</h3><ul class='mf-ct'><li><a href='%s' target='_blank' rel='noopener'><i class='i-wa'></i><span><small>WhatsApp</small>%s</span></a></li>"
            "<li><a href='tel:+212667307641'><i class='i-phone'></i><span><small>Phone</small>%s</span></a></li>"
            "<li><a href='mailto:%s'><i class='i-mail'></i><span><small>Email</small>%s</span></a></li>"
            "<li><span class='mf-li'><i class='i-pin'></i><span><small>Office</small>Fes, Morocco – Sais</span></span></li></ul></div></div>"
            "<div class='mst-wrap mf-bot'><span>© <span class='mf-y'>2026</span> Morocco Sky Travel. All rights reserved.</span>"
            "<nav aria-label='Footer'><a href='%s/elementor-366/'>About</a><a href='%s/contact-us/'>Contact</a><a href='%s/book/'>Book</a></nav></div></footer>"
            "<script>document.querySelectorAll('.mf-y').forEach(function(e){e.textContent=new Date().getFullYear()})</script>") % (
        SITE, wa_link(WA_HI), LOGO_W, soc, col((2805, 2771, 2847, 2814, 2784, 2829)), SITE, col((2947, 2943, 2934, 2926, 2952)), SITE,
        wa_link(WA_HI), PHONE, PHONE, EMAIL, EMAIL, SITE, SITE, SITE)

SERVICES = [('i-car', 'Private road trips', 'Imperial cities, kasbahs and coastal towns with your own driver, at your pace.', 2805),
            ('i-flag', 'Sahara desert & camels', 'Camel rides over golden dunes and nights in desert camps under a sky full of stars.', 2947),
            ('i-pin', 'Atlas Mountains treks', 'Guided walks through Berber villages and valleys, for first-timers and keen hikers.', 2943)]
TABS = [('Desert adventures', (2805, 2771, 2789, 2847, 2800, 2809)),
        ('Grand tours', (2814, 2784, 2839, 2834, 2829, 2816)),
        ('Day trips', (2947, 2943, 2934, 2926, 2952, 2960))]
DEST = [('Marrakech', 'Red city, souks & palaces', U + '2025/11/pexels-reyyan-505450018-33429795-1-scaled.jpg', '/our-destinations/', 'a'),
        ('Merzouga', 'Sahara dunes & desert camps', U + '2025/11/pexels-vlasceanu-19190946-scaled.jpg', '/4day-trip-to-the-desert/', 'b'),
        ('Fes', 'The oldest medina in the world', U + '2025/11/pexels-artem-yellow-422929671-15188458-1-scaled.jpg', '/our-destinations/', 'c'),
        ('Atlas Mountains', 'Berber villages & mountain trails', None, '/destinations-copy/', 'd')]
STEPS = [('Tell us your dream trip', 'Share your dates, group size and the places you want to see, by WhatsApp or with our form.'),
         ('We design your itinerary', 'We send you a private, day-by-day plan with hotels, driver and a clear personal quote.'),
         ('Enjoy Morocco, stress-free', 'Your driver meets you on arrival and our family team stays one message away for the whole trip.')]
WHY_IC = ['i-pin', 'i-flag', 'i-car', 'i-clock', 'i-flag', 'i-phone']
HERO = U + '2025/11/pexels-taryn-elliott-4253829-scaled.jpg'
ABOUT1 = U + '2024/10/WhatsApp-Image-2024-10-28-at-12.15.31-PM.jpeg'
WA_PLAN = 'Hello Morocco Sky Travel, I would like help planning a trip to Morocco.'

HOME_JS = ("<script>(function(){var r=document.querySelector('.msx');if(!r)return;"
           # tabs
           "r.querySelectorAll('.msx-tabs button').forEach(function(b){b.addEventListener('click',function(){r.querySelectorAll('.msx-tabs button').forEach(function(x){x.setAttribute('aria-selected',x===b?'true':'false')});"
           "r.querySelectorAll('.msx-track').forEach(function(t){t.hidden=t.id!==b.getAttribute('aria-controls');t.scrollLeft=0})})});"
           # arrows
           "r.querySelectorAll('.msx-arr').forEach(function(b){b.addEventListener('click',function(){var t=r.querySelector('.msx-track:not([hidden])');if(!t)return;var c=t.querySelector('.mst-tc');"
           "t.scrollBy({left:(c?c.offsetWidth+22:340)*(b.dataset.d==='1'?1:-1),behavior:'smooth'})})});"
           # reveal + counters
           "var rd=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;"
           "function cnt(el){var n=+el.dataset.n,s=el.dataset.s||'',t0=null;if(rd){el.textContent=n+s;return}function st(ts){if(!t0)t0=ts;var p=Math.min((ts-t0)/1400,1);"
           "el.textContent=Math.round(n*(1-Math.pow(1-p,3)))+s;if(p<1)requestAnimationFrame(st)}requestAnimationFrame(st)}"
           "if(!('IntersectionObserver' in window)||rd){r.querySelectorAll('[data-n]').forEach(cnt);return}"
           "r.classList.add('msx-on');var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;e.target.classList.add('in');"
           "e.target.querySelectorAll('[data-n]').forEach(cnt);io.unobserve(e.target)})},{rootMargin:'0px 0px -8% 0px'});"
           "r.querySelectorAll('.rv').forEach(function(el){io.observe(el)});"
           "setTimeout(function(){r.querySelectorAll('.rv').forEach(function(el){el.classList.add('in')})},4000)})()</script>")

def opt(name, vals):
    return "<label><span>%s</span><select name='%s'>%s</select></label>" % (name[0], name[1], ''.join('<option>%s</option>' % v for v in vals))

def head(eyebrow, title, text=None, cls=''):
    return "<div class='msx-head rv %s'><span class='mst-eyebrow'>%s</span><h2>%s</h2>%s</div>" % (cls, eyebrow, title, '<p>%s</p>' % esc(text) if text else '')

def home_top():
    wa = wa_link(WA_PLAN)
    hero = ("<header class='msx-hero'><div class='msx-hero-bg' style='background-image:url(%s)'></div><div class='mst-wrap msx-hero-in'>"
            "<span class='msx-place'>Marrakech <i></i> Fes <i></i> Merzouga <i></i> Atlas Mountains</span>"
            "<h1>Private Morocco Tours <em>&amp; Sahara Desert Trips</em></h1>"
            "<p class='msx-lead'>Tailor-made journeys through imperial cities, Atlas villages and golden dunes, with your own private driver and a local family team behind every detail.</p>"
            "<div class='mst-hero-ctas'><a class='mst-btn mst-btn--gold' href='%s/our-destinations/'>Explore our tours</a>"
            "<a class='mst-btn mst-btn--ghost' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> Chat on WhatsApp</a></div>"
            "<ul class='msx-trust'><li><i class='i-car'></i>Private driver &amp; 4x4</li><li><i class='i-flag'></i>Hand-picked riads &amp; camps</li>"
            "<li><i class='i-clock'></i>Flexible, tailor-made routes</li><li><i class='i-wa'></i>Free quote, fast reply</li></ul></div>" + DUNE % ('msx-dune', '#fffaf2', '#fffaf2') + "</header>") % (HERO, SITE, wa)
    svc = ("<section class='msx-sec'><div class='mst-wrap msx-intro2'><div class='rv'><span class='mst-eyebrow'>What we offer</span>"
           "<h2>Morocco, the way <em>locals</em> know it</h2><p>We are a family from the desert of Zagora. For over seven years we have been creating private journeys across Morocco, "
           "sharing the places, flavours and people we love, with the comfort and care you expect.</p>"
           "<a class='msx-link' href='%s/elementor-366/'>Meet our family <span>→</span></a></div><ol class='msx-svc'>" +
           ''.join("<li class='rv'><span class='im' style='background-image:url(%s)'></span><div><span class='n'>0%d</span><h3>%s</h3><p>%s</p></div></li>" % (
               BY[tid]['img'], n + 1, esc(a), esc(b)) for n, (i, a, b, tid) in enumerate(SERVICES)) + '</ol></div></section>') % SITE
    tabs = ''.join("<button type='button' role='tab' id='msx-t%d' aria-controls='msx-p%d' aria-selected='%s'>%s</button>" % (n, n, 'true' if n == 0 else 'false', name) for n, (name, ids) in enumerate(TABS))
    tracks = ''.join("<div class='msx-track' role='tabpanel' id='msx-p%d' aria-labelledby='msx-t%d'%s>%s</div>" % (n, n, '' if n == 0 else ' hidden', ''.join(card(BY[i]) for i in ids)) for n, (name, ids) in enumerate(TABS))
    tours = ("<section class='msx-sec msx-sec--sand'><div class='mst-wrap'><div class='msx-row rv'><div><span class='mst-eyebrow'>Most popular</span><h2>Our best-loved journeys</h2></div>"
             "<div class='msx-ctl'><div class='msx-tabs' role='tablist'>%s</div><div class='msx-arrs'><button type='button' class='msx-arr' data-d='-1' aria-label='Previous'>←</button>"
             "<button type='button' class='msx-arr' data-d='1' aria-label='Next'>→</button></div></div></div>%s"
             "<p class='mst-more'><a class='mst-btn mst-btn--dark' href='%s/our-destinations/'>See all tours</a> <a class='mst-btn mst-btn--line' href='%s/destinations-copy/'>See all day trips</a></p></div></section>") % (tabs, tracks, SITE, SITE)
    dests = ''.join("<a class='msx-d msx-d--%s rv' href='%s%s' style='background-image:url(%s)'><span><b>%s</b><small>%s</small></span><i>→</i></a>" % (
        k, SITE, u, img or BY[2943]['img'], n, d) for n, d, img, u, k in DEST)
    dest = ("<section class='msx-sec'><div class='mst-wrap'>" + head('Key destinations', 'From the medinas <em>to the dunes</em>',
            'Journeys across Morocco’s most iconic regions: imperial cities, Atlas valleys, Saharan dunes and the Atlantic coast.') +
            "<div class='msx-bento'>" + dests + '</div></div></section>')
    stats = ("<section class='msx-band' style='background-image:url(%s)'><div class='mst-wrap msx-band-in rv'><blockquote>“We don’t just show you Morocco. <em>We welcome you home.</em>”"
             "<cite>The Morocco Sky Travel family</cite></blockquote><ul class='msx-num'>"
             "<li><b data-n='7' data-s='+'>7+</b><span>years of experience</span></li><li><b data-n='21'>21</b><span>ready-made itineraries</span></li>"
             "<li><b data-n='5'>5</b><span>departure cities</span></li><li><b data-n='100' data-s='%%'>100%%</b><span>private tours</span></li></ul></div></section>") % BY[2847]['img']
    about = ("<section class='msx-sec'><div class='mst-wrap msx-about'><div class='msx-pics rv'><span class='p1' style='background-image:url(%s)' role='img' aria-label='Morocco Sky Travel team in the desert'></span>"
             "<span class='p2' style='background-image:url(%s)'></span><span class='msx-seal'><b>7+</b>years on the road</span></div>"
             "<div class='rv'><span class='mst-eyebrow'>Our story</span><h2>A family story that began <em>in the sands of Zagora</em></h2>"
             "<p>Our journey began generations ago with a grandfather who guided travellers across the dunes by camel. Today we carry on that family legacy, creating private trips across Morocco.</p>"
             "<p>We blend our Berber heritage with modern comfort, so you can ride across the Sahara, wander through vibrant medinas and discover the Atlas with people who call this land home.</p>"
             "<ul class='msx-ticks'><li>Experienced private drivers</li><li>Local guides on request</li><li>No hidden costs</li><li>Support during your whole trip</li></ul>"
             "<a class='mst-btn mst-btn--dark' href='%s/elementor-366/'>Read our story</a></div></div></section>") % (ABOUT1, BY[2947]['img'], SITE)
    steps = ("<section class='msx-sec msx-sec--sand'><div class='mst-wrap'>" + head('How it works', 'Your trip in <em>three easy steps</em>') + "<ol class='msx-steps'>" +
             ''.join("<li class='rv'><span>%d</span><h3>%s</h3><p>%s</p></li>" % (n + 1, esc(a), esc(b)) for n, (a, b) in enumerate(STEPS)) +
             "</ol><p class='mst-more'><a class='mst-btn mst-btn--gold' href='#book'>Start planning</a> <a class='mst-btn mst-btn--wa' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> WhatsApp us</a></p></div></section>") % wa
    why = ("<section class='msx-sec'><div class='mst-wrap'>" + head('Why travel with us', 'Authentic, comfortable, <em>truly local</em>') + "<div class='msx-why'>" +
           ''.join("<div class='rv'><span class='ic'><i class='%s'></i></span><h3>%s</h3><p>%s</p></div>" % (WHY_IC[n], esc(a), esc(b)) for n, (a, b) in enumerate(WHY)) + '</div></div></section>')
    ld = ldscript({'@context': 'https://schema.org', '@type': 'TravelAgency', '@id': SITE + '/#agency', 'name': 'Morocco Sky Travel', 'url': SITE + '/',
                   'logo': LOGO, 'image': HERO, 'telephone': '+212667307641', 'email': EMAIL,
                   'description': 'Family-run travel company offering private Morocco tours, Sahara desert trips and day trips.',
                   'address': {'@type': 'PostalAddress', 'addressLocality': 'Fes', 'addressCountry': 'MA'}, 'sameAs': [u for n, u in SOCIAL]})
    return "<div class='mst msx'>" + hero + svc + tours + dest + stats + about + steps + why + '</div>' + HOME_JS + ld

def reviews_head():
    return ("<div class='mst msx msx-head' style='margin-bottom:0'><span class='mst-eyebrow'>Testimonials</span><h2>What our travellers <em>say</em></h2>"
            "<p>Our clients’ satisfaction is our top priority. Read real reviews from travellers on Tripadvisor.</p></div>")

def cta_band():
    return ("<div class='mst msx'><section class='mst-wrap'><div class='msx-cta' style='background-image:url(%s)'><div><span class='mst-eyebrow'>Ready when you are</span>"
            "<h2>Your Moroccan adventure <em>starts here</em></h2><p>Tell us what you dream of. We reply with a free, personal plan, with no payment needed to ask.</p></div>"
            "<div class='acts'><a class='mst-btn mst-btn--gold' href='#book'>Get a free quote</a><a class='mst-btn mst-btn--ghost' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> %s</a></div></div></section></div>") % (
        BY[2805]['img'], wa_link(WA_PLAN), PHONE)

def home():
    k = 479
    rev = container(eid(k, 'c5'), [w_html(eid(k, 'w5'), reviews_head()), w_sc(eid(k, 'w6'), '[trustindex no-registration=tripadvisor]')],
                    {'css_classes': 'mst-rev', 'padding': {'unit': 'px', 'top': '88', 'right': '20', 'bottom': '40', 'left': '20', 'isLinked': False},
                     'flex_gap': {'unit': 'px', 'size': 20, 'column': '20', 'row': '20'}})
    head_ = book_head(title='Plan your trip with us', text='Tell us your dates, group size and the places you dream of. We will design a private itinerary and send you a personal quote.')
    return [container(eid(k, 'c1'), [w_html(eid(k, 'w1'), home_top())]), rev,
            book_container(k, head_)]

def payload_raw(pid, ed, extra=None):
    m = {'_elementor_data': nobs(json.dumps(ed, ensure_ascii=False, separators=(',', ':')))}
    if extra: m.update(extra)
    return {'ID': pid, 'meta_input': m}

if __name__ == '__main__':
    from build import preview
    css = open('style.css').read()
    hd, ft = header(), footer()
    hed = [container(eid(308, 'c1'), [w_html(eid(308, 'w1'), hd)])]
    fed = [container(eid(316, 'c1'), [w_html(eid(316, 'w1'), ft)])]
    hm = home()
    json.dump(payload_raw(308, hed), open('out/308.json', 'w'), ensure_ascii=False)
    json.dump(payload_raw(316, fed), open('out/316.json', 'w'), ensure_ascii=False)
    json.dump({'ID': 479, 'fields': {'post_title': 'Home'}, 'meta_input': payload_raw(479, hm, {
        '_elementor_edit_mode': 'builder', '_wp_page_template': 'elementor_header_footer', 'site-post-title': 'disabled',
        'ast-title-bar-display': 'disabled', 'ast-featured-img': 'disabled'})['meta_input']}, open('out/479.json', 'w'), ensure_ascii=False)
    body = (hm[0]['elements'][0]['settings']['html'] + "<div class='mst-rev' style='padding:88px 20px 40px'>" + reviews_head() + "<div style='height:200px;background:#eee;max-width:1180px;margin:20px auto'>Tripadvisor widget</div></div>"
            + "<div class='mst-book' id='book'>" + hm[2]['elements'][0]['settings']['html'] + "<div class='mst-formbox'><div class='wpcf7'>form</div></div></div>")
    open('preview/home.html', 'w').write("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{margin:0}" + css + '</style></head><body>' + hd + body + ft + '</body></html>')
    print('ok', [len(json.dumps(x)) for x in (hed, fed, hm)])
