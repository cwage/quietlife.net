---
post_id: 105
title: jabber init script
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=105
permalink: /2002/03/27/jabber-init-script/
dsq_thread_id:
  - 368868474
categories:
  - geek
tags:
  - geek
---
Well, I finally got a [jabber server][1] set up on agenteight.com.

In the process, I discovered that it's a lot safer and more stable to run each transport (the piece that lets you talk to other IMs) in a separate process.

This makes management a little hairy, though, so I whipped up an [init script][2] for SYSV init style UNIXes that I think works pretty well.

 [1]: http://jabber.agenteight.com/
 [2]: http://chris.agenteight.com/jabber