"""Destinations page: searchable, sortable grid of places; clicking one lists the tours and day trips that visit it.
Plain HTML/JS, no '$' and no backslashes (pushed through the WordPress tools)."""
from programs import P, IMG

# (key, EN name, FR name, image key, program keys that visit the place)
DEST = [
    ("agafay", "Agafay", "Agafay", "agafay", ["agafay"]),
    ("casablanca", "Casablanca", "Casablanca", "casablanca", ["casablanca", "chefchaouen", "imperial"]),
    ("chefchaouen", "Chefchaouen", "Chefchaouen", "chefchaouen", ["chefchaouen"]),
    ("dades", "Dades Gorges", "Gorges du Dadès", "dades", ["merzouga"]),
    ("fes", "Fes", "Fès", "fes", ["chefchaouen", "imperial"]),
    ("imlil", "Imlil & Asni", "Imlil & Asni", "imlil", ["imlil", "3valleys"]),
    ("marrakech", "Marrakech", "Marrakech", "koutoubia", ["medina", "gardens"]),
    ("merzouga", "Merzouga", "Merzouga", "merzouga", ["merzouga"]),
    ("ouarzazate", "Ouarzazate & Aït Ben Haddou", "Ouarzazate & Aït Ben Haddou", "aitbenhaddou", ["ouarzazate", "zagora", "todra2", "merzouga"]),
    ("oukaimeden", "Oukaimeden", "Oukaïmeden", "oukaimeden", ["oukaimeden"]),
    ("ourika", "Ourika Valley", "Vallée de l'Ourika", "ourika", ["ourika", "3valleys"]),
    ("ouzoud", "Ouzoud & Bin El Ouidane", "Ouzoud & Bin El Ouidane", "ouzoud", ["ouzoud2"]),
    ("rabat", "Rabat", "Rabat", "rabat", ["rabat", "chefchaouen", "imperial"]),
    ("todra", "Todra Gorge", "Gorges du Todra", "todra", ["todra2", "merzouga"]),
    ("zagora", "Zagora", "Zagora", "zagora", ["zagora"]),
]

TXT = {
    "en": dict(h1="Destinations", sub="Choose a destination and see the tours and day trips that go there.",
               search="Search a city or place", sort="Sort by", az="A to Z", za="Z to A", most="Most trips",
               one="1 tour or day trip", many="%d tours & day trips", none="No destination found.",
               trips="Tours & day trips to", back="Back to destinations"),
    "fr": dict(h1="Destinations", sub="Choisissez une destination et découvrez les circuits et excursions qui s'y rendent.",
               search="Rechercher une ville ou un lieu", sort="Trier par", az="De A à Z", za="De Z à A", most="Le plus de voyages",
               one="1 circuit ou excursion", many="%d circuits et excursions", none="Aucune destination trouvée.",
               trips="Circuits et excursions :", back="Retour aux destinations"),
}

JS = ("<script>(function(){var r=document.getElementById('aim-dest');if(!r)return;"
      "var g=r.querySelector('.aim-dgrid'),q=r.querySelector('.aim-dq'),s=r.querySelector('.aim-ds'),no=r.querySelector('.aim-dnone'),"
      "box=document.getElementById('aim-dtrips'),ttl=box.querySelector('.aim-dtt'),trips=[].slice.call(box.querySelectorAll('[data-k]')),cards=[].slice.call(g.children);"
      "function f(){var v=q.value.toLowerCase().trim(),n=0;cards.forEach(function(c){var ok=!v||c.getAttribute('data-name').indexOf(v)>-1;c.style.display=ok?'':'none';if(ok)n++});no.hidden=n>0}"
      "function o(){var m=s.value;cards.sort(function(a,b){if(m==='n')return b.getAttribute('data-n')-a.getAttribute('data-n');"
      "var x=a.getAttribute('data-name'),y=b.getAttribute('data-name');return m==='za'?y.localeCompare(x):x.localeCompare(y)});cards.forEach(function(c){g.appendChild(c)})}"
      "function show(k,scroll){var c=r.querySelector('.aim-dcard[data-dest=\"'+k+'\"]');if(!c)return;var ks=c.getAttribute('data-trips').split(' ');"
      "trips.forEach(function(t){t.style.display=ks.indexOf(t.getAttribute('data-k'))>-1?'':'none'});ttl.textContent=c.querySelector('h3').textContent;"
      "box.hidden=false;cards.forEach(function(x){x.classList.toggle('on',x===c)});if(scroll)box.scrollIntoView({behavior:'smooth'})}"
      "q.addEventListener('input',f);s.addEventListener('change',o);"
      "cards.forEach(function(c){c.addEventListener('click',function(e){e.preventDefault();var k=c.getAttribute('data-dest');history.replaceState(null,'','#'+k);show(k,true)})});"
      "box.querySelector('.aim-dback').addEventListener('click',function(e){e.preventDefault();box.hidden=true;cards.forEach(function(c){c.classList.remove('on')});r.scrollIntoView({behavior:'smooth'})});"
      "var h=location.hash.slice(1);if(h)show(h,true)})();</script>")


def destinations(lang, url, card, crumbs_home):
    t = TXT[lang]
    tiles = ""
    for key, en, fr, img, progs in DEST:
        name = en if lang == "en" else fr
        n = len(progs)
        tiles += ('<a class="aim-dcard" href="#%s" data-dest="%s" data-name="%s" data-n="%d" data-trips="%s"><div class="aim-dimg"><img src="%s" alt="%s" loading="lazy" width="600" height="760"></div>'
                  '<h3>%s</h3><span>%s</span></a>') % (key, key, name.lower(), n, " ".join(progs), IMG[img], name, name, t["one"] if n == 1 else t["many"] % n)
    pool = "".join(card(p, lang).replace('<a class="aim-card aim-rv"', '<a class="aim-card" data-k="%s"' % p["key"], 1) for p in P)
    body = ('<section class="aim-dhead"><div class="aim-wrap"><div class="aim-crumb"><a href="%s">%s</a> / %s</div><h1>%s</h1><p>%s</p></div></section>'
            '<section class="aim-sec aim-dsec" id="aim-dest"><div class="aim-wrap">'
            '<div class="aim-dbar"><input class="aim-dq" type="search" placeholder="%s" aria-label="%s">'
            '<label class="aim-dsort"><span>%s</span><select class="aim-ds"><option value="az">%s</option><option value="za">%s</option><option value="n">%s</option></select></label></div>'
            '<div class="aim-dgrid">%s</div><p class="aim-dnone" hidden>%s</p></div></section>'
            '<section class="aim-sec aim-sand" id="aim-dtrips" hidden><div class="aim-wrap"><div class="aim-dgh"><h2>%s <span class="aim-dtt"></span></h2>'
            '<a class="aim-dback" href="#">← %s</a></div><div class="aim-grid">%s</div></div></section>%s') % (
        url("home", lang), crumbs_home, t["h1"], t["h1"], t["sub"],
        t["search"], t["search"], t["sort"], t["az"], t["za"], t["most"], tiles, t["none"], t["trips"], t["back"], pool, JS)
    return body


CSS = """/* destinations page */
.aim-dhead{padding:60px 0 26px;background:#fff}
.aim-dhead .aim-crumb{color:#8a8279;font-size:13.5px;margin-bottom:14px}
.aim-dhead .aim-crumb a{color:var(--aim-red)}
.aim-dhead h1{font-size:clamp(34px,4.6vw,52px);margin:0 0 8px;color:var(--aim-ink)}
.aim-dhead p{color:var(--aim-muted);margin:0;max-width:640px}
.aim-dsec{padding-top:10px}
.aim-dbar{display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;background:var(--aim-sand);border-radius:16px;padding:12px;margin-bottom:30px}
.aim-dq{flex:0 1 420px;min-width:0;border:1.5px solid transparent;background:#fff;border-radius:12px;padding:13px 16px;font:inherit;font-size:15px;color:var(--aim-ink);outline:0}
.aim-dq:focus{border-color:var(--aim-red)}
.aim-dsort{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--aim-muted)}
.aim-ds{border:1.5px solid transparent;background:#fff;border-radius:12px;padding:12px 14px;font:inherit;font-size:14.5px;color:var(--aim-ink);cursor:pointer;outline:0}
.aim-ds:focus{border-color:var(--aim-red)}
.aim-dgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 22px}
.aim-dcard{display:block;color:var(--aim-ink);cursor:pointer}
.aim-dimg{aspect-ratio:3/4;border-radius:14px;overflow:hidden;background:var(--aim-sand2);box-shadow:0 8px 24px rgba(40,25,10,.1);border:2px solid transparent;transition:border-color .2s,box-shadow .3s}
.aim-dimg img{width:100%;height:100%;object-fit:cover;transition:transform .8s}
.aim-dcard:hover .aim-dimg img{transform:scale(1.06)}
.aim-dcard:hover .aim-dimg{box-shadow:0 16px 36px rgba(40,25,10,.18)}
.aim-dcard.on .aim-dimg{border-color:var(--aim-red)}
.aim-dcard h3{font-size:19px;margin:14px 0 2px;color:var(--aim-ink)}
.aim-dcard span{font-size:13.5px;color:var(--aim-muted)}
.aim-dnone{text-align:center;color:var(--aim-muted);padding:40px 0}
.aim-dgh{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-bottom:28px}
.aim-dgh h2{margin:0}
.aim-dback{font-weight:600;color:var(--aim-red)}
@media (max-width:1080px){.aim-dgrid{grid-template-columns:repeat(3,1fr)}}
@media (max-width:760px){.aim-dgrid{grid-template-columns:repeat(2,1fr);gap:20px 14px}.aim-dhead{padding:40px 0 18px}.aim-dq{flex:1 1 100%}.aim-dsort{width:100%;justify-content:space-between}.aim-dcard h3{font-size:16px}}
"""
