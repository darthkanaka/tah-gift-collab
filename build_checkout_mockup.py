"""Build the checkout design mockup from the live proposal page.

Reads ~/Documents/Developer/tah-gift-collab/index.html (the approved proposal, images embedded)
and writes the vault mockup with the Touch A Heart toolbar, the checkout window and the
landing page changes approved on 2026-10-15. Design only: nothing is charged.
"""
from pathlib import Path

SRC = Path.home() / "Documents/Developer/tah-gift-collab/index.html"
OUT = Path.home() / "Documents/Obsidian/projects/bakers-heart-checkout-mockup.html"

s = SRC.read_text(encoding="utf-8")


def swap(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, f"expected {count} of {old[:70]!r}, found {n}"
    s = s.replace(old, new)


TAH = "https://touchahearthawaii.org"

# ---------- head ----------
swap("<title>Touch A Heart x Kawika Lopez: Gifts Made on Oʻahu</title>",
     "<title>Touch A Heart x Kawika Lopez: Holiday Gift Boxes</title>")
swap("<!-- Mockup for Touch A Heart.",
     "<!-- Checkout design mockup (2026-10-15). Built from the approved proposal page by build_checkout_mockup.py.\n     Design only: the window works, but nothing is charged.\n     Mockup for Touch A Heart.")
swap("<style>\n  /* Fonts:",
     '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
     '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap">\n'
     "<style>\n  /* Fonts:")

CSS = r"""
  /* ---------- Touch A Heart toolbar (copies touchahearthawaii.org's header) ---------- */
  .tah-bar { background: #C29D3B; color: #fff; text-align: center; font: 500 0.875rem/1.35 "Open Sans", var(--sans); padding: 9px var(--gutter); margin: 0; }
  .tah-head { position: sticky; top: 0; z-index: 30; background: #fff; border-bottom: 1px solid #eee; font-family: "Open Sans", var(--sans); color: #2b2b2b; }
  .tah-in { max-width: 1440px; margin-inline: auto; display: flex; align-items: center; gap: 16px; padding: 8px var(--gutter); }
  .tah-logo { display: block; flex: none; }
  .tah-logo img { height: 48px; width: auto; }
  .tah-nav { display: none; list-style: none; margin: 0; padding: 0; flex: 1; justify-content: center; gap: 26px; font-size: 15px; }
  .tah-nav > li { position: relative; }
  .tah-nav a { color: inherit; text-decoration: none; }
  .tah-nav > li > a { display: inline-flex; align-items: center; gap: 6px; padding: 20px 0; }
  .tah-nav > li > a:hover, .tah-nav > li:focus-within > a { color: #c51c74; }
  .tah-nav .caret { font-size: 9px; }
  .tah-sub { display: none; position: absolute; left: -16px; top: 100%; min-width: 250px; background: #fff; border: 1px solid #e5e5e5;
    box-shadow: 0 8px 20px rgba(0, 0, 0, .12); list-style: none; margin: 0; padding: 8px 0; }
  .tah-nav > li:hover .tah-sub, .tah-nav > li:focus-within .tah-sub { display: block; }
  .tah-sub a { display: block; padding: 8px 16px; font-size: 14px; }
  .tah-sub a:hover { color: #c51c74; }
  .tah-menu { flex: none; }
  .tah-menu summary { list-style: none; cursor: pointer; font-size: 26px; line-height: 1; padding: 6px 4px; }
  .tah-menu summary::-webkit-details-marker { display: none; }
  .tah-menu-list { position: absolute; left: 0; right: 0; top: 100%; background: #fff; border-bottom: 1px solid #e5e5e5; box-shadow: 0 10px 20px rgba(0, 0, 0, .1);
    padding: 8px var(--gutter) 16px; max-height: 70vh; overflow: auto; }
  .tah-menu-list p { margin: 14px 0 2px; font-weight: 600; font-size: 15px; }
  .tah-menu-list a { display: block; color: inherit; text-decoration: none; }
  .tah-menu-list .grp a { padding: 6px 0 6px 14px; font-size: 14.5px; color: #555; border-left: 1px solid #e5e5e5; }
  .tah-menu-list > a { font-weight: 600; font-size: 15px; padding: 14px 0 2px; }
  .mine { margin-left: auto; flex: none; display: inline-flex; align-items: center; gap: 8px; background: var(--green); color: #fff; border: 0; cursor: pointer;
    font: 500 0.875rem/1 var(--sans); padding: 12px 16px; white-space: nowrap; }
  .mine:hover { background: var(--green-3); }
  .mine .n { background: var(--gold); border-radius: 10px; padding: 3px 7px; font-size: 0.75rem; }
  @media (min-width: 1060px) {
    .tah-nav { display: flex; }
    .tah-menu { display: none; }
    .tah-in { padding-inline: 28px; gap: 24px; }
    .tah-logo img { height: 60px; }
    .mine { margin-left: 0; }
  }

  /* ---------- landing page tweaks ---------- */
  .mat-fig[role="button"] { cursor: pointer; }
  .mat-fig[role="button"]:hover figcaption, .mat-fig[role="button"]:focus-visible figcaption { text-decoration: underline; text-underline-offset: 4px; }
  .mat-fig[role="button"]:focus-visible { outline: 2px solid #f1ecdd; outline-offset: 8px; }
  .btn-gold { background: var(--gold); border-color: var(--gold); color: #fff; margin-top: 24px; }
  .btn-gold:hover { background: var(--gold-2); border-color: var(--gold-2); }

  /* ---------- the checkout window ---------- */
  .co[hidden] { display: none; }
  .co { position: fixed; inset: 0; z-index: 50; }
  .co-dim { position: absolute; inset: 0; background: rgba(27, 26, 24, .5); }
  .co-panel { position: absolute; inset: 0; background: var(--card); display: flex; flex-direction: column; }
  .co-top { display: flex; align-items: center; gap: 16px; padding: 14px var(--gutter); border-bottom: 1px solid var(--rule); flex: none; }
  .co-top h2 { font-size: 1.75rem; margin: 0; }
  .co-x { margin-left: auto; background: none; border: 0; font-size: 30px; line-height: 1; color: var(--ink-2); cursor: pointer; padding: 4px 8px; }
  .co-scroll { flex: 1; overflow: auto; overscroll-behavior: contain; }
  .co-body { display: grid; gap: 24px; padding: 18px var(--gutter) 96px; }
  .co-main { display: grid; gap: 14px; align-content: start; }
  .co-tabs { display: grid; grid-template-columns: 1fr 1fr; border: 1px solid var(--green); }
  .co-tabs button { font: inherit; background: #fff; color: var(--ink); border: 0; padding: 10px 8px; cursor: pointer; text-align: center; line-height: 1.3; }
  .co-tabs button[aria-selected="true"] { background: var(--green); color: #fff; }
  .co-tabs .t { font-weight: 600; font-size: 0.9375rem; }
  .co-tabs small { display: block; font-size: 0.75rem; opacity: .85; }
  .badge { display: inline-block; min-width: 20px; padding: 1px 6px; border-radius: 10px; background: var(--gold); color: #fff; font-size: 0.75rem; margin-left: 4px; }
  .badge[data-zero] { display: none; }
  .co-what { margin: 0; color: var(--ink-2); font-size: 0.875rem; line-height: 1.5; }
  .co-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
  .tile { background: #fff; border: 1px solid var(--rule); padding: 14px 8px 10px; display: grid; justify-items: center; gap: 4px; text-align: center; transition: box-shadow .2s, border-color .2s; }
  .tile.on { border-color: var(--green); box-shadow: 0 0 0 1px var(--green); }
  .tile.pulse { animation: pulse 1.4s ease-out 1; }
  @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(168, 132, 63, .9); } 100% { box-shadow: 0 0 0 14px rgba(168, 132, 63, 0); } }
  .tile .art { --in: 6.4px; height: calc(var(--in) * 14); display: flex; align-items: center; margin-bottom: 8px; }
  .tile .mat { box-shadow: 1px 1px 2px rgba(0, 0, 0, .25), 3px 3px 8px rgba(0, 0, 0, .15); }
  .tile .nm { font-weight: 600; font-size: 0.875rem; line-height: 1.25; }
  .tile .sz { font-size: 0.75rem; color: var(--ink-2); }
  .step { display: inline-flex; align-items: center; border: 1px solid var(--rule); margin-top: 6px; }
  .step button { width: 36px; height: 34px; border: 0; background: none; font-size: 20px; line-height: 1; color: var(--green); cursor: pointer; }
  .step button:disabled { color: #c9c4ba; cursor: default; }
  .step output { min-width: 28px; text-align: center; font-weight: 600; font-variant-numeric: tabular-nums; }
  .co-hint { margin: 0; font-size: 0.8125rem; color: var(--ink-2); }
  .co-side { background: var(--paper); border: 1px solid var(--rule); padding: 16px; display: grid; gap: 14px; align-content: start; scroll-margin-top: 12px; }
  .co-side h3 { font-size: 1.375rem; }
  .co-grp { border-top: 1px solid var(--rule); padding-top: 8px; }
  .co-gh { display: flex; font-weight: 600; font-size: 0.9375rem; margin-bottom: 4px; }
  .co-gh span:last-child { margin-left: auto; }
  .co-ln { display: flex; align-items: center; gap: 10px; padding: 4px 6px; margin-inline: -6px; font-size: 0.875rem; }
  .co-ln img { width: 34px; height: 26px; object-fit: cover; border: 3px solid #e3dfd6; flex: none; }
  .co-ln .q { margin-left: auto; color: var(--ink-2); font-variant-numeric: tabular-nums; }
  .co-ln.flash { animation: flash 1.2s ease-out 1; }
  @keyframes flash { 0% { background: rgba(168, 132, 63, .35); } 100% { background: transparent; } }
  .co-empty { margin: 0; color: var(--ink-2); font-size: 0.875rem; }
  .co-tot { border-top: 2px solid var(--ink); padding-top: 10px; display: flex; font-weight: 600; }
  .co-tot span:last-child { margin-left: auto; }
  .co-clear { background: none; border: 0; padding: 0; font: inherit; font-size: 0.8125rem; color: var(--ink-2); text-decoration: underline; cursor: pointer; justify-self: start; }
  .co-lbl { font-weight: 600; font-size: 0.9375rem; margin: 0 0 -6px; }
  .co-spots { border: 0; margin: 0; padding: 0; display: grid; gap: 8px; }
  .co-spots legend { font-weight: 600; font-size: 0.9375rem; padding: 0; margin-bottom: 8px; }
  .spot { display: grid; grid-template-columns: auto 1fr; gap: 0 10px; background: #fff; border: 1px solid var(--rule); padding: 10px 12px; cursor: pointer; font-size: 0.875rem; line-height: 1.4; }
  .spot input { margin: 3px 0 0; accent-color: var(--green); width: 16px; height: 16px; grid-row: span 3; }
  .spot b { font-size: 0.9375rem; }
  .spot small { color: var(--ink-2); font-size: 0.8125rem; }
  .spot:has(input:checked) { border-color: var(--green); box-shadow: 0 0 0 1px var(--green); }
  .co-field { border: 1px solid var(--rule); background: #fff; padding: 10px 12px; font-size: 0.9375rem; color: var(--ink-2); }
  .co-field.set { border-color: var(--green); color: var(--ink); font-weight: 600; }
  .cal { background: #fff; border: 1px solid var(--rule); padding: 10px; }
  .cal[hidden] { display: none; }
  .cal-h { display: flex; align-items: center; margin-bottom: 8px; }
  .cal-h b { flex: 1; text-align: center; font-family: var(--serif); font-weight: 400; font-size: 1.25rem; }
  .cal-h button { background: none; border: 0; font-size: 22px; line-height: 1; color: var(--green); cursor: pointer; padding: 2px 10px; }
  .cal-h button:disabled { color: #d6d1c7; cursor: default; }
  .cal-g { display: grid; grid-template-columns: repeat(7, 1fr); gap: 3px; text-align: center; }
  .cal-g .wd { font-size: 0.6875rem; font-weight: 600; color: var(--ink-2); padding: 2px 0; }
  .cal-g button, .cal-g span.off { font: inherit; font-size: 0.875rem; padding: 7px 0; border: 1px solid transparent; background: none; }
  .cal-g span.off { color: #c3beb4; text-decoration: line-through; }
  .cal-g button { border-color: var(--rule); color: var(--ink); cursor: pointer; }
  .cal-g button:hover { border-color: var(--green); }
  .cal-g button[aria-pressed="true"] { background: var(--green); border-color: var(--green); color: #fff; font-weight: 600; }
  .co-note { margin: 0; font-size: 0.8125rem; color: var(--ink-2); line-height: 1.5; }
  .co-msg { margin: 0; font-size: 0.875rem; background: #f3ead4; border-left: 3px solid var(--gold); padding: 8px 10px; }
  .co-msg[hidden] { display: none; }
  .co-pbar { position: absolute; left: 0; right: 0; bottom: 0; display: flex; align-items: center; gap: 12px; background: var(--green-3); color: #fff;
    padding: 12px var(--gutter); font-weight: 600; font-size: 0.9375rem; }
  .co-pbar button { margin-left: auto; background: var(--gold); color: #fff; border: 0; font: 600 0.875rem/1 var(--sans); padding: 11px 14px; cursor: pointer; }
  @media (min-width: 720px) { .co-grid { grid-template-columns: repeat(3, 1fr); } }
  @media (min-width: 960px) {
    .co-panel { left: auto; width: min(1080px, 94vw); box-shadow: -10px 0 30px rgba(0, 0, 0, .25); }
    .co-top { padding-inline: 28px; }
    .co-body { grid-template-columns: 1.35fr 1fr; padding: 22px 28px 28px; align-items: start; }
    .co-side { position: sticky; top: 0; }
    .co-pbar { display: none; }
  }
  @media (prefers-reduced-motion: reduce) { .tile.pulse, .co-ln.flash { animation: none; } }
</style>"""
swap("  @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }\n</style>",
     "  @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }\n" + CSS)

# ---------- toolbar ----------
MENU = [
    ("About", "/pages/about", [("About", "/pages/about"), ("Pickup Information", "/pages/pickup-delivery-information")]),
    ("Programs", "/pages/programs", [("Internship &amp; Apprenticeship", "/pages/programs"), ("Growth Mindset", "/pages/growth-mindset")]),
    ("Social Enterprises", "/pages/social-enterprises", [
        ("'Ohana Meals", "/pages/social/#shopify-section-template--15893091713104__51f6c67c-19a1-4b9e-b352-dfbb10c2f5e6"),
        ("Baker's Heart", "/pages/social/#shopify-section-template--15893091713104__2b71388a-4a06-4e6f-ba37-9fb6c47e6716"),
        ("Catering", "/pages/social/#shopify-section-template--15893091713104__e6346e4a-a6fa-47eb-8e80-c043bfd8cbbc")]),
    ("Our Community", "/pages/staying-connected", [("Get Involved", "/pages/get-involved"), ("Staying Connected", "/pages/staying-connected")]),
    ("Donate", "https://give.touchahearthawaii.org/campaign/748420/donate", []),
    ("Shop", "/collections/ohana-meals", [
        ("'Ohana Meals", "/collections/ohana-meals"),
        ("🦃 'Ohana Meals Thanksgiving Pre-Order", "/collections/thanksgiving-2026"),
        ("Baker's Heart", "/collections/bakersheart"),
        ("✴︎ Baker's Heart Holiday Pre-Order ✴︎", "/collections/bh-holiday")]),
    ("Contact Us", "/pages/contact", []),
]


def url(u):
    return u if u.startswith("http") else TAH + u


desk, phone = [], []
for name, top, subs in MENU:
    if subs:
        items = "".join(f'<li><a href="{url(h)}">{t}</a></li>' for t, h in subs)
        desk.append(f'<li><a href="{url(top)}">{name}<span class="caret" aria-hidden="true">▾</span></a><ul class="tah-sub">{items}</ul></li>')
        phone.append(f'<div class="grp"><p>{name}</p>' + "".join(f'<a href="{url(h)}">{t}</a>' for t, h in subs) + '</div>')
    else:
        desk.append(f'<li><a href="{url(top)}">{name}</a></li>')
        phone.append(f'<a href="{url(top)}">{name}</a>')

TOOLBAR = f"""<p class="tah-bar">✴︎ Holiday gift boxes from Baker's Heart and Kawika Lopez. Pickups start November 16. ✴︎</p>
<div class="tah-head">
  <div class="tah-in">
    <details class="tah-menu"><summary aria-label="Menu">☰</summary><nav class="tah-menu-list" aria-label="Touch A Heart">{''.join(phone)}</nav></details>
    <a class="tah-logo" href="{TAH}/"><img src="{TAH}/cdn/shop/files/TAH_logo.jpg?v=1677166552" width="1838" height="914" alt="Touch A Heart home"></a>
    <ul class="tah-nav" aria-label="Touch A Heart">{''.join(desk)}</ul>
    <button class="mine" type="button" data-open="">Your order <span class="n" id="mine-n">8</span></button>
  </div>
</div>
"""
swap('<p class="mock-banner">A proposal for Touch A Heart from Kawika Lopez. It isn\'t live yet, and the order buttons don\'t go anywhere.</p>\n',
     TOOLBAR)

# ---------- landing page changes ----------
# Opening line, StoryBrand rewrite (Kawika, 2026-10-15). The old line claimed people here know the place by heart.
swap("<p class=\"lede\">A gift for your clients and your team. Handcrafted Baker's Heart cookies to share now, and a matted print of a place people here know by heart, to keep on the wall long after the box is empty.</p>",
     "<p class=\"lede\">Your clients and team get cookies to share now and a photograph that lives on the wall for years. Every box supports Touch A Heart's job training and a local artist.</p>")
swap("The holiday boxes are available starting Monday, November 16.</p>",
     "You can order now. Pickups run November 16 to December 22, at Kalihi Union Church on weekdays or Pearl City Community Church on Wednesdays.</p>")
swap('<span class="btn btn-wide" role="button" aria-disabled="true">Order the Team box</span>',
     '<button class="btn btn-order" type="button" data-open="team">Order the Team box</button>')
swap('<span class="btn btn-wide" role="button" aria-disabled="true">Order the Client box</span>',
     '<button class="btn btn-order" type="button" data-open="client">Order the Client box</button>')
WALL = [("mokulele", "Mokulele"), ("mokulua", "Mokulua"), ("shoreline", "Shoreline Cascade"),
        ("leahi", "Lēʻahi Kahiko"), ("kahana", "Kahana"), ("malie", "Mālie")]
for pid, name in WALL:
    swap(f'<figcaption>{name}</figcaption>\n            </figure>',
         f'<figcaption>{name}</figcaption>\n            </figure><!--{pid}-->')
s = s.replace('<figure class="mat-fig">', '<figure class="mat-fig" role="button" tabindex="0" data-pick="PID">')
for pid, name in WALL:
    i = s.index(f"<!--{pid}-->")
    j = s.rindex('data-pick="PID"', 0, i)
    s = s[:j] + f'data-pick="{pid}" aria-label="Order a box with {name}"' + s[j + len('data-pick="PID"'):]
    s = s.replace(f"<!--{pid}-->", "", 1)
assert 'data-pick="PID"' not in s
swap("<p>Tell us how many and who they're for, and we'll help you put it together. Either of us can help.</p>",
     "<p>Tell us how many and who they're for, and we'll help you put it together. Either of us can help.</p>\n"
     '      <button class="btn btn-gold" type="button" data-open="team">Order gift boxes</button>')

# ---------- the window ----------
WINDOW = """
<div class="co" id="co" hidden>
  <div class="co-dim" data-close></div>
  <section class="co-panel" role="dialog" aria-modal="true" aria-labelledby="co-title">
    <header class="co-top"><h2 id="co-title">Build your order</h2><button class="co-x" type="button" data-close aria-label="Close">×</button></header>
    <div class="co-scroll" id="co-scroll">
      <div class="co-body">
        <div class="co-main">
          <div class="co-tabs" role="tablist" aria-label="Box">
            <button type="button" role="tab" data-box="team" aria-selected="true"><span class="t">Team box, $80<span class="badge" data-badge="team"></span></span><small>A print and a Double Box</small></button>
            <button type="button" role="tab" data-box="client" aria-selected="false"><span class="t">Client box, $120<span class="badge" data-badge="client"></span></span><small>A print and a gift box</small></button>
          </div>
          <p class="co-what" id="co-what"></p>
          <div class="co-grid" id="co-grid"></div>
          <p class="co-hint">Pick as many of each photograph as you need. You can mix photographs, and both boxes, in one order.</p>
        </div>
        <aside class="co-side" id="co-side" aria-label="Your order">
          <h3>Your order</h3>
          <div id="co-lines"></div>
          <div class="co-tot"><span id="co-count"></span><span id="co-sum"></span></div>
          <button class="co-clear" type="button" id="co-clear">Clear the order</button>
          <fieldset class="co-spots">
            <legend>Pickup spot</legend>
            <label class="spot"><input type="radio" name="spot" value="kalihi"><b>Kalihi Union Church</b><small>2214 N. King St., Honolulu</small><small>Monday to Friday, 8 am to 1 pm</small></label>
            <label class="spot"><input type="radio" name="spot" value="pearl"><b>Pearl City Community Church</b><small>933 Lehua Ave., Pearl City</small><small>Wednesdays, 1:30 to 3 pm</small></label>
          </fieldset>
          <p class="co-lbl">Pickup date</p>
          <div class="co-field" id="co-field">Pick a spot first</div>
          <div class="cal" id="co-cal" hidden></div>
          <p class="co-note" id="co-note" hidden></p>
          <button class="btn btn-wide" type="button" id="co-pay"></button>
          <p class="co-msg" id="co-msg" role="status" hidden></p>
        </aside>
      </div>
    </div>
    <div class="co-pbar"><span id="co-pb"></span><button type="button" id="co-pb-go">Pickup and payment</button></div>
  </section>
</div>
"""

JS = r"""
<script>
(() => {
  const PRINTS = [
    { id: 'mokulele', name: 'Mokulele', h: false, img: 'mokulele' },
    { id: 'mokulua', name: 'Mokulua', h: true, img: 'mokulua-islands' },
    { id: 'shoreline', name: 'Shoreline Cascade', h: false, img: 'shorelinecascade' },
    { id: 'leahi', name: 'Lēʻahi Kahiko', h: true, img: 'leahikahiko' },
    { id: 'kahana', name: 'Kahana', h: false, img: 'kahana' },
    { id: 'malie', name: 'Mālie', h: true, img: 'malie' },
  ];
  const BOXES = {
    team: { label: 'Team', price: 80, what: "Every Team box has a matted print of the photograph you pick and a Baker's Heart Double Box, twelve lace cookies in three flavors." },
    client: { label: 'Client', price: 120, what: "Every Client box has a matted print of the photograph you pick and a Baker's Heart gift box of lace cookies and biscotti bites." },
  };
  const src = p => `https://kawikalopez.com/assets/img/prints/${p.img}-480.jpg`;
  // Sample order so the design shows filled in. "Clear the order" shows the empty state.
  const order = { team: { mokulele: 4, shoreline: 2 }, client: { malie: 2 } };
  let tab = 'team', spot = null, picked = null, month = null;

  // ---- pickup rules (2026-10-15) ----
  const FIRST = new Date(2026, 10, 16), LAST = new Date(2026, 11, 22);
  const CLOSED = new Set(['2026-11-26', '2026-11-27', '2026-12-24', '2026-12-25']);
  const key = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const isBiz = d => d.getDay() > 0 && d.getDay() < 6 && !CLOSED.has(key(d));
  const today = (() => { const t = new Date(); return new Date(t.getFullYear(), t.getMonth(), t.getDate()); })();
  const addBiz = (d, n) => { const x = new Date(d); while (n > 0) { x.setDate(x.getDate() + 1); if (isBiz(x)) n--; } return x; };
  const floor = (() => { const f = addBiz(today, 5); return f < FIRST ? FIRST : f; })();
  const open = (d, where) => isBiz(d) && d >= floor && d <= LAST && (where !== 'pearl' || d.getDay() === 3);
  const firstOpen = where => { for (let d = new Date(floor); d <= LAST; d.setDate(d.getDate() + 1)) if (open(d, where)) return new Date(d); return null; };
  const long = d => d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' });
  const short = d => d.toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric' });

  const $ = id => document.getElementById(id);
  const co = $('co'), grid = $('co-grid');
  let lastFocus = null;

  const count = box => Object.values(order[box]).reduce((a, b) => a + b, 0);
  const total = () => count('team') * BOXES.team.price + count('client') * BOXES.client.price;
  const boxes = () => count('team') + count('client');
  const plural = (n, w) => `${n} ${w}${n === 1 ? '' : 'es'}`;

  function tiles() {
    grid.innerHTML = PRINTS.map(p => `
      <div class="tile" data-id="${p.id}">
        <div class="art"><div class="mat ${p.h ? 'h' : 'v'}"><div class="photo"><img src="${src(p)}" alt="" loading="lazy"></div></div></div>
        <div class="nm">${p.name}</div><div class="sz">${p.h ? '8 x 12' : '8 x 10'} print</div>
        <div class="step"><button type="button" data-step="-1" aria-label="One less ${p.name}">−</button><output aria-live="polite">0</output><button type="button" data-step="1" aria-label="One more ${p.name}">+</button></div>
      </div>`).join('');
  }

  function render(flashId) {
    $('co-what').textContent = BOXES[tab].what;
    document.querySelectorAll('.co-tabs [role=tab]').forEach(b => b.setAttribute('aria-selected', String(b.dataset.box === tab)));
    document.querySelectorAll('[data-badge]').forEach(b => { const n = count(b.dataset.badge); b.textContent = n; b.toggleAttribute('data-zero', n === 0); });
    grid.querySelectorAll('.tile').forEach(t => {
      const n = order[tab][t.dataset.id] || 0;
      t.querySelector('output').textContent = n;
      t.querySelector('[data-step="-1"]').disabled = n === 0;
      t.classList.toggle('on', n > 0);
    });
    let html = '';
    for (const box of ['team', 'client']) {
      const n = count(box); if (!n) continue;
      html += `<div class="co-grp"><div class="co-gh"><span>${BOXES[box].label} ${n === 1 ? 'box' : 'boxes'}, ${n}</span><span>$${n * BOXES[box].price}</span></div>`;
      for (const p of PRINTS) {
        const q = order[box][p.id]; if (!q) continue;
        html += `<div class="co-ln" data-line="${box}-${p.id}"><img src="${src(p)}" alt="">${p.name}<span class="q">${q}</span></div>`;
      }
      html += '</div>';
    }
    $('co-lines').innerHTML = html || '<p class="co-empty">Nothing here yet. Add a photograph to start your order.</p>';
    if (flashId) { const l = document.querySelector(`[data-line="${flashId}"]`); if (l) { l.classList.remove('flash'); void l.offsetWidth; l.classList.add('flash'); } }
    const n = boxes(), sum = total();
    $('co-count').textContent = plural(n, 'box'); $('co-sum').textContent = `$${sum}`;
    $('co-clear').hidden = n === 0;
    $('co-pay').textContent = n ? `Continue to payment, $${sum}` : 'Continue to payment';
    $('co-pb').textContent = `${plural(n, 'box')}, $${sum}`;
    const mine = document.querySelector('.mine');
    mine.innerHTML = n ? `Your order <span class="n" id="mine-n">${n}</span>` : 'Order a gift box';
    renderPickup();
  }

  function renderPickup() {
    const cal = $('co-cal'), note = $('co-note'), field = $('co-field');
    if (!spot) { cal.hidden = true; note.hidden = true; field.textContent = 'Pick a spot first'; field.classList.remove('set'); return; }
    const first = firstOpen(spot);
    note.hidden = false;
    if (!first) { cal.hidden = true; field.textContent = 'No pickup days left'; field.classList.remove('set');
      note.textContent = "There are no pickup days left at this spot this season."; return; }
    if (picked && !open(picked, spot)) picked = null;
    field.textContent = picked ? long(picked) : 'Pick a date';
    field.classList.toggle('set', !!picked);
    note.textContent = spot === 'pearl'
      ? `Pearl City pickups are on Wednesdays, 1:30 to 3 pm, through December 16. We need five business days to get your order ready, so the earliest you can pick is ${short(first)}.`
      : `Kalihi pickups are weekdays, 8 am to 1 pm, through December 22, and we're closed Thanksgiving weekend. We need five business days to get your order ready, so the earliest you can pick is ${short(first)}.`;
    if (!month) month = new Date((picked || first).getFullYear(), (picked || first).getMonth(), 1);
    const y = month.getFullYear(), m = month.getMonth();
    const minM = new Date(first.getFullYear(), first.getMonth(), 1), maxM = new Date(2026, 11, 1);
    let h = `<div class="cal-h"><button type="button" data-mon="-1" aria-label="Previous month" ${month <= minM ? 'disabled' : ''}>‹</button><b>${month.toLocaleDateString('en-US', { month: 'long', year: 'numeric' })}</b><button type="button" data-mon="1" aria-label="Next month" ${month >= maxM ? 'disabled' : ''}>›</button></div><div class="cal-g">`;
    h += ['S', 'M', 'T', 'W', 'T', 'F', 'S'].map(w => `<span class="wd">${w}</span>`).join('');
    h += '<span></span>'.repeat(new Date(y, m, 1).getDay());
    for (let d = 1; d <= new Date(y, m + 1, 0).getDate(); d++) {
      const day = new Date(y, m, d);
      h += open(day, spot)
        ? `<button type="button" data-day="${key(day)}" aria-pressed="${picked && key(picked) === key(day)}" aria-label="${long(day)}">${d}</button>`
        : `<span class="off" aria-hidden="true">${d}</span>`;
    }
    cal.innerHTML = h + '</div>';
    cal.hidden = false;
  }

  function openCo(box, pick) {
    if (box) tab = box;
    lastFocus = document.activeElement;
    co.hidden = false; document.body.style.overflow = 'hidden';
    render();
    co.querySelector('.co-x').focus();
    if (pick) {
      const t = grid.querySelector(`[data-id="${pick}"]`);
      t.scrollIntoView({ block: 'center' }); t.classList.remove('pulse'); void t.offsetWidth; t.classList.add('pulse');
    }
  }
  function closeCo() { co.hidden = true; document.body.style.overflow = ''; if (lastFocus) lastFocus.focus(); }

  document.addEventListener('click', e => {
    const o = e.target.closest('[data-open]'); if (o) { openCo(o.dataset.open || null); return; }
    const pk = e.target.closest('[data-pick]'); if (pk) { openCo(null, pk.dataset.pick); return; }
    if (e.target.closest('[data-close]')) { closeCo(); return; }
    const tb = e.target.closest('.co-tabs [role=tab]'); if (tb) { tab = tb.dataset.box; render(); return; }
    const st = e.target.closest('[data-step]');
    if (st) {
      const id = st.closest('.tile').dataset.id, d = +st.dataset.step;
      const n = Math.max(0, (order[tab][id] || 0) + d);
      if (n) order[tab][id] = n; else delete order[tab][id];
      $('co-msg').hidden = true;
      render(d > 0 ? `${tab}-${id}` : null); return;
    }
    if (e.target.id === 'co-clear') { order.team = {}; order.client = {}; $('co-msg').hidden = true; render(); return; }
    const mo = e.target.closest('[data-mon]'); if (mo) { month = new Date(month.getFullYear(), month.getMonth() + +mo.dataset.mon, 1); renderPickup(); return; }
    const dy = e.target.closest('[data-day]'); if (dy) { const [y, m, d] = dy.dataset.day.split('-').map(Number); picked = new Date(y, m - 1, d); $('co-msg').hidden = true; renderPickup(); return; }
    if (e.target.id === 'co-pb-go') { $('co-side').scrollIntoView({ behavior: 'smooth', block: 'start' }); return; }
    if (e.target.id === 'co-pay') {
      const msg = $('co-msg');
      msg.textContent = !boxes() ? 'Add at least one box first.'
        : !spot ? 'Pick a pickup spot first.'
        : !picked ? 'Pick a pickup date first.'
        : `This is the design mockup, so payment isn't hooked up yet. In the real page this goes to the secure payment step, then a receipt with your boxes, photographs, and pickup on ${long(picked)}.`;
      msg.hidden = false; return;
    }
  });
  document.addEventListener('change', e => {
    if (e.target.name === 'spot') { spot = e.target.value; month = null; $('co-msg').hidden = true; renderPickup(); }
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && !co.hidden) closeCo();
    if ((e.key === 'Enter' || e.key === ' ') && e.target.matches('[data-pick]')) { e.preventDefault(); openCo(null, e.target.dataset.pick); }
  });

  // Keep the two Order buttons drawing the eye (Kawika, 2026-10-15): a thin outline in Baker's Heart gold with one
  // spark circling it, plus a light sweep across the button. People who ask their device for less motion get the
  // outline with nothing moving.
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const NS = 'http://www.w3.org/2000/svg';
  document.querySelectorAll('.btn-order').forEach((btn, i) => {
    const clip = document.createElement('span');
    clip.className = 'shine-clip'; clip.setAttribute('aria-hidden', 'true');
    const shine = document.createElement('span');
    shine.className = 'shine'; clip.appendChild(shine); btn.appendChild(clip);
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('class', 'trace'); svg.setAttribute('aria-hidden', 'true');
    const base = document.createElementNS(NS, 'rect'), spark = document.createElementNS(NS, 'rect');
    base.setAttribute('class', 'trace-base'); spark.setAttribute('class', 'trace-spark');
    for (const r of [base, spark]) { r.setAttribute('pathLength', '100'); r.setAttribute('x', '1'); r.setAttribute('y', '1'); svg.appendChild(r); }
    btn.appendChild(svg);
    const fit = () => {
      const w = btn.offsetWidth + 12, h = btn.offsetHeight + 12;
      svg.setAttribute('width', w + 2); svg.setAttribute('height', h + 2); svg.setAttribute('viewBox', `0 0 ${w + 2} ${h + 2}`);
      for (const r of [base, spark]) { r.setAttribute('width', w); r.setAttribute('height', h); }
    };
    fit(); new ResizeObserver(fit).observe(btn);
    if (still) { spark.style.display = 'none'; return; }
    spark.animate([{ strokeDashoffset: 0 }, { strokeDashoffset: -100 }],
      { duration: 3000, iterations: Infinity, easing: 'linear', delay: -1500 * i });
    shine.animate([
      { transform: 'translateX(-130%) skewX(-20deg)', offset: 0 },
      { transform: 'translateX(330%) skewX(-20deg)', offset: 0.3 },
      { transform: 'translateX(330%) skewX(-20deg)', offset: 1 },
    ], { duration: 3600, iterations: Infinity, easing: 'ease-in-out', delay: 400 + 600 * i });
  });

  tiles(); render();
  window.__co = { order, open: openCo, state: () => ({ tab, spot, picked: picked && key(picked), floor: key(floor) }) };
})();
</script>
"""
swap("</footer>\n</body>", "</footer>\n" + WINDOW + JS + "</body>")

# ---------- sale first (Kawika, 2026-10-15): the boxes and order buttons come right after the opening ----------
i = s.index("  <!-- The boxes -->\n")
j = s.index("  <!-- Who's behind it -->")
buy = s[i:j]
s = s[:i] + s[j:]
d0 = s.index('    <div class="diptych">')
d1 = s.index("    </div>\n  </section>", d0) + len("    </div>\n")
dip = s[d0:d1]
s = s[:d0] + s[d1:]
p0 = buy.index('    <p class="prose">')
p1 = buy.index("</p>\n", p0) + len("</p>\n")
note = buy[p0:p1].replace('<p class="prose">', '<p class="prose box-note">')
buy = buy[:p0] + buy[p1:]
for line in ('    <p class="eyebrow">The gift</p>\n', "    <h2>Two boxes</h2>\n"):
    assert buy.count(line) == 1
    buy = buy.replace(line, "")
buy = buy.replace('<section class="wrap section" id="boxes">', '<section class="wrap buy" id="boxes">')
# The box details sit under the photo wall; a "+" ties the boxes to the photograph (Kawika, 2026-10-15).
k = buy.rindex("  </section>")
buy = buy[:k] + note.replace("    <p", "    <p", 1) + buy[k:]
old_head = """      <div class="pick-head">
        <h3>Pick the photograph</h3>
        <p>Six to choose from, all of them Oʻahu. Shown to scale in their mats.</p>
      </div>"""
assert buy.count(old_head) == 1
buy = buy.replace(old_head + "\n", "")
# The wall sits right against the boxes, and each box gets its own + riding the seam (Kawika, 2026-10-15).
assert buy.count("      </article>") == 2
buy = buy.replace("      </article>", '        <span class="plus" aria-hidden="true">+</span>\n      </article>')
# The heading and its line go under the green wall (Kawika, 2026-10-15).
after_wall = '      <p class="bigger">'
assert buy.count(after_wall) == 1
buy = buy.replace(after_wall, """      <div class="pick-foot">
        <h3>Plus the photograph you pick</h3>
        <p>Every box comes with one matted print. Choose from these six, all of them Oʻahu, shown here to scale in their mats. Each box in your order can have a different one.</p>
      </div>
""" + after_wall)
# One frame around the boxes, the + and the photo wall, so they read as one offer (Kawika, 2026-10-15).
b0 = buy.index('    <div class="boxes">')
buy = buy[:b0] + '    <div class="offer">\n' + buy[b0:]
n0 = buy.index('    <p class="prose box-note">')
buy = buy[:n0] + "    </div>\n" + buy[n0:]
hero_end = s.index("  </section>\n", s.index("<!-- Opening -->")) + len("  </section>\n")
s = s[:hero_end] + "\n" + buy + "  <!-- Both halves of the gift -->\n  <section class=\"wrap section\">\n" + dip + "  </section>\n" + s[hero_end:]
swap("  .lockup { display: flex; align-items: center; justify-content: center; gap: clamp(16px, 4vw, 40px); padding-block: clamp(28px, 5vw, 48px) clamp(20px, 3vw, 28px); }\n  .lockup img { height: clamp(52px, 9vw, 92px); width: auto; }",
     "  .lockup { display: flex; align-items: center; justify-content: center; gap: clamp(14px, 3vw, 28px); padding-block: clamp(18px, 3vw, 28px) clamp(12px, 2vw, 18px); }\n  .lockup img { height: clamp(40px, 6vw, 64px); width: auto; }")
swap("  .hero { text-align: center; padding-top: clamp(28px, 4vw, 48px); }",
     "  .hero { text-align: center; padding-top: clamp(20px, 3vw, 32px); }\n  .hero .lede { margin-bottom: 0; }\n"
     "  .buy { padding-top: clamp(24px, 3vw, 36px); }\n  .buy .boxes { margin-top: 0; }\n  .box-note { margin: 28px auto 0; text-align: center; max-width: 60ch; }\n"
     "  .offer { background: var(--paper-2); border: 1px solid #d3cfbf; padding: 12px 12px 16px; }\n  .buy .box h3, .buy .price { font-size: clamp(1.5rem, 1.2rem + 1vw, 2rem); }\n"
     "  .offer .box { background: #fff; }\n"
     "  @media (min-width: 720px) { .offer { padding: 20px 24px 28px; } }\n"
     "  @media (min-width: 960px) { .offer { padding: 20px 28px 32px; } }\n"
     "  .buy .pick { margin-top: 0; }\n"
     "  .buy .box-body { padding-bottom: 48px; }\n"
     "  .btn-order { position: relative; justify-self: center; min-height: 44px; padding: 10px 22px; font-size: 0.9375rem; }\n"
     "  .btn-order .shine-clip { position: absolute; inset: 0; overflow: hidden; pointer-events: none; }\n"
     "  .btn-order .trace { position: absolute; left: -8px; top: -8px; overflow: visible; pointer-events: none; }\n"
     "  .btn-order .trace rect { fill: none; }\n"
     "  .btn-order .trace-base { stroke: rgba(194, 157, 59, .45); stroke-width: 1; }\n"
     "  .btn-order .trace-spark { stroke: #c29d3b; stroke-width: 2.5; stroke-linecap: round; stroke-dasharray: 12 88; }\n"
     "  .btn-order .shine { position: absolute; top: -20%; bottom: -20%; left: 0; width: 45%; pointer-events: none; transform: translateX(-130%) skewX(-20deg);\n"
     "    background: linear-gradient(90deg, rgba(255, 255, 255, 0), rgba(255, 255, 255, .45), rgba(255, 255, 255, 0)); }\n"
     "  .buy .box { position: relative; }\n"
     "  .buy .box .plus { position: absolute; left: 50%; bottom: -1px; transform: translate(-50%, 50%); z-index: 2; margin: 0;\n"
     "    box-shadow: 0 0 0 4px #fff, 0 3px 10px rgba(0, 0, 0, .25); }\n"
     "  .buy .wall { margin-top: 0; padding-top: clamp(48px, 6vw, 64px); }\n"
     "  @media (max-width: 719px) { .buy .box:first-child .plus { display: none; } }\n"
     "  .buy .pick-head { text-align: center; }\n"
     "  .buy .pick-foot { text-align: center; margin-top: clamp(20px, 3vw, 28px); }\n"
     "  .buy .pick-foot h3 { margin-bottom: 10px; }\n"
     "  .buy .pick-foot p { max-width: 56ch; margin: 0 auto; color: var(--ink-2); }\n"
     "  .plus { display: grid; place-items: center; width: 52px; height: 52px; margin: 0 auto 18px; border-radius: 50%; background: var(--gold); color: #fff; font: 300 36px/1 var(--sans); padding-bottom: 3px; }\n"
     "  .wrap.hero h1 { font-size: clamp(2.5rem, 1.6rem + 3.2vw, 4rem); max-width: 20em; }\n"
     "  @media (min-width: 960px) {\n"
     "    .buy .box { grid-template-columns: 0.9fr 1fr; grid-template-rows: none; }\n"
     "    .buy .box > img { aspect-ratio: auto; height: 100%; }\n"
     "  }\n"
     "  .just { padding-bottom: var(--space); }\n"
     "  .just-grid { display: grid; gap: 24px; }\n"
     "  .just-card { background: var(--card); border: 1px solid var(--rule); padding: clamp(24px, 3vw, 36px); display: grid; gap: 12px; align-content: start; justify-items: start; }\n"
     "  .just-card h3 { font-size: var(--step-2); }\n"
     "  .just-card p { margin: 0; color: var(--ink-2); max-width: 46ch; }\n"
     "  .btn-line { background: transparent; color: var(--green); margin-top: 6px; }\n"
     "  .btn-line:hover { background: var(--green); color: #fff; }\n"
     "  @media (min-width: 720px) { .just-grid { grid-template-columns: 1fr 1fr; } }")

# Only one half of the gift: send them to the right store (Kawika, 2026-10-15). It replaces the line under the photo wall.
swap('      <p class="bigger">Want something bigger for a client\'s lobby? Kawika\'s photographs also come on metal and canvas, from $210.</p>\n', "")
swap("</main>", """  <!-- Just one half of the gift -->
  <section class="wrap section just">
    <div class="just-grid">
      <article class="just-card">
        <h3>Just looking for cookies?</h3>
        <p>Baker's Heart's whole holiday collection is on the Touch A Heart store, from single-flavor boxes to gift boxes. You can order now for pickup, delivery, or shipping starting November 16.</p>
        <a class="btn btn-line" href="https://touchahearthawaii.org/collections/bh-holiday">Shop the Baker's Heart holiday collection</a>
      </article>
      <article class="just-card">
        <h3>Just looking for prints?</h3>
        <p>Kawika's Hawaiʻi prints are on kawikalopez.com, with matted prints from $55 and metal and canvas from $210.</p>
        <a class="btn btn-line" href="https://kawikalopez.com/store/">Shop Kawika's prints</a>
      </article>
    </div>
  </section>

</main>""")

OUT.write_text(s, encoding="utf-8")
print(f"wrote {OUT} ({len(s) // 1024} KB)")
