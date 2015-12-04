---
post_id: 362
title: new things
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=362
permalink: /2004/06/24/new-things/
dsq_thread_id:
  - 236777705
categories:
  - misc
tags:
  - misc
---
In case it isn't immediately obvious, I have been neglecting this site. This is because I've taken a new direction in my career, signing on with [CentreSource, Inc][1], where I am doing small-business IT consulting. We provide a wide array of services, and I'd encourage you to recommend us to all your friends for all your IT/networking/security/you-name-it needs, if you're in the Nashville area (or even if you're not!).

In this line of work, I'm thrust into an arena I haven't previously spent much time in: the world of the small-business and personal technology consumer. On that note, I have a few observations so far:  
<!--more-->

1. Windows sucks
:   It sounds almost trite to say it these days, doesn't it? But forgive me for my ranting. I can't help it.</p> 
    
    I've been windows-free for around 3 years now, and I think during those 3 years, I cultivated a passive acceptance of Microsoft products as a viable computing choice. "Sure, Windows is fine, I guess," I told myself, "They've probably made some real improvements by now, and I'm sure it's just as powerful and stable a choice as any, if you know what you're doing." No. No, no, no! In my time away from Windows I have forgotten just how bad it is.
    
    The amount of productivity I have seen drained from my customers alone in this month is astounding. Never-ending wars with spy-ware. Viruses. Crashes. It's a serious chore for me, someone that knows what they're doing, to clean these computers up and restore them to a functional state. I am surprised anyone else is able to get anything done at all.
    
    If you'll allow one pathetic war story: I had one client whose NIC appeared fully functional, but it wouldn't pull a DHCP lease. In the deep recesses of my memory, I recalled a similar problem in Windows 95, wherein you had to uninstall and re-install the TCP/IP drivers to "re-bind" it to the NIC. Of course, you can't do that in XP, because TCP/IP is built-in, but lo and behold, I found a Microsoft knowledge-base article detailing the solution to this very problem: You have to re-install TCP/IP over itself manually. 9 years and 3 or 4 major releases of windows, and it's having the exact same problems.
    
    I then proceeded to spend 15 minutes trying to find the driver file on the hard drive itself, (since Sony, like most OEMs these days, I guess does not distribute an actual Windows CD with their computers [?!]) only to discover that it was right where it should be, but windows explorer was "hiding" the file from me. Thank you, Microsoft.
    
    Anyways, it's a big adjustment for me. Troubleshooting and configuring Windows is different in some ways than UNIX. There are rarely log files that are of any use. There's no "tcpdump". There's no "strace". I've often been confronted by misbehaviour which I don't know where to start troubleshooting, because there's nothing to go on. You just point and click until you find the magic combination. It seems that being an experienced windows sysadmin (and I don't mean to slight this accomplishment at all) requires less basic troubleshooting skills and more of a very large base of knowledge and experience with what can go wrong. </dd> 
    
    2. Where are the mid-line network devices?
    :   This is a problem I didn't expect to encounter. It seems there's a yawning gap in the market for networking devices between base-line home-use firewalls and high-dollar corporate firewalls. There are some things smaller businesses may need to do -- a simple port redirection, an extra physical interface, etc. -- which no affordable device can accomodate. I shouldn't have to buy a $500-$1000 Cisco or Checkpoint just so I can redirect a port, or get an extra physical interface.</p> 
        
        After all, these are things that a 486 running OpenBSD can do. But you can hardly offer an old 486 to a client as a solution, because it isn't a stable hardware platform. The most affordable hardware solution I know of as a router/firewall base, the [Soekris Net*][2] line, is still far too expensive to compete with a $50 Linksys or Netgear, even with the added functionality.
        
        The market is bleak for the small business that wants even a modicum of network functionality on a tight budget. This is another adjustment for me, coming from my previous job, where expensive top-of-the-line network **was** the norm. It's a shock for me to encounter a network device where you can't rely that it will pass GRE, or do something as simple as redirect a port.
        
        But, all is not doom and gloom. I expect this arena will get much better. Linksys's involvement with open-source software is encouraging, and hopefully as their hardware improves, a cheap hardware platform will be made available to secure, powerful software like OpenBSD that can offer an affordable choice with all the functionality you could ask for.
        
        Here's hoping, anyway.</dd> </dl> 
        
        So there you have it. My complaining aside, two technological problems I've noticed that are plaguing today's small business.

 [1]: http://www.centresource.com/
 [2]: http://www.soekris.com/products.htm