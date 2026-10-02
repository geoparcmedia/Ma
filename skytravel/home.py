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

def header():
    links = ''.join("<a href='%s%s'>%s</a>" % (SITE, u, n) for n, u in NAV)
    js = ("<script>(function(){var p=location.pathname;document.querySelectorAll('.msh-nav a').forEach(function(a){var h=new URL(a.href).pathname;"
          "if(h===p||(h!=='/'&&p.indexOf(h)===0))a.classList.add('on')});"
          "var b=document.querySelector('.msh-burger'),n=document.getElementById('msh-nav');if(b&&n)b.addEventListener('click',function(){var o=n.classList.toggle('open');"
          "b.setAttribute('aria-expanded',o?'true':'false')})})()</script>")
    return (FONTS + "<div class='mst msh'><div class='msh-in'><a class='msh-logo' href='%s/' aria-label='Morocco Sky Travel home'><img src='%s' alt='Morocco Sky Travel' height='56'></a>"
            "<nav class='msh-nav' id='msh-nav' aria-label='Main menu'>%s<a class='msh-m' href='%s/book/'>Book your trip</a></nav>"
            "<div class='msh-act'><a class='msh-wa' href='%s' target='_blank' rel='noopener' aria-label='WhatsApp'><i class='i-wa'></i><span>%s</span></a>"
            "<a class='mst-btn mst-btn--gold msh-cta' href='%s/book/'>Book your trip</a>"
            "<button type='button' class='msh-burger' aria-label='Menu' aria-expanded='false' aria-controls='msh-nav'><span></span><span></span><span></span></button></div></div></div>%s") % (
        SITE, LOGO, links, SITE, wa_link('Hello Morocco Sky Travel, I would like some information about a trip.'), PHONE, SITE, js)

def footer():
    tours = [BY[i] for i in (2805, 2794, 2771, 2847, 2814, 2829)]
    col_t = ''.join("<li><a href='%s/%s/'>%s</a></li>" % (SITE, t['url'], esc(t['card'])) for t in tours)
    col_c = ''.join("<li><a href='%s%s'>%s</a></li>" % (SITE, u, n) for n, u in NAV + [('Book your trip', '/book/')])
    soc = ''.join("<a href='%s' target='_blank' rel='noopener'>%s</a>" % (u, n) for n, u in SOCIAL)
    return ("<footer class='mst msf'><div class='mst-wrap msf-grid'>"
            "<div class='msf-brand'><img src='%s' alt='Morocco Sky Travel' height='64' loading='lazy'><p>%s</p><div class='msf-soc'>%s</div></div>"
            "<div><h3>Popular tours</h3><ul>%s</ul></div><div><h3>Company</h3><ul>%s</ul></div>"
            "<div><h3>Contact</h3><ul class='msf-ct'><li><a href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> %s</a></li>"
            "<li><a href='mailto:%s'><i class='i-mail'></i> %s</a></li><li><a href='tel:+212667307641'><i class='i-phone'></i> Call us: %s</a></li>"
            "<li><span><i class='i-pin'></i> Fez, Morocco – Sais</span></li></ul></div></div>"
            "<div class='mst-wrap msf-bot'><span>© <span class='msf-y'>2026</span> Morocco Sky Travel. All rights reserved.</span><a href='%s/our-destinations/'>Private Morocco tours &amp; desert trips</a></div></footer>"
            "<script>document.querySelectorAll('.msf-y').forEach(function(e){e.textContent=new Date().getFullYear()})</script>") % (
        LOGO_W, esc('Join us at Morocco Sky Travel and let us guide you through the enchanting landscapes and vibrant cultures of Morocco. Your adventure awaits!'),
        soc, col_t, col_c, wa_link('Hello Morocco Sky Travel, I would like some information about a trip.'), PHONE, EMAIL, EMAIL, PHONE, SITE)

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
           # trip finder -> WhatsApp
           "var f=r.querySelector('.msx-find');if(f)f.addEventListener('submit',function(e){e.preventDefault();var v=function(n){return f.elements[n].value};"
           "var m='Hello Morocco Sky Travel, I am planning a trip: '+v('len')+' starting from '+v('from')+', '+v('pax')+', travelling in '+v('when')+'. Could you send me an itinerary and a quote?';"
           "window.open('https://wa.me/" + WA + "?text='+encodeURIComponent(m),'_blank')});"
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
    find = ("<form class='msx-find' aria-label='Plan your trip'>" +
            opt(('Starting city', 'from'), ['Marrakech', 'Fes', 'Casablanca', 'Tangier', 'Agadir', 'Not sure yet']) +
            opt(('Trip length', 'len'), ['a 2–4 day trip', 'a 5–8 day trip', 'a 9–15 day trip', 'a day trip']) +
            opt(('Travellers', 'pax'), ['2 travellers', '1 traveller', '3–4 travellers', '5+ travellers', 'a family with children']) +
            opt(('When', 'when'), ['the next 3 months', 'spring', 'summer', 'autumn', 'winter', 'dates not fixed yet']) +
            "<button type='submit' class='mst-btn mst-btn--gold'><i class='i-wa'></i> Get my free plan</button></form>")
    hero = ("<header class='msx-hero'><div class='msx-hero-bg' style='background-image:url(%s)'></div><div class='mst-wrap msx-hero-in'>"
            "<span class='msx-pill'><b></b> Family-run local company · Fes, Morocco</span>"
            "<h1>Private Morocco Tours <em>&amp; Sahara Desert Trips</em></h1>"
            "<p class='msx-lead'>Tailor-made journeys through imperial cities, Atlas villages and golden dunes, with your own private driver and a local family team behind every detail.</p>"
            "<div class='mst-hero-ctas'><a class='mst-btn mst-btn--gold' href='%s/our-destinations/'>Explore our tours</a>"
            "<a class='mst-btn mst-btn--ghost' href='%s' target='_blank' rel='noopener'><i class='i-wa'></i> Chat on WhatsApp</a></div>%s"
            "<ul class='msx-trust'><li><i class='i-car'></i>Private driver &amp; 4x4</li><li><i class='i-flag'></i>Hand-picked riads &amp; camps</li>"
            "<li><i class='i-clock'></i>Flexible, tailor-made routes</li><li><i class='i-wa'></i>Free quote, fast reply</li></ul></div></header>") % (HERO, SITE, wa, find)
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
            container(eid(k, 'c7'), [w_html(eid(k, 'w7'), cta_band())], {'padding': {'unit': 'px', 'top': '40', 'right': '0', 'bottom': '80', 'left': '0', 'isLinked': False}}),
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
            + "<div style='padding:40px 0 80px'>" + cta_band() + "</div><div class='mst-book' id='book'>" + hm[3]['elements'][0]['settings']['html'] + "<div class='mst-formbox'><div class='wpcf7'>form</div></div></div>")
    open('preview/home.html', 'w').write("<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><style>body{margin:0}" + css + '</style></head><body>' + hd + body + ft + '</body></html>')
    print('ok', [len(json.dumps(x)) for x in (hed, fed, hm)])
