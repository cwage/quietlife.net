---
post_id: 96
title: bandwidth throttling
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=96
permalink: /2002/02/24/bandwidth-throttling/
dsq_thread_id:
  - 236773657
categories:
  - geek
tags:
  - geek
---
It all started when I set up my FTP server, which was right around the time that I also installed [AudioGalaxy][1] for MP3 sharing. I started noticing that when people downloaded anything from my FTP server or from my Audiogalaxy client, my latency went through the roof -- 300+ ms.

Why? Because my upstream bandwidth is only 256kbps, and it was being maxed out by these transfers. I am all for sharing my files and all, but interrupting my IRCing and MUDding is simply inexcusable.

So, I recently discovered that [OpenBSD][2] supports [ALTQ][3] which stands for "ALTernate Queueing". Basically, it's a way to do bandwidth throttling.

[This is my altq.conf][4]. It's pretty self-explanatory ... Okay, not really.

Basically you just define classes that get certain percentages of your bandwidth. Then you apply filters to your traffic that lump them into certain classes. In my case, my config is pretty simple. I made a class called "fx_class", and configured it to get 60% of my 256k upstream bandwidth. Then, I made a bunch of filters to lump traffic from my FTP server (active and passive connections) and traffic from the Audiogalaxy client into that class.

Voila -- no more bandwidth choking. If I ever get time, I may write this up into a more comprehensive informal how-to so that other people interested in it can get some guidance.

 [1]: http://www.audiogalaxy.com/
 [2]: http://www.openbsd.org
 [3]: http://www.csl.sony.co.jp/person/kjc/kjc/software.html
 [4]: http://chris.agenteight.com/altq.conf