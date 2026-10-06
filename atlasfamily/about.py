"""Clean rebuild of the About Us page (8277), keeping the owner's text and photos."""
import json
from home import CSS, container, html, eid, U, S, WA, TREKS, CONTACT

ABOUT_CSS = ("<style>.afh-stats{display:flex;gap:14px;margin-top:24px}.afh-stats div{background:var(--sand);border-radius:14px;padding:16px 22px}"
             ".afh-stats b{display:block;font-size:30px;line-height:1;color:var(--o)}.afh-stats span{font-size:14px;color:var(--mut)}"
             ".afh-founder{display:grid;grid-template-columns:380px 1fr;gap:56px;align-items:center}.afh-founder .ph{border-radius:20px;min-height:480px;background:#c9a77c center/cover}"
             ".afh-founder h2{font-size:clamp(28px,3vw,40px);margin-bottom:18px}.afh-founder p{color:var(--mut);font-size:16.5px}"
             ".afh-team{display:grid;grid-template-columns:1fr 1fr;gap:28px}.afh-team article{background:#fff;border-radius:20px;overflow:hidden;box-shadow:0 18px 44px -26px rgba(0,0,0,.35)}"
             ".afh-team .ph{height:340px;background:#c9a77c center/cover}.afh-team .tx{padding:26px 28px}.afh-team h3{font-size:24px;margin-bottom:4px}"
             ".afh-team small{display:block;color:var(--o);font-weight:700;font-size:14px;margin-bottom:12px}.afh-team p{color:var(--mut);margin:0 0 10px}"
             ".afh-band{position:relative;background:#2a2017 center/cover;color:#fff;padding:110px 0;text-align:center}.afh-band:before{content:'';position:absolute;inset:0;background:rgba(20,14,8,.72)}"
             ".afh-band .afh-w{position:relative;max-width:820px}.afh-band h2{color:#fff;font-size:clamp(28px,3.2vw,42px);margin-bottom:16px}.afh-band p{color:rgba(255,255,255,.9);font-size:17px}"
             ".afh-band .afh-btns{justify-content:center;margin-top:24px}"
             "@media (max-width:900px){.afh-founder,.afh-team{grid-template-columns:1fr}.afh-founder .ph{min-height:340px}.afh-stats{flex-wrap:wrap}}</style>")

INTRO = ["At Atlas Family Adventure, we believe that the best way to discover Morocco is to experience it from the inside. Our journeys are built around the landscapes, traditions, and local communities that make this country unique.",
         "From mountain trails and Amazigh villages to desert landscapes and authentic cultural encounters, we create meaningful adventures that go beyond sightseeing. We keep our groups personal, our experiences genuine, and our journeys connected to the places and people we visit.",
         "Whether you come to hike, explore, learn, or simply experience a different side of Morocco, we are here to make your journey feel personal, welcoming, and unforgettable."]
FOUNDER = ["My journey as a mountain guide began after the passing of my uncle, Mohamed, who was a renowned guide in our family and one of the most respected mountain guides in our region.",
           "After he passed away, I decided to step into his role and continue the path he had started. I began leading treks through the mountains I have called home all my life, learning from my family, the local communities, and every journey along the way.",
           "For me, guiding is more than leading people from one place to another. It is about sharing the mountains, the culture, the stories, and the way of life that I grew up with.",
           "Today, through Atlas Family Adventure, I have the opportunity to share these places with travelers from around the world and show them a side of Morocco that goes beyond the usual tourist trails."]
TEAM = [('Mohamed', 'Driver, local guide & partner', U + 'unnamed-1-scaled.jpg',
         ['Mohamed is an experienced driver, local guide, and partner of Mehdi at Atlas Family Adventure. As Mehdi’s cousin, he has been part of the adventure from the beginning.',
          'Born and raised in the High Atlas Mountains, he knows the roads, valleys, and desert routes of Morocco by heart. With his calm personality, safe driving, and local knowledge, Mohamed helps make every journey smooth, comfortable, and authentic for our guests.']),
        ('Brahim', 'Mehdi’s father', U + 'unnamed-2.jpg',
         ['Brahim is Mehdi’s father and has been part of trekking life from the very beginning. Having traveled across Morocco for many years, he knows the mountains, valleys, and desert like few others.',
          'His experience, kindness, and warm hospitality make every meal a special moment and every guest feel like part of the family. For many of our travelers, sharing tea and dinner with Brahim around the campfire becomes one of the most memorable parts of the journey.'])]

def page():
    intro = ("<section class='afh-sec'><div class='afh-w afh-split'><div><span class='afh-k'>We are Atlas Family Adventure</span><h2>More Than a Tour</h2>"
             + ''.join('<p>%s</p>' % p for p in INTRO) +
             "<div class='afh-stats'><div><b>12+</b><span>Years of experience</span></div><div><b>250+</b><span>Happy clients</span></div></div></div>"
             "<div class='afh-pics'><span style='background-image:url(%sGFFI9802.jpg)'></span><span style='background-image:url(%sWhatsApp-Image-2026-09-20-at-11.17.35-1-1.jpeg)'></span></div></div></section>") % (U, U)
    founder = ("<section class='afh-sec afh-sand'><div class='afh-w afh-founder'><div class='ph' style='background-image:url(%sWhatsApp-Image-2026-09-22-at-02.12.45.jpeg)' role='img' aria-label='Mehdi, founder of Atlas Family Adventure'></div>"
               "<div><span class='afh-k'>Our founder</span><h2>Hello, I’m Mehdi</h2><p><b>The founder of Atlas Family Adventure.</b></p>" + ''.join('<p>%s</p>' % p for p in FOUNDER) + '</div></div></section>') % U
    team = ("<section class='afh-sec'><div class='afh-w'><div class='afh-head'><span class='afh-k'>Our family team</span><h2>The people behind your journey</h2></div><div class='afh-team'>"
            + ''.join("<article><div class='ph' style='background-image:url(%s)'></div><div class='tx'><h3>Meet %s</h3><small>%s</small>%s</div></article>" % (img, n, r, ''.join('<p>%s</p>' % p for p in ps)) for n, r, img, ps in TEAM)
            + '</div></div></section>')
    band = ("<section class='afh-band' style='background-image:url(%sWhatsApp-Image-2026-09-20-at-18.29.24.jpeg)'><div class='afh-w'><span class='afh-k' style='color:#ffd2bd'>Our treks</span>"
            "<h2>Discover Morocco Beyond the Ordinary</h2><p>We offer spectacular treks and authentic adventures through places that are often known only to local people. From hidden mountain trails and remote valleys to traditional villages and quiet desert landscapes, we take you beyond the usual tourist routes.</p>"
            "<p>With our local knowledge and deep connection to the places we call home, we invite you to experience Morocco in a more authentic way, through its landscapes, people, culture, and stories.</p>"
            "<div class='afh-btns'><a class='afh-b afh-b--p' href='%s'>Our Treks</a><a class='afh-b afh-b--g' href='%s'>Contact us</a></div></div></section>") % (U, TREKS, CONTACT)
    return CSS + ABOUT_CSS + "<div class='afh'>" + intro + founder + team + band + '</div>'

if __name__ == '__main__':
    ed = [container(eid('about', 'c1'), [html(eid('about', 'w1'), page())])]
    s = json.dumps(ed, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s
    open('about_elementor.json', 'w').write(s)
    open('about_preview.html', 'w').write("<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><body style='margin:0;font-family:system-ui'>" + page())
    print(len(s))
