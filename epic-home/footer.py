"""Epic Travel Morocco – site-wide header + footer (Elementor footer templates 3433 and 3436), chic Moroccan style.

python3 footer.py -> chrome-widget.html (header + footer + script, stored as a Custom HTML widget in the theme footer area
                     'footer-widget' so it shows on every page, including the tour pages built by the theme)
                     footer-3433.json (same block in the Elementor template 3433)
contact.py / pages.py / build.py also add the block at the end of each Elementor page; the script keeps one copy.
The header markup is plain HTML with position:fixed, so the menu shows even if JavaScript is delayed;
the mobile menu opens with a CSS checkbox. A small script only hides the old theme header and marks the current link.
The previous (Marcellus / zellij band) version is in git history.
"""
import json, os
import build as B
import chic as C

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = C.SITE
FB = 'https://web.facebook.com/epictravelmorocco'
IG = 'https://www.instagram.com/epictravelmorocco/'
TA = 'https://www.tripadvisor.com/Attraction_Review-g293734-d25394757-Reviews-Epic_Travel_Morocco-Marrakech_Marrakech_Safi.html'
NEWS = "[contact-form-7 id='a4499c9' title='footer email']"

NAV = [('Home', SITE + '/'), ('Tours', SITE + '/destination/'), ('Our fleet', SITE + '/fleet/'),
       ('About us', SITE + '/about-us/'), ('Contact', SITE + '/contact-2/')]
TOURS = [('Sahara Desert Experience', 'sahara-desert-experience'), ('Majestic Kasbah & Desert', 'majestic-kasbah-and-desert-adventure'),
         ('Highlights of Morocco', 'highlights-of-morocco'), ('The Magic of Morocco', 'the-magic-of-morocco'),
         ('Moroccan Odyssey', 'moroccan-odyssey-15-day-grand-tour')]

SOC = {
    'fb': '<path fill="currentColor" stroke="none" d="M13.5 21v-7.5H16l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21z"/>',
    'ig': '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".9" fill="currentColor" stroke="none"/>',
    'ta': '<circle cx="7.5" cy="13" r="3.2"/><circle cx="16.5" cy="13" r="3.2"/><circle cx="7.5" cy="13" r=".9" fill="currentColor"/><circle cx="16.5" cy="13" r=".9" fill="currentColor"/><path d="M3 8.5h18M4.3 8.5 3 7M19.7 8.5 21 7M12 8.5c-1.5-1.4-3.4-2-6-2M12 8.5c1.5-1.4 3.4-2 6-2M12 16.5l-1.2-1.8M12 16.5l1.2-1.8"/>',
}


def soc(n):
    return '<svg class="chf-i" viewBox="0 0 24 24" aria-hidden="true">' + SOC[n] + '</svg>'


VARS = """--ink:#0d1a1f;--gold:#b98a5e;--gold2:#d1a47b;--fh:'Cormorant Garamond',Georgia,serif;--fb:'Jost',system-ui,-apple-system,'Segoe UI',sans-serif;"""

CSS = """
/* header */
.chh,.chh-dr{""" + VARS + """font-family:var(--fb);font-weight:400;line-height:1.6;-webkit-font-smoothing:antialiased}
.chh *,.chh-dr *{box-sizing:border-box}.chh a,.chh-dr a{text-decoration:none!important}
.chh{position:fixed;left:0;right:0;top:0;z-index:9999;background:rgba(13,26,31,.97);backdrop-filter:blur(10px);border-bottom:1px solid rgba(209,164,123,.35)}
.admin-bar .chh{top:32px}
.chh-in{max-width:1320px;margin:0 auto;padding:0 28px;height:78px;display:flex;align-items:center;gap:30px}
.chh-logo img{display:block;max-height:54px;width:auto}
.chh-menu{display:flex;gap:6px;margin:0 auto}
.chh-menu a{position:relative;padding:10px 16px;color:rgba(255,255,255,.82)!important;font-size:12px;font-weight:500;letter-spacing:.24em;text-transform:uppercase;transition:color .3s}
.chh-menu a:after{content:'';position:absolute;left:50%;bottom:2px;width:5px;height:5px;margin-left:-2.5px;background:var(--gold2);transform:rotate(45deg) scale(0);transition:transform .3s}
.chh-menu a:hover,.chh-menu a.cur{color:#fff!important}
.chh-menu a:hover:after,.chh-menu a.cur:after{transform:rotate(45deg) scale(1)}
.chh-cta{display:flex;align-items:center;gap:22px}
.chh-tel{color:rgba(255,255,255,.82)!important;font-size:13px;letter-spacing:.08em;white-space:nowrap}
.chh-btn{padding:13px 22px;border:1px solid var(--gold2);color:#fff!important;font-size:11.5px;font-weight:500;letter-spacing:.26em;text-transform:uppercase;white-space:nowrap;transition:background .3s,color .3s}
.chh-btn:hover{background:var(--gold2);color:var(--ink)!important}
.chh-burger{display:none;margin-left:auto;width:46px;height:46px;cursor:pointer;flex-direction:column;align-items:center;justify-content:center;gap:7px}
.chh-burger span{display:block;width:26px;height:1px;background:#fff;transition:transform .3s}
#chh-t{position:absolute;opacity:0;pointer-events:none}
#chh-t:checked ~ .chh .chh-burger span:first-child{transform:translateY(4px) rotate(45deg)}
#chh-t:checked ~ .chh .chh-burger span:last-child{transform:translateY(-4px) rotate(-45deg)}
.chh-dr{position:fixed;inset:0;z-index:9998;overflow:hidden;background:var(--ink);display:flex;flex-direction:column;justify-content:center;padding:100px 34px 40px;opacity:0;visibility:hidden;transition:opacity .35s,visibility .35s}
#chh-t:checked ~ .chh-dr{opacity:1;visibility:visible}
.chh-dr .ch-ros{position:absolute;right:-180px;bottom:-160px;width:460px;height:460px;fill:none;stroke:var(--gold2);stroke-width:.55;opacity:.14}
.chh-dr a{position:relative;display:block;padding:12px 0;color:#fff!important;font:400 34px/1.2 var(--fh);border-bottom:1px solid rgba(255,255,255,.08)}
.chh-dr a.chh-btn{margin-top:30px;text-align:center;font:500 12px var(--fb);border:1px solid var(--gold2);padding:18px}
.chh-dr .chh-tel{display:block;border:0;margin-top:14px;text-align:center;font:400 15px var(--fb)}
body:not(.home){padding-top:78px}body.tp-page{margin:0}
@media (max-width:1180px){.chh-tel{display:none}}
@media (max-width:960px){.chh-menu,.chh-cta{display:none}.chh-burger{display:flex}.chh-in{height:68px}.chh-logo img{max-height:44px}body:not(.home){padding-top:68px}}
@media (max-width:782px){.admin-bar .chh{top:46px}}
/* footer */
.chf{""" + VARS + """position:relative;overflow:hidden;background:var(--ink);color:rgba(239,232,222,.66);font-family:var(--fb);font-weight:300;font-size:15px;line-height:1.8;-webkit-font-smoothing:antialiased}
.chf *,.chf *:before,.chf *:after{box-sizing:border-box}
.chf a{color:rgba(239,232,222,.78)!important;text-decoration:none!important;transition:color .3s}
.chf a:hover{color:var(--gold2)!important}
.chf .ch-ros{position:absolute;left:-170px;top:-150px;width:560px;height:560px;fill:none;stroke:var(--gold2);stroke-width:.5;opacity:.08;pointer-events:none}
.chf-w{position:relative;max-width:1240px;margin:0 auto;padding:0 28px}
.chf-top{text-align:center;padding:90px 0 60px}
.chf-top img{max-height:84px;width:auto;margin:0 auto 26px;display:block}
.chf-orn{display:flex;align-items:center;justify-content:center;gap:16px;color:var(--gold2);max-width:240px;margin:0 auto 22px}
.chf-orn span{flex:1;height:1px;background:currentColor;opacity:.45}
.chf-orn svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.3}
.chf-tag{font:italic 400 clamp(24px,2.6vw,32px)/1.35 var(--fh);color:#fff;max-width:640px;margin:0 auto}
.chf-g{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border-top:1px solid rgba(239,232,222,.1);border-bottom:1px solid rgba(239,232,222,.1)}
.chf-g>div{padding:46px 30px 44px;border-left:1px solid rgba(239,232,222,.1)}
.chf-g>div:first-child{border-left:0;padding-left:0}
.chf h4{margin:0 0 20px;font:500 11px var(--fb);letter-spacing:.32em;text-transform:uppercase;color:var(--gold2)}
.chf ul{list-style:none;margin:0;padding:0}
.chf li{margin:0 0 8px}
.chf li:before{display:none}
.chf-c{display:block;margin-bottom:10px}
.chf-c small{display:block;font-size:10.5px;letter-spacing:.26em;text-transform:uppercase;color:rgba(239,232,222,.45)}
.chf-c b{font:400 19px/1.4 var(--fh);color:#fff}
.chf-soc{display:flex;gap:10px;margin-top:6px}
.chf-soc a{display:grid;place-items:center;width:42px;height:42px;border:1px solid rgba(239,232,222,.2);border-radius:999px 999px 0 0}
.chf-soc a:hover{border-color:var(--gold2)}
.chf-i{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
.chf-bot{border-top:1px solid rgba(239,232,222,.1)}
.chf-bot .chf-w{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:24px 28px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:rgba(239,232,222,.5)}
@media (max-width:1024px){.chf-g{grid-template-columns:repeat(2,minmax(0,1fr))}.chf-g>div:nth-child(3){border-left:0;padding-left:0}.chf-g>div:nth-child(n+3){border-top:1px solid rgba(239,232,222,.1)}}
@media (max-width:640px){.chf-g{grid-template-columns:1fr}.chf-g>div{border-left:0!important;padding:34px 0!important}.chf-g>div+div{border-top:1px solid rgba(239,232,222,.1)}.chf-top{padding:70px 0 46px}.chf-w{padding:0 22px}}
"""


def header_markup():
    menu = ''.join('<a href="%s">%s</a>' % (u, t) for t, u in NAV)
    tel = '<a class="chh-tel" href="tel:' + B.PHONE1 + '">' + B.PHONE1_T + '</a>'
    return ('<input type="checkbox" id="chh-t" aria-hidden="true" tabindex="-1">'
            '<header class="chh etm" id="chh"><div class="chh-in">'
            '<a class="chh-logo" href="' + SITE + '/" aria-label="Epic Travel Morocco"><img src="' + B.LOGO + '" alt="Epic Travel Morocco"></a>'
            '<nav class="chh-menu" aria-label="Main menu">' + menu + '</nav>'
            '<div class="chh-cta">' + tel + '<a class="chh-btn" href="' + SITE + '/contact-2/">Plan my trip</a></div>'
            '<label class="chh-burger" for="chh-t" aria-label="Menu"><span></span><span></span></label></div></header>'
            '<nav class="chh-dr etm" aria-label="Mobile menu">' + menu
            + '<a class="chh-btn" href="' + SITE + '/contact-2/">Plan my trip</a>' + tel + '</nav>')


EXTRA_CSS = """
/* chrome guards: tour contents ship global header/section rules */
header.chh{margin:0!important;text-align:left!important}
#etm-top,#etm-drawer{display:none!important}
.chh.chh-tr{background:linear-gradient(180deg,rgba(13,26,31,.65),rgba(13,26,31,0));border-bottom-color:transparent;backdrop-filter:none}
.chf-cta{display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap;padding:44px 0 46px}
.chf-cta p{margin:0;font:italic 400 clamp(22px,2.2vw,28px)/1.3 var(--fh);color:#fff}
.chf-cta a{padding:16px 30px;border:1px solid var(--gold2);color:#fff!important;font-size:11.5px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;transition:background .3s,color .3s}
.chf-cta a:hover{background:var(--gold2);color:var(--ink)!important}
/* tour programme pages (built from the itinerary in the tour content) */
.tp-hero{position:relative;min-height:min(86vh,780px);display:flex;align-items:flex-end;color:#fff;overflow:hidden;background:#0d1a1f}
.tp-hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;max-width:none}
.tp-hero:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,26,31,.1) 25%,rgba(13,26,31,.9))}
.tp-hero-in{position:relative;z-index:1;width:100%;padding-top:150px;padding-bottom:84px}
.tp-hero h1{font-size:clamp(46px,6.6vw,104px);color:#fff;max-width:980px}
.tp-hero p{max-width:580px;margin:24px 0 38px;color:rgba(255,255,255,.84)}
.tp-nav{position:sticky;top:78px;z-index:50;background:#fff;border-bottom:1px solid var(--line)}
.admin-bar .tp-nav{top:110px}
.tp-nav .ch-w{display:flex;gap:36px;height:62px;align-items:center;overflow-x:auto}
.tp-nav a{font-size:11.5px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;white-space:nowrap;transition:color .3s}
.tp-nav a:hover{color:var(--gold)}
.tp-nav a.tp-nb{margin-left:auto;padding:12px 22px;background:var(--ink);color:#fff!important}
.tp-split{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(40px,7vw,100px);align-items:center}
.tp-facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));border-top:1px solid var(--line);margin-top:34px}
.tp-facts div{padding:20px 20px 20px 0;border-bottom:1px solid var(--line)}
.tp-facts small{display:block;font-size:10.5px;font-weight:500;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:4px}
.tp-facts b{font:400 24px/1.3 var(--fh)}
.tp-split .ch-arch{height:clamp(420px,44vw,580px)}
.tp-route{padding:76px 0}
.tp-chips{display:flex;flex-wrap:wrap;align-items:center;gap:14px 18px;font:400 clamp(22px,2.4vw,32px)/1.3 var(--fh)}
.tp-chips .ch-star{color:var(--gold);width:12px;height:12px}
.tp-itg{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:clamp(40px,6vw,90px);align-items:start}
.tp-head{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;margin-bottom:34px;flex-wrap:wrap}
.tp-head .ch-h2{margin:0}
.tp-all{background:none;border:0;border-bottom:1px solid var(--gold);padding:0 0 6px;font:500 11.5px var(--fb);letter-spacing:.28em;text-transform:uppercase;color:var(--ink);cursor:pointer}
.tp-day{border-top:1px solid var(--line)}
.tp-day:last-child{border-bottom:1px solid var(--line)}
.tp-day summary{list-style:none;display:grid;grid-template-columns:70px minmax(0,1fr) 24px;gap:22px;align-items:center;padding:22px 0;cursor:pointer}
.tp-day summary::-webkit-details-marker{display:none}
.tp-n{display:flex;flex-direction:column;align-items:center;justify-content:center;width:62px;height:76px;padding-top:10px;border:1px solid var(--gold);border-radius:999px 999px 0 0;color:var(--gold);font-size:9.5px;font-weight:500;letter-spacing:.24em;text-transform:uppercase;transition:background .3s}
.tp-n b{font:400 26px/1 var(--fh);letter-spacing:0;color:var(--ink);margin-top:2px}
.tp-t{font:400 clamp(21px,2vw,27px)/1.3 var(--fh)}
.tp-x{position:relative;width:22px;height:22px}
.tp-x:before,.tp-x:after{content:'';position:absolute;left:0;right:0;top:50%;height:1px;background:var(--ink);transition:transform .3s}
.tp-x:after{transform:rotate(90deg)}
.tp-day[open] .tp-x:after{transform:rotate(0)}
.tp-day[open] .tp-n{background:var(--ink);border-color:var(--ink)}
.tp-day[open] .tp-n b{color:#fff}
.tp-b{padding:0 30px 30px 92px;color:var(--mut)}
.tp-b p{margin:0}
.tp-card{position:sticky;top:170px;background:var(--paper);border-radius:999px 999px 0 0;padding:80px 32px 34px;text-align:center}
.tp-card .ch-star{width:20px;height:20px;color:var(--gold);margin:0 auto 14px;display:block}
.tp-card h3{font-size:30px;margin-bottom:10px}
.tp-card p{color:var(--mut);font-size:15px}
.tp-card ul{list-style:none;margin:20px 0 22px;padding:0;text-align:left;font-size:15px}
.tp-card li{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px solid var(--line)}
.tp-card li:before{display:none}
.tp-card li span{color:var(--mut)}
.tp-card .ch-btn{width:100%;justify-content:center;margin-top:10px;padding:18px 20px}
.tp-card .tp-wa{background:transparent;color:var(--ink)!important}
.tp-card .tp-wa:hover{background:var(--ink);color:#fff!important}
@media (max-width:960px){.tp-itg,.tp-split{grid-template-columns:1fr}.tp-card{position:static}.tp-nav{top:68px}.tp-nav a.tp-nb{display:none}}
@media (max-width:600px){.tp-b{padding:0 0 26px}.tp-day summary{grid-template-columns:54px minmax(0,1fr) 20px;gap:14px}.tp-n{width:50px;height:62px}.tp-n b{font-size:21px}.tp-facts{grid-template-columns:1fr}.tp-hero-in{padding-top:120px;padding-bottom:56px}}
"""

# One script for every page (no double quotes or backslashes: it also lives in Elementor data).
# 1. keeps one copy of this chrome, moves header / mobile menu / footer to <body>;
# 2. hides the theme header and footer (and the home page's own header);
# 3. on tour pages, rebuilds the programme (hero, overview, route, day-by-day itinerary, enquiry) from the tour content;
# 4. marks the current menu link, closes the mobile menu after a click, prefills the contact form subject.
JS = """<script>(function(){if(window.chw)return;window.chw=1;var d=document,W=window,q=String.fromCharCode(34);
function ready(f){if(d.readyState!=='loading')f();else d.addEventListener('DOMContentLoaded',f)}
function hideEl(el){el.style.setProperty('display','none','important')}
function outer(l){return l.filter(function(el){return !l.some(function(o){return o!==el&&o.contains(el)})})}
function mine(el){return el.closest('.chw,.chh,.chh-dr,.chf,.ch,.etm')}
function at(k,v){return ' '+k+'='+q+v+q}
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function tc(s){var small=['of','to','and','the','from','in','a','de','el'];return s.toLowerCase().trim().split(' ').filter(Boolean).map(function(w,i){return i&&small.indexOf(w)>-1?w:w.charAt(0).toUpperCase()+w.slice(1)}).join(' ')}
var SITE='SITEURL',WA='WAURL',TEL='TELNUM',TELT='TELTEXT';
function cls(el){return (el.getAttribute&&el.getAttribute('class'))||''}function footy(c){return c.tagName==='FOOTER'||/footer|subscribe|newsletter|copyright/i.test(cls(c))||!!c.querySelector('footer,[class*=footer],[class*=copyright],[class*=subscribe]')}function place(ft,a){while(a.parentNode&&a.parentNode!==d.body){var par=a.parentNode,me=a;if([].some.call(par.children,function(c){return c!==me&&!mine(c)&&c.tagName!=='SCRIPT'&&footy(c)}))break;a=par}if(a.parentNode===d.body){d.body.appendChild(ft);return}var s=a.nextElementSibling;while(s){var nx=s.nextElementSibling;if(!mine(s)&&['SCRIPT','STYLE','LINK','NOSCRIPT'].indexOf(s.tagName)<0&&s.id!=='wpadminbar'&&getComputedStyle(s).position!=='fixed')hideEl(s);s=nx}a.parentNode.insertBefore(ft,a.nextSibling)}
function tour(w){var it=d.querySelector('.itinerary');if(!it||!it.querySelector('.day-title'))return;
var root=it.closest('section')||it.parentNode,img=root.querySelector('img'),h=root.querySelector('h2,h1'),p=root.querySelector('header p');
var days=[].slice.call(it.querySelectorAll('.day-title')).map(function(t){var c=t.nextElementSibling,s=t.textContent.trim(),i=s.indexOf(':'),n='';
for(var k=0;k<(i>0?i:s.length);k++){var ch=s.charAt(k);if(ch>='0'&&ch<='9')n+=ch}
var pl=(i>-1?s.slice(i+1):s).split('|').map(tc).filter(Boolean);return {n:n,pl:pl,c:c?c.textContent.trim():''}});
var name=d.title;[' – ',' — ',' - ',' | ',' » '].forEach(function(sp){name=name.split(sp)[0]});name=tc(name||(h?h.textContent:''));
var sub=h?h.textContent.trim():'',intro=p?p.textContent.trim():'',nd=days.length;
var top=root;while(top.parentNode&&top.parentNode!==d.body){var par=top.parentNode,ext=[].some.call(par.querySelectorAll('header,footer,.chf,.chw'),function(x){return !root.contains(x)});if(ext)break;top=par}
var STAR=w.querySelector('.chf-orn svg').outerHTML,ROS=w.querySelector('.chf .ch-ros').outerHTML;
var route=[];days.forEach(function(x){x.pl.forEach(function(s){var l=s.toLowerCase();if(/day|explor|depart|arriv|transfer|return|free|airport|pick|visit|tour/.test(l))return;if(route.indexOf(s)<0)route.push(s)})});
var first=route[0]||'',last=route.length>1?route[route.length-1]:'';days.forEach(function(x){var v=parseInt(x.n,10);if(v>nd)nd=v});
var enq=SITE+'/contact-2/?tour='+encodeURIComponent(name),wa=WA+'?text='+encodeURIComponent('Hello, I am interested in the '+name+' tour.');
var src=img?img.getAttribute('src'):'';
var o='<div'+at('class','tp-hero')+'>'+(src?'<img'+at('src',src)+at('alt',esc(name))+'>':'')+'<div'+at('class','ch-w tp-hero-in')+'><span'+at('class','ch-k ch-k-l')+'>'+STAR+'Private tour · '+nd+' days</span><h1>'+esc(name)+'</h1>'+(intro?'<p>'+esc(intro)+'</p>':'')
+'<div'+at('class','ch-hero-act')+'><a'+at('class','ch-btn ch-btn-g')+at('href','#tp-book')+'>Enquire now</a><a'+at('href','#tp-it')+'>See the itinerary</a></div></div></div>'
+'<nav'+at('class','tp-nav')+'><div'+at('class','ch-w')+'><a'+at('href','#tp-ov')+'>Overview</a><a'+at('href','#tp-route')+'>Route</a><a'+at('href','#tp-it')+'>Itinerary</a><a'+at('href','#tp-book')+'>Enquire</a><a'+at('class','tp-nb')+at('href',enq)+'>Book this tour</a></div></nav>'
+'<div'+at('class','ch-s')+at('id','tp-ov')+'><div'+at('class','ch-w tp-split')+'><div><span'+at('class','ch-k')+'>'+STAR+'Overview</span><h2'+at('class','ch-h2')+'>At a <em>glance</em></h2>'
+'<p'+at('class','ch-lead')+'>'+esc(intro||sub)+'</p><div'+at('class','tp-facts')+'><div><small>Duration</small><b>'+nd+' days</b></div><div><small>Style</small><b>Private tour</b></div>'
+(first?'<div><small>Starts</small><b>'+esc(first)+'</b></div>':'')+(last?'<div><small>Ends</small><b>'+esc(last)+'</b></div>':'')+'</div></div>'
+(src?'<div'+at('class','ch-archf')+'><div'+at('class','ch-arch')+'><img'+at('src',src)+at('alt',esc(name))+at('loading','lazy')+'></div></div>':'')+'</div></div>'
+(route.length>1?'<div'+at('class','tp-route ch-paper')+at('id','tp-route')+'><div'+at('class','ch-w')+'><span'+at('class','ch-k')+'>'+STAR+'The route</span><div'+at('class','tp-chips')+'>'+route.map(esc).join(STAR)+'</div></div></div>':'')
+'<div'+at('class','ch-s')+at('id','tp-it')+'><div'+at('class','ch-w tp-itg')+'><div><div'+at('class','tp-head')+'><div><span'+at('class','ch-k')+'>'+STAR+'Itinerary</span><h2'+at('class','ch-h2')+'>Day by <em>day</em></h2></div><button'+at('class','tp-all')+at('type','button')+'>Open all days</button></div>'
+days.map(function(x,i){var nn=x.n||String(i+1);return '<details'+at('class','tp-day')+(i?'':' open')+'><summary><span'+at('class','tp-n')+'>Day<b>'+(nn.length<2?'0'+nn:nn)+'</b></span><span'+at('class','tp-t')+'>'+esc(x.pl.join(' · '))+'</span><span'+at('class','tp-x')+'></span></summary><div'+at('class','tp-b')+'><p>'+esc(x.c)+'</p></div></details>'}).join('')
+'</div><aside'+at('class','tp-card')+'>'+STAR+'<h3>'+esc(name)+'</h3><p>A private journey with your own driver, adapted to your dates and pace.</p><ul><li><span>Duration</span>'+nd+' days</li>'+(first?'<li><span>From</span>'+esc(first)+'</li>':'')+(last?'<li><span>To</span>'+esc(last)+'</li>':'')+'</ul>'
+'<a'+at('class','ch-btn')+at('href',enq)+'>Request a quote</a><a'+at('class','ch-btn tp-wa')+at('href',wa)+'>WhatsApp</a><p style'+'='+q+'margin:16px 0 0'+q+'><a'+at('href','tel:'+TEL)+'>'+TELT+'</a></p></aside></div></div>'
+'<div'+at('class','ch-cta')+at('id','tp-book')+'>'+ROS+'<div'+at('class','ch-w')+'><div'+at('class','ch-orn')+'><span></span>'+STAR+'<span></span></div><h2>Make this journey <em>yours</em></h2><p>Every tour is private and can be adapted to your dates, your pace and the places you dream of.</p>'
+'<div'+at('class','ch-cta-act')+'><a'+at('class','ch-btn ch-btn-g')+at('href',enq)+'>Send an enquiry</a><a'+at('class','ch-btn ch-btn-g')+at('href',wa)+'>WhatsApp</a></div></div></div>';
var box=d.createElement('div');box.className='ch tp';box.innerHTML=o;top.parentNode.insertBefore(box,top);
[].forEach.call(top.querySelectorAll('style,script'),function(s){if(s.tagName==='STYLE')s.remove()});hideEl(top);
var sib=box.previousElementSibling;while(sib){if(/breadcrumb|banner|page-title|page-header/.test(sib.className||''))hideEl(sib);sib=sib.previousElementSibling}
var all=box.querySelector('.tp-all');all.addEventListener('click',function(){var ds=box.querySelectorAll('.tp-day'),open=[].every.call(ds,function(x){return x.open});[].forEach.call(ds,function(x){x.open=!open});all.textContent=open?'Open all days':'Close all days'});
d.body.classList.add('tp-page')}
ready(function(){var ws=[].slice.call(d.querySelectorAll('.chw'));if(!ws.length)return;var w=ws[0];ws.slice(1).forEach(function(x){x.remove()});
var cb=w.querySelector('#chh-t'),top=w.querySelector('.chh'),dr=w.querySelector('.chh-dr'),ft=w.querySelector('.chf'),home=d.getElementById('etm-top');
d.body.insertBefore(cb,d.body.firstChild);d.body.appendChild(top);d.body.appendChild(dr);dr.insertBefore(ft.querySelector('.ch-ros').cloneNode(true),dr.firstChild);
try{tour(w)}catch(e){}
var anchor=d.querySelector('.tp')?d.querySelector('.tp').nextElementSibling:(d.querySelector('[data-elementor-type=wp-page]')||w);place(ft,anchor||w);
var path=location.pathname.replace(/[/]+$/,'')||'/';[].forEach.call(d.querySelectorAll('.chh-menu a,.chh-dr a'),function(a){var pp=a.pathname.replace(/[/]+$/,'')||'/';if(pp===path||(pp==='/destination'&&path.indexOf('/all-tour')===0))a.classList.add('cur')});
dr.addEventListener('click',function(e){if(e.target.closest('a'))cb.checked=false});
if(home){var tr=function(){top.classList.toggle('chh-tr',W.pageYOffset<40)};tr();W.addEventListener('scroll',tr,{passive:true})}
var m=location.search.match(/tour=([^&]+)/);if(m){var t=decodeURIComponent(m[1].replace(/[+]/g,' ')),f=d.querySelector('.etc-form input[name*=subject],.etc-form input[name*=sujet]');if(f&&!f.value)f.value='Enquiry: '+t;var ta=d.querySelector('.etc-form textarea');if(ta&&!ta.value)ta.value='Hello, I am interested in the '+t+' tour. ';}
var hide=function(){
var hs=[].slice.call(d.querySelectorAll('header,nav,div,section')).filter(function(el){if(mine(el)||el.querySelector('.chw,.ch,.etm,.chf,footer'))return false;var r=el.getBoundingClientRect();if(r.top+W.pageYOffset>330||r.height===0)return false;
return el.tagName==='HEADER'||(el.querySelector('a[href*=destination]')&&el.querySelector('a[href*=contact],a[href*=about]'))});outer(hs).forEach(hideEl);
var fs=[].slice.call(d.querySelectorAll('footer,[class*=footer]')).filter(function(el){if(el===d.body||el===d.documentElement||mine(el))return false;return !el.querySelector('.ch,.etm,.tp')});outer(fs).forEach(hideEl)};
hide();W.addEventListener('load',hide)});})();</script>""".replace('\n', '')
JS = (JS.replace('SITEURL', SITE).replace('WAURL', 'https://wa.me/' + B.PHONE1.lstrip('+'))
      .replace('TELNUM', B.PHONE1).replace('TELTEXT', B.PHONE1_T))


def chrome_html():
    """Header + mobile menu + footer + script: the same block goes on every page."""
    nav = ''.join('<li><a href="%s">%s</a></li>' % (u, t) for t, u in NAV)
    tours = ''.join('<li><a href="%s/all-tour/%s/">%s</a></li>' % (SITE, s, t) for t, s in TOURS)
    return ('<div class="chw">' + C.FONTS + '<style>' + ' '.join((C.CSS + CSS + EXTRA_CSS).split()) + '</style>' + header_markup()
            + '<footer class="chf" role="contentinfo">' + C.rosette() + '<div class="chf-w">'
            '<div class="chf-top"><a href="' + SITE + '/"><img src="' + B.LOGO + '" alt="Epic Travel Morocco"></a>'
            '<div class="chf-orn"><span></span>' + C.star() + '<span></span></div>'
            '<p class="chf-tag">Private journeys across Morocco, from the medinas of Marrakech to the silence of the Sahara.</p></div>'
            '<div class="chf-g">'
            '<div><h4>Explore</h4><ul>' + nav + '</ul></div>'
            '<div><h4>Popular tours</h4><ul>' + tours + '<li><a href="' + SITE + '/destination/">All tours</a></li></ul></div>'
            '<div><h4>Contact</h4>'
            '<a class="chf-c" href="tel:' + B.PHONE1 + '"><small>Morocco</small><b>' + B.PHONE1_T + '</b></a>'
            '<a class="chf-c" href="tel:' + B.PHONE2 + '"><small>Canada &amp; USA</small><b>' + B.PHONE2_T + '</b></a>'
            '<a class="chf-c" href="mailto:' + B.EMAIL + '"><small>Email</small>' + B.EMAIL + '</a></div>'
            '<div><h4>Visit &amp; follow</h4><p style="margin:0 0 18px">Gueliz, Marrakech 22000<br>Morocco</p>'
            '<div class="chf-soc"><a href="' + FB + '" target="_blank" rel="noopener" aria-label="Facebook">' + soc('fb') + '</a>'
            '<a href="' + IG + '" target="_blank" rel="noopener" aria-label="Instagram">' + soc('ig') + '</a>'
            '<a href="' + TA + '" target="_blank" rel="noopener" aria-label="Tripadvisor">' + soc('ta') + '</a></div></div>'
            '</div><div class="chf-cta"><p>Ready when you are. Let’s plan your Moroccan journey.</p><a href="' + SITE + '/contact-2/">Plan my trip</a></div></div>'
            '<div class="chf-bot"><div class="chf-w"><span>© 2026 Epic Travel Morocco. All rights reserved.</span><span>Private tours from Marrakech</span></div></div>'
            '</footer>' + JS + '</div>')


def chrome_widget(key='chrome'):
    """The chrome as an Elementor html widget (added at the end of every Elementor page)."""
    return C.widget('html', C.noq(chrome_html()), key)


def preview_footer():
    return chrome_html()


if __name__ == '__main__':
    html = C.noq(chrome_html())
    open(os.path.join(HERE, 'chrome-widget.html'), 'w').write(html)
    main = [{'id': C.eid('etf-main'), 'elType': 'container', 'isInner': False,
             'settings': {'content_width': 'full', 'flex_direction': 'column', 'flex_gap': C.GAP0, 'padding': C.PAD0},
             'elements': [C.widget('html', html, 'etf-main0')]}]
    s = json.dumps(main, ensure_ascii=False, separators=(',', ':'))
    assert '\\' not in s
    open(os.path.join(HERE, 'footer-3433.json'), 'w').write(s)
    print('chrome', len(html), 'footer-3433.json', len(s))
