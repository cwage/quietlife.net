---
post_id: 394
title: XMPP file transfer
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=394
permalink: /2004/08/27/xmpp-file-transfer/
dsq_thread_id:
  - 236777797
categories:
  - geek
tags:
  - geek
---
Peter Saint-Andre [notes][1]:

> Not many people have heard of [Volity][2] yet. It's a platform (largely based on [XMPP][3]) for building and playing multiplayer games over the net. It [seems][4] that the Volity folks are trying to do file transfer over XMPP in some creative, er, non-standard ways. Why not use [JEP-0096][5]? We don't write these specs for fun, ya know. 😉

Volity was first introduced to me by [Doug][6] and it looks pretty cool.

More generally, I am glad to know about JEP 0096. A lot of jabber client developers implement file transfer with XMPP via out-of-band connections, which for all intents and purposes is **completely useless** for the 95% of the world that is behind NAT/firewalls (not to mention endlessly confusing and frustrating). Further, in my opinion, the current inability to send files is one of the biggest weaknesses in Jabber.

XMPP client developers, take note: [JEP 0096][5] is your friend!

 [1]: http://www.saint-andre.com/blog/2004-08.html#2004-08-26T15:37
 [2]: http://www.volity.org/
 [3]: http://www.xmpp.org/
 [4]: http://ianso.blogspot.com/2004/08/file-transfer-xmpp.html
 [5]: http://www.jabber.org/jeps/jep-0096.html
 [6]: http://www.livejournal.com/users/dougo/