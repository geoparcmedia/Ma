"""Homepage hero: rotating photo slideshow + 'what do you need' search box (EN/FR).
Plain HTML/JS, no '$' and no backslashes (pushed with wp_alter_post)."""
import json
from programs import P, IMG

SLIDES = ["jemaa", "merzouga", "chefchaouen", "agafay"]

TXT = {
    "en": dict(ey="Private tours & transport · Marrakech", h1="Discover Morocco<br><span>your way</span>",
               lead="Desert tours, day trips and airport transfers with your own driver. Tell us what you need, we take care of the rest.",
               tabs=[("tours", "Multi-day tours"), ("days", "Day trips"), ("transfer", "Transfers & driver")],
               dest="Where to?", any_t="All multi-day tours", any_d="All day trips",
               date="Date", pax="Travellers", btn="Search",
               t_from="From", t_to="To", t_from_v=["Marrakech airport (RAK)", "Marrakech hotel / riad", "Casablanca airport (CMN)", "Agadir airport (AGA)", "Other city"],
               t_type="Service", t_types=["Airport transfer", "City-to-city transfer", "Driver for the day", "Group transport (minibus / coach)"],
               t_to_ph="e.g. Riad in the medina, Essaouira...",
               trust=["Local Marrakech team", "Vehicles from 3 to 84 seats", "Reply within a few hours"]),
    "fr": dict(ey="Circuits privés & transport · Marrakech", h1="Découvrez le Maroc<br><span>à votre façon</span>",
               lead="Circuits dans le désert, excursions et transferts aéroport avec votre propre chauffeur. Dites-nous ce dont vous avez besoin, on s'occupe du reste.",
               tabs=[("tours", "Circuits"), ("days", "Excursions"), ("transfer", "Transferts & chauffeur")],
               dest="Où allez-vous ?", any_t="Tous les circuits", any_d="Toutes les excursions",
               date="Date", pax="Voyageurs", btn="Rechercher",
               t_from="Départ", t_to="Arrivée", t_from_v=["Aéroport de Marrakech (RAK)", "Hôtel / riad à Marrakech", "Aéroport de Casablanca (CMN)", "Aéroport d'Agadir (AGA)", "Autre ville"],
               t_type="Service", t_types=["Transfert aéroport", "Transfert entre villes", "Chauffeur à la journée", "Transport de groupe (minibus / autocar)"],
               t_to_ph="ex. Riad dans la médina, Essaouira...",
               trust=["Équipe locale à Marrakech", "Véhicules de 3 à 84 places", "Réponse en quelques heures"]),
}

ICON = {
    "tours": '<svg viewBox="0 0 24 24"><path d="m20.5 3-.2.1L15 5.1 9 3 3.4 4.9a.5.5 0 0 0-.4.5v15.1a.5.5 0 0 0 .7.5L9 18.9l6 2.1 5.6-1.9a.5.5 0 0 0 .4-.5V3.5a.5.5 0 0 0-.5-.5zM15 19l-6-2.1V5l6 2.1z"/></svg>',
    "days": '<svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zM11 1h2v3h-2zm0 19h2v3h-2zM1 11h3v2H1zm19 0h3v2h-3zM4.2 5.6l1.4-1.4 2.1 2.1-1.4 1.4zm12.1 12.1 1.4-1.4 2.1 2.1-1.4 1.4zM4.2 18.4l2.1-2.1 1.4 1.4-2.1 2.1zM16.3 6.3l2.1-2.1 1.4 1.4-2.1 2.1z"/></svg>',
    "transfer": '<svg viewBox="0 0 24 24"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/></svg>',
    "search": '<svg viewBox="0 0 24 24"><path d="M15.5 14h-.8l-.3-.3A6.5 6.5 0 1 0 14 15.5l.3.3v.8l5 5 1.5-1.5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/></svg>',
    "star": '<svg viewBox="0 0 24 24"><path d="M12 17.3 18.2 21l-1.6-7L22 9.2l-7.2-.6L12 2 9.2 8.6 2 9.2 7.5 14l-1.7 7z"/></svg>',
}


def hero(lang, url):
    t = TXT[lang]
    slides = "".join('<img class="aim-sl%s" src="%s" alt="" %s>' % (" on" if i == 0 else "", IMG[k], 'fetchpriority="high"' if i == 0 else 'loading="lazy"')
                     for i, k in enumerate(SLIDES))
    tabs = "".join('<button type="button" class="aim-tab%s" data-tab="%s">%s<span>%s</span></button>' % (" on" if i == 0 else "", k, ICON[k], lbl)
                   for i, (k, lbl) in enumerate(t["tabs"]))

    def opts(kind, any_lbl, any_url):
        o = '<option value="%s">%s</option>' % (any_url, any_lbl)
        for p in P:
            if p["kind"] == kind:
                o += '<option value="%s">%s · %s %d€</option>' % (url(p["key"], lang), p[lang]["title"], "" if True else "", p["price"])
        return o

    def opts_clean(kind, any_lbl, any_url):
        o = '<option value="%s">%s</option>' % (any_url, any_lbl)
        for p in P:
            if p["kind"] == kind:
                o += '<option value="%s">%s</option>' % (url(p["key"], lang), p[lang]["title"])
        return o

    date_f = '<label class="aim-f aim-f-date"><small>%s</small><input type="date" name="d"></label>' % t["date"]
    pax_f = '<label class="aim-f aim-f-pax"><small>%s</small><select name="p">%s</select></label>' % (
        t["pax"], "".join('<option value="%s"%s>%s</option>' % (n, " selected" if n == "2" else "", n) for n in ["1", "2", "3", "4", "5", "6", "7", "8-17", "18+"]))
    btn = '<button type="submit" class="aim-go">%s<span>%s</span></button>' % (ICON["search"], t["btn"])
    pane_t = ('<div class="aim-pane on" data-pane="tours"><label class="aim-f aim-f-dest"><small>%s</small><select name="u">%s</select></label>%s%s%s</div>'
              % (t["dest"], opts_clean("circuit", t["any_t"], url("tours", lang)), date_f, pax_f, btn))
    pane_d = ('<div class="aim-pane" data-pane="days"><label class="aim-f aim-f-dest"><small>%s</small><select name="u">%s</select></label>%s%s%s</div>'
              % (t["dest"], opts_clean("day", t["any_d"], url("days", lang)), date_f, pax_f, btn))
    pane_x = ('<div class="aim-pane" data-pane="transfer"><label class="aim-f"><small>%s</small><select name="s">%s</select></label>'
              '<label class="aim-f"><small>%s</small><select name="f">%s</select></label>'
              '<label class="aim-f aim-f-dest"><small>%s</small><input type="text" name="t" placeholder="%s"></label>%s%s%s</div>'
              % (t["t_type"], "".join("<option>%s</option>" % x for x in t["t_types"]), t["t_from"], "".join("<option>%s</option>" % x for x in t["t_from_v"]),
                 t["t_to"], t["t_to_ph"], date_f, pax_f, btn))
    trust = "".join("<span>%s %s</span>" % (ICON["star"], x) for x in t["trust"])
    js = ("<script>(function(){var h=document.querySelector('.aim-hero2');if(!h)return;"
          "var s=h.querySelectorAll('.aim-sl'),i=0;if(s.length>1)setInterval(function(){s[i].classList.remove('on');i=(i+1)%s.length;s[i].classList.add('on')},6000);"
          "h.querySelectorAll('.aim-tab').forEach(function(b){b.addEventListener('click',function(){"
          "h.querySelectorAll('.aim-tab').forEach(function(x){x.classList.toggle('on',x===b)});"
          "h.querySelectorAll('.aim-pane').forEach(function(p){p.classList.toggle('on',p.getAttribute('data-pane')===b.getAttribute('data-tab'))})})});"
          "h.querySelector('form').addEventListener('submit',function(e){e.preventDefault();var p=h.querySelector('.aim-pane.on'),k=p.getAttribute('data-pane');"
          "var d=p.querySelector('[name=d]').value,n=p.querySelector('[name=p]').value;"
          "if(k==='transfer'){var txt=p.querySelector('[name=s]').value+': '+p.querySelector('[name=f]').value+' > '+(p.querySelector('[name=t]').value||'?');"
          "var f=document.getElementById('aim-trip');if(f)f.value=txt;var dd=document.querySelector('.wpcf7 [name=travel-date]');if(dd&&d)dd.value=d;"
          "var tv=document.querySelector('.wpcf7 [name=travellers]');if(tv)tv.value=parseInt(n)||2;var b=document.getElementById('book');if(b)b.scrollIntoView({behavior:'smooth'});return}"
          "var u=p.querySelector('[name=u]').value;u+=(u.indexOf('?')<0?'?':'&')+'d='+encodeURIComponent(d)+'&p='+encodeURIComponent(n)+'#book';location.href=u})})();</script>")
    return ('<section class="aim-hero aim-hero2"><div class="aim-slides">%s</div><div class="aim-wrap">'
            '<span class="aim-eyebrow">%s</span><h1>%s</h1><p class="aim-lead">%s</p>'
            '<form class="aim-search" autocomplete="off"><div class="aim-tabs">%s</div>%s%s%s</form>'
            '<div class="aim-trust">%s</div></div></section>%s') % (
        slides, t["ey"], t["h1"], t["lead"], tabs, pane_t, pane_d, pane_x, trust, js)


CSS = """
/* hero v2: slideshow + search */
.aim-hero2{min-height:100vh;min-height:100svh;align-items:center;text-align:center}
.aim-hero2:after{background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,.25) 40%,rgba(0,0,0,.35) 65%,rgba(0,0,0,.75) 100%)}
.aim-slides{position:absolute;inset:0}
.aim-slides img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;max-width:none;opacity:0;transform:scale(1.08);transition:opacity 1.6s ease,transform 7s ease}
.aim-slides img.on{opacity:1;transform:scale(1)}
.aim-hero2 .aim-wrap{padding-top:110px;padding-bottom:70px}
.aim-hero2 .aim-eyebrow{display:inline-block;padding:8px 18px;border:1px solid rgba(255,255,255,.45);border-radius:999px;background:rgba(255,255,255,.08);backdrop-filter:blur(6px);color:#fff;letter-spacing:.18em;margin-bottom:22px}
.aim-hero2 h1{max-width:900px;margin:0 auto 18px;font-size:clamp(40px,6.4vw,80px);text-shadow:0 6px 40px rgba(0,0,0,.35)}
.aim-hero2 h1 span{color:var(--aim-gold);font-style:italic}
.aim-hero2 p.aim-lead{margin:0 auto 34px;max-width:680px}
.aim-search{max-width:1060px;margin:0 auto;text-align:left}
.aim-tabs{display:flex;gap:6px;flex-wrap:wrap}
.aim-tab{display:inline-flex;align-items:center;gap:8px;border:0;cursor:pointer;font:inherit;font-size:14.5px;font-weight:600;padding:13px 20px;border-radius:14px 14px 0 0;background:rgba(18,18,18,.55);color:#fff;backdrop-filter:blur(8px);transition:background .2s}
.aim-tab svg{width:18px;height:18px;fill:currentColor}
.aim-tab:hover{background:rgba(18,18,18,.75)}
.aim-tab.on{background:#fff;color:var(--aim-red)}
.aim-pane{display:none;background:#fff;border-radius:0 18px 18px 18px;padding:14px;box-shadow:0 24px 60px rgba(0,0,0,.35);gap:10px;align-items:stretch}
.aim-pane.on{display:flex;flex-wrap:wrap}
.aim-pane[data-pane=transfer] .aim-f{flex:1 1 210px}
.aim-pane[data-pane=transfer] .aim-f-dest{flex:2 1 280px}
.aim-f{flex:1 1 150px;display:flex;flex-direction:column;justify-content:center;gap:2px;padding:8px 14px;border-radius:12px;background:var(--aim-sand);min-width:0}
.aim-f-dest{flex:2.2 1 260px}
.aim-f-pax{flex:.8 1 110px}
.aim-f small{font-size:11.5px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--aim-red)}
.aim-f select,.aim-f input{border:0;background:transparent;font:inherit;font-size:15px;font-weight:500;color:var(--aim-ink);padding:2px 0;width:100%;outline:0;min-width:0}
.aim-go{display:inline-flex;align-items:center;justify-content:center;gap:8px;border:0;cursor:pointer;font:inherit;font-weight:600;font-size:16px;color:#fff;background:var(--aim-red);border-radius:12px;padding:0 28px;min-height:58px;transition:background .2s}
.aim-go:hover{background:var(--aim-red2)}
.aim-go svg{width:20px;height:20px;fill:#fff}
.aim-hero2 .aim-trust{justify-content:center}
@media (max-width:860px){
 .aim-pane.on{flex-direction:column}
 .aim-f,.aim-f-dest,.aim-f-pax,.aim-pane[data-pane=transfer] .aim-f{flex:1 1 auto}
 .aim-go{min-height:54px}
 .aim-tab{padding:11px 14px;font-size:13.5px}
 .aim-hero2 .aim-wrap{padding-top:90px;padding-bottom:50px}
}
@media (max-width:480px){.aim-tab span{display:none}.aim-tab{flex:1;justify-content:center}.aim-tab.on span{display:inline}}
"""
