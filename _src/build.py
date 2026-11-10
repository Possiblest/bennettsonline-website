"""Build the Vault Movement static site.

  python3 _src/build.py                 -> writes every page + SEO files + docs into the repo root
  python3 _src/build.py --dc OUT BLOBS  -> also writes design-canvas artboards to OUT using the BLOBS json map
"""
import json, os, sys, csv, io
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib
from lib import *
import pages_core, pages_more
from pages_core import PAGES

ROOT = Path(__file__).resolve().parent.parent
VER = UPDATED.replace("-", "")

def render_all():
    report = []
    for meta, fn in PAGES:
        p = dict(meta); lib.MODE["dc"] = False; CUR["faqs"] = []
        body = fn(p)
        html_out = shell(p, body).replace('/assets/css/site.css"', f'/assets/css/site.css?v={VER}"').replace('/assets/js/site.js"', f'/assets/js/site.js?v={VER}"')
        out = ROOT / p["file"]; out.parent.mkdir(parents=True, exist_ok=True); out.write_text(html_out)
        report.append(p)
        tl, dl = len(p["title"]), len(p["desc"])
        flag = "" if tl <= 60 and dl <= 155 else "  <-- LENGTH"
        print(f"{p['path']:45s} t{tl:3d} d{dl:3d}{flag}")
    return report

def render_dc(outdir, blobs):
    css = (ROOT / "assets/css/site.css").read_text()
    outdir = Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    for meta, fn in PAGES:
        if not meta.get("dc"): continue
        name, hpx = meta["dc"]
        p = dict(meta); lib.MODE["dc"] = True; CUR["faqs"] = []
        body = fn(p)
        (outdir / name).write_text(dc_shell(p, body, css, blobs, hpx))
        print("dc:", name)
    lib.MODE["dc"] = False

def write(path, text):
    f = ROOT / path; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(text)

def seo_files(pages):
    idx = [p for p in pages if not p.get("noindex")]
    pri = lambda p: "1.0" if p["path"] == "/" else ("0.9" if p["path"] in ("/journey", "/experience-session", "/programmes/vault-12", "/kids", "/programmes/movement-and-strength", "/programmes/personal-training") else "0.7")
    urls = "".join(f"  <url><loc>{SITE}{'' if p['path'] == '/' else p['path']}{'/' if p['path'] == '/' else ''}</loc><lastmod>{UPDATED}</lastmod><priority>{pri(p)}</priority></url>\n" for p in idx)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')

    search = ["Googlebot", "Bingbot", "Applebot", "OAI-SearchBot", "ChatGPT-User", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User"]
    training = ["GPTBot", "ClaudeBot", "Google-Extended"]
    robots = "# Vault Movement — robots.txt\n\nUser-agent: *\nAllow: /\nDisallow: /thank-you\n\n# Search engines and AI answer engines: allowed\n"
    robots += "".join(f"User-agent: {b}\n" for b in search) + "Allow: /\nDisallow: /thank-you\n\n"
    robots += "# AI training crawlers: allowed by default (owner decision). To opt out, change Allow: / to Disallow: / below.\n"
    robots += "".join(f"User-agent: {b}\n" for b in training) + "Allow: /\nDisallow: /thank-you\n\n"
    robots += f"Sitemap: {SITE}/sitemap.xml\n"
    write("robots.txt", robots)

    llms = f"""# Vault Movement

> Vault Movement (legal name Vault Movement Pvt Ltd), formerly Chennai Parkour, is a Fitness & Lifestyle Studio in Chennai, India, established in 2008. It runs coach-led strength, movement and lifestyle programmes for adults and kids. Tagline: Movement for Everybody.

## Key facts
- Name: Vault Movement (legal: Vault Movement Pvt Ltd). Formerly: Chennai Parkour. Established 2008, Chennai.
- Type: Fitness & Lifestyle Studio.
- Studios: City Studio · Ekkattuthangal — {STUDIOS[0]['address']}. Coast Studio · Injambakkam, ECR — {STUDIOS[1]['address']}.
- Hours: both studios, every day, 6:00 AM – 9:00 PM.
- Phone and WhatsApp: {PHONE}.
- Programmes: Vault 12 · Movement & Strength · Personal Training (PT Trio, PT 1:1) · Vault Kids (Toddlers, Under 10, Under 14) · More from Vault Movement.
- Method: The Vault — a library of 750+ movements built since 2008, with five coach-verified levels (Vault One to Vault Five). Member app: My Vault (app.vaultmovement.fit).
- Prices are not published. Every journey starts with an Experience Session; plans are shared on a call or on WhatsApp.
- Executive Coaches: Vishal Kumar, Vishwa Dayakaran, Vignesh Raghavan (18+ years each).
- Trusted to train TNCF, CISF, NSG and Tamil Nadu Fire & Rescue Services. Movement work for the Tamil films Chekka Chivantha Vaanam, Irumbu Thirai and Kanithan.

## Start here
- [Home]({SITE}/): overview, where to start, studios and hours
- [Your Journey]({SITE}/journey): Experience Session → Vault 12 → Movement & Strength → Personal Training
- [Experience Session]({SITE}/experience-session): the first visit — baseline assessment, coach consultation, programme match

## Programmes
- [Vault 12]({SITE}/programmes/vault-12): 12-week, coach-led starter for basic fitness, sustainable weight loss and strength
- [Movement & Strength]({SITE}/programmes/movement-and-strength): 6 days a week, 60-minute sessions, Vault One to Three
- [Personal Training]({SITE}/programmes/personal-training): PT Trio and PT 1:1
- [Vault Kids]({SITE}/kids): Toddlers, Under 10 and Under 14 batches
- [More from Vault Movement]({SITE}/more): Adaptive Movement, workshops, schools, corporate, armed forces, events, coach certification

## About
- [The Vault Method]({SITE}/vault-method)
- [Story behind the name]({SITE}/story)
- [Philosophy]({SITE}/philosophy)
- [Coaches]({SITE}/coaches)
- [Locations]({SITE}/locations)
- [FAQ]({SITE}/faq)

## Optional
- [Franchise]({SITE}/franchise)
- [Member stories]({SITE}/stories)
"""
    write("llms.txt", llms)

    write("site.webmanifest", json.dumps({
        "name": "Vault Movement", "short_name": "Vault Movement", "description": "Movement for Everybody — Fitness & Lifestyle Studio",
        "start_url": "/", "display": "standalone", "theme_color": "#1F4BB8", "background_color": "#F4EFE6",
        "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
                  {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}, indent=2))

REDIRECTS = [
    ("/", "/"), ("/index.html", "/"),
    ("/program-parkour-movement.html", "/programmes/movement-and-strength"),
    ("/program-calisthenics.html", "/programmes/movement-and-strength"),
    ("/program-kids-events.html", "/more/birthdays-and-events"),
    ("/program-kaladi.html", "/more/kaladi-kuthuvarisai"),
    ("/program-competitive-sports.html", "/more/sports-performance-ltad"),
    ("/program-schools.html", "/more/schools-and-colleges"),
    ("/program-corporate.html", "/more/corporate"),
    ("/program-armed-forces.html", "/more/armed-forces-tactical"),
    ("/program-stunts.html", "/more/screen-movement"),
    ("/program-coach-cert.html", "/more/coach-certification"),
]

def deploy_files():
    hosts = ["chennaiparkour.fit", "www.chennaiparkour.fit"]
    red = []
    for hst in hosts:
        for old, new in REDIRECTS:
            if old == "/":
                continue
            red.append({"source": old, "has": [{"type": "host", "value": hst}], "destination": "https://vaultmovement.fit" + new, "statusCode": 301})
        red.append({"source": "/assets/:path*", "has": [{"type": "host", "value": hst}], "destination": "https://vaultmovement.fit/assets/:path*", "statusCode": 301})
        red.append({"source": "/:path*", "has": [{"type": "host", "value": hst}], "destination": "https://vaultmovement.fit/", "statusCode": 301})
    red.append({"source": "/programmes", "destination": "/more", "statusCode": 301})
    red.append({"source": "/index", "destination": "/", "statusCode": 301})
    vercel = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "cleanUrls": True, "trailingSlash": False,
        "redirects": red,
        "headers": [
            {"source": "/(.*)", "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()"}]},
            {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=604800, stale-while-revalidate=86400"}]},
            {"source": "/(favicon.ico|favicon.svg|apple-touch-icon.png|icon-192.png|icon-512.png)", "headers": [{"key": "Cache-Control", "value": "public, max-age=2592000"}]},
        ],
    }
    write("vercel.json", json.dumps(vercel, indent=2))
    old = {"$schema": "https://openapi.vercel.sh/vercel.json",
           "redirects": [{"source": o, "destination": "https://vaultmovement.fit" + n, "statusCode": 301} for o, n in REDIRECTS if o != "/"]
           + [{"source": "/assets/:path*", "destination": "https://vaultmovement.fit/assets/:path*", "statusCode": 301},
              {"source": "/:path*", "destination": "https://vaultmovement.fit/", "statusCode": 301}]}
    write("docs/old-domain-vercel.json", json.dumps(old, indent=2))
    buf = io.StringIO(); w = csv.writer(buf)
    w.writerow(["old_url", "new_url", "status", "note"])
    for o, n in REDIRECTS:
        note = "Anchors (#about, #programs, #journey, #coaches, #locations, #leadform) cannot be redirected server-side; they land on the home page." if o == "/" else ""
        w.writerow(["https://www.chennaiparkour.fit" + o, "https://vaultmovement.fit" + n, 301, note])
    w.writerow(["https://www.chennaiparkour.fit/assets/*", "https://vaultmovement.fit/assets/*", 301, "Keeps old image links working once the old assets folder is copied over"])
    w.writerow(["https://www.chennaiparkour.fit/* (anything else)", "https://vaultmovement.fit/", 301, "Catch-all; keep for at least 12 months"])
    write("docs/redirects.csv", buf.getvalue())
    write(".vercelignore", "_src\ndocs\nREADME.md\n")

def docs(pages):
    buf = io.StringIO(); w = csv.writer(buf)
    w.writerow(["path", "title", "title_chars", "meta_description", "description_chars", "indexed"])
    for p in pages:
        w.writerow([p["path"], p["title"], len(p["title"]), p["desc"], len(p["desc"]), "no" if p.get("noindex") else "yes"])
    write("docs/meta-titles-descriptions.csv", buf.getvalue())
    # JSON-LD templates
    jd = "docs/jsonld/"
    write(jd + "organization.json", json.dumps({"@context": "https://schema.org", **org_ld()}, indent=2, ensure_ascii=False))
    for s in STUDIOS:
        write(jd + f"healthclub-{s['key']}.json", json.dumps({"@context": "https://schema.org", **studio_ld(s)}, indent=2, ensure_ascii=False))
    write(jd + "service-template.json", json.dumps({"@context": "https://schema.org", "@type": "Service", "name": "<Programme name>", "serviceType": "<Type>",
           "description": "<Same summary as the page>", "provider": {"@id": ORG_ID}, "areaServed": {"@type": "City", "name": "Chennai"}, "url": SITE + "/<path>"}, indent=2))
    write(jd + "event-template.json", json.dumps({"@context": "https://schema.org", "@type": "Event", "name": "<Workshop name, e.g. Bharatanatyam workshop>",
           "startDate": "2026-12-01T07:00:00+05:30", "endDate": "2026-12-01T09:00:00+05:30", "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
           "eventStatus": "https://schema.org/EventScheduled", "location": {"@id": SITE + "/locations/ekkattuthangal#studio"}, "organizer": {"@id": ORG_ID},
           "description": "<Exactly what the page says>", "url": SITE + "/more/<workshop-page>"}, indent=2))
    for n, _, u, _, b in pages_more.COACHES:
        write(jd + f"person-{n.split()[0].lower()}.json", json.dumps({"@context": "https://schema.org", "@type": "Person", "name": n, "jobTitle": "Executive Coach",
              "worksFor": {"@id": ORG_ID}, "description": strip_tags(b), "sameAs": [u]}, indent=2, ensure_ascii=False))
    write(jd + "README.md", "These templates mirror the JSON-LD already embedded in every page's <head>. Keep them identical to the visible page text. No Review or AggregateRating markup for our own testimonials. No prices in Service markup.\n")

if __name__ == "__main__":
    pages = render_all()
    seo_files(pages); deploy_files(); docs(pages)
    if len(sys.argv) > 1 and sys.argv[1] == "--dc":
        render_dc(sys.argv[2], json.loads(Path(sys.argv[3]).read_text()))
    print(len(pages), "pages")
