"""Build the 8-slide educational Instagram carousel (1080x1350):
SEO, AEO, GEO, AIO and SXO explained.

Run: python3 make_seo_carousel.py  -> PNGs in carousel-seo/
"""
import subprocess, pathlib
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "carousel-seo"
TMP = OUT / "_html"
TMP.mkdir(parents=True, exist_ok=True)
CHROME = "/opt/pw-browsers/chromium"
BLUE, ORANGE, DARK = "#3D6FE0", "#E77717", "#22253A"

CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:Inter,sans-serif;background:linear-gradient(180deg,#EEF3FF 0%,#FFFFFF 50%,#F6F8FD 100%);color:{DARK};position:relative}}
.top{{display:flex;justify-content:space-between;align-items:center;padding:44px 60px 0;font-weight:800;font-size:24px;color:#8A8FA3;letter-spacing:1px}}
.kicker{{padding:30px 60px 0;font-size:26px;font-weight:800;color:{ORANGE};text-transform:uppercase;letter-spacing:3px}}
h1{{padding:2px 60px 0;font-size:120px;line-height:1;font-weight:900;color:{BLUE};letter-spacing:-3px}}
.full{{padding:6px 60px 0;font-size:34px;color:{BLUE};font-weight:600}}
.card{{margin:26px 60px 0;background:#fff;border-radius:30px;box-shadow:0 10px 40px rgba(34,37,58,.10);border:2px solid #DCE4F7;padding:26px 30px;height:430px;overflow:hidden}}
.brace{{margin:20px auto 0;width:80%;height:34px;border:6px solid {BLUE};border-top:0;border-radius:0 0 36px 36px;position:relative}}
.brace:after{{content:"";position:absolute;left:50%;bottom:-20px;margin-left:-15px;width:30px;height:30px;border-right:6px solid {BLUE};border-bottom:6px solid {BLUE};transform:rotate(45deg)}}
.goal{{text-align:center;margin-top:24px;font-size:46px;font-weight:900;color:{BLUE}}}
.goal small{{display:block;font-size:28px;font-weight:600;color:#5C6178;margin-top:4px}}
.do{{margin:22px 60px 0;display:flex;flex-direction:column;gap:12px}}
.do div{{font-size:27px;line-height:1.3;padding-left:46px;position:relative;color:#3B3F55}}
.do div:before{{content:"✓";position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;background:#E6F9EE;color:#1E9E57;font-weight:900;font-size:20px;display:flex;align-items:center;justify-content:center}}
.do b{{color:{DARK}}}
.next{{position:absolute;left:60px;right:60px;bottom:48px;display:flex;justify-content:space-between;align-items:center;background:{DARK};color:#fff;border-radius:999px;padding:24px 34px;font-size:30px;font-weight:700}}
.next span{{color:#FFB46B}}
/* mock UI */
.g{{font-size:40px;font-weight:800;letter-spacing:-1px}}
.g i{{font-style:normal}}
.search{{margin-top:14px;border:2px solid #DADCE0;border-radius:999px;padding:12px 22px;font-size:22px;color:#3C4043;display:flex;justify-content:space-between}}
.res{{display:flex;gap:16px;margin-top:18px;align-items:flex-start}}
.num{{flex:none;width:38px;height:38px;border-radius:50%;background:{BLUE};color:#fff;font-weight:800;font-size:20px;display:flex;align-items:center;justify-content:center}}
.res .t{{font-size:24px;color:#1A3FA8;font-weight:700}}
.res .u{{font-size:18px;color:#1E7A3C;margin-top:2px}}
.res .d{{font-size:18px;color:#5F6368;margin-top:2px}}
.line{{height:12px;border-radius:6px;background:#E3E7F0;margin-top:12px}}
.aio{{margin-top:16px;border:2px solid #C9D7FA;background:#F3F7FF;border-radius:20px;padding:18px 22px}}
.aio .h{{font-size:20px;color:{BLUE};font-weight:700}}
.aio .a{{font-size:26px;font-weight:800;margin-top:10px;line-height:1.25}}
.aio .s{{font-size:19px;color:#4A4E63;margin-top:8px;line-height:1.35}}
.src{{margin-top:12px;display:inline-flex;gap:10px;align-items:center;background:#fff;border:2px solid #DCE4F7;border-radius:14px;padding:8px 14px;font-size:18px;font-weight:700}}
.bubble{{margin-left:auto;width:62%;background:#F0F1F5;border-radius:20px;padding:14px 18px;font-size:21px}}
.chat{{font-size:21px;line-height:1.45;margin-top:16px;color:#2B2E40}}
.pick{{margin-top:14px;display:flex;gap:16px;align-items:center;border:2px solid #FFD8B0;background:#FFF6EC;border-radius:18px;padding:14px 18px}}
.pick .ic{{width:64px;height:64px;border-radius:14px;background:{ORANGE};color:#fff;display:flex;align-items:center;justify-content:center;font-size:34px}}
.pick .n{{font-size:23px;font-weight:800}}
.pick .m{{font-size:18px;color:#5C6178}}
.flow{{display:flex;align-items:center;gap:14px;margin-top:10px}}
.box{{border:2px solid #DCE4F7;border-radius:18px;padding:14px;background:#F8FAFF;font-size:19px;font-weight:700;text-align:center}}
.pill{{display:flex;align-items:center;gap:12px;border:2px solid #DCE4F7;border-radius:16px;padding:12px 16px;font-size:21px;font-weight:700;background:#fff}}
.pill .i{{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px}}
.arrow{{font-size:34px;color:{BLUE};font-weight:900}}
table{{width:100%;border-collapse:collapse;font-size:21px}}
th{{background:{DARK};color:#fff;text-align:left;padding:12px 12px;font-size:20px}}
td{{padding:12px 12px;border-bottom:2px solid #EEF1F8;vertical-align:top;line-height:1.3}}
td:first-child{{font-weight:900;color:{BLUE};font-size:24px}}
"""
CSS += """
/* vivid theme */
body.v{background:var(--bg);color:#fff}
body.v:before,body.v:after{content:"";position:absolute;border-radius:50%;filter:blur(10px);opacity:.35;z-index:0}
body.v:before{width:620px;height:620px;right:-260px;top:-200px;background:var(--b1)}
body.v:after{width:520px;height:520px;left:-240px;bottom:120px;background:var(--b2)}
body.v>*{position:relative;z-index:1}
body.v>.next,body.v>.dots{position:absolute}
body.v .card{color:#22253A}
body.v .top{color:rgba(255,255,255,.85)}
body.v .handle{display:flex;align-items:center;gap:12px;color:#fff}
body.v .handle .av{width:46px;height:46px;border-radius:50%;background:#fff;color:var(--acc);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:22px}
body.v .kicker{color:var(--k)}
body.v h1{color:#fff;text-shadow:0 6px 30px rgba(0,0,0,.18)}
body.v .full{color:rgba(255,255,255,.92)!important}
body.v .card{border:0;box-shadow:0 24px 60px rgba(0,0,0,.25)}
body.v .brace{border-color:#fff}
body.v .brace:after{border-color:#fff}
body.v .goal{color:#fff}
body.v .goal small{color:rgba(255,255,255,.85)}
body.v .do div{color:rgba(255,255,255,.95)}
body.v .do b{color:#fff}
body.v .do div:before{background:#fff;color:var(--acc)}
body.v .next{background:#fff;color:#22253A;box-shadow:0 14px 40px rgba(0,0,0,.25)}
body.v .next span{color:var(--acc)}
body.v .dots{position:absolute;left:0;right:0;bottom:16px;display:flex;justify-content:center;gap:10px}
body.v .dots i{width:10px;height:10px;border-radius:50%;background:rgba(255,255,255,.45)}
body.v .dots i.on{width:34px;border-radius:6px;background:#fff}
"""

THEMES = {
 1: ("linear-gradient(150deg,#4F46E5 0%,#7C3AED 45%,#DB2777 100%)", "#F472B6", "#22D3EE", "#FDE047", "#7C3AED"),
 2: ("linear-gradient(150deg,#2563EB 0%,#1D4ED8 40%,#7C3AED 100%)", "#22D3EE", "#A78BFA", "#FDE047", "#2563EB"),
 3: ("linear-gradient(150deg,#059669 0%,#0D9488 45%,#0EA5E9 100%)", "#A3E635", "#22D3EE", "#FEF08A", "#0D9488"),
 4: ("linear-gradient(150deg,#F97316 0%,#EF4444 50%,#DB2777 100%)", "#FDE047", "#F472B6", "#FEF3C7", "#EF4444"),
 5: ("linear-gradient(150deg,#7C3AED 0%,#6D28D9 45%,#2563EB 100%)", "#F0ABFC", "#38BDF8", "#FDE047", "#7C3AED"),
 6: ("linear-gradient(150deg,#EC4899 0%,#F43F5E 45%,#F59E0B 100%)", "#FDE047", "#A78BFA", "#FFF7ED", "#F43F5E"),
 7: ("linear-gradient(150deg,#0F172A 0%,#1E3A8A 55%,#7C3AED 100%)", "#22D3EE", "#F472B6", "#FDE047", "#2563EB"),
 8: ("linear-gradient(150deg,#F59E0B 0%,#F97316 40%,#E11D48 100%)", "#FDE047", "#DB2777", "#FFFFFF", "#F97316"),
}

def page(n, body):
    bg, b1, b2, k, acc = THEMES[n]
    dots = "".join(f'<i class="{"on" if i == n else ""}"></i>' for i in range(1, 9))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="v" style="--bg:{bg};--b1:{b1};--b2:{b2};--k:{k};--acc:{acc}">
<div class="top"><div class="handle"><div class="av">W</div>@wegravel_morocco</div><div>{n}/8</div></div>{body}<div class="dots">{dots}</div></body></html>"""

def _old_page(n, body):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
{body}</body></html>"""

def nxt(label, last=False):
    if last:
        return '<div class="next"><div>Save it · Follow <span>@wegravel_morocco</span></div><div>↗</div></div>'
    return f'<div class="next"><div>Next: <span>{label}</span></div><div style="font-size:40px">→</div></div>'

def section(n, kicker, title, full, card, goal, goal_sub, todo, next_label):
    items = "".join(f"<div>{t}</div>" for t in todo)
    return page(n, f"""<div class="kicker">{kicker}</div><h1>{title}</h1><div class="full">{full}</div>
<div class="card">{card}</div><div class="brace"></div>
<div class="goal">{goal}<small>{goal_sub}</small></div>
<div class="do">{items}</div>{nxt(next_label)}""")

GOOGLE = '<div class="g"><i style="color:#4285F4">G</i><i style="color:#EA4335">o</i><i style="color:#FBBC05">o</i><i style="color:#4285F4">g</i><i style="color:#34A853">l</i><i style="color:#EA4335">e</i></div>'
Q = '<div class="search"><span>best hiking boots for beginners</span><span>🔍</span></div>'

SEO_CARD = GOOGLE + Q + "".join(
    f'<div class="res"><div class="num">{i}</div><div><div class="t">{t}</div><div class="u">{u}</div><div class="d">{d}</div></div></div>'
    for i, t, u, d in [
        (1, "10 Best Hiking Boots for Beginners", "yourbrand.com/guides/hiking-boots", "Tested on 300 km of trails. Fit, grip and price compared."),
        (2, "Beginner Hiking Boots: Buying Guide", "outdoorshop.example/boots", "How to choose size, sole and waterproofing."),
        (3, "Hiking Boots Reviews 2026", "trailblog.example/reviews", "Our top picks for comfort and support."),
    ])

AEO_CARD = GOOGLE + Q + """<div class="aio"><div class="h">✦ AI Overview</div>
<div class="a">For beginners, choose a light, waterproof mid-cut boot with a grippy sole.</div>
<div class="s">Go half a size up for thick socks and break them in on short walks before a long trek.</div>
<div class="src">🥾 yourbrand.com · Hiking boots guide</div></div><div class="line" style="width:70%"></div><div class="line" style="width:45%"></div>"""

GEO_CARD = """<div style="display:flex;justify-content:space-between;align-items:center"><div style="font-size:36px">💬</div><div style="font-size:20px;color:#8A8FA3;font-weight:700">AI assistant</div></div>
<div class="bubble">What are the best hiking boots for a beginner?</div>
<div class="chat">For a first pair, look for:<br>• a waterproof membrane<br>• mid-cut ankle support<br>• a light, flexible sole<br>Here is my top pick:</div>
<div class="pick"><div class="ic">🥾</div><div><div class="n">YourBrand Trail Mid WP</div><div class="m">89 € · yourbrand.com + 3 shops · ★ 4.6 (1,200 reviews)</div></div></div>"""

AIO_CARD = """<div style="display:flex;align-items:center;gap:20px;height:100%">
<div class="box" style="width:250px;padding:20px"><div style="font-size:60px">🌐</div>Your website content</div>
<div class="arrow">→</div>
<div style="width:110px;height:110px;border-radius:50%;background:#22253A;color:#fff;display:flex;align-items:center;justify-content:center;font-size:54px;flex:none">✦</div>
<div class="arrow">→</div>
<div style="display:flex;flex-direction:column;gap:14px;flex:1">
<div class="pill"><div class="i" style="background:#3D6FE0">&lt;/&gt;</div>Structured data</div>
<div class="pill"><div class="i" style="background:#1E9E57">👤</div>Entity clarity</div>
<div class="pill"><div class="i" style="background:#E77717">🔗</div>Connected content</div>
</div></div>"""

SXO_CARD = """<div style="display:flex;align-items:center;gap:14px;margin-top:6px">
<div class="box" style="flex:1"><div style="font-size:44px">🔍</div>Search visitor<div style="font-size:16px;color:#8A8FA3;font-weight:600;margin-top:6px">"hiking boots"</div></div>
<div class="arrow">→</div>
<div class="box" style="flex:1.2"><div style="font-size:44px">📄</div>Useful page<div style="font-size:16px;color:#8A8FA3;font-weight:600;margin-top:6px">answer first, fast</div></div>
<div class="arrow">→</div>
<div style="flex:1.2;display:flex;flex-direction:column;gap:10px">
<div class="pill" style="font-size:19px">🛒 Buy</div><div class="pill" style="font-size:19px">📖 Read guide</div><div class="pill" style="font-size:19px">💬 Get help</div></div></div>
<div style="display:flex;gap:12px;margin-top:26px">
<div class="pill" style="flex:1;font-size:19px">🎯 Intent match</div><div class="pill" style="flex:1;font-size:19px">⚡ Fast page</div><div class="pill" style="flex:1;font-size:19px">➡️ Clear next step</div></div>"""

def build_slides():
  return [
    page(1, f"""<div class="kicker">Search has changed</div>
<h1 style="font-size:104px">SEO is not<br>enough<br>anymore.</h1>
<div class="full" style="font-size:36px;line-height:1.35;margin-top:10px">People now find brands on Google, in AI answers and in chat assistants. Here are the <b style="color:#FDE047">5 optimizations</b> your website needs in 2026.</div>
<div style="margin:44px 60px 0;display:flex;flex-direction:column;gap:16px">
""" + "".join(f'<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.16);border:2px solid rgba(255,255,255,.35);border-radius:22px;padding:18px 24px"><div style="width:120px;font-size:40px;font-weight:900;color:#FDE047">{a}</div><div style="font-size:28px;font-weight:700;color:#fff">{b}</div></div>' for a, b in [("SEO","Rank on page 1"),("AEO","Be in the answer box"),("GEO","Be the AI recommendation"),("AIO","Be understood by AI"),("SXO","Turn visits into clients")]) + "</div>" + nxt("SEO, the foundation")),
    section(2, "01 · The foundation", "SEO", "Search Engine Optimization", SEO_CARD,
            "Rankings", "Rank on page 1 of Google",
            ["<b>One page per search intent</b>, with the keyword in the title, H1 and URL",
             "<b>Fast, mobile-friendly pages</b> that Google can crawl",
             "<b>Links from trusted sites</b> in your niche"], "AEO, the answer box"),
    section(3, "02 · Answers first", "AEO", "Answer Engine Optimization", AEO_CARD,
            "Answers", "Be the answer in the box",
            ["<b>Answer the question in the first 2–3 sentences</b> of the page",
             "<b>Use questions as headings</b> (H2) and short, direct answers",
             "<b>Add FAQ, tables and lists</b> that are easy to quote"], "GEO, AI recommendations"),
    section(4, "03 · AI assistants", "GEO", "Generative Engine Optimization", GEO_CARD,
            "Recommendation", "Be the brand AI recommends",
            ["<b>Be mentioned on other sites</b>: reviews, lists, press, forums",
             "<b>Give exact facts</b>: prices, numbers, dates, locations",
             "<b>Same name, offer and details</b> everywhere online"], "AIO, AI visibility"),
    section(5, "04 · Machine-readable", "AIO", "AI Optimization", AIO_CARD,
            "AI Visibility", "Be understood across AI systems",
            ["<b>Schema markup</b>: Organization, Product, FAQ, Review",
             "<b>Clear entity</b>: who you are, what you do, where",
             "<b>Link related pages</b> so AI sees the full picture"], "SXO, the experience"),
    section(6, "05 · From visit to client", "SXO", "Search Experience Optimization", SXO_CARD,
            "Experience", "Make the next step effortless",
            ["<b>Match the intent</b>: give people what they searched for",
             "<b>Load in under 2.5 seconds</b> on mobile",
             "<b>One clear call to action</b>: buy, book or contact"], "The cheat sheet"),
    page(7, f"""<div class="kicker">Save this ✦</div><h1 style="font-size:96px">Cheat sheet</h1>
<div class="full" style="color:#3B3F55">Where each one shows up and how to measure it.</div>
<div class="card" style="height:auto;padding:0;margin-top:30px"><table>
<tr><th></th><th>Goal</th><th>Where</th><th>Measure</th></tr>
<tr><td>SEO</td><td>Rank on page 1</td><td>Google results</td><td>Positions, clicks</td></tr>
<tr><td>AEO</td><td>Be the answer</td><td>AI Overviews, snippets</td><td>Answer boxes won</td></tr>
<tr><td>GEO</td><td>Be recommended</td><td>ChatGPT, Gemini, Perplexity</td><td>Brand mentions</td></tr>
<tr><td>AIO</td><td>Be understood</td><td>All AI systems</td><td>Schema, entity data</td></tr>
<tr><td style="border:0">SXO</td><td style="border:0">Convert visits</td><td style="border:0">Your website</td><td style="border:0">Bookings, sales, leads</td></tr>
</table></div>
<div class="brace"></div><div class="goal">One strategy, 5 layers<small>Each layer builds on the one before</small></div>
{nxt("Your 5-minute checklist")}"""),
    page(8, f"""<div class="kicker">Your next step</div><h1 style="font-size:96px">Quick check</h1>
<div class="full" style="color:#3B3F55">Can you tick all 5 for your website?</div>
<div class="card" style="height:auto;margin-top:30px">""" + "".join(
        f'<div style="display:flex;gap:20px;align-items:center;padding:14px 0;border-bottom:2px solid #EEF1F8;font-size:27px"><div style="width:46px;height:46px;border:3px solid {BLUE};border-radius:12px;flex:none"></div><div><b style="color:{BLUE}">{a}</b> · {b}</div></div>'
        for a, b in [("SEO", "My main pages rank in the top 10"), ("AEO", "Each page answers the question in 2 sentences"),
                     ("GEO", "Other sites mention my brand"), ("AIO", "My site has schema markup"),
                     ("SXO", "A visitor can buy or book in 2 clicks")]) + f"""</div>
<div class="brace"></div><div class="goal">Missed one?<small>Follow @wegravel_morocco for more</small></div>
{nxt("", last=True)}"""),
]


if __name__ == "__main__":
 SLIDES = build_slides()
 for i, html_text in enumerate(SLIDES, 1):
     html = TMP / f"slide-{i}.html"
     html.write_text(html_text, encoding="utf-8")
     png = OUT / f"slide-{i}.png"
     subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                     "--force-device-scale-factor=1", "--window-size=1080,1600",
                     f"--screenshot={png}", html.as_uri()],
                    check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
     Image.open(png).convert("RGB").crop((0, 0, 1080, 1350)).save(png)
     print(png)
