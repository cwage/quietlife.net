---
post_id: 4259
title: "comet hunting, part two"
author: cwage
layout: post
guid: http://quietlife.net/?p=4259
permalink: /2026/10/31/comet-hunting-part-two/
categories:
  - tech
---

A few weeks ago I wrote about [building a comet detector](/2026/10/13/comet-hunting/) for the [Sungrazer Project](https://sungrazer.nrl.navy.mil/) and finding my first Kreutz sungrazer in CCOR-1's frames. Over the last few weeks I expanded it to cover three new instruments: CCOR-2, and LASCO C2 and C3. This was kinda neat not only because it meant more candidates to find but also because I could cross-check candidates between them. I also got approved to officially report them on the site! Along the way I ran into a lot of problems: false positives, mostly. Clippy and I spent a lot of time ruling out obvious artifacts or other things showing up in frames that the detector thought might be a candidate, and carving out rules/vetoes for them.

Here's probably the coolest pair of animations -- the same comet identified via CCOR-1 and CCOR-2:

<figure class="pair">
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A Kreutz comet crossing the CCOR-2 field, 2026-10-22 23:45 to 2026-10-24 02:45 UTC">
    <source src="/images/kreutz/ccor2-2026-10-23-field-soft.mp4" type="video/mp4" />
  </video>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="The same Kreutz comet crossing the CCOR-1 field, 2026-10-23 08:00 to 2026-10-24 05:15 UTC">
    <source src="/images/kreutz/ccor1-2026-10-23-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>The same comet from two vantage points. Left: CCOR-2, from the Sun-Earth L1 point, 2026-10-22 23:45 to 2026-10-24 02:45 UTC, 106 frames. Right: CCOR-1, from geostationary orbit, 2026-10-23 08:00 to 2026-10-24 05:15 UTC, 86 frames. Reported by me from <a href="https://sungrazer.nrl.navy.mil/report/reportcw20261022213630">CCOR-2</a> and <a href="https://sungrazer.nrl.navy.mil/report/reportcw20261023091620">CCOR-1</a>.</figcaption>
</figure>

The details:

<!--more-->

## what changed

The [first post](/2026/10/13/comet-hunting/) covered the basic idea: subtract everything in the frame that's stationary, subtract the stars, look for dots, then shift/stack the last eight frames along every plausible comet velocity to see what adds up. A lot of the work since then was eliminating the false positives:

**False positives**: hot pixels, stray sunlight from eclipse season, cosmic rays, passing satellites or glint from them, etc.

**Orbits.** This was a neat one. These comets aren't just moving in roughly the same direction, they're literally on nearly the same orbit (roughly the same orbit as the parent they originally broke apart from). So we added a model that takes an actual orbit, puts it in the sky as seen from wherever the instrument is, and projects it onto the frame. That gives us three things. First, a second search that stacks frames along the curve of a Kreutz orbit. Second, matching other hunters' reports to our tracks by asking whether one orbit passes through both, instead of drawing a straight line through their handful of points. Third, matching across instruments, so the CCOR-1 watcher knows when a CCOR-2 report is about the comet it's following and vice versa (that's how the two videos at the top were tied together: their fitted orbits agree on the time of perihelion to within five minutes).

As mentioned above, I also added a few more instruments:

- *CCOR-2*, CCOR-1's sibling on the SWFO-L1 spacecraft, parked at the Sun-Earth L1 point. Same camera design, same cadence, but the data is released at a less-processed level.
- *LASCO C2 and C3*, the coronagraphs on SOHO (a joint ESA/NASA solar observatory), which has been doing this since 1996 and is where most of the Sungrazer Project's comets have come from. Different cadence (12 minutes, often irregular), a spacecraft that flips upside down every few months, and a field so wide (C3) that where comets come from swings around through the year, so the search has to know what time of year it is. In testing, the search found every reported comet bright enough to see.

We built it out so that each instrument gets its own watcher.

## the comets

### reported by me!

The pair at the top is the same comet in both CCOR instruments. The CCOR-2 watcher alerted at 01:15 UTC on October 23 and I filed [the report](https://sungrazer.nrl.navy.mil/report/reportcw20261022213630) about twenty minutes later; it was later endorsed by Robert Pickard. The CCOR-1 watcher picked it up at 11:00 UTC, about ten hours later, and I [reported that too](https://sungrazer.nrl.navy.mil/report/reportcw20261023091620). Chuck Fields had it in LASCO C3's much wider field; his C3 observations posted about ten and a half hours after my CCOR-2 report.

Then on October 26, another one:

<figure class="pair">
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A Kreutz comet crossing the CCOR-1 field, 2026-10-26 16:45 to 2026-10-27 10:30 UTC">
    <source src="/images/kreutz/ccor1-2026-10-26-field-soft.mp4" type="video/mp4" />
  </video>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="The same comet entering the CCOR-2 field, 2026-10-26 21:30 to 2026-10-27 04:45 UTC">
    <source src="/images/kreutz/ccor2-2026-10-26-entering-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>October 26. Left: CCOR-1, 2026-10-26 16:45 to 2026-10-27 10:30 UTC, 72 frames. The watcher alerted at 18:07 UTC and <a href="https://sungrazer.nrl.navy.mil/report/reportcw20261026142456">my report</a> posted at 18:24, endorsed by Eryk Banach. Right: the same comet arriving in CCOR-2, 2026-10-26 21:30 to 2026-10-27 04:45 UTC, 30 frames, filed as a <a href="https://sungrazer.nrl.navy.mil/report/reportcw20261026190428">Known Comet Now Entering</a>. The CCOR-2 watcher matched it to the CCOR-1 report by orbit on its own.</figcaption>
</figure>

I filed one more on October 29: a faint one on CCOR-1 that the watcher alerted on at 22:32 UTC. I measured it back an hour or so by hand and [filed it](https://sungrazer.nrl.navy.mil/report/reportcw20261029184227) ten minutes later, with a [matching entry](https://sungrazer.nrl.navy.mil/report/reportcw20261029184632) for CCOR-2. Worachate Boonplod endorsed it. It faded below what the watcher could follow shortly after, so there's no animation of that one.

### detected first, before I could report

Two comets the watcher found ahead of the eventual reporter, while I was still waiting on approval:

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A Kreutz comet crossing the CCOR-1 field, 2026-10-21 10:00 to 17:15 UTC">
    <source src="/images/kreutz/ccor1-2026-10-21-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>October 21, CCOR-1, 10:00 to 17:15 UTC, 30 frames. The watcher alerted at 11:18 UTC and confirmed at 11:33; <a href="https://sungrazer.nrl.navy.mil/report/reportjr20261021075102">Jiangao Ruan's report</a> posted at 11:51. It ran 273 pixels from any comet in the archive, so the watcher held the first alert as too far off the usual path and only paged me at confirmation.</figcaption>
</figure>

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A faint Kreutz comet crossing the CCOR-1 field, 2026-10-15 00:00 to 07:00 UTC">
    <source src="/images/kreutz/ccor1-2026-10-15-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>October 15, CCOR-1, 00:00 to 07:00 UTC, 29 frames. Alerted at 01:15 UTC, 16 minutes before <a href="https://sungrazer.nrl.navy.mil/report/reportnu20261014213108">a new user's report</a> posted at 01:31; the confirmation came about an hour after that.</figcaption>
</figure>

### LASCO

The LASCO watchers have only been running since October 23. All three were reported from another instrument around the same time or earlier, but in each case the watcher had them before the C2 report was filed:

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A Kreutz comet crossing the LASCO C2 field, 2026-10-24 03:48 to 08:00 UTC">
    <source src="/images/kreutz/c2-2026-10-24-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>October 24, LASCO C2, 03:48 to 08:00 UTC, 20 frames. A bright one, and as far as I can tell the same comet as the pair at the top, in its last hours before perihelion. Alerted about 6.8 hours before <a href="https://sungrazer.nrl.navy.mil/report/reportcf20261024072819">Chuck Fields' C2 report</a>, though he had already reported it from C3 the day before.</figcaption>
</figure>

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A Kreutz comet crossing the LASCO C2 field, 2026-10-25 07:12 to 09:48 UTC">
    <source src="/images/kreutz/c2-2026-10-25a-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>October 25, LASCO C2, 07:12 to 09:48 UTC, 13 frames. The watcher's alert and <a href="https://sungrazer.nrl.navy.mil/report/reportgc20261025045450">Gioele Cerati's CCOR-2 report</a> of the same comet landed within three minutes of each other; <a href="https://sungrazer.nrl.navy.mil/report/reportcf20261025182113">Chuck Fields' C2 report</a> came 13.5 hours later.</figcaption>
</figure>

<figure>
  <video autoplay loop muted playsinline controls preload="metadata" aria-label="A Kreutz comet crossing the LASCO C2 field, 2026-10-25 19:36 to 23:48 UTC">
    <source src="/images/kreutz/c2-2026-10-25b-field-soft.mp4" type="video/mp4" />
  </video>
  <figcaption>October 25, LASCO C2, 19:36 to 23:48 UTC, 21 frames. <a href="https://sungrazer.nrl.navy.mil/report/reportmk20261025150502">Mikolaj Kaszczyk had reported it</a> from CCOR-2 almost two hours before the alert; <a href="https://sungrazer.nrl.navy.mil/report/reportcf20261025182736">Chuck Fields' C2 report</a> came about an hour and a half after.</figcaption>
</figure>


## the code and a funny coda

I went ahead and made the [code public](https://github.com/cwage/kreutz) -- feel free to try it on your own! I originally waffled on making the code public at all. The sungrazer project is a NASA-funded citizen science/outreach project -- part of the point, obviously, is to get people interested in astronomy and science in the process of participating in it. I didn't wanna be the nerdlinger blasting out a repo of code that lets anyone automate it, much less be that guy. But the more time I spent watching the reports come in, the more it became clear that others were automating it already -- reports landing on the site sometimes within minutes of the data. Nevertheless, I demurred and kept it private and wrote the original post. In the process of discussing these concerns with claude (don't judge me), it occurred to me that it's really kinda moot -- with the post up detailing the goal and strategy, anyone (like me) with claude code and a few hours could probably replicate it. Skip forward a week, and a friend of mine sends me a screenshot of what looked exactly like the web UI I built, showing a candidate confirmed but already reported by "Chris Wage":

<figure>
  <img src="/images/kreutz/scotts-status-row-2026-10-26.png" alt="A status-page row from a friend's copy of the detector: CCOR-1, candidate with 10 frames measured, reported by Chris Wage 10-26 18:24 UTC, found here 18 minutes before the report" />
  <figcaption>His watcher's status row for the October 26 comet: found 18 minutes before my report.</figcaption>
</figure>

At first I was like "oh cool you're running it as well?" before getting confused, like "... wait, my code isn't public yet." Turns out he had proactively done precisely what I reasoned about above -- he took my original blog post, pointed claude code at it and said "build this". And [it did](https://github.com/scottholdren/sungrazer) -- minus all the refinements I spent the last few weeks doing as detailed above, but nonetheless succeeded. What a world.
