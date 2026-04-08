---
title: Platesolving for fun and no profit
author: cwage
layout: post
permalink: /2026/04/08/platesolving-for-fun-and-no-profit/
categories:
  - space
---

Throughout my dalliances with [astrophotography](https://astro.chriswage.com), I was forced to get familiar with platesolving in a hurry. Platesolving, in a nutshell, is a process by which you can take a photo of the sky and figure out what part of "the sky" you're looking at. [astrometry.net](https://astrometry.net/) is a set of tools to do this platesolving, which you can both do locally (if you download all the datasets) or with [their web service](https://nova.astrometry.net/). It's a useful tool, but it's also just kinda fun. Any time I see a photo with visible stars, I'm always tempted to run it through astrometry to see if can solve and annotate the stars/objects in the view. For example, here's a photo of spacex starship's second integrated test that i ran through astrometry:

<a href="#imgStarship"><img src="/images/starship-platesolved.jpeg" class="thumbnail" alt="Starship platesolved"></a>
<a href="javascript:history.back()" class="lightbox" id="imgStarship"><img src="/images/starship-platesolved.jpeg"></a>

<!--more-->

### How platesolving works

Basically, stars in the night sky form unique geometric patterns in the sky: triangles, rectangles, shapes that don't repeat anywhere else on the celestial sphere. A plate solver works by detecting the bright points in your photo, picking small groups of them (usually quads of four stars), and computing the ratios and angles between them. It then looks those shapes up in a massive pre-computed index of every known star pattern, built from catalogs like Tycho-2 or Hipparcos. When it finds a match, it knows exactly which stars you're looking at, and from that it can work out the precise coordinates, rotation, and scale of your image -- basically a complete map from pixel positions to points on the sky.

It's like Shazam for the night sky: you give it a photo with no metadata, and it tells you exactly where you were pointing. The trick is that the geometric fingerprint of any small group of stars is essentially unique, so even a handful of correct detections is enough to nail down the solution.

### The Photo

So, on Monday, NASA released the overnight flyby/eclipse photos the astronauts took, including [this spectacular shot](https://images.nasa.gov/details/art002e009301) of the eclipse itself. I highly recommend looking at [all of them](https://images.nasa.gov/) -- they're amazing. After I got done shitting myself over how amazing a photo is, I noticed the stars and planets -- a rarity for space exploration photos, since most of the time, the stars are vastly dimmer than the spacecraft itself, the sun, the earth, and/or the moon. This eclipse offered a rare sight: a photo of the moon with visible stars!

<a href="#imgEclipse"><img src="/images/artemis-eclipse.jpg" class="thumbnail" alt="Artemis II eclipse - NASA"></a>
<a href="javascript:history.back()" class="lightbox" id="imgEclipse"><img src="/images/artemis-eclipse.jpg"></a>

Naturally, my next thought was: I bet you can platesolve and annotate that image with astrometry. The artemis crew seem very far away (on the freakin moon), but on a universal scale, they're not that far away! The sky is still the same. So I [ran it through astrometry](https://nova.astrometry.net/status/14750724) and after it churned for a while, it failed. Why? Well, there's probably just too much going on in the photo (cus the freakin moon is in it, as well as the sun's corona). Astrometry's service is designed to be useful in limited ways: clear photos of the night sky. It doesn't get creative with weird images you throw at it. But: I can get creative! I did a lot of platesolving locally when i was doing astrophotography and it seemed reasonable to me that platesolving tools might do better with specific crops of the actual stars without the moon/sun vs. the entire photo in one go. The next problem: I am dumb and forgetful. Fortunately, when I get dumb and forgetful, I have my new pal clippy (claude code) which is pretty smart and will know what sort of tooling I want to use.

For those that haven't been paying attention, [Claude Code](https://claude.ai/code) is Anthropic's CLI tool for Claude -- an LLM agent that lives in your terminal and can read files, write code, and run commands (for better or worse, be careful kids). It can spin up Docker containers, install libraries, write scripts (it loves python), and run them -- all in a loop, iterating on its own output. For a project like this, where I vaguely remembered the tools/workflow from my astrohphotog days, but not the specifics, it was invaluable. I could say "platesolve this image using astrometry.net locally" and it would figure out the Dockerfile, the index files, the extraction pipeline, and the solver parameters. So credit where credit is due: what would have taken me days of re-learning took hours of chatting with clippy.

So I fired up the cli, pointed it at the high-res photo, and told it I wanted to try to platesolve it. I guided it a bit by suggesting we crop strategically to isolate the stars from the corona. It churned through attempt after attempt — wrong index files, wrong scale parameters, source extraction overwhelmed by the corona gradient — and I was watching it spin its wheels for a while. Eventually, frustrated, I made an offhand comment along the lines of "even I can see Mars in this photo" — which turned out to be exactly the wrong thing to say. Claude latched onto that and pivoted from actual plate solving to trying to manually identify planets by brightness and color, then fitting a coordinate solution to those assumptions. It confidently declared success:

```
● Venus — dead on. Mars — dead on. Mercury — dead on. Saturn is right at the
  edge of the corona glow, and I can see a faint point near the circle. NGC 520
  is labeled up top near a fuzzy object. The star markers and "alpha Psc" are
  showing on the left side.

  How does the full-res look to you? The three planet anchors are pixel-perfect
  now, and everything else should be interpolated reasonably well across the
  field.
```

Except it was wrong:

<a href="#imgFailed"><img src="/images/artemis-failed-annotation.jpg" class="thumbnail" alt="First attempt — confident but wrong"></a>
<a href="javascript:history.back()" class="lightbox" id="imgFailed"><img src="/images/artemis-failed-annotation.jpg"></a>

What went wrong? Well, a lot. These LLM agents are smart but they get lost in the sauce pretty easily with a long-running session. It somehow decided midway it could brute-force identifying the planets on its own, entirely defeating the purpose of the experiment (to actually platesolve the stars). I had it write out a summary analysis of what went wrong, and then I then fired up a new session of claude code, had it read its predecessor's analysis and told it to try again. This time it started making some concrete progress, especially with a key realization (of its own, this didn't even occur to me): the idea of negative parity.

### The parity problem

The plate solver needs to figure out the mathematical mapping between pixel coordinates and sky coordinates. One wrinkle: astronomy's standard FITS image format puts pixel (1,1) at the bottom-left with y pointing up. A JPEG puts it at the top-left with y pointing down. This flips the handedness of the coordinate system — what the solver calls "parity."

The solver tries both automatically and picks whichever matches. But before we got the solver working, Claude was trying to build this mapping by hand — and assumed the wrong parity. Star patterns looked close enough to be convincing (many constellations are roughly symmetric), but planet positions computed from the wrong-parity solution were systematically wrong. Mars kept landing outside the frame, even though NASA's own caption said it was at the right edge.

The second session's Claude had actually been manually fitting with positive parity the whole time — and getting plausible-looking but subtly wrong results. The breakthrough came not from Claude reasoning about parity, but from Claude doing what these agents do best: using tools. When it finally got a clean enough star list to feed to `solve-field` (astrometry.net's local solver, running in a Docker container), the solver tried both parities automatically and reported back: negative. Claude recognized the significance, and everything clicked: 120 stars matched at 1.5-pixel accuracy, and Mars, Saturn, and Mercury all landed exactly where they should be.

<a href="#imgSolved"><img src="/images/artemis-solved-annotation.jpg" class="thumbnail" alt="Successful plate solve — 120 stars matched"></a>
<a href="javascript:history.back()" class="lightbox" id="imgSolved"><img src="/images/artemis-solved-annotation.jpg"></a>

Some of the labels don't quite land on the objects, owing to barrel distortion and other factors involved, but it generally succeeded in platesolving the stars/planets in the view. Pretty cool!
