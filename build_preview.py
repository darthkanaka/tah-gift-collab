"""Build the review copy of the holiday gift boxes page for Robin's team (2026-10-16).

Takes the page rendered by the kawikalopez.com build on the holiday-gift-boxes branch and makes a
standalone copy for this repo (darthkanaka.github.io/tah-gift-collab):

  gifts/holiday-gift-boxes.html   the page, with a preview banner, no analytics, and links to
                                  kawikalopez.com pages made absolute
  assets/...                      every file the page uses, copied from the site
  index.html                      sends the old proposal link on to the page

Checkout runs in Stripe test mode through the deployed gift checkout script, whose BASE_TEST
Script Property must be https://darthkanaka.github.io/tah-gift-collab/ so Stripe returns here.

First, in ~/Documents/Developer/kawikalopez-site-gift:
  KL_BH_PREVIEW=1 python3 tools/build.py --production
Then here: python3 build_preview.py
"""
import re
import shutil
from pathlib import Path

SITE = Path.home() / "Documents/Developer/kawikalopez-site-gift"
HERE = Path(__file__).resolve().parent
PAGE = SITE / "gifts/holiday-gift-boxes.html"

s = PAGE.read_text(encoding="utf-8")
assert 'data-mode="test"' in s, "the review copy must be a test mode build"

# No analytics from the review copy.
s, n = re.subn(r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\n<script>window\.dataLayer[^<]*</script>\n', "", s)
assert n == 1, "analytics block not found"

# Links to kawikalopez.com pages (not assets) go to the live site.
s = re.sub(r'href="\.\./(?!assets/)([^"]*)"', lambda m: f'href="https://kawikalopez.com/{m.group(1)}"', s)

# A banner so nobody mistakes the review copy for the real thing.
banner = ('<p style="background:#1b1a18;color:#f4f2ed;text-align:center;font:500 13px/1.4 Inter,system-ui,sans-serif;'
          'padding:8px 16px;margin:0">A preview for Touch A Heart from Kawika Lopez. Checkout is in test mode, so nothing is charged. '
          'Use card 4242 4242 4242 4242 with any future date and any CVC.</p>\n')
s = s.replace('<body class="t-gift-boxes">\n', '<body class="t-gift-boxes">\n' + banner, 1)
assert banner in s

# Every site file the page uses: assets in the HTML, fonts in the CSS, print images the window draws.
files = {m.split("?")[0] for m in re.findall(r'\.\./(assets/[^"\')\s]+)', s)}
css = (SITE / "assets/css/bh-gift.css").read_text()
files |= {"assets/" + f for f in re.findall(r'url\("\.\./([^"]+)"', css)}
rules = (SITE / "assets/js/bh-pickup.js").read_text()
files |= {f"assets/img/prints/{img}-480.jpg" for img in re.findall(r'img: "([^"]+)"', rules)}
for f in sorted(files):
    src, dst = SITE / f, HERE / f
    assert src.exists(), f"missing {f}"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

out = HERE / "gifts/holiday-gift-boxes.html"
out.parent.mkdir(exist_ok=True)
out.write_text(s, encoding="utf-8")

(HERE / "index.html").write_text("""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex, nofollow">
<title>Holiday gift boxes preview</title>
<meta http-equiv="refresh" content="0; url=gifts/holiday-gift-boxes">
<script>location.replace("gifts/holiday-gift-boxes" + location.search);</script>
</head>
<body><p><a href="gifts/holiday-gift-boxes">Open the holiday gift boxes preview</a></p></body>
</html>
""", encoding="utf-8")
print(f"page {len(s) // 1024} KB, {len(files)} asset files")
