"""More from Vault Movement, method, story, people, locations, stories, FAQ, franchise, legal and utility pages."""
from lib import *
from pages_core import PAGES, page, LEGACY_PARKOUR

def lists_block(blocks):
    """blocks: list of (eyebrow, title, items)."""
    cols = ""
    for eb, title, items in blocks:
        lis = "".join(f'<li style="display:flex;gap:12px;align-items:flex-start"><span style="margin-top:3px">{icon("check", 18, "#1F4BB8", 1.9)}</span><span class="body">{i}</span></li>' for i in items)
        cols += f'<div class="card card-pad stack"><p class="eyebrow">{eb}</p><h3 class="h3">{title}</h3><ul class="stack-sm" style="list-style:none">{lis}</ul></div>'
    return f'<div class="grid g-300">{cols}</div>'

def more_page(p, eyebrow, h1, summary, blocks, faqs=None, extra="", aside=None, tagline=None, cta=True):
    hero = phero(p, eyebrow, h1, summary, tagline=tagline, aside=aside)
    body = sec(f'<div class="stack-lg">{head("At a glance", "What is it, who is it for, and how does it run?")}{lists_block(blocks)}</div>', "sec sec-top0")
    f = faq_block(faqs, title="Questions.", eyebrow="FAQ") if faqs else ""
    return hero + body + extra + f + (cta_band(p) if cta else "")

# ================================================================ MORE HUB
MORE = [
    ("Adaptive Movement", "/more/adaptive-movement", "For neurodivergent children and children with additional needs. Small groups or 1:1."),
    ("Mind &amp; Movement workshops", "/more/mind-and-movement", "M&amp;M workshops. Details coming soon."),
    ("Bharatanatyam workshops", "/more/bharatanatyam-workshops", "Rhythm, posture, balance and expression."),
    ("Kaladi Kuthuvarisai", "/more/kaladi-kuthuvarisai", "Tamil martial heritage: footwork, rhythm, balance and composure."),
    ("Sports Performance &amp; LTAD", "/more/sports-performance-ltad", "Periodised training for athletes and teams, and long-term athlete development."),
    ("Schools &amp; Colleges", "/more/schools-and-colleges", "Half-day workshops, full-day events and weekly programmes."),
    ("Corporate", "/more/corporate", "Movement challenges for teams, from two hours to full-day retreats."),
    ("Armed Forces &amp; Tactical", "/more/armed-forces-tactical", "Individual, unit-level and pre-selection training."),
    ("Birthdays &amp; Events", "/more/birthdays-and-events", "Movement birthday parties, school outreach and community events."),
    ("Movement Coach Certification", "/more/coach-certification", "From mover to teacher, with senior-coach mentorship."),
    ("Screen Movement", "/more/screen-movement", "Movement preparation for actors and production teams."),
]

@page(path="/more", file="more.html", slug="more", dc=("More.dc.html", 4900),
      title="Workshops & Specialist Programmes | Vault Movement Chennai",
      desc="Adaptive movement, heritage arts, workshops, sports performance, schools, corporate and armed forces training, and coach certification, in Chennai.",
      crumbs=[("More from Vault Movement", "/more")], wa="Hi Vault Movement, I'm not sure which programme fits. Can you help?")
def more_hub(p):
    hero = phero(p, "Workshops &amp; specialist programmes", "More from Vault Movement",
                 "Beyond our core programmes: workshops, heritage arts and specialist training for schools, teams and institutions. Every one built on the same coach-led method.",
                 ctas=False, extra=f'<div class="row"><p class="body"><strong style="color:#0B1426">Not sure which fits?</strong></p>{wa_btn(p["wa"], "more-hero")}</div>')
    def card(tag, title, desc, best, href, ph, src=None, alt=None):
        return (f'<a class="card card-link" href="{href}">{photo(ph, src, "r-169", "flat", alt=alt)}<div class="card-body">'
                f'<p class="eyebrow">{tag}</p><h3 class="h3">{title}</h3><p class="body" style="font-size:16px">{desc}</p>'
                f'<p class="bestfor"><strong>Best for:</strong> {best}</p><span class="arrow mt-auto">Explore {icon("arrow", 18)}</span></div></a>')
    groups = [
        ("For kids and families", [
            card("Adaptive", "Adaptive Movement", "Patient, small-group and 1:1 movement sessions for neurodivergent children and children with additional needs. It complements your child's therapy and never replaces it.", "autistic children, children with ADHD and children with additional needs.", "/more/adaptive-movement", "Coach and child moving together on mats, calm setting"),
            card("Celebrate", "Birthdays &amp; Events", "Movement birthday parties, seasonal events and community festivals: jump, climb, crawl and play.", "kids' birthdays, schools and community groups.", "/more/birthdays-and-events", "Kids movement party", "/assets/schools/s02.jpg", "Kids movement event at Vault Movement"),
        ]),
        ("Heritage, mind and movement", [
            card("Heritage", "Kaladi Kuthuvarisai", "A Tamil martial art rooted in warrior tradition: footwork, rhythm, balance and composure under pressure, taught through direct lineage.", "beginners and movers who want discipline with roots.", "/more/kaladi-kuthuvarisai", "Kaladi Kuthuvarisai training", "/assets/kaladi/k01.jpg", "Kaladi Kuthuvarisai training at Vault Movement"),
            card("Dance", "Bharatanatyam Workshops", f"Classical dance for rhythm, posture, balance and expression. Instructor and format {confirm()}", "movers, dancers and the curious.", "/more/bharatanatyam-workshops", "Bharatanatyam workshop in the studio"),
            card("Workshop", "Mind &amp; Movement (M&amp;M)", f'Description {confirm()} <span class="eg">For example: breath, focus, mobility and playful movement to reset body and mind.</span>', "adults, teams and communities.", "/more/mind-and-movement", "Mind &amp; Movement workshop"),
        ]),
        ("Teams and institutions", [
            card("Schools", "Schools &amp; Colleges", "Age-tailored movement education: half-day workshops, full-day events or ongoing weekly programmes that fit your timetable.", "primary, secondary and college students.", "/more/schools-and-colleges", "School movement programme", "/assets/schools/s05.jpg", "School movement programme at Vault Movement"),
            card("Corporate", "Corporate Programmes", "Structured movement challenges that build trust, communication and cohesion, from two-hour sessions to full-day leadership retreats, for groups of 10 to 200+.", "teams, leadership groups and offsites.", "/more/corporate", "Team movement challenge", "/assets/corporate/c01.jpg", "Corporate team movement programme at Vault Movement"),
            card("Tactical", "Armed Forces &amp; Tactical Fitness", "Functional strength, agility, obstacle navigation and load-bearing movement under service-adapted safety protocols. Trusted by TNCF, CISF, NSG and Tamil Nadu Fire &amp; Rescue Services.", "units, personnel and pre-selection candidates.", "/more/armed-forces-tactical", "Tactical conditioning session", "/assets/armed/a04.jpg", "Tactical fitness training at Vault Movement"),
        ]),
        ("Performance and coaching", [
            card("Performance", "Sports Performance &amp; LTAD", "Periodised, measurable training for athletes and teams, and long-term athlete development for young athletes.", "competitive athletes, sports teams and young athletes.", "/more/sports-performance-ltad", "Athlete sprint or jump drill with a coach"),
            card("Coaching", "Movement Coach Certification", "From mover to teacher: pedagogy, session design, safety and risk assessment, in small cohorts with senior-coach mentorship.", "members with six months of training, or equivalent experience, who want to coach.", "/more/coach-certification", "Coach-in-training leading a session", "/assets/parkour/p14.jpg", "Movement coach training at Vault Movement"),
        ]),
    ]
    body = "".join(f'<div class="stack"><h2 class="group-h">{g}</h2><div class="grid g-300">{"".join(cs)}</div></div>' for g, cs in groups)
    also = f'<p class="body">Also: <a href="/more/screen-movement">Screen Movement</a> — movement preparation for actors and production teams.</p>'
    return hero + sec(f'<div class="stack-lg">{body}{also}</div>', "sec sec-top0") + cta_band(p)

@page(path="/more/adaptive-movement", file="more/adaptive-movement.html", slug="adaptive-movement",
      title="Adaptive Movement — for neurodivergent children",
      desc="Adaptive Movement: coach-led movement for autistic children, children with ADHD and children with additional needs. Small groups or 1:1.",
      crumbs=[("More from Vault Movement", "/more"), ("Adaptive Movement", "/more/adaptive-movement")],
      wa="Hi Vault Movement, I'd like to ask about Adaptive Movement for my child.", programme="Adaptive Movement")
def adaptive(p):
    p["ld"] = [service_ld(p, "Adaptive Movement", "Coach-led movement for neurodivergent children, including autistic children and children with ADHD, and children with additional needs, in small groups or 1:1.", "Children's movement programme")]
    return more_page(p, "More from Vault Movement", "Adaptive Movement",
        "Adaptive Movement is Vault Movement's programme for neurodivergent children — including autistic children and children with ADHD — and for children with additional needs. Sessions run in small groups or 1:1, with patient coaching, predictable routines and close collaboration with parents. It complements your child's therapy, never replaces it.",
        [("Who it's for", "Children who learn differently", ["Autistic children", "Children with ADHD", "Children with additional needs"]),
         ("How we work", "Patient and predictable", ["Patient coaching", f"Predictable routines {confirm()}", "Close parent collaboration", "Complements your child's therapy, never replaces it"]),
         ("Formats", "Small groups or 1:1", ["Small groups", "1:1 sessions", "Starts with an Experience Session"])],
        [("Is Adaptive Movement a therapy?", "No. Adaptive Movement is coach-led movement. It complements your child's therapy, never replaces it."),
         ("Small group or 1:1?", "Both are available. Your child's Experience Session helps us suggest the right fit."),
         ("Can I talk to the coach first?", "Yes. The Experience Session includes a consultation with a Movement Coach, so you can share what works for your child.")],
        aside=photo("Coach and child moving together on mats, calm setting", ratio="r-45"))

@page(path="/more/mind-and-movement", file="more/mind-and-movement.html", slug="mind-and-movement",
      title="Mind & Movement workshops — Vault Movement",
      desc="Mind & Movement (M&M) workshops from Vault Movement. Details coming soon — WhatsApp us to hear about the next workshop.",
      crumbs=[("More from Vault Movement", "/more"), ("Mind &amp; Movement", "/more/mind-and-movement")],
      wa="Hi Vault Movement, I'd like to hear about the next Mind & Movement workshop.", programme="Mind & Movement")
def mm(p):
    hero = phero(p, "Workshops", "Mind &amp; Movement workshops",
                 "Mind &amp; Movement (M&amp;M) workshops are part of Vault Movement's workshop programme. Full details are being finalised — WhatsApp us to hear about the next workshop.")
    body = sec(f'<div class="card card-pad stack maxw"><p class="eyebrow">About the workshops</p><p class="body">Workshop description {confirm()}</p><p class="small">Format, duration and dates to be confirmed.</p></div>', "sec sec-top0")
    return hero + body + cta_band(p)

@page(path="/more/bharatanatyam-workshops", file="more/bharatanatyam-workshops.html", slug="bharatanatyam",
      title="Bharatanatyam workshops — Vault Movement",
      desc="Bharatanatyam workshops at Vault Movement build rhythm, posture, balance and expression. Message us for the next workshop dates.",
      crumbs=[("More from Vault Movement", "/more"), ("Bharatanatyam workshops", "/more/bharatanatyam-workshops")],
      wa="Hi Vault Movement, I'd like to hear about the next Bharatanatyam workshop.", programme="Bharatanatyam workshops")
def bharat(p):
    return more_page(p, "Workshops", "Bharatanatyam workshops",
        "Vault Movement hosts Bharatanatyam workshops that build rhythm, posture, balance and expression.",
        [("What you work on", "Four foundations", ["Rhythm", "Posture", "Balance", "Expression"]),
         ("Instructor", f"To be confirmed", [f"Instructor {confirm()}"]),
         ("Format", "Workshops", [f"Format and duration {confirm()}", "Dates shared on WhatsApp and Instagram"])],
        [("When is the next workshop?", "Dates are shared on WhatsApp and Instagram. Message us to hear about the next one.")],
        aside=photo("Bharatanatyam workshop in the studio", ratio="r-45"))

@page(path="/more/kaladi-kuthuvarisai", file="more/kaladi-kuthuvarisai.html", slug="kaladi",
      title="Kaladi Kuthuvarisai — Tamil martial heritage training",
      desc="Kaladi Kuthuvarisai at Vault Movement: Tamil martial heritage training in footwork, rhythm, balance and composure. Beginners welcome.",
      crumbs=[("More from Vault Movement", "/more"), ("Kaladi Kuthuvarisai", "/more/kaladi-kuthuvarisai")],
      wa="Hi Vault Movement, I'd like to ask about Kaladi Kuthuvarisai.", programme="Kaladi Kuthuvarisai")
def kaladi(p):
    p["ld"] = [service_ld(p, "Kaladi Kuthuvarisai", "Tamil martial heritage training in footwork, body positioning, rhythm, balance, coordination and discipline, taught through direct lineage instruction.", "Martial arts training")]
    extra = (sec(f'<div class="stack-lg">{head("In their words", "What members say.")}<div class="grid g-460">{tcard("karthik", light=True)}</div></div>', "sec bg-silk")
             + sec(f'<div class="stack-lg">{head("See it in action", "Kaladi Kuthuvarisai, from Instagram.")}{reels(["DX4DCuySVK-", "DYPOYwBpu_g", "DY1zygqpph2", "DXtuqH8EeTJ"])}</div>'))
    return more_page(p, "Heritage &amp; discipline", "Kaladi Kuthuvarisai",
        "Kaladi Kuthuvarisai is a Tamil martial heritage practice of footwork, rhythm, balance and composure. At Vault Movement it is taught through direct lineage instruction and disciplined repetition, and beginners are welcome.",
        [("Who it's for", "Beginners welcome", ["Beginners", "Movement practitioners", "Anyone interested in Tamil martial heritage"]),
         ("What you train", "Footwork and rhythm", ["Footwork", "Body positioning", "Spatial awareness", "Rhythmic movement", "Balance and coordination", "Discipline"]),
         ("What it builds", "Composure", ["Composure under pressure", "Proprioceptive awareness", "Coordination", "Patience", "Modern capability rooted in Tamil heritage"])],
        [("Do I need martial arts experience?", "No. Beginners are welcome."), ("How is it taught?", "Through direct lineage instruction and disciplined repetition.")],
        extra=extra, aside=photo("Kaladi Kuthuvarisai training", "/assets/kaladi/k01.jpg", "r-45", alt="Kaladi Kuthuvarisai training at Vault Movement"))

@page(path="/more/sports-performance-ltad", file="more/sports-performance-ltad.html", slug="sports-performance",
      title="Sports Performance & LTAD — Vault Movement",
      desc="Periodised, measurable performance training for athletes and teams, plus long-term athlete development (LTAD) for young athletes.",
      crumbs=[("More from Vault Movement", "/more"), ("Sports Performance &amp; LTAD", "/more/sports-performance-ltad")],
      wa="Hi Vault Movement, I'd like to ask about Sports Performance training.", programme="Sports Performance & LTAD")
def sports(p):
    p["ld"] = [service_ld(p, "Sports Performance & LTAD", "Periodised, measurable performance training for competitive athletes and sports teams, and long-term athlete development for young athletes.", "Athletic performance training")]
    extra = sec(f'''<div class="panel-mist row" style="gap:32px 56px;align-items:flex-start"><div style="flex:1 1 360px" class="stack"><p class="eyebrow">LTAD</p><h2 class="h2">What is long-term athlete development?</h2></div>
<div style="flex:1.3 1 420px" class="stack"><p class="body">Long-term athlete development (LTAD) builds a young athlete's movement, strength and speed in the right order for their stage of development, so performance is built on solid foundations.</p><p class="small">Format and age groups {confirm()}</p></div></div>''', "sec sec-top0")
    return more_page(p, "Performance training", "Sports Performance &amp; LTAD",
        "Sports Performance at Vault Movement is periodised, measurable training for competitive athletes and sports teams: explosive jumps, sprint mechanics, throwing power, agility, endurance and movement control. Our long-term athlete development (LTAD) work builds young athletes' foundations in the right order.",
        [("Who it's for", "Athletes and teams", ["Competitive athletes", "Sports teams", "Team-sport and combat-sport athletes", "Young athletes (LTAD)"]),
         ("What you train", "Speed, power, control", ["Explosive jumps", "Sprint mechanics", "Throwing power", "Agility and endurance", "Movement control"]),
         ("How it runs", "Periodised and measurable", ["Periodised training cycles", "Measurable progress", "For individuals and teams"])],
        [("Will movement training help my sport?", "Yes. Whether it's football, tennis, cricket or badminton, movement training builds agility, mobility and spatial awareness that carry into your sport."),
         ("Do you work with teams?", "Yes. Training cycles are built for individuals and for teams.")],
        extra=extra, aside=photo("Athlete sprint or jump drill with a coach", ratio="r-45"))

@page(path="/more/schools-and-colleges", file="more/schools-and-colleges.html", slug="schools",
      title="Schools & Colleges — movement programmes | Vault Movement",
      desc="Movement programmes for schools and colleges: half-day workshops, full-day events and ongoing weekly programmes that fit school schedules.",
      crumbs=[("More from Vault Movement", "/more"), ("Schools &amp; Colleges", "/more/schools-and-colleges")],
      wa="Hi Vault Movement, I'd like to ask about a programme for our school.", programme="Schools & Colleges")
def schools(p):
    p["ld"] = [service_ld(p, "Schools & Colleges", "Age-tailored movement education for primary schools, secondary schools and colleges, as half-day workshops, full-day events or weekly programmes.", "Physical education programme")]
    imgs = ["s01", "s02", "s03", "s05", "s06", "s04", "s08", "s10"]
    extra = sec(f'<div class="stack-lg">{head("Gallery", "School programmes in action.")}{gallery([(f"/assets/schools/{n}.jpg", "School movement programme at Vault Movement") for n in imgs])}</div>', "sec bg-silk")
    return more_page(p, "Schools &amp; colleges", "Schools &amp; Colleges",
        "Vault Movement runs movement programmes for primary schools, secondary schools and colleges: age-tailored movement education that builds coordination, discipline, teamwork and confidence. Formats range from half-day workshops and full-day events to ongoing weekly programmes that fit school schedules.",
        [("Who it's for", "Students of every age", ["Primary schools", "Secondary schools", "Colleges"]),
         ("What we deliver", "Age-tailored movement", ["Movement fundamentals", "Play and spatial awareness", "Coordination", "Discipline and teamwork", "Physical challenge"]),
         ("Formats", "Fits your schedule", ["Half-day workshops", "Full-day events", "Ongoing weekly programmes"])],
        [("Do you come to our campus?", "Yes. School outreach sessions run on school campuses."),
         ("Which age groups do you work with?", "Primary and secondary school students, and colleges. Every session is tailored to the age group.")],
        extra=extra, aside=photo("School movement programme", "/assets/schools/s05.jpg", "r-45", alt="School movement programme at Vault Movement"))

@page(path="/more/corporate", file="more/corporate.html", slug="corporate",
      title="Corporate programmes — team movement | Vault Movement",
      desc="Structured movement challenges for corporate teams and leadership groups, from two-hour activities to full-day retreats, for 10 to 200+.",
      crumbs=[("More from Vault Movement", "/more"), ("Corporate", "/more/corporate")],
      wa="Hi Vault Movement, I'd like to ask about a corporate programme.", programme="Corporate")
def corporate(p):
    p["ld"] = [service_ld(p, "Corporate programmes", "Structured movement challenges for teams, leadership groups, offsites and retreats, from two-hour activities to full-day leadership retreats, for groups of 10 to 200+.", "Corporate team programme")]
    extra = (sec(f'<div class="stack-lg">{head("In their words", "What teams say.")}<div class="grid g-460">{tcard("vijay", light=True)}</div></div>', "sec bg-silk")
             + sec(f'<div class="stack-lg">{head("Gallery", "Teams on the move.")}{gallery([("/assets/corporate/c01.jpg", "Corporate movement programme at Vault Movement"), ("/assets/parkour/p11.jpg", "Corporate movement programme at Vault Movement"), ("/assets/parkour/p10.jpg", "Corporate movement programme at Vault Movement")])}</div>'))
    return more_page(p, "Corporate", "Corporate programmes",
        "Vault Movement designs structured movement challenges for corporate teams, leadership groups, offsites and retreats, built to strengthen communication, trust and performance under stress. Formats run from two-hour activities to full-day leadership retreats, for groups of 10 to 200+.",
        [("Who it's for", "Teams and leaders", ["Corporate teams", "Leadership groups", "Offsites and retreats"]),
         ("What we deliver", "Movement challenges", ["Structured movement challenges", "Team-building through physical problem-solving", "Trust and communication exercises", "Leadership and cohesion experiences"]),
         ("Formats", "2 hours to a full day", ["Two-hour activities", "Full-day leadership retreats", "Groups of 10 to 200+"])],
        [("How big can the group be?", "From 10 to 200+ people."), ("How long is a programme?", "From a two-hour activity to a full-day leadership retreat.")],
        extra=extra, aside=photo("Team movement challenge", "/assets/corporate/c01.jpg", "r-45", alt="Corporate team movement programme at Vault Movement"))

@page(path="/more/armed-forces-tactical", file="more/armed-forces-tactical.html", slug="armed-forces",
      title="Armed Forces & Tactical training — Vault Movement",
      desc="Functional strength, agility and obstacle training for armed forces and tactical personnel: individual, unit-level and pre-selection.",
      crumbs=[("More from Vault Movement", "/more"), ("Armed Forces &amp; Tactical", "/more/armed-forces-tactical")],
      wa="Hi Vault Movement, I'd like to ask about tactical training.", programme="Armed Forces & Tactical")
def armed(p):
    p["ld"] = [service_ld(p, "Armed Forces & Tactical training", "Functional strength, agility, obstacle navigation, load-bearing movement and high-intensity conditioning for armed forces and tactical personnel.", "Tactical fitness training")]
    extra = sec(f'<div class="stack-lg">{head("Gallery", "Tactical training.")}{gallery([(f"/assets/armed/a0{n}.jpg", "Tactical fitness training at Vault Movement") for n in [4, 5, 3, 6, 2, 1]])}</div>', "sec bg-silk")
    return more_page(p, "Specialised training", "Armed Forces &amp; Tactical",
        "Vault Movement trains armed forces and tactical personnel through individual preparation, unit-level conditioning and pre-selection training, under service-adapted safety protocols. We have been trusted to train TNCF, CISF and NSG personnel and Tamil Nadu Fire &amp; Rescue Services.",
        [("Who it's for", "Personnel and units", ["TNCF, CISF, NSG and Tamil Nadu Fire &amp; Rescue Services", "Individual personnel", "Units", "Pre-selection candidates"]),
         ("What you train", "Operational movement", ["Functional strength", "Agility", "Obstacle navigation", "Load-bearing movement", "Terrain adaptation", "High-intensity conditioning"]),
         ("What it builds", "Capacity under stress", ["Mission-relevant movement capacity", "Performance under physical and psychological stress", "Obstacle adaptability", "Injury-conscious service longevity"])],
        [("Do you train individuals preparing for selection?", "Yes. Pre-selection training is one of our three formats, alongside individual preparation and unit-level conditioning.")],
        extra=extra, aside=photo("Tactical conditioning session", "/assets/armed/a04.jpg", "r-45", alt="Tactical fitness training at Vault Movement"))

@page(path="/more/birthdays-and-events", file="more/birthdays-and-events.html", slug="birthdays",
      title="Kids Birthdays & Events — Vault Movement",
      desc="Screen-free, joy-first movement birthday parties, school outreach and community events, run by Vault Movement coaches.",
      crumbs=[("More from Vault Movement", "/more"), ("Birthdays &amp; Events", "/more/birthdays-and-events")],
      wa="Hi Vault Movement, I'd like to plan a movement birthday party.", programme="Birthdays & Events")
def birthdays(p):
    p["ld"] = [service_ld(p, "Birthdays & Events", "Movement birthday parties, school outreach, seasonal events and community festivals where children jump, climb, vault and play under coach guidance.", "Children's events")]
    extra = (sec(f'<div class="stack-lg">{head("See it in action", "Parties and events, from Instagram.")}{reels(["DZKZD8KzQRH", "DXJnV-jkjQj", "DZ4whF5SJyW"])}</div>', "sec bg-silk")
             + sec(f'<div class="stack-lg">{head("Gallery", "Joy-first, screen-free.")}{gallery([(f"/assets/schools/{n}.jpg", "Kids movement event at Vault Movement") for n in ["s02", "s05", "s06", "s10"]] + [("/assets/parkour/p10.jpg", "Kids movement event at Vault Movement")])}</div>'))
    return more_page(p, "Kids &amp; community", "Birthdays &amp; Events",
        "Vault Movement's Birthdays &amp; Events are screen-free, joy-first movement experiences: birthday parties, school outreach, seasonal events and community festivals. Children jump, climb, vault and play under the guidance of our coaches, in a safe, structured environment.",
        [("What we run", "Parties and events", ["Movement birthday parties", "School outreach", "Seasonal events", "Community festivals"]),
         ("What children build", "Real confidence", ["Physical confidence", "Spatial awareness", "Resilience", "Coordination"]),
         ("How it runs", "Coach-led", ["Guided by our coaches", "Safe, structured environment", f"Venue, group size and timings {confirm()}"])],
        [("How do I book a party?", "WhatsApp or call us with your preferred date and the number of children, and we will share the options.")],
        extra=extra, aside=photo("Kids movement party", "/assets/schools/s02.jpg", "r-45", alt="Kids movement event at Vault Movement"))

@page(path="/more/coach-certification", file="more/coach-certification.html", slug="coach-certification",
      title="Movement Coach Certification — Vault Movement",
      desc="Become a movement coach: pedagogy, session design, safety and risk assessment, in limited cohorts with senior-coach mentorship.",
      crumbs=[("More from Vault Movement", "/more"), ("Movement Coach Certification", "/more/coach-certification")],
      wa="Hi Vault Movement, I'd like to ask about the Movement Coach Certification.", programme="Movement Coach Certification")
def coachcert(p):
    p["ld"] = [service_ld(p, "Movement Coach Certification", "A coaching certification covering movement pedagogy, teaching methodology, movement science, session design, safety, risk assessment and coaching diverse populations.", "Coach education")]
    extra = (sec(f'''<div class="panel-mist row" style="gap:32px 56px"><div style="flex:1 1 380px" class="stack"><p class="eyebrow">The coaching path</p><h2 class="h2">Where Vault Four and Five lead.</h2>
<p class="body">Vault Four and Five are mainly the coaching path. A few members reach them through Personal Training on the way to becoming coaches.</p>{arrow("Personal Training", "/programmes/personal-training")}</div><div class="badges" style="flex:1 1 280px">{pill(4)}{pill(5)}</div></div>''', "sec sec-top0")
             + sec(f'<div class="stack-lg">{head("Gallery", "Coaches in the making.")}{gallery([(f"/assets/parkour/{n}.jpg", "Movement coach training at Vault Movement") for n in ["p14", "p03", "p13", "p10"]])}</div>', "sec bg-silk"))
    return more_page(p, "Coaching &amp; certification", "Movement Coach Certification",
        "The Vault Movement Coach Certification is for practitioners moving from mover to teacher. It covers movement pedagogy, teaching methodology, movement science, progressive session design, safety, risk assessment and coaching diverse populations, in limited cohorts with senior-coach mentorship.",
        [("Entry", "Who can apply", ["At least six months of active training at Vault Movement (formerly Chennai Parkour)", "Or equivalent, demonstrated movement experience"]),
         ("Curriculum", "What you learn", ["Movement pedagogy and teaching methodology", "Movement science fundamentals", "Progressive session design", "Safety protocols and risk assessment", "Coaching diverse populations"]),
         ("Outcome", "Where you can coach", ["Schools", "Gyms", "Corporate settings", "Independently"])],
        [("What are the entry requirements?", "At least six months of active training at Vault Movement (formerly Chennai Parkour), or equivalent demonstrated movement experience."),
         ("How big are the cohorts?", "Cohorts are kept small, with direct mentorship from senior coaches.")],
        extra=extra, aside=photo("Coach-in-training leading a session", "/assets/parkour/p14.jpg", "r-45", alt="Movement coach training at Vault Movement"))

@page(path="/more/screen-movement", file="more/screen-movement.html", slug="screen-movement",
      title="Screen Movement — movement for film | Vault Movement",
      desc="Camera-ready movement preparation for actors and production teams, from the coaches behind movement work on Tamil films since 2012.",
      crumbs=[("More from Vault Movement", "/more"), ("Screen Movement", "/more/screen-movement")],
      wa="Hi Vault Movement, I'd like to ask about Screen Movement for a production.", programme="Screen Movement")
def screen(p):
    return more_page(p, "Film &amp; screen", "Screen Movement",
        "Screen Movement is Vault Movement's movement preparation for actors, performers and production teams: a camera-ready movement vocabulary, precision and repeatable performance with safety discipline. Our coaches have done movement work for Tamil films including Chekka Chivantha Vaanam, Irumbu Thirai and Kanithan.",
        [("Who it's for", "Screen professionals", ["Actors and performers", "Directors and movement coordinators", "Production teams"]),
         ("What we train", "Camera-ready movement", ["Vaults and safe falling", "Combat movement", "Wire-work preparation", "Expressive physical storytelling", "Movement choreography"]),
         ("Film work", "Tamil cinema", ["Mugamoodi (2012)", "Kaaki Sattai (2015)", "Kanithan (2016)", "Irumbu Thirai (2018)", "Chekka Chivantha Vaanam (2018)", f"Sarpatta Parambarai (2021) — the “Dancing Rose” character {confirm('Years')}"])], None, cta=False) + \
        sec(f'<div class="card card-pad split"><div class="stack-sm maxw"><h2 class="h3">Planning a production?</h2><p class="body">Tell us about the project and the movement it needs.</p></div><div class="row">{wa_btn(p["wa"], "screen")}{call_link("screen")}</div></div>', "sec sec-top0")

# ================================================================ VAULT METHOD
@page(path="/vault-method", file="vault-method.html", slug="vault-method",
      title="The Vault Method — 750+ movements, five levels",
      desc="The Vault Method: a library of 750+ movements built since 2008, organised into five coach-verified levels and tracked in the My Vault app.",
      crumbs=[("The Vault Method", "/vault-method")])
def method(p):
    hero = phero(p, "The Vault Method", "A Vault of Movements, each unlocks one level at a time.",
                 "The Vault Method is how Vault Movement coaches: a library of 750+ movements, built and refined since 2008, organised into five coach-verified levels. Your coach unlocks a movement, you attempt it, and your coach verifies it live.",
                 tagline="Built to Move, Built for Life.", aside=f'<div style="max-width:300px;margin:0 auto">{vring("mv", cls="", label="Vault Movement V-ring")}</div>')
    vault = sec(f'''<div class="row" style="align-items:flex-start;gap:32px 64px"><div style="flex:1 1 360px" class="stack">{head("The Vault", "What is the Vault?")}</div>
<div style="flex:1.3 1 460px" class="stack"><p class="lead">Our Vault has 750+ movements, built and refined since 2008. Master every move to unlock your next level, on a Gameplan you and your coach have tailored to your goal!</p></div></div>''', "sec sec-top0")
    how = sec(f'<div class="stack-lg">{head("Progression", "How does progression work?")}' + numcards([
        ("Your coach unlocks a movement", "Movements open up in order, on your Gameplan."),
        ("You attempt it", "With coaching, at your pace, as many sessions as it takes."),
        ("Your coach verifies it live", "No self-logging. A level badge is earned when every movement in that level is verified."),
    ], "g-300") + "</div>", "sec bg-silk")
    levels = sec(f'<div class="stack-lg">{head("Five levels", "What are the five Vault levels?", "Vault One and Two are for everybody. Vault Three is for committed movers. Vault Four and Five are mainly the coaching path, open to a few members through Personal Training.")}{levels_grid()}</div>')
    app = sec(f'''<div class="panel-mist row" style="gap:32px 56px"><div style="flex:1 1 380px" class="stack"><p class="eyebrow">My Vault</p><h2 class="h2">What is the My Vault app?</h2>
<p class="body">My Vault is the member app for your Gameplans, progress, level badges and nutrition plan.</p><div class="row"><a class="btn btn-secondary" href="{APP}">Member login</a></div></div>
<div style="flex:1 1 320px">{photo("My Vault app screens: Gameplan, progress and badges", ratio="r-43", cls="ph-silk", kind="Screenshot needed")}</div></div>''', "sec sec-top0")
    faqs = faq_block([
        ("Can I log my own progress?", "No. Your coach verifies every movement live. That is what makes a Vault level mean something."),
        ("Who reaches Vault Four and Five?", "Mainly our coaches. A few members reach them through Personal Training on the way to becoming coaches."),
        ("Do you publish the movement list?", "No. The Vault is our own method. Your coach shows you what comes next on your Gameplan."),
        ("What is the My Vault app?", "The member app for your Gameplans, progress, badges and nutrition plan. Members log in at app.vaultmovement.fit."),
    ], title="Vault Method questions.")
    return hero + vault + how + levels + app + faqs + cta_band(p)

# ================================================================ STORY
@page(path="/story", file="story.html", slug="story", dc=("Story.dc.html", 4000), title="The story behind the name — Vault Movement",
      desc="Why Vault? A library of movement, one of the oldest human movements, and the V every founder shares. Vault Movement, formerly Chennai Parkour.",
      crumbs=[("Our Story", "/story")])
def story(p):
    hero = phero(p, "Our story", "The story behind the name.",
                 "Every great practice needs a place to keep what it learns. Since 2008, our coaches have collected, tested and refined the ways the human body moves — landing, balancing, crawling, climbing, lifting, vaulting. That collection became our Vault.",
                 ctas=False, aside=f'<div style="max-width:300px;margin:0 auto">{vring("sv", animate=True, cls="vring-hero", label="The V-ring: a V breaking through a circle")}</div>')
    three = sec(f'<div class="stack-lg">{head("Three meanings", "Why Vault?")}' + numcards([
        ("A vault of movement", "A library of skills, built over eighteen years and unlocked one level at a time."),
        ("Vaulting", "One of the oldest human movements — hands down, and through the obstacle."),
        ("The V", "Every founding partner's first name begins with V. The mark carries that initial."),
    ], "g-300") + "</div>", "sec sec-top0")
    mark = sec(f'''<div class="row" style="align-items:flex-start;gap:32px 64px"><div style="flex:1 1 360px" class="stack">{head("The mark", "A V breaking through a circle.")}</div>
<div style="flex:1.3 1 460px" class="stack">
<p class="serif" style="font-size:clamp(24px,2.4vw,30px);line-height:1.35">The circle represents every pattern you are ready to outgrow. The V represents your first move that quantum leaps your transformation!</p>
<p class="body">Transformation is not one leap. It is choosing to move differently, again and again, until a new pattern takes hold and you move freely.</p></div></div>''', "sec bg-silk")
    wemove = sec(f'''<div class="row" style="align-items:flex-start;gap:32px 64px"><div style="flex:1 1 360px" class="stack">{head("We Move", "From Vault Movement to We Move.")}</div>
<div style="flex:1.3 1 460px" class="stack"><p class="lead">Take “ault” from Vault and “ment” from Movement and you are left with V Move. Say it aloud and it becomes Vee &amp; Mouve — and, in the end, We Move.</p>
<p class="body">Vee and Mouve are our two movers on the <a href="/kids">Vault Kids</a> pages.</p></div></div>''')
    formerly = sec(f'''<div class="panel-mist row" style="gap:32px 64px"><div style="flex:1.4 1 420px" class="stack">{head("Formerly Chennai Parkour", "Why did the name change?")}
<p class="lead" style="max-width:760px">We grew beyond one city and one discipline. Same coaches, same safety-first method — and a name for where we are going.</p>
<div class="row">{arrow("Founders &amp; journey", "/story/founders")}{arrow("Our philosophy", "/philosophy")}</div></div>
<div style="flex:1 1 260px;display:flex;justify-content:center"><img src="/assets/brand/crest.webp" alt="Vault Movement shield crest — Fitness &amp; Lifestyle Studio, Movement for Everybody, established 2008" width="440" height="548" loading="lazy" style="width:min(300px,100%)"></div></div>''', "sec sec-top0")
    return hero + three + mark + wemove + formerly + cta_band(p)

@page(path="/story/founders", file="story/founders.html", slug="founders", dc=("Founders.dc.html", 4050),
      title="Founders & journey — Vault Movement since 2007",
      desc="Three friends met online in 2007 and started training in Chennai's parks. That passion became Chennai Parkour, and today, Vault Movement.",
      crumbs=[("Our Story", "/story"), ("Founders &amp; journey", "/story/founders")])
def founders(p):
    hero = phero(p, "Our story", "Three friends. One Passion. Eighteen years of movement.",
                 "Vishal, Vishwa and Vicky met online in 2007 and started training in Chennai's parks. What began as passion became Chennai Parkour, and today, Vault Movement.", ctas=False)
    people = "".join(f'<article class="card" style="overflow:hidden">{photo(n + " — portrait", ratio="r-45", cls="flat")}<div class="card-body"><h3 class="h3">{n}</h3><p class="label">Founder · Executive Coach</p></div></article>' for n in FOUNDERS)
    ppl = sec(f'<div class="stack-lg">{head("Founders", "The three friends behind Vault Movement.")}<div class="grid g-300">{people}</div></div>', "sec sec-top0")
    tl = [
        ("2007", "Three strangers meet on Orkut and start training together in Chennai's outdoor parks."),
        ("2008", f"Chennai Parkour begins. {confirm('What marked 2008')}"),
        ("2007–2012", "Training videos on YouTube build a following. People start asking: will you teach us?"),
        ("2012", "The Tamil Nadu Parkour Association is founded. Classes run in outdoor parks across three Chennai locations."),
        ("2012–2021", f"Movement for Tamil cinema: action sequences for Mugamoodi (2012), Kaaki Sattai (2015), Kanithan (2016), Irumbu Thirai (2018) and Chekka Chivantha Vaanam (2018), and movement training for the “Dancing Rose” character in Sarpatta Parambarai (2021). {confirm('Years')}"),
        ("2018", "Our first indoor gym opens in Ekkattuthangal: outdoor obstacles rebuilt indoors, so people could train safely. Martial arts, calisthenics and strength training join parkour."),
        ("Ongoing", "Workshops for schools and colleges, corporate programmes, and training for TNCF, CISF, NSG and Tamil Nadu's firefighters."),
        ("2025", "A second studio opens in Injambakkam, on ECR."),
        ("2026", "Chennai Parkour becomes Vault Movement: the same founders and coaches, a Fitness &amp; Lifestyle Studio built for everybody, and the My Vault app."),
    ]
    lis = "".join(f'<li><span class="num" style="min-width:130px;font-size:18px">{y}</span><p class="body" style="color:#0B1426">{x}</p></li>' for y, x in tl)
    timeline = sec(f'''<div class="stack-lg">{head("Our journey", "From Chennai's parks to Vault Movement.")}<ol class="numlist">{lis}</ol>
<div class="card card-pad"><p class="ph-k">Video needed</p><p class="body">The founders' story video (Instagram post, English and Tamil audio) {confirm("Link")}</p></div></div>''', "sec bg-silk")
    close = sec(f'''<div class="stack" style="max-width:820px"><p class="serif" style="font-size:clamp(30px,3.2vw,44px);line-height:1.25">“And we believe movement is for everybody.”</p>
<div class="row">{arrow("Meet the coaches", "/coaches")}{book("founders-close")}</div></div>''')
    return hero + ppl + timeline + close

# ================================================================ PHILOSOPHY
SOURCES = [
    ("Physical activity and allostatic load", "https://doi.org/10.1002/dev.22499"),
    ("Allostatic load and frailty", "https://doi.org/10.1002/smi.70219"),
    ("Play", "https://doi.org/10.1111/aphw.12220"),
    ("Fear and confidence", "https://doi.org/10.1002/jcop.70001"),
    ("Social bonds and survival", "https://doi.org/10.1111/j.1751-9004.2011.00406.x"),
    ("Loneliness", "https://doi.org/10.1002/alz.13072"),
    ("Purpose and functional disability", "https://doi.org/10.1002/lim2.70018"),
]
def fn(*ns):
    return '<sup class="fn">' + ",".join(f'<a href="#src-{n}" aria-label="Source {n}">{n}</a>' for n in ns) + "</sup>"

@page(path="/philosophy", file="philosophy.html", slug="philosophy", title="Our philosophy — five principles | Vault Movement",
      desc="Natural movement, play, fear metabolism, belonging and purpose: the five principles behind every Vault Movement session, with sources.",
      crumbs=[("Philosophy", "/philosophy")])
def philosophy(p):
    hero = phero(p, "Our philosophy", "Five principles every session is built on.",
                 "Vault Movement's coaching rests on five principles: natural movement, play, fear metabolism, belonging and purpose. Here is what each one means in practice, with the research behind it.", ctas=False)
    rows = [
        ("01 · Natural Movement", "The body was made to move all day, not for one intense hour.", "24/7 · Not one hour",
         f"We train the movements you use in life — walking, crawling, climbing, carrying and landing — so moving well becomes part of your day. Physical activity is linked to a lower allostatic load,{fn(1)} and a high allostatic load predicts frailty.{fn(2)}"),
        ("02 · Play", "Play is not a reward. It is essential.", "Joy-first",
         f"Every session leaves room for curiosity and play — for adults as much as kids.{fn(3)}"),
        ("03 · Fear Metabolism", "Most people never learn to move through fear. We teach it, one safe step at a time.", "One safe step at a time",
         f"We break every movement into safe steps, on padded surfaces and at ground level, so confidence builds one success at a time.{fn(4)}"),
        ("04 · Belonging", "The people who live longest belong somewhere.", "+50% survival odds with strong social bonds",
         f"Strong social bonds are linked to 50% better survival odds, and loneliness is comparable to smoking up to 15 cigarettes a day.{fn(5, 6)} Our studios are communities, not just class timetables."),
        ("05 · Purpose / Ikigai", "People with a reason to get up every morning live longer — and stay capable longer.", "31% lower risk of functional disability",
         f"A sense of purpose is linked to a 31% lower risk of functional disability.{fn(7)} A practice that grows with you for decades is a reason to keep showing up."),
    ]
    lis = "".join(f'<li><div class="stack"><p class="eyebrow">{l}</p><p class="phil-q" style="font-size:clamp(24px,2.4vw,30px)">{q}</p><p class="phil-hook" style="min-height:0;border:0;padding:0">{hk}</p></div><p class="body" style="align-self:center">{b}</p></li>' for l, q, hk, b in rows)
    body = sec(f'<ol class="phil-full">{lis}</ol>', "sec sec-top0")
    close = sec(f'<div class="stack" style="max-width:820px"><p class="serif" style="font-size:clamp(28px,3vw,40px);line-height:1.3">We are not just building athletes. We are building humans who age differently.</p><p class="tagline">Five principles. Every session.</p></div>', "sec bg-silk")
    src = "".join(f'<li id="src-{i}">{t}: <a href="{u}" target="_blank" rel="noopener">{u}</a></li>' for i, (t, u) in enumerate(SOURCES, 1))
    sources = sec(f'<div class="stack"><h2 class="h3">Sources</h2><ol class="sources">{src}</ol><p class="updated">Last updated {UPDATED_TEXT}</p></div>', "sec-sm")
    return hero + body + close + sources + cta_band(p)

# ================================================================ COACHES
COACHES = [
    ("Vishal Kumar", "@vishal_cpk", "https://www.instagram.com/vishal_cpk", ["Technical", "Structure", "Mentorship"],
     "The technical backbone of our coaching. Known for clean execution, methodical progression and fundamentals that last."),
    ("Vishwa Dayakaran", "@vishwa_chennaiparkour", "https://www.instagram.com/vishwa_chennaiparkour", ["Energy", "Community", "Youth"],
     "The heartbeat of our community. Brings energy to conditioning and drills, team culture and youth engagement."),
    ("Vignesh Raghavan", "@parkourpaiyan", "https://www.instagram.com/parkourpaiyan", ["Cinematic", "Expression", "Elite"],
     "Has trained TNCF, CISF and NSG personnel, and is an official Tamil Nadu Fire &amp; Rescue Services coach. Known in Tamil cinema for movement work on Chekka Chivantha Vaanam, Irumbu Thirai and Kanithan."),
]

@page(path="/coaches", file="coaches.html", slug="coaches", dc=("Coaches.dc.html", 2800), title="Coaches — Vault Movement Executive Coaches",
      desc="Meet Vault Movement's three Executive Coaches — Vishal Kumar, Vishwa Dayakaran and Vignesh Raghavan — each with 18+ years of coaching.",
      crumbs=[("Coaches", "/coaches")])
def coaches(p):
    p["ld"] = [{"@type": "Person", "name": n, "jobTitle": "Executive Coach", "worksFor": {"@id": ORG_ID}, "description": strip_tags(b), "sameAs": [u]} for n, _, u, _, b in COACHES]
    hero = phero(p, "Coaches", "Coach-led, every session.",
                 f"Vault Movement is led by three Executive Coaches, each with 18+ years of coaching, and our team of {confirm('N')} coaches.", ctas=False)
    cards = "".join(f'''<article class="card" style="overflow:hidden">{photo(n + " — portrait", ratio="r-45", cls="flat")}<div class="card-body">
<p class="label">Executive Coach · 18+ years</p><h2 class="h3">{n}</h2><p class="body" style="font-size:16px">{b}</p>{chips(tags)}<a class="arrow mt-auto" href="{u}" target="_blank" rel="noopener">{hd} {icon("ext", 18)}</a></div></article>''' for n, hd, u, tags, b in COACHES)
    return hero + sec(f'<div class="grid g-300">{cards}</div>', "sec sec-top0") + cta_band(p)

# ================================================================ LOCATIONS
@page(path="/locations", file="locations.html", slug="locations", dc=("Locations.dc.html", 2850), title="Locations — City Studio and Coast Studio | Vault Movement",
      desc="Vault Movement studios: City Studio · Ekkattuthangal and Coast Studio · Injambakkam, ECR. Both open every day, 6:00 AM – 9:00 PM.",
      crumbs=[("Locations", "/locations")])
def locations(p):
    p["ld"] = [studio_ld(s) for s in STUDIOS]
    hero = phero(p, "Locations", "Two studios, open every day.",
                 "Vault Movement has two studios in Chennai: City Studio · Ekkattuthangal and Coast Studio · Injambakkam, ECR. Both are open every day, 6:00 AM – 9:00 PM.", ctas=False)
    return hero + sec(f'<div class="grid g-460">{"".join(studio_card(s, 2) for s in STUDIOS)}</div>', "sec sec-top0") + cta_band(p)

def studio_page(p, s):
    p["ld"] = [studio_ld(s)]
    hero = phero(p, "Locations", s["label"],
                 f"Vault Movement's {s['name']} is at {h(s['address'])}. It is open every day, 6:00 AM – 9:00 PM. Book an Experience Session to find the right batch here.",
                 aside=studio_card(s, 2, False))
    rows = [("V12", "Vault 12"), ("M&amp;S", "Movement &amp; Strength"), ("PT", "Personal Training (Trio and 1:1)"), ("U14", "Vault Kids · Under 14"), ("U10", "Vault Kids · Under 10"), ("Toddler", "Vault Kids · Toddlers")]
    tt = "".join(f'<tr><td><strong>{c}</strong></td><td>{n}</td><td>{confirm()}</td></tr>' for c, n in rows)
    timetable = sec(f'''<div class="stack-lg">{head("Timetable", f"What runs at the {s['name']}?")}
<div class="tt-wrap"><table class="tt"><thead><tr><th scope="col">Code</th><th scope="col">Programme</th><th scope="col">Days and times</th></tr></thead><tbody>{tt}</tbody></table></div></div>''', "sec sec-top0")
    getting = sec(f'''<div class="grid g-300">
<div class="card card-pad stack"><p class="eyebrow">Directions</p><p class="body">{confirm()}</p>{arrow("Open in Google Maps", "https://www.google.com/maps/search/?api=1&amp;query=" + urllib.parse.quote(s["map_q"]), ext=True)}</div>
<div class="card card-pad stack"><p class="eyebrow">Parking</p><p class="body">{confirm()}</p></div>
<div class="card card-pad stack"><p class="eyebrow">Hours</p><p class="body">{HOURS}</p></div></div>''', "sec bg-silk")
    nm = s["name"]
    slots = "".join(photo(f"{nm} interior, natural light — photo {i}", ratio="r-43") for i in (1, 2, 3))
    gal = sec(f'<div class="stack-lg">{head("Inside the studio", "Photos.")}<div class="gallery">{slots}</div></div>')
    return hero + timetable + getting + gal + cta_band(p)

@page(path="/locations/ekkattuthangal", file="locations/ekkattuthangal.html", slug="studio-city",
      title="City Studio · Ekkattuthangal — Vault Movement",
      desc="Vault Movement City Studio: TS 69, Second Floor, SIDCO Industrial Estate, Ekkaduthangal, Chennai. Open every day, 6 AM – 9 PM.",
      crumbs=[("Locations", "/locations"), ("City Studio · Ekkattuthangal", "/locations/ekkattuthangal")],
      wa="Hi Vault Movement, I'd like to book an Experience Session at the City Studio, Ekkattuthangal.", studio="City Studio · Ekkattuthangal")
def city(p):
    return studio_page(p, STUDIOS[0])

@page(path="/locations/injambakkam-ecr", file="locations/injambakkam-ecr.html", slug="studio-coast",
      title="Coast Studio · Injambakkam, ECR — Vault Movement",
      desc="Vault Movement Coast Studio: East Coast Road, Cholamandal Artists Village, Injambakkam, Chennai. Open every day, 6 AM – 9 PM.",
      crumbs=[("Locations", "/locations"), ("Coast Studio · Injambakkam, ECR", "/locations/injambakkam-ecr")],
      wa="Hi Vault Movement, I'd like to book an Experience Session at the Coast Studio, ECR.", studio="Coast Studio · Injambakkam, ECR")
def coast(p):
    return studio_page(p, STUDIOS[1])

# ================================================================ STORIES
@page(path="/stories", file="stories.html", slug="stories", title="Member stories — Vault Movement",
      desc="Real words from Vault Movement members and teams, verbatim, plus member stories on Instagram.",
      crumbs=[("Stories", "/stories")])
def stories(p):
    hero = phero(p, "Member stories", "In their words.",
                 "Real words from Vault Movement members and teams, shared verbatim. More member stories live on our Instagram.", ctas=False)
    band = sec(tband(["arun", "santhosh", "vijay", "karthik"], "Members and teams.", link_all=False) + ig_cards() + "</div>", "sec bg-ink")
    return hero + band + cta_band(p)

# ================================================================ FAQ
FAQ_GROUPS = [
    ("About Vault Movement", [
        ("Is Vault Movement the same as Chennai Parkour?", "Yes. Chennai Parkour, founded in Chennai in 2008, is now Vault Movement. Same coaches, same safety-first method — a new name for where we are going."),
        ("Where are your studios, and what are your hours?", "City Studio · Ekkattuthangal and Coast Studio · Injambakkam, ECR. Both are open every day, 6:00 AM – 9:00 PM."),
        ("How much does it cost?", "Every journey starts with an Experience Session. We share plans after it, on a call or on WhatsApp."),
        ("Do you offer franchises?", "Yes. We welcome franchise enquiries — see our <a href=\"/franchise\">Franchise</a> page."),
    ]),
    ("Programmes", [
        ("What is Vault 12, and how is it different from Movement &amp; Strength?", "Vault 12 is a 12-week, coach-led starter programme with a structured Monday–Friday Gameplan and a nutrition plan. Movement &amp; Strength comes next: six days a week, sixty-minute sessions on two alternating Gameplans, progressing through Vault One, Two and Three."),
        ("Do you offer personal training?", "Yes. Personal Training runs as PT Trio (a group of three) or PT 1:1, on a Gameplan built around you."),
        ("What is the My Vault app?", "The member app for your Gameplans, progress, level badges and nutrition plan. Members log in at app.vaultmovement.fit."),
        ("Are there levels?", "Yes. The Vault Method has five coach-verified levels, Vault One to Vault Five. Your coach verifies every movement live, and you earn a level when every movement in it is verified."),
        ("What happens in a Movement &amp; Strength session?", "Movement skills after a warm-up, then your strength workout, then a flexibility and mobility routine."),
        ("What is calisthenics?", "Strength training that uses your own bodyweight as resistance, from your first push-up, pull-up or squat to dips, muscle-ups and handstands. We use progressive calisthenics to build strength, mobility, coordination and body control, whether you are a complete beginner or already strong."),
        ("Is weight training required?", "Not at the start. Most of the work uses your own bodyweight. Beginners learn good form on bodyweight movements for a few weeks before free weights are added for more strength and power."),
        ("Is parkour still part of Vault Movement?", "Yes. The fundamentals — balance, landing and safe falling, running and jumps, vaults, swings and climbs — are part of Movement &amp; Strength, taught progressively at ground level."),
    ]),
    ("Getting started", [
        ("What level of fitness do I need to start?", "None. People of all fitness levels are welcome — lean or heavy, short or tall, or feeling weak. We start with the basics, within your comfort zone, and help you build from there, with a community that keeps you going."),
        ("Should I lose weight or get stronger before I join?", "Not at all. There are movements for every body type, and your coach builds your programme around where you are today."),
        ("Am I too old to start?", "No. Our members range from toddlers, who train with a parent, to adults in their sixties and beyond. It is never too late to start moving."),
    ]),
    ("Vault Kids", [
        ("What age can kids start?", "Vault Kids runs Toddler, Under 10 and Under 14 batches. Parents are welcome to join in at Toddler sessions."),
        ("Do you work with neurodivergent children?", "Yes. Adaptive Movement is for autistic children, children with ADHD and children with additional needs, in small groups or 1:1. It complements your child's therapy, never replaces it."),
        ("How do you keep children safe?", "A higher coach-to-child ratio, age-appropriate equipment and mats, and regular parent updates. No child moves to a new skill until the prerequisite is solid."),
    ]),
    ("Safety and training", [
        ("Is it safe?", "Yes, when you train with a coach through the right progressions and conditioning. We teach on padded surfaces, so you can learn without fear, and processing fear in stages is one of the first skills you learn."),
        ("Do you train at ground level?", "Yes. We do not teach or encourage training anywhere with a risk of serious injury. Most experienced movers train at ground level, and there is plenty of challenge and fun in safe, ground-level training."),
        ("Does movement training help concentration?", "Yes. Every movement needs focus. Beginners practise landing and balance drills that build precision, control and concentration."),
        ("Will it help my other sports?", "Yes. Whether it's football, tennis, cricket or badminton, movement training builds agility, mobility and spatial awareness that carry into your sport."),
    ]),
]

@page(path="/faq", file="faq.html", slug="faq", title="FAQ — Vault Movement",
      desc="Answers about Vault Movement: studios and hours, programmes, Vault Kids, levels, the My Vault app, safety, costs and franchises.",
      crumbs=[("FAQ", "/faq")])
def faq(p):
    hero = phero(p, "FAQ", "Frequently asked questions.",
                 "Answers about Vault Movement — formerly Chennai Parkour — our studios, programmes, Vault Kids, the Vault Method and how to get started.", ctas=False)
    groups = "".join(f'<div class="faq-group"><h2 class="h3">{g}</h2><div class="faq">{faq_items(items)}</div></div>' for g, items in FAQ_GROUPS)
    body = sec(f'<div style="max-width:880px">{groups}<p class="updated" style="margin-top:32px">Last updated {UPDATED_TEXT}</p></div>', "sec sec-top0")
    return hero + body + cta_band(p)

# ================================================================ FRANCHISE
@page(path="/franchise", file="franchise.html", slug="franchise", title="Franchise — bring Vault Movement to your city",
      desc="Franchise enquiries for Vault Movement: a proven coaching method, a 750+ movement library, the My Vault app and a brand built since 2008.",
      crumbs=[("Franchise", "/franchise")], wa="Hi Vault Movement, I'd like to ask about a franchise.", programme="Franchise")
def franchise(p):
    hero = phero(p, "Franchise", "Bring Vault Movement to your city.",
                 "Vault Movement is open to franchise enquiries. Partners get the Vault Method, our 750+ movement library, the My Vault app and a brand built in Chennai since 2008.", ctas=False)
    why = sec(f'<div class="stack-lg">{head("Why Vault Movement", "What does a franchise partner get?")}' + numcards([
        ("The Vault Method", "A coach-led method with five coach-verified levels."),
        ("The movement library", "750+ movements, built and refined since 2008."),
        ("The My Vault app", "Gameplans, progress, level badges and nutrition plans for members."),
        ("The brand", "Vault Movement — formerly Chennai Parkour — and Movement for Everybody."),
    ], "g-240") + "</div>", "sec sec-top0")
    who = sec(f'<div class="card card-pad stack maxw"><p class="eyebrow">Who we look for</p><h2 class="h3">Partners who share our values</h2><p class="body">Criteria {confirm()}</p></div>', "sec bg-silk")
    how = sec(f'<div class="stack-lg">{head("How it works", "What are the steps?")}' + numcards([
        ("Enquire", "Send the franchise enquiry form."), ("Conversation", f"An introductory conversation {confirm()}"),
        ("Evaluation", f"Location and partner evaluation {confirm()}"), ("Launch", f"Training and launch support {confirm()}"),
    ], "g-240") + "</div>")
    form = sec(f'''<div class="row" style="align-items:flex-start;gap:40px 64px"><div style="flex:1 1 340px;max-width:440px" class="stack"><p class="eyebrow">Enquire</p><h2 class="h2">Franchise enquiry.</h2><p class="body">We'll reply within 24 hours.</p>{wa_btn(p["wa"], "franchise")}</div>
<div style="flex:1.4 1 460px;min-width:0" class="card card-pad stack"><p class="ph-k">Franchise Zoho form</p><p class="body">Separate Zoho enquiry form — form link {confirm()}</p></div></div>''', "sec bg-silk", id="enquire")
    return hero + why + who + how + form

# ================================================================ LEGAL
def legal(p, h1, intro, sections_html):
    hero = phero(p, "Legal", h1, intro, ctas=False)
    note = f'<p class="panel-ink" style="margin-bottom:32px"><strong>Draft for legal review.</strong> Items marked Confirm need the owner\'s input.</p>'
    return hero + sec(f'<div class="prose">{note}{sections_html}<p class="updated" style="margin-top:40px">Last updated {UPDATED_TEXT}</p></div>', "sec sec-top0")

@page(path="/privacy", file="privacy.html", slug="privacy", title="Privacy Policy — Vault Movement",
      desc="How Vault Movement Pvt Ltd collects, uses and protects your personal data when you use our website, forms and WhatsApp.",
      crumbs=[("Privacy", "/privacy")])
def privacy(p):
    s = f'''<h2>Who we are</h2><p>Vault Movement Pvt Ltd (“Vault Movement”, “we”), formerly Chennai Parkour, runs this website and our studios in Chennai. Contact: {PHONE} · email {confirm()}.</p>
<h2>What we collect</h2><ul><li>Details you send through our enquiry forms, which run on Zoho Forms: your name, phone number, email (optional), programme, studio and message.</li>
<li>For Vault Kids enquiries: a parent or guardian's details, the child's first name and batch only. We do not ask for a child's date of birth or photos on this website.</li>
<li>Messages you send us on WhatsApp or by phone.</li><li>How you arrived at the site (for example, campaign tags in the link), recorded with your enquiry.</li></ul>
<h2>Cookies and analytics</h2><p>Essential storage keeps the site working and remembers your cookie choice. Google Analytics 4 and the Meta Pixel load only if you choose “Accept all”. You can change your choice at any time with “Cookie settings” in the footer.</p>
<h2>Embedded content</h2><p>Instagram reels and Google Maps load only when you tap them. When they load, Instagram or Google may collect data under their own policies.</p>
<h2>How we use your data</h2><p>To reply to your enquiry, book your Experience Session, share plans, and run and improve our programmes. We do not sell your data.</p>
<h2>Who we share it with</h2><p>Service providers who help us run the website and enquiries, such as Zoho (forms), Meta (WhatsApp) and Google — and no one else, unless the law requires it.</p>
<h2>How long we keep it</h2><p>Retention period {confirm()}.</p>
<h2>Your rights</h2><p>Under India's Digital Personal Data Protection Act, 2023, you can ask to access, correct or erase your personal data, withdraw consent, and raise a grievance. Contact us at {PHONE} or email {confirm()}.</p>
<h2>Changes</h2><p>We will post any changes to this policy on this page.</p>'''
    return legal(p, "Privacy Policy", "How Vault Movement collects, uses and protects your personal data.", s)

@page(path="/terms", file="terms.html", slug="terms", title="Terms of Use — Vault Movement",
      desc="Terms of use for the Vault Movement website, run by Vault Movement Pvt Ltd.", crumbs=[("Terms", "/terms")])
def terms(p):
    s = f'''<h2>About this website</h2><p>This website is run by Vault Movement Pvt Ltd, formerly Chennai Parkour. By using it, you agree to these terms.</p>
<h2>Information on this site</h2><p>We work to keep information accurate, but programmes, timings and details may change. We do not publish prices; plans are shared after your Experience Session.</p>
<h2>Health and safety</h2><p>Talk to your doctor before starting any new exercise programme, especially if you have a medical condition, an injury or are pregnant. Train only under the guidance of our coaches. Moves marked “Try at home” on our kids pages are ground-safe and should be done with an adult nearby.</p>
<h2>Our brand and content</h2><p>Vault Movement™, the V-ring mark, the shield crest, Vee, Mouve and the content on this site belong to Vault Movement Pvt Ltd. Please do not copy or reuse them without permission.</p>
<h2>Links to other sites</h2><p>We link to Instagram, Google Maps, WhatsApp and Zoho. We are not responsible for their content or policies.</p>
<h2>Liability</h2><p>Limitation of liability {confirm()}.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of India, with courts in Chennai having jurisdiction {confirm()}.</p>
<h2>Contact</h2><p>{PHONE} · email {confirm()}.</p>'''
    return legal(p, "Terms of Use", "The terms for using the Vault Movement website.", s)

# ================================================================ UTILITY
@page(path="/thank-you", file="thank-you.html", slug="thank-you", noindex=True, title="Thank you — Vault Movement",
      desc="Thank you for your enquiry. We will reply on WhatsApp or call within 24 hours.", crumbs=[("Thank you", "/thank-you")])
def thanks(p):
    body = f'''<section class="phero"><div class="wrap"><div class="stack" style="max-width:760px;margin-top:40px">
<span class="check-dot" style="width:56px;height:56px;background:#2E7D4F">{icon("check", 28, "#FAF8F3", 2)}</span>
<h1 class="h1 h1-sm">Thank you — we've got your request.</h1>
<p class="lead">We'll reply on WhatsApp or call within 24 hours to book your Experience Session.</p>
<ol class="numlist" style="margin-top:16px"><li><span class="num">01</span><p class="body">We contact you on WhatsApp or by phone.</p></li><li><span class="num">02</span><p class="body">We pick a time for your Experience Session.</p></li><li><span class="num">03</span><p class="body">You come in for your baseline assessment and programme match.</p></li></ol>
<div class="row">{wa_btn(DEFAULT_WA, "thank-you", "WhatsApp us now")}{arrow("See how the journey works", "/journey")}</div></div></div></section>'''
    return body

@page(path="/404", file="404.html", slug="not-found", noindex=True, title="Page not found — Vault Movement",
      desc="This page could not be found.", crumbs=[("Page not found", "/404")])
def notfound(p):
    return f'''<section class="phero"><div class="wrap"><div class="stack" style="max-width:760px;margin-top:40px">
<p class="eyebrow">404</p><h1 class="h1 h1-sm">This page has moved on.</h1>
<p class="lead">If you followed a Chennai Parkour link, the page may now live somewhere new on Vault Movement.</p>
<div class="row">{book("404")}{arrow("Go to the home page", "/")}{arrow("Programmes", "/more")}</div></div></div></section>'''
