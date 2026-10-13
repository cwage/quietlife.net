---
post_id: 4258
title: "comet hunting"
author: cwage
layout: post
guid: http://quietlife.net/?p=4258
permalink: /2026/10/13/comet-hunting/
categories:
  - tech
---

## tl;dr

So yeah. I found a comet! The weekend before last I ran across the [sungrazer project](https://sungrazer.nrl.navy.mil/) -- a neat little NASA-funded citizen science project run by the Naval Research Laboratory, soliciting the public to find [kreutz comets](https://en.wikipedia.org/wiki/Kreutz_sungrazer). There's a coronagraph on [GOES-19](https://en.wikipedia.org/wiki/GOES-19) -- a geostationary weather satellite -- that releases images publicly every 15 mins. It dawned on me that some of the techniques useful in astrophotography (stacking photos, frame subtraction, etc) might be applicable to detecting comets in these frames. Here's an animation of all the frames of this comet I tracked. It's faint, but it's there!

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A faint Kreutz sungrazing comet crossing the CCOR-1 field, 2026-10-08 21:15 to 2026-10-09 11:00 UTC. The yellow crosshair marks the comet.">
    <source src="/images/kreutz/first-catch-2026-10-08-field-soft.webm" type="video/webm" />
    <source src="/images/kreutz/first-catch-2026-10-08-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>The comet the detector found on its own, crossing CCOR-1's field toward the Sun (off to the left). The yellow crosshair marks it; the stars drift the other way. 2026-10-08 21:15 to 2026-10-09 11:00 UTC, 56 frames at 15 minutes each, about 14 hours.</figcaption>
</figure>

The bright flash in the middle is not aliens or a supernova, but rather glare from a period during which the earth actually eclipses the sun from the perspective of the instrument. Confirmation came for me when I saw that someone eventually [reported it](https://sungrazer.nrl.navy.mil/report/reporteb20261008225115) as well, though from CCOR-2, not CCOR-1 -- I beat them to it by around 4 hours!

The nerdy details:

<!--more-->

## the sungrazer project

So as mentioned above, the sungrazer project is a NASA-funded citizen science project run by the Naval Research Laboratory. It grew up around the coronagraphs on SOHO in the 90s, but these days most of the finds come from CCOR-1, a coronagraph aboard NOAA's GOES-19 weather satellite (and its sibling CCOR-2 on a different spacecraft). These instruments are [coronagraphs](https://en.wikipedia.org/wiki/Coronagraph) -- basically a camera with a disc mounted in the middle to block out the sun itself so that the corona and the area around it that would normally be blown out by the sun's glare are visible for study. As it happens, it's also quite useful for detecting comets at their perihelion around (or into) the sun! There's an entire family of such comets called the [Kreutz sungrazers](https://en.wikipedia.org/wiki/Kreutz_sungrazer) -- likely fragments from a large comet that broke up hundreds of years ago.

Amateurs have discovered thousands of comets via coronagraph data (most of those from SOHO; CCOR-1 had passed a hundred confirmed comets by late summer 2025, and hunters have been reporting dozens more a month from it since), most of them very small and faint. Some people use visual inspection, some use tools like GIMP (recommended on their site with a small tutorial), and others are clearly automating it (like I did) much more rigorously.

<figure>
  <a href="#imgRawFrame"><img src="/images/kreutz/ccor1-raw-frame.png" class="thumbnail half" alt="A raw CCOR-1 frame" /></a>
  <a href="#" class="lightbox" id="imgRawFrame"><img src="/images/kreutz/ccor1-raw-frame.png" alt="A raw CCOR-1 frame" /></a>
  <figcaption>A raw CCOR-1 frame: the occulter disc and its arm hide the Sun; the glow is sunlight scattered off interplanetary dust. Comets are invisible at this stretch.</figcaption>
</figure>

## how it works

So CCOR-1 publishes a 2048 x 1920 calibrated frame every 15 minutes. Anyone is free to do whatever they like to figure out if there's a comet in the frame. Obviously comets move, so this typically involves comparing repeated frames as they're published by NOAA. But there's a lot of "stuff" in every frame: dust glow, the disc (occulter), stars, and of course the sun's corona itself. In my experience with astrophotography, there are a lot of steps necessary when processing imagery before stacking to remove defects, dustmotes, noise from the camera, etc. so that this stuff doesn't stack alongside the stars and galaxies resulting in garbage. Much of that process involves taking various forms of photos (so-called "flat", "bias" and "dark" frames) so you can average them together and subtract (or divide) them out of the actual light frames. It dawned on me that a similar approach could work here to remove that stuff (except here the "calibration frame" is just the median of the last few hours of real frames, since anything that holds still for four hours isn't a comet) and then look for point-sources of light that are clearly not stars but still moving from frame to frame.

So I fired up claude code (as one does), pitched the idea and told it to get to work. The first task was building out some detection tooling but then running it on the archive of historical CCOR-1 frames (checked against sungrazer's old reports) to make sure it even worked at all. There were a lot of false positives for a variety of reasons, but when we were done, this is the high-level workflow:

The detector looks at a sliding window of the last N frames (where N = 8 currently) and then attempts to identify anything moving in a way that a Kreutz comet moves:

1. Subtract all the relatively static stuff in the frame: the corona, the dust glow, the occulter itself. This is easy enough to do: take the median of the previous 16 frames (~4 hours of time) and subtract it.

2. Get rid of the stars -- they drift across the frame together (around 2 pixels per frame, but it varies), so each of the previous eight frames is aligned to the current frame by matching a few hundred stars, combined into a model of the star field, and subtracted. Whatever's left of the stars gets masked out (4 pixel radius).

3. Now that the stars are gone, we can get rid of everything else that's not a dot (since a comet in any given frame is just gonna be a dot): difference-of-Gaussians filter (1.2 pixel core, 4 pixel surround) keeps point sources and nukes anything else (coronal streamers, rays, etc).

4. Shift and stack. Any potential comet is too faint to see in any one frame, but it moves in a straight line. So the detector picks a speed and direction, slides each frame back by that amount and "stacks" them -- if the speed is right, the comet "dot" will be in the same place in every frame, increasing the intensity. If not, it tries another speed, iterating over a range of speeds pre-calculated on the backlog of historical Kreutz comets.

5. Next we just look at the next few batches of frames for the suspect comet (dot) where it should be at the given speed. Three in a row makes it a candidate, unless it moves with the stars (a star the model missed), doesn't move at all, or is heading somewhere Kreutz comets don't go.

6. Confirmed once we have 5 frames of movement.

<figure>
  <img src="/images/kreutz/strip-bright-comet.png" alt="A vetting strip for a real comet" />
  <figcaption>How candidates get vetted by eye: each tile is a crop that moves with the candidate's predicted motion (raw on top, significance below). A real object sits still in the middle while stars slide past.</figcaption>
</figure>

So how well does it work? I ran the tooling over a range of historical data from Jul 17-Jul 24, 2025 with 8 confirmed CCOR-1 comets, all of which were found by our detector. Six of the eight were (or would have been) detected before the date/time of the human submission, ranging from 17 mins to 4.5 hours ahead; the other two it found late, an hour or two after the human report. The more that I've stared at this data and watched this detector report potential comets, I've noticed they're often already submitted, or submitted very quickly after our tool detects it. These hunters are thorough! I'm also fairly confident the top hunters are automating it in a similar fashion as I am. One in particular that my tooling caught was reported within 4 mins of NOAA releasing the last frame needed for confirmation, which makes me think they're not only automating the search but in some cases automating the form submission.

I didn't submit mine because I was (and still am) kicking the tires on this, and I want to be super careful not to send noise/garbage their way (and i'm not approved yet). Still fun though!

And because I'm a huge nerd, I also built a live dashboard so I can look at the current candidates being tracked, false positives, objects that faded, etc:

<figure>
  <a href="#imgDashboard"><img src="/images/kreutz/dashboard-2026-10-13.png" class="thumbnail half" alt="The kreutz live status dashboard" /></a>
  <a href="#" class="lightbox" id="imgDashboard"><img src="/images/kreutz/dashboard-2026-10-13.png" alt="The kreutz live status dashboard" /></a>
  <figcaption>The live status page: what's being followed and at which stage, who reported it first, and the recent decisions.</figcaption>
</figure>

## the code

I'm still kicking the tires on it, but I'll probably throw the source up on github once it's closer to "done" eventually and link it there. brief summary of the tools used, though:

- **Plain Python**, about 3,700 lines across 18 modules: numpy and scipy do the image work, astropy reads the FITS frames and their pointing info, pillow makes the GIFs. There's an optional torch path that runs the shift-and-stack on the GPU and falls back to numpy without it.
- **Everything runs in Docker.** Each container is capped at 1.5 CPUs with single-threaded math libraries, so several searches can run side by side at a predictable load instead of all of them fanning out across every core. GPU is opt-in via a compose override.
- **Data in, data out.** Frames come from NOAA's archive (for history) or its real-time feed (for live), about 880 MB a day. Sungrazer's report pages get scraped into a local file and serve as the answer key: every track the detector finds is checked against them.
- **Archive tooling**: fetch a span of days, search it, score the results against the reports (what would have been found, and how early), and build contact sheets of the unexplained candidates for vetting by eye.
- **The live watcher**: polls the feed, searches each new window as it lands, vets anything that fires, follows it frame by frame, and once it's confirmed writes out the block of times and positions that Sungrazer's report form wants. It pings my phone via ntfy at the candidate and confirmed stages, saves its state after every window so a restart picks up where it left off, and rewrites the status page above.
- **Pictures**: a renderer follows a comet through the frames and writes the aligned cutouts as FITS cubes, and a separate styler turns those into animations. All of the comet videos here came out of that.
- A small test suite and CI, mostly so claude couldn't break the coordinate conventions without noticing.

## other people's comets

For fun, here are some renderings of some other already-reported comets:

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A bright Kreutz comet with a tail crossing the CCOR-1 field, 2026-09-15 23:30 to 2026-09-16 15:45 UTC">
    <source src="/images/kreutz/comet-2026-09-16-field-soft.webm" type="video/webm" />
    <source src="/images/kreutz/comet-2026-09-16-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>The bright one from September that I used for testing early on: head and tail, 2026-09-15 23:30 to 2026-09-16 15:45 UTC, 61 frames. Reported from CCOR-1 by <a href="https://sungrazer.nrl.navy.mil/report/reportbc20260916012011">Bill Collins</a> (posted 05:20 UTC) and from CCOR-2 by <a href="https://sungrazer.nrl.navy.mil/report/reportjr20260916030908">Jiangao Ruan</a> (07:09 UTC).</figcaption>
</figure>

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A Kreutz comet crossing the CCOR-1 field, 2026-10-06 11:45 to 23:45 UTC">
    <source src="/images/kreutz/comet-2026-10-06-field-soft.webm" type="video/webm" />
    <source src="/images/kreutz/comet-2026-10-06-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>The first real comet the live watcher caught, 2026-10-06 11:45 to 23:45 UTC, 49 frames. <a href="https://sungrazer.nrl.navy.mil/report/reporteb20261006085434">Eryk Banach had reported it</a> from CCOR-2 at 12:54 UTC, about an hour and a half before the detector flagged it.</figcaption>
</figure>

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A non-Kreutz comet entering the CCOR-1 field from the left, 2026-10-11 12:30 to 2026-10-12 03:00 UTC">
    <source src="/images/kreutz/comet-2026-10-11-field-soft.webm" type="video/webm" />
    <source src="/images/kreutz/comet-2026-10-11-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>Not a Kreutz: a known comet entering from the other side of the field, 2026-10-11 12:30 to 2026-10-12 03:00 UTC, 59 frames, <a href="https://sungrazer.nrl.navy.mil/report/reportms20261011134716">reported by Michael Stark</a> from CCOR-1.</figcaption>
</figure>
