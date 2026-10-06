"""Custom header (35 + 38), footer (41), preloader and site-wide button/font styles for atlasfamilyadventure.com."""
import json
from home import container, html, eid, WA, TREKS, CONTACT, S
from brand import EXTRA

U = 'https://atlasfamilyadventure.com/wp-content/uploads/'
LOGO = U + '2023/10/IMG_23471.png'
SITE = 'https://atlasfamilyadventure.com'
NAV = [('Home', SITE + '/'), ('Our Treks', TREKS), ('Sahara Tours', S + '/sahara-desert-tours/'), ('About Us', S + '/about/'), ('Contact', CONTACT)]
C1, C1D, INK, SAND = '#b8432b', '#8f3320', '#2a2017', '#faf3ea'   # clay red, dark clay, Atlas night, sand

GLOBAL = ("<link rel='preconnect' href='https://fonts.googleapis.com'><link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Caveat:wght@600;700&display=swap'>"
 "<style>"
 # brand colour everywhere (theme, Elementor globals, WP Travel Engine, our pages)
 ":root{--theme-color:%(c1)s!important;--e-global-color-travolo_opt_primary:%(c1)s!important;--wpte-primary-color:%(c1)s!important;--primary-color:%(c1)s!important}"
 ".afh,.afs{--o:%(c1)s!important;--od:%(c1d)s!important}"
 # buttons: colour + font site-wide
 ".vs-btn,[class*=vs-btn],.wpcf7-submit,input[type=submit],button[type=submit],[class*=wpte][class*=btn],[class*=wte][class*=btn],[class*=wpte][class*=button],.afh a.afh-b,.afs a.afs-b,.afg-btn"
 "{font-family:Poppins,sans-serif!important;font-weight:600!important;letter-spacing:.01em!important;text-transform:none!important;border-radius:999px!important}"
 ".vs-btn,[class*=vs-btn]:not(.afh-b),.wpcf7-submit,input[type=submit],button[type=submit],[class*=wpte][class*=btn],[class*=wte][class*=btn],[class*=wpte][class*=button]"
 "{background:%(c1)s!important;border-color:%(c1)s!important;color:#fff!important}"
 ".vs-btn:hover,[class*=vs-btn]:hover,.wpcf7-submit:hover,input[type=submit]:hover,button[type=submit]:hover,[class*=wpte][class*=btn]:hover,[class*=wte][class*=btn]:hover"
 "{background:%(ink)s!important;border-color:%(ink)s!important;color:#fff!important}"
 # hide theme preloader (the squares) - ours replaces it
 ".preloader,#preloader,.vs-preloader,.th-preloader,.preloader-inner{display:none!important}"
 # our preloader
 "#afp{position:fixed;inset:0;z-index:999999;background:%(sand)s;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;transition:opacity .5s ease,visibility .5s}"
 "#afp{animation:afpout .5s ease 1.3s forwards}@keyframes afpout{to{opacity:0;visibility:hidden}}#afp img{width:120px;height:auto}"
 "#afp .z{font:700 46px/1 system-ui,sans-serif;color:%(c1)s;animation:afpz 1.4s ease-in-out infinite}"
 "#afp svg{width:180px;height:40px}#afp path{fill:none;stroke:%(ink)s;stroke-width:2.5;stroke-linejoin:round;stroke-dasharray:400;stroke-dashoffset:400;animation:afpl 1.8s ease-in-out infinite}"
 "@keyframes afpz{0%%,100%%{transform:scale(1);opacity:.6}50%%{transform:scale(1.18);opacity:1}}@keyframes afpl{0%%{stroke-dashoffset:400}60%%,100%%{stroke-dashoffset:0}}"
 "</style>") % dict(c1=C1, c1d=C1D, ink=INK, sand=SAND)

PRELOADER = ("<div id='afp' aria-hidden='true'><img src='%s' alt=''><div class='z'>ⵣ</div>"
             "<svg viewBox='0 0 180 40'><path d='M2 38 L30 14 L44 26 L70 4 L92 28 L108 16 L132 34 L150 20 L178 38'/></svg></div>") % LOGO

HCSS = ("<style>.afg{font-family:Poppins,system-ui,sans-serif;position:relative;z-index:50}"
 ".afg *{box-sizing:border-box}.afg a{text-decoration:none}"
 ".afg-top{background:%(ink)s;color:rgba(255,255,255,.85);font-size:13.5px}"
 ".afg-top .in,.afg-bar .in{max-width:1240px;margin:0 auto;padding:0 20px;display:flex;align-items:center;justify-content:space-between;gap:20px}"
 ".afg-top .in{min-height:42px}.afg-top a{color:rgba(255,255,255,.88)}.afg-top a:hover{color:#fff}"
 ".afg-top .l{display:flex;gap:22px;flex-wrap:wrap}.afg-top .l a:before{margin-right:7px;color:#f2c9a0}"
 ".afg-top .m:before{content:'✉'}.afg-top .t:before{content:'☎'}.afg-top .tag{font-family:Caveat,cursive;font-size:20px;color:#f2c9a0}"
 ".afg-bar{background:#fff;box-shadow:0 10px 30px -20px rgba(0,0,0,.35)}.afg-bar .in{min-height:86px}"
 ".afg-logo img{height:64px;width:auto;display:block}"
 ".afg-nav{display:flex;gap:6px;align-items:center}.afg-nav a{color:%(ink)s;font-weight:500;font-size:15.5px;padding:10px 14px;border-radius:999px;transition:all .2s;position:relative}"
 ".afg-nav a:hover,.afg-nav a.on{color:%(c1)s}.afg-nav a.on:after{content:'ⵣ';position:absolute;left:50%%;bottom:-8px;transform:translateX(-50%%);font-size:11px;color:%(c1)s}"
 ".afg a.afg-btn{display:inline-flex;align-items:center;gap:8px;background:%(c1)s;color:#fff;padding:12px 22px;font-size:15px}.afg a.afg-btn:hover{background:%(ink)s}"
 ".afg-burger{display:none;width:46px;height:46px;border:1px solid #e8dccb;border-radius:12px;background:#fff;padding:13px 11px;flex-direction:column;justify-content:space-between;cursor:pointer}"
 ".afg-burger span{display:block;height:2px;background:%(ink)s;border-radius:2px}"
 ".afg .afh-rug{height:10px;background-size:26px 10px!important}"
 "@media (max-width:1024px){.afg-top .tag{display:none}.afg-nav{display:none;position:absolute;left:0;right:0;top:100%%;background:#fff;flex-direction:column;align-items:stretch;padding:12px 20px 20px;box-shadow:0 20px 30px -16px rgba(0,0,0,.3)}"
 ".afg-tg:checked~.afg-nav{display:flex}.afg-nav a{padding:14px 10px;border-bottom:1px solid #f0e6d8;border-radius:0}.afg-nav a.on:after{display:none}.afg-burger{display:flex}.afg-bar .afg-btn{display:none}.afg-logo img{height:52px}}"
 "@media (max-width:600px){.afg-top .in{justify-content:center}.afg-top .m{display:none}}</style>") % dict(c1=C1, ink=INK)

def header():
    nav = ''.join("<a href='%s'>%s</a>" % (u, n) for n, u in NAV)
    rug = EXTRA.replace('%23ff4911', '%23b8432b').replace('repeat-x center/56px 22px}', 'repeat-x center/56px 22px!important}')
    body = ("<header class='afg'><div class='afg-top'><div class='in'><div class='l'><a class='m' href='mailto:aelmahdizaki@gmail.com'>aelmahdizaki@gmail.com</a>"
            "<a class='t' href='tel:+212703501612'>+212 703 501 612</a></div><span class='tag'>Hiking & cultural journeys, from the Atlas to the Sahara</span></div></div>"
            "<div class='afg-bar'><div class='in'><a class='afg-logo' href='{site}/' aria-label='Atlas Family Adventure home'><img src='{logo}' alt='Atlas Family Adventure'></a>"
            "<input type='checkbox' id='afg-tg' class='afg-tg' hidden><nav class='afg-nav' aria-label='Main menu'>{nav}</nav>"
            "<a class='afg-btn' href='{wa}' target='_blank' rel='noopener'>Plan your trek</a>"
            "<label for='afg-tg' class='afg-burger' aria-label='Menu'><span></span><span></span><span></span></label></div></div><div class='afh-rug'></div></header>").format(site=SITE, logo=LOGO, nav=nav, wa=WA)
    return GLOBAL + rug + HCSS + PRELOADER + body

FCSS = ("<style>.aff{position:relative;background:%(ink)s;color:rgba(255,255,255,.78);font-family:Poppins,system-ui,sans-serif;font-size:15px;line-height:1.7;padding:120px 0 0;margin-top:40px}"
 ".aff *{box-sizing:border-box}.aff a{color:rgba(255,255,255,.82);text-decoration:none}.aff a:hover{color:#f2c9a0}"
 ".aff-peaks{position:absolute;top:-1px;left:0;width:100%%;height:90px;display:block}"
 ".aff .in{max-width:1240px;margin:0 auto;padding:0 20px}.aff-grid{display:grid;grid-template-columns:1.4fr 1fr 1.2fr 1.2fr;gap:44px}"
 ".aff-logo{background:#fff;border-radius:16px;padding:10px 14px;display:inline-block;margin-bottom:16px}.aff-logo img{height:64px;width:auto;display:block}"
 ".aff .tag{font-family:Caveat,cursive;font-size:28px;color:#f2c9a0;line-height:1.1;margin:0 0 10px}"
 ".aff h4{color:#fff;font-size:16px;font-weight:600;margin:6px 0 18px;position:relative;padding-bottom:12px}.aff h4:after{content:'';position:absolute;left:0;bottom:0;width:30px;height:2px;background:%(c1)s}"
 ".aff ul{list-style:none;margin:0;padding:0}.aff li{margin:0 0 10px}"
 ".aff-fam{display:flex;margin:14px 0 6px}.aff-fam span{width:52px;height:52px;border-radius:50%%;border:3px solid %(ink)s;background:#8a6a4a center/cover;margin-left:-12px}.aff-fam span:first-child{margin-left:0}"
 ".aff small{color:rgba(255,255,255,.6)}"
 ".aff a.afg-btn{display:inline-flex;margin-top:14px;background:%(c1)s;color:#fff;padding:12px 22px;border-radius:999px;font-weight:600}.aff a.afg-btn:hover{background:#fff;color:%(ink)s}"
 ".aff-bot{margin-top:60px;border-top:1px solid rgba(242,201,160,.18);padding:20px 0 24px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:10px;font-size:13.5px;color:rgba(255,255,255,.6)}"
 ".aff-bot b{color:#f2c9a0;font-weight:700}.aff .aff-dev a{color:#f2c9a0;font-weight:600}.aff .aff-dev a:hover{color:#fff}"
 "@media (max-width:1024px){.aff-grid{grid-template-columns:1fr 1fr}}@media (max-width:640px){.aff-grid{grid-template-columns:1fr;gap:30px}.aff{padding-top:90px}.aff-peaks{height:50px}.aff-bot{flex-direction:column}}</style>") % dict(c1=C1, ink=INK)

TREK_LINKS = [('M’Goun Summit Trek (4 days)', S + '/trip/4-day-mgoun-summit-trek/'), ('M’Goun Summit & Hidden Gorges (7 days)', S + '/trip/mgoun-4071m-summit-valleys-hidden-gorges/'),
              ('Saghro Volcanic Mountains (5 days)', S + '/trip/across-the-land-of-volcanoes/'), ('Sahara Desert Trek, Draa Valley (5 days)', S + '/trip/5-day-desert-trek-in-the-draa-valley-2/')]

def footer():
    peaks = ("<svg class='aff-peaks' viewBox='0 0 1440 90' preserveAspectRatio='none' aria-hidden='true'>"
             "<path d='M0 0 L1440 0 L1440 40 L1350 24 L1250 52 L1150 30 L1040 58 L930 18 L850 46 L760 26 L640 60 L520 34 L420 50 L330 16 L210 56 L120 38 L0 54Z' fill='#ffffff'/></svg>")
    fam = ''.join("<span style='background-image:url(%s)'></span>" % (U + p) for p in ('2026/09/WhatsApp-Image-2026-09-22-at-02.12.45.jpeg', '2026/09/unnamed-1-scaled.jpg', '2026/09/unnamed-2.jpg'))
    return FCSS + "<footer class='aff'>" + peaks + ("<div class='in'><div class='aff-grid'>"
            "<div><a class='aff-logo' href='%s/'><img src='%s' alt='Atlas Family Adventure' loading='lazy'></a><p class='tag'>Beyond Landscapes, Into Morocco.</p>"
            "<p>A family of mountain guides from the High Atlas, sharing treks and cultural journeys from the Atlas to the Sahara.</p>"
            "<div class='aff-fam'>%s</div><small>Mehdi, Mohamed &amp; Brahim</small><br><a class='afg-btn' href='%s' target='_blank' rel='noopener'>Plan your trek on WhatsApp</a></div>"
            "<div><h4>Explore</h4><ul>%s</ul></div>"
            "<div><h4>Popular treks</h4><ul>%s</ul></div>"
            "<div><h4>Contact</h4><ul><li><a href='tel:+212703501612'>+212 703 501 612</a></li><li><a href='mailto:aelmahdizaki@gmail.com'>aelmahdizaki@gmail.com</a></li>"
            "<li>Gueliz, Marrakech 22000, Morocco</li><li><a href='%s'>Send us a message →</a></li></ul></div></div>"
            "<div class='aff-bot'><span>© <span class='aff-y'>2026</span> Atlas Family Adventure. All rights reserved.</span><span>Made with care in the Atlas Mountains <b>ⵣ</b></span><span class='aff-dev'>Website developed by <a href='https://majdoulinean.com' target='_blank' rel='noopener'>Majdoulinean</a></span></div></div></footer>"
            "<script>document.querySelectorAll('.aff-y').forEach(function(e){e.textContent=new Date().getFullYear()})</script>") % (
        SITE, LOGO, fam, WA, ''.join("<li><a href='%s'>%s</a></li>" % (u, n) for n, u in NAV),
        ''.join("<li><a href='%s'>%s</a></li>" % (u, n) for n, u in TREK_LINKS), CONTACT)

if __name__ == '__main__':
    for name, key, h in (('header', 'hdr', header()), ('footer', 'ftr', footer())):
        ed = [container(eid('afchrome', key), [html(eid('afchrome', key, 'w'), h)])]
        s = json.dumps(ed, ensure_ascii=False, separators=(',', ':'))
        assert '\\' not in s, name
        open(name + '_elementor.json', 'w').write(s)
        print(name, len(s))
    open('chrome_preview.html', 'w').write("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><body style='margin:0'>" + header() +
        "<div style='height:500px;background:#eee;display:grid;place-items:center;font-family:system-ui'>page content<br><a class='vs-btn' href='#'>Theme button</a></div>" + footer())
