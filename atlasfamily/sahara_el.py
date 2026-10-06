"""Sahara Desert Tours (8776) as an Elementor page: full width (no theme sidebar) + other treks grid."""
import json, re
import sahara
from home import container, html, eid

def build():
    full = sahara.page().replace('\n', '')
    full = full.replace('</style>', '.afs{max-width:1240px;margin:0 auto;padding:60px 20px 70px}.afs-cta{margin-top:30px}</style>', 1)
    return [container(eid('sah', 'c1'), [html(eid('sah', 'w1'), full)])]

if __name__ == '__main__':
    s = json.dumps(build(), ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s
    open('sahara_elementor.json', 'w').write(s)
    print(len(s))
