"""Print-ready files for the framed square mailer sticker (layout C), at 300 dpi with 1/8 inch bleed."""
import base64, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
BG_FULL = "/Users/veex/Desktop/bh_holidaybackground_r0-01 2.png"
b64 = lambda p, mime: f"data:{mime};base64," + base64.b64encode(Path(p).read_bytes()).decode()
BG = b64(BG_FULL, "image/png")
KLD = b64(Path.home() / "Documents/Developer/kawikalopez-site/assets/img/site/logo.svg", "image/svg+xml")
CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DPI, BLEED = 300, 0.125

def page(size, guides=False):
    u = DPI * size / 3.5          # the design is drawn in 3.5 inch units, scaled to the sticker size
    full = (size + 2 * BLEED) * DPI
    g = ""
    if guides:
        g = (f'<div style="position:absolute;left:{BLEED*DPI}px;top:{BLEED*DPI}px;width:{size*DPI}px;height:{size*DPI}px;'
             f'border:3px dashed #e0245e;border-radius:{0.12*u}px;box-sizing:border-box"></div>'
             f'<div style="position:absolute;left:{(BLEED+0.125)*DPI}px;top:{(BLEED+0.125)*DPI}px;width:{(size-0.25)*DPI}px;height:{(size-0.25)*DPI}px;'
             f'border:3px dotted #1e88e5;box-sizing:border-box"></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@600&display=block">
<style>
html,body{{margin:0;width:{full}px;height:{full}px;overflow:hidden}}
.art{{position:absolute;inset:0;background:url({BG}) no-repeat;background-size:{11.113*DPI}px auto;
     background-position:{-5.9*u + BLEED*DPI}px {-0.4*u + BLEED*DPI}px}}
.panel{{position:absolute;left:{BLEED*DPI + .38*u}px;top:{BLEED*DPI + .38*u}px;width:{size*DPI - .76*u}px;height:{size*DPI - .76*u}px;
       background:#f6f1e4;border-radius:{.05*u}px;box-shadow:0 0 0 {.02*u}px #c29d3b;display:flex;flex-direction:column;align-items:center;justify-content:center}}
.kl{{width:{1.9*u}px}}
.rule{{width:{.5*u}px;height:{.02*u}px;background:#c29d3b;margin:{.08*u}px 0 {.04*u}px}}
.cap{{font:600 {.085*u}px/1 Inter,sans-serif;letter-spacing:.16em;color:#6b5a2e;margin-top:{.03*u}px}}
.cap.soft{{color:#8a7a52;letter-spacing:.22em}}
</style></head><body><div class="art"></div>
<div class="panel"><img class="kl" src="{KLD}" alt=""><span class="rule"></span>
<span class="cap">BAKER’S HEART × KAWIKA LOPEZ</span><span class="cap soft">HOLIDAY 2026</span></div>{g}</body></html>"""

out_dir = Path(sys.argv[1])
out_dir.mkdir(parents=True, exist_ok=True)
for size in (4.0, 3.5):
    for guides in (False, True):
        html = H / f"print-{size}-{int(guides)}.html"
        html.write_text(page(size, guides))
        full = round((size + 2 * BLEED) * DPI)
        name = f"sticker-{str(size).replace('.0','')}in-{'guides' if guides else 'print'}.png"
        subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                        f"--window-size={full},{full}", "--virtual-time-budget=8000", f"--screenshot={out_dir / name}", html.as_uri()],
                       check=True, capture_output=True)
        subprocess.run(["sips", "-s", "dpiWidth", "300", "-s", "dpiHeight", "300", str(out_dir / name)], check=True, capture_output=True)
        print(name, full, "px")
