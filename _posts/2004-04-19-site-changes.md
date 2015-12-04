---
post_id: 314
title: site changes
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=314
permalink: /2004/04/19/site-changes/
dsq_thread_id:
  - 4085359347
categories:
  - geek
tags:
  - geek
---
Just some assorted geekery here. I added two new sections to the bar on the right.

One is a list of the 10 last songs I've listened to, as collected by [audioscrobbler.com][1], which is a pretty neat site. Basically, you install a plugin into your favorite music player and it collects statistics about your listening habits. My profile is [here][2].

The other is [allconsuming.net][3], which tracks what I am currently reading. This is actually re-added, as I had it before and took it down.

The reason I took it down was because it was dependent on the allconsuming.net webserver to work, which was unacceptable for me. When allconsuming.net went down, or was slow (which is just about always), my site would subsequently hang. I've fixed this by having a cronjob pull everything I need down regularly and linking to it locally. The only thing my site is dependent on now is amazon.com.

 [1]: http://www.audioscrobbler.com/
 [2]: http://www.audioscrobbler.com/user/cwage/
 [3]: http://www.allconsuming.net/