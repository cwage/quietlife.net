---
post_id: 141
title: opera + antialiased fonts
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=141
permalink: /2002/09/12/opera-antialiased-fonts/
dsq_thread_id:
  - 344809865
categories:
  - geek
tags:
  - geek
---
I finally got antialiased fonts working on Opera this week. My fonts got screwed up somehow (I am still unclear on what happened, really), so I decided to get it working once and for all.

Things I did to get it working, in a not so particular order:

  * TrueType Fonts (best for antialiasing):
  *   * Mounted "C:\Windows\fonts" on my WinXP PC from my laptop on /home/cwage/fonts
      * cd /usr/lib/X11/fonts/TrueType
      * cp /home/cwage/fonts/*.ttf .
      * ttmkfdir -o fonts.scale
      * mkfontdir
      * **(If you don't already have /usr/lib/X11/fonts/TrueType/ in your FontPath in your XF86Config, add it now. I already had it)**
  * Opera:
  *   * In order for antialiased fonts to work with Opera, you **must** have the version that is built **dynamically** against QT. So, the first thing I did was: apt-get remove opera-static; I then downloaded the non-static package and installed it. You'll need libqt2 if you don't already have it.
      * Created a wrapper script to spawn opera in ~/bin/opera: 
        <pre>#!/bin/sh

export QT_XFT=true

/usr/bin/opera
</pre>

  * Voila! The results: (Warning: big images)
  *   * <a href="http://chris.agenteight.com/archives/opera_before.html" onclick="window.open('http://chris.agenteight.com/archives/opera_before.html', 'popup', 'width=1209,height=1176,scrollbars=no,resizable=no,toolbar=no,directories=no,location=no,menubar=no,status=no,left=0,top=0'); return false">Before.</a>
      * <a href="http://chris.agenteight.com/archives/opera_after.html" onclick="window.open('http://chris.agenteight.com/archives/opera_after.html', 'popup', 'width=1209,height=1148,scrollbars=no,resizable=no,toolbar=no,directories=no,location=no,menubar=no,status=no,left=0,top=0'); return false">After.</a>

Okay, so the JPG sampling sorta makes it hard to tell. But, trust me, it looks nice. Oh so nice. Now if only I could get it working for all my GTK apps.