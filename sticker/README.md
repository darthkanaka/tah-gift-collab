# Mailer sticker (holiday gift boxes)

The sticker that goes on the 12.75 x 15 rigid mailers holding Kawika's matted prints. Approved by Kawika on 2026-10-16: layout C, a framed square with a cream center inside a frame of Jill's Comfort and Joy leaf art and a gold keyline, his logo only, and the words "BAKER'S HEART × KAWIKA LOPEZ" and "HOLIDAY 2026" (the Baker's Heart logo is already on the cookies).

- `print/sticker-4in-print.png` is the file to upload (4 x 4 inch, 300 dpi, 1/8 inch bleed). Recommended order: Sticker Mule, rounded corner stickers, 4 x 4, matte. Held until Robin and Jenn approve the page and buyers show interest.
- `print/sticker-3.5in-print.png` is the same design at 3.5 inches. `print/sticker-4in-guides.png` shows the cut line (red) and safe area (blue). `print/mailer-mockup-4in.png` shows it on the mailer to scale.
- `make_print.py` renders the print files with headless Chrome from Jill's background (`~/Desktop/bh_holidaybackground_r0-01 2.png`, a copy in the vault at `projects/bakers-heart-assets/`) and Kawika's logo from the kawikalopez-site repo. `make_options.py` and `sticker-options.tpl.html` made the three option boards Kawika chose from.
- `bh_gold.png` is the Baker's Heart logo with its cream reflection removed, for dark backgrounds (unused in the chosen design). `kl-cream.svg` is Kawika's logo in cream.
