"""Epic Travel Morocco – About us (1247), Our fleet (1334) and Tours (69, /destination/) in the chic Moroccan style (chic.py).

python3 pages.py -> about-1247.json, fleet-1334.json, tours-69.json (values of _elementor_data)
                    preview-about.html, preview-fleet.html, preview-tours.html
Texts come from the previous versions of the pages (summaries in backups/epictravelmorocco/).
"""
import json, os
import build as B
import chic as C

HERE = os.path.dirname(os.path.abspath(__file__))
U, SITE = C.U, C.SITE

# ---------------------------------------------------------------- shared page css
CSS = """
.cp-split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(40px,7vw,110px);align-items:center}
.cp-pair{position:relative;padding:0 0 70px 0}
.cp-pair .ch-archf{width:74%}
.cp-pair .ch-arch{height:clamp(420px,42vw,560px)}
.cp-pair .cp-pair2{position:absolute;right:0;bottom:0;width:46%;border:10px solid #fff;border-radius:999px 999px 0 0;overflow:hidden;background:#fff;box-shadow:0 30px 60px rgba(13,26,31,.14)}
.cp-pair .cp-pair2 img{width:100%;height:clamp(240px,24vw,320px);object-fit:cover}
.cp-txt p{color:var(--mut)}
.cp-txt h3{font-size:30px;margin:34px 0 12px}
.cp-pillars{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid var(--line)}
.cp-pillars>div{padding:50px 38px 10px;border-left:1px solid var(--line)}
.cp-pillars>div:first-child{border-left:0;padding-left:0}
.cp-num{display:flex;align-items:center;gap:12px;font:italic 400 22px var(--fh);color:var(--gold);margin-bottom:16px}
.cp-pillars h3{font-size:32px;margin-bottom:14px}
.cp-pillars p{color:var(--mut);margin:0}
.cp-quote{max-width:860px;margin:0 auto;text-align:center}
.cp-quote blockquote{margin:0;font:italic 400 clamp(28px,3.2vw,42px)/1.35 var(--fh);color:var(--ink)}
.cp-quote p{margin-top:28px;color:var(--mut)}
/* fleet */
.cp-feat{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.cp-feat>div{padding:38px 34px;border-left:1px solid var(--line);text-align:center}
.cp-feat>div:first-child{border-left:0}
.cp-feat .ch-star{width:22px;height:22px;color:var(--gold);margin:0 auto 14px;display:block}
.cp-feat b{display:block;font:400 25px/1.25 var(--fh);margin-bottom:6px}
.cp-feat span{color:var(--mut);font-size:15px}
.cp-car{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(40px,7vw,100px);align-items:center;padding:clamp(50px,6vw,80px) 0;border-top:1px solid var(--line)}
.cp-car:first-child{border-top:0}
.cp-car.rev .cp-car-i{order:2}
.cp-car-i .ch-arch{height:clamp(320px,34vw,460px);background:var(--paper)}
.cp-car-i .ch-arch img{object-fit:contain;padding:8% 6% 0}
.cp-car-n{font:italic 400 64px/1 var(--fh);color:var(--gold);opacity:.55;margin-bottom:10px}
.cp-car h3{font-size:clamp(34px,3.6vw,48px);margin-bottom:12px}
.cp-cap{display:inline-flex;align-items:center;gap:10px;font-size:11.5px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:18px}
.cp-car p{color:var(--mut);max-width:440px}
/* tours */
.cp-tours{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:70px 40px}
.cp-tour{display:block;color:var(--ink)}
.cp-tour .ch-archf{padding:10px}
.cp-tour .ch-arch{height:clamp(340px,30vw,430px)}
.cp-tour:hover .ch-arch img{transform:scale(1.06)}
.cp-tour small{display:flex;align-items:center;gap:10px;margin:22px 0 10px;font-size:11px;font-weight:500;letter-spacing:.3em;text-transform:uppercase;color:var(--gold)}
.cp-tour h3{font-size:clamp(26px,2.3vw,32px);line-height:1.12;margin-bottom:14px;text-transform:capitalize}
.cp-tour .ch-link{font-size:11px}
.cp-intro{max-width:720px;margin:0 auto 80px;text-align:center}
@media (max-width:1024px){.cp-tours{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:900px){.cp-split,.cp-car{grid-template-columns:1fr}.cp-car.rev .cp-car-i{order:0}.cp-pillars,.cp-feat{grid-template-columns:1fr}
 .cp-pillars>div,.cp-feat>div{border-left:0!important;padding:36px 0 30px!important}.cp-pillars>div+div,.cp-feat>div+div{border-top:1px solid var(--line)}}
@media (max-width:640px){.cp-tours{grid-template-columns:1fr;gap:56px}.cp-pair .ch-archf{width:82%}.cp-pair .cp-pair2{width:52%}}
"""


def page(body):
    return C.style(CSS) + '<div class="ch">' + body + '</div>'


def btn_wa(cls='ch-btn ch-btn-g'):
    return '<a class="' + cls + '" href="https://wa.me/' + B.PHONE1.lstrip('+') + '">WhatsApp</a>'


# ---------------------------------------------------------------- About us
WHO = ('We are a team of passionate travelers and Morocco enthusiasts who are dedicated to sharing the best of what this incredible country has to offer. '
       'With years of experience in the travel industry and a deep understanding of Morocco’s hidden treasures, we pride ourselves on creating '
       'tailor-made experiences that are as unique as our clients.')
OFFER = ('At Epic Travel Morocco, we specialize in personalized travel experiences that highlight the diversity and richness of Moroccan culture. '
         'Whether you’re looking for a luxurious escape, an adventure-filled journey, or a cultural immersion, we customize every itinerary '
         'to meet your needs and exceed your expectations.')
STORY = ('Epic Travel Morocco began with a simple idea: to offer travelers a more meaningful way to experience Morocco. Our founders, experienced '
         'globetrotters with a deep connection to Morocco, saw the need for travel experiences that are authentic, enriching, and truly epic. '
         'Today, we are known for our personalized approach and commitment to quality.')


def about():
    hero = C.hero('About us', 'Your epic Moroccan<br><em>adventure awaits</em>',
                  'At Epic Travel Morocco, we’re passionate about one thing: crafting journeys that take you to the heart of Morocco’s most captivating destinations.',
                  U + '2025/11/pexels-henrik-le-botos-1588507-3878114-scaled.jpg',
                  '<a class="ch-btn ch-btn-g" href="' + SITE + '/destination/">Explore our tours</a><a href="' + SITE + '/contact-2/">Contact us</a>',
                  'Kasbah and desert landscape in Morocco')
    intro = ('<section class="ch-s"><div class="ch-w cp-split"><div class="cp-pair">'
             '<div class="ch-archf"><div class="ch-arch"><img src="' + U + '2025/11/WhatsApp-Image-2023-03-27-at-22.53.18-1.jpeg" alt="Epic Travel Morocco on tour" loading="lazy"></div></div>'
             '<div class="cp-pair2"><img src="' + U + '2025/11/pexels-piotr-arnoldes-7862031-6441048-scaled.jpg" alt="Moroccan landscape" loading="lazy"></div></div>'
             '<div class="cp-txt">' + C.kicker('Who we are') + '<h2 class="ch-h2">Passionate about<br><em>Morocco</em></h2>'
             '<p class="ch-lead">Our company was founded on the belief that travel should be a blend of adventure, discovery and cultural immersion.</p>'
             '<p>' + WHO + '</p><p style="margin-top:34px"><a class="ch-link" href="' + SITE + '/destination/">Discover our journeys</a></p></div></div></section>')
    pillars = ('<section class="ch-s ch-paper"><div class="ch-w"><div class="ch-center" style="margin-bottom:70px">' + C.orn()
               + '<h2 class="ch-h2">What makes a journey<br><em>epic</em></h2></div><div class="cp-pillars">'
               '<div><div class="cp-num">' + C.star() + 'I</div><h3>Who we are</h3><p>A local team of travelers and Morocco enthusiasts, sharing the hidden treasures of our country.</p></div>'
               '<div><div class="cp-num">' + C.star() + 'II</div><h3>Our offerings</h3><p>' + OFFER + '</p></div>'
               '<div><div class="cp-num">' + C.star() + 'III</div><h3>Our promise</h3><p>Every itinerary is tailor-made around your pace, your interests and the places you dream of.</p></div>'
               '</div></div></section>')
    story = ('<section class="ch-s"><div class="ch-w cp-split"><div class="cp-txt">' + C.kicker('Our story')
             + '<h2 class="ch-h2">A more meaningful way<br>to <em>experience Morocco</em></h2><p>' + STORY + '</p></div>'
             '<div class="ch-archf"><div class="ch-arch" style="height:clamp(420px,44vw,600px)"><img src="' + U + '2025/11/pexels-reyyan-505450018-33429795-scaled.jpg" alt="Moroccan architecture" loading="lazy"></div></div>'
             '</div></section>')
    return page(hero + intro + pillars + story + C.cta())


# ---------------------------------------------------------------- Our fleet
CARS = [
    ('Mercedes Mini Van', 'From 2 up to 7 passengers', 'Gemini_Generated_Image_kunskunskunskuns-2.png',
     'Ideal for small groups and families, providing a comfortable and private travel option with a premium touch.'),
    ('Toyota Prado SUV', 'For adventurous journeys', 'Gemini_Generated_Image_tqr8vttqr8vttqr8.png',
     'For the adventurous souls, our SUV vehicles are perfect for exploring Morocco’s diverse and challenging terrains.'),
    ('Mercedes Sprinter Minibus', 'From 8 up to 17 passengers', 'Gemini_Generated_Image_pelh0jpelh0jpelh.png',
     'Perfect for medium-sized groups, offering a spacious and relaxing ride while exploring Morocco’s diverse landscapes.'),
    ('Big Buses', 'From 18 up to 48 passengers', 'Gemini_Generated_Image_wnw2hgwnw2hgwnw2.png',
     'Suitable for large groups, ensuring everyone travels together comfortably.'),
]


def fleet():
    hero = C.hero('Our fleet', 'Car rental<br><em>with driver</em>',
                  'Tailored travel transport across Morocco. Experience the country in comfort and luxury, with professional drivers and a fleet for every journey.',
                  U + '2025/11/Gemini_Generated_Image_vvja03vvja03vvja.png',
                  '<a class="ch-btn ch-btn-g" href="' + SITE + '/contact-2/">Book a vehicle</a>' + '<a href="https://wa.me/' + B.PHONE1.lstrip('+') + '">WhatsApp</a>',
                  'Epic Travel Morocco vehicle')
    intro = ('<section class="ch-s" style="padding-bottom:60px"><div class="ch-w"><div class="cp-intro">' + C.orn()
             + '<p class="ch-lead">From the elegant Mercedes Vito to the rugged Toyota Prado, from Sprinter minibuses to spacious coaches, '
             'each vehicle is meticulously maintained for a smooth and enjoyable ride.</p></div>'
             '<div class="cp-feat"><div>' + C.star() + '<b>Professional drivers</b><span>Safe and seamless journeys</span></div>'
             '<div>' + C.star() + '<b>Maintained vehicles</b><span>Modern, clean and comfortable</span></div>'
             '<div>' + C.star() + '<b>All of Morocco</b><span>Medinas, Atlas Mountains and Sahara</span></div></div></div></section>')
    cars = ''
    for k, (name, cap, img, txt) in enumerate(CARS):
        cars += ('<div class="cp-car' + (' rev' if k % 2 else '') + '"><div class="cp-car-i"><div class="ch-archf"><div class="ch-arch">'
                 '<img src="' + U + '2025/11/' + img + '" alt="' + name + '" loading="lazy"></div></div></div>'
                 '<div><div class="cp-car-n">0' + str(k + 1) + '</div><h3>' + name + '</h3><div class="cp-cap">' + C.star() + cap + '</div>'
                 '<p>' + txt + '</p><p style="margin-top:28px"><a class="ch-link" href="' + SITE + '/contact-2/">Request this vehicle</a></p></div></div>')
    cars = '<section class="ch-s" style="padding-top:20px"><div class="ch-w">' + cars + '</div></section>'
    return page(hero + intro + cars + C.cta('Travel Morocco <em>in comfort</em>',
                                            'Tell us your route and the size of your group. We will suggest the right vehicle and driver.'))


# ---------------------------------------------------------------- Tours (Destination)
TOURS = [
    ('Sahara Desert Experience', 'sahara-desert-experience', '2025/11/pexels-zakariahanif-12214734-scaled.jpg', '4 nights · 3 days'),
    ('Majestic Kasbah and Desert Adventure', 'majestic-kasbah-and-desert-adventure', '2025/11/pexels-henrik-le-botos-1588507-3878114-scaled.jpg', '5 nights · 4 days'),
    ('Journeys Through Morocco', 'journeys-trough-morocco', '2025/11/pexels-adthiry-18661913-scaled.jpg', '5 nights · 4 days'),
    ('Highlights of Morocco', 'highlights-of-morocco', '2025/11/WhatsApp-Image-2023-03-02-at-22.42.11.jpeg', '5 nights · 6 days'),
    ('Discover Northern Morocco', 'discover-northern-morocco-tour', '2025/11/pexels-abdel-achkouk-2861018-22717119-scaled.jpg', '6 nights · 5 days'),
    ('Moroccan Historical Cities', 'moroccan-historical-cities-tour', '2025/11/MXLU7731.jpg', '7 nights · 8 days'),
    ('The Essence of Morocco', 'the-essence-of-morocco-tour', '2025/11/ifrane-1.jpg', '8 nights · 9 days'),
    ('The Magic of Morocco', 'the-magic-of-morocco', '2025/11/pexels-micklatter-18375222-scaled.jpg', '9 nights · 8 days'),
    ('Authentic Morocco Tour', 'n', '2025/11/pexels-gabriel-garcia-1263144-2404046-scaled.jpg', '11 nights · 10 days'),
    ('Moroccan Odyssey, 15-Day Grand Tour', 'moroccan-odyssey-15-day-grand-tour', '2025/07/IMG_5641.jpg', '15 nights · 14 days'),
]


def tours():
    hero = C.hero('Our tours', 'Journeys across<br><em>Morocco</em>',
                  'Private tours from Marrakech to the Sahara, the Atlas Mountains and the imperial cities. Every itinerary can be adapted to your dates and pace.',
                  U + '2025/11/pexels-micklatter-18375222-scaled.jpg',
                  '<a class="ch-btn ch-btn-g" href="#cp-tours">See the tours</a><a href="' + SITE + '/contact-2/">Tailor-made trip</a>',
                  'Morocco landscape')
    cards = ''.join('<a class="cp-tour" href="' + SITE + '/all-tour/' + s + '/"><div class="ch-archf"><div class="ch-arch">'
                    '<img src="' + U + img + '" alt="' + t + '" loading="lazy"></div></div><small>' + C.star() + d + '</small>'
                    '<h3>' + t + '</h3><span class="ch-link">Discover</span></a>' for t, s, img, d in TOURS)
    grid = ('<section class="ch-s" id="cp-tours"><div class="ch-w"><div class="cp-intro">' + C.orn()
            + '<h2 class="ch-h2">Choose your <em>journey</em></h2><p class="ch-mut">From a few days in the desert to a grand tour of the kingdom, '
            'each journey is private and guided by our local team.</p></div><div class="cp-tours">' + cards + '</div></div></section>')
    return page(hero + grid + C.cta('Dreaming of <em>something else?</em>',
                                    'We design tailor-made itineraries. Tell us what you would like to see and we will create your journey.'))


PAGES = [('about-1247', 'About', about), ('fleet-1334', 'Our fleet', fleet), ('tours-69', 'Tours', tours)]

if __name__ == '__main__':
    for key, title, fn in PAGES:
        html = fn()
        s = json.dumps(C.html_page(key, html), ensure_ascii=False, separators=(',', ':'))
        assert '\\' not in s and '"' not in json.loads(s)[0]['elements'][0]['settings']['html']
        open(os.path.join(HERE, key + '.json'), 'w').write(s)
        open(os.path.join(HERE, 'preview-' + key.split('-')[0] + '.html'), 'w').write(C.preview(html, title))
        print(key, len(s))
