"""Builds brand assets for the Vault Movement site.

Inputs: transparent logo crops (lockup, crest) and character crops.
Outputs into the repo root: assets/brand, assets/characters, favicons, manifest icons, OG image.
Run: python3 _src/make_assets.py <brand_crops_dir> <character_crops_dir>
"""
import sys, os, io
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BRAND_IN = Path(sys.argv[1])
CHAR_IN = Path(sys.argv[2])

COBALT = "#1F4BB8"
IVORY = (244, 239, 230, 255)

# The V-ring, rebuilt as vector from the supplied mark (viewBox 512 x 566).
def vring_svg(stroke=COBALT, dark=None, uid="v", size_attr=""):
    dark_css = ""
    if dark:
        dark_css = f'<style>@media (prefers-color-scheme: dark){{.m{{stroke:{dark}}}}}</style>'
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 566"{size_attr}>{dark_css}'
        f'<defs>'
        f'<mask id="{uid}r" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="566"><rect width="512" height="566" fill="#fff"/><path d="M69.75 18 L256 390.5" stroke="#000" stroke-width="95" fill="none"/></mask>'
        f'<mask id="{uid}a" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="566"><rect width="512" height="566" fill="#fff"/><circle cx="256" cy="310" r="222" stroke="#000" stroke-width="96" fill="none"/><path d="M69.75 18 L256 390.5" stroke="#fff" stroke-width="56" fill="none"/></mask>'
        f'</defs>'
        f'<circle class="m" cx="256" cy="310" r="222" fill="none" stroke="{stroke}" stroke-width="56" mask="url(#{uid}r)"/>'
        f'<path class="m" d="M69.75 18 L256 390.5 L442.25 18" fill="none" stroke="{stroke}" stroke-width="55" stroke-linejoin="miter" mask="url(#{uid}a)"/>'
        f'</svg>'
    )

def save_webp_png(img, base, width):
    h = round(img.height * width / img.width)
    r = img.resize((width, h), Image.LANCZOS)
    r.save(str(base) + ".webp", "WEBP", quality=92, alpha_quality=90, method=6)
    r.save(str(base) + ".png", optimize=True)
    return r.size

def main():
    brand = ROOT / "assets" / "brand"; brand.mkdir(parents=True, exist_ok=True)
    chars = ROOT / "assets" / "characters"; chars.mkdir(parents=True, exist_ok=True)
    og = ROOT / "assets" / "og"; og.mkdir(parents=True, exist_ok=True)

    lock = Image.open(BRAND_IN / "lockup_full.png").convert("RGBA")
    crest = Image.open(BRAND_IN / "crest_full.png").convert("RGBA")
    word = Image.open(BRAND_IN / "wordmark_full.png").convert("RGBA")
    print("lockup", save_webp_png(lock, brand / "lockup", 560))
    print("crest", save_webp_png(crest, brand / "crest", 440))
    print("wordmark", save_webp_png(word, brand / "wordmark", 1200))

    (brand / "vring.svg").write_text(vring_svg(uid="b"))
    (ROOT / "favicon.svg").write_text(vring_svg(dark="#8FA8EC", uid="f"))

    for name in ["vee-curious", "mouve-mischievous", "vee-land"]:
        im = Image.open(CHAR_IN / f"{name}.png").convert("RGB")
        im.save(chars / f"{name}.webp", "WEBP", quality=88, method=6)
        print(name, im.size)

    # Raster icons via Chromium so the masked SVG renders exactly.
    from playwright.sync_api import sync_playwright
    svg = vring_svg(uid="r")
    def render(size, bg, mark_frac, path):
        mark_h = round(size * mark_frac)
        html = (f'<html><body style="margin:0;width:{size}px;height:{size}px;display:flex;align-items:center;justify-content:center;background:{bg}">'
                f'<div style="height:{mark_h}px;aspect-ratio:512/566">{svg.replace("<svg ", "<svg style=\'width:100%;height:100%;display:block\' ")}</div></body></html>')
        pg.set_viewport_size({"width": size, "height": size})
        pg.set_content(html)
        pg.screenshot(path=str(path), omit_background=(bg == "transparent"))
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        tmp = ROOT / "_src" / "_tmp"; tmp.mkdir(exist_ok=True)
        render(256, "transparent", 0.92, tmp / "fav256.png")
        render(180, "#F4EFE6", 0.66, ROOT / "apple-touch-icon.png")
        render(192, "#F4EFE6", 0.56, ROOT / "icon-192.png")
        render(512, "#F4EFE6", 0.56, ROOT / "icon-512.png")
        # OG image 1200x630: lockup on Ivory + tagline in Poppins (installed locally).
        import base64
        lock_png = "data:image/png;base64," + base64.b64encode((BRAND_IN / "lockup_full.png").read_bytes()).decode()
        og_html = f'''<html><body style="margin:0;width:1200px;height:630px;background:#F4EFE6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px;font-family:Poppins,sans-serif;position:relative">
<img src="{lock_png}" style="width:800px;height:auto;display:block">
<div style="width:96px;height:6px;border-radius:6px;background:#F5B700"></div>
<div style="font-weight:700;font-size:54px;letter-spacing:-0.5px;color:#0B1426">Movement for Everybody</div>
<div style="position:absolute;bottom:34px;left:0;right:0;text-align:center;font-weight:500;font-size:22px;color:#2A2F38;letter-spacing:.5px">vaultmovement.fit · formerly Chennai Parkour</div>
</body></html>'''
        pg.set_viewport_size({"width": 1200, "height": 630})
        pg.set_content(og_html); pg.wait_for_timeout(300)
        pg.screenshot(path=str(og / "og-default.png"))
        b.close()
    fav = Image.open(tmp / "fav256.png").convert("RGBA")
    fav.save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    for f in tmp.iterdir(): f.unlink()
    tmp.rmdir()
    print("icons + og done")

if __name__ == "__main__":
    main()
