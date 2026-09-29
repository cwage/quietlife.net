---
post_id: 4256
title: "Claude and the moon"
author: cwage
layout: post
guid: http://quietlife.net/?p=4256
permalink: /2026/09/29/claude-and-the-moon/
categories:
  - tech
---

Last Thursday, I got a bit of bad news, so decided to deal with it as I normally do -- poured a glass of bourbon and went to go stare at the stars. The only problem? The moon was up, shining bright, waxing gibbous. So I decided to point a camera at it, instead. Despite being an avid photographer and astrophotog (once upon a lifetime), i don't actually have a particularly good setup for shooting the moon. I realized i did have an old sigma 600mm reflex (mirror) lens and after scrambling through half a dozen adapters I got it rigged up to my camera and started shooting. My impulse (laziness) was to just take a video and stack the frames -- a strategy called "lucky imaging", which is primarily advantageous for atmospheric turbulence (more on this later, highly relevant). So I took a [few videos](https://x.com/cwage/status/2103307761975267515) that are fairly enjoyable, but being paranoid I took a few bracketed exposures as well (also relevant).

Once I finished the fun part -- staring at the sky, enjoying the nice weather, pressing a shutter button every 30 seconds -- I got to the more annoying part: sitting at a computer and loading the usual tools and doing the processing. It's been a while since I did any planetary body image processing, so I was rusty.. I vaguely recalled [PIPP](https://sites.google.com/site/astropipp/) and [autostakkert](https://www.autostakkert.com/), and even how to do it the hard (but superior) way in [pixinsight](https://pixinsight.com/). But it occurred to me: you know who is really good at shit like this? clippy. So I fired up [claude code](https://code.claude.com/) and got to work. And it did great! Eventually. But first, the result:

<a href="#imgHero"><img src="/images/moonstack/17-night1-as-posted.jpg" class="thumbnail" alt="Night 1 result as posted: 6 raw stills, RL40 deconvolution, toned in darktable"></a>
<a href="#" class="lightbox" id="imgHero"><img src="/images/moonstack/17-night1-as-posted.jpg" alt="Night 1 result as posted: 6 raw stills, RL40 deconvolution, toned in darktable"></a>

Not bad for a very blurry 40 year old reflex lens with a fixed aperture! And now, the gory details:

<!--more-->

So, as mentioned, I was familiar with some of the tooling to do this in the past, so I asked claude if that was still the right/best option and it instantly pointed me at [Planetary System Stacker](https://github.com/Rolf-Hempel/PlanetarySystemStacker) which would be perfect for this. We fired up a new project with a docker container to do the needful on arbitrary inputs and gave it a go. Most of the initial results weren't great -- no better than what a single frame from the video looked like. Claude's (as it turns out, incorrect) assessment at the time:

> The stack has exactly the detail of a single frame with a quarter of the noise. It is not sharper, and I was wrong earlier when I said it was. The wavelets then amplify what's there, which is why the sharpened versions look "processed" without looking more resolved.
>
> Why stacking can't add resolution here. The moon is 1900 arcseconds across and 557 pixels in the 4K frame, so each pixel covers about 3.4 arcseconds. Typical seeing blur is 2 to 4 arcseconds. Your sampling is coarser than the seeing, so the atmosphere barely changes one frame to the next, and every frame is equally soft. Lucky imaging only works when some frames are sharper than others, which needs sampling of well under an arcsecond per pixel. That takes roughly 5 to 10 times the focal length: a small telescope in the 1500 to 3000 mm range, or a Barlow on the mirror lens. At 400 to 600 mm on a 12 MP full-frame sensor, single frame and stack are the same picture. The video looks as good as the stack because it is as good as the stack.
>
> What's actually worth doing with this data: take the unsharpened stack for its clean noise floor, apply mild sharpening, and stop.

Sounds convincing, right? Don't worry if you don't understand what any of it means (i barely do, myself). Basically claude was saying this is as good as it's gonna get. The problem is that it was wrong (which it later figured out). Lucky imaging wasn't doing anything for us because the seeing was at least good enough that it wasn't the real thing to fix.

I got a little dismayed at this point, but also somewhat unconvinced. Instead of using my own brain (I did mention there was bourbon involved), I just cranked fable 5.1's thinking to max effort and told it to try again:

> idk i'm not satisfied. these all look like garbage. please purge everything you've produced except the originals. there's so much more we can pull out of these pixels, between stacking and HDR

This is the part where claude (fable specifically) did what it's best at: completely abandoning any pre-existing software and writing python. But first it did what we should have done from the beginning and measured the actual blur off the moon's edge. Once the real problem (blur from the lens) was clear, the solution was as well, and it didn't involve the video at all -- the bracketed individual exposures were what we wanted:

1. **[dcraw](https://dechifro.org/dcraw/)** (a shell one-liner): decode the 14 raw ARW files to linear 16-bit PPMs, no white balance, no color matrix, so the numbers are the sensor's actual numbers.
2. **`frame_quality.py`**: measure the width of the moon's edge in every frame. This is what caught the eight frames smeared by shutter shock; they were excluded.
3. **`hdr_stills.py`**: line up the remaining six by fitting a circle to the moon's edge, average them weighted by exposure, and nudge the red and blue channels to match green.
4. **`psf_deconv.py`**: measure the edge profile of that merge, fit a blob shape (Moffat) to it, and run Richardson-Lucy deconvolution at 10/20/30/40/60 iterations on the black-and-white version, picking 40 by an overshoot-and-noise rule.
5. **`deconv_rgb.py`**: run the same 40 iterations on each color channel and write a 16-bit linear TIFF.
6. **[darktable](https://www.darktable.org/)**, by me: black point, contrast, sharpening.

Hilariously, even after claude had long-ago abandoned the video, I thought we were still using frames from it. (again: bourbon)

<a href="#imgBeforeAfter"><img src="/images/moonstack/22-before-after-mild-vs-rl40-1to1.png" class="thumbnail" alt="Before and after: video stack with mild sharpening vs six raw stills deconvolved, 1:1 pixels"></a>
<a href="#" class="lightbox" id="imgBeforeAfter"><img src="/images/moonstack/22-before-after-mild-vs-rl40-1to1.png" alt="Before and after: video stack with mild sharpening vs six raw stills deconvolved, 1:1 pixels"></a>

### Philosophizin'

This was a small experiment, but it's part of a larger trend (that i'm not remotely the first to notice, of course). We increasingly live in a world where anyone sufficiently motivated person can build their own software. I guided claude here and there with technical and photography expertise of my own, but not much. I feel pretty confident that if someone less experienced but at least knew stacking was a thing and had claude code (or codex, or whatever), they could have pulled this off (possibly with fewer wrong paths, because my expertise is what got us into trouble at first). If the software is open source, [you can change/fix it](https://x.com/cwage/status/2096686511060066427). If the binaries can be decompiled or whatever, you can change it.

This process could have been done by me with PIPP, registax, autostakkert and other tools, but it would have taken me hours just to remember the steps, how each tool's GUI works, etc. Instead I was able to reproduce the results in an hour (not counting the time for the meat interface -- me -- goin out to point the camera at the moon). The aforementioned tools are relatively small/niche (and free or OSS), but there's a truly powerful piece of software called pixinsight -- not cheap at around ~$300 -- for astrophotography, and I feel pretty confident that an even more sufficiently motivated could piecemeal recreate it with an LLM coding agent.

Just in the last few weeks, I:

- got annoyed at the fixed font size of my [xteink x3](https://x.com/cwage/status/2095365427081687378) ereader, and it dawned on me that I already had an alternative (OSS) firmware on it, so I had claude recompile a version with larger fonts in about 10 mins.
- Valheim 1.0 came out and, as happens with any update, most of my favorite QoL mods broke. Usually it takes days to weeks for the various mod authors to get their mod updated -- I fired up claude and had all 30 of my mods updated and working in around 20 mins.
- While playing Valheim later I had a "it would be nice if" moment for a feature the game lacked. 10 mins later I had a functioning mod installed and working.

The future is wild.

There's also an interesting lesson in how/how not to use these agents. I originally set the tone that led down the wrong lucky imaging path by specifically mentioning the video, and it kept iterating on lucky imaging techniques -- techniques that don't really buy us anything here. It's a good lesson that LLMs will dutifully do what you ask and that the longer a session goes, the past session context means they will continue marching down that wrong path.
