import json,sys
def load(p):
    d=json.load(open(p))
    while isinstance(d,str): d=json.loads(d)
    return d
def walk(e,depth=0):
    s=e.get('settings',{})
    if not isinstance(s,dict): s={}
    wt=e.get('widgetType',e.get('elType'))
    info=[]
    for k,v in s.items():
        if isinstance(v,dict) and v.get('url'): info.append(f"{k}={v['url']}")
        elif isinstance(v,str) and v and any(x in k for x in('title','link','editor','html','text','heading','shortcode','description')) and not k.startswith(('premium_tooltip','element_pack','_ob')): info.append(f"{k}={v[:150]!r}")
    print('  '*depth+wt, ' | '.join(info)[:500])
    for c in e.get('elements',[]): walk(c,depth+1)
if __name__=='__main__':
    for e in load(sys.argv[1]): walk(e)
