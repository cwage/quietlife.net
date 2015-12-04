---
post_id: 29
title: My company is currently looking
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=29
permalink: /2001/07/26/my-company-is-currently-looking/
dsq_thread_id:
  - 1724071144
categories:
  - geek
tags:
  - geek
---
My company is currently looking for firewall/VPN solutions, and they are considering a Nokia solution.. While I'm sure the Nokia stuff is pretty cool, I am confident it would be foolish not to tap the resources we have around the office and not have us computer geeks just put together a powerful firewall/VPN box using something like [OpenBSD][1] and [IPfilter][2].

Using IPSEC tunnels and firewalling with ipfilter and stuff in OpenBSD is really painless, however one of the prerequisites to incorporating a solution like this is that it has to include a user-friendly (read: idiot-proof) web-based GUI. Unfortunately, we can't have the administration of our firewall rules rely on the knowledge of how to add and remove ipfilter rules in BSD by hand.

I've looked around and found a few ipfilter pre-processors, and some that use a higher level language that can output its rules formatted for ipfilter, iptables, ipchains, etc., however they all seem to be very alpha, and not very web-oriented, nor very functional.

If you have any ideas, [let me know.][3]

 [1]: http://www.openBSD.org/
 [2]: http://coombs.anu.edu.au/~avalon/
 [3]: mailto:cwage@place.org