import base64
from pathlib import Path
H = Path(__file__).parent
b64 = lambda p, mime: f"data:{mime};base64," + base64.b64encode((H / p).read_bytes()).decode()
BG = b64("bg-1600.jpg", "image/jpeg")
BH = b64("bh_logo.png", "image/png")
BHG = b64("bh_gold.png", "image/png")
KLC = b64("kl-cream.svg", "image/svg+xml")
KLD = "data:image/svg+xml;base64," + base64.b64encode(Path.home().joinpath("Documents/Developer/kawikalopez-site/assets/img/site/logo.svg").read_bytes()).decode()
n = [0]
def A(px):
    n[0] += 1; i = n[0]
    return (f'<div class="sA bgart" style="--in:{px}px"><div class="ring"></div>'
            f'<svg class="arc" viewBox="0 0 400 400" aria-hidden="true"><defs>'
            f'<path id="t{i}" d="M 35 200 A 165 165 0 0 1 365 200"/><path id="b{i}" d="M 24 200 A 176 176 0 0 0 376 200"/></defs>'
            f'<text class="gold"><textPath href="#t{i}" startOffset="50%" text-anchor="middle">BAKER\u2019S HEART × KAWIKA LOPEZ</textPath></text>'
            f'<text><textPath href="#b{i}" startOffset="50%" text-anchor="middle">HOLIDAY 2026</textPath></text></svg>'
            f'<div class="stack"><img class="kl" src="{KLC}" alt="Kawika Lopez Photography"></div></div>')
def B(px):
    return (f'<div class="sB" style="--in:{px}px"><div class="side bgart"><img src="{KLC}" alt="Kawika Lopez Photography"></div>'
            f'<div class="txt"><span class="eyebrow">Baker\u2019s Heart × Kawika Lopez</span><h4>A photograph to keep</h4>'
            f'<p>A matted print of Oʻahu, made here and ready for an 11 x 14 frame.</p><span class="eyebrow soft">Holiday 2026</span></div></div>')
def C(px):
    return (f'<div class="sC bgart" style="--in:{px}px"><div class="panel"><img class="kl" src="{KLD}" alt="Kawika Lopez Photography">'
            f'<span class="rule"></span><span class="cap">BAKER\u2019S HEART × KAWIKA LOPEZ</span><span class="cap soft">HOLIDAY 2026</span></div></div>')
t = (H / "sticker-options.tpl.html").read_text()
for k, v in {"__BG__": BG, "__A26__": A(26), "__A62__": A(62), "__B26__": B(26), "__B62__": B(62), "__C26__": C(26), "__C62__": C(62)}.items():
    assert k in t, k
    t = t.replace(k, v)
out = Path("/private/tmp/claude-501/-Users-veex-Documents-Obsidian/f0a654fc-cb9b-4d51-b9b1-64e4d4eaa8c8/scratchpad/bh-design/.superpowers/brainstorm/24095-1792195612/content/sticker-options.html")
out.write_text(t); print(len(t)//1024, "KB")
