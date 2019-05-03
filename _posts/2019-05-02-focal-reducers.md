---
post_id: 4249
title: focal reducers
author: cwage
layout: post
guid: http://quietlife.net/?p=4249
permalink: /2019/05/02/focal-reducers
categories:
  - Uncategorized
tags:
  - photography
  - focal reducer
---

A few years ago, I ran across an ad for a product: a "speed booster" lens adapter that promised to increase the 'speed' (effective light-gathering normally associated with the maximum aperture of the lens) by up to [1 full stop][1]. A popular example is the [Metabones adapter][2] for various cameras/lenses. It sounded, at first, like a scam. "How can you change the fundamental limits of a lens to be .. better? You can't, it makes no sense." I blew it off and moved on. It wasn't till I got into astrophotography that I started hearing talk of similar devices: "focal reducers", which increased the effective field-of-view (of a lens or telescope) and also gave a similar "speed" boost. Again, I was confused -- how is this possible? I couldn't blow it off this time (turns out they are fairly important for astrophotography), so I did some learnin' -- turns out it's not a scam! It's a real thing, and here's how it works:

First a quick review of a basic lens. This is a basic diagram of a converging lens from wikipedia:

<img src="/images/Lens1.svg" alt="simple converging lens" />

Where the rays of light converge at the focal point, the result is, of course, a circle of light -- the size of which depends on the lens design. Specifically, it depends on what sort of camera the lens is designed to work with: how large the sensor (or film plate) is and how far away from the lens it is. This circle is not perfect, of course -- light falls off gradually due to diffraction around the non-optical parts of the camera and lens (this, incidentally, is what causes [vignetting][3], at least when it's not being applied digitally by instagram). The result is something like this, with a rectangle representing the sensor the image circle is actually projected on:

<img src="/images/1024px-Image_circle.jpg" alt="image circle" />

With a well-coupled lens and camera, there's not much wasted light: the chosen rectangle of the sensor or film generally extends to the border of the light circle for the largest image possible without excessive vignetting in the corners. But! There are a lot of cameras and lenses out there -- and now more than ever. In the world of digital, cameras are getting smaller and lighter -- sometimes with reductions in the size of the actual sensor. You may be familiar with the term "crop sensor" -- a broad term for a variety of sensor sizes that are smaller than the standard 35mm film/sensor plane (e.g. APS-C). They are generally called "crop" sensors because they are smaller rectangles and, when used with a lens designed for a full 35mm frame, they effectively "crop" a smaller portion of the image. Naturally manufacturers also design lenses to match these smaller sensors, but people of course want to still be able to use their old lenses. So, often the result, when you use a lens designed for a full frame sensor with a smaller sensor, is a light circle projection like this:

<img src="/images/sensor-sizes-with-image-circle.png" alt="image circle with various sensors" />

Note that there's a lot of light being converged by the lense that is effectively "wasted" because it's outside the bounds of the sensor being used in the cases of the APS-C and 4/3" sensors. This part of the image circle projected by the lens falls not on the sensor, but on the back/sides of the camera, never to be seen again. This is where the voodoo comes in. If, say, you're using a Canon EF 200mm lens (designed for a 35mm sensor) on your fancy new micro 4/3" sensor camera -- obviously you already need an adapter to convert the mount and [flange distance][4] (the expected distance between the lens and the camera). What if you put an optical element in that adapter as well to further converge the light? This, effectively, is what a focal reducing "speed booster" is doing:

<img src="/images/metabones_mb_spom_m43_bm3_speed_booster_ultra_0_71x_1259766.jpg" alt="metabones speed boster" />

Think back to when you were a kid playing with a magnifying glass: you'll remember that converged light through the magnifying glass was warmer, right? The closer you move the magnifying glass to something (hopefully not an ant, you psychopath), the hotter it gets. The same thing (sortof) is at play in optics -- converging the light available (formerly 'wasted') on the smaller sensor makes it, effectively, brighter. So it's not changing anything fundamental about the limits of a lens, but is instead sortof 'reclaiming' otherwise wasted light the lens is converging for you.

So, there you have it -- not a scam or magic, but capitalization on otherwise imperfectly adapted gear!

[1]: https://en.wikipedia.org/wiki/F-number
[2]: https://www.bhphotovideo.com/c/product/1158844-REG/metabones_mb_spef_m43_bt4_canon_ef_micro_4_3_t.html
[3]: https://en.wikipedia.org/wiki/Vignetting
[4]: https://en.wikipedia.org/wiki/Flange_focal_distance
