"""Home, Journey, Experience Session, core programmes and Vault Kids pages."""
from lib import *

PAGES = []
def page(**meta):
    def deco(fn):
        PAGES.append((meta, fn)); return fn
    return deco

# ================================================================ HOME
@page(path="/", file="index.html", slug="home", dc=("Main.dc.html", 9700),
      title="Vault Movement — Fitness & Lifestyle Studio, Chennai",
      desc="Vault Movement, formerly Chennai Parkour, is a Fitness & Lifestyle Studio in Chennai since 2008. Coach-led programmes for adults and kids.",
      crumbs=None, wa=DEFAULT_WA)
def home(p):
    seq = ('<div class="seq" aria-hidden="true">'
           '<p class="seq-l"><span class="w w1">Your</span> <span class="w w2">first</span> <span class="w w3">move!</span></p>'
           '<p class="seq-l"><span class="w w4">Your</span> <span class="w w5">transformation</span> <span class="w w6">begins!</span></p>'
           '<p class="seq-l seq-l3"><span class="seq-word">'
           '<span class="w w7"><span class="mp mV">V</span><span class="mp m-in mW">W</span><span class="mp m-in mE1">e</span><span class="mp m-in mE2">e</span><span class="mp mAult">ault</span></span>'
           '<span class="mp"> </span>'
           '<span class="w w8"><span class="mp">Mo</span><span class="mp m-in mU">u</span><span class="mp">ve</span><span class="mp mMent">ment</span><span class="mp m-in mBang">!</span></span>'
           '<span class="seq-ul"></span></span></p></div>'
           '<p class="sr-only">Your first move! Your transformation begins! Vault Movement — We Move!</p>')
    hero = f'''<section class="hero"><div class="wrap">
<div class="hero-grid">
<div class="hero-copy">
<p class="eyebrow">Fitness &amp; Lifestyle Studio · Since 2008</p>
<h1 class="h1 hero-h1">Movement for <u>Everybody</u></h1>
<p class="lead" style="max-width:600px">Vault Movement is a Fitness &amp; Lifestyle Studio. Coach-led strength, movement and lifestyle programmes for adults and kids, since 2008.</p>
{cta_row(DEFAULT_WA, "hero")}
<p class="small">Formerly Chennai Parkour.</p>
</div>
<div class="hero-mark">
{vring("hv", animate=True, cls="vring-hero")}
{seq}
{arrow("Why We Move", "/story", "arrow seq-why")}
</div>
</div>
<dl class="facts">
<div><dt>Since 2008</dt><dd>Founded in Chennai as Chennai Parkour</dd></div>
<div><dt>2 studios</dt><dd>City Studio · Ekkattuthangal and Coast Studio · Injambakkam, ECR</dd></div>
<div><dt>Open every day</dt><dd>6:00 AM – 9:00 PM at both studios</dd></div>
<div><dt>Coach-led</dt><dd>Every session, every level</dd></div>
</dl>
</div></section>'''

    paths = [
        ("Build your foundation", "Vault 12", "Best if you're new to fitness", "Twelve coach-led weeks of strength, movement and nutrition habits.", "/programmes/vault-12", "Adult member early in training, coach cueing technique", "Start here"),
        ("Progress with purpose", "Movement &amp; Strength", "Best if you're already active", "Six days a week, sixty-minute sessions, progressing through Vault One, Two and Three.", "/programmes/movement-and-strength", "Adult class on vaults or calisthenics, ground level", "Explore"),
        ("Movement for life", "Personal Training", "Or start here, one-to-one", "PT Trio or PT 1:1, on a Gameplan built around you.", "/programmes/personal-training", "Coach with one member, focused cueing", "Explore"),
    ]
    def path_card(i, label, name, tag, line, href, ph, go, kids=False):
        return (f'<a class="card card-link path-card" href="{href}" data-cta="path-{i}">{photo(ph, ratio="r-43", cls="flat" + (" ph-silk" if kids else ""))}'
                f'<div class="card-body"><p class="label">{label}</p><h3 class="h3">{name}</h3><span class="path-tag">{tag}</span>'
                f'<p class="body" style="font-size:16px">{line}</p><span class="arrow mt-auto">{go} {icon("arrow", 18)}</span></div></a>')
    cards3 = "".join(f'<li>{path_card(i, *pd)}</li>' for i, pd in enumerate(paths))
    chev = '<svg class="prog-chev" width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 1.5l5.5 4.5L3 10.5" fill="none" stroke="#1F4BB8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    prog = f'<div class="prog" aria-hidden="true"><span class="prog-line"><span class="seg"></span>{chev}<span class="seg"></span>{chev}<span class="seg"></span>{chev}</span><span class="prog-label">Your progression</span></div>'
    kids_card = path_card(3, "Born to Play. Built to Move.", "Vault Kids", "For your child", "Toddler, Under 10 and Under 14 batches. Screen-free, joy-first sessions.", "/kids", "Kids class on mats with a coach", "Explore", kids=True)
    transform = sec(f'''<div class="stack-lg">
{head("Your transformation", "From your first move to mastery", "Book an Experience Session. We assess your baseline and match you to the right path.", arrow("See the full journey", "/journey"))}
<div class="stack">
<p class="step-head"><span class="num">01</span>Assess your baseline</p>
<div class="strip"><p class="body"><strong style="color:#0B1426">Experience Session</strong> — a baseline assessment of your strength, mobility, coordination and movement patterns, and a chat with a Movement Coach.</p>{book("transformation-strip")}</div>
</div>
<div class="stack">
<p class="step-head"><span class="num">02</span>Choose your path</p>
<div class="paths">
<div class="paths-main"><p class="sr-only">Your progression: Vault 12, then Movement and Strength, then Personal Training.</p><ol class="paths-cards">{cards3}</ol>{prog}</div>
<div class="paths-kids">{kids_card}</div>
</div></div>
</div>''', "sec sec-top0", id="your-transformation")

    method = sec(f'''<div class="stack-lg">
{head("The Vault Method", "A Vault of Movements, each unlocks one level at a time.", "Our Vault has 750+ movements, built and refined since 2008. Master every move to unlock your next level, on a Gameplan you and your coach have tailored to your goal!", arrow("How the Vault Method works", "/vault-method"))}
{levels_grid()}
<p class="tagline" style="font-size:20px">Built to Move, Built for Life.</p>
</div>''', id="vault-method")

    phil_items = [
        ("01 · Natural Movement", "The body was made to move all day, not for one intense hour.", "24/7 · Not one hour"),
        ("02 · Play", "Play is not a reward. It is essential.", "Joy-first"),
        ("03 · Fear Metabolism", "Most people never learn to move through fear. We teach it.", "One safe step at a time"),
        ("04 · Belonging", "The people who live longest belong somewhere.", "+50% survival odds with strong social bonds"),
        ("05 · Purpose / Ikigai", "People with a reason to get up every morning live longer — and stay capable longer.", "31% lower risk of functional disability"),
    ]
    phil = "".join(f'<li><p class="eyebrow">{l}</p><p class="phil-q">{q}</p><p class="phil-hook">{hk}</p></li>' for l, q, hk in phil_items)
    philosophy = sec(f'<div class="stack-lg">{head("Our philosophy", "Five principles every session is built on.", link=arrow("Read the philosophy and sources", "/philosophy"))}<ol class="phil">{phil}</ol></div>', "sec bg-silk", id="philosophy")

    proof = sec(f'''<div class="stack-lg">
{head("Our heritage", "Eighteen years of coaching Chennai to move.")}
<div class="grid g-300">
<div class="card stat"><p class="stat-n">2008</p><p class="body">Founded in Chennai as Chennai Parkour.</p></div>
<div class="card stat"><p class="stat-n">2</p><p class="body">Studios: City Studio · Ekkattuthangal and Coast Studio · Injambakkam, ECR.</p></div>
<div class="card stat"><p class="stat-n">18+ yrs</p><p class="body">Each, for our three Executive Coaches.</p></div>
</div>
<div class="proof-rows">
<div><p class="kicker">Trusted to train</p><p class="v">TNCF · CISF · NSG · Tamil Nadu Fire &amp; Rescue Services</p></div>
<div><p class="kicker">Movement work for Tamil cinema</p><p class="v">Chekka Chivantha Vaanam · Irumbu Thirai · Kanithan</p></div>
</div></div>''')

    stories = sec(tband(["arun", "santhosh", "vijay", "karthik"]) + ig_cards() + "</div>", "sec bg-ink", attrs=' data-placement="stories"')

    kids = sec(f'''<div class="panel-mist row" style="gap:clamp(28px,4vw,56px)">
<div style="flex:1 1 420px;min-width:0">{photo("Children playing and moving with a coach, mats, ground level", ratio="r-43", cls="ph-silk")}</div>
<div style="flex:1 1 400px;min-width:0" class="stack">
<p class="eyebrow">Vault Kids</p><h2 class="h2">Screen-free, joy-first movement for children.</h2>
<p class="body">Coordination, balance, strength, confidence, focus and real friendships. Toddler, Under 10 and Under 14 batches, with a higher coach-to-child ratio and regular parent updates.</p>
<div class="row"><a class="btn btn-secondary" href="/kids" data-cta="kids-teaser">Explore Vault Kids</a>{wa_btn("Hi Vault Movement, I'd like to book an Experience Session for my child.", "kids-teaser", "WhatsApp about a kids batch", "tert", False)}</div>
</div></div>''')

    locs = sec(f'<div class="stack-lg">{head("Locations", "Where are the studios, and when are they open?", "Two studios. Both are open every day, 6:00 AM – 9:00 PM.", arrow("All locations", "/locations"))}<div class="grid g-460">{"".join(studio_card(s) for s in STUDIOS)}</div></div>', "sec sec-top0")

    faqs = faq_block([
        ("Is Vault Movement the same as Chennai Parkour?", "Yes. Chennai Parkour, founded in Chennai in 2008, is now Vault Movement. Same coaches, same safety-first method — a new name for where we are going."),
        ("Where are your studios, and what are your hours?", "We have two studios in Chennai: City Studio · Ekkattuthangal and Coast Studio · Injambakkam, ECR. Both are open every day, 6:00 AM – 9:00 PM."),
        ("How much does it cost?", "Every journey starts with an Experience Session. We share plans after it, on a call or on WhatsApp."),
        ("I'm new to fitness. How do I begin?", "Book an Experience Session. Your coach assesses your strength, mobility, coordination and movement patterns, and matches you to a programme — for most people new to fitness, that is Vault 12, our 12-week coach-led starter."),
        ("What age can kids start?", "Vault Kids runs Toddler, Under 10 and Under 14 batches. Parents are welcome to join in at Toddler sessions."),
    ])
    return hero + transform + method + philosophy + proof + stories + kids + locs + faqs + cta_band(p)

# ================================================================ JOURNEY
@page(path="/journey", file="journey.html", slug="journey", dc=("Journey.dc.html", 7000),
      title="Your Journey — how training works at Vault Movement",
      desc="Every Vault Movement journey starts with an Experience Session, then levels up through coach-led programmes, verified level by level.",
      crumbs=[("Your Journey", "/journey")], wa=DEFAULT_WA)
def journey(p):
    hero = phero(p, "Your Journey", "From your first move to mastery",
                 "Every Vault Movement journey starts with an Experience Session, where a Movement Coach assesses your baseline and matches you to a programme. From there you level up through coach-led programmes, with your progress verified level by level.")
    nxt = "You and your coach decide together, based on your goal and verified progress — not the calendar."
    def step(n, title, prog, href, what, who, leave, levels=None, extra=""):
        lv = f'<div class="tl-levels"><dt>Levels</dt><dd><span class="lv-row">{levels}</span></dd></div>' if levels else ""
        return (f'<li class="tl-step"><span class="tl-num" aria-hidden="true">{n}</span><article class="card tl-card">'
                f'<div class="stack-sm"><p class="kicker" style="color:#1F4BB8"><span class="sr-only">Step {n}: </span>{prog}</p><h3 class="h2" style="font-size:clamp(26px,2.6vw,34px)">{title}</h3></div>'
                f'<dl class="tl-facts"><div><dt>What happens</dt><dd>{what}</dd></div><div><dt>Who it\'s for</dt><dd>{who}</dd></div>'
                f'<div><dt>You leave with</dt><dd>{leave}</dd></div>{lv}</dl>{extra}'
                f'<p class="tl-next"><strong>Ready for the next step?</strong> {nxt}</p>'
                f'<div class="row">{arrow("About " + prog, href)}</div></article></li>')
    tl = ('<ol class="timeline">'
          + step("01", "Assess your baseline", "Experience Session", "/experience-session",
                 "A baseline assessment of your strength, mobility, coordination and movement patterns; a consultation with a Movement Coach; and a programme match.",
                 "Everyone starting at Vault Movement — adults and kids.",
                 "Clarity on where your body is today, and the right programme for your goal.",
                 extra='<p class="small"><strong>Duration:</strong> 1 hour · <strong>What to bring:</strong> Yourself. Ready to Transform. Comfortable clothes.</p>')
          + step("02", "Build your foundation", "Vault 12", "/programmes/vault-12",
                 "Twelve coach-led weeks on a structured weekly Gameplan, with a nutrition plan from our nutritionist, and a tailored Gameplan with coach attention through every move.",
                 "People new to fitness, getting back to form, or training without progress.",
                 "Habits that last and a foundation of safety-first technique, body awareness and the confidence to move without hesitation.",
                 levels=pill(1))
          + step("03", "Progress with purpose", "Movement &amp; Strength", "/programmes/movement-and-strength",
                 "Six days a week, sixty-minute sessions on two alternating Gameplans, progressing through Vault One to Three.",
                 "Vault 12 graduates and already-active adults.",
                 "Strength and skill that compound, with every level verified by your coach.",
                 levels=pill(1) + pill(2) + pill(3))
          + step("04", "Movement for life", "Personal Training", "/programmes/personal-training",
                 "PT Trio, PT 1:1, LTAD on a personal Gameplan. For a few, the path leads to Vault Four and Five — and to coaching.",
                 "Members with specific goals, who require exclusive or specialised training Gameplans.",
                 "Movement that stops being a phase and becomes how you live.",
                 levels=pill(1) + pill(2) + pill(3) + pill(4) + pill(5))
          + '</ol>')
    sym1 = tally(1, "#0B1426", 34, 2.6, label=False).replace('class="tally"', 'class="tally h-sym"')
    sym5 = tally(5, "#0B1426", 34, 2.4, label=False).replace('class="tally"', 'class="tally h-sym"')
    h2 = "Your First Vault " + sym1 + " to Vault Level Five " + sym5
    timeline = sec(f'<div class="stack-lg">{head("Vault levels", h2)}<p class="sr-only">From Vault One to Vault Five.</p>{tl}</div>', "sec sec-top0")
    sides = sec(f'''<div class="stack-lg">{head("Open Vaults directly", "Access specially curated Gameplans, just for YOU.")}
<div class="grid g-460">
<div class="card card-pad stack"><h3 class="h3">Want one-to-one from day one?</h3><p class="body">Start with Personal Training, right after your Experience Session.</p>{arrow("Personal Training", "/programmes/personal-training")}</div>
<div class="card card-pad stack"><h3 class="h3">Already active?</h3><p class="body">Your baseline may place you straight into Movement &amp; Strength.</p>{arrow("Movement &amp; Strength", "/programmes/movement-and-strength")}</div>
</div></div>''', "sec bg-silk")
    kids = sec(f'''<div class="panel-mist stack-lg">
{head("Kids track", "How does the journey work for children?", "Children start with an Experience Session too. Their coach then places them in the right batch, where they work through Vault One and Two.")}
<ol class="steps4">
<li><p class="num">01</p><h3 class="h3" style="font-size:20px">Experience Session</h3><p class="body" style="font-size:16px">A playful first visit and a batch match.</p></li>
<li><p class="num">02</p><h3 class="h3" style="font-size:20px">Toddlers · Under 10 · Under 14</h3><p class="body" style="font-size:16px">Screen-free, joy-first sessions with a higher coach-to-child ratio.</p></li>
<li><p class="num">03</p><h3 class="h3" style="font-size:20px">Vault One and Two</h3><div class="badges">{pill(1)}{pill(2)}</div></li>
</ol>
<div>{arrow("Explore Vault Kids", "/kids")}</div></div>''', "sec")
    verified = sec(f'''<div class="row" style="align-items:flex-start;gap:32px 64px">
<div style="flex:1 1 380px" class="stack">{head("Verified progress", "How is progress verified?")}</div>
<div style="flex:1.3 1 460px" class="stack"><p class="lead">Your coach unlocks a movement as part of your Gameplan, you train together, you achieve the Level-Up Target, and your coach verifies it live. Every level-up is recorded in the My Vault app, where you see your Gameplan and progress.</p>
<div class="row">{arrow("How the Vault Method works", "/vault-method")}<a class="arrow" href="{APP}">Member login {icon("arrow", 18)}</a></div></div></div>''', "sec sec-top0")
    faqs = faq_block([
        ("How long does each stage take?", "Vault 12 runs for twelve weeks. After that there is no fixed timeline: you and your coach decide when you are ready for the next step, based on your goal and verified progress — not the calendar."),
        ("Can I skip Vault 12?", "Yes, if your baseline shows you are ready. Already-active adults may be placed straight into Movement &amp; Strength after their Experience Session, and Personal Training can start right after it."),
        ("Can I switch paths?", "Yes. Your path follows your goal. Talk to your coach about moving between programmes — for example, from Movement &amp; Strength to Personal Training."),
        ("Is it suitable at my age or fitness level?", "Yes. All ages and fitness levels are welcome. Your Experience Session starts from where your body is today, and every programme is coach-led and safety-first."),
    ], title="Journey questions.")
    return hero + timeline + sides + kids + verified + faqs + cta_band(p)

# ================================================================ EXPERIENCE SESSION
@page(path="/experience-session", file="experience-session.html", slug="experience-session",
      title="Book an Experience Session — Vault Movement",
      desc="Start at Vault Movement with an Experience Session: a baseline assessment, a consultation with a Movement Coach and a programme match.",
      crumbs=[("Experience Session", "/experience-session")], wa=DEFAULT_WA, programme="Experience Session")
def experience(p):
    hero = phero(p, "Every journey starts here", "Experience Session",
                 "An Experience Session is your first visit to Vault Movement: a baseline assessment, a consultation with a Movement Coach and a programme match. It is for adults and kids, at City Studio · Ekkattuthangal and Coast Studio · Injambakkam, ECR.",
                 ctas=False, extra=f'<div class="row"><a class="btn btn-primary" href="#book-form" data-cta="hero">Book now</a>{wa_btn(DEFAULT_WA, "hero")}{call_link("hero")}</div>')
    what = sec(f'<div class="stack-lg">{head("What happens", "What happens in an Experience Session?")}' + numcards([
        ("Baseline assessment", "Your coach looks at your strength, mobility, coordination and movement patterns."),
        ("Consultation with a Movement Coach", "We talk about what you want from your body — your goal, your history and your week."),
        ("Programme match", "You leave with clarity, and the right programme for you."),
    ], "g-300") + "</div>", "sec sec-top0")
    info = sec(f'''<div class="grid g-300">
<div class="card card-pad stack"><p class="eyebrow">Who it's for</p><h3 class="h3">Adults and kids</h3><p class="body">All ages and fitness levels welcome. Parents book for children.</p></div>
<div class="card card-pad stack"><p class="eyebrow">Duration</p><h3 class="h3">1 hour</h3><p class="body">Baseline assessment, coach consultation and programme match.</p></div>
<div class="card card-pad stack"><p class="eyebrow">What to bring</p><h3 class="h3">Yourself.</h3><p class="body">Ready to Transform. Comfortable clothes.</p></div>
<div class="card card-pad stack"><p class="eyebrow">Plans</p><h3 class="h3">Shared after your session</h3><p class="body">Plans are shared after your Experience Session — call or WhatsApp us.</p></div>
</div>''', "sec bg-silk")
    form = sec(f'''<div class="row" style="align-items:flex-start;gap:40px 64px">
<div style="flex:1 1 360px;max-width:460px" class="stack"><p class="eyebrow">Book</p><h2 class="h2">Book your Experience Session.</h2>
<p class="body">Tell us a little about you and we will find a time.</p><p class="body"><strong>We'll reply on WhatsApp or call within 24 hours.</strong></p>
<div class="stack-sm">{wa_btn(DEFAULT_WA, "form-side", cls="arrow", with_icon=False)}<a class="arrow" href="{TEL}" data-cta="form-side">Call {PHONE}</a></div></div>
<div style="flex:1.4 1 480px;min-width:0" class="card" id="book-form">{zoho_box("Experience Session")}</div></div>''', "sec")
    faqs = faq_block([
        ("What level of fitness do I need?", "None. People of all fitness levels are welcome — lean or heavy, short or tall, or feeling weak. We start with the basics, within your comfort zone, and help you build from there."),
        ("Should I lose weight or get stronger before I start?", "Not at all. There are movements for every body type, and your coach builds your programme around where you are today."),
        ("How much does it cost?", "Every journey starts with an Experience Session. We share plans after it, on a call or on WhatsApp."),
        ("Can I book for my child?", "Yes. Kids start with an Experience Session too, and their coach places them in the right batch: Toddlers, Under 10 or Under 14."),
    ], title="Before you book.")
    return hero + what + info + form + faqs

# ================================================================ VAULT 12
@page(path="/programmes/vault-12", file="programmes/vault-12.html", slug="vault-12", dc=("Vault12.dc.html", 6600),
      title="Vault 12 — 12-week coach-led starter programme",
      desc="Vault 12 is a 12-week, coach-led starter programme for basic fitness, sustainable weight loss and strength, with a nutrition plan.",
      crumbs=[("Vault 12", "/programmes/vault-12")], wa="Hi Vault Movement, I'd like to book an Experience Session for Vault 12.", programme="Vault 12")
def vault12(p):
    p["ld"] = [service_ld(p, "Vault 12", "A 12-week, coach-led starter programme for basic fitness, sustainable weight loss and strength gain, with small-group coaching, a structured weekly Gameplan and a nutrition plan.")]
    aside = (photo("Small group of adults of varied ages and body types, coach cueing a squat or hinge, natural warm light", ratio="r-45")
             + '<p class="panel-ink" style="margin-top:16px;font:600 clamp(20px,2vw,24px)/1.3 Poppins,sans-serif">Lose weight, not your favourite food.</p>')
    hero = phero(p, "Stage 2 · Build your foundation", "Vault 12",
                 "Vault 12 is a 12-week, coach-led starter programme at Vault Movement, a Fitness &amp; Lifestyle Studio. It builds basic fitness, sustainable weight loss and strength through small-group coaching, a structured weekly Gameplan and a nutrition plan from our nutritionist. It is built for people new to fitness, getting back to form, or training without progress.",
                 tagline="A 12-week, coach-led starter transformation.", aside=aside)
    facts = facts_band([("Length", "12 weeks"), ("Format", "Small-group coaching"), ("Gameplan", "Monday – Friday"), ("Nutrition", "Plan from our nutritionist"), ("Batch", f"V12 · {confirm('Times')}")])
    who = sec(f'<div class="stack-lg">{head("Who it&#39;s for", "Is Vault 12 right for me?", "If one of these sounds like you, Vault 12 is a good place to start.")}' + checks([
        ("You want sustainable weight loss", None), ("You need accountability", None), ("You're getting back to form", None),
        ("You have an important event coming up", None), ("You already work out but see no progress", None),
        ("Your doctor has advised you to lose weight to protect your knees", "Train with your doctor's clearance."),
    ]) + "</div>")
    incl = sec(f'''<div class="stack-lg">{head("What's included", "What do I get in Vault 12?")}
<div class="row" style="align-items:stretch;gap:20px">
<div style="flex:999 1 560px;min-width:0">{numcards([
        ("Small-group coaching", "Coach-led sessions on a structured weekly Gameplan, with safety-first technique from day one."),
        ("Nutrition consultation and plan", "A consultation and a nutrition plan from our nutritionist."),
        ("Tailored Gameplan and Coach attention", "You get a tailored Gameplan and coach attention during your every move through your transformation journey."),
        ("My Vault app", "Habit tracking and progress, your Gameplan and your nutrition plan in one place."),
    ], "g-260")}</div>
<aside class="panel-mist stack" style="flex:1 1 320px;border-radius:16px;padding:32px" aria-label="Your weekly Gameplan">
<p class="eyebrow">Your weekly Gameplan</p><p class="h3" style="font-size:24px">Six movement patterns, across Monday to Friday.</p>
{chips(["Pull", "Push", "Hinge", "Squat", "Core", "Cardio"], "chips chips-silk")}
<p class="body mt-auto">Your coach builds the Gameplan along with you tailored for your needs and tracks it with you in My Vault.</p></aside></div></div>''', "sec sec-top0")
    lines = "".join(f'<li style="display:flex;align-items:center;gap:24px;padding:26px 0;border-bottom:1px solid #2A2F38">{tally(1, "#F5B700", 34, 2.6, label=False)}<p class="h2" style="font-size:clamp(26px,3.6vw,46px);color:#F4EFE6">{t}</p></li>'
                    for t in ["Lose weight, not your favourite food.", "Build habits that last, not results that disappear.", "Move better, feel lighter, live stronger."])
    band = sec(f'<ul style="list-style:none">{lines}</ul>', "sec bg-ink")
    leads = sec(f'''<div class="stack-lg">{head("Your journey", "What happens after the 12 weeks?", "Vault 12 is stage two. Once your foundation is built, your training evolves with you.")}
<ol class="grid g-300" style="list-style:none">
<li class="card card-pad stack"><p class="num">01</p><p class="kicker">Before · Assess your baseline</p><h3 class="h3">Experience Session</h3><p class="body">Strength, mobility, coordination and movement patterns, with a Movement Coach.</p></li>
<li class="card-pad stack" style="background:#1F4BB8;border-radius:16px;color:#F4EFE6"><p class="num" style="color:#F5B700">02</p><p class="kicker" style="color:#F4EFE6">You are here · Build your foundation</p><h3 class="h3" style="color:#F4EFE6">Vault 12</h3><p style="color:#F4EFE6">Twelve coach-led weeks of strength, movement and nutrition habits.</p></li>
<li class="card card-pad stack"><p class="num">03</p><p class="kicker">Next · Progress with purpose</p><h3 class="h3">Movement &amp; Strength</h3><p class="body">Six days a week, sixty minutes a session, progressing through Vault One, Two and Three, verified by your coach.</p>{arrow("Explore Movement &amp; Strength", "/programmes/movement-and-strength", "arrow mt-auto")}</li>
</ol>
<p class="body">Want one-to-one from day one? <a href="/programmes/personal-training"><strong>Personal Training</strong></a> can start right after your Experience Session.</p></div>''', "sec")
    story_slot = sec(f'''<div class="card card-pad split" style="border-style:dashed;border-color:#2A2F38">
<div class="stack-sm maxw"><p class="ph-k">Testimonial needed</p><p class="serif" style="font-size:26px;line-height:1.35">A real Vault 12 member's words, verbatim, with their consent.</p><p class="small">No before/after photos, no kg or inch figures.</p></div>
{arrow("All member stories", "/stories")}</div>''', "sec sec-top0")
    faqs = faq_block([
        ("What is Vault 12, and how is it different from Movement &amp; Strength?", "Vault 12 is a 12-week, coach-led starter programme: a structured Monday–Friday Gameplan, small-group coaching and a nutrition plan. Movement &amp; Strength comes next — six days a week, sixty-minute sessions on two alternating Gameplans, progressing through Vault One, Two and Three."),
        ("Do I need to be fit to start?", "No. Vault 12 is built for people new to fitness or getting back to form. Your Experience Session sets your baseline first."),
        ("Will I have to give up my favourite food?", "Lose weight, not your favourite food. Vault 12 includes a nutrition consultation and a nutrition plan from our nutritionist, built for sustainable habits."),
        ("My doctor has advised me to lose weight. Can I join?", "Yes, with your doctor's clearance. Share it at your Experience Session so your coach can plan around it."),
        ("How much does Vault 12 cost?", "Every journey starts with an Experience Session. We share plans after it, on a call or on WhatsApp."),
        ("What happens after the 12 weeks?", "The next step is Movement &amp; Strength, where you progress through Vault One, Two and Three, verified by your coach."),
    ], title="Questions about Vault 12.", eyebrow="Vault 12 FAQ")
    return hero + facts + who + incl + band + leads + story_slot + faqs + cta_band(p)

# ================================================================ MOVEMENT & STRENGTH
LEGACY_PARKOUR = ["p01", "p02", "p06", "p07", "p08", "p09", "p12", "p15"]

def hero_two_ctas(p, eyebrow, h1, tagline, summary, aside=None):
    extra = f'<div class="row">{book("hero")}{wa_btn(p.get("wa", DEFAULT_WA), "hero")}</div>'
    return phero(p, eyebrow, h1, summary, tagline=tagline, aside=aside, ctas=False, extra=extra)

def tiles(items):
    cells = "".join(f'<div class="card card-pad stack-sm"><p class="kicker">{k}</p><p class="h3" style="font-size:24px">{v}</p></div>' for k, v in items)
    return f'<div class="grid g-240">{cells}</div>'

@page(path="/programmes/movement-and-strength", file="programmes/movement-and-strength.html", slug="movement-and-strength", dc=("MS.dc.html", 9000),
      title="Movement & Strength Classes in Chennai | Vault Movement",
      desc="Coach-led movement, parkour fundamentals, calisthenics and strength, six days a week. Progress through Vault levels at our Chennai studios.",
      crumbs=[("Movement &amp; Strength", "/programmes/movement-and-strength")], wa="Hi Vault Movement, I'd like to book an Experience Session for Movement & Strength.", programme="Movement & Strength")
def ms(p):
    p["ld"] = [service_ld(p, "Movement & Strength", "Vault Movement's core adult programme in Chennai: parkour fundamentals, calisthenics and strength training in 60-minute coach-led sessions, up to six days a week, progressing through Vault One, Two and Three.")]
    hero = hero_two_ctas(p, "Programme · Progress with purpose", "Movement &amp; Strength",
        "Strength becomes skill. Sixty-minute sessions of movement, calisthenics and strength, coached and verified level by level.",
        "Movement &amp; Strength is Vault Movement's core adult programme in Chennai. It combines parkour fundamentals, calisthenics and strength training in 60-minute coach-led sessions, up to six days a week, at our City Studio (Ekkattuthangal) and Coast Studio (Injambakkam, ECR).",
        aside=photo("Adults training vaults, balance or calisthenics at ground level, coach nearby", ratio="r-45"))
    glance = sec(f'<div class="stack-lg">{head("At a glance", "How does Movement &amp; Strength run?")}' + tiles([
        ("Days", "6 days a week"), ("Sessions", "60-minute sessions"), ("Gameplans", "2 alternating Gameplans"), ("Levels", "Vault One → Vault Three")]) + "</div>", "sec sec-top0")
    train_items = [
        ("balance", "Land, balance, fall safely", "Balance lines and bars, soft landings, floor connectors and break-falls. The foundation everything else is built on."),
        ("jump", "Run and jump", "Running mechanics, jump technique, precision and control. Then: stick the landing."),
        ("vault", "Vault", "Leaping and diving vaults over boxes and rails, linked into flowing combo lines."),
        ("swing", "Swing and climb", "Bar swings, traverses, cat hangs, climb-ups and wall runs. Grip, pull and whole-body control."),
        ("lever", "Calisthenics skills", "Inversions, levers, planche progressions and the muscle-up, unlocked as your strength allows."),
        ("dumbbell", "Strength, conditioning, mobility", "Pull, push, hinge and squat, single-leg work, core and cardio, finished with pike, shoulder, back-bridge and ankle mobility."),
    ]
    cards = "".join(f'<li class="card card-pad stack">{icon(ic, 30, "#1F4BB8", 1.5)}<h3 class="h3">{t}</h3><p class="body">{d}</p></li>' for ic, t, d in train_items)
    train = sec(f'<div class="stack-lg">{head("What you train", "What will I train in Movement &amp; Strength?")}<ul class="grid g-300" style="list-style:none">{cards}</ul><p class="body"><strong style="color:#0B1426">Every movement is progressed from the ground up, on mats, by your coach.</strong></p></div>', "sec bg-silk")
    week = sec(f'''<div class="stack-lg">{head("How a week works", "Two Gameplans, alternating.")}
<div class="grid g-460">
<div class="card card-pad stack"><p class="eyebrow">Gameplan A · Mon, Wed, Fri</p><p class="h4">Focus {confirm()}</p><p class="eg">For example: movement skills — jumps and vaults — plus lower-body strength.</p></div>
<div class="card card-pad stack"><p class="eyebrow">Gameplan B · Tue, Thu, Sat</p><p class="h4">Focus {confirm()}</p><p class="eg">For example: balance and control, calisthenics skills, upper-body strength.</p></div>
</div><p class="body">Two alternating Gameplans mean every part of you gets work, and every part gets recovery.</p></div>''')
    flow_items = ["Warm-up (5 min)", "Movement skills", "Strength and calisthenics", "Core and conditioning", "Mobility cool-down"]
    flow = "".join(f'<li><span class="num">{i+1:02d}</span><p class="h4">{s}</p></li>' for i, s in enumerate(flow_items))
    session = sec(f'<div class="stack-lg">{head("Inside a session", "What happens in a 60-minute session?")}<ol class="flow">{flow}</ol><p class="body">On the day, your coach picks the right variation of every exercise for you, from your Gameplan.</p></div>', "sec sec-top0")
    progress = sec(f'''<div class="row" style="align-items:flex-start;gap:32px 64px">
<div style="flex:1 1 380px" class="stack">{head("How you progress", "Vault One → Vault Two → Vault Three.")}<div class="lv-row">{pill(1)}{pill(2)}{pill(3)}</div></div>
<div style="flex:1.3 1 460px" class="stack"><p class="lead">Our Vault has 750+ movements, built and refined since 2008. Master every move to unlock your next level, on a Gameplan you and your coach have tailored to your goal!</p>
<p class="body">Your coach unlocks each movement, you attempt it, and your coach verifies it live. Progress is recorded in your My Vault app.</p>{arrow("How the Vault Method works", "/vault-method")}</div></div>''', "sec bg-silk")
    who = sec(f'''<div class="grid g-460" style="align-items:start">
<div class="stack">{head("Who it&#39;s for", "Is Movement &amp; Strength right for me?")}
<ul class="checks" style="list-style:none">{"".join(f'<li><span class="check-dot">{icon("check", 18, "#1F4BB8", 1.9)}</span><p class="body" style="padding-top:5px">{x}</p></li>' for x in ["Vault 12 graduates ready for the next step", "Already-active adults — your baseline may place you here directly", "Anyone who wants strength they can use, not just lift"])}</ul>
<p class="small">Minimum age {confirm()}</p></div>
<div class="card card-pad stack"><p class="eyebrow">What you leave with</p><p class="h3" style="font-size:24px;line-height:1.35">Real strength and body control. Confidence moving through space. Better mobility. And a community that trains together.</p></div>
</div>''')
    batches = sec(f'<div class="card card-pad split"><div class="stack-sm"><p class="eyebrow">Batches</p><p class="h3">Morning batches from 6:30 AM</p><p class="body">6:30 · 7:40 · 8:50 {confirm("Per studio")} · Evening batches {confirm()}</p></div>{book("ms-batches")}</div>', "sec sec-top0")
    stories = sec(tband(["arun", "santhosh"], "Members on movement and strength.") + "</div>", "sec bg-ink")
    media = sec(f'''<div class="stack-lg">{head("See it in action", "Sessions and photos from our studios.")}
{reels(["Cllhk5ggTBs", "DZoSDtaJUUw", "DXrGeimh0P3", "DZjjKsuzKhK"])}
{gallery([(f"/assets/parkour/{n}.jpg", "Movement training at Vault Movement") for n in LEGACY_PARKOUR])}</div>''')
    faqs = faq_block([
        ("Do I need to finish Vault 12 first?", "No. If you're already active, your baseline at the Experience Session may place you straight into Movement &amp; Strength."),
        ("Is this parkour?", "Parkour fundamentals — vaults, jumps and safe landings — are a big part of it, trained at ground level on mats, alongside calisthenics and strength."),
        ("Do I have to come six days a week?", f"Six days are available. Your coach will recommend how many suit your goal and recovery. Minimum days {confirm()}"),
        ("How do I level up?", "Your coach verifies each movement live. When every movement in a level is verified, the level is yours, recorded in My Vault."),
        ("I'm over 40. Can I join?", "Yes. Progressions start where your body is today. Our members range from teenagers to people in their 60s."),
    ], title="Movement &amp; Strength questions.")
    return hero + glance + train + week + session + progress + who + batches + stories + media + faqs + cta_band(p)

# ================================================================ PERSONAL TRAINING
@page(path="/programmes/personal-training", file="programmes/personal-training.html", slug="personal-training", dc=("PT.dc.html", 5500),
      title="Personal Training in Chennai: PT Trio & 1:1 | Vault Movement",
      desc="Coach-led personal training in a trio or one-to-one, on a Gameplan built around your goal. City and Coast studios, Chennai, 6 AM–9 PM daily.",
      crumbs=[("Personal Training", "/programmes/personal-training")], wa="Hi Vault Movement, I'd like to book an Experience Session for Personal Training.", programme="Personal Training")
def pt(p):
    p["ld"] = [service_ld(p, "Personal Training", "Personal training in Chennai as PT Trio (one coach, three people) or PT 1:1, starting with a baseline assessment and run on a personal Gameplan tracked in the My Vault app.")]
    hero = hero_two_ctas(p, "Programme · Movement for life", "Personal Training",
        "Your goal. Your Gameplan. Your coach — in a trio or one-to-one.",
        "Vault Movement offers personal training in Chennai in two formats: PT Trio (one coach, three people) and PT 1:1. Both start with a baseline assessment and run on a personal Gameplan tracked in the My Vault app.",
        aside=photo("Coach and one member, focused cueing, natural light", ratio="r-45"))
    two = sec(f'''<div class="stack-lg">{head("Two ways to train", "PT Trio or PT 1:1?")}<div class="grid g-460">
<article class="card card-pad stack"><p class="eyebrow">PT Trio</p><h3 class="h2" style="font-size:clamp(28px,2.6vw,36px)">Train as three.</h3>
<p class="body">One coach, three people, one Gameplan shaped around your shared goal and adjusted for each of you. Personal attention, with the energy of training together.</p>
<p class="bestfor"><strong>Best for:</strong> friends, partners, family or colleagues who want to train together.</p><p class="small">Can we match individuals into a trio? {confirm()}</p></article>
<article class="card card-pad stack"><p class="eyebrow">PT 1:1</p><h3 class="h2" style="font-size:clamp(28px,2.6vw,36px)">All of your coach. All of the session.</h3>
<p class="body">A fully personal Gameplan, at your pace, on your schedule.</p>
<p class="bestfor"><strong>Best for:</strong> a specific goal or deadline · privacy · returning after a break (with your doctor's clearance if recovering from an injury) · mastering a specific skill · training toward Vault Four and coaching.</p></article>
</div></div>''', "sec sec-top0")
    inc_items = ["Baseline assessment and goal-setting", "A personal Gameplan in your My Vault app", "Coach-verified progress and level-ups", "Regular check-ins and goal reviews", f"Nutrition guidance {confirm()}", "Train at either studio, 6 AM – 9 PM, every day"]
    inc = sec(f'''<div class="stack-lg">{head("What's included", "What do both formats include?")}
<ul class="checks grid g-340" style="list-style:none">{"".join(f'<li class="card card-pad"><span class="check-dot">{icon("check", 18, "#1F4BB8", 1.9)}</span><p class="h4" style="padding-top:5px">{x}</p></li>' for x in inc_items)}</ul>
<p class="small">Sessions per week {confirm()}</p></div>''', "sec bg-silk")
    rows = [("Coaching", "Shared between three", "Fully yours"), ("Pace", "Set for the group, adjusted for each", "Set entirely by you"),
            ("Scheduling", "Agreed by the three", "Built around you"), ("Best for", "Training with people you know", "Specific goals, privacy, skills")]
    tr = "".join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    compare = sec(f'<div class="stack-lg">{head("Trio or 1:1?", "How do the two formats compare?")}<div class="tt-wrap"><table class="tt"><thead><tr><th scope="col"><span class="sr-only">Feature</span></th><th scope="col">PT Trio</th><th scope="col">PT 1:1</th></tr></thead><tbody>{tr}</tbody></table></div></div>')
    path = sec(f'''<div class="panel-mist row" style="gap:32px 56px">
<div style="flex:1 1 380px" class="stack"><p class="eyebrow">The path to coaching</p><h2 class="h2">Where Vault Four and Five lead.</h2>
<p class="body">For a few members, Personal Training is where the path leads on to Vault Four and Five, and to coaching. If you'd like to teach one day, tell your coach.</p>{arrow("Movement Coach Certification", "/more/coach-certification")}</div>
<div style="flex:1 1 300px" class="lv-row">{pill(4)}{pill(5)}</div></div>''', "sec sec-top0")
    faqs = faq_block([
        ("Can I start with Personal Training straight away?", "Yes. Book an Experience Session first; your baseline shapes your Gameplan."),
        ("Can I move from Trio to 1:1, or back?", "Yes, any time. Your Gameplan comes with you."),
        ("Do I need two friends for a Trio?", f"{confirm()} To be confirmed."),
        ("Is personal training right for beginners or older adults?", "Yes. Your Gameplan starts exactly where you are."),
        ("Where do sessions happen?", f"At our City Studio (Ekkattuthangal) or Coast Studio (Injambakkam, ECR). Home or on-site sessions {confirm()}"),
    ], title="Personal Training questions.")
    return hero + two + inc + compare + path + faqs + cta_band(p)

# ================================================================ VAULT KIDS
KIDS_WA = "Hi Vault Movement, I'd like to book an Experience Session for my child."
KIDS_CTA = dict(eyebrow="Get started", title="Book your child's Experience Session.",
                body="We only ask for a parent or guardian's details, your child's first name and batch. No date of birth, no photos.")

def kids_hero_art(desc):
    return (f'<div class="kids-hero-art">{photo(desc, ratio="r-43", cls="ph-mist")}'
            f'<figure class="char-badge bob"><img src="/assets/characters/vee-curious.webp" alt="Vee, looking curious" width="270" height="290" loading="lazy">'
            f'<figcaption class="brush" style="font-size:26px">Vee</figcaption></figure></div>')

BUILD = [("Coordination", "Hands, feet and eyes working together."), ("Balance", "Steady on a line, soft and quiet on landing."),
         ("Strength", "Crawling, pushing and bridging with their own bodyweight."), ("Confidence", "Trying something new, one safe step at a time."),
         ("Focus", "Listening, taking turns and finishing a move well."), ("Real friendships", "Moving together and cheering each other on.")]
SAFETY = [("group", "A higher coach-to-child ratio"), ("mat", "Age-appropriate equipment and mats"),
          ("steps", "No child moves to a new skill until the prerequisite is solid"), ("chat", "Regular parent updates")]

def safety_panel():
    lis = "".join(f'<li class="card card-pad stack" style="border:0">{icon(i, 28, "#1F4BB8", 1.5)}<p class="h4">{t}</p></li>' for i, t in SAFETY)
    return sec(f'''<div class="panel-mist row" style="align-items:flex-start;gap:40px 64px">
<div style="flex:1 1 300px;max-width:420px" class="stack"><p class="eyebrow">Safety</p><h2 class="h2">How do you keep children safe?</h2><p class="body">Safety-first coaching is how we have worked since 2008.</p></div>
<ul class="grid g-240" style="flex:999 1 480px;min-width:0;list-style:none">{lis}</ul></div>''', "sec sec-top0")

def build_list():
    lis = "".join(f'<li><span class="num">{i+1:02d}</span><div class="stack-sm"><h3 class="h3">{t}</h3><p class="body" style="font-size:16px">{d}</p></div></li>' for i, (t, d) in enumerate(BUILD))
    return f'<ul class="numlist grid g-340" style="gap:0 40px">{lis}</ul>'

@page(path="/kids", file="kids.html", slug="kids", kids=True, dc=("Kids.dc.html", 7800),
      title="Vault Kids — movement for children in Chennai",
      desc="Vault Kids: screen-free, joy-first movement for children in Toddler, Under 10 and Under 14 batches, with a higher coach-to-child ratio.",
      crumbs=[("Vault Kids", "/kids")], wa=KIDS_WA, programme="Vault Kids")
def kids(p):
    p["ld"] = [service_ld(p, "Vault Kids", "Screen-free, joy-first movement sessions for children in Toddler, Under 10 and Under 14 batches, building coordination, balance, strength, confidence, focus and friendships.", "Children's fitness programme")]
    hero = phero(p, "Toddlers · Under 10 · Under 14", "Vault Kids",
                 "Vault Kids is Vault Movement's programme for children, in Toddler, Under 10 and Under 14 batches. Screen-free, joy-first sessions build coordination, balance, strength, confidence, focus and real friendships.",
                 tagline="Born to Play. Built to Move.", aside=kids_hero_art("Children mid-play with a coach, mats, ground level, warm light"))
    build = sec(f'<div class="stack-lg">{head("What kids build", "What will my child get from Vault Kids?", "Screen-free, joy-first sessions where children move, play and build real physical confidence.")}{build_list()}</div>', "sec bg-silk")
    cohorts = [("TODDLER", "Toddlers", "Parents are welcome to join in.", "/kids/toddlers", "Toddler and parent moving together on mats with a coach"),
               ("U10", "Under 10", "Joy-first sessions for children under 10.", "/kids/under-10", "Under-10 group balancing or crawling with a coach"),
               ("U14", "Under 14", "Skill, strength and confidence for children under 14.", "/kids/under-14", "Under-14 group on a low-box vault or a strength drill")]
    cards = "".join(f'<a class="card card-link" href="{href}">{photo(ph, ratio="r-43", cls="flat ph-mist")}<div class="card-body"><p class="kicker">{code}</p><h3 class="h3">{name}</h3><p class="body" style="font-size:16px">{line}</p><p class="small">Batch times {confirm()}</p><span class="arrow mt-auto">{name} batches {icon("arrow", 18)}</span></div></a>' for code, name, line, href, ph in cohorts)
    batches = sec(f'<div class="stack-lg">{head("Batches", "Which batch is right for my child?", "Your child&#39;s Experience Session confirms the right batch.")}<div class="grid g-300">{cards}</div></div>')
    meet = sec(f'''<div class="stack-lg">{head("Meet the movers", "Say hello to Vee and Mouve.", "Take “ault” from Vault and “ment” from Movement and you are left with V Move. Say it aloud and it becomes Vee &amp; Mouve — and, in the end, We Move.")}
<div class="grid g-460">
<article class="card char-card"><img src="/assets/characters/vee-curious.webp" alt="Vee, a seven-year-old with big wavy hair, looking curious" width="270" height="290" loading="lazy">
<div class="stack-sm" style="flex:1 1 200px"><p class="brush" style="font-size:44px;line-height:1">Vee</p><p class="h4">Age 7 · curious and cheeky</p></div></article>
<article class="card char-card"><img src="/assets/characters/mouve-mischievous.webp" alt="Mouve, an eleven-year-old with a high ponytail and gold scrunchie, pulling a mischievous face" width="260" height="300" loading="lazy">
<div class="stack-sm" style="flex:1 1 200px"><p class="brush" style="font-size:44px;line-height:1">Mouve</p><p class="h4">Age 11 · confident and mischievous</p></div></article>
</div></div>''', "sec sec-top0")
    moves = ["Line balance", "Soft, quiet landing", "Dismount", "Side roll on a mat", "Bear crawl", "Crab crawl", "Safety vault on a low box", "Broad jump and stick the landing", "Shoulder, neck and hamstring stretches", "Wall push-up", "Glute bridge", "Light-band strength"]
    learn = sec(f'''<div class="row" style="gap:48px 64px">
<figure style="flex:1 1 320px;max-width:420px;margin:0" class="stack-sm"><img src="/assets/characters/vee-land.webp" alt="Vee landing softly in a low crouch, hands touching the floor" width="340" height="322" loading="lazy" style="width:100%;max-width:380px;margin:0 auto">
<figcaption class="brush" style="font-size:30px;text-align:center;transform:rotate(-3deg)">Soft and quiet!</figcaption></figure>
<div style="flex:999 1 520px;min-width:0" class="stack"><p class="eyebrow">Learn with Vee &amp; Mouve</p><h2 class="h2">Vault One moves, explained for kids.</h2>
<p class="body">Each move comes in three simple steps, one funny mistake to avoid, and a “Coach says” safety line. Ground-safe moves are marked Try at home.</p>
{chips(moves)}<div>{arrow("Start learning with Vee &amp; Mouve", "/kids/learn-with-vee-and-mouve")}</div></div></div>''', "sec bg-silk")
    action = sec(f'<div class="stack-lg">{head("See it in action", "Kids sessions, from our Instagram.", "Reels load only when you tap, so the page stays fast.")}{reels(["DZKZD8KzQRH", "DXJnV-jkjQj", "DZ4whF5SJyW"])}</div>')
    more = sec(f'''<div class="grid g-460">
<a class="card card-pad card-link stack" href="/more/birthdays-and-events"><p class="eyebrow">Birthdays &amp; Events</p><h3 class="h3" style="font-size:26px">Movement birthday parties</h3><p class="body">Children jump, climb, vault and play under the guidance of our coaches, in a safe, structured environment.</p><span class="arrow mt-auto">Plan a party {icon("arrow", 18)}</span></a>
<a class="card card-pad card-link stack" href="/more/adaptive-movement"><p class="eyebrow">Adaptive Movement</p><h3 class="h3" style="font-size:26px">For neurodivergent children</h3><p class="body">For autistic children, children with ADHD and children with additional needs. Small groups or 1:1, patient coaching and close parent collaboration. It complements your child's therapy, never replaces it.</p><span class="arrow mt-auto">Learn about Adaptive Movement {icon("arrow", 18)}</span></a>
</div>''', "sec sec-top0")
    faqs = faq_block([
        ("What age can kids start?", "Vault Kids runs Toddler, Under 10 and Under 14 batches. Parents are welcome to join in at Toddler sessions."),
        ("How do you keep children safe?", "A higher coach-to-child ratio, age-appropriate equipment and mats, and regular parent updates. No child moves to a new skill until the prerequisite is solid."),
        ("Do you work with neurodivergent children?", "Yes. Adaptive Movement is for autistic children, children with ADHD and children with additional needs, in small groups or 1:1, with close parent collaboration. It complements your child's therapy, never replaces it."),
        ("Do you host birthday parties?", "Yes. Birthdays &amp; Events are movement parties where children play under the guidance of our coaches."),
        ("How much does it cost?", "Every journey starts with an Experience Session. We share plans after it, on a call or on WhatsApp."),
        ("What should my child wear and bring?", "To be confirmed."),
    ], title="Vault Kids questions.", eyebrow="Parents ask")
    return hero + build + batches + safety_panel() + meet + learn + action + more + faqs + cta_band(p, **KIDS_CTA)

def cohort_page(p, name, code, line, extra_faq):
    p["ld"] = [service_ld(p, f"Vault Kids — {name}", f"Vault Kids {name} batch: screen-free, joy-first movement sessions for children.", "Children's fitness programme")]
    hero = phero(p, f"Vault Kids · {code}", name, line, tagline="Born to Play. Built to Move.", aside=kids_hero_art(f"{name} batch with a coach, mats, ground level"))
    times = sec(f'''<div class="stack-lg">{head("Batch times", f"When are the {name} batches?")}
<div class="tt-wrap"><table class="tt"><thead><tr><th scope="col">Studio</th><th scope="col">Batch</th><th scope="col">Days and times</th></tr></thead><tbody>
{"".join(f'<tr><td>{s["label"]}</td><td>{code}</td><td>{confirm()}</td></tr>' for s in STUDIOS)}</tbody></table></div></div>''', "sec sec-top0")
    build = sec(f'<div class="stack-lg">{head("What kids build", "What does my child work on?")}{build_list()}</div>', "sec bg-silk")
    learn = sec(f'<div class="card card-pad split"><div class="stack-sm maxw"><p class="brush" style="font-size:30px">Learn with Vee &amp; Mouve</p><p class="body">Vault One moves in three simple steps, with a “Coach says” safety line.</p></div>{arrow("Start learning", "/kids/learn-with-vee-and-mouve")}</div>', "sec sec-top0")
    faqs = faq_block(extra_faq + [
        ("How do you keep children safe?", "A higher coach-to-child ratio, age-appropriate equipment and mats, and regular parent updates. No child moves to a new skill until the prerequisite is solid."),
        ("How much does it cost?", "Every journey starts with an Experience Session. We share plans after it, on a call or on WhatsApp."),
    ], title=f"{name} questions.", eyebrow="Parents ask")
    return hero + times + build + safety_panel() + learn + faqs + cta_band(p, **KIDS_CTA)

@page(path="/kids/toddlers", file="kids/toddlers.html", slug="kids-toddlers", kids=True,
      title="Toddlers — Vault Kids | Vault Movement",
      desc="Vault Kids Toddler batches: playful, coach-led movement for the youngest children. Parents are welcome to join in.",
      crumbs=[("Vault Kids", "/kids"), ("Toddlers", "/kids/toddlers")], wa="Hi Vault Movement, I'd like to book an Experience Session for my toddler.", programme="Vault Kids — Toddlers")
def toddlers(p):
    return cohort_page(p, "Toddlers", "Toddler", "Toddler batches are Vault Kids' first step: playful, coach-led movement for the youngest children. Parents are welcome to join in.",
                       [("Can parents join in?", "Yes. Parents are welcome to join in at Toddler sessions."), ("What age is the Toddler batch for?", "Your child's Experience Session confirms the right batch.")])

@page(path="/kids/under-10", file="kids/under-10.html", slug="kids-under-10", kids=True,
      title="Under 10 — Vault Kids | Vault Movement",
      desc="Vault Kids Under 10: screen-free, joy-first movement building coordination, balance, strength, confidence, focus and friendships.",
      crumbs=[("Vault Kids", "/kids"), ("Under 10", "/kids/under-10")], wa="Hi Vault Movement, I'd like to book an Experience Session for my child (Under 10).", programme="Vault Kids — Under 10")
def u10(p):
    return cohort_page(p, "Under 10", "U10", "Under 10 batches are screen-free, joy-first sessions for children under ten, building coordination, balance, strength, confidence, focus and real friendships.",
                       [("Which Vault levels do kids work on?", "Kids work through Vault One and Two, each movement verified by their coach.")])

@page(path="/kids/under-14", file="kids/under-14.html", slug="kids-under-14", kids=True,
      title="Under 14 — Vault Kids | Vault Movement",
      desc="Vault Kids Under 14: coach-led movement building skill, strength, confidence and focus, with a higher coach-to-child ratio.",
      crumbs=[("Vault Kids", "/kids"), ("Under 14", "/kids/under-14")], wa="Hi Vault Movement, I'd like to book an Experience Session for my child (Under 14).", programme="Vault Kids — Under 14")
def u14(p):
    return cohort_page(p, "Under 14", "U14", "Under 14 batches are coach-led sessions for children under fourteen, building skill, strength, confidence and focus — with a higher coach-to-child ratio and regular parent updates.",
                       [("Which Vault levels do kids work on?", "Kids work through Vault One and Two, each movement verified by their coach.")])

# ================================================================ LEARN WITH VEE & MOUVE
MOVES = [
    ("Line balance", True, "Vee",
     ["Stand on a straight line on the floor, one foot in front of the other.", "Bend your knees a little and stretch your arms out wide.", "Walk slowly along the line, eyes looking ahead, not at your feet."],
     "Vee stares at his toes and wobbles off the line like a jelly.", "Practise on a line on the floor. Raised edges are for the studio, with a coach."),
    ("Soft, quiet landing", True, "Mouve",
     ["Stand tall and do a small jump on the spot.", "Land on the balls of your feet, knees bending softly.", "Land so quietly nobody hears you — like a cat."],
     "Mouve lands flat-footed — THUD! The whole room turns around.", "Small jumps on flat ground only. Never jump down from furniture."),
    ("Dismount", False, "Vee",
     ["Start on a low, knee-height box your coach sets up.", "Step off and land on your toes, knees bent, palms on the floor between your feet.", "Stand up and run forwards."],
     "Vee forgets to bend his knees and lands like a stiff robot — clunk!", "Only from a knee-height box in the studio, with your coach watching."),
    ("Side roll on a mat", False, "Mouve",
     ["Kneel on a soft mat and tuck your chin to your chest.", "Lower one shoulder to the mat, keeping your head tucked.", "Roll across your back to the opposite hip and come up to kneeling."],
     "Mouve forgets to tuck her chin and rolls like a wobbly potato.", "Roll from shoulder to opposite hip, never over your head or neck. Mats and a coach only."),
    ("Bear crawl", True, "Vee",
     ["Start on hands and feet, knees just off the floor, back flat like a table.", "Move one hand and the opposite foot forward together.", "Swap sides and keep crawling, slow and steady."],
     "Vee's bottom shoots up into the air like a mountain!", "Keep your back flat and your knees low. Clear a safe space on the floor first."),
    ("Crab crawl", True, "Mouve",
     ["Sit down and place your hands behind you, fingers pointing to your feet.", "Lift your hips off the floor.", "Walk with your hands and feet — forwards, backwards, sideways."],
     "Mouve's bottom keeps sinking until she's sitting down — plop!", "Keep your hips up and move slowly, on a clear floor away from furniture."),
    ("Safety vault on a low box", False, "Vee",
     ["Place both hands on top of a low box.", "Put one foot on the box and swing your other leg over the side.", "Land softly on both feet on the other side."],
     "Vee tries it without his hands and gets stuck halfway, like a sock on a washing line.", "Low boxes and padded floors only, with your coach watching."),
    ("Broad jump and stick the landing", True, "Mouve",
     ["Stand with feet hip-width apart and swing your arms back.", "Swing your arms forward and jump as far as you can.", "Land softly on both feet and freeze — stick it!"],
     "Mouve jumps far… then keeps stumbling forward three extra steps.", "Jump on flat, non-slippery ground with plenty of space. Land with soft knees."),
    ("Shoulder, neck and hamstring stretches", True, "Vee",
     ["Shoulders: hug one arm across your chest and hold for five slow breaths.", "Neck: slowly tip one ear towards your shoulder, then switch sides.", "Hamstrings: sit with legs straight and reach gently towards your toes."],
     "Vee tries to touch his toes with big bounces — boing, boing!", "Stretch slowly and gently. No bouncing, and stop if anything hurts."),
    ("Wall push-up", True, "Mouve",
     ["Stand an arm's length from a wall and place your hands flat on it.", "Bend your elbows and bring your chest towards the wall.", "Push back to the start, body straight like a plank."],
     "Mouve bends only at the hips and does a wall bow instead.", "Keep your body straight and your feet still. Use a solid wall, not a door."),
    ("Glute bridge", True, "Vee",
     ["Lie on your back, knees bent, feet flat on the floor.", "Squeeze your bottom and lift your hips up.", "Hold for two seconds, then lower slowly."],
     "Vee lifts so fast he flops back down like a pancake.", "Lift slowly, keep your feet flat and breathe out as you lift."),
    ("Light-band strength", False, "Mouve",
     ["Hold a light band with both hands, arms straight in front of you.", "Pull the band apart slowly, squeezing your shoulder blades together.", "Let it come back slowly — don't let it snap!"],
     "Mouve lets go and the band zings across the room. Oops!", "Light bands only, held away from your face, with your coach."),
]

@page(path="/kids/learn-with-vee-and-mouve", file="kids/learn-with-vee-and-mouve.html", slug="learn", kids=True,
      title="Learn with Vee & Mouve — Vault One moves for kids",
      desc="Vault One moves for kids in three simple steps, with a funny mistake to avoid and a Coach says safety line. Ground-safe moves marked Try at home.",
      crumbs=[("Vault Kids", "/kids"), ("Learn with Vee &amp; Mouve", "/kids/learn-with-vee-and-mouve")], wa=KIDS_WA, programme="Vault Kids")
def learn(p):
    aside = ('<div class="row" style="justify-content:center;gap:16px">'
             '<figure class="card" style="margin:0;padding:8px;width:180px"><img src="/assets/characters/vee-curious.webp" alt="Vee, looking curious" width="270" height="290" style="border-radius:10px"><figcaption class="brush" style="font-size:26px;text-align:center">Vee</figcaption></figure>'
             '<figure class="card" style="margin:0;padding:8px;width:174px"><img src="/assets/characters/mouve-mischievous.webp" alt="Mouve, pulling a mischievous face" width="260" height="300" style="border-radius:10px"><figcaption class="brush" style="font-size:26px;text-align:center">Mouve</figcaption></figure></div>')
    hero = phero(p, "Learn with Vee &amp; Mouve", "Vault One moves, for kids.",
                 "Twelve Vault One moves, each explained in three simple steps — with one funny mistake to avoid and a “Coach says” safety line. Moves marked Try at home are ground-safe; everything else is for the studio, with a coach.",
                 tagline="Born to Play. Built to Move.", aside=aside, ctas=False)
    cards = ""
    for name, home_ok, who, steps, oops, coach in MOVES:
        tag = '<span class="tag-home">Try at home</span>' if home_ok else '<span class="tag-studio">Studio, with a coach</span>'
        st = "".join(f"<li>{s}</li>" for s in steps)
        cards += (f'<article class="card move">{illus(who + " doing: " + name.lower(), "r-43", "ph-mist flat")}<div class="move-body">{tag}<h2 class="h3">{name}</h2>'
                  f'<ol>{st}</ol><p class="oops"><span class="brush">{who}\'s oops!</span>{oops}</p><p class="coach"><strong>Coach says:</strong> {coach}</p></div></article>')
    grid = sec(f'<div class="grid g-340">{cards}</div>', "sec sec-top0")
    note = sec(f'<div class="card card-pad"><p class="body"><strong>For grown-ups:</strong> clear a safe space, stay close, and stop if anything hurts. Every other move is learned at the studio with a coach. Never practise on furniture, walls or anything raised.</p></div>', "sec sec-top0")
    return hero + grid + note + cta_band(p, **KIDS_CTA)
