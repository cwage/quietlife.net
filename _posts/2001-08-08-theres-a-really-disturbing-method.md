---
post_id: 38
title: 'There&#039;s a really disturbing method'
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=38
permalink: /2001/08/08/theres-a-really-disturbing-method/
dsq_thread_id:
  - 1724075234
categories:
  - geek
tags:
  - geek
---
There's a really disturbing method implemented in the HTTP spec (see [here][1] for more) that was intended for hosts to support SSL redirection, so that you can say "CONNECT \*sslhost\*:443 HTTP/1.1"

However, it seems on a misconfigured caching server (which a great number are), you can simply specify "CONNECT \*random host\*:\*random port\* HTTP/1.1" and voila, you have an instant tunnel.

What does this mean? Find a misconfigured caching server and you have yourself an instant mail relay, an instant anonymous web proxy, IRC proxy, etc.

What should you do? Well, if you run a network using caching servers, make sure they don't allow the CONNECT method. Squid allows you to turn it off, as does Volera ICS 2.0, however I haven't figured out how to make Cacheflow not allow it yet.

 [1]: http://sunsite.dk/RFC/rfc/rfc2817.html