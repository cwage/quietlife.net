---
post_id: 1442
title: HDR and Tonemapping in Linux
author: cwage
layout: post
guid: http://chris.quietlife.net/2006/09/06/hdr-and-tonemapping-in-linux/
permalink: /2006/09/06/hdr-and-tonemapping-in-linux/
ljID:
  - 612
dsq_thread_id:
  - 236780865
categories:
  - Uncategorized
tags:
  - digital
  - hdr
  - high-dynamic-range
  - pfstools
  - photography
  - tonemapping
---
I thought I'd write up my workflow for mucking around with HDR and Tonemapping in Linux. Actually, come to think of it, though, most of this software would probably work fine in Windows (pfstools being the toughest, but I bet it works fine in cygwin). But first, a point of clarification in definitions: most people associate HDR with tonemapping, but they aren't the same thing:

HDR stands for [High Dynamic Range][1], and it's a process by which you can combine multiple exposures into one image that contains more dynamic range than one exposure would normally contain. These images need to be displayed on equipment that can display the range, or they need to be .. tone-mapped:

[Tone-mapping][2] is a process by which the high dynamic range is converted to a standard low-dynamic range image. There are many algorithms to accomplish this, and they all have different effects -- some realistic, and some not. (Some prefer to call it hyperreal or surreal. Whatever.)

I was loathe to write this up, since I haven't really produced anything that phenomenal, but I do have some tricks up my sleeves that other people with more photographic skill might find useful:

<!--more-->

## Equipment

You need a camera. A camera that will do bracketed exposures is nice, but not strictly necessary -- especially if you're, uh, really patient. A tripod will come in handy, but is also not strictly necessary (more on this later). I use a Canon EOS D30 DSLR, and I sometimes lug around a tripod. Nothing fancy.

## File Format

I shoot in Canon RAW format (the debate on the merits of this is a whole other story), but you can do JPG or RAW, really. I do RAW because I like it for other purposes, and three exposures of RAW actually have a little bit more range than JPG alone, since the RAW format is a little more dynamic than JPG alone to begin with.

## Software

  * [Bibble Lite][3] - excellent software for processing RAW files.
  * [pfstools][4] - command-line HDR software.
  * [pfstmo][5] - command-line tone-mapping algorithms for use with pfstools
  * [autopano][6] -- automatic panoramic stitching points generator. <span style="color: red;">*</span>
  * [hugin][7] -- panorama stitching software. <span style="color: red;">*</span>
  * [HDRShop][8] -- HDR assembly software. <span style="color: red;">*</span>
  * [Cinepaint][9] -- alternative to [GIMP][10] that does 16-bit images.
  * [GIMP][10] -- everyone's favorite Photoshop alternative.

<span style="color: red;">*</span> These packages are Windows-only (or at least superior in Windows), and I am running them in [Codeweaver's Crossover Office][11] implementation of WINE -- they will all probably work fine in [stock WINE][12].

Phew, that's a lot of software. Before, I get into the actual workflow, a brief explanation of a useful technique for HDR assembly:

## Tripod-Less HDR Assembly

When you are making an HDR image, typically you hear that you need to use a tripod. This is because you are taking multiple exposures of the same scene and essentially "combining" them into one picture. If the picture is mis-aligned, you'll get one funky-looking image (and believe me, I've got loads of these.) Imagery-nerds refer to this as "co-registration", which needs to be corrected if you haven't used a tripod. Software like Photoshop CS and Photomatix have some degree of auto-correction, but since I'm a cheapskate, I have to make do.

Fortunately, a friend of mine tipped me to the idea that co-registration correction has a more widespread application: panorama generation. By taking advantage of this, you can actually use panorama software (autopano and Hugin) to fix the co-registration of exposures that are misaligned because you didn't use a tripod. I don't know how well the auto-correction in Photoshop/Photomatix works, but from what I've read compared to the exposures I've fixed, I think this actually might work a fair amount better.

So, on to the details:

## Workflow

  1. Open Bibble Lite, and save two copies of each exposure: one 8-bit JPG file, and one 16-bit TIF file -- same name for each, but different extension: 1.jpg, 1.tif; 2.jpg, 2.tif; etc... If some of your exposures are particularly dark, you may want to bump up the exposure on the 8-bit JPGs (but not on the TIFs) -- don't worry about how they look. The JPGs will be discarded. Why are we doing this? autopano doesn't (yet) work on 16-bit images, so we have to make some 8-bit JPGs to feed to autopano to generate points.
  2. Now, in a directory with the 8-bit JPG files, run autopano: 
    <pre>$ wine ./autopano.exe
...
PANORAMA CREATION
Panorama number 1, pictures : 0 2 1
Writing Project file
</pre>

  3. Hopefully, if the autopano run was successful, you'll have a file, 'panorama0.oto', containing "points" which we'll feed to hugin for the actual co-registration correction. But we don't want to use the JPG files, we want to use the 16-bit TIF files (hugin **can** process 16-bit images). So we'll be sneaky and just edit the 'panorama0.oto' file and change the names from jpg to tif. Do this however you prefer -- I'm a nerd, so I use perl: 
    <pre>$ perl -i -ne 's/\.jpg/\.tif/g; print' panorama0.oto
</pre>

  4. Now, go ahead and start Hugin and load the panorama0.oto file. Here, in Hugin, there are a number of options we want to tweak -- Hugin by default is expecting that we'll be feeding it multiple images and having it stitch them together. Instead, we want it to take the input images and simply fix the co-registration and spit them back out: 
      1. Open the panorama0.oto file.
      2. Click the Optimizer tab, and select "Positions (y, p, r)". Click "Optimize Now!", and click "Apply" when it asks (unless it recommends against it, which can happen if there are no or erroneous optimizations made.
      3. Click the "Stitcher" tab.
      4. Change the projection to "Rectilinear"
      5. Click "Calculate Field of View"
      6. Click "Calculate Optimal Size"
      7. Under "Output File Options", choose the "Multiple TIFF" image format -- this is crucial, as it's the part where we tell Hugin that we want it to just spit out multiple TIFFs instead of one stitched file.
      8. Click "Stitch Now!" and pick something like "out.tif" to save. Hugin will do its thing, now, and generate an output tif for each input image: out0000.tif, out0001.tif, and so on.
  5. Open HDRShop, and go to "Create -> Assemble HDR From Image Sequence"
  6. Click "Load Images" and load all of the out000N.tif files that were generated.
  7. Click on "Change" under "Camera Response Curve" -- this is where you will want to load a response curve you've generated for your camera. The process for doing this is outside the scope of this document ([see here][13]), but trust me, **you want to do this**. Your results will look like ass if you don't. Trust me.
  8. Using HDRShop, you can tell it what f-stop increments you used on the original exposures, but in my experience, it does a perfectly good job of calculating them itself -- click on "Calculate" under "Calculate Scale Increments"
  9. All done! Click "Generate Image". Congratulations, you've created an HDR image. If you're lucky, it might not look like someone pooped all over your monitor.
 10. Click File -> Save As to save the HDR image. There are numerous HDR formats to choose from -- I use Radiance (HDR) format, as it's well-supported by pfstools.
 11. Now for the tone-mapping: 
      1. This is where pfstools come in. pfstools are commandline tools designed to just pipe the HDR pfs data format from utility to utility, which is handy. I usually use pfsview on the HDR file without any tone-mapping to see what I am dealing with first: 
        <pre>$ pfsin filename.hdr | pfsview
</pre>
        
        Sometimes I like what I get here just by tweaking the gamma and the limits and saving right from here. </li> 
        
          * But if you want to apply tone-mapping: 
            <pre>$ pfsin filename.hdr | pfstmo_fattal02 | pfsview
</pre>
            
            You get the idea. the tone-mapping utilities are named pfstmo_[algorithm]. </li> </ol> </li> </ol> 
            
            ## A Note About Tonemapping Algorithms
            
            I've gotten pretty familiar with the algorithms available in pfstmo. Some quick observations on some of them from my usage (disclaimer: negative perceptions of any one of these algorithms is probably as much my usage of it as it is a deficiency in the algorithm itself):
            
              * pfstmo_drago3 -- This is a decent multi-purpose algorithm. It's fast as hell, but when I use it, it tends to utterly obliterate any detail in the highlights (clouds tend to become a splat of color, for example.)
              * pfstmo_durand02 -- This algorithm produces some really gorgeous low-saturation results that are very subtle -- no eye-popping contrasts, opting instead for a more lifelike result. It also takes .. a long time. Like, a really long time. Like, go get some coffee, drink it, have a kid or two, retire, and come back.
              * pfstmo_fattal02 -- This is clearly the algorithm that Photoshop CS2 and Photomatix use -- it produces results that are sometimes awesome and sometimes comical. It's the algorithm that produces the "halo effect" that most people associate almost exclusively with HDR and tone-mapping. I have not had much luck with this in creating realistic HDR images (it can be done -- mostly on landscape shots, from what I've seen), but I've managed to get some decent effectish type results with it.
              * pfstmo_pattanaik00 -- Produces low-saturation (sometimes nearly B&W) images similar to durand02, but much faster, and not as nice.</ul> 
            
            ## Conclusion
            
            So, there you have it. I admit this is a pretty insanely convoluted workflow, but it's actually not so bad once you learn how all the different tools work -- and they are all really powerful tools to have at your disposal in doing all kinds of image-processing -- not just HDR. Hopefully as some of this software, many of these steps will be consolidated (16-bit support in autopano, for example, would simplify things quite a bit -- as would automated co-registration correction in tools like HDRShop or Cinepaint).
            
            Also, I am actually fairly new to this, so if anyone out there spots any glaring problems or things that are potentially causing me grief in getting decent results, let me know. The biggest challenge I face in actually making some Cool Shit (tm) with these techniques appears to be taking images that are all of a) interesting, b) low-noise, and c) actual contain high dynamic range. It's been harder than I expected. Wish me luck!
            
            **UPDATE:** Oh yeah, you can see the meager results I've produced so far [here][14].

 [1]: http://en.wikipedia.org/wiki/High_dynamic_range_imaging
 [2]: http://en.wikipedia.org/wiki/Tone_mapping
 [3]: http://www.bibblelabs.com/
 [4]: http://www.mpi-inf.mpg.de/resources/pfstools/
 [5]: http://www.mpi-sb.mpg.de/resources/tmo/
 [6]: http://www.autopano.net/
 [7]: http://hugin.sourceforge.net/
 [8]: http://athens.ict.usc.edu/HDRShop/
 [9]: http://www.cinepaint.org/
 [10]: http://www.gimp.org/
 [11]: http://www.codeweavers.com/
 [12]: http://www.winehq.com/
 [13]: http://gl.ict.usc.edu/HDRShop/tutorial/tutorial3.html
 [14]: http://www.flickr.com/photos/cwage/sets/72157594207406605/