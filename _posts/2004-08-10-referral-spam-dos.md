---
post_id: 380
title: referral spam DoS
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=380
permalink: /2004/08/10/referral-spam-dos/
dsq_thread_id:
  - 236777735
categories:
  - geek
tags:
  - geek
---
Well, my website was down briefly this afternoon. Why? I was effectively <acronym title="Denial of Service">DoS</acronym>ed by referral spam. See [this][1] and [this][2] for details.

I have been referer-spammed before in the past, but nothing on this scale:  
<!--more-->

  
In the past it had been a hit or two with the forged referer header. Once a few years ago, I did get some sustained hits from one IP that flooded my link until I firewalled it off.

This was on a different level -- straight up DoS. At any given time, around 2-3 different IPs were slamming my website with requests at a rate of 1-2 per second. They were doing a full GET request, meaning the entire page was being pulled down (rather than a HEAD request, which would accomplish the same goal and not pull down the actual content). You don't have to be a network engineer to realize that this utterly devastated my poor 256Kbps upstream bandwidth.

After about 30 minutes, I eventually got almost all of the requesting IPs blocked at my firewall -- around 100 total. It's quite obvious that these requests were coming from a swarm of zombie compromised windows PCs all over the internet. This is what makes the attack so insidious and difficult to block -- each request came from a different IP from a network completely separate from the last, so there's no single way to block it.

I was lucky in that there were only around 100 PCs being rotated -- I guess this shithead could only afford the entry-level DoS zombie swarm. I'd shudder to think what would happen if a few thousand were used. I'd be unable to contain it and have to shut down my website.

After about 45 minutes, I checked my firewall log and they were still furiously running up against the block. A few hours later, now, it appears to have stopped.

Very infuriating.

As a result, I have password-protected my stats pages, effectively taking them off the internet at large. While I doubt this will make much difference, I am doing it on the off-chance that these referer-log spammers try to target websites that actively run stats-gathering tools, rather than just spraying wildly. But I wouldn't hold out much hope.

 [1]: http://chris.quietlife.net/archives/000400.html
 [2]: http://chris.quietlife.net/archives/000405.html