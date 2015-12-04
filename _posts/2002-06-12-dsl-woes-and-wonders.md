---
post_id: 125
title: DSL woes and wonders
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=125
permalink: /2002/06/12/dsl-woes-and-wonders/
dsq_thread_id:
  - 490277000
categories:
  - geek
tags:
  - geek
---
Well, I am officially no longer a customer of [Bellsouth][1] [Fastaccess DSL][2]. The reasons are numerous:

  1. Before we moved, I told them to switch my DSL over to the new place on May 23rd (the date we were supposed to move). Despite having a lengthy conversation explaining this, by May 10th my DSL and phone at my old apartment (where we were still living) was cut off, leaving us with no internet access or phone. Strike 1.
  2. After we got mostly moved in (on an accelerated schedule, thanks to Bellsouth), I started trying to get my DSL hooked up. It took me nearly 3 weeks working on and off with Bellsouth trying to get it working before I was at my wits' end. Bellsouth was unable to figure out why I couldn't get online, despite having sync on my modem, and were alternately unhelpful, rude, incredulous, incompetent, and sometimes all of the above. Strike two.
  3. Finally, I got ahold of a tech support rep that knew his ass from his elbow. I explained at length (one of a number of times I had done so) that I had a DSL modem operating in \*bridged\* mode, and that I preferred it this way. He informed me that Bellsouth no longer did bridged access, and my new neighborhood didn't even support it. If I wanted DSL from them, I'd have to use PPPoE, meaning I'd have a little dialup connection my windows box and whatnot. I understand there are PPPoE clients for OpenBSD (my current firewall) but I totally don't have the time to mess with that. Not to mention the overhead of PPPoE compared to just doing a straight bridged connection. But anyways. Strike three.

Of course, it's misleading for me to act like I was counting strikes, because I was pretty much bent over, seeing as how Bellsouth was pretty much the only reasonable DSL provider in my area -- or so I thought.

My salvation came in the form of [butler.net][3], a company owned by a friend of mine, Bill Butler. I called him up and he said he had no problems doing a bridged setup, and even got the transfer from Bellsouth's network started for me. If you're in the Tennessee area, I heartily recommend giving Bill a call.

I was online in a matter of days. I am officially relocated off of Bellsouth's network and I couldn't be happier. Score one for the little guy.

 [1]: http://www.bellsouth.com/
 [2]: http://www.fastaccess.com/
 [3]: http://www.butler.net/