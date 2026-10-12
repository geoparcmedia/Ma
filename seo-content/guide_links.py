"""Blocks added to the 5 travel guides (posts 4006-4011):
- a 'More guides' block at the end of every guide, linking the other four
- for the Toubkal guide (4007): quick answer, comparison table of our Toubkal
  trips and an FAQ with FAQPage schema (same pattern as the cycling guide).
Prints each block so it can be pasted into wp_alter_post."""
import json

B = 'https://wegravelmorocco.com'
GUIDES = {
    4006: ('/cycling-in-morocco-guide/', 'Gravel Biking in Morocco: The Complete Guide'),
    4007: ('/mount-toubkal-trek-guide/', 'Climbing Mount Toubkal: The Complete Trekking Guide'),
    4008: ('/best-time-to-visit-morocco-cycling-trekking/', 'Best Time to Visit Morocco for Cycling and Trekking'),
    4010: ('/happy-valley-ait-bouguemez-hiking-guide/', 'Hiking the Happy Valley (Ait Bouguemez)'),
    4011: ('/sahara-desert-trek-morocco-guide/', 'Sahara Desert Trek in Morocco'),
}


def more_guides(pid):
    items = ''.join('<li><a href="%s%s">%s</a></li>' % (B, u, t) for k, (u, t) in GUIDES.items() if k != pid)
    return ('<!-- wp:heading -->\n<h2>More Guides From Our Local Team</h2>\n<!-- /wp:heading -->\n\n'
            '<!-- wp:list -->\n<ul>%s</ul>\n<!-- /wp:list -->' % items)


ANSWER = ('<!-- wp:html -->\n<div class="wgm-answer" style="border-left:4px solid #E77717;background:#FAF5EE;padding:16px 20px;'
          'border-radius:8px;margin:0 0 24px"><p style="margin:0"><strong>Quick answer:</strong> Mount Toubkal (4,167 m) is a '
          'non-technical but tough trek. The classic route from Imlil takes 2 to 3 days, with one night at the refuge (about '
          '3,200 m) and an early start for the summit. The best months are April to June and September to October. From '
          'November to March there is snow and ice, and you need crampons, an ice axe and winter experience. Trekkers in the '
          'Toubkal National Park are expected to go with a licensed guide.</p></div>\n<!-- /wp:html -->')

ROWS = [
    ('/trip/classic-toubkal-mountain-trek/', 'Classic Toubkal Trek', '3 days', 'Imlil, the refuge and the summit',
     'Moderate to hard', '380 €'),
    ('/trip/climb-mount-toubkal-4167-m-13671-ft/', 'Climb Mount Toubkal (Berber villages)', '6 days',
     'Tizi Mzik and Aguelzim passes, Tamsoult valley, the summit', 'Moderate to hard', '600 €'),
    ('/trip/toubkal-ascent-essaouira-city-4167-m-13671-ft/', 'Toubkal Trek and Essaouira', '7 days',
     '3-day Toubkal climb, then 2 days in Essaouira', 'Moderate to hard', '680 €'),
    ('/trip/hike-and-bike-morocco-tour/', 'Hike and Bike: Toubkal and Agafay', '8 days',
     '3 days trekking to the summit, 2 days cycling', 'Challenging trek, moderate riding', '1,050 €'),
]
TH = 'padding:10px;text-align:left'
TD = 'padding:10px'
table_rows = ''.join(
    '<tr style="border-bottom:1px solid #eee"><td style="%s"><a href="%s%s">%s</a></td>%s</tr>' % (
        TD, B, u, n, ''.join('<td style="%s">%s</td>' % (TD, c) for c in cells))
    for u, n, *cells in ROWS)
TABLE = ('<!-- wp:heading -->\n<h2>Which Toubkal Trek Should You Choose?</h2>\n<!-- /wp:heading -->\n\n'
         '<!-- wp:paragraph -->\n<p>All four trips start in Marrakech and are led by our local mountain guides. The 3-day trek is the fastest way to the summit; the longer routes give you '
         'more time to acclimatise and quieter trails.</p>\n<!-- /wp:paragraph -->\n\n'
         '<!-- wp:html -->\n<div style="overflow-x:auto;margin:0 0 24px"><table style="width:100%%;min-width:560px;'
         'border-collapse:collapse;font-size:15px"><thead><tr style="background:#313041;color:#fff">'
         '<th style="%s">Trip</th><th style="%s">Duration</th><th style="%s">Route</th><th style="%s">Level</th>'
         '<th style="%s">From</th></tr></thead><tbody>%s</tbody></table></div>\n<!-- /wp:html -->') % (
    TH, TH, TH, TH, TH, table_rows)

FAQ = [
    ('How many days do you need to climb Toubkal?',
     'The classic route from Imlil takes 2 to 3 days: one day up to the refuge (about 3,200 m), an early summit day and the '
     'walk back down. Our Classic Toubkal Trek does it in 3 days from Marrakech. A 5 to 6 day route through Berber villages '
     'gives you more time to acclimatise.'),
    ('Can a beginner climb Mount Toubkal?',
     'Yes, if you have a good basic fitness level and some hiking experience. The summer route is not technical, but the '
     'summit day is long, steep and rocky in places, and the altitude makes it harder. We grade our Toubkal treks moderate '
     'to hard.'),
    ('Do you need a guide to climb Toubkal?',
     'Yes. Trekkers in the Toubkal National Park are expected to be accompanied by a licensed mountain guide. A local guide '
     'also manages the pace and altitude and picks the safest route when the weather changes.'),
    ('What is the best month to climb Toubkal?',
     'April to June and September to October usually have mild temperatures and stable weather. July and August are warmer '
     'and busier. From November to March the summit is covered in snow and ice and needs winter equipment and experience.'),
    ('How much does a guided Toubkal trek cost?',
     'Our 3-day Classic Toubkal Trek starts from 380 € per person, including the guide, mules and muleteers, meals during '
     'the trek, one night in a camp or refuge, one night in a guesthouse and transport from Marrakech. The 6-day route starts '
     'from 600 €.'),
]
faq_html = ''.join('<h3>%s</h3><p>%s</p>' % qa for qa in FAQ)
faq_ld = json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
    {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]},
    ensure_ascii=False, separators=(',', ':'))
FAQ_BLOCK = ('<!-- wp:heading -->\n<h2>Toubkal Trek: Frequently Asked Questions</h2>\n<!-- /wp:heading -->\n\n'
             '<!-- wp:html -->\n<div class="wgm-faq">%s</div>\n<script type="application/ld+json">%s</script>\n'
             '<!-- /wp:html -->') % (faq_html, faq_ld)

if __name__ == '__main__':
    import sys
    what = sys.argv[1]
    if what == 'more':
        print(more_guides(int(sys.argv[2])))
    else:
        print({'answer': ANSWER, 'table': TABLE, 'faq': FAQ_BLOCK}[what])
