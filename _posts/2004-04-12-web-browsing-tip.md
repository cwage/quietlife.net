---
post_id: 308
title: web browsing tip
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=308
permalink: /2004/04/12/web-browsing-tip/
dsq_thread_id:
  - 236777571
categories:
  - geek
tags:
  - geek
---
I [ranted][1] earlier about my irritation with blogs that have approximately 8 billion panels on the left and right, usually images hosted off-site, javascript, etc. This results in extremely long loading time, particularly if a site is overloaded (\*cough\* blogads.com \*cough\*) and hangs.

In Opera, in particular, and perhaps other browsers, this means the page renders slowly, choppily, or not at all.

Thanks to my pal [Ben][2], though, I discovered an obvious solution for the Opera browser. Opera lets you turn off images while surfing. You can also turn off JavaScript. This cuts down on a lot. But [atrios][3], for example, has some stuff in iframes, which will load anyway. But Opera lets you include a custom CSS file to apply to all web browsing. Add this to it to eliminate iframes:

<pre>iframe { display: none }
</pre>

Of course, it wasn't until after this that I discovered Opera actually lets you turn off inline frames (i am assuming this is the same as iframes) as well. So, let that be a handy Opera tip for you: if something about someone's webpage annoys you, you can override it in your own CSS file.

Reading blogs is a joy, now. They load near instantaneously because all that loads it the content, and the 14 blogrolls, 10 blogads, and 13 sitemeters are ignored.

 [1]: http://chris.quietlife.net/archives/000437.html
 [2]: http://www.ben.com/
 [3]: http://atrios.blogspot.com/