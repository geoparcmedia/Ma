import json,re,copy,sys
sys.path.insert(0,'.')
T={}
for m in ['trips_new_a','trips_new_b','trips_new_c']:
    T.update(__import__(m).T)
old=json.load(open('trips_prev.json'))
LBL={'activity level':'Level','level':'Level','level of trek':'Level','accommodation':'Accommodation','drive duration':'Drive','hike duration':'Walking','meals included':'Meals','cycling distance':'Cycling distance','elevation':'Elevation','optional activities':'Optional','included activities':'Included'}
def nv(label,v):
    v=v.replace('&nbsp;',' ').strip().strip('.').strip()
    v=re.sub(r'\s+',' ',v)
    if label=='Elevation':
        v=v.replace('|','/').replace('–','-')
        v=re.sub(r'([+-])\s*',r'\1',v)
        v=re.sub(r'(\d)\s*[mM]\b',r'\1 m',v)
        v=re.sub(r'\s*=\s*[\d,]+\s*Ft','',v)
        v=re.sub(r'\s*/\s*',' / ',v)
        return v
    v=re.sub(r'\b(\d+)\s*[Kk]m\b',r'\1 km',v)
    v=re.sub(r'(\d)[Hh](\d\d)',lambda m:m.group(1)+'h'+m.group(2),v)
    v=re.sub(r'\b(\d)[Hh]\b',r'\1 hours',v)
    v=v.replace(' – ',', ').replace(' - ',', ')
    v=re.sub(r'\bGuest ?[Hh]ouse\b','guesthouse',v)
    w=v.split(' ')
    out=[]
    for i,x in enumerate(w):
        if i>0 and x in('Or','To','And','Hours','Hour','Minutes','Hotel','Riad','Camp','Camping','Guesthouse','Auberge','Kasbah','Luxury','Wild','Similar','Dinner','Lunch','Breakfast','Camel','Ride','In','Desert','City','Tour','Guided','Old','Medina','Village','Summit','Climb'):
            x=x.lower()
        out.append(x)
    v=' '.join(out)
    v=re.sub(r'(?<=\S)(,? )(Lunch|Dinner|Hard|Moderate|Riad|Hotel)\b',lambda m:m.group(1)+m.group(2).lower(),v)
    v={'9h00':'9 hours','6h00':'6 hours','1h30':'1.5 hours','2h30':'2.5 hours','1h00':'1 hour','6h30':'6.5 hours'}.get(v,v)
    v=v[0].upper()+v[1:]
    v=v.replace('Dar armed','Dar Aremd').replace('Armed','Aremd').replace('agafay desert','Agafay desert').replace('marrakech','Marrakech').replace('toubkal','Toubkal').replace('imlil','Imlil').replace('aremd village','Aremd village')
    return v
def facts(html):
    h=re.sub(r'<!--.*?-->','',html).replace('\n',' ')
    pairs=re.findall(r'<strong>\s*([^<:]+?)\s*:?\s*(?:</strong>\s*:?|:\s*</strong>)\s*([^<]*)',h)
    res=[]
    for l,v in pairs:
        k=l.strip().lower().replace('&nbsp;','').strip()
        if k in('note','trip details','tour details','trek details'): continue
        L=LBL.get(k)
        if not L: print('UNK',l); continue
        if v.strip().lower() in('','none'): continue
        if L in('Optional','Included'): continue
        res.append((L,nv(L,v)))
    return res
def P(x): return '<!-- wp:paragraph -->\n<p>'+x+'</p>\n<!-- /wp:paragraph -->'
def UL(items): return '<!-- wp:list -->\n<ul>'+''.join('<li>'+i+'</li>' for i in items)+'</ul>\n<!-- /wp:list -->'
out={}
for id_,t in T.items():
    s=copy.deepcopy(old[str(id_)]['wp_travel_engine_setting'])
    tc='\n\n'.join([P(p) for p in t['ov']]+[P('<strong>Trip details</strong>'),UL(['<strong>%s:</strong> %s'%f for f in t['facts']])])
    s['tab_content']['1_wpeditor']=tc
    s['cost']['includes_title']='What’s included'; s['cost']['excludes_title']='Not included'
    s['cost']['cost_includes']='\n'.join(t['inc']); s['cost']['cost_excludes']='\n'.join(t['exc'])
    s['trip_highlights_title']='Highlights'
    s['trip_highlights']=[{'highlight_text':h} for h in t['hl']]
    s['trip_itinerary_title']='Day-by-day itinerary'
    it=s['itinerary']; assert len(it['itinerary_title'])==len(t['it']),id_
    for k in it['itinerary_title']:
        ti,tx=t['it'][int(k)]
        f=facts(it['itinerary_content'][k])
        it['itinerary_title'][k]=ti
        body=P(tx)
        if f: body+='\n\n'+P('<br>'.join('<strong>%s:</strong> %s'%x for x in f))
        it['itinerary_content'][k]=body
    out[id_]={'title':t['title'],'setting':s}
json.dump(out,open('trips_new.json','w'),ensure_ascii=False)
# show facts sample
for id_ in out:
    for k,v in out[id_]['setting']['itinerary']['itinerary_content'].items():
        m=re.findall(r'<p>(<strong>.*?)</p>',v)
        if m: print(id_,k,m[-1].replace('<strong>','').replace('</strong>','').replace('<br>',' | '))
