---
post_id: 1587
title: animation
author: cwage
layout: post
guid: http://chris.quietlife.net/2007/04/04/animation/
permalink: /2007/04/04/animation/
ljID:
  - 754
dsq_thread_id:
  - 236781447
categories:
  - Uncategorized
tags:
  - animated
  - camera
  - gif
  - photography
  - pictures
---
In the comments on [the animated storm/lightning pic][1], [Rex][2] asked me to detail how I made it.. So here you go!:

<!--more-->

It was probably less complicated than you may think -- though some of the steps I took are sorta complicated, but they are unnecessary. I used my fancypants 20D, but there's not a lot that I did that I couldn't have done with my Powershot -- it just would have been a little slower and cumbersome.

### Step 1 -- Camera Placement:

This one's easy. Get a tripod, position it where you want it. Put the camera on it.

### Step 2 -- Camera Settings:

The whole animation was only around 23 frames, but each frame was a 30 second exposure. To take an exposure with your camera that long, obviously you have to change something, since an exposure that long would normally let in a blinding amount of light. This is accomplished by stopping down the lens (the aperture) sufficient that you get a decent amount of light over the 30 second period -- the light meter on your camera will tell you this. I operate in manual mode all the time, and you'll probably want to for this, as well -- or you can just set it to Exposure priority mode (Tv) and set to 30 seconds, or whatever you want, really. That's pretty much it.

There are also a few things I had to do, or opted to do, on my 20D that also facilitated this process. Some of these are optional or otherwise irrelevant, depending on your camera:

  * Turn on timed exposure mode -- unless you have a remote. I don't have a remote, so if I didn't do a timed exposure, the camera would be wobbling from me depressing the shutter. (This may not seem like a big deal, buit it can be.)
  * Turn on mirror-lockup. (Under the custom functions.) This isn't a huge deal, but it has two benefits: it locks up the mirror before opening the shutter -- this is because the mirror can vibrate slightly when the shutter opens simultaneously, reducing sharpness. More importantly, as a matter of coincidence, it also reduces the duration of the Canon firmware's timer from 10s to 3s, which was nice, since I had no reason to wait around.
  * Turn off the long-exposure noise reduction. As it turns out, this was important, because the way this noise reduction works is by taking an exposure of the equal amount of time, with the shutter closed, and then subtracting the result from the original. This is just a way to eliminate sensor noise. However, it means if you are taking 30 second exposures, you have to wait an additional 30 seconds until you can take a second exposure. That's 30 second gaps in between each frame, so that sucks for an animation.

### Step 3 -- Taking the Exposures:

This part is pretty easy. Hit the shutter. Wait. Hit the shutter again. Wait. Hit the shutter again. Wait. Etc. Staring off into space and contemplating the nature of your existence is optional (but recommended). Quit whenever you get bored, or think you have enough. I probably should have taken more, since the result was a bit short, but I didn't really have an animation in mind when I was taking them -- I was just trying to catch some damn lightning. Then again, like a good pop song, maybe the best animated GIF is short, always leaving you wanting more.

### Step 4 - Processing

Processing the individual pictures is all up to you, but really the goal is just to get the pictures into a GIF. I take pictures in Canon RAW format, so I had to convert them, but my photo processing software ([Bibble][3] -- best software ever) makes this pretty easy via batch processing.

Once I had the images, it was a simple matter of combining them into an animated gif of an appropriate size (you have to resize the final resultant animated GIF, since most people will not download a 50 megabyte animated GIF). Doing this [ImageMagick][4] (my swiss army imaging tool of choice) is a snap:

<pre>convert -resize 50% -loop 0 -delay 10 *.gif out/output.gif
</pre>

These arguments basically say to take all the GIFs (*.gif), resize them all 50%, loop 0 (infinitely) with a 1/10th of a second delay, and dump it into out/output.gif. This is where my workflow might deviate from the norm, since I exist in crazy Linux lala-land, so to do this next step in Windows you may need to find a tool to create an animated GIF. Although theoretically imagemagick probably runs fine under [Cygwin][5].

GIMP (and probably Photoshop) also lets you create an animated GIF from stacked layers, I believe.

Happy gifanimation!

 [1]: http://www.flickr.com/photos/cwage/445718983/
 [2]: http://www.rexblog.com/
 [3]: http://www.bibblelabs.com/
 [4]: http://www.imagemagick.org/
 [5]: http://www.cygwin.com/