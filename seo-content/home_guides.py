"""Add a 'Plan Your Trip' section with the 5 travel guides to the homepage
(page 3247), right after the FAQ inside widget 62d7d51.
Reads ../homepage-redesign/elementor-data.json (same as live on 2026-10-12)
and writes home_elementor_guides.json."""
import json
from category_guides import CSS, card

CARDS = [
    card('Cycling', 'Gravel Biking in Morocco: The Complete Guide',
         'The best gravel routes, which bike to bring and how a guided tour works.', '/cycling-in-morocco-guide/'),
    card('Toubkal', 'Climbing Mount Toubkal: The Complete Guide',
         'Routes, difficulty, best season and what to pack for the highest peak in North Africa.', '/mount-toubkal-trek-guide/'),
    card('Seasons', 'Best Time to Visit Morocco',
         'Month by month: when to ride, when to climb and when to go to the desert.',
         '/best-time-to-visit-morocco-cycling-trekking/'),
    card('Happy Valley', 'Hiking the Happy Valley (Ait Bouguemez)',
         'Morocco&rsquo;s Berber heartland, home of our team in Azilal.', '/happy-valley-ait-bouguemez-hiking-guide/'),
]
SECTION = (CSS + "<section class='wgm-sec wgm-sand'><div class='wgm-wrap'><div class='wgm-head'>"
           "<span class='wgm-eyebrow'>Travel guides</span><h2>Plan Your Trip</h2>"
           "<p>Free guides written by our local team. Also read our <a href='https://wegravelmorocco.com/sahara-desert-trek-morocco-guide/'>"
           "Sahara desert trek guide</a>.</p></div><div class='wgg-cards'>%s</div></div></section>") % ' '.join(CARDS)

d = json.load(open('../homepage-redesign/elementor-data.json'))


def find(e):
    if isinstance(e, dict):
        if e.get('id') == '62d7d51':
            return e
        for v in e.values():
            r = find(v)
            if r:
                return r
    elif isinstance(e, list):
        for v in e:
            r = find(v)
            if r:
                return r


w = find(d)['settings']
END = '</section> </div><script>'
assert w['html'].count(END) == 1 and 'wgg-cards' not in w['html']
w['html'] = w['html'].replace(END, '</section> ' + SECTION + '</div><script>')


def by_id(e, i):
    if isinstance(e, dict):
        if e.get('id') == i:
            return e
        for v in e.values():
            x = by_id(v, i)
            if x:
                return x
    elif isinstance(e, list):
        for v in e:
            x = by_id(v, i)
            if x:
                return x


# reviews heading sat right under the white FAQ with no top padding; it now follows a sand section
rv = by_id(d, '9de2f0a')['settings']
assert rv['html'].count("padding-top:0;padding-bottom:24px") == 1
rv['html'] = rv['html'].replace("padding-top:0;padding-bottom:24px", "padding-top:64px;padding-bottom:24px")
out = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
assert '\\' not in out
open('home_elementor_guides.json', 'w').write(out)
print(len(out))
