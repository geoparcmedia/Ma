"""Add an intro text block and a 'Travel guides' section to the Cycling (3493)
and Trekking (498) pages, so the guides get internal links from the main pages.
Reads ../homepage-redesign/{cycling,trekking}_elementor.json (same as live),
writes the updated JSON next to them. The HTML uses single quotes only, so the
JSON carries no backslashes (safe for update_post_meta unslashing)."""
import json

B = 'https://wegravelmorocco.com'
CSS = ("<style>.wgg-in{max-width:860px;margin:0 auto}.wgg-in h2{text-align:center}.wgg-in p{font-size:16.5px}"
       ".wgg-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}.wgg-cards.n3{grid-template-columns:repeat(3,1fr)}"
       ".wgg-card{display:block;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px 22px;color:var(--ink);transition:transform .2s,box-shadow .2s}"
       ".wgg-card:hover{transform:translateY(-4px);box-shadow:0 22px 40px -22px rgba(29,35,48,.4)}"
       ".wgg-card .wgm-eyebrow{font-size:12px;margin-bottom:8px}.wgg-card h3{font-size:18px;margin-bottom:8px}.wgg-card p{font-size:15px;margin:0 0 12px}"
       ".wgg-card span{color:var(--o);font-weight:700;font-size:15px}"
       "@media (max-width:1024px){.wgg-cards,.wgg-cards.n3{grid-template-columns:repeat(2,1fr)}}"
       "@media (max-width:767px){.wgg-cards,.wgg-cards.n3{grid-template-columns:1fr}}</style>")


def card(tag, title, text, url):
    return ("<a class='wgg-card wgm-rv' href='%s%s'><span class='wgm-eyebrow'>%s</span><h3>%s</h3><p>%s</p>"
            "<span>Read the guide &rarr;</span></a>") % (B, url, tag, title, text)


def section(intro_h2, intro_ps, cards):
    n = ' n3' if len(cards) == 3 else ''
    return (CSS + "<section class='wgm-sec' style='padding-top:40px;padding-bottom:56px'><div class='wgm-wrap'><div class='wgg-in'>"
            "<h2>%s</h2>%s</div></div></section>"
            "<section class='wgm-sec wgm-sand' style='padding-top:64px;padding-bottom:64px'><div class='wgm-wrap'>"
            "<div class='wgm-head'><span class='wgm-eyebrow'>Travel guides</span><h2>Plan Your Trip</h2>"
            "<p>Free guides written by our local team to help you choose the right route and season.</p></div>"
            "<div class='wgg-cards%s'>%s</div></div></section>") % (
        intro_h2, ''.join('<p>%s</p>' % p for p in intro_ps), n, ' '.join(cards))


CYCLING = section(
    'Gravel Bike and Cycling Tours in Morocco',
    ["Morocco has thousands of kilometres of quiet dirt roads and old caravan tracks. On our guided bike tours you ride from the "
     "High Atlas to the palm groves of the Draa Valley, over the volcanic Jebel Saghro and to the dunes of the Sahara, with a "
     "4x4 support vehicle behind the group every day.",
     "All our bike tours last 8 days and start and finish in Marrakech, with 30 to 68 km of riding a day. Choose the "
     "<a href='%s/trip/caravan-road-gravel-bike-tour/'>Caravan Road Gravel Bike Tour</a> for pure gravel, the "
     "<a href='%s/trip/morocco-cycling-tour/'>Atlas to Sahara cycling tour</a> for the most riding days, or one of our "
     "hike and bike tours if your group mixes walkers and riders. You can ride a gravel bike, a mountain bike or an e-bike, "
     "your own or rented through us." % (B, B),
     "The best seasons are spring (March to May) and autumn (September to November). Groups are 2 to 16 riders, and every "
     "tour can be booked as a private trip on your own dates."],
    [card('Cycling', 'Gravel Biking in Morocco: The Complete Guide',
          'The best gravel routes, which bike to bring, daily distances and how a guided tour works.', '/cycling-in-morocco-guide/'),
     card('Seasons', 'Best Time to Cycle in Morocco',
          'Month by month: when to ride the Atlas, the south and the desert.', '/best-time-to-visit-morocco-cycling-trekking/'),
     card('Hike &amp; Bike', 'Happy Valley (Ait Bouguemez) Guide',
          'The green valley of the Central Atlas where our Hike and Bike tour starts.', '/happy-valley-ait-bouguemez-hiking-guide/')])

TREKKING = section(
    'Guided Trekking Tours in Morocco',
    ["Our treks are led by licensed local mountain guides from the Atlas. Mules carry the luggage, our team cooks the meals, "
     "and you sleep in Berber guesthouses, mountain refuges or desert camps, so you only carry a small day pack.",
     "Climb <a href='%s/trip/classic-toubkal-mountain-trek/'>Toubkal in 3 days from Marrakech</a> or on the quieter "
     "<a href='%s/trip/climb-mount-toubkal-4167-m-13671-ft/'>6-day Berber villages route</a>, reach the summit of "
     "<a href='%s/trip/climb-mount-mgoun4071m-13356-ft/'>M&rsquo;Goun (4,071 m)</a>, walk village to village in the "
     "<a href='%s/trip/hiking-in-bougmaz-valleykigdom-of-berbers/'>Happy Valley</a>, or trek with camels across the dunes "
     "on our <a href='%s/trip/edge-of-the-sahara-desert-trek/'>Sahara desert trek</a>." % (B, B, B, B, B),
     "Mountain treks run from March to November. Sahara treks run from September to May. "
     "Every trek can also be booked as a private trip on your own dates."],
    [card('Toubkal', 'Climbing Mount Toubkal: The Complete Guide',
          'Routes, difficulty, best season and what to pack for the highest peak in North Africa.', '/mount-toubkal-trek-guide/'),
     card('Sahara', 'Sahara Desert Trek in Morocco',
          'Where treks start, a typical day with camels, the best season and what to pack.', '/sahara-desert-trek-morocco-guide/'),
     card('Happy Valley', 'Hiking the Happy Valley (Ait Bouguemez)',
          'Morocco&rsquo;s Berber heartland: villages, easy hikes and the best time to go.', '/happy-valley-ait-bouguemez-hiking-guide/'),
     card('Seasons', 'Best Time to Trek in Morocco',
          'When to climb the Atlas and when to walk in the desert, month by month.', '/best-time-to-visit-morocco-cycling-trekking/')])

if __name__ == '__main__':
    MARK = "<section class='wgp-cta'>"
    for name, extra in (('cycling', CYCLING), ('trekking', TREKKING)):
        src = '../homepage-redesign/%s_elementor.json' % name
        d = json.load(open(src))
        w = d[0]['elements'][0]['elements'][0]['settings']
        assert w['html'].count(MARK) == 1 and 'wgg-cards' not in w['html']
        w['html'] = w['html'].replace(MARK, extra + MARK)
        out = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
        assert '\\' not in out
        open('%s_elementor_guides.json' % name, 'w').write(out)
        print(name, len(out))
