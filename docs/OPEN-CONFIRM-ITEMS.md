# Vault Movement website v1 — open items to confirm

Every item below appears on the site as a **CONFIRM** tag, a labelled placeholder or a setting that still needs a value. Updated 10 November 2026.

## Facts and contact
1. **Email address** — not shown anywhere yet (footer, Organization schema, Privacy, Terms).
2. **Hours** — the site uses the brief: every day, 6:00 AM – 9:00 PM. The current chennaiparkour.fit says Mon–Fri 6–9, Sat–Sun 7–8.
3. **City Studio address spelling** — the address uses "Ekkaduthangal" (as supplied); the studio name and URL use "Ekkattuthangal".
4. **Map coordinates** — latitude/longitude for both studios, so they can be added to the HealthClub schema.
5. **Timetables** — batch days and times for V12, M&S, PT, U14, U10 and Toddler, per studio, and which programmes run at which studio.

## Movement & Strength
6. **Gameplan A and B focus** — Gameplan A runs Mon/Wed/Fri and Gameplan B runs Tue/Thu/Sat. Your example focus for each is shown as an "e.g." under a CONFIRM tag.
7. **Minimum age.**
8. **Batches** — morning times (6:30 · 7:40 · 8:50) per studio, and evening batches.
9. **Minimum days per week.**

## Personal Training
10. **Trio matching** — can you match individuals into a trio? Do members need two friends?
11. **Nutrition guidance** — is it included?
12. **Sessions per week.**
13. **Home or on-site sessions** — offered or not?

## Other programme pages
14. **Adaptive Movement** — what "predictable routines" means in practice.
15. **Mind & Movement** — description, format, duration and dates. Your example is shown as an "e.g." under a CONFIRM tag on the More page.
16. **Bharatanatyam workshops** — instructor and format.
17. **Sports Performance & LTAD** — LTAD format and age groups.
18. **Birthdays & Events** — venue, group size and timings.
19. **Coach Certification** — cohort size.
20. **More page, last group** — your message cut off after the Armed Forces card. I finished that card's "Best for" line as "units, personnel and pre-selection candidates". I also built a fourth group, "Performance and coaching" (Sports Performance & LTAD, Movement Coach Certification), plus a low-key text link to Screen Movement. Send the rest of the spec if it differs.
21. **Franchise** — the Zoho franchise form link, "who we look for" criteria, and the steps (currently placeholders).

## Story and people
22. **What marked 2008** on the Founders & journey timeline.
23. **Film years** — Mugamoodi 2012, Kaaki Sattai 2015, Kanithan 2016, Irumbu Thirai 2018, Chekka Chivantha Vaanam 2018, Sarpatta Parambarai 2021. The same list is now on the Screen Movement page.
24. **Founders' story video** — the Instagram post link. The video file was not attached.
25. **Coach team size** — "[and our team of N coaches]".
26. **Portraits** — photos of the three founders / Executive Coaches.

## Media
27. **Instagram highlight titles** — titles for the two highlight cards.
28. **Social handles** — the footer and schema still use the Chennai Parkour accounts.
29. **Vault 12 testimonial** — a real member's words, verbatim, with consent.
30. **Ranjani M. video testimonial** — left out until the video is supplied.
31. **Reels to review** — check every reel for flips, heights or stunt moments before launch. Remove any that show them:
    - Movement & Strength: Cllhk5ggTBs, DZoSDtaJUUw, DXrGeimh0P3, DZjjKsuzKhK
    - Vault Kids and Birthdays: DZKZD8KzQRH, DXJnV-jkjQj, DZ4whF5SJyW
    - Kaladi: DX4DCuySVK-, DYPOYwBpu_g, DY1zygqpph2, DXtuqH8EeTJ
32. **Ported photos** — see `legacy-photos.md`. Review each against the no-flips / no-heights / no-stunts rule, write descriptive alt text, and check the armed forces photos for insignia.
33. **New photography** — every "PHOTO NEEDED" slot (Home path cards, kids heroes and cohorts, programme heroes, portraits, studio interiors, the My Vault app screenshot).

## Vee & Mouve (Kids pages)
34. **Ages** — now Vee 7 and Mouve 11, per your instruction (the earlier brief said 10 and 13). The kit lines were removed from the Kids page.
35. **Character art** — the current art is interim: heads cropped from the reference sheets, with lime recoloured to Gold. Final art should follow the locked kit and the new ages.
36. **Learn with Vee & Mouve** — 12 move cards drafted from *Basic Body Movements*. **A coach must review them before launch.** Each card also needs an illustration.

## Brand and wording
37. **Logo gold** — the supplied logo file uses about #FFD21F; the Gold token is #F5B700. Which is master?
38. **Small wording fixes made to your text:**
    - "your train together" → "you train together"
    - "acheive" → "achieve"
    - "gameplan" → "Gameplan" (the brand term)
    - "specialized training gameplan" → "specialised training Gameplans" (Indian English, as in the brief)
    - Personal Training meta title: "—" → ":" to stay within 60 characters
39. **Header** — "Member login" shows as an icon between 1200 and 1499 px so the nav fits on one line. Above 1500 px the text shows.
40. **Menu** — "The Vault Method" and "Philosophy" now jump to their sections on Home. The full /vault-method and /philosophy pages (with research sources) are still live and linked from those Home sections and the footer.
41. **Toddler age** — the site states no age. The Aug 2026 FAQ said "above the age of 2" and "2 to 60+".

## Set-up (in tools, not on the page)
42. **GA4 and Meta Pixel IDs** — paste into `assets/js/site.js`.
43. **Zoho WebsiteLeads form:**
    - submit label "Book an Experience Session"
    - hidden fields with these aliases: page, programme, studio, utm_source, utm_medium, utm_campaign, gclid, fbclid
    - thank-you redirect to `https://vaultmovement.fit/thank-you`
    - a kids variant: parent or guardian, child's first name and cohort only — no date of birth, no photos
44. **AI training crawlers** — allowed in robots.txt, as the brief set as the default.
45. **Legal review** — Privacy (retention period) and Terms (liability, jurisdiction) are drafts.

## Resolved in this round
- Experience Session: 1 hour; bring yourself, ready to transform, in comfortable clothes.
- Founders: Vignesh Raghavan, Vishwa Dayakaran, Vishal Kumar. The timeline from 2007 to 2026 is in.

## FAQ items not migrated
From the Aug 2026 FAQ, these are about parkour as a sport and were left out:
- What is Parkour?
- Parkour competitions (SPL, Chase Tag, Olympics)
- How is Parkour different from other sports?
- Is Parkour popular in India?
- Old level timing
