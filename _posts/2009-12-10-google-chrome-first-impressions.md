---
post_id: 2505
title: 'google chrome: first impressions'
author: cwage
layout: post
guid: http://chris.quietlife.net/?p=2505
permalink: /2009/12/10/google-chrome-first-impressions/
aktt_notify_twitter:
  - yes
ljxp_comments:
  - 0
ljxp_privacy:
  - 0
ljID:
  - 1136
aktt_tweeted:
  - 1
dsq_thread_id:
  - 236782789
categories:
  - misc
tags:
  - browser
  - chrome
  - google
  - review
  - software
---
I've been using [google chrome][1] here and there via the dev channel for a while now. As it's officially in beta now, I figured I'd post a few of my initial impressions.

  * Tab switching order: every browser I've ever used was able to switch tabs (via CTRL+TAB) in the order they were accessed -- either by default (Opera) or by configuration (Firefox). Chrome doesn't have it at all and it's driving me nuts. Apparently I am [not the only one][2] to be annoyed by this.
  * Middle-click to paste a URL into the browser window should load it. This is also missing, and it is also driving me nuts. (ARRRRRrrrr matey)
  * Middle-clicking a URL opens it in a new tab, but only in the background. Shift-middle-click circumvents that, but it's just not what I am used to, and it's not configurable.
  * Flash is very fast. There's a very large flash application we use at work, and it expects to run full-screen. In Firefox, it's nigh unusable due to slowness. In Chrome, it's quite zippy. I am not really sure what they did here, but I approve.
  * Mouse gestures. I really have a hard time living without these.. Opera spoiled me early, and I've never been able to go back. There are various extensions to address this, but none of them work in Linux, and they tend to be error-prone, because I think the Google guys are still changing a lot of stuff with respect to window handling/context menus, and such.
  * Chrome lets you store users and passwords for websites -- however, I was perplexed to see that nowhere in the config can you set a "master" password. So I poked around a bit, and sure enough Chrome stores all its passwords in an unencrypted sqlite3 database. Massive fail:  
    > cwage@portaptty:~$ sqlite3 .config/google-chrome/Default/Web\ Data  
    > SQLite version 3.6.16  
    > Enter ".help" for instructions  
    > Enter SQL statements terminated with a ";"  
    > sqlite> .tables  
    > autofill ie7\_logins logins web\_app_icons  
    > autofill\_dates keywords meta web\_apps  
    > sqlite> select * from logins;  
    > https://www.google.com/accounts/ServiceLogin |https://www.google.com/accounts/ServiceLoginAuth|Email|cmwage|Passwd|ThisIsNotMyRealPassword| |https://www.google.com/|1|1|1260412604|0|0 
    
    I can only assume this is something they intend to address eventually, but why bother even half-assing it like this? For now I've wrapped google-chrome in a script to encrypt/decrypt this, so I can continue using it:
    
    > #!/bin/sh
    > 
    > gpg --no-tty -d /media/thumbdrive/Web\ Data.gpg > ~/.config/google-chrome/Default/Web\ Data  
    > /usr/bin/google-chrome  
    > gpg -e -r cwage@quietlife.net ~/.config/google-chrome/Default/Web\ Data  
    > mv ~/.config/google-chrome/Default/Web\ Data.gpg /media/thumbdrive/  
    > wipe -f -s ~/.config/google-chrome/Default/Web\ Data 

So, aside from the password security issue, you may already be scoffing at my review: nothing but a list of relatively minor issues, right? Well, see, the thing is -- these are all minor issues that are major for my habits and efficiency, and every other browser lets you configure them. Chrome doesn't -- not right now. Now, it may, eventually -- either via built-in functionality or extensions that other people write. But knowing that, the current speed of Chrome doesn't really impress me. It's like if you built a car from the ground up out of nothing but tube-frame, an engine and a drive-train and then marketed it on its speed. Well, of course it's fast -- that doesn't mean I want to drive to work in it.

I actually have high hopes for Chrome, but I expect the final product to be marginally better, not revolutionary. We seem to be seeing a cycle with respect to this in the world of browsers. The release of Chrome reminds me of the release of Mozilla's Phoenix. Everyone was shitting their pants then, too, about this incredibly fast browser emerging from the flames of Netscape, re-written from the ground up to be super-fast and awesome. And it was. But it didn't do very much. And now, 6 years later, we have a browser that is still pretty good, but nowhere near the flawless speed daemon it started out as. This isn't a bad thing -- it's just the natural evolution of a software product that has to cater to literally everyone that uses the Internet. So Chrome is pretty cool, but it won't be my primary browser for a while yet. Talk to me again when you can configure ... anything.

 [1]: http://www.google.com/chrome
 [2]: http://code.google.com/p/chromium/issues/detail?id=5569