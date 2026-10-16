"""Build the 8-slide Instagram carousel (1080x1350) for We Gravel Morocco.

Run: python3 make_carousel.py  -> PNGs in carousel-1/
"""
import os, subprocess, pathlib

HERE = pathlib.Path(__file__).resolve().parent
MEDIA = HERE.parent / "media"
OUT = HERE / "carousel-1"
TMP = OUT / "_html"
TMP.mkdir(parents=True, exist_ok=True)
CHROME = "/opt/pw-browsers/chromium"

GROUP = (MEDIA / "gravel-bike-group-high-atlas-morocco.jpg").as_uri()
SUNSET = (MEDIA / "gravel-bike-sunset-atlas-morocco.jpg").as_uri()
SUPPORT = (MEDIA / "bike-tour-4x4-support-morocco.jpg").as_uri()

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Inter,sans-serif;background:linear-gradient(180deg,#F3F7FF 0%,#FFFFFF 55%,#FAF5EE 100%);color:#313041;position:relative}
.top{display:flex;justify-content:space-between;align-items:center;padding:44px 60px 0}
.brand{font-weight:800;font-size:26px;letter-spacing:.5px;color:#313041}
.brand b{color:#E77717}
.count{font-weight:700;font-size:24px;color:#8A8FA3}
.kicker{padding:34px 60px 0;font-size:28px;font-weight:700;color:#3D6FE0;text-transform:uppercase;letter-spacing:2px}
h1{padding:6px 60px 0;font-size:96px;line-height:1;font-weight:900;color:#3D6FE0;letter-spacing:-2px}
h1.orange{color:#E77717}
.sub{padding:14px 60px 0;font-size:34px;line-height:1.3;color:#4A4E63;font-weight:500}
.card{margin:30px 60px 0;background:#fff;border-radius:34px;box-shadow:0 10px 40px rgba(49,48,65,.12);border:2px solid #E3E9F7;overflow:hidden}
.photo{height:520px;background-size:cover;background-position:center}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:2px solid #EEF1F8}
.stat{padding:22px 10px;text-align:center;border-right:2px solid #EEF1F8}
.stat:last-child{border-right:0}
.stat .v{font-size:40px;font-weight:900;color:#313041}
.stat .l{font-size:20px;color:#8A8FA3;font-weight:600;margin-top:4px;text-transform:uppercase;letter-spacing:1px}
.route{padding:22px 30px;font-size:27px;color:#4A4E63;line-height:1.4}
.route b{color:#313041}
.next{position:absolute;left:60px;right:60px;bottom:50px;display:flex;justify-content:space-between;align-items:center;background:#313041;color:#fff;border-radius:999px;padding:24px 34px;font-size:30px;font-weight:700}
.next span{color:#FFB46B}
.next .arrow{font-size:40px;line-height:1}
.brace{margin:22px auto 0;width:84%;height:40px;border:6px solid #3D6FE0;border-top:0;border-radius:0 0 40px 40px;position:relative}
.brace:after{content:"";position:absolute;left:50%;bottom:-24px;margin-left:-18px;width:36px;height:36px;border-right:6px solid #3D6FE0;border-bottom:6px solid #3D6FE0;transform:rotate(45deg);background:transparent}
.tagline{text-align:center;margin-top:30px;font-size:44px;font-weight:900;color:#3D6FE0}
.tagline small{display:block;font-size:28px;font-weight:600;color:#6B7088;margin-top:6px}
.chips{display:flex;flex-wrap:wrap;gap:14px;padding:22px 30px 26px}
.chip{background:#EEF3FF;color:#3D6FE0;border-radius:999px;padding:12px 22px;font-size:24px;font-weight:700}
.chip.o{background:#FFF1E3;color:#E77717}
.illus{height:520px;position:relative;overflow:hidden}
"""

def page(n, body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="top"><div class="brand">WE GRAVEL <b>MOROCCO</b></div><div class="count">{n}/8</div></div>
{body}</body></html>"""

def nxt(label):
    return f'<div class="next"><div>Next: <span>{label}</span></div><div class="arrow">→</div></div>'

def stats(items):
    return '<div class="stats">' + "".join(f'<div class="stat"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in items) + "</div>"

MOUNTAIN = """<div class="illus" style="background:linear-gradient(180deg,#BFD3FF 0%,#EAF0FF 70%)">
<div style="position:absolute;left:-60px;bottom:0;width:0;height:0;border-left:360px solid transparent;border-right:360px solid transparent;border-bottom:330px solid #8C9BC4"></div>
<div style="position:absolute;right:-80px;bottom:0;width:0;height:0;border-left:340px solid transparent;border-right:340px solid transparent;border-bottom:300px solid #9AA8CE"></div>
<div style="position:absolute;left:50%;margin-left:-330px;bottom:0;width:0;height:0;border-left:330px solid transparent;border-right:330px solid transparent;border-bottom:450px solid #313041"></div>
<div style="position:absolute;left:50%;margin-left:-95px;bottom:320px;width:0;height:0;border-left:95px solid transparent;border-right:95px solid transparent;border-bottom:130px solid #fff"></div>
<div style="position:absolute;left:50%;top:26px;transform:translateX(-50%);background:#E77717;color:#fff;font-weight:900;font-size:40px;padding:10px 26px;border-radius:999px">4,167 m</div>
<div style="position:absolute;left:30px;bottom:24px;background:rgba(255,255,255,.9);border-radius:16px;padding:10px 18px;font-size:22px;font-weight:700">Imlil 1,740 m → Refuge 3,200 m → Summit</div>
</div>"""

DUNES = """<div class="illus" style="background:linear-gradient(180deg,#FFD9A8 0%,#FFF1DC 60%)">
<div style="position:absolute;right:120px;top:70px;width:150px;height:150px;border-radius:50%;background:#E77717;opacity:.9"></div>
<div style="position:absolute;left:-200px;bottom:-260px;width:900px;height:520px;border-radius:50%;background:#E9A55B"></div>
<div style="position:absolute;right:-260px;bottom:-300px;width:1000px;height:560px;border-radius:50%;background:#D88A3A"></div>
<div style="position:absolute;left:-100px;bottom:-380px;width:1300px;height:560px;border-radius:50%;background:#C47528"></div>
<div style="position:absolute;left:30px;top:30px;background:rgba(255,255,255,.92);border-radius:16px;padding:10px 18px;font-size:22px;font-weight:700">M'Hamid → Erg Chegaga dunes</div>
<div style="position:absolute;left:0;right:0;bottom:30px;text-align:center;font-size:90px">🐪 🐪 🐪</div>
</div>"""

MONTHS = ["J","F","M","A","M","J","J","A","S","O","N","D"]
def bar(label, on, color):
    cells = "".join(f'<div style="flex:1;height:54px;border-radius:10px;background:{color if i in on else "#EEF1F8"};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px;color:{"#fff" if i in on else "#A3A8BA"}">{m}</div>' for i, m in enumerate(MONTHS))
    return f'<div style="padding:18px 30px 6px;font-size:28px;font-weight:800">{label}</div><div style="display:flex;gap:6px;padding:0 30px 10px">{cells}</div>'

SLIDES = [
    # 1 cover
    f"""<div class="kicker">Bike tour Morocco · Trekking Morocco</div>
<h1>Ride or hike<br>Morocco?</h1>
<div class="sub">5 ways to explore the Atlas &amp; the Sahara with local guides. Swipe to find yours.</div>
<div class="card"><div class="photo" style="background-image:url('{GROUP}');height:560px"></div>
<div class="chips"><div class="chip">Gravel</div><div class="chip">MTB</div><div class="chip">E-bike</div><div class="chip o">Toubkal</div><div class="chip o">Sahara</div></div></div>
{nxt("Gravel on the Caravan Road")}""",
    # 2 caravan road
    f"""<div class="kicker">01 · Gravel bike tour</div>
<h1>Caravan<br>Road</h1>
<div class="sub">Old caravan tracks of southern Morocco, almost no cars.</div>
<div class="card"><div class="photo" style="background-image:url('{SUNSET}')"></div>
{stats([("8","days"),("281","km"),("3,700","m climb"),("1,100€","from")])}
<div class="route"><b>Route:</b> Skoura oasis · Rose Valley · Dades Gorges · Saghro</div></div>
{nxt("Atlas to Sahara by bike")}""",
    # 3 atlas to sahara
    f"""<div class="kicker">02 · Cycling tour</div>
<h1>Atlas →<br>Sahara</h1>
<div class="sub">From the High Atlas to a night in the Chegaga dunes.</div>
<div class="card"><div class="photo" style="background-image:url('{SUPPORT}')"></div>
{stats([("6","ride days"),("~300","km"),("4x4","support"),("1,100€","from")])}
<div class="route"><b>Ride it on:</b> gravel bike, mountain bike or e-bike</div></div>
{nxt("Hike &amp; Bike")}""",
    # 4 hike and bike
    f"""<div class="kicker">03 · Hike &amp; Bike</div>
<h1>Walk 2 days,<br>ride 3</h1>
<div class="sub">Perfect for mixed groups: hikers and riders on one trip.</div>
<div class="card"><div class="photo" style="background-image:url('{GROUP}');background-position:center 30%"></div>
{stats([("8","days"),("160","km ride"),("Easy","level"),("1,050€","from")])}
<div class="route"><b>Route:</b> Happy Valley (Ait Bouguemez) · Bin El Ouidane lake · Ouzoud waterfalls</div></div>
{nxt("Climb Toubkal")}""",
    # 5 toubkal
    f"""<div class="kicker">04 · Trekking</div>
<h1 class="orange">Toubkal</h1>
<div class="sub">The highest peak in North Africa. No climbing skills needed.</div>
<div class="card">{MOUNTAIN}
{stats([("3","days"),("4,167","metres"),("Mules","carry bags"),("380€","from")])}
<div class="route"><b>Best months:</b> April–June &amp; September–October</div></div>
{nxt("Sahara desert trek")}""",
    # 6 sahara
    f"""<div class="kicker">05 · Desert trek</div>
<h1 class="orange">Sahara</h1>
<div class="sub">Walk with camels, sleep under the stars, tea around the fire.</div>
<div class="card">{DUNES}
{stats([("8","days"),("4","walk days"),("Easy","level"),("1,050€","from")])}
<div class="route"><b>Season:</b> September to May · great for families</div></div>
{nxt("When should you go?")}""",
    # 7 when to go
    f"""<div class="kicker">Save this ✦</div>
<h1>When to go</h1>
<div class="sub">Morocco has a season for every adventure.</div>
<div class="card" style="padding:10px 0 24px">
{bar("🚵 Bike tours", [2,3,4,5,6,7,8,9,10], "#3D6FE0")}
{bar("🏜️ Sahara treks", [0,1,2,3,4,8,9,10,11], "#E77717")}
{bar("⛰️ Toubkal (no snow)", [3,4,5,8,9], "#313041")}
<div style="padding:20px 30px 0;font-size:26px;color:#4A4E63;line-height:1.4">Sweet spot for everything: <b>April–May</b> and <b>September–October</b>.</div>
</div>
<div class="brace"></div>
<div class="tagline">Pick your trip<small>All tours start in Marrakech</small></div>
{nxt("How to book")}""",
    # 8 CTA
    f"""<div class="kicker">Your next step</div>
<h1>Which one<br>is yours?</h1>
<div class="sub">Comment <b style="color:#3D6FE0">BIKE</b> or <b style="color:#E77717">TREK</b> and we'll send you the full itinerary.</div>
<div class="card" style="padding:30px">
<div style="display:flex;flex-direction:column;gap:22px;font-size:32px;font-weight:700">
<div style="display:flex;align-items:center;gap:20px"><div style="width:70px;height:70px;border-radius:20px;background:#EEF3FF;display:flex;align-items:center;justify-content:center;font-size:38px">🔗</div>Link in bio · wegravelmorocco.com</div>
<div style="display:flex;align-items:center;gap:20px"><div style="width:70px;height:70px;border-radius:20px;background:#E6F9EE;display:flex;align-items:center;justify-content:center;font-size:38px">💬</div>WhatsApp +212 660 435 569</div>
<div style="display:flex;align-items:center;gap:20px"><div style="width:70px;height:70px;border-radius:20px;background:#FFF1E3;display:flex;align-items:center;justify-content:center;font-size:38px">🧭</div>Private tours on your dates</div>
<div style="display:flex;align-items:center;gap:20px"><div style="width:70px;height:70px;border-radius:20px;background:#F1EEF8;display:flex;align-items:center;justify-content:center;font-size:38px">⚡</div>We reply within 24 hours</div>
</div></div>
<div class="brace"></div>
<div class="tagline">Local guides from the Atlas<small>Small groups · 4x4 support · mules · airport transfers</small></div>
<div class="next" style="background:#E77717"><div>Save &amp; share with your travel buddy</div><div class="arrow">↗</div></div>""",
]

for i, body in enumerate(SLIDES, 1):
    html = TMP / f"slide-{i}.html"
    html.write_text(page(i, body), encoding="utf-8")
    png = OUT / f"slide-{i}.png"
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--force-device-scale-factor=1",
                    "--window-size=1080,1600", f"--screenshot={png}", html.as_uri()],
                   check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    from PIL import Image
    Image.open(png).convert("RGB").crop((0, 0, 1080, 1350)).save(png)
    print(png)
