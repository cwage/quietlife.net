---
post_id: 1090
title: wordverify update
author: cwage
layout: post
guid: http://chris.quietlife.net/2006/01/18/wordverify-update/
permalink: /2006/01/18/wordverify-update/
dsq_thread_id:
  - 365336657
categories:
  - geek
tags:
  - geek
---
Posted a small fix to [WordVerify][1] today. If are using WordVerify and have noticed that trackbacks and pingbacks suddenly stopped working, well, join the club.

Turns out the comment routine that WordVerify hooks into in WordPress is the same as used for trackbacks and pingbacks, so those were getting killed. I added an exclusion there so only actual comments require verification.

**Update:** Gah. And with that I promptly got 3 trackback spam.

 [1]: http://chris.quietlife.net/wordverify