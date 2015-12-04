---
post_id: 222
title: Redundant OpenBSD
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=222
permalink: /2003/12/16/redundant-openbsd/
dsq_thread_id:
  - 264702383
categories:
  - geek
tags:
  - geek
---
Looks like [OpenBSD][1] 3.5 is shaping up to add many improvements that will suit its use in load-balanced/failover applications. This is a crucial step for competing with products like [CheckPoint][2], which have (using VRRP) some pretty advanced redundant failover capability.

<!--more-->

First there's [the addition][3] of <acronym title="Common Address Redundancy Protocol">CARP</acronym>:

> As those of you who follow source-changes know, I have just imported support for CARP, OpenBSD's Common Address Redundancy Protocol.
> 
> This protocol allows multiple hosts on the same local network to share a set of IP addresses among them. Some of the functionality it provides is similar to VRRP, although CARP differs in some significant aspects: CARP has been designed to provide greater security and be protocol independent (so we can support both IPv4 and IPv6). Finally, CARP allows for some level of load balancing in addition to it's high-availability functionality.

Then, [announced yesterday][4], is the addtion of pf state table synchronization:

> Log message:  
> Add initial support for pf state synchronization over the network.  
> Implemented as an in-kernel multicast IP protocol.
> 
> Turn it on like this:
> 
> \# ifconfig pfsync0 up syncif fxp0
> 
> There is not yet any authentication on this protocol, so the syncif must be on a trusted network. ie, a crossover cable between the two firewalls.

This is important because any stateful firewall will keep a table of stateful connections. If you load-balance between two or more firewalls, it's important that they all know about established connections. If you initiate a connection that goes through one firewall, it creates an entry in the state table, however if subsequent packets go through the other, it won't know about your connection and will drop the packets. This would resolve that by keeping the state tables synchronized over an isolated network connection between the two.

And finally, [source tracking has been added][5] to -current:

> I just committed code which adds support to track stateful connections by source IP address. This allows a user to:
> 
> - Ensure that clients get a consistent IP mapping with load-balanced translation/routing rules  
> - Limit the number of simultaneous connections a client can make  
> - Limit the number of clients which can connect through a rule

This is great for sites that are multihomed and such, as well as being very useful in load-balanced situations.

More great work from the OpenBSD team!

 [1]: http://www.openbsd.org/
 [2]: http://www.checkpoint.com/
 [3]: http://kerneltrap.org/node/view/1021
 [4]: http://www.deadly.org/article.php3?sid=20031216002544
 [5]: http://www.deadly.org/article.php3?sid=20031215080551