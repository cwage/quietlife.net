---
post_id: 1561
title: NiT on WordPress?
author: cwage
layout: post
guid: http://chris.quietlife.net/2007/02/02/nit-on-wordpress/
permalink: /2007/02/02/nit-on-wordpress/
ljID:
  - 726
dsq_thread_id:
  - 236781345
categories:
  - Uncategorized
---
So, apparently [Nashville Is Talking][1] is moving from Movable Type to WordPress. I can't say for sure that this is a bad idea, but it surely smells.. Movable Type would seem at a glance to be much more scalable than WordPress. Movable Type pushes static HTML around, whereas WordPress is entirely PHP/MySQL driven, which is infinitely slower. I'm concerned that with NiT's performance problems in the past even with Movable Type, that this is going to be a serious detriment to their site. You can alleviate a lot of the load from the dynamic nature of WordPress by implementing rigorous MySQL query caching, installing WP-Cache, and installing a PHP caching accelerator like [eaccelerator][2] (and I certainly hope they are doing these things), but still, I find myself wondering about this particular move.

Does NiT's webmaster perchance read this blog? I'd be curious to hear their thoughts.

 [1]: http://www.nashvilleistalking.com/
 [2]: http://eaccelerator.net/