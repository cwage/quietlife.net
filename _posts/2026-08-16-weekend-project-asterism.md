---
title: "asterism"
author: cwage
layout: post
permalink: /2026/08/16/asterism/
categories:
  - tech
  - space
---

### tl;dr
- I made a website you can upload a photo of the night sky (optimized for photos taken with a phonecam) and get an annotated version sohwing the identified stars, planets, and other solar system bodies.
- live at: [https://asterism.quietlife.net](https://asterism.quietlife.net)
- repo: [cwage/asterism](https://github.com/cwage/asterism) — MIT license if you wanna run it yourself
- no account needed, no location permission, no compass. it works out where the camera was pointing from the star pattern alone (usually. sometimes. disclaimers apply.)

<!--more-->

### but why?

A few months ago when I was working on [some extreme nerdery with platesolving](/2026/04/08/platesolving-for-fun-and-no-profit/), I found myself explaining to people what platesolving is, and how it works (specifically how [astrometry](https://astrometry.net/) works -- see my aforementioned post for details on that.). It dawned on me that while astrometry is very cool, it's definitely not optimized for the average joe -- the nova web interface is kinda buried on their site, and the solving is optimized for astrophotographers, not the "I took a photo of the night sky with my phone, what am i looking at" crowd. With smartphone cameras getting better and better, that crowd is expanding, especially since the pixel camera app's "night sight" now has an actual astrophotography mode (i assume iphones have something similar as well). So I figured I'd build a website similar to nova.astrometry.net, but oriented around non-astronomers with smartphones. This actually works out well, because we can assume a tighter subset of potential Fields of View, meaning fewer datasets necessary and much faster platesolving. Amusingly, despite it being oriented for phone photos, it [successfully solved](https://asterism.quietlife.net/?job=01ff926f933947748c7f3a141d0eb829) the same NASA artemis moon eclipse shot I previously worked to solve by hand!

### what it does

- upload a night-sky photo → it plate-solves it and draws labels over your own photo on a canvas
- **stars** — named + Bayer designations (α Lup, γ² Vel) down to mag 4.5, from the HYG catalog
- **constellations** — Stellarium's modern stick-figure line set, resolved through HYG
- **Moon and planets** — the thing astrometry.net structurally can't do: they move, so they aren't in any star index. computed from the photo's EXIF timestamp + GPS
- **deep-sky objects** — the naked-eye Messier stuff (M31, M42, Pleiades)
- **satellites** — which satellites passed through the frame while the shutter was open, propagated from archived orbital element sets
- **narration** — a short LLM-written "what you captured" writeup + a one-line caption
- **share card** — server-rendered PNG of the annotated photo, so a link unfurls with the picture
- **failure is a feature** — if it *can't* solve, EXIF time + GPS still answers "Venus, WSW, 12° up"
- public feed of recent solves on the homepage; everything deleted after 24h

It doesn't work 100% of the time, of course -- the quality of the night sky itself is frequently the main barrier, obviously. Most people live in cities, and most cities are [bortle 7 or 8 at best](https://en.wikipedia.org/wiki/Bortle_scale). But even in testing outside my house (solidly bortle 8) with the astrophotog mode or even just night sight, i got some good results!

### how it works: the interesting parts

Full disclosure: claude code (fable 5 model) figured most of this shit out -- I was just along for the ride. I'd have ragequit much earlier and fired up minecraft or something. So I just had claude code write this part:

> **Guessing the field of view from EXIF.** The solver needs to know roughly how wide your photo is before it can search. EXIF gives a focal length, but:
>
> - phones lie. Pixel 9 reports 24mm-equivalent (~74°) while the saved frame is a 2x crop of the 50MP sensor and truly spans 38.4°
> - crops and digital zoom only ever make the field *narrower* than the lens implies, never wider — so the scale bracket is deliberately lopsided (0.35x to 1.2x)
> - if that fails, walk fallback tiers: 30–90° (phone-typical), 8–35° (cropped/zoomed), 2.5–10° (telephoto)
> - the shipped wide-field indexes are ~100MB; the multi-GB telescope index sets stay out of scope. a 10x phone periscope is only ~8.6° wide, so phone telephoto works without them
>
> **Failing fast.** An unsolvable image used to burn ~200s walking every tier.
>
> - ~1s star-count pre-check rejects zero-star uploads (photos of food, daylight, a dark room) instantly
> - the quick pass tries only the likeliest tier; the user can click "dig deeper" to opt into the slow fallbacks
> - "we searched and it isn't there" vs. "we ran out of CPU time" are *different answers* and get reported differently — saying "no solution" for a timeout is a lie
>
> **The solver will confidently lie to you.** `solve-field` exits 0 and writes a valid WCS for a match built from three stars — which points somewhere confidently wrong.
>
> - so acceptance is gated on match confidence (log-odds ≥ 25, ≥ 8 matched stars), not on exit code
> - calibrated against real solves: genuine ones came in at log-odds 43–825; the false one that prompted this was 9.5 with 2 matched stars
> - the first calibration was wrong because it used only my *featured* (i.e. best) solves — two ordinary phone shots later landed well below that "floor"
>
> **Phone night modes physically move the stars.** This is my favorite one.
>
> - night mode is a computational stack: it aligns and merges many frames, tile by tile
> - if a tile locks onto a moving cloud instead of the stars, it drags those stars up to ~1° away from where the geometry says they are
> - so after projecting labels, verify them against the actual pixels: find the real source near each predicted position, fit a smooth residual field over the confident matches, re-place every label through it
> - a star with no source under it gets flagged `hidden` — it's in the frame, but a cloud ate it
> - deep-sky objects are extended, so they can't be snapped to a point: they get a photometric check instead (core brightness vs. surrounding annulus), so a label never circles "Andromeda Galaxy" over bare sky-glow
>
> **Honesty about what we don't know.**
>
> - the EXIF compass heading turned out to be wrong by 60–160° on real frames whose true pointing a solve could confirm. so nothing user-facing is built on it — directions are absolute bearings computed from the solve
> - without GPS, location comes from the clock's UTC offset, which is ambiguous by a whole timezone (the offset fits both a standard-time and a DST meridian). so both are checked, and altitude is quoted as a *range* rather than a precision the data doesn't support
> - satellite tracks are drawn **dashed**, because they're computed from orbital elements, not detected in the pixels. streak detection is explicitly out of scope


### how it works: the nerdy details

> - **astrometry.net / `solve-field`** — the actual plate solver, running locally in the container (not the web service)
> - **FastAPI** — `POST /jobs` queues, `GET /jobs/{id}` polls, `/feed` is the homepage strip
> - **SQLite** as the job queue and the whole database. deliberately single-worker: `solve-field` is CPU-bound on one shared vCPU, so concurrency would just make every solve slower
> - **astropy** — parse the WCS (the pixel→sky mapping the solver produces) and project catalog coordinates into pixel space
> - **skyfield + JPL DE421** — Moon/planet positions, topocentric when there's GPS
> - **sgp4** (via skyfield) + **Space-Track** element sets — satellite propagation
> - **numpy + Pillow** — the pixel-level verification pass and the share card renderer
> - **Anthropic API** (Claude Haiku) — narration. sees the *label list*, never the photo
> - **frontend is one 700-line `index.html`** — vanilla JS, no framework, no build step. canvas overlay on top of an `<img>`
> - **docker compose** locally, **Fly.io** in prod: one machine running web + worker, `auto_stop_machines` so it sleeps when nobody's uploading. indexes + catalogs baked into the release image so machines stay stateless; only `/data` is a volume
> - **CI**: three tiers — node frontend logic tests, fast python tests, and a slow tier that runs real `solve-field` against synthetic star fields with known ground truth

*(end claude. back to me.)*

### the testing problem

While building this, I had an interesting problem: how do you test a website whose input is photos of the actual sky? Despite being an astrophotographer, I have very few photos of the night sky taken with my actual phone -- I had one blurry night sight attempt of orion years ago and not much else. And of course, when I was building this, it was either daytime, or cloudy. Fortunately, I found [a corpus of tons of pixel night sky photos](https://doi.org/10.5281/zenodo.14933725) that were perfect for testing. The downside: the CC BY-NC license means I couldn't commit it to my MIT-licensed project, so I couldn't actually use it for automated/CI testing. So in the interim before I went out and actually took some photos of varying quality to test both success/fail solving, I asked claude if we could simply generate synthetic star fields, which is [what we did](https://github.com/cwage/asterism/blob/92aafdd/tests/synth.py#L183)!

### what it's not

- It's not for proper astrophotographer -- images shot with a actual telescope would require the narrow-field solving needing the multi-GB index sets and stays out of scope
- It's not a streak detector: satellite tracks are computed
- It's not for hosting photos -- images/solves are retained for 24h, though I pinned a few of mine so there's always a handful of working examples (since probably no one will ever use this)
- [the honest "who will ever use this" bit, if you want the whoarewe-style ending]

### try it out!

- [https://asterism.quietlife.net](https://asterism.quietlife.net) — point your phone at the sky tonight and upload the result
- works best with an ordinary night-mode phone photo. handheld and a little hazy is fine; more stars = better
- [screenshot / annotated example goes here]
