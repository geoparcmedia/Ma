"""Artistic version of the SEO/AEO/GEO/AIO/SXO carousel.

One 8640x1350 panorama (dark base, neon mesh gradients, grain, a ribbon that
flows across every slide) cut into 8 slides of 1080x1350.
Run: python3 make_seo_art.py  -> PNGs in carousel-seo-art/
"""
import subprocess, pathlib
from PIL import Image
import make_seo_carousel as base

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "carousel-seo-art"
OUT.mkdir(exist_ok=True)
W, H, N = 1080, 1350, 8
HANDLE = "@wegravel_morocco"

# neon accent per slide: (accent, second, title gradient)
ACC = {
 1: ("#FF3CAC", "#FDE047"), 2: ("#3D8BFF", "#22D3EE"), 3: ("#00E5A0", "#C6FF00"),
 4: ("#FF6A3D", "#FFD23F"), 5: ("#B26BFF", "#FF3CAC"), 6: ("#FF3C78", "#FFB13D"),
 7: ("#22D3EE", "#B26BFF"), 8: ("#FFD23F", "#FF3CAC"),
}

blobs = []
for i in range(N):
    a, b = ACC[i + 1]
    x = i * W
    blobs.append(f"radial-gradient(520px 520px at {x + 900}px 160px,{a}cc,transparent 70%)")
    blobs.append(f"radial-gradient(460px 460px at {x + 120}px 1150px,{b}99,transparent 70%)")
BG = ",".join(blobs) + ",linear-gradient(90deg,#12062E,#0B1033 30%,#071F2B 45%,#1E0B2E 60%,#14082E 80%,#0B0B2B)"

# ribbon path across the whole panorama
pts = []
for i in range(N * 2 + 1):
    x = i * W / 2
    y = 1215 if i % 2 == 0 else 1290
    pts.append((x, y))
d = f"M -50 1240 " + " ".join(f"S {x - 270:.0f} {y + (60 if k % 2 else -60)} {x:.0f} {y}" for k, (x, y) in enumerate(pts[1:], 1))
stops = "".join(f'<stop offset="{i / (N - 1):.3f}" stop-color="{ACC[i + 1][0]}"/>' for i in range(N))

CSS = base.CSS.split("/* vivid theme */")[0] + f"""
html,body{{width:{W * N}px;height:{H}px;overflow:hidden}}
body{{background:{BG};color:#fff;font-family:Inter,sans-serif}}
.grain{{position:absolute;inset:0;opacity:.18;mix-blend-mode:overlay;z-index:5;pointer-events:none}}
.sl{{position:absolute;top:0;width:{W}px;height:{H}px;overflow:visible}}
.ghost{{position:absolute;right:-30px;top:330px;font-size:400px;font-weight:900;line-height:.8;color:transparent;-webkit-text-stroke:3px rgba(255,255,255,.14);letter-spacing:-12px;z-index:0}}
.hd{{position:absolute;left:60px;top:46px;display:flex;align-items:center;gap:14px;font-weight:800;font-size:24px;z-index:3}}
.hd .av{{width:48px;height:48px;border-radius:50%;background:conic-gradient(var(--a),var(--b),var(--a));padding:3px}}
.hd .av div{{width:100%;height:100%;border-radius:50%;background:#12062E;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:22px}}
.pg{{position:absolute;right:60px;top:56px;font-weight:800;font-size:22px;color:rgba(255,255,255,.7);z-index:3}}
.sticker{{position:absolute;right:70px;top:120px;width:170px;height:170px;border-radius:50%;background:var(--b);color:#12062E;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(12deg);font-weight:900;box-shadow:0 0 0 8px rgba(255,255,255,.12),0 20px 50px rgba(0,0,0,.35);z-index:3}}
.sticker b{{font-size:64px;line-height:1}}
.sticker span{{font-size:18px;letter-spacing:2px;text-transform:uppercase}}
.kk{{position:absolute;left:60px;top:132px;font-size:24px;font-weight:800;letter-spacing:4px;text-transform:uppercase;color:var(--b);z-index:3}}
.ttl{{position:absolute;left:54px;top:160px;font-size:170px;font-weight:900;line-height:1;letter-spacing:-6px;background:linear-gradient(100deg,#fff 10%,var(--b) 55%,var(--a) 95%);-webkit-background-clip:text;color:transparent;z-index:3}}
.ff{{position:absolute;left:62px;top:345px;font-size:32px;font-weight:600;color:rgba(255,255,255,.88);z-index:3}}
.ff i{{font-style:normal;background:var(--a);color:#fff;padding:2px 12px;border-radius:8px}}
.glass{{position:absolute;left:44px;top:405px;width:{W - 88}px;padding:16px;border-radius:40px;background:rgba(255,255,255,.10);border:2px solid rgba(255,255,255,.28);backdrop-filter:blur(8px);box-shadow:0 30px 80px rgba(0,0,0,.4);transform:rotate(-1.2deg);z-index:3}}
.glass .card{{margin:0;height:400px;border:0;box-shadow:none;color:#22253A}}
.goal2{{position:absolute;left:60px;top:860px;z-index:3}}
.goal2 .w{{display:inline-block;font-size:62px;font-weight:900;color:#12062E;background:linear-gradient(90deg,var(--b),var(--a));padding:4px 22px 8px;border-radius:14px;transform:rotate(-2deg)}}
.goal2 .sm{{font-size:28px;font-weight:600;color:rgba(255,255,255,.85);margin-top:14px}}
.tips{{position:absolute;left:60px;right:60px;top:1010px;display:flex;flex-direction:column;gap:12px;z-index:3}}
.tips div{{font-size:26px;line-height:1.3;padding-left:50px;position:relative;color:rgba(255,255,255,.92)}}
.tips div:before{{content:"";position:absolute;left:0;top:4px;width:30px;height:30px;border-radius:9px;background:linear-gradient(135deg,var(--b),var(--a));transform:rotate(45deg) scale(.8)}}
.tips b{{color:#fff}}
.sw{{position:absolute;right:40px;bottom:58px;display:flex;align-items:center;gap:12px;background:#fff;color:#12062E;font-weight:900;font-size:24px;padding:14px 22px;border-radius:999px;transform:rotate(-4deg);box-shadow:0 14px 40px rgba(0,0,0,.35);z-index:4}}
.sw span{{color:var(--a)}}
.star{{position:absolute;z-index:2;font-size:60px;color:var(--b);text-shadow:0 0 30px var(--b)}}
.ring{{position:absolute;z-index:1;border-radius:50%;border:3px dashed rgba(255,255,255,.25)}}
"""

GRAIN = """<svg class="grain" width="100%" height="100%"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>"""
RIBBON = f"""<svg style="position:absolute;left:0;top:0;z-index:2" width="{W * N}" height="{H}"><defs><linearGradient id="rg" x1="0" x2="1">{stops}</linearGradient></defs>
<path d="{d}" fill="none" stroke="url(#rg)" stroke-width="34" stroke-linecap="round" opacity=".95"/>
<path d="{d}" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="2 18" stroke-linecap="round" opacity=".7" transform="translate(0,-40)"/></svg>"""

def wrap(n, inner, ghost=""):
    a, b = ACC[n]
    deco = f'<div class="star" style="left:{60 + (n * 97) % 300}px;top:{300 + (n * 53) % 60}px">✦</div><div class="ring" style="width:260px;height:260px;left:{700 - (n * 41) % 200}px;top:{820 + (n * 29) % 80}px"></div>'
    return f"""<div class="sl" style="left:{(n - 1) * W}px;--a:{a};--b:{b}">
<div class="ghost">{ghost}</div>{deco}
<div class="hd"><div class="av"><div>W</div></div>{HANDLE}</div><div class="pg">{n}/{N}</div>
{inner}</div>"""

def sw(label):
    return f'<div class="sw">{label} <span>→</span></div>'

def section(n, kicker, title, full, card, goal, goal_sub, todo, next_label):
    tips = "".join(f"<div>{t}</div>" for t in todo)
    return wrap(n, f"""<div class="sticker"><b>0{n - 1}</b><span>of 05</span></div>
<div class="kk">{kicker}</div><div class="ttl">{title}</div><div class="ff">{full}</div>
<div class="glass"><div class="card">{card}</div></div>
<div class="goal2"><div class="w">{goal}</div><div class="sm">{goal_sub}</div></div>
<div class="tips">{tips}</div>{sw(next_label)}""", title)

LIST = "".join(
    f'<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.10);border:2px solid rgba(255,255,255,.25);border-radius:24px;padding:13px 24px;transform:rotate({r}deg)"><div style="width:120px;font-size:42px;font-weight:900;color:{c}">{a}</div><div style="font-size:28px;font-weight:700">{b}</div></div>'
    for (a, b), c, r in zip([("SEO", "Rank on page 1"), ("AEO", "Be in the answer box"), ("GEO", "Be the AI recommendation"), ("AIO", "Be understood by AI"), ("SXO", "Turn visits into clients")],
                            [ACC[i][0] for i in range(2, 7)], [-1, 1, -1, 1, -1]))

S1 = wrap(1, f"""<div class="sticker" style="width:200px;height:200px"><b style="font-size:44px">2026</b><span>search guide</span></div>
<div class="kk">Search has changed</div>
<div class="ttl" style="font-size:136px;line-height:.95;top:170px">SEO is<br>not enough<br>anymore.</div>
<div class="ff" style="top:590px;line-height:1.4;width:900px">People find brands on Google, in AI answers and chat assistants. <i>5 optimizations</i> your website needs now:</div>
<div style="position:absolute;left:60px;right:60px;top:720px;display:flex;flex-direction:column;gap:12px;z-index:3">{LIST}</div>
{sw("Swipe")}""", "SEO")

ROWS = [("SEO", "Rank on page 1", "Google results", "Positions, clicks"), ("AEO", "Be the answer", "AI Overviews, snippets", "Answer boxes won"),
        ("GEO", "Be recommended", "ChatGPT, Gemini, Perplexity", "Brand mentions"), ("AIO", "Be understood", "All AI systems", "Schema, entity data"),
        ("SXO", "Convert visits", "Your website", "Bookings, sales, leads")]
TABLE = '<table><tr><th></th><th>Goal</th><th>Where</th><th>Measure</th></tr>' + "".join(
    f'<tr><td style="color:{ACC[i + 2][0]}">{a}</td><td>{b}</td><td>{c}</td><td>{e}</td></tr>' for i, (a, b, c, e) in enumerate(ROWS)) + "</table>"
S7 = wrap(7, f"""<div class="sticker"><b style="font-size:40px">SAVE</b><span>this one</span></div>
<div class="kk">The cheat sheet</div><div class="ttl" style="font-size:150px">Cheat<br>sheet</div>
<div class="glass" style="top:500px"><div class="card" style="height:auto;padding:0;overflow:hidden">{TABLE}</div></div>
<div class="goal2" style="top:900px"><div class="w">One strategy, 5 layers</div><div class="sm">Each layer builds on the one before</div></div>
{sw("Quick check")}""", "5")

CHECK = "".join(
    f'<div style="display:flex;gap:20px;align-items:center;padding:14px 0;border-bottom:2px solid #EEF1F8;font-size:27px"><div style="width:46px;height:46px;border:4px solid {ACC[i + 2][0]};border-radius:12px;flex:none"></div><div><b style="color:{ACC[i + 2][0]}">{a}</b> · {b}</div></div>'
    for i, (a, b) in enumerate([("SEO", "My main pages rank in the top 10"), ("AEO", "Each page answers the question in 2 sentences"),
                                ("GEO", "Other sites mention my brand"), ("AIO", "My site has schema markup"), ("SXO", "A visitor can buy or book in 2 clicks")]))
S8 = wrap(8, f"""<div class="sticker"><b style="font-size:40px">5 MIN</b><span>check</span></div>
<div class="kk">Your next step</div><div class="ttl" style="font-size:150px">Quick<br>check</div>
<div class="glass" style="top:500px"><div class="card" style="height:auto;padding:18px 30px">{CHECK}</div></div>
<div class="goal2" style="top:960px"><div class="w">Missed one?</div><div class="sm">Save this · Follow {HANDLE} for more</div></div>
<div class="sw" style="background:linear-gradient(90deg,#FFD23F,#FF3CAC);color:#12062E">Follow <span style="color:#12062E">↗</span></div>""", "✓")

SL = [S1,
      section(2, "01 · The foundation", "SEO", "Search <i>Engine</i> Optimization", base.SEO_CARD, "Rankings", "Rank on page 1 of Google",
              ["<b>One page per search intent</b>, keyword in title, H1 and URL", "<b>Fast, mobile-friendly pages</b> Google can crawl", "<b>Links from trusted sites</b> in your niche"], "AEO"),
      section(3, "02 · Answers first", "AEO", "Answer <i>Engine</i> Optimization", base.AEO_CARD, "Answers", "Be the answer in the box",
              ["<b>Answer in the first 2–3 sentences</b> of the page", "<b>Questions as headings</b>, short direct answers", "<b>FAQ, tables and lists</b> that are easy to quote"], "GEO"),
      section(4, "03 · AI assistants", "GEO", "Generative <i>Engine</i> Optimization", base.GEO_CARD, "Recommendation", "Be the brand AI recommends",
              ["<b>Get mentioned on other sites</b>: reviews, lists, press", "<b>Exact facts</b>: prices, numbers, dates, places", "<b>Same name and details</b> everywhere online"], "AIO"),
      section(5, "04 · Machine-readable", "AIO", "<i>AI</i> Optimization", base.AIO_CARD, "AI Visibility", "Be understood across AI systems",
              ["<b>Schema markup</b>: Organization, Product, FAQ, Review", "<b>Clear entity</b>: who you are, what you do, where", "<b>Link related pages</b> so AI sees the full picture"], "SXO"),
      section(6, "05 · Visit to client", "SXO", "Search <i>Experience</i> Optimization", base.SXO_CARD, "Experience", "Make the next step effortless",
              ["<b>Match the intent</b> of the search", "<b>Load in under 2.5 s</b> on mobile", "<b>One clear call to action</b>: buy, book, contact"], "Cheat sheet"),
      S7, S8]

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{RIBBON}{''.join(SL)}{GRAIN}</body></html>"""
src = OUT / "_panorama.html"
src.write_text(html, encoding="utf-8")
pano = OUT / "_panorama.png"
subprocess.run(["/opt/pw-browsers/chromium", "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                "--force-device-scale-factor=1", f"--window-size={W * N},{H + 250}", f"--screenshot={pano}", src.as_uri()],
               check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
im = Image.open(pano).convert("RGB")
for i in range(N):
    im.crop((i * W, 0, (i + 1) * W, H)).save(OUT / f"slide-{i + 1}.png")
im.crop((0, 0, W * N, H)).resize((W * N // 4, H // 4)).save(OUT / "_preview.jpg", quality=85)
print("ok")
