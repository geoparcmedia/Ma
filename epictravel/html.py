import json, sys
for pid in sys.argv[1:]:
    d = json.loads(open('out/%s.json' % pid).read())
    for w in d[0]['elements'][1:-1]:
        print('--', w['widgetType'], '--')
        print(w['settings'].get('html') or w['settings'].get('shortcode'))
