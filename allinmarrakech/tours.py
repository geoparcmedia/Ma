"""Tour listing pages (circuits / day trips) with a filter sidebar: destination search, duration, trip type, price range.
Every program is on both pages; each page pre-ticks its own type. Plain HTML/JS, no '$' and no backslashes."""
from programs import P, IMG

PIN = '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
CLOCK = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 3.5 2.1-.8 1.3L11 13V7h2z"/></svg>'

# where each program goes (shown on the card and used by the destination search)
LOC = {
    "chefchaouen": ("Chefchaouen, Rabat, Fes", "Chefchaouen, Rabat, Fès"),
    "merzouga": ("Merzouga, Dades & Todra gorges", "Merzouga, gorges du Dadès & du Todra"),
    "imperial": ("Casablanca, Rabat, Meknes, Fes", "Casablanca, Rabat, Meknès, Fès"),
    "zagora": ("Ouarzazate, Zagora", "Ouarzazate, Zagora"),
    "ouzoud2": ("Ouzoud, Bin El Ouidane", "Ouzoud, Bin El Ouidane"),
    "todra2": ("Ouarzazate, Todra gorge", "Ouarzazate, gorges du Todra"),
    "agafay": ("Agafay desert", "Désert d'Agafay"),
    "gardens": ("Marrakech", "Marrakech"),
    "medina": ("Marrakech medina", "Médina de Marrakech"),
    "ourika": ("Ourika valley", "Vallée de l'Ourika"),
    "imlil": ("Tahanaout, Asni, Imlil", "Tahanaout, Asni, Imlil"),
    "oukaimeden": ("Oukaimeden, High Atlas", "Oukaïmeden, Haut Atlas"),
    "rabat": ("Rabat", "Rabat"),
    "casablanca": ("Casablanca", "Casablanca"),
    "ouarzazate": ("Ouarzazate, Aït Ben Haddou", "Ouarzazate, Aït Ben Haddou"),
    "3valleys": ("Ourika, Imlil, Ouirgane", "Ourika, Imlil, Ouirgane"),
}

TXT = {
    "en": dict(h={"tours": "Multi-day tours", "days": "Day trips"}, crumb="Tours",
               sub={"tours": "Private circuits from Marrakech with your own driver.", "days": "Private day trips from Marrakech, with pick-up at your riad."},
               where="Where to?", where_ph="All destinations", sel="Your filters", clear="Clear filters",
               dur="Duration", durs=[("d1", "1 day or less"), ("d2", "2 to 3 days"), ("d4", "4 days or more")],
               typ="Trip type", types=[("circuit", "Multi-day tour"), ("day", "Day trip")], badge={"circuit": "Circuit", "day": "Day trip"},
               price="Price", reset="Reset", go="Search", found="trips found", none="No trip matches your filters.",
               frm="From", filters="Filters"),
    "fr": dict(h={"tours": "Circuits", "days": "Excursions"}, crumb="Tours",
               sub={"tours": "Circuits privés au départ de Marrakech avec votre propre chauffeur.", "days": "Excursions privées d'une journée depuis Marrakech, avec prise en charge à votre riad."},
               where="Où allez-vous ?", where_ph="Toutes les destinations", sel="Vos filtres", clear="Effacer les filtres",
               dur="Durée", durs=[("d1", "1 jour ou moins"), ("d2", "2 à 3 jours"), ("d4", "4 jours ou plus")],
               typ="Type de voyage", types=[("circuit", "Circuit"), ("day", "Excursion")], badge={"circuit": "Circuit", "day": "Excursion"},
               price="Prix", reset="Réinitialiser", go="Rechercher", found="voyages trouvés", none="Aucun voyage ne correspond à vos filtres.",
               frm="À partir de", filters="Filtres"),
}

PMIN, PMAX = 50, 750


def _days(p):
    if p["kind"] == "circuit":
        return len(p["en"]["days"])
    return 0.5 if p["en"]["dur"].startswith("Half") else 1


def _card(p, lang, url):
    t, c = TXT[lang], p[lang]
    loc = LOC[p["key"]][0 if lang == "en" else 1]
    return ('<a class="aim-tc" href="%s" data-type="%s" data-days="%s" data-price="%d" data-q="%s">'
            '<div class="aim-tci"><img src="%s" alt="%s" loading="lazy" width="600" height="420"></div>'
            '<div class="aim-tcb"><span class="aim-tcl">%s %s</span><h3>%s</h3><span class="aim-tcg aim-tcg-%s">%s</span>'
            '<div class="aim-tcf"><span>%s <b>€%d</b></span><span>%s %s</span></div></div></a>') % (
        url(p["key"], lang), p["kind"], _days(p), p["price"], (loc + " " + c["title"]).lower().replace('"', ""),
        IMG[p["img"]], c["title"], PIN, loc, c["title"], p["kind"], t["badge"][p["kind"]], t["frm"], p["price"], CLOCK, c["dur"].split(" · ")[0])


def tour_list(kind, lang, url, crumbs_home):
    t = TXT[lang]
    own = "circuit" if kind == "tours" else "day"
    items = sorted(P, key=lambda p: (p["kind"] != "circuit", p["price"]))  # same order on both pages; the type filter hides the rest
    durs = "".join('<label><input type="checkbox" name="dur" value="%s"> %s</label>' % d for d in t["durs"])
    types = "".join('<label><input type="checkbox" name="type" value="%s"%s> %s</label>' % (k, " checked" if k == own else "", l) for k, l in t["types"])
    side = ('<details class="aim-flt" open><summary>%s</summary>'
            '<div class="aim-ftop"><h3>%s</h3><label class="aim-fq">%s<input type="search" placeholder="%s" aria-label="%s"></label></div>'
            '<div class="aim-fbox"><div class="aim-fh"><h4>%s</h4><a href="#" class="aim-fclear">%s</a></div></div>'
            '<div class="aim-fbox"><h4>%s</h4>%s</div><div class="aim-fbox"><h4>%s</h4>%s</div>'
            '<div class="aim-fbox"><div class="aim-fh"><h4>%s</h4><a href="#" class="aim-freset">%s</a></div>'
            '<div class="aim-fpr"><label>€<input type="number" class="aim-pmin" value="%d" min="%d" max="%d" step="10"></label>'
            '<label>€<input type="number" class="aim-pmax" value="%d" min="%d" max="%d" step="10"></label></div>'
            '<div class="aim-frg"><span class="aim-frt"></span><input type="range" class="aim-rmin" min="%d" max="%d" step="10" value="%d" aria-label="min">'
            '<input type="range" class="aim-rmax" min="%d" max="%d" step="10" value="%d" aria-label="max"></div>'
            '<button type="button" class="aim-btn aim-fgo">%s</button></div></details>') % (
        t["filters"], t["where"], PIN, t["where_ph"], t["where"], t["sel"], t["clear"], t["dur"], durs, t["typ"], types,
        t["price"], t["reset"], PMIN, PMIN, PMAX, PMAX, PMIN, PMAX, PMIN, PMAX, PMIN, PMIN, PMAX, PMAX, t["go"])
    cards = "".join(_card(p, lang, url) for p in items)
    js = ("<script>(function(){var r=document.getElementById('aim-tl');if(!r)return;"
          "var q=r.querySelector('.aim-fq input'),mn=r.querySelector('.aim-pmin'),mx=r.querySelector('.aim-pmax'),"
          "rn=r.querySelector('.aim-rmin'),rx=r.querySelector('.aim-rmax'),tr=r.querySelector('.aim-frt'),cnt=r.querySelector('.aim-tcount b'),"
          "no=r.querySelector('.aim-tnone'),cards=[].slice.call(r.querySelectorAll('.aim-tc')),boxes=[].slice.call(r.querySelectorAll('.aim-flt input[type=checkbox]')),"
          "own=[].slice.call(r.querySelectorAll('input[name=type]:checked')).map(function(x){return x.value}),lo=" + str(PMIN) + ",hi=" + str(PMAX) + ";"
          "if(window.innerWidth<900)r.querySelector('.aim-flt').removeAttribute('open');"
          "function vals(n){return boxes.filter(function(b){return b.name===n&&b.checked}).map(function(b){return b.value})}"
          "function bar(){var a=(rn.value-lo)/(hi-lo)*100,b=(rx.value-lo)/(hi-lo)*100;tr.style.left=a+'%';tr.style.right=(100-b)+'%'}"
          "function f(){var s=q.value.toLowerCase().trim(),d=vals('dur'),ty=vals('type'),a=+mn.value||lo,b=+mx.value||hi,n=0;"
          "cards.forEach(function(c){var dy=+c.getAttribute('data-days'),p=+c.getAttribute('data-price'),"
          "db=dy<=1?'d1':dy<=3?'d2':'d4',ok=(!s||c.getAttribute('data-q').indexOf(s)>-1)&&(!d.length||d.indexOf(db)>-1)"
          "&&(!ty.length||ty.indexOf(c.getAttribute('data-type'))>-1)&&p>=a&&p<=b;c.style.display=ok?'':'none';if(ok)n++});"
          "cnt.textContent=n;no.hidden=n>0;bar()}"
          "function sync(e){var a=+rn.value,b=+rx.value;if(a>b){if(e.target===rn)rn.value=b;else rx.value=a}mn.value=rn.value;mx.value=rx.value;f()}"
          "rn.addEventListener('input',sync);rx.addEventListener('input',sync);"
          "mn.addEventListener('change',function(){rn.value=mn.value;sync({target:rn})});mx.addEventListener('change',function(){rx.value=mx.value;sync({target:rx})});"
          "q.addEventListener('input',f);boxes.forEach(function(b){b.addEventListener('change',f)});"
          "function rp(){rn.value=mn.value=lo;rx.value=mx.value=hi}"
          "r.querySelector('.aim-freset').addEventListener('click',function(e){e.preventDefault();rp();f()});"
          "r.querySelector('.aim-fclear').addEventListener('click',function(e){e.preventDefault();q.value='';boxes.forEach(function(b){b.checked=false});rp();f()});"
          "r.querySelector('.aim-fgo').addEventListener('click',function(){f();r.querySelector('.aim-tmain').scrollIntoView({behavior:'smooth'})});f()})();</script>")
    return ('<section class="aim-dhead"><div class="aim-wrap"><div class="aim-crumb"><a href="%s">%s</a> / %s / %s</div><h1>%s</h1><p>%s</p></div></section>'
            '<section class="aim-sec aim-dsec" id="aim-tl"><div class="aim-wrap aim-tlay">%s<div class="aim-tmain">'
            '<p class="aim-tcount"><b>0</b> %s</p><div class="aim-tgrid">%s</div><p class="aim-tnone" hidden>%s</p></div></div></section>%s') % (
        url("home", lang), crumbs_home, t["crumb"], t["h"][kind], t["h"][kind], t["sub"][kind], side, t["found"], cards, t["none"], js)


CSS = """/* tour listings with filter sidebar */
.aim-tlay{display:grid;grid-template-columns:290px 1fr;gap:30px;align-items:start}
.aim-flt{background:#fff;border:1px solid var(--aim-line);border-radius:16px;overflow:hidden;position:sticky;top:96px;box-shadow:0 8px 26px rgba(40,25,10,.06)}
.aim-flt summary{display:none}
.aim-ftop{background:var(--aim-red);padding:18px 16px}
.aim-ftop h3{color:#fff;font-size:19px;margin:0 0 12px}
.aim-fq{display:flex;align-items:center;gap:8px;background:#fff;border-radius:10px;padding:0 12px}
.aim-fq svg{width:18px;height:18px;fill:#a39b91;flex:none}
.aim-fq input{border:0;outline:0;font:inherit;font-size:14.5px;padding:12px 0;width:100%;min-width:0;color:var(--aim-ink);background:transparent}
.aim-fbox{padding:16px;border-top:1px solid var(--aim-line)}
.aim-fbox h4{font-size:16px;margin:0 0 10px;color:var(--aim-ink)}
.aim-fh{display:flex;align-items:baseline;justify-content:space-between;gap:10px}
.aim-fh a{font-size:13px;color:#9a9188}
.aim-fh a:hover{color:var(--aim-red)}
.aim-fbox>.aim-fh:only-child h4{margin:0}
.aim-fbox label{display:flex;align-items:center;gap:10px;font-size:14.5px;color:#4d4741;padding:5px 0;cursor:pointer}
.aim-fbox input[type=checkbox]{width:18px;height:18px;accent-color:var(--aim-red);margin:0}
.aim-fpr{display:flex;gap:12px;margin-bottom:16px}
.aim-fpr label{flex:1;gap:6px;font-weight:600;color:var(--aim-ink)}
.aim-fpr input{width:100%;min-width:0;border:0;background:var(--aim-sand);border-radius:10px;padding:10px 12px;font:inherit;font-size:14.5px;color:var(--aim-ink);outline:0}
.aim-frg{position:relative;height:22px;margin:0 9px 18px}
.aim-frg:before{content:"";position:absolute;left:0;right:0;top:9px;height:4px;border-radius:4px;background:#e6dccb}
.aim-frt{position:absolute;top:9px;height:4px;border-radius:4px;background:var(--aim-red)}
.aim-frg input{position:absolute;left:-9px;right:-9px;width:calc(100% + 18px);top:0;margin:0;height:22px;background:none;pointer-events:none;-webkit-appearance:none;appearance:none}
.aim-frg input::-webkit-slider-thumb{-webkit-appearance:none;pointer-events:auto;width:18px;height:18px;border-radius:50%;background:var(--aim-red);border:3px solid #fff;box-shadow:0 0 0 1px var(--aim-red);cursor:pointer}
.aim-frg input::-moz-range-thumb{pointer-events:auto;width:14px;height:14px;border-radius:50%;background:var(--aim-red);border:3px solid #fff;box-shadow:0 0 0 1px var(--aim-red);cursor:pointer}
.aim-frg input::-moz-range-track{background:none}
.aim-fgo{width:100%;justify-content:center}
.aim-tcount{margin:0 0 14px;color:var(--aim-muted);font-size:14.5px}
.aim-tcount b{color:var(--aim-ink)}
.aim-tgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.aim-tc{display:flex;flex-direction:column;background:#fff;border:1px solid var(--aim-line);border-radius:14px;overflow:hidden;color:var(--aim-ink);box-shadow:0 6px 22px rgba(40,25,10,.06);transition:transform .25s,box-shadow .25s}
.aim-tc:hover{transform:translateY(-4px);box-shadow:0 16px 36px rgba(40,25,10,.13)}
.aim-tci{aspect-ratio:10/7;overflow:hidden;background:var(--aim-sand2)}
.aim-tci img{width:100%;height:100%;object-fit:cover;transition:transform .8s}
.aim-tc:hover .aim-tci img{transform:scale(1.06)}
.aim-tcb{display:flex;flex-direction:column;flex:1;padding:14px 16px 0}
.aim-tcl{display:flex;align-items:flex-start;gap:5px;font-size:12.5px;color:#8a8279;line-height:1.4}
.aim-tcl svg{width:14px;height:14px;fill:#a39b91;flex:none;margin-top:1px}
.aim-tc h3{font-size:17px;line-height:1.3;margin:8px 0 10px}
.aim-tcg{align-self:flex-start;font-size:12px;font-weight:700;padding:3px 10px;border-radius:6px;color:#fff;margin-bottom:14px}
.aim-tcg-circuit{background:var(--aim-red)}
.aim-tcg-day{background:var(--aim-gold)}
.aim-tcf{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:10px;border-top:1px solid var(--aim-line);padding:12px 0 14px;font-size:13px;color:#8a8279}
.aim-tcf b{font-size:16px;color:var(--aim-ink)}
.aim-tcf span:first-child{white-space:nowrap}
.aim-tcf span:last-child{display:inline-flex;align-items:center;gap:5px;text-align:right}
.aim-tcf svg{width:14px;height:14px;fill:#a39b91;flex:none}
.aim-tnone{text-align:center;color:var(--aim-muted);padding:50px 0}
@media (max-width:1180px){.aim-tgrid{grid-template-columns:repeat(2,1fr)}}
@media (max-width:900px){.aim-tlay{grid-template-columns:1fr}.aim-flt{position:static}
 .aim-flt summary{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;font-weight:700;cursor:pointer;list-style:none;background:var(--aim-red);color:#fff}
 .aim-flt summary::-webkit-details-marker{display:none}.aim-flt summary:after{content:"+";font-size:20px}.aim-flt[open] summary:after{content:"–"}
 .aim-ftop h3{display:none}}
@media (max-width:560px){.aim-tgrid{grid-template-columns:1fr}}
"""
