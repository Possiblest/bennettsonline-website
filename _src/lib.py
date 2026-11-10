"""Vault Movement static site — shared config, components and page shell.

Two render targets:
  site  -> plain static HTML for GitHub + Vercel (external CSS/JS)
  dc    -> Design-canvas artboards (CSS inlined, no scripts, images as uploaded blobs)
"""
import html, json, re, urllib.parse

SITE = "https://vaultmovement.fit"
UPDATED = "2026-11-09"
UPDATED_TEXT = "9 November 2026"
MODE = {"dc": False}
CUR = {"faqs": [], "page": None}

PHONE = "+91 99626 96859"
TEL = "tel:+919962696859"
WA_BASE = "https://wa.me/919962696859"
APP = "https://app.vaultmovement.fit"
DEFAULT_WA = "Hi Vault Movement, I'd like to book an Experience Session."
HOURS = "Every day, 6:00 AM – 9:00 PM"
SOCIAL = [  # current handles; new ones to confirm
    ("Instagram", "https://www.instagram.com/chennaiparkour_official"),
    ("Instagram · ECR", "https://www.instagram.com/chennaiparkour_ecr"),
    ("Facebook", "https://www.facebook.com/ChennaiParkour"),
    ("YouTube", "https://www.youtube.com/ChennaiParkour"),
]

STUDIOS = [
    dict(key="city", name="City Studio", area="Ekkattuthangal", label="City Studio · Ekkattuthangal",
         path="/locations/ekkattuthangal",
         address="TS 69, Second Floor, SIDCO Industrial Estate, Ekkaduthangal, Chennai, Tamil Nadu 600032",
         street="TS 69, Second Floor, SIDCO Industrial Estate, Ekkaduthangal", postal="600032",
         map_q="TS 69, SIDCO Industrial Estate, Ekkaduthangal, Chennai 600032"),
    dict(key="coast", name="Coast Studio", area="Injambakkam, ECR", label="Coast Studio · Injambakkam, ECR",
         path="/locations/injambakkam-ecr",
         address="2nd floor, No 41 & 42, East Coast Road, Cholamandal Artists Village, Injambakkam, Chennai 600115",
         street="2nd floor, No 41 & 42, East Coast Road, Cholamandal Artists Village, Injambakkam", postal="600115",
         map_q="No 41 & 42, East Coast Road, Cholamandal Artists Village, Injambakkam, Chennai 600115"),
]

def h(s):
    return html.escape(s, quote=True)

def wa(msg=DEFAULT_WA):
    return WA_BASE + "?text=" + urllib.parse.quote(msg)

# ---------------------------------------------------------------- icons
ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "ext": '<path d="M14 5h5v5M19 5l-8 8M18 14v5H5V6h5"/>',
    "chat": '<path d="M4 19.5V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H8.5z"/><path d="M8.5 9.5h7M8.5 12.5h4.5"/>',
    "phone": '<path d="M5 4h3.2l1.8 4.6-2.4 1.5a11 11 0 0 0 6.3 6.3l1.5-2.4L20 15.8V19a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 20c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "camera": '<path d="M4 8h3l2-2.5h6L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "pencil": '<path d="M4 20l4-1 10-10-3-3L5 16z"/><path d="M13 7l3 3"/>',
    "group": '<circle cx="8" cy="7" r="3"/><circle cx="17" cy="9" r="2.2"/><path d="M2.5 19c.8-3.4 3-5.2 5.5-5.2s4.7 1.8 5.5 5.2M13.5 17.5c.6-2.3 2-3.6 3.5-3.6s2.9 1.3 3.5 3.6"/>',
    "mat": '<rect x="3" y="12" width="18" height="6" rx="1.5"/><path d="M9 12v6M15 12v6"/>',
    "steps": '<path d="M4 19h5v-5h5V9h6"/><path d="M17 6l3 3-3 3"/>',
    "balance": '<path d="M3 19h18"/><circle cx="12" cy="6" r="2.2"/><path d="M12 8.5V15M6.5 11.5h11M12 15l-2.5 4M12 15l2.5 4"/>',
    "jump": '<path d="M3 19h4M17 19h4"/><path d="M5 17c2-8 5-11 7-11s5 3 7 11"/><path d="M16.5 14.5l2.5 2.5 1-3.4"/>',
    "vault": '<rect x="7" y="13" width="10" height="7" rx="1"/><path d="M3 13c2.5-6 15.5-6 18 0"/>',
    "swing": '<path d="M3 4h18"/><path d="M9.5 4l2.5 5 2.5-5"/><circle cx="12" cy="11.5" r="2"/><path d="M12 13.5V19M9 16h6"/>',
    "lever": '<path d="M3 5h18"/><path d="M7 5v4"/><circle cx="7" cy="11" r="2"/><path d="M9 11h12"/>',
    "dumbbell": '<path d="M6.5 7v10M17.5 7v10M3.5 9.5v5M20.5 9.5v5M6.5 12h11"/>',
}

def icon(name, size=20, stroke="currentColor", sw=1.6, cls="ico"):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

def play_icon(size=22):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="#0B1426" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>'

LEVEL_NAMES = {1: "Vault One", 2: "Vault Two", 3: "Vault Three", 4: "Vault Four", 5: "Vault Five"}

def tally(n, color="#0B1426", height=24, sw=2.4, label=True):
    vbw = 24 if n >= 4 else 6 * n
    width = round(height * vbw / 24)
    lines = "".join(f'<line x1="{3 + 6 * i}" y1="3" x2="{3 + 6 * i}" y2="21" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>' for i in range(min(n, 4)))
    if n == 5:
        lines += f'<line x1="0.8" y1="17.6" x2="23.2" y2="6.4" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
    a11y = f'role="img" aria-label="{LEVEL_NAMES[n]}"' if label else 'aria-hidden="true"'
    return f'<svg class="tally" width="{width}" height="{height}" viewBox="0 0 {vbw} 24" {a11y}>{lines}</svg>'

def pill(n):
    col = "#F4EFE6" if n == 4 else "#0B1426"
    return f'<span class="pill lv{n}">{tally(n, col, 18, 2.6, label=False)}{LEVEL_NAMES[n]}</span>'

def vring(uid, animate=False, cls="", label="Vault Movement V-ring: a V breaking through a circle"):
    rc = ' class="vm-ring" transform="rotate(-114 256 310)"' if animate else ""
    vc = ' class="vm-vee"' if animate else ""
    return (f'<svg class="{cls}" viewBox="0 0 512 566" role="img" aria-label="{label}">'
            f'<defs><mask id="{uid}r" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="566"><rect width="512" height="566" fill="#fff"/><path d="M69.75 18 L256 390.5" stroke="#000" stroke-width="95" fill="none"/></mask>'
            f'<mask id="{uid}a" maskUnits="userSpaceOnUse" x="0" y="0" width="512" height="566"><rect width="512" height="566" fill="#fff"/><circle cx="256" cy="310" r="222" stroke="#000" stroke-width="96" fill="none"/><path d="M69.75 18 L256 390.5" stroke="#fff" stroke-width="56" fill="none"/></mask></defs>'
            f'<g mask="url(#{uid}r)"><circle{rc} cx="256" cy="310" r="222" fill="none" stroke="#1F4BB8" stroke-width="56"/></g>'
            f'<g mask="url(#{uid}a)"><path{vc} d="M69.75 18 L256 390.5 L442.25 18" fill="none" stroke="#1F4BB8" stroke-width="55" stroke-linejoin="miter"/></g></svg>')

# ---------------------------------------------------------------- small components
def book(placement, label="Book an Experience Session", cls="btn btn-primary"):
    return f'<a class="{cls}" href="/experience-session" data-cta="{placement}">{label}</a>'

def wa_btn(msg, placement, label="WhatsApp us", cls="btn btn-secondary", with_icon=True):
    ic = icon("chat", 20) if with_icon else ""
    return f'<a class="{cls}" href="{h(wa(msg))}" data-cta="{placement}">{ic}{label}</a>'

def call_link(placement, label="Call us"):
    return f'<a class="tert" href="{TEL}" data-cta="{placement}">{icon("phone", 18)}{label}</a>'

def cta_row(msg, placement):
    return f'<div class="row">{book(placement)}{wa_btn(msg, placement)}{call_link(placement)}</div>'

def arrow(label, href, cls="arrow", ext=False):
    extra = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="{cls}" href="{href}"{extra}>{label} {icon("ext" if ext else "arrow", 18)}</a>'

def sec(inner, cls="sec", id=None, wrap="wrap", attrs=""):
    i = f' id="{id}"' if id else ""
    return f'<section class="{cls}"{i}{attrs}><div class="{wrap}">{inner}</div></section>'

def head(eyebrow, title, intro=None, link=None, level=2, maxw=True):
    intro_html = f'<p class="body">{intro}</p>' if intro else ""
    left = f'<div class="stack{" maxw" if maxw else ""}"><p class="eyebrow">{eyebrow}</p><h{level} class="h2">{title}</h{level}>{intro_html}</div>'
    if link:
        return f'<div class="split">{left}{link}</div>'
    return left

def confirm(text="Confirm"):
    return f'<span class="confirm">{text}</span>'

def photo(desc, src=None, ratio="r-43", cls="", alt=None, kind=None):
    """A photo slot. With src (a ported current-site photo) it shows the photo, falling back to the label."""
    k = kind or ("Photo to port" if src else "Photo needed")
    label = f'{icon("camera", 26, "#2A2F38", 1.4)}<span class="ph-k">{k}</span><span class="ph-d">{desc}</span>'
    if src and not MODE["dc"]:
        return (f'<figure class="ph {ratio} {cls}"><img class="photo" src="{src}" alt="{h(alt or desc)}" loading="lazy" decoding="async" width="1200" height="900">'
                f'{label}</figure>')
    return f'<div class="ph {ratio} {cls}">{label}</div>'

def illus(desc, ratio="r-43", cls="ph-mist"):
    return f'<div class="ph {ratio} {cls}">{icon("pencil", 24, "#2A2F38", 1.4)}<span class="ph-k">Illustration needed</span><span class="ph-d">{desc}</span></div>'

def gallery(items, note=None):
    """items: list of (src, alt)."""
    figs = "".join(photo("Current-site photo " + src.split('/')[-1], src, "r-43", alt=alt) for src, alt in items)
    n = f'<p class="xs">{note}</p>' if note else ""
    return f'<div class="stack"><div class="gallery">{figs}</div>{n}</div>'

def checks(items, cols="g-340"):
    lis = ""
    for t, s in items:
        sub = f'<p class="small">{s}</p>' if s else ""
        lis += f'<li class="card card-pad"><span class="check-dot">{icon("check", 18, "#1F4BB8", 1.9)}</span><div class="stack-sm"><p class="h4">{t}</p>{sub}</div></li>'
    return f'<ul class="checks grid {cols}">{lis}</ul>'

def numcards(items, cols="g-260"):
    lis = "".join(f'<li class="card card-pad stack"><p class="num">{i+1:02d}</p><h3 class="h3">{t}</h3><p class="body">{b}</p></li>' for i, (t, b) in enumerate(items))
    return f'<ol class="grid {cols}" style="list-style:none">{lis}</ol>'

def chips(items, cls="chips"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def facts_band(items):
    cells = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items)
    return f'<section class="facts-band"><div class="wrap"><dl class="facts">{cells}</dl></div></section>'

def two_col(left, right):
    return f'<div class="row" style="align-items:flex-start;gap:40px 64px"><div style="flex:1 1 360px;min-width:0" class="stack">{left}</div><div style="flex:1.4 1 460px;min-width:0" class="stack">{right}</div></div>'

# ---------------------------------------------------------------- testimonials + Instagram
T = {
    "arun": dict(q="Chennai Parkour completely changed how I move through the city. In six months I went from zero fitness to vaulting walls I used to walk past every day.", who="Arun R.", meta="Parkour &amp; Movement · 8 months"),
    "santhosh": dict(q="The coaches here train you like athletes, not hobbyists. The calisthenics programme gave me strength I didn't know was possible from bodyweight alone.", who="Santhosh K.", meta="Calisthenics &amp; Strength · 14 months"),
    "vijay": dict(q="We used CPK for a corporate retreat for our 60-person team. The movement experience they designed was unlike any team-building activity we had done before.", who="Vijay N.", meta="Corporate Programme · Team Lead"),
    "karthik": dict(q="The Kaladi Kuthuvarisai sessions are unlike anything else in Chennai. You're learning a living martial art, not performing a recreation of one.", who="Karthik S.", meta="Kaladi Kuthuvarisai · 11 months"),
}

def tcard(key, light=False):
    t = T[key]
    return (f'<figure class="tcard{" tcard-light" if light else ""}"><blockquote><span class="q" aria-hidden="true">“</span>{h(t["q"])}<span class="q" aria-hidden="true">”</span></blockquote>'
            f'<figcaption><span class="who">{t["who"]}</span><span class="meta">{t["meta"]}</span></figcaption></figure>')

def tband(keys, title="In their words.", eyebrow="Member stories", link_all=True):
    cards = "".join(tcard(k) for k in keys)
    link = f'<div class="row">{arrow("All stories", "/stories")}</div>' if link_all else ""
    inner = f'<div class="stack-lg">{head(eyebrow, title, link=link)}<div class="grid g-460">{cards}</div>'
    return inner

def ig_cards(light=False):
    lc = " light" if light else ""
    reel = (f'<div class="ig-card{lc}"><span class="ig-play">{play_icon()}</span><p class="ig-title">Watch a member story</p>'
            f'<p class="ig-sub">Instagram reel from our Coast Studio · loads when you tap</p>'
            f'<a class="btn btn-primary btn-sm" href="https://www.instagram.com/reel/DZKZD8KzQRH/" data-ig="DZKZD8KzQRH" data-cta="ig-reel">Watch reel</a></div>')
    hl = ""
    for i, url in enumerate(["https://www.instagram.com/stories/highlights/17996246815225816/", "https://www.instagram.com/stories/highlights/18086576537080278/"], 1):
        hl += (f'<div class="ig-card{lc}"><span class="ig-play">{play_icon()}</span><p class="ig-title">Highlight title {i} {confirm()}</p>'
               f'<p class="ig-sub">Member stories on Instagram</p>'
               f'<a class="btn btn-primary btn-sm" href="{url}" target="_blank" rel="noopener" data-cta="ig-highlight-{i}">Watch on Instagram ↗</a></div>')
    return f'<div class="ig-grid">{reel}{hl}</div>'

def reels(ids, note=None):
    cards = "".join(
        f'<div class="reel-wrap"><a class="reel" href="https://www.instagram.com/reel/{i}/" data-ig="{i}"><span class="kicker">Instagram reel</span>'
        f'<span class="ig-play">{play_icon(28)}</span><span class="stack-sm"><span class="h4" style="color:#F4EFE6">Tap to load</span><span class="xs" style="color:#C9C6C0">Opens the reel here</span></span></a></div>'
        for i in ids)
    n = f'<p class="xs">{note}</p>' if note else ""
    return f'<div class="stack"><div class="reels">{cards}</div>{n}</div>'

# ---------------------------------------------------------------- FAQ
def faq_items(items, collect=True):
    out = ""
    for i, (q, a) in enumerate(items):
        if collect:
            CUR["faqs"].append((q, a))
        op = ' open="open"' if (i == 0 and collect) else ""
        ans = "".join(f"<p>{p}</p>" for p in (a if isinstance(a, list) else [a]))
        out += f'<details{op}><summary>{q}{icon("plus", 22, "#1F4BB8", 1.6, "plus")}</summary><div class="ans">{ans}</div></details>'
    return out

def faq_block(items, title="Questions, answered.", eyebrow="FAQ", all_link=True, updated=True):
    link = arrow("All FAQs", "/faq") if all_link else ""
    upd = f'<p class="updated" style="margin-top:24px">Last updated {UPDATED_TEXT}</p>' if updated else ""
    side = f'<div class="faq-side"><p class="eyebrow">{eyebrow}</p><h2 class="h2">{title}</h2>{link}</div>'
    return sec(f'<div class="faq-wrap">{side}<div class="faq">{faq_items(items)}{upd}</div></div>', "sec bg-silk", id="faq")

# ---------------------------------------------------------------- forms + CTA band
def zoho_box(programme="", studio="", title="Book an Experience Session form", form=None):
    if MODE["dc"]:
        return mock_form()
    df = f' data-form="{h(form)}"' if form else ""
    return (f'<div class="zoho" data-zoho="1" data-programme="{h(programme)}" data-studio="{h(studio)}" data-title="{h(title)}"{df}>'
            f'<div class="zoho-fallback"><p class="h4">Book an Experience Session</p><p class="small">The enquiry form loads here. If it doesn\'t, '
            f'<a href="{h((form or "https://forms.zohopublic.in/cpkformszoho1/form/WebsiteLeads/formperma/JdH2H50F6gaokRRyTUzDz5V_0EQ9sQ6OEVGA_8cIyiU"))}" target="_blank" rel="noopener">open the form in a new tab</a>, '
            f'WhatsApp or call {PHONE}.</p></div></div>')

def mock_form():
    f = lambda i, l, t="text": f'<div class="field"><label for="{i}">{l}</label><input class="input" id="{i}" type="{t}"></div>'
    return ('<div class="formcard-pad stack"><p class="kicker">Zoho form · WebsiteLeads (embedded on the live site)</p>'
            '<form class="mockform" aria-label="Experience Session enquiry (preview)">'
            + f("mf-n", "Your name") + f("mf-p", "Mobile number (WhatsApp)", "tel") + f("mf-e", "Email (optional)", "email")
            + '<div class="field"><label for="mf-s">Studio</label><select class="input" id="mf-s"><option>City Studio · Ekkattuthangal</option><option>Coast Studio · Injambakkam, ECR</option></select></div>'
            + '<div class="full row" style="gap:12px;align-items:flex-start"><input id="mf-c" type="checkbox" style="width:22px;height:22px;margin:2px 0 0;accent-color:#1F4BB8"><label for="mf-c" class="small" style="flex:1">I agree to Vault Movement contacting me about this enquiry, as set out in the <a href="#">Privacy Policy</a>.</label></div>'
            + '<div class="full"><button class="btn btn-primary" type="submit">Book an Experience Session</button></div></form></div>')

def cta_band(page, eyebrow="Get started", title="Your first session starts with one step.",
             body="Talk to our Movement Coach for a baseline assessment of your strength, mobility, coordination and movement patterns, to tailor the right programme for you. All ages and fitness levels welcome"):
    msg = page.get("wa", DEFAULT_WA)
    return (f'<section class="cta-band bg-cobalt" id="book" data-placement="cta-band"><div class="wrap cta-grid">'
            f'<div class="cta-copy"><p class="eyebrow">{eyebrow}</p><h2 class="h2">{title}</h2><p class="lead">{body}</p>'
            f'<p class="small">We\'ll reply on WhatsApp or call within 24 hours.</p></div>'
            f'<div class="cta-form"><div class="formcard">{zoho_box(page.get("programme", ""), page.get("studio", ""))}</div>'
            f'<div class="row">{wa_btn(msg, "cta-band", cls="btn btn-ivory")}<a class="tert" href="{TEL}" data-cta="cta-band">{icon("phone", 18)}Call {PHONE}</a></div></div>'
            f'</div></section>')

# ---------------------------------------------------------------- studio card
def studio_card(s, heading_level=3, show_page=True):
    pg = arrow("Studio page", s["path"]) if show_page else ""
    return (f'<article class="card studio"><div class="ph r-167 map">{icon("pin", 26, "#2A2F38", 1.4)}<span class="ph-k">Map</span>'
            f'<a class="btn btn-secondary btn-sm map-btn" href="https://www.google.com/maps/search/?api=1&amp;query={urllib.parse.quote(s["map_q"])}" data-map="{h(s["map_q"])}" data-title="Map of {s["label"]}">Show map</a></div>'
            f'<div class="studio-body"><h{heading_level} class="h3">{s["label"]}</h{heading_level}>'
            f'<p class="body">{h(s["address"])}</p>'
            f'<p class="hours">{icon("clock", 20, "#1F4BB8", 1.5)}{HOURS}</p>'
            f'<div class="row" style="gap:4px 24px">{arrow("Directions", "https://www.google.com/maps/search/?api=1&amp;query=" + urllib.parse.quote(s["map_q"]), ext=True)}'
            f'<a class="arrow" href="{TEL}" data-cta="studio-{s["key"]}">Call</a>'
            f'<a class="arrow" href="{h(wa("Hi Vault Movement, I would like to visit the " + s["label"] + "."))}" data-cta="studio-{s["key"]}">WhatsApp</a>{pg}</div></div></article>')

# ---------------------------------------------------------------- levels
def levels_grid():
    rows = [
        (1, "Foundations · for everybody"), (2, "Confidence · for everybody"), (3, "Fluency · for committed movers"),
        (4, "Mainly the coaching path · through Personal Training"), (5, "Mainly the coaching path · open to a few"),
    ]
    lis = ""
    for n, d in rows:
        col = "#F4EFE6" if n == 4 else "#0B1426"
        lis += f'<li class="level lv{n}">{tally(n, col, 64, 2.2)}<div class="stack-sm"><h3 class="h3" style="font-size:20px">{LEVEL_NAMES[n]}</h3><p>{d}</p></div></li>'
    return f'<ol class="levels">{lis}</ol>'

# ---------------------------------------------------------------- page heroes
def crumbs_html(crumbs):
    items = '<li><a href="/">Home</a></li>'
    for label, href in crumbs[:-1]:
        items += f'<li aria-hidden="true">/</li><li><a href="{href}">{label}</a></li>'
    items += f'<li aria-hidden="true">/</li><li aria-current="page">{crumbs[-1][0]}</li>'
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{items}</ol></nav>'

def phero(page, eyebrow, h1, summary, tagline=None, aside=None, ctas=True, extra=""):
    tg = f'<p class="tagline">{tagline}</p>' if tagline else ""
    cta = cta_row(page.get("wa", DEFAULT_WA), "hero") if ctas else ""
    solo = "" if aside else " phero-solo"
    asd = f'<div class="phero-aside">{aside}</div>' if aside else ""
    return (f'<section class="phero{solo}"><div class="wrap">{crumbs_html(page["crumbs"])}'
            f'<div class="phero-grid"><div class="phero-copy"><p class="eyebrow">{eyebrow}</p><h1 class="h1 h1-sm">{h1}</h1>{tg}'
            f'<p class="lead">{summary}</p>{cta}{extra}</div>{asd}</div></div></section>')

# ---------------------------------------------------------------- header / footer
NAV_PROG = [("Vault 12", "/programmes/vault-12"), ("Movement &amp; Strength", "/programmes/movement-and-strength"),
            ("Personal Training", "/programmes/personal-training"), ("Vault Kids", "/kids"), ("More from Vault Movement", "/more")]
NAV_STORY = [("Story behind the name", "/story"), ("Founders &amp; journey", "/story/founders"), ("Philosophy", "/#philosophy"), ("Coaches", "/coaches")]

def header(active_path):
    def cur(p):
        return ' aria-current="page"' if p == active_path else ""
    prog_active = any(active_path == p or active_path.startswith(p + "/") for _, p in NAV_PROG)
    story_active = any(active_path == p for _, p in NAV_STORY)
    def dd(label, items, act):
        links = "".join(f'<a href="{p}"{cur(p)}>{l}</a>' for l, p in items)
        st = ' style="color:#1F4BB8"' if act else ""
        return (f'<div class="dd"><button class="nav-a" type="button" aria-expanded="false" aria-haspopup="true"{st}>{label} {icon("chev", 16)}</button>'
                f'<div class="dd-menu">{links}</div></div>')
    nav = (dd("Programmes", NAV_PROG, prog_active) + f'<a class="nav-a" href="/journey"{cur("/journey")}>Your Journey</a>'
           + '<a class="nav-a" href="/#vault-method">The Vault Method</a>' + dd("Our Story", NAV_STORY, story_active)
           + f'<a class="nav-a" href="/locations"{cur("/locations")}>Locations</a>')
    mob = ('<p class="mnav-h">Programmes</p><div class="mnav-sub">' + "".join(f'<a href="{p}">{l}</a>' for l, p in NAV_PROG) + '</div>'
           + '<a href="/journey">Your Journey</a><a href="/#vault-method">The Vault Method</a>'
           + '<p class="mnav-h">Our Story</p><div class="mnav-sub">' + "".join(f'<a href="{p}">{l}</a>' for l, p in NAV_STORY) + '</div>'
           + f'<a href="/locations">Locations</a><a href="{APP}">{icon("user", 18, "#1F4BB8", 1.5)}&nbsp;Member login</a>'
           + book("mobile-menu", cls="btn btn-primary"))
    return (f'<div class="topstrip"><div class="wrap-wide topstrip-in"><p>Vault Movement <span class="dot" aria-hidden="true">·</span> formerly Chennai Parkour</p>'
            f'<p class="topstrip-r hide-sm"><span>Both studios open every day, 6:00 AM – 9:00 PM</span><a href="{TEL}" data-cta="topstrip">{PHONE}</a></p></div></div>'
            f'<header class="hdr"><div class="wrap-wide hdr-in">'
            f'<a class="logo" href="/" aria-label="Vault Movement home"><img src="/assets/brand/lockup.webp" alt="Vault Movement — Fitness &amp; Lifestyle Studio" width="560" height="102"><span class="tm" aria-hidden="true">™</span></a>'
            f'<nav class="nav" aria-label="Main">{nav}</nav>'
            f'<div class="hdr-actions"><a class="nav-a login" href="{APP}">{icon("user", 18, "#1F4BB8", 1.5)}<span class="login-t">Member login</span></a>'
            f'{book("header", cls="btn btn-primary hdr-cta")}'
            f'<details class="mnav"><summary aria-label="Menu" aria-expanded="false">{icon("menu", 20, cls="ico i-menu")}{icon("close", 20, cls="ico i-close")}<span>Menu</span></summary>'
            f'<nav class="mnav-panel" aria-label="Mobile">{mob}</nav></details></div></div></header>')

def footer():
    col = lambda title, links: (f'<nav class="foot-col" aria-label="{title}"><p class="foot-h">{title}</p>' + "".join(f'<a href="{p}">{l}</a>' for l, p in links) + "</nav>")
    studios = '<div class="foot-col"><p class="foot-h">Studios</p>' + "".join(f'<a href="{s["path"]}">{s["label"]}</a>' for s in STUDIOS) + \
              f'<p class="small" style="margin:6px 0 8px">{HOURS}</p><a href="{TEL}" data-cta="footer">Call {PHONE}</a><a href="{h(wa())}" data-cta="footer">WhatsApp us</a></div>'
    connect = '<div class="foot-col"><p class="foot-h">Connect</p>' + "".join(f'<a href="{u}" target="_blank" rel="noopener">{l}</a>' for l, u in SOCIAL) + \
              f'<a href="{APP}">Member login</a><a href="/franchise">Franchise</a></div>'
    return ('<footer class="foot"><div class="wrap"><div class="foot-cols">'
            '<div class="foot-brand"><img src="/assets/brand/crest.webp" alt="Vault Movement shield crest — Movement for Everybody, established 2008" width="440" height="548" loading="lazy">'
            '<p class="h4">Movement for Everybody</p><p class="small">Vault Movement · formerly Chennai Parkour</p></div>'
            + col("Programmes", NAV_PROG)
            + col("Explore", [("Your Journey", "/journey"), ("Experience Session", "/experience-session"), ("The Vault Method", "/vault-method"), ("Our Story", "/story"), ("Philosophy", "/philosophy"), ("Coaches", "/coaches"), ("Stories", "/stories"), ("FAQ", "/faq")])
            + studios + connect +
            '</div><div class="foot-base"><p>© 2026 Vault Movement Pvt Ltd. All rights reserved. · Vault Movement™</p>'
            '<nav aria-label="Legal"><a href="/privacy">Privacy</a><a href="/terms">Terms</a><button class="linkbtn" type="button" data-open-consent="1">Cookie settings</button></nav></div></div></footer>')

def mbar(page):
    return (f'<nav class="mbar" aria-label="Quick actions">{wa_btn(page.get("wa", DEFAULT_WA), "sticky", "WhatsApp", "btn btn-secondary", False)}'
            f'<a class="btn btn-secondary" href="{TEL}" data-cta="sticky">Call</a>{book("sticky", "Book", "btn btn-primary")}</nav>')

def consent_banner():
    return ('<div class="consent" role="dialog" aria-label="Cookie consent" aria-live="polite">'
            '<p class="small">We use analytics and advertising cookies only with your consent. Essential cookies keep the site working. <a href="/privacy">Privacy Policy</a></p>'
            '<div class="row"><button class="btn btn-primary btn-sm" type="button" data-consent="all">Accept all</button>'
            '<button class="btn btn-ivory btn-sm" type="button" data-consent="essential">Essential only</button></div></div>')

# ---------------------------------------------------------------- JSON-LD
FOUNDERS = ["Vignesh Raghavan", "Vishwa Dayakaran", "Vishal Kumar"]
ORG_ID = SITE + "/#organization"

def org_ld():
    return {
        "@type": "Organization", "@id": ORG_ID, "name": "Vault Movement", "legalName": "Vault Movement Pvt Ltd",
        "alternateName": "Chennai Parkour", "foundingDate": "2008", "url": SITE + "/",
        "logo": SITE + "/assets/brand/crest.png", "image": SITE + "/assets/og/og-default.png",
        "slogan": "Movement for Everybody", "telephone": "+91-99626-96859",
        "description": "Vault Movement, formerly Chennai Parkour, is a Fitness & Lifestyle Studio in Chennai, established in 2008. Coach-led strength, movement and lifestyle programmes for adults and kids.",
        "founder": [{"@type": "Person", "name": n} for n in FOUNDERS],
        "sameAs": [u for _, u in SOCIAL],
        "areaServed": {"@type": "City", "name": "Chennai"},
    }

def studio_ld(s):
    return {
        "@type": "HealthClub", "@id": SITE + s["path"] + "#studio", "name": "Vault Movement — " + s["label"],
        "url": SITE + s["path"], "telephone": "+91-99626-96859", "image": SITE + "/assets/og/og-default.png",
        "parentOrganization": {"@id": ORG_ID},
        "address": {"@type": "PostalAddress", "streetAddress": s["street"], "addressLocality": "Chennai",
                    "addressRegion": "Tamil Nadu", "postalCode": s["postal"], "addressCountry": "IN"},
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                       "opens": "06:00", "closes": "21:00"}],
    }

def service_ld(page, name, desc, stype="Fitness programme"):
    return {"@type": "Service", "@id": SITE + page["path"] + "#service", "name": name, "serviceType": stype,
            "description": desc, "provider": {"@id": ORG_ID}, "areaServed": {"@type": "City", "name": "Chennai"},
            "url": SITE + page["path"]}

def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()

def page_ld(page):
    graph = []
    if page["path"] == "/":
        graph.append(org_ld())
        graph.append({"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Vault Movement", "publisher": {"@id": ORG_ID}, "inLanguage": "en-IN"})
        graph += [studio_ld(s) for s in STUDIOS]
    else:
        graph.append({"@type": "Organization", "@id": ORG_ID, "name": "Vault Movement", "url": SITE + "/"})
    if page.get("crumbs"):
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
        for i, (label, href) in enumerate(page["crumbs"], 2):
            items.append({"@type": "ListItem", "position": i, "name": strip_tags(label), "item": SITE + (href if href != "#" else page["path"])})
        items[-1]["item"] = SITE + page["path"]
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    graph += page.get("ld", [])
    if CUR["faqs"] and not page.get("no_faq_ld"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(" ".join(a) if isinstance(a, list) else a)}}
            for q, a in CUR["faqs"]]})
    return {"@context": "https://schema.org", "@graph": graph}

# ---------------------------------------------------------------- page shell
FONTS = "https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Inter:wght@400;500;600&family=Cormorant+Garamond:ital,wght@1,500;1,600&display=swap"
FONTS_KIDS = "https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Inter:wght@400;500;600&family=Cormorant+Garamond:ital,wght@1,500;1,600&family=Caveat+Brush&display=swap"

def shell(page, body):
    url = SITE + (page["path"] if page["path"] != "/" else "/")
    robots = "noindex,follow" if page.get("noindex") else "index,follow,max-image-preview:large"
    fonts = FONTS_KIDS if page.get("kids") else FONTS
    ld = json.dumps(page_ld(page), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    canon = f'<link rel="canonical" href="{url}">' if not page.get("noindex") else ""
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{h(page["title"])}</title>
<meta name="description" content="{h(page["desc"])}">
<meta name="robots" content="{robots}">
{canon}
<meta name="theme-color" content="#F4EFE6">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Vault Movement">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{h(page["title"])}">
<meta property="og:description" content="{h(page["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Vault Movement — Movement for Everybody">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{h(page["title"])}">
<meta name="twitter:description" content="{h(page["desc"])}">
<meta name="twitter:image" content="{SITE}/assets/og/og-default.png">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{h(fonts)}">
<link rel="stylesheet" href="/assets/css/site.css">
<link rel="preload" as="image" href="/assets/brand/lockup.webp" type="image/webp">
<script defer src="/assets/js/site.js"></script>
<script type="application/ld+json">{ld}</script>
</head>
<body data-page="{page.get("slug", "page")}">
<div class="site{" kids" if page.get("kids") else ""}">
<a class="btn btn-primary skip" href="#main">Skip to content</a>
{header(page["path"])}
<main id="main">
{body}
</main>
{footer()}
{mbar(page)}
{consent_banner()}
</div>
</body>
</html>
'''

# ---------------------------------------------------------------- dc (design canvas) output
DC_LINKS = {"/": "Main.dc.html", "/journey": "Journey.dc.html", "/programmes/vault-12": "Vault12.dc.html", "/kids": "Kids.dc.html",
            "/programmes/movement-and-strength": "MS.dc.html", "/programmes/personal-training": "PT.dc.html", "/more": "More.dc.html",
            "/story": "Story.dc.html", "/story/founders": "Founders.dc.html", "/coaches": "Coaches.dc.html", "/locations": "Locations.dc.html",
            "/vault-method": "Main.dc.html#vault-method", "/philosophy": "Main.dc.html#philosophy"}

def dc_shell(page, body, css, blobs, h_px):
    inner = f'''<div class="site{" kids" if page.get("kids") else ""}">
{header(page["path"])}
<main id="main">
{body}
</main>
{footer()}
{mbar(page)}
</div>'''
    def relink(m):
        href = m.group(1)
        base, _, frag = href.partition("#")
        base = base or "/"
        if base in DC_LINKS:
            if frag:
                return f'href="#{frag}"' if base == page["path"] else f'href="{DC_LINKS[base]}#{frag}"'
            return f'href="{DC_LINKS[base]}"'
        return 'href="#"'
    inner = re.sub(r'href="(/[^"]*)"', relink, inner)
    for k, v in blobs.items():
        inner = inner.replace(k, v)
    fonts = (FONTS_KIDS if page.get("kids") else FONTS).replace("&", "&amp;")
    # self-close fix for dc parser: expand <x .../> in svg into explicit closing tags
    inner = re.sub(r"<(line|path|rect|circle)([^<>]*?)/>", r"<\1\2></\1>", inner)
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<title>{h(page["title"])}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="{fonts}" rel="stylesheet">
<style>
{css}
</style>
</helmet>
{inner}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":{h_px}}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{}};
  }}
}}
</script>
</body>
</html>
'''
