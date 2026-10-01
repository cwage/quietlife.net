---
post_id: 4257
title: "aistrophotography"
author: cwage
layout: post
guid: http://quietlife.net/?p=4257
permalink: /2026/10/01/aistrophotography/
image_comparison: true
categories:
  - tech
---

AIstrophotography, get it! ahem, anyway.

The other night, while working on [this moon shenanigans](https://quietlife.net/2026/09/29/claude-and-the-moon/), I had a passing thought (mentioned in that post as well): how much of my astrophotography workflow in pixinsight could I task clippy with automating?

So, I fired up claude code (model Fable 5.1 in xhigh thinking mode) and gave it the parameters: a handful of folders with past imaging session data of mine (either RGB sony pics or mono LRGB image sets ready to be stacked) on my NAS and a github repo. As it happens, pixinsight's project file format actually keeps a history of each step done to the data to reach the final product, so the natural progression would be to delineate all the steps I did in pixinsight and automate it. This was the most hands-off vibecoding session I've ever done (mostly cus it was late and i wanted to go to bed). I told it to create issues on the repo for every step we need to automate/recreate and asked it to iterate on each one till it was done and went to bed.

When I woke up in the morning, it had stopped (because my screensaver kicked in, which purges my ssh key, cutting off its access to github -- "security first!" says the guy that handed clippy the keys and went to bed). I had it pick up where it left off and then had it run the full workflow on two targets:

- [My first (terrible) attempt at M13](https://app.astrobin.com/i/366417)
- [A less terrible attempt at M81](https://app.astrobin.com/i/396206)

Without exaggeration, it basically one-shot it (pun intended!):

<!--more-->

<figure class="comparison-wrapper">
  <div class="js-comparison-container">
    <img class="comparison-image" src="/images/aistrophotography/m13_compare_quietsky.jpg" alt="quietsky" />
    <img class="comparison-image" src="/images/aistrophotography/m13_compare_pixinsight.jpg" alt="PixInsight" />
  </div>
  <figcaption>M13, Sony A7S II, 43 x 30 s. left: quietsky, auto-stretched, no color calibration. right: original PixInsight processing</figcaption>
</figure>

<figure class="comparison-wrapper">
  <div class="js-comparison-container">
    <img class="comparison-image" src="/images/aistrophotography/m81_compare_quietsky.jpg" alt="quietsky" />
    <img class="comparison-image" src="/images/aistrophotography/m81_compare_pixinsight.jpg" alt="PixInsight" />
  </div>
  <figcaption>M81, ASI1600MM R+G+B, 20 x 120 s each. left: quietsky, auto-stretched, no color calibration. right: original PixInsight processing</figcaption>
</figure>

In some ways its results are better, though for M13 its background extraction left a lot of noise and dust motes, which I "solved" by just dropping detail like crazy (I was fighting a losing battle against weird noise/artifacts from my Sony at the time).

One concern I had was that in claude's iteration overnight it may have diverged from the actual goal of a generalized tool and onto "just recreate a flow that works for cwage's shitty data". So just to kick the tires, I snagged some RGB data of M13 from the [MOANA data](https://erellaz.com/moana/open-datasets/) and set it to work on those images (much better quality than anything I ever did or will take):

<a href="#imgMOANA"><img src="/images/aistrophotography/moana_m13_full.jpg" class="thumbnail" alt="M13 from the MOANA project, 252 x 60 s RGB, quietsky"></a>
<a href="#" class="lightbox" id="imgMOANA"><img src="/images/aistrophotography/moana_m13_full.jpg" alt="M13 from the MOANA project, 252 x 60 s RGB, quietsky"></a>

And for fun, a comparison of the core between my shitty sony and a 200mm lens vs. proper gear and dark skies:

<a href="#imgCompare"><img src="/images/aistrophotography/comparison_sony_vs_moana.png" class="thumbnail" alt="The two M13s at the same angular scale: Sony A7S II at 200mm vs MOANA at 254mm"></a>
<a href="#" class="lightbox" id="imgCompare"><img src="/images/aistrophotography/comparison_sony_vs_moana.png" alt="The two M13s at the same angular scale: Sony A7S II at 200mm vs MOANA at 254mm"></a>

So, I haven't actually answered the "how much could I replace" question, but what claude did overnight was pretty impressive. It's a tiny fraction of what pixinsight is capable of, and recreating it into a cli would defeat the purpose, because basically all the work done aside from the actual integration is highly subjective/creative where you need visual feedback. It was still a fun experiment though!

The repo is [up here](https://github.com/cwage/quietsky) -- if there are any astrophotographers out there that wanna play around with it, give it a go! It should Just Work in docker. Have fun!
