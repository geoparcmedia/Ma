"""Generates every page of the new allinmarrakech.com (EN + FR).

Each page is stored as one Custom HTML block (post_content) on the Elementor
Canvas template; the shared CSS (style.css) lives in Appearance > Customize >
Additional CSS. Run: python3 site.py  -> writes out/<slug>.html
"""
import json
import os
import re
from urllib.parse import quote

from programs import P, IMG, CREDITS
from dest import destinations
from transfers import transfer_page
from tours import tour_list
from hero import hero as hero_v2

SITE = "https://allinmarrakech.com/"
LOGO = SITE + "wp-content/uploads/2025/07/ChatGPT-Image-16-mai-2026-14_57_58.png"
PHONE = "+212 662 667 975"
TEL = "+212662667975"
WA = "212662667975"
EMAIL = "allinmarrakechtravel@gmail.com"
FORM = {"en": 1909, "fr": 1910}
UP = SITE + "wp-content/uploads/2026/05/"
VEH = [  # (key, name, seats, bags, image, en note, fr note)
    ("e", "Mercedes E-Class", "3", "2", UP + "Gemini_Generated_Image_gkvc6sgkvc6sgkvc.png",
     "Executive sedan for business and airport transfers.", "Berline de prestige pour les transferts d'affaires et aéroport."),
    ("rr", "Range Rover Vogue", "4", "3", UP + "WhatsApp-Image-2026-05-15-at-7.54.33-PM-e1778950141788.jpeg",
     "Luxury 4x4 for VIP transfers and weddings.", "4x4 de luxe pour transferts VIP et mariages."),
    ("tg", "Volkswagen Touareg", "4", "3", UP + "WhatsApp-Image-2026-05-15-at-8.01.44-PM-1-e1778950066957.jpeg",
     "Premium SUV for private tours and transfers.", "SUV premium pour circuits privés et transferts."),
    ("sk", "Skoda 4x4", "4", "3", UP + "Gemini_Generated_Image_ifukrnifukrnifuk.png",
     "Comfortable 4x4 for the Atlas and desert roads.", "4x4 confortable pour les routes de l'Atlas et du désert."),
    ("v", "Mercedes V-Class", "7", "6", UP + "Gemini_Generated_Image_3thgsl3thgsl3thg.png",
     "Luxury van for families and small groups.", "Van de luxe pour familles et petits groupes."),
    ("sp", "Mercedes Sprinter", "17–18", "15", UP + "pp.png",
     "Minibus for groups, excursions and events.", "Minibus pour groupes, excursions et événements."),
    ("bus", "Tourist coach", "40–84", "XL", UP + "Gemini_Generated_Image_dr180udr180udr18.png",
     "Coaches for large groups, congresses and school trips.", "Autocars pour grands groupes, congrès et voyages scolaires."),
]

# page slugs per language (EN home is the front page)
SLUG = {
    "home": {"en": "", "fr": "fr"},
    "tours": {"en": "morocco-tours", "fr": "circuits-maroc"},
    "days": {"en": "day-trips-from-marrakech", "fr": "excursions-marrakech"},
    "fleet": {"en": "transfers-and-fleet", "fr": "transferts-et-flotte"},
    "dest": {"en": "destinations", "fr": "destinations-maroc"},
    "city": {"en": "inter-city-transfers", "fr": "transferts-inter-villes"},
    "air": {"en": "airport-transfers", "fr": "transferts-aeroport"},
    "about": {"en": "about-us", "fr": "a-propos"},
    "contact": {"en": "contact-us", "fr": "contactez-nous"},
}
for p in P:
    SLUG[p["key"]] = {"en": p["en"]["slug"], "fr": p["fr"]["slug"]}


def url(key, lang):
    s = SLUG[key][lang]
    return SITE if s == "" else SITE + "?pagename=" + s


T = {
    "en": dict(nav=[("home", "Home"), ("dest", "Destinations"), ("tours", "Tours"), ("fleet", "Transfers"), ("about", "About"), ("contact", "Contact")],
               book="Book now", from_="From", per="per private vehicle", more="View details", wa_msg="Hello All in Marrakech, I would like information about: ",
               tagline="Tourist transport, airport transfers and private tours in Morocco, from Marrakech.", fleet_h="Our fleet", seats="seats",
               cm_h="How would you like to contact us?", cm_p="Choose what is easiest for you. We usually reply within a few hours.", cm_wa="Fastest reply", cm_form="Or fill in our booking form",
               links="Explore", info="Contact", follow="Our services", rights="All rights reserved.", photos="Destination photos: Wikimedia Commons",
               svc=["Airport transfers", "Private tours", "Day trips", "Group transport", "Weddings & events"],
               days_lbl="Day", hl="Highlights", itin="Itinerary", inc="Included", exc="Not included", req="Request this trip", wa_btn="Ask on WhatsApp",
               dur="Duration", dep="Departure", dep_v="Marrakech, from your hotel or riad", grp="Group size", grp_v="Private, 1 to 84 people",
               pnote="Prices are per private vehicle with driver, not per person. Bigger group? Ask us for a quote.",
               ptab="Price table", ptab_p="One price for the whole vehicle, driver and fuel included. Pick the size that fits your group.", ptab_book="Book",
               tiers=[("Comfort minibus", "4"), ("Standard minibus", "7"), ("Group minibus", "14"), ("Large minibus", "17"), ("Comfort coach", "29"), ("Premium coach", "48")],
               inc_l=["Private air-conditioned vehicle", "Professional driver", "Fuel and tolls", "Pick-up and drop-off at your hotel or riad in Marrakech"],
               exc_l=["Accommodation (we can book it for you)", "Meals and drinks", "Entrance tickets and local guides", "Optional activities (camel, quad, boat...)"],
               form_t="Book or ask a question", form_p="Send us your dates and number of travellers. We reply quickly by email or WhatsApp with a clear price, no commitment.",
               related="You may also like", crumbs_home="Home", sub_to=[("tours", "Multi-day tours"), ("days", "Day trips")], sub_tr=[("air", "Airport transfers"), ("city", "Inter-city transfers"), ("fleet", "Our fleet")]),
    "fr": dict(nav=[("home", "Accueil"), ("dest", "Destinations"), ("tours", "Tours"), ("fleet", "Transferts"), ("about", "À propos"), ("contact", "Contact")],
               book="Réserver", from_="À partir de", per="par véhicule privé", more="Voir le détail", wa_msg="Bonjour All in Marrakech, je souhaite des informations sur : ",
               tagline="Transport touristique, transferts aéroport et circuits privés au Maroc, au départ de Marrakech.", fleet_h="Notre flotte", seats="places",
               cm_h="Comment souhaitez-vous nous contacter ?", cm_p="Choisissez ce qui vous convient le mieux. Nous répondons en général en quelques heures.", cm_wa="Réponse la plus rapide", cm_form="Ou remplissez notre formulaire de réservation",
               links="Découvrir", info="Contact", follow="Nos services", rights="Tous droits réservés.", photos="Photos des destinations : Wikimedia Commons",
               svc=["Transferts aéroport", "Circuits privés", "Excursions", "Transport de groupes", "Mariages & événements"],
               days_lbl="Jour", hl="Points forts", itin="Programme", inc="Inclus", exc="Non inclus", req="Demander ce circuit", wa_btn="Demander sur WhatsApp",
               dur="Durée", dep="Départ", dep_v="Marrakech, depuis votre hôtel ou riad", grp="Groupe", grp_v="Privé, de 1 à 84 personnes",
               pnote="Prix par véhicule privé avec chauffeur, pas par personne. Groupe plus grand ? Demandez-nous un devis.",
               ptab="Tableau des prix", ptab_p="Un seul prix pour tout le véhicule, chauffeur et carburant compris. Choisissez la taille adaptée à votre groupe.", ptab_book="Réserver",
               tiers=[("Minibus Confort", "4"), ("Minibus Standard", "7"), ("Minibus Groupe", "14"), ("Minibus Large", "17"), ("Autocar Confort", "29"), ("Autocar Premium", "48")],
               inc_l=["Véhicule privé climatisé", "Chauffeur professionnel", "Carburant et péages", "Prise en charge et retour à votre hôtel ou riad à Marrakech"],
               exc_l=["Hébergement (nous pouvons le réserver pour vous)", "Repas et boissons", "Entrées des sites et guides locaux", "Activités en option (dromadaire, quad, bateau...)"],
               form_t="Réserver ou poser une question", form_p="Envoyez-nous vos dates et le nombre de voyageurs. Nous répondons vite par e-mail ou WhatsApp avec un prix clair, sans engagement.",
               related="Vous aimerez aussi", crumbs_home="Accueil", sub_to=[("tours", "Circuits"), ("days", "Excursions")], sub_tr=[("air", "Transferts aéroport"), ("city", "Transferts inter-villes"), ("fleet", "Notre flotte")]),
}

# --- small inline icons
I = {
    "phone": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><path d="M20 4H4a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1s-.5-.1-.7.1-.8 1-1 1.2-.4.2-.7.1a8.2 8.2 0 0 1-4-3.5c-.3-.5.3-.5.9-1.6.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 0 0-.9.4 3.6 3.6 0 0 0-1.1 2.7 6.3 6.3 0 0 0 1.3 3.3 14.4 14.4 0 0 0 5.5 4.9c2 .9 2.9.9 3.9.8a3.4 3.4 0 0 0 2.2-1.6 2.8 2.8 0 0 0 .2-1.6c-.1-.1-.3-.2-.6-.3zM12 21.8a9.9 9.9 0 0 1-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1 1 12 21.8zm8.4-18.2A11.8 11.8 0 0 0 1.8 17.8L.1 24l6.3-1.7A11.8 11.8 0 0 0 24 12a11.7 11.7 0 0 0-3.6-8.4z"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm1 10.4 3.5 2.1-.8 1.3L11 13V7h2z"/></svg>',
    "users": '<svg viewBox="0 0 24 24"><path d="M16 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-8 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 2c-2.3 0-7 1.2-7 3.5V19h14v-2.5C15 14.2 10.3 13 8 13zm8 0h-1c1.2.8 2 1.9 2 3.5V19h6v-2.5c0-2.3-4.7-3.5-7-3.5z"/></svg>',
    "bag": '<svg viewBox="0 0 24 24"><path d="M17 6h-2V3H9v3H7a2 2 0 0 0-2 2v11a2 2 0 0 0 2 2h1v1h2v-1h4v1h2v-1h1a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2zM11 5h2v1h-2z"/></svg>',
    "plane": '<svg viewBox="0 0 24 24"><path d="M21 16v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/></svg>',
    "map": '<svg viewBox="0 0 24 24"><path d="m20.5 3-.2.1L15 5.1 9 3 3.4 4.9a.5.5 0 0 0-.4.5v15.1a.5.5 0 0 0 .7.5L9 18.9l6 2.1 5.6-1.9a.5.5 0 0 0 .4-.5V3.5a.5.5 0 0 0-.5-.5zM15 19l-6-2.1V5l6 2.1z"/></svg>',
    "sun": '<svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zM11 1h2v3h-2zm0 19h2v3h-2zM1 11h3v2H1zm19 0h3v2h-3zM4.2 5.6l1.4-1.4 2.1 2.1-1.4 1.4zm12.1 12.1 1.4-1.4 2.1 2.1-1.4 1.4zM4.2 18.4l2.1-2.1 1.4 1.4-2.1 2.1zM16.3 6.3l2.1-2.1 1.4 1.4-2.1 2.1z"/></svg>',
    "car": '<svg viewBox="0 0 24 24"><path d="M18.9 6c-.2-.6-.8-1-1.4-1h-11c-.7 0-1.2.4-1.4 1L3 12v8c0 .6.4 1 1 1h1c.6 0 1-.4 1-1v-1h12v1c0 .6.4 1 1 1h1c.6 0 1-.4 1-1v-8zM6.5 16a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm11 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM5 11l1.5-4.5h11L19 11z"/></svg>',
    "van": '<svg viewBox="0 0 24 24"><path d="M17 5H3a2 2 0 0 0-2 2v9h2a3 3 0 0 0 6 0h5.5a3 3 0 0 0 6 0H23v-5zM3 11V7h4v4zm3 6.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM13 11H9V7h4zm4.5 6.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM15 11V7h1l4 4z"/></svg>',
    "bus": '<svg viewBox="0 0 24 24"><path d="M4 16c0 .9.4 1.7 1 2.2V20a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h8v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1.8c.6-.5 1-1.3 1-2.2V6c0-3.5-3.6-4-8-4S4 2.5 4 6zm3.5 1a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm9 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm1.5-6H6V6h12z"/></svg>',
    "heart": '<svg viewBox="0 0 24 24"><path d="M12 21.4 10.6 20C5.4 15.4 2 12.3 2 8.5 2 5.4 4.4 3 7.5 3c1.7 0 3.4.8 4.5 2.1A6 6 0 0 1 16.5 3C19.6 3 22 5.4 22 8.5c0 3.8-3.4 6.9-8.6 11.5z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 1 3 5v6c0 5.6 3.8 10.7 9 12 5.2-1.3 9-6.4 9-12V5zm-2 16-4-4 1.4-1.4 2.6 2.6 6.6-6.6L18 9z"/></svg>',
    "star": '<svg viewBox="0 0 24 24"><path d="M12 17.3 18.2 21l-1.6-7L22 9.2l-7.2-.6L12 2 9.2 8.6 2 9.2 7.5 14l-1.7 7z"/></svg>',
    "menu": '<svg viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>',
}


def wa_link(lang, topic=""):
    return "https://wa.me/" + WA + "?text=" + quote(T[lang]["wa_msg"] + topic)


def header(lang):
    t = T[lang]
    def item(k, lbl):
        subs = {"fleet": t["sub_tr"], "tours": t["sub_to"]}.get(k)
        if not subs:
            return '<a href="%s">%s</a>' % (url(k, lang), lbl)
        sub = "".join('<a href="%s">%s</a>' % (url(sk, lang), sl) for sk, sl in subs)
        return '<div class="aim-dd"><a href="%s">%s</a><div class="aim-ddm">%s</div></div>' % (url(k, lang), lbl, sub)
    nav = "".join(item(k, lbl) for k, lbl in t["nav"])
    lang_sw = '<span class="aim-lang"><a id="aim-l-en" href="%s"%s>EN</a><a id="aim-l-fr" href="%s"%s>FR</a></span>' % (
        url("home", "en"), ' class="on"' if lang == "en" else "", url("home", "fr"), ' class="on"' if lang == "fr" else "")
    return '<div class="aim">' + (
        '<div class="aim-top"><div class="aim-wrap"><div>'
        '<a href="tel:%s">%s %s</a><a class="aim-hide" href="mailto:%s">%s %s</a></div>%s</div></div>'
        '<header class="aim-hdr"><div class="aim-wrap" style="position:relative">'
        '<a class="aim-logo" href="%s"><img src="%s" alt="All in Marrakech" width="180" height="60"></a>'
        '<input type="checkbox" id="aim-mt"><label class="aim-burger" for="aim-mt" aria-label="Menu">%s</label>'
        '<nav class="aim-nav">%s<a class="aim-btn" href="%s#book">%s</a></nav></div></header>'
    ) % (TEL, I["phone"], PHONE, EMAIL, I["mail"], EMAIL, lang_sw, url("home", lang), LOGO, I["menu"], nav,
         url("contact", lang), t["book"]) + '</div>'


# footer "Our fleet" column: every vehicle in VEH, with a car / van / bus icon
FOOT_FLEET = [({"e": "car", "rr": "car", "tg": "car", "sk": "car", "v": "van", "sp": "van", "bus": "bus"}[k], n, seats)
              for k, n, seats, *_ in VEH]


def contact_modal(lang):
    t = T[lang]
    return ('<div class="aim aim-cm" id="aim-cm" aria-hidden="true"><div class="aim-cm-bg" data-cm-close></div>'
            '<div class="aim-cm-box" role="dialog" aria-modal="true" aria-labelledby="aim-cm-h">'
            '<button type="button" class="aim-cm-x" data-cm-close aria-label="Close">×</button>'
            '<h3 id="aim-cm-h">%s</h3><p>%s</p>'
            '<a class="aim-cm-opt aim-cm-wa" href="%s" target="_blank" rel="noopener"><span class="aim-cm-ic">%s</span><span><b>WhatsApp</b><small>%s · %s</small></span><i>→</i></a>'
            '<a class="aim-cm-opt aim-cm-mail" href="mailto:%s"><span class="aim-cm-ic">%s</span><span><b>E-mail</b><small>%s</small></span><i>→</i></a>'
            '<a class="aim-cm-form" data-cm-direct href="%s#book">%s →</a></div></div>') % (
        t["cm_h"], t["cm_p"], wa_link(lang), I["wa"], t["cm_wa"], PHONE, EMAIL, I["mail"], EMAIL, url("contact", lang), t["cm_form"])


def footer(lang):
    t = T[lang]
    subs = {"tours": t["sub_to"], "fleet": t["sub_tr"]}
    links = "".join('<li><a href="%s">%s</a></li>' % (url(sk, lang), sl)
                    for k, lbl in t["nav"][1:] for sk, sl in subs.get(k, [(k, lbl)]))
    name = {"Tourist coach": "Autocar de tourisme"} if lang == "fr" else {}
    fleet = "".join('<li><a href="%s"><span class="aim-fi">%s</span><span>%s<small>%s %s</small></span></a></li>' % (
        url("fleet", lang), I[ic], name.get(n, n), seats, t["seats"]) for ic, n, seats in FOOT_FLEET)
    return '<div class="aim">' + (
        '<footer class="aim-ftr"><div class="aim-wrap"><div class="aim-cols">'
        '<div class="aim-fabout"><a class="aim-logo" href="%s"><img src="%s" alt="All in Marrakech" width="210" height="70"></a><p>%s</p>'
        '<div class="aim-fbtns"><a class="aim-fbtn aim-fbtn-wa" href="%s" target="_blank" rel="noopener">%s WhatsApp</a><a class="aim-fbtn" href="mailto:%s">%s E-mail</a></div></div>'
        '<div><h4>%s</h4><ul class="aim-ffleet">%s</ul></div>'
        '<div><h4>%s</h4><ul class="aim-flinks">%s</ul></div>'
        '<div><h4>%s</h4><ul class="aim-contact">'
        '<li><span class="aim-ic">%s</span><span><b>WhatsApp</b><a href="%s" target="_blank" rel="noopener">%s</a></span></li>'
        '<li><span class="aim-ic">%s</span><span><b>E-mail</b><a href="mailto:%s">%s</a></span></li>'
        '<li><span class="aim-ic">%s</span><span><b>Marrakech</b>%s</span></li></ul></div>'
        '</div><div class="aim-copy"><span>© 2026 All in Marrakech. %s</span></div></div></footer>'
        '<a class="aim-wa-float" href="%s" target="_blank" rel="noopener" aria-label="WhatsApp">%s</a>%s'
    ) % (url("home", lang), LOGO, t["tagline"], wa_link(lang), I["wa"], EMAIL, I["mail"],
         t["fleet_h"], fleet, t["links"], links, t["info"],
         I["wa"], wa_link(lang), PHONE, I["mail"], EMAIL, EMAIL, I["pin"], "Morocco" if lang == "en" else "Maroc",
         t["rights"], wa_link(lang), I["wa"], contact_modal(lang)) + '</div>' + JS


JS = ("<script>(function(){var d=document.documentElement;d.classList.add('aim-js');"
      "var r=document.querySelectorAll('.aim-rv');if(!('IntersectionObserver' in window)){r.forEach(function(e){e.classList.add('in')});return}"
      "var o=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');o.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});"
      "r.forEach(function(e){o.observe(e)});setTimeout(function(){r.forEach(function(e){e.classList.add('in')})},4000)})();"
      "(function(){"
      "document.querySelectorAll('.aim-nav a').forEach(function(a){if(a.href===location.href)a.classList.add('on');a.addEventListener('click',function(){var c=document.getElementById('aim-mt');if(c)c.checked=false})});"
      "var m=document.querySelector('[data-alt-en]');if(m){var e=document.getElementById('aim-l-en'),f=document.getElementById('aim-l-fr');if(e)e.href=m.getAttribute('data-alt-en');if(f)f.href=m.getAttribute('data-alt-fr');"
      "var t=m.getAttribute('data-trip'),i=document.getElementById('aim-trip');if(t&&i&&!i.value)i.value=t}"
      "var q=new URLSearchParams(location.search),qd=q.get('d'),qp=q.get('p'),fd=document.querySelector('.wpcf7 [name=travel-date]'),fp=document.querySelector('.wpcf7 [name=travellers]');"
      "if(qd&&fd)fd.value=qd;if(qp&&fp)fp.value=parseInt(qp)||2})();"
      "(function(){var c=document.getElementById('aim-cm');if(!c)return;document.body.appendChild(c);"
      "function op(){c.classList.add('on');c.setAttribute('aria-hidden','false')}function cl(){c.classList.remove('on');c.setAttribute('aria-hidden','true')}"
      "document.addEventListener('click',function(e){var a=e.target.closest('a,[data-cm-close]');if(!a)return;if(a.hasAttribute('data-cm-close')){cl();return}"
      "if(a.hasAttribute('data-cm-direct')){cl();return}var h=a.getAttribute('href')||'';"
      "var m=h.match(/pagename=([a-z-]+)/);if(a.hasAttribute('data-aim-contact')||m&&(m[1]==='contact-us'||m[1]==='contactez-nous')&&h.indexOf('#book')<0){e.preventDefault();op()}});"
      "document.addEventListener('keydown',function(e){if(e.key==='Escape')cl()})})();</script>")


BLOCK = {}  # filled in by push step: ("header"|"footer"|"book", lang) -> wp_block id


def page(lang, active, alt_key, body, trip="", book=True):
    attrs = ' data-alt-en="%s" data-alt-fr="%s"' % (url(alt_key, "en"), url(alt_key, "fr"))
    if trip:
        attrs += ' data-trip="%s"' % trip.replace('"', "'")
    main = '<div class="aim" lang="%s"%s><main>%s</main></div>' % (lang, attrs, body)
    ref = lambda k: '<!-- wp:block {"ref":%d} /-->' % BLOCK[(k, lang)]
    out = ref("header") + '\n<!-- wp:html -->\n' + main + '\n<!-- /wp:html -->\n'
    if book:
        out += ref("book") + "\n"
    return out + ref("footer")


def card(p, lang):
    t, c = T[lang], p[lang]
    return ('<a class="aim-card aim-rv" href="%s"><div class="aim-card-img"><img src="%s" alt="%s" loading="lazy" width="800" height="600">'
            '<span class="aim-badge">%s</span></div><div class="aim-card-b"><h3>%s</h3><p>%s</p>'
            '<div class="aim-card-f"><span class="aim-price">%s<b>€%d</b></span><span class="aim-more">%s →</span></div></div></a>') % (
        url(p["key"], lang), IMG[p["img"]], c["title"], c["dur"], c["title"], c["short"], t["from_"], p["price"], t["more"])


FR_NAME = {"Mercedes E-Class": "Mercedes Classe E", "Mercedes V-Class": "Mercedes Classe V", "Tourist coach": "Autocar de tourisme"}


def vcard(v, lang):
    k, name, seats, bags, img, en, fr = v
    if lang == "fr":
        name = FR_NAME.get(name, name)
    pax = ("passengers" if lang == "en" else "passagers")
    lug = ("suitcases" if lang == "en" else "valises")
    if bags == "XL":
        lug_t = "Large luggage hold" if lang == "en" else "Grande soute"
    else:
        lug_t = "%s %s" % (bags, lug)
    return ('<div class="aim-card aim-veh aim-rv"><div class="aim-card-img"><img src="%s" alt="%s" loading="lazy"></div>'
            '<div class="aim-card-b"><h3>%s</h3><div class="aim-specs"><span>%s %s %s</span><span>%s %s</span></div><p>%s</p>'
            '<a class="aim-more" href="%s">%s →</a></div></div>') % (
        img, name, name, I["users"], seats, pax, I["bag"], lug_t, en if lang == "en" else fr,
        wa_link(lang, name), "Get a quote" if lang == "en" else "Demander un devis")


def form_section(lang, sand=True):  # rendered once per language as a synced block
    t = T[lang]
    return ('<div class="aim"><section class="aim-sec%s" id="book"><div class="aim-wrap aim-formwrap"><div class="aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p>'
            '<ul class="aim-contact" style="margin-top:28px">'
            '<li><span class="aim-ic">%s</span><span><b>WhatsApp</b><a href="%s" target="_blank" rel="noopener">%s</a></span></li>'
            '<li><span class="aim-ic">%s</span><span><b>E-mail</b><a href="mailto:%s">%s</a></span></li>'
            '<li><span class="aim-ic">%s</span><span><b>%s</b>%s</span></li></ul>'
            '<a class="aim-btn aim-btn-wa" href="%s" target="_blank" rel="noopener">%s %s</a></div>'
            '<div class="aim-form aim-rv">[contact-form-7 id="%d"]</div></div></section></div>') % (
        " aim-sand" if sand else "", t["book"], t["form_t"], t["form_p"],
        I["wa"], wa_link(lang), PHONE, I["mail"], EMAIL, EMAIL, I["clock"],
        "7 days a week" if lang == "en" else "7 jours sur 7", "Reply within a few hours" if lang == "en" else "Réponse en quelques heures",
        wa_link(lang), I["wa"], t["wa_btn"], FORM[lang])


# ------------------------------------------------------------------ HOME
HOME = {
    "en": dict(
        ey="Private tours & transport · Marrakech", h1="Discover Morocco with your private driver",
        lead="Desert tours, day trips from Marrakech, airport transfers and group transport. One local team, modern vehicles and a clear price before you travel.",
        b1="See our tours", b2="Book on WhatsApp",
        trust=["Local Marrakech team", "Vehicles from 3 to 84 seats", "Reply within a few hours"],
        svc_ey="What we do", svc_h="Everything you need to travel in Morocco",
        svc_p="From a simple airport pick-up to a 5-day tour across the country, we take care of the road so you can enjoy the trip.",
        svcs=[("plane", "Airport transfers", "Marrakech, Casablanca, Agadir and Fes airports. We follow your flight and wait for you."),
              ("map", "Private tours", "Multi-day tours to the Sahara, Chefchaouen and the imperial cities, at your pace."),
              ("sun", "Day trips", "Ourika, Ouzoud, Essaouira, Agafay and more, with pick-up at your riad."),
              ("bus", "Groups & events", "Minibuses and coaches up to 84 seats for groups, congresses and weddings.")],
        t_ey="Multi-day tours", t_h="Our most popular tours", t_p="Private circuits from Marrakech with your own driver. Every tour can be adapted to your dates and wishes.", t_all="All tours",
        d_ey="Day trips", d_h="Day trips from Marrakech", d_p="Leave in the morning, come back in the evening. Mountains, waterfalls, deserts and cities around Marrakech.", d_all="All day trips",
        f_ey="Our speciality: transport", f_h="A vehicle for every group, from 1 to 84 people", f_p="Air-conditioned and clean, with professional drivers. Choose the right size for your group.", f_all="Transfers & fleet",
        w_ey="Why travel with us", w_h="A local team you can trust",
        w_p="All in Marrakech is a Marrakech-based tourist transport company. We know the roads, the weather and the best stops, and we answer your messages ourselves.",
        w_l=["Private trips only: no shared buses, no waiting", "Clear prices sent before you book", "Experienced, careful drivers", "Flexible: change the route, the stops or the time", "Help on WhatsApp before and during your trip"],
        s_ey="How it works", s_h="Book in 3 simple steps",
        steps=[("Tell us your plan", "Send your dates, number of people and the trip you like, by WhatsApp or with the form."),
               ("Get your price", "We reply quickly with a clear price and the best vehicle for your group."),
               ("Enjoy Morocco", "Your driver picks you up at your hotel or riad on time. You just enjoy the trip.")],
        q_ey="FAQ", q_h="Frequently asked questions",
        faq=[("Are your tours private?", "Yes. Every tour and day trip is private: only you and your group travel in the vehicle, with your own driver."),
             ("What is included in the price?", "The private air-conditioned vehicle, the driver, fuel and tolls, and pick-up at your hotel or riad in Marrakech. Accommodation, meals and entrance tickets are not included unless we agree otherwise."),
             ("Can you book hotels and desert camps?", "Yes, we can book riads, hotels and desert camps along the way. Just tell us your budget."),
             ("How do I book and pay?", "Send us your request by WhatsApp or with the form. We reply with a clear price and the payment options, and your trip is confirmed once you accept."),
             ("Do you do airport transfers at night?", "Yes, we work 7 days a week and at any hour. Send us your flight number and we will follow your arrival."),
             ("Can we change the itinerary?", "Of course. All our programs are examples: we can add stops, change the number of days or build a trip only for you.")],
        c_h="Ready to explore Morocco?", c_p="Tell us where you want to go. We answer quickly with a plan and a clear price.", c_b="Contact us"),
    "fr": dict(
        ey="Circuits privés & transport · Marrakech", h1="Découvrez le Maroc avec votre chauffeur privé",
        lead="Circuits dans le désert, excursions depuis Marrakech, transferts aéroport et transport de groupes. Une équipe locale, des véhicules récents et un prix clair avant de partir.",
        b1="Voir nos circuits", b2="Réserver sur WhatsApp",
        trust=["Équipe locale à Marrakech", "Véhicules de 3 à 84 places", "Réponse en quelques heures"],
        svc_ey="Nos services", svc_h="Tout pour voyager au Maroc",
        svc_p="D'un simple transfert depuis l'aéroport à un circuit de 5 jours à travers le pays, nous nous occupons de la route pour que vous profitiez du voyage.",
        svcs=[("plane", "Transferts aéroport", "Aéroports de Marrakech, Casablanca, Agadir et Fès. Nous suivons votre vol et vous attendons."),
              ("map", "Circuits privés", "Circuits de plusieurs jours vers le Sahara, Chefchaouen et les villes impériales, à votre rythme."),
              ("sun", "Excursions", "Ourika, Ouzoud, Essaouira, Agafay et plus, avec prise en charge à votre riad."),
              ("bus", "Groupes & événements", "Minibus et autocars jusqu'à 84 places pour groupes, congrès et mariages.")],
        t_ey="Circuits", t_h="Nos circuits les plus demandés", t_p="Circuits privés au départ de Marrakech avec votre propre chauffeur. Chaque circuit s'adapte à vos dates et à vos envies.", t_all="Tous les circuits",
        d_ey="Excursions", d_h="Excursions d'une journée depuis Marrakech", d_p="Départ le matin, retour le soir. Montagnes, cascades, déserts et villes autour de Marrakech.", d_all="Toutes les excursions",
        f_ey="Notre spécialité : le transport", f_h="Un véhicule pour chaque groupe, de 1 à 84 personnes", f_p="Climatisés et propres, avec des chauffeurs professionnels. Choisissez la taille adaptée à votre groupe.", f_all="Transferts & flotte",
        w_ey="Pourquoi nous choisir", w_h="Une équipe locale de confiance",
        w_p="All in Marrakech est une société de transport touristique basée à Marrakech. Nous connaissons les routes, la météo et les meilleurs arrêts, et nous répondons nous-mêmes à vos messages.",
        w_l=["Uniquement en privé : pas de bus partagé, pas d'attente", "Des prix clairs envoyés avant la réservation", "Des chauffeurs expérimentés et prudents", "Flexible : changez l'itinéraire, les arrêts ou l'horaire", "Assistance sur WhatsApp avant et pendant le voyage"],
        s_ey="Comment ça marche", s_h="Réservez en 3 étapes",
        steps=[("Parlez-nous de votre projet", "Envoyez vos dates, le nombre de personnes et le circuit qui vous plaît, par WhatsApp ou via le formulaire."),
               ("Recevez votre prix", "Nous répondons vite avec un prix clair et le véhicule adapté à votre groupe."),
               ("Profitez du Maroc", "Votre chauffeur vous attend à l'heure à votre hôtel ou riad. Vous n'avez plus qu'à profiter.")],
        q_ey="FAQ", q_h="Questions fréquentes",
        faq=[("Vos circuits sont-ils privés ?", "Oui. Tous nos circuits et excursions sont privés : seuls vous et votre groupe voyagez dans le véhicule, avec votre propre chauffeur."),
             ("Qu'est-ce qui est inclus dans le prix ?", "Le véhicule privé climatisé, le chauffeur, le carburant et les péages, et la prise en charge à votre hôtel ou riad à Marrakech. L'hébergement, les repas et les entrées ne sont pas inclus, sauf accord contraire."),
             ("Pouvez-vous réserver les hôtels et les camps ?", "Oui, nous pouvons réserver riads, hôtels et camps dans le désert sur votre route. Indiquez-nous simplement votre budget."),
             ("Comment réserver et payer ?", "Envoyez-nous votre demande par WhatsApp ou via le formulaire. Nous répondons avec un prix clair et les modes de paiement, et votre voyage est confirmé dès que vous acceptez."),
             ("Faites-vous des transferts aéroport la nuit ?", "Oui, nous travaillons 7 jours sur 7, à toute heure. Envoyez-nous votre numéro de vol et nous suivrons votre arrivée."),
             ("Peut-on modifier l'itinéraire ?", "Bien sûr. Nos programmes sont des exemples : nous pouvons ajouter des arrêts, changer le nombre de jours ou créer un voyage rien que pour vous.")],
        c_h="Prêt à découvrir le Maroc ?", c_p="Dites-nous où vous voulez aller. Nous répondons vite avec un programme et un prix clair.", c_b="Nous contacter"),
}


def faq_html(items):
    return '<div class="aim-faq">' + "".join("<details class=\"aim-rv\"><summary>%s</summary><p>%s</p></details>" % qa for qa in items) + "</div>"


def home(lang):
    h, t = HOME[lang], T[lang]
    tours = [p for p in P if p["kind"] == "circuit"]
    days = [p for p in P if p["kind"] == "day"]
    pick_days = [d for d in days if d["key"] in ("agafay", "ourika", "imlil", "ouarzazate", "casablanca", "3valleys")]
    body = hero_v2(lang, url)
    body += ('<section class="aim-sec aim-darkbg"><div class="aim-wrap"><div class="aim-head aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p></div>'
             '<div class="aim-grid aim-grid4">%s</div><div class="aim-center"><a class="aim-btn" href="%s">%s</a></div></div></section>') % (
        h["f_ey"], h["f_h"], h["f_p"], "".join(vcard(v, lang) for v in VEH if v[0] in ("e", "v", "sp", "bus")), url("fleet", lang), h["f_all"])
    body += ('<section class="aim-sec"><div class="aim-wrap"><div class="aim-head aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p></div>'
             '<div class="aim-feats">%s</div></div></section>') % (
        h["svc_ey"], h["svc_h"], h["svc_p"],
        "".join('<div class="aim-feat aim-rv"><span class="aim-ic">%s</span><h3>%s</h3><p>%s</p></div>' % (I[i], a, b) for i, a, b in h["svcs"]))
    body += ('<section class="aim-sec aim-sand" id="tours"><div class="aim-wrap"><div class="aim-head aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p></div>'
             '<div class="aim-grid">%s</div><div class="aim-center"><a class="aim-btn" href="%s">%s</a></div></div></section>') % (
        h["t_ey"], h["t_h"], h["t_p"], "".join(card(p, lang) for p in tours), url("tours", lang), h["t_all"])
    body += ('<section class="aim-sec"><div class="aim-wrap"><div class="aim-head aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p></div>'
             '<div class="aim-grid">%s</div><div class="aim-center"><a class="aim-btn" href="%s">%s</a></div></div></section>') % (
        h["d_ey"], h["d_h"], h["d_p"], "".join(card(p, lang) for p in pick_days), url("days", lang), h["d_all"])
    body += ('<section class="aim-sec"><div class="aim-wrap aim-split"><div class="aim-rv"><img src="%s" alt="Aït Ben Haddou" loading="lazy"></div>'
             '<div class="aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p><ul class="aim-checks">%s</ul></div></div></section>') % (
        IMG["aitbenhaddou"], h["w_ey"], h["w_h"], h["w_p"], "".join("<li>%s</li>" % x for x in h["w_l"]))
    body += ('<section class="aim-sec aim-sand"><div class="aim-wrap"><div class="aim-head aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2></div>'
             '<div class="aim-steps">%s</div></div></section>') % (
        h["s_ey"], h["s_h"], "".join('<div class="aim-step aim-rv"><h3>%s</h3><p>%s</p></div>' % s for s in h["steps"]))
    body += ('<section class="aim-sec"><div class="aim-wrap"><div class="aim-head aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2></div>%s</div></section>') % (
        h["q_ey"], h["q_h"], faq_html(h["faq"]))
    return page(lang, "home", "home", body)


# ------------------------------------------------------------------ LISTINGS
LIST = {
    ("tours", "en"): ("Private tours in Morocco", "Multi-day tours from Marrakech",
                      "Desert, mountains, blue city and imperial cities. Every tour is private, with your own driver, and can be adapted to your dates, pace and budget.", "merzouga"),
    ("tours", "fr"): ("Circuits privés au Maroc", "Circuits de plusieurs jours depuis Marrakech",
                      "Désert, montagnes, ville bleue et villes impériales. Chaque circuit est privé, avec votre propre chauffeur, et s'adapte à vos dates, votre rythme et votre budget.", "merzouga"),
    ("days", "en"): ("Day trips", "Day trips from Marrakech",
                     "Leave after breakfast, come back for dinner. Waterfalls, Berber valleys, the Agafay desert and the big cities of the coast, all with pick-up at your riad.", "ourika"),
    ("days", "fr"): ("Excursions", "Excursions d'une journée depuis Marrakech",
                     "Départ après le petit-déjeuner, retour pour le dîner. Cascades, vallées berbères, désert d'Agafay et grandes villes de la côte, avec prise en charge à votre riad.", "ourika"),
}


def custom_card(lang):
    if lang == "en":
        h, p, b = "Your tailor-made trip", "Have your own idea? Tell us the places you want to see and the number of days, and we build the route and the price for you.", "Ask for a custom trip"
    else:
        h, p, b = "Votre voyage sur mesure", "Vous avez votre propre idée ? Dites-nous les lieux à voir et le nombre de jours, nous préparons l'itinéraire et le prix pour vous.", "Demander un voyage sur mesure"
    return ('<div class="aim-card aim-rv" style="background:var(--aim-dark);color:#fff;justify-content:center"><div class="aim-card-b" style="justify-content:center">'
            '<span class="aim-eyebrow" style="color:var(--aim-gold)">%s</span><h3 style="color:#fff;font-size:26px">%s</h3><p style="color:#bbb;flex:0">%s</p>'
            '<a class="aim-btn" style="align-self:flex-start;margin-top:10px" href="%s#book">%s</a></div></div>') % (
        "Sur mesure" if lang == "fr" else "Tailor-made", h, p, url("contact", lang), b)


def listing(kind, lang):
    return page(lang, kind, kind, tour_list(kind, lang, url, T[lang]["crumbs_home"]))


# ------------------------------------------------------------------ PROGRAM
# extra price per vehicle size over the base ("from") price, taken from the reference price tables
TIER_ADD = {"day": [0, 10, 20, 30], "circuit": [0, 10, 40, 55, 230, 430]}


def price_table(p, lang):
    """Per-vehicle price table. Day trips: 4 minibus sizes; circuits: 4 minibuses + 2 coaches.
    A program can set its own 'tiers' list of prices to override the default steps."""
    t, c = T[lang], p[lang]
    prices = p.get("tiers") or [p["price"] + x for x in TIER_ADD[p["kind"]]]
    tiles = ""
    names = [(n, seats) for n, (_, seats) in zip(p["tier_names"][lang], t["tiers"])] if p.get("tier_names") else t["tiers"]
    for n, ((name, seats), price) in enumerate(zip(names, prices), 1):
        tiles += ('<a class="aim-tp" href="%s" target="_blank" rel="noopener"><span class="aim-tpi">%s</span><span class="aim-tpn">%s %s</span>'
                  '<span class="aim-tpv">%s</span><b>%d €</b><span class="aim-tpb"><s></s> %s</span></a>') % (
            wa_link(lang, "%s, %s %s %s (%d €)" % (c["title"], name, seats, t["seats"], price)), "<i></i>" * n, seats, t["seats"], name, price, t["ptab_book"])
    return ('<div class="aim-tr aim-ptab aim-rv"><div class="aim-trh"><div class="aim-trr"><span>%s</span></div><div class="aim-trm"><span>%s</span></div></div>'
            '<div class="aim-tps%s">%s</div></div>') % (t["ptab"], t["ptab_p"], " aim-tps6" if len(prices) > 4 else "", tiles)


def program(p, lang):
    t, c = T[lang], p[lang]
    kind = "tours" if p["kind"] == "circuit" else "days"
    kind_lbl = {"en": {"tours": "Tours", "days": "Day trips"}, "fr": {"tours": "Circuits", "days": "Excursions"}}[lang][kind]
    days = ""
    for i, (h, txt) in enumerate(c["days"], 1):
        lbl = ("%s %d" % (t["days_lbl"], i)) if p["kind"] == "circuit" else h
        h4 = h if p["kind"] == "circuit" else ""
        days += "<li><small>%s</small>%s<p>%s</p></li>" % (lbl, ("<h4>%s</h4>" % h4) if h4 else "", txt)
    side = ('<aside class="aim-side"><div class="aim-side-h"><small>%s</small><b>€%d</b><small>%s</small></div><div class="aim-side-b"><ul>'
            '<li><span>%s</span><span>%s</span></li><li><span>%s</span><span>%s</span></li><li><span>%s</span><span>%s</span></li></ul>'
            '<a class="aim-btn" href="#book">%s</a><a class="aim-btn aim-btn-wa" href="%s" target="_blank" rel="noopener">%s %s</a>'
            '<p class="aim-note">%s</p></div></aside>') % (
        t["from_"], p["price"], t["per"], t["dur"], c["dur"], t["dep"], "Marrakech", t["grp"], t["grp_v"].split(",")[0],
        t["req"], wa_link(lang, c["title"]), I["wa"], t["wa_btn"], t["pnote"])
    main = ('<div><p class="aim-intro aim-rv">%s</p>[PTAB]'
            '<div class="aim-box aim-rv"><h3>%s</h3><ul class="aim-checks">%s</ul></div>'
            '<h2 class="aim-rv">%s</h2><ul class="aim-tl aim-rv">%s</ul>'
            '<div class="aim-two aim-rv"><div class="aim-box" style="margin:10px 0"><h3>%s</h3><ul class="aim-checks">%s</ul></div>'
            '<div class="aim-box" style="margin:10px 0"><h3>%s</h3><ul class="aim-checks aim-x">%s</ul></div></div></div>') % (
        c["intro"], t["hl"], "".join("<li>%s</li>" % x for x in c["hl"]), t["itin"], days,
        t["inc"], "".join("<li>%s</li>" % x for x in t["inc_l"]), t["exc"], "".join("<li>%s</li>" % x for x in t["exc_l"]))
    main = main.replace("[PTAB]", price_table(p, lang))
    body = ('<section class="aim-hero aim-phero"><img src="%s" alt="%s" fetchpriority="high"><div class="aim-wrap">'
            '<div class="aim-crumb"><a href="%s">%s</a> / <a href="%s">%s</a></div><h1>%s</h1><p class="aim-lead" style="margin-bottom:6px">%s</p>'
            '<div class="aim-pills"><span class="aim-pill">%s %s</span><span class="aim-pill">%s <b>€%d</b></span><span class="aim-pill">%s</span></div></div></section>') % (
        IMG[p["img"]], c["title"], url("home", lang), t["crumbs_home"], url(kind, lang), kind_lbl, c["title"], c["short"],
        I["clock"].replace("<svg", '<svg style="width:15px;height:15px;fill:#fff;vertical-align:-2px"'), c["dur"], t["from_"], p["price"],
        "Private" if lang == "en" else "Privé")
    body += '<section class="aim-sec"><div class="aim-wrap aim-prog">%s%s</div></section>' % (main, side)
    same = [q for q in P if q["kind"] == p["kind"] and q["key"] != p["key"]][:3]
    body += ('<section class="aim-sec"><div class="aim-wrap"><div class="aim-head aim-rv"><h2>%s</h2></div><div class="aim-grid">%s</div></div></section>') % (
        t["related"], "".join(card(q, lang) for q in same))
    return page(lang, p["key"], p["key"], body, trip=c["title"])


# ------------------------------------------------------------------ FLEET / TRANSFERS
def fleet(lang):
    if lang == "en":
        ey, h1, lead = "Transfers & fleet", "Airport transfers and private transport in Morocco", "Comfortable, air-conditioned vehicles with professional drivers, from a 3-seat sedan to an 84-seat coach. Airport pick-ups, city-to-city transfers and transport for groups and events."
        tr_h, tr_p = "Airport & city transfers", "We meet you in the arrivals hall with your name on a sign, help with your luggage and drive you straight to your hotel or riad. We follow your flight, so a delay is never a problem."
        tr_l = ["Marrakech Menara airport ↔ your hotel or riad", "Marrakech ↔ Essaouira, Agadir, Casablanca, Rabat, Fes", "Transfers to Imlil, Ouirgane, Agafay and the Palmeraie", "Night and early-morning transfers, 7 days a week", "Child seats on request"]
        fh, fp = "Our vehicles", "Pick the vehicle that fits your group and luggage. Not sure? Tell us how many you are and we will advise you."
    else:
        ey, h1, lead = "Transferts & flotte", "Transferts aéroport et transport privé au Maroc", "Des véhicules confortables et climatisés avec chauffeurs professionnels, de la berline 3 places à l'autocar de 84 places. Accueil à l'aéroport, transferts entre villes et transport de groupes et d'événements."
        tr_h, tr_p = "Transferts aéroport & villes", "Nous vous accueillons dans le hall des arrivées avec une pancarte à votre nom, vous aidons avec vos bagages et vous conduisons directement à votre hôtel ou riad. Nous suivons votre vol : un retard n'est jamais un problème."
        tr_l = ["Aéroport Marrakech Ménara ↔ votre hôtel ou riad", "Marrakech ↔ Essaouira, Agadir, Casablanca, Rabat, Fès", "Transferts vers Imlil, Ouirgane, Agafay et la Palmeraie", "Transferts de nuit et tôt le matin, 7 jours sur 7", "Sièges enfants sur demande"]
        fh, fp = "Nos véhicules", "Choisissez le véhicule adapté à votre groupe et vos bagages. Vous hésitez ? Dites-nous combien vous êtes, nous vous conseillons."
    body = ('<section class="aim-hero aim-phero"><img src="%s" alt="%s" fetchpriority="high"><div class="aim-wrap">'
            '<div class="aim-crumb"><a href="%s">%s</a> / %s</div><span class="aim-eyebrow">%s</span><h1>%s</h1><p class="aim-lead">%s</p></div></section>') % (
        VEH[4][4], h1, url("home", lang), T[lang]["crumbs_home"], ey, ey, h1, lead)
    body += ('<section class="aim-sec"><div class="aim-wrap aim-split"><div class="aim-rv"><img src="%s" alt="%s" loading="lazy"></div>'
             '<div class="aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p><ul class="aim-checks">%s</ul>'
             '<a class="aim-btn aim-btn-wa" style="margin-top:12px" href="%s" target="_blank" rel="noopener">%s %s</a></div></div></section>') % (
        VEH[0][4], tr_h, "Transfers" if lang == "en" else "Transferts", tr_h, tr_p, "".join("<li>%s</li>" % x for x in tr_l),
        wa_link(lang, tr_h), I["wa"], T[lang]["wa_btn"])
    body += ('<section class="aim-sec aim-sand"><div class="aim-wrap"><div class="aim-head aim-rv"><span class="aim-eyebrow">%s</span><h2>%s</h2><p>%s</p></div>'
             '<div class="aim-grid">%s</div></div></section>') % ("Fleet" if lang == "en" else "Flotte", fh, fp, "".join(vcard(v, lang) for v in VEH))
    return page(lang, "fleet", "fleet", body, trip="Airport transfer" if lang == "en" else "Transfert aéroport")


# ------------------------------------------------------------------ ABOUT
def about(lang):
    if lang == "en":
        ey, h1, lead = "About us", "All in Marrakech, your local travel partner", "A Marrakech-based team specialised in tourist transport, private tours and transfers across Morocco."
        st_h = "Our story"
        st = ["All in Marrakech was born in the Red City with a simple idea: give travellers a reliable, friendly and honest way to discover Morocco. We started with airport transfers and private excursions, and today we drive families, couples, companies and big groups all over the country.",
              "Our modern fleet goes from executive sedans and luxury SUVs to Mercedes V-Class vans, Sprinter minibuses and tourist coaches of up to 84 seats. Whatever the size of your group, we have the right vehicle.",
              "We are proud of our drivers: experienced, careful on the road and happy to share their country with you. They know the best viewpoints, the cleanest places to stop and the right time to leave to avoid traffic."]
        v_h = "What we promise"
        vals = [("shield", "Safety first", "Well-maintained vehicles and experienced drivers who respect speed limits and rest times."),
                ("heart", "Real hospitality", "We treat every traveller as a guest. Questions are always welcome, before and during the trip."),
                ("star", "Honest prices", "Clear prices sent in advance. No hidden extras and no forced shopping stops."),
                ("clock", "Always on time", "We track your flights and plan our routes so you never wait.")]
        cr_h, cr_p = "Photo credits", "Destination photos on this site come from Wikimedia Commons and are used under their Creative Commons licences:"
    else:
        ey, h1, lead = "À propos", "All in Marrakech, votre partenaire de voyage local", "Une équipe basée à Marrakech, spécialisée dans le transport touristique, les circuits privés et les transferts dans tout le Maroc."
        st_h = "Notre histoire"
        st = ["All in Marrakech est née dans la ville ocre avec une idée simple : offrir aux voyageurs une façon fiable, chaleureuse et honnête de découvrir le Maroc. Nous avons commencé par les transferts aéroport et les excursions privées, et aujourd'hui nous conduisons familles, couples, entreprises et grands groupes dans tout le pays.",
              "Notre flotte récente va de la berline de prestige et du SUV de luxe au van Mercedes Classe V, au minibus Sprinter et aux autocars de tourisme jusqu'à 84 places. Quelle que soit la taille de votre groupe, nous avons le bon véhicule.",
              "Nous sommes fiers de nos chauffeurs : expérimentés, prudents sur la route et heureux de partager leur pays avec vous. Ils connaissent les plus beaux points de vue, les bons endroits pour s'arrêter et la bonne heure pour éviter la circulation."]
        v_h = "Nos engagements"
        vals = [("shield", "La sécurité avant tout", "Des véhicules bien entretenus et des chauffeurs expérimentés qui respectent les limitations et les temps de repos."),
                ("heart", "Une vraie hospitalité", "Chaque voyageur est notre invité. Vos questions sont toujours les bienvenues, avant et pendant le voyage."),
                ("star", "Des prix honnêtes", "Des prix clairs envoyés à l'avance. Pas de frais cachés ni d'arrêts shopping imposés."),
                ("clock", "Toujours à l'heure", "Nous suivons vos vols et planifions nos trajets pour que vous n'attendiez jamais.")]
        cr_h, cr_p = "Crédits photos", "Les photos des destinations de ce site proviennent de Wikimedia Commons et sont utilisées selon leurs licences Creative Commons :"
    body = ('<section class="aim-hero aim-phero"><img src="%s" alt="%s" fetchpriority="high"><div class="aim-wrap">'
            '<div class="aim-crumb"><a href="%s">%s</a> / %s</div><span class="aim-eyebrow">%s</span><h1>%s</h1><p class="aim-lead">%s</p></div></section>') % (
        IMG["koutoubia"], h1, url("home", lang), T[lang]["crumbs_home"], ey, ey, h1, lead)
    body += ('<section class="aim-sec"><div class="aim-wrap aim-split"><div class="aim-rv"><span class="aim-eyebrow">All in Marrakech</span><h2>%s</h2>%s</div>'
             '<div class="aim-rv"><img src="%s" alt="%s" loading="lazy"></div></div></section>') % (
        st_h, "".join("<p>%s</p>" % x for x in st), VEH[4][4], "Mercedes V-Class" if lang == "en" else "Mercedes Classe V")
    body += ('<section class="aim-sec aim-darkbg"><div class="aim-wrap"><div class="aim-head aim-rv"><h2>%s</h2></div><div class="aim-feats">%s</div></div></section>') % (
        v_h, "".join('<div class="aim-feat aim-rv"><span class="aim-ic">%s</span><h3>%s</h3><p>%s</p></div>' % (I[i], a, b) for i, a, b in vals))
    return page(lang, "about", "about", body)


# ------------------------------------------------------------------ CONTACT
def contact(lang):
    if lang == "en":
        ey, h1, lead = "Contact", "Let's plan your trip", "Write to us on WhatsApp or by email, or fill in the form. We reply quickly, 7 days a week."
    else:
        ey, h1, lead = "Contact", "Préparons votre voyage", "Écrivez-nous sur WhatsApp ou par e-mail, ou remplissez le formulaire. Nous répondons vite, 7 jours sur 7."
    body = ('<section class="aim-hero aim-phero" style="min-height:46vh"><img src="%s" alt="Marrakech" fetchpriority="high"><div class="aim-wrap">'
            '<div class="aim-crumb"><a href="%s">%s</a> / %s</div><span class="aim-eyebrow">%s</span><h1>%s</h1><p class="aim-lead">%s</p></div></section>') % (
        IMG["majorelle"], url("home", lang), T[lang]["crumbs_home"], ey, ey, h1, lead)
    return page(lang, "contact", "contact", body)


def build():
    out = {}
    for lang in ("en", "fr"):
        out[("home", lang)] = home(lang)
        out[("tours", lang)] = listing("tours", lang)
        out[("days", lang)] = listing("days", lang)
        out[("fleet", lang)] = fleet(lang)
        out[("air", lang)] = page(lang, "air", "air", transfer_page(lang, "air", url, T[lang]["crumbs_home"]))
        out[("city", lang)] = page(lang, "city", "city", transfer_page(lang, "city", url, T[lang]["crumbs_home"]))
        out[("dest", lang)] = page(lang, "dest", "dest", destinations(lang, url, card, T[lang]["crumbs_home"]), book=False)
        out[("about", lang)] = about(lang)
        out[("contact", lang)] = contact(lang)
        for p in P:
            out[(p["key"], lang)] = program(p, lang)
    return out


TITLES = {
    ("home", "en"): "Home", ("home", "fr"): "Accueil",
    ("tours", "en"): "Morocco Tours", ("tours", "fr"): "Circuits au Maroc",
    ("days", "en"): "Day Trips from Marrakech", ("days", "fr"): "Excursions depuis Marrakech",
    ("air", "en"): "Airport Transfers", ("air", "fr"): "Transferts aéroport",
    ("city", "en"): "Inter-city Transfers", ("city", "fr"): "Transferts inter-villes",
    ("dest", "en"): "Destinations", ("dest", "fr"): "Destinations",
    ("fleet", "en"): "Transfers & Fleet", ("fleet", "fr"): "Transferts & flotte",
    ("about", "en"): "About Us", ("about", "fr"): "À propos",
    ("contact", "en"): "Contact Us", ("contact", "fr"): "Contactez-nous",
}


def title(key, lang):
    if (key, lang) in TITLES:
        return TITLES[(key, lang)]
    return next(p[lang]["title"] for p in P if p["key"] == key)


if __name__ == "__main__":
    os.makedirs("out/blocks", exist_ok=True)
    for lang in ("en", "fr"):
        for k, fn in (("header", header), ("footer", footer), ("book", form_section)):
            open("out/blocks/%s-%s.html" % (k, lang), "w").write("<!-- wp:html -->\n" + fn(lang) + "\n<!-- /wp:html -->")
    if os.path.exists("blocks.json"):
        for k, v in json.load(open("blocks.json")).items():
            BLOCK[tuple(k.split("-"))] = v
    else:
        BLOCK.update({(k, l): 0 for k in ("header", "footer", "book") for l in ("en", "fr")})
    pages = build()
    manifest = []
    for (key, lang), content in pages.items():
        slug = SLUG[key][lang] or "home"
        fn = "out/%s.html" % slug
        open(fn, "w").write(content)
        manifest.append({"key": key, "lang": lang, "slug": slug, "title": title(key, lang), "file": fn, "size": len(content)})
    json.dump(manifest, open("out/manifest.json", "w"), indent=1, ensure_ascii=False)
    print(len(manifest), "pages, total", sum(m["size"] for m in manifest), "bytes")
    for f in sorted(os.listdir("out/blocks")):
        print(f, os.path.getsize("out/blocks/" + f))
