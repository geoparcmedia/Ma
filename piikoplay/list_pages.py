"""Builds three 'best X games' list pages for piikoplay.com in the same block
format as /best-car-games/. Every game blurb only uses facts from that game's
own page on the site. Writes <slug>.html next to this file."""
B = 'https://piikoplay.com'


def P(t):
    return '<!-- wp:paragraph -->\n<p>%s</p>\n<!-- /wp:paragraph -->' % t


def H2(t):
    return '<!-- wp:heading -->\n<h2 class="wp-block-heading">%s</h2>\n<!-- /wp:heading -->' % t


def H3(t):
    return '<!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">%s</h3>\n<!-- /wp:heading -->' % t


def GAME(slug, name, text):
    return H3('<a href="%s/%s/">%s</a>' % (B, slug, name)) + '\n\n' + P(text)


def UL(items):
    return ('<!-- wp:list -->\n<ul class="wp-block-list">\n' +
            '\n'.join('<!-- wp:list-item -->\n<li>%s</li>\n<!-- /wp:list-item -->' % i for i in items) +
            '\n</ul>\n<!-- /wp:list -->')


def FAQ(qas):
    out = [H2('Frequently asked questions')]
    for q, a in qas:
        out += [H3(q), P(a)]
    return out


def page(blocks):
    return '\n\n'.join(blocks)


MORE = ('More lists: the <a href="%s/best-car-games/">best car games</a>, the <a href="%s/best-obby-games/">best obby games</a>, '
        'the <a href="%s/best-shooting-games/">best shooting games</a> or all <a href="%s/new-games/">new games</a>.') % (B, B, B, B)

PAGES = {}

PAGES['best-survival-games'] = dict(
    title='Best Survival Games to Play Online for Free',
    excerpt='The best free survival games to play online: forest nights, zombie hordes, alien waves and sandbox crafting. No download, in your browser.',
    seo_title='Best Survival Games 2026 – Play Free Online, No Download - PiikoPlay',
    seo_desc='Play the best free survival games online: survive 99 nights in the forest, ride a zombie train, hold the barricade and craft in a sandbox world. Instant play.',
    kw='survival games,free survival games online,survival games online free',
    body=page([
        P('Gather what you can, build defenses and try to last one more night. Survival games are about staying alive when '
          'everything is trying to stop you. Here is our selection of the <strong>best survival games to play online for free</strong> '
          'on PiikoPlay. They all run instantly in your browser, with no download and no sign-up.'),
        P('To see every game of this type, open the full <a href="%s/category/survival/">Survival Games</a> category.' % B),
        H2('Best day and night survival games'),
        GAME('99-nights-in-the-forest', '99 Nights In The Forest',
             'Explore the forest and collect food and materials by day, then build shelters and keep your campfire burning before '
             'night falls. Animals and enemies get stronger every night, and the goal is to last all 99.'),
        GAME('sandbox-world-builder-3d', 'Sandbox World Builder 3D',
             'A calmer kind of survival: explore an open 3D world, gather wood, ore and fruit, build shops, craft weapons and fight '
             'monsters at your own pace.'),
        H2('Best zombie survival games'),
        GAME('dead-rails', 'Dead Rails',
             'A virus has turned the Wild West into a zombie wasteland. Ride an armored train, raid abandoned towns for fuel and gear, '
             'upgrade your weapons and fight your way to the last station.'),
        GAME('tiny-zomby-the-barricade', 'Tiny Zomby The Barricade',
             'Hold the barricade from your watchtower, plant mines and survive six stages of zombie waves. A good pick if you like '
             'defense games.'),
        GAME('zombie-shooter-evil-outbreak', 'Zombie Shooter: Evil Outbreak',
             'A 3D survival horror shooter where you clear five zombie-infested locations with six weapons.'),
        H2('Best sci-fi and action survival games'),
        GAME('project-void', 'Project VOID',
             'Survive waves of alien drones, collect Void Skulls and upgrade between rounds in this sci-fi roguelike.'),
        GAME('doomfront-iron-breach', 'Doomfront Iron Breach',
             'A sci-fi first-person shooter: blast through five sectors, from bunkers to a spaceport, with five weapons.'),
        GAME('countercraft-nether-strike', 'Countercraft Nether Strike',
             'A blocky 3D shooter where you fight mobs with six weapons and set off TNT chain reactions across five sectors.'),
        H2('How to choose a survival game'),
        UL(['<strong>Like building and planning?</strong> Start with 99 Nights In The Forest or Sandbox World Builder 3D.',
            '<strong>Want to fight zombies?</strong> Try Dead Rails, Tiny Zomby The Barricade or Zombie Shooter: Evil Outbreak.',
            '<strong>Prefer fast action?</strong> Project VOID, Doomfront Iron Breach and Countercraft Nether Strike are all about combat.',
            '<strong>Short on time?</strong> Wave-based games like Project VOID and Tiny Zomby are easy to play in short sessions.']),
    ] + FAQ([
        ('Are these survival games free?',
         'Yes. All survival games on PiikoPlay are free and run in your browser without any download or account.'),
        ('Which survival game is the hardest?',
         '99 Nights In The Forest gets harder every night, so surviving all 99 nights is a real challenge.'),
        ('Do I need to install anything?',
         'No. Every game opens straight in your browser. Each game page lists its exact controls.'),
    ]) + [P(MORE)]))

PAGES['best-horror-games'] = dict(
    title='Best Horror Games to Play Online for Free',
    excerpt='The best free horror games to play online: night shifts, haunted houses, creepy villages and zombie outbreaks. No download, in your browser.',
    seo_title='Best Horror Games 2026 – Play Free Online, No Download - PiikoPlay',
    seo_desc='Play the best free horror games online: guard the door in Night Shift at Block 13, escape Granny Horror Village, run a haunted house and fight zombies. Instant play.',
    kw='horror games,free horror games online,scary games online',
    body=page([
        P('Dark corridors, strange visitors and things that move when you are not looking. Here is our selection of the '
          '<strong>best horror games to play online for free</strong> on PiikoPlay, from tense escape games to spooky games that '
          'are more fun than frightening. Every game runs in your browser with no download and no sign-up.'),
        P('To see every scary game on the site, open the full <a href="%s/category/horror/">Horror Games</a> category.' % B),
        H2('Best scary horror games'),
        GAME('night-shift-at-block-13', 'Night Shift at Block 13',
             'You are the night guard. Check every visitor\'s papers and keep the shapeshifters out for seven nights.'),
        GAME('granny-horror-village', 'Granny Horror Village',
             'Explore a dark village in first person, solve puzzles and find a way out. A classic horror escape game.'),
        GAME('zombie-shooter-evil-outbreak', 'Zombie Shooter: Evil Outbreak',
             'Survival horror with a gun in your hands: clear five zombie-infested locations using six weapons.'),
        H2('Best spooky games for younger players'),
        GAME('haunted-house-idle', 'Haunted House Idle',
             'Build and run your own haunted house attraction, scare visitors and expand your empire. Spooky, but relaxed.'),
        GAME('rainbow-friends-hide-and-seek', 'Rainbow Friends Hide And Seek',
             'Choose to hide or seek in a colorful rainbow world and outsmart the other side.'),
        H2('Creepy survival games'),
        GAME('99-nights-in-the-forest', '99 Nights In The Forest',
             'Every night in the forest is more dangerous than the last. Prepare by day and survive the dark.'),
        GAME('dead-rails', 'Dead Rails',
             'Ride an armored train through a zombie-filled Wild West and fight your way to the last station.'),
        H2('How to choose a horror game'),
        UL(['<strong>Want real tension?</strong> Night Shift at Block 13 and Granny Horror Village are the scariest picks.',
            '<strong>Prefer action?</strong> Zombie Shooter: Evil Outbreak lets you fight back.',
            '<strong>Playing with kids?</strong> Haunted House Idle and Rainbow Friends Hide And Seek are spooky without being too scary.',
            '<strong>Like survival?</strong> 99 Nights In The Forest and Dead Rails mix horror with building and looting.']),
    ] + FAQ([
        ('Are these horror games free?',
         'Yes. All horror games on PiikoPlay are free to play in your browser, with no download or account.'),
        ('Which horror game is the scariest?',
         'Night Shift at Block 13 and Granny Horror Village are the most tense. Haunted House Idle and Rainbow Friends Hide And Seek are much lighter.'),
        ('Do I need to download anything?',
         'No. Every game opens straight in your browser. Each game page lists its exact controls.'),
    ]) + [P(MORE)]))

PAGES['best-simulator-games'] = dict(
    title='Best Simulator Games to Play Online for Free',
    excerpt='The best free simulator games to play online: bus, taxi, forklift and motorcycle driving, drone flying, car washing and life sims. No download.',
    seo_title='Best Simulator Games 2026 – Play Free Online, No Download - PiikoPlay',
    seo_desc='Play the best free simulator games online: drive a city bus or taxi, deliver parcels on a motorcycle, fly a drone, wash cars and live a virtual life. Instant play.',
    kw='simulator games,free simulator games online,driving simulator games',
    body=page([
        P('Drive a bus, run deliveries, fly a drone or build a new life in a virtual city. Simulator games let you try jobs and '
          'vehicles you do not get to use every day. Here is our selection of the <strong>best simulator games to play online for '
          'free</strong> on PiikoPlay. Every game runs instantly in your browser, with no download and no sign-up.'),
        P('To see them all, open the full <a href="%s/category/simulation/">Simulation Games</a> category.' % B),
        H2('Best driving simulator games'),
        GAME('city-bus-simulator-driving-games', 'City Bus Simulator Driving Games',
             'Drive a city bus, pick up passengers and park at every stop. A steady, satisfying driving sim.'),
        GAME('city-taxi-driving-simulator', 'City Taxi Driving Simulator',
             'Pick up passengers and drive them across the 3D city before the timer runs out.'),
        GAME('city-rescue-forklift-simulator', 'City Rescue Forklift Simulator',
             'Drive a rescue forklift through the city, pick up wrecked cars and deliver them before time runs out across ten missions.'),
        H2('Best bike and motorcycle simulators'),
        GAME('extreme-motorcycle-simulator', 'Extreme Motorcycle Simulator',
             'Ride powerful motorcycles through an open 3D city, complete missions or just explore freely.'),
        GAME('city-delivery-rider-simulator', 'City Delivery Rider Simulator',
             'Deliver parcels across a busy city on a motorcycle and reach every customer before time runs out.'),
        H2('Best flying and job simulators'),
        GAME('drone-vs-tractor-challenge', 'Drone vs Tractor Challenge',
             'Fly a drone around a 3D farm, dodge the tractors and complete tricky flying missions.'),
        GAME('super-car-wash-3d', 'Super Car Wash 3D',
             'Rinse, soap, scrub and polish muddy cars until they shine. One of the most relaxing games on the site.'),
        H2('Best life and sandbox simulators'),
        GAME('brookhaven-real-life', 'Brookhaven Real Life',
             'Create your character, design your home and explore a colorful city at your own pace.'),
        GAME('sandbox-world-builder-3d', 'Sandbox World Builder 3D',
             'Explore an open world, gather resources, build shops and craft weapons in this 3D sandbox.'),
        H2('How to choose a simulator game'),
        UL(['<strong>Like driving?</strong> Start with the bus, taxi or forklift simulators.',
            '<strong>Prefer two wheels?</strong> Try Extreme Motorcycle Simulator or City Delivery Rider Simulator.',
            '<strong>Want to relax?</strong> Super Car Wash 3D and Brookhaven Real Life are the calmest picks.',
            '<strong>Like a challenge?</strong> The timed taxi, forklift and delivery missions keep you on the clock.']),
    ] + FAQ([
        ('Are these simulator games free?',
         'Yes. All simulator games on PiikoPlay are free and run in your browser without any download or account.'),
        ('What is the most relaxing simulator?',
         'Super Car Wash 3D is one of the most relaxing games on the site, and in Brookhaven Real Life you explore the city at your own pace.'),
        ('Where can I find the controls?',
         'Every game page has a Controls section with the exact keys or buttons for that game.'),
    ]) + [P(MORE)]))

if __name__ == '__main__':
    import json
    for slug, p in PAGES.items():
        open('%s.html' % slug, 'w').write(p['body'])
    json.dump({k: {x: v for x, v in p.items() if x != 'body'} for k, p in PAGES.items()},
              open('list_pages_meta.json', 'w'), indent=1, ensure_ascii=False)
    print({k: len(p['body']) for k, p in PAGES.items()})
