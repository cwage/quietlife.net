---
post_id: 1364
title: ignoring the wall
author: cwage
layout: post
guid: http://chris.quietlife.net/2006/07/02/ignoring-the-wall/
permalink: /2006/07/02/ignoring-the-wall/
ljID:
  - 534
dsq_thread_id:
  - 236780551
categories:
  - Uncategorized
tags:
  - china
  - firewall
  - geek
  - reset
  - technology
---
Via [Bruce Schneier][1], an [interesting paper][2] about a technique to bypass the filtering technique currently employed by China's Great Firewall. I am gonna get a little nerdy here -- something I generally reserve for the [CentreBlog][3] -- so bear with me here:

The way this firewall works is precisely the same as many commonly-available content-based filtering appliances available here. (I tested and evaluated a number of them for the TN K-12 school system back when I worked for [ENA][4].) It's not the routers or firewalls themselves that monitor for keywords and allow/drop connections, but rather servers that sit on an adjacent port on a switch and sniff the traffic. When they see a verboten word, they make an attempt to kill the connection. This is done utilizing a very simple technique.

In any TCP connection on the Internet, there is a packet with a certain flag that can be sent at any time by either end to reset the connection. The flag is called RST, which stands for .. you guessed it.. "reset". So, in order to kill a connection, these servers merely spoof RST packets both to the source and the destination of the connection, effectively terminating the connection. More advanced products hijack the connection entirely -- sending RST packets to the origin webserver and delivering a "block page" instead of the requested content to the client, letting them know that the content is forbidden, or perhaps in this case, that the storm troopers are en route to their house.

This is a fairly effective technique with one major drawback: it's subject to race conditions. If the server monitoring traffic gets bogged down, it may not get around to issuing the RST packets before the connection has already proceeded and data has been transferred. At the time, this was a major reason we opted not to use this technology at ENA. The amount of hardware needed to ensure a "race" was never lost was exorbitant in the face of more cost-effective methods. Apparently this isn't an issue for China.

But anyways, back to the paper. They are pointing out another obvious downside to this technique: if both sides of the connection ignore the RST packets, the connection won't be terminated. So, theoretically, firewall administrators in China could simply configure their firewall to ignore RST packets and if the server on the other end did the same, there would be no censorship. But of course this is useless if the other end doesn't cooperate. It raises an interesting possibility: a movement on the rest of the Internet to cooperate, and implement firewall rules to ignore RST packets on port 80 from IP addresses in China? Are there any possible negative side-effects of this? Other than some very dysfunctional situations in the event that a connection actually **needs** to be reset.

F1ght the P0w3r D00dZ!!

 [1]: http://www.schneier.com/blog/archives/2006/06/ignoring_the_gr.html
 [2]: http://www.lightbluetouchpaper.org/2006/06/27/ignoring-the-great-firewall-of-china/
 [3]: http://blog.centresource.com/
 [4]: http://www.ena.com/