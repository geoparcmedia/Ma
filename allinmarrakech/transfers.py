"""Transfer price pages (inter-city now, airport later): one card per route, four group sizes with people icons,
each price books on WhatsApp. Plain HTML, no '$' and no backslashes (pushed through the WordPress tools)."""
from urllib.parse import quote

PERSON = '<svg viewBox="0 0 24 24"><path d="M12 12a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9zm0 2c-4.4 0-8 2.2-8 5v2h16v-2c0-2.8-3.6-5-8-5z"/></svg>'
PIN = '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
CLOCK = '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 3.5 2.1-.8 1.3L11 13V7h2z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24"><path d="m9 16.2-4.2-4.2-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>'
WA_SVG = '<svg viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.9.9 3.9.8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c-.1-.1-.3-.2-.6-.3zM12 21.8a9.9 9.9 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.8L.1 24l6.3-1.7A11.8 11.8 0 0 0 24 12a11.7 11.7 0 0 0-3.6-8.4z"/></svg>'

# group sizes: (label EN, label FR, people icons shown, vehicle EN, vehicle FR)
SIZES = [("1–3", "1–3", 1, "Sedan", "Berline"), ("4–7", "4–7", 2, "Van", "Van"),
         ("8–13", "8–13", 3, "Minibus", "Minibus"), ("14–17", "14–17", 4, "Sprinter", "Sprinter")]

# inter-city routes: (from, to EN, to FR, approx distance, approx drive time, prices for the 4 sizes)
CITY = [
    ("Marrakech", "Casablanca", "Casablanca", "240 km", "2h45", [140, 150, 200, 210]),
    ("Marrakech", "Essaouira", "Essaouira", "190 km", "2h45", [120, 135, 165, 175]),
    ("Marrakech", "Ouarzazate", "Ouarzazate", "200 km", "4h", [165, 180, 205, 220]),
    ("Marrakech", "Zagora", "Zagora", "360 km", "7h", [235, 265, 315, 365]),
    ("Marrakech", "Merzouga", "Merzouga", "560 km", "9h", [335, 365, 465, 515]),
    ("Marrakech", "Rabat", "Rabat", "320 km", "3h30", [235, 265, 325, 365]),
    ("Agadir Airport (AGA)", "Marrakech", "Marrakech", "250 km", "3h", [150, 165, 195, 210]),
]

TXT = {
    "en": dict(h1="Inter-city transfers", sub="Fixed prices per private vehicle, not per person. Pick your route and group size, then book in one tap on WhatsApp.",
               people="people", per="per vehicle", book="Book", one_way="One way", note="Price for the whole private vehicle, one way.",
               inc_h="Always included", inc=["Private air-conditioned vehicle", "Professional driver", "Fuel and tolls", "Pick-up at your hotel or riad", "Luggage included"],
               other="Another route?", other_p="We drive everywhere in Morocco. Tell us your route and we send you a price.", other_b="Ask for a price",
               wa="Hello All in Marrakech, I would like to book a transfer: %s, %s people (%d €)."),
    "fr": dict(h1="Transferts inter-villes", sub="Prix fixes par véhicule privé, pas par personne. Choisissez votre trajet et votre groupe, puis réservez en un clic sur WhatsApp.",
               people="pers.", per="par véhicule", book="Réserver", one_way="Aller simple", note="Prix pour tout le véhicule privé, aller simple.",
               inc_h="Toujours inclus", inc=["Véhicule privé climatisé", "Chauffeur professionnel", "Carburant et péages", "Prise en charge à votre hôtel ou riad", "Bagages inclus"],
               other="Un autre trajet ?", other_p="Nous roulons partout au Maroc. Indiquez-nous votre trajet et nous vous envoyons un prix.", other_b="Demander un prix",
               wa="Bonjour All in Marrakech, je souhaite réserver un transfert : %s, %s personnes (%d €)."),
}


SPRITE = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true">'
          '<symbol id="aim-sp" viewBox="0 0 24 24">' + PERSON[PERSON.index('>') + 1:-6] + '</symbol>'
          '<symbol id="aim-sw" viewBox="0 0 24 24">' + WA_SVG[WA_SVG.index('>') + 1:-6] + '</symbol></svg>')
P_USE = '<svg viewBox="0 0 24 24"><use href="#aim-sp"/></svg>'
W_USE = '<svg viewBox="0 0 24 24"><use href="#aim-sw"/></svg>'


def _wa(text):
    return "https://wa.me/212662667975?text=" + quote(text)


def route_card(lang, frm, to, meta, prices, js=False):
    """frm/to: place names (to may be empty for a single-place service); meta: header extras html."""
    t = TXT[lang]
    label = "%s → %s" % (frm, to) if to else frm
    tiles = ""
    for (en, fr, n, v_en, v_fr), price in zip(SIZES, prices):
        lbl = en if lang == "en" else fr
        tiles += ('<a class="aim-tp" href="%s"' + ('' if js else ' target="_blank" rel="noopener"') + '><span class="aim-tpi">%s</span>'
                  '<span class="aim-tpn">%s %s</span><span class="aim-tpv">%s</span><b>%d €</b><span class="aim-tpb">%s %s</span></a>') % (
            ("https://wa.me/212662667975" if js else _wa(t["wa"] % (label, lbl, price))), ("<i></i>" * n if js else P_USE * n), lbl, t["people"], v_en if lang == "en" else v_fr, price, ("<s></s>" if js else W_USE), t["book"])
    title = ('<span>%s</span><i>→</i><span>%s</span>' % (frm, to)) if to else '<span>%s</span>' % frm
    return ('<div class="aim-tr aim-rv"><div class="aim-trh"><div class="aim-trr">%s</div>'
            '<div class="aim-trm">%s<span>%s</span></div></div><div class="aim-tps">%s</div></div>') % (title, meta, t["one_way"], tiles)


# airport & Marrakech transfers, grouped: (section EN, section FR, [(from FR, to FR, from EN, to EN, prices)])
AIR = [
    ("From Marrakech airport (RAK)", "Depuis l'aéroport de Marrakech (RAK)", [
        ("Aéroport de Marrakech", "Guéliz", "Marrakech Airport", "Guéliz", [29, 31, 48, 60]),
        ("Aéroport de Marrakech", "Médina", "Marrakech Airport", "Medina", [29, 31, 48, 60]),
        ("Aéroport de Marrakech", "Hivernage", "Marrakech Airport", "Hivernage", [29, 31, 48, 60]),
        ("Aéroport de Marrakech", "Centre-ville", "Marrakech Airport", "City centre", [29, 31, 48, 60]),
        ("Aéroport de Marrakech", "Zone touristique Agdal", "Marrakech Airport", "Agdal tourist zone", [30, 33, 48, 60]),
        ("Aéroport de Marrakech", "Targa", "Marrakech Airport", "Targa", [15, 18, 35, 45]),
        ("Aéroport de Marrakech", "Palmeraie (jusqu'à 7 km)", "Marrakech Airport", "Palmeraie (up to 7 km)", [30, 33, 50, 60]),
        ("Aéroport de Marrakech", "Palmeraie (jusqu'à 15 km)", "Marrakech Airport", "Palmeraie (up to 15 km)", [35, 40, 55, 65]),
    ]),
    ("Inside Marrakech", "Dans Marrakech", [
        ("Guéliz ou Médina", "Palmeraie (jusqu'à 7 km)", "Guéliz or Medina", "Palmeraie (up to 7 km)", [29, 31, 50, 60]),
        ("Guéliz ou Médina", "Palmeraie (jusqu'à 15 km)", "Guéliz or Medina", "Palmeraie (up to 15 km)", [29, 35, 50, 65]),
        ("Hôtel centre-ville", "Palmeraie", "City-centre hotel", "Palmeraie", [29, 31, 48, 60]),
        ("Centre-ville", "Spa", "City centre", "Spa", [29, 31, 48, 60]),
        ("Palmeraie", "Spa", "Palmeraie", "Spa", [29, 31, 48, 60]),
        ("Hôtel La Mamounia", "Hôtel Royal Mansour", "La Mamounia hotel", "Royal Mansour hotel", [29, 31, 48, 60]),
        ("Hôtel La Mamounia", "Palais des congrès", "La Mamounia hotel", "Palais des Congrès", [29, 31, 48, 60]),
        ("Hôtel Royal Mansour", "Palais des congrès", "Royal Mansour hotel", "Palais des Congrès", [29, 31, 48, 60]),
    ]),
    ("Garden visits & outer zones", "Visites de jardins & zones", [
        ("Visite du jardin Majorelle", "", "Majorelle Garden visit", "", [29, 31, 48, 60]),
        ("Visite du Jardin Secret", "", "Le Jardin Secret visit", "", [29, 31, 48, 60]),
        ("Visite du jardin Anima", "", "Anima Garden visit", "", [29, 31, 48, 60]),
        ("Visite du jardin Front du Paradis", "", "Front du Paradis garden visit", "", [29, 31, 48, 60]),
        ("Zone route de l'Ourika", "", "Ourika road zone", "", [29, 31, 48, 60]),
        ("Zone route de Fès", "", "Fes road zone", "", [29, 31, 48, 60]),
        ("Zone route d'Agadir", "", "Agadir road zone", "", [29, 31, 48, 60]),
    ]),
]

AIR_TXT = {
    "en": dict(h1="Airport transfers", sub="Marrakech airport and city transfers at fixed prices per private vehicle. Your driver waits for you at arrivals with a name sign.",
               extra=["Flight followed, free waiting time", "Meet & greet with name sign"]),
    "fr": dict(h1="Transferts aéroport", sub="Transferts depuis l'aéroport de Marrakech et dans la ville, à prix fixe par véhicule privé. Votre chauffeur vous attend à l'arrivée avec une pancarte à votre nom.",
               extra=["Vol suivi, attente offerte", "Accueil avec pancarte à votre nom"]),
}


def transfer_page(lang, kind, url, crumbs_home):
    t = TXT[lang]
    inc_list = list(t["inc"])
    if kind == "city":
        h1, sub = t["h1"], t["sub"]
        fr_from = {"Agadir Airport (AGA)": "Aéroport d'Agadir (AGA)"}
        body = '<div class="aim-trs">%s</div>' % "".join(
            route_card(lang, f if lang == "en" else fr_from.get(f, f), to_en if lang == "en" else to_fr,
                       "<span>%s %s</span><span>%s %s</span>" % (PIN, km, CLOCK, d), p)
            for f, to_en, to_fr, km, d, p in CITY)
    else:
        a = AIR_TXT[lang]
        h1, sub = a["h1"], a["sub"]
        inc_list = a["extra"] + inc_list
        chips, body = "", ""
        for n, (sec_en, sec_fr, routes) in enumerate(AIR):
            sec = sec_en if lang == "en" else sec_fr
            chips += '<a href="#aim-air%d">%s</a>' % (n, sec)
            cards = "".join(route_card(lang, fe if lang == "en" else ff, te if lang == "en" else tf, "", p, js=True) for ff, tf, fe, te, p in routes)
            body += '<h2 class="aim-trsh" id="aim-air%d">%s</h2><div class="aim-trs aim-trs2">%s</div>' % (n, sec, cards)
        pre, post = t["wa"].split("%s, %s")
        js = ("<script>(function(){document.querySelectorAll('.aim-trs2 .aim-tp').forEach(function(a){a.addEventListener('click',function(){"
              "var c=a.closest('.aim-tr'),r=[].map.call(c.querySelectorAll('.aim-trr span'),function(x){return x.textContent}).join(' → '),"
              "n=a.querySelector('.aim-tpn').textContent.split(' ')[0],p=a.querySelector('b').textContent;"
              "a.target='_blank';a.rel='noopener';a.href='https://wa.me/212662667975?text='+encodeURIComponent('" + pre.replace("'", "’") + "'+r+', '+n+'" + post.split("(")[0].replace("'", "’") + "('+p+').')})})})();</script>")
        body = '<div class="aim-trchips">%s</div>%s%s' % (chips, body, js)
    inc = "".join("<li>%s %s</li>" % (CHECK, x) for x in inc_list)
    return ('<section class="aim-dhead"><div class="aim-wrap"><div class="aim-crumb"><a href="%s">%s</a> / %s</div><h1>%s</h1><p>%s</p></div></section>'
            '<section class="aim-sec aim-dsec"><div class="aim-wrap">' + (SPRITE if kind == "city" else "") + '%s'
            '<div class="aim-trinfo"><div><h3>%s</h3><ul>%s</ul></div><div class="aim-trother"><h3>%s</h3><p>%s</p>'
            '<a class="aim-btn" href="#book">%s</a></div></div></div></section>') % (
        url("home", lang), crumbs_home, h1, h1, sub, body, t["inc_h"], inc, t["other"], t["other_p"], t["other_b"])


CSS = """/* transfer price pages */
.aim-trs{display:grid;grid-template-columns:1fr;gap:22px}
.aim-tr{background:#fff;border:1px solid var(--aim-line);border-radius:18px;box-shadow:0 8px 28px rgba(40,25,10,.07);overflow:hidden}
.aim-trh{display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap;padding:18px 22px;background:var(--aim-dark);color:#fff}
.aim-trr{display:flex;align-items:center;gap:12px;font-family:"Playfair Display",serif;font-size:22px;font-weight:700}
.aim-trr i{font-style:normal;color:var(--aim-gold);font-family:Poppins,sans-serif}
.aim-trm{display:flex;gap:16px;flex-wrap:wrap;font-size:13.5px;color:#cfc8bf}
.aim-trm span{display:inline-flex;align-items:center;gap:6px}
.aim-trm svg{width:16px;height:16px;fill:var(--aim-gold)}
.aim-tps{display:grid;grid-template-columns:repeat(4,1fr)}
.aim-tp{display:flex;flex-direction:column;align-items:center;text-align:center;gap:4px;padding:20px 12px 18px;border-right:1px solid var(--aim-line);color:var(--aim-ink);transition:background .2s}
.aim-tp:last-child{border-right:0}
.aim-tp:hover{background:var(--aim-sand)}
.aim-tpi{display:flex;gap:1px;height:30px;align-items:flex-end;margin-bottom:4px}
.aim-tpi svg{width:24px;height:24px;fill:var(--aim-red)}
.aim-tpi svg:nth-child(n+2){width:20px;height:20px;opacity:.85}
.aim-tpn{font-weight:700;font-size:15px}
.aim-tpv{font-size:12.5px;color:var(--aim-muted)}
.aim-tp b{font-family:"Playfair Display",serif;font-size:28px;color:var(--aim-red);line-height:1.2;margin:6px 0 8px}
.aim-tpb{display:inline-flex;align-items:center;gap:6px;background:var(--aim-wa);color:#fff;font-size:13.5px;font-weight:600;padding:8px 16px;border-radius:999px}
.aim-tpb svg{width:15px;height:15px;fill:#fff}
.aim-tp:hover .aim-tpb{background:#1ebe5b}
.aim-trinfo{display:grid;grid-template-columns:1.2fr 1fr;gap:22px;margin-top:34px}
.aim-trinfo>div{background:var(--aim-sand);border-radius:18px;padding:26px}
.aim-trinfo h3{margin:0 0 14px;font-size:21px}
.aim-trinfo ul{display:grid;grid-template-columns:1fr 1fr;gap:10px 18px}
.aim-trinfo li{display:flex;align-items:center;gap:8px;font-size:14.5px}
.aim-trinfo li svg{width:18px;height:18px;fill:var(--aim-red);flex:none}
.aim-trother p{color:var(--aim-muted);margin:0 0 16px}
@media (max-width:760px){.aim-tps{grid-template-columns:repeat(2,1fr)}.aim-tp:nth-child(2){border-right:0}.aim-tp:nth-child(-n+2){border-bottom:1px solid var(--aim-line)}
 .aim-trr{font-size:19px}.aim-trh{padding:16px 18px}.aim-tp b{font-size:24px}.aim-trinfo{grid-template-columns:1fr}.aim-trinfo ul{grid-template-columns:1fr}}
/* airport transfers: section chips + 2-column compact cards */
.aim-trchips{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:8px}
.aim-trchips a{padding:10px 18px;border-radius:999px;background:var(--aim-sand);color:var(--aim-ink);font-weight:600;font-size:14px;border:1px solid var(--aim-line)}
.aim-trchips a:hover{background:var(--aim-red);color:#fff;border-color:var(--aim-red)}
.aim-trsh{font-size:26px;margin:38px 0 18px;scroll-margin-top:100px}
.aim-trs2{grid-template-columns:1fr 1fr}
.aim-trs2 .aim-trr{font-size:18px;flex-wrap:wrap;gap:4px 10px}
.aim-trs2 .aim-trh{padding:15px 18px}
.aim-trs2 .aim-tp{padding:16px 6px 14px}
.aim-trs2 .aim-tp b{font-size:24px;margin:4px 0 6px}
.aim-trs2 .aim-tpb{padding:7px 12px;font-size:12.5px}
.aim-trs2 .aim-tpi svg{width:20px;height:20px}
.aim-trs2 .aim-tpi svg:nth-child(n+2){width:16px;height:16px}
@media (max-width:1080px){.aim-trs2{grid-template-columns:1fr}}
.aim-tpi i{display:block;width:20px;height:20px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23970000' d='M12 12a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9zm0 2c-4.4 0-8 2.2-8 5v2h16v-2c0-2.8-3.6-5-8-5z'/%3E%3C/svg%3E") center/contain no-repeat}
.aim-tpi i+i{width:16px;height:16px;opacity:.85}
.aim-tpb s{display:block;width:15px;height:15px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23ffffff' d='M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.9.9 3.9.8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c-.1-.1-.3-.2-.6-.3zM12 21.8a9.9 9.9 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.8L.1 24l6.3-1.7A11.8 11.8 0 0 0 24 12a11.7 11.7 0 0 0-3.6-8.4z'/%3E%3C/svg%3E") center/contain no-repeat}
"""
