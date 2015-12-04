---
post_id: 1157
title: dnsblcheck
author: cwage
layout: post
guid: http://chris.quietlife.net/2006/02/15/dnsblcheck/
permalink: /2006/02/15/dnsblcheck/
ljID:
  - 328
dsq_thread_id:
  - 236779785
categories:
  - Uncategorized
tags:
  - blacklist
  - comment
  - DNSBL
  - geek
  - plugin
  - rbl
  - spam
  - trackback
  - wordpress
---
I have written a new WordPress plugin called [DNSBLCheck][1]. As you might expect from the name, it's a plugin that allows you to .. check [DNSBLs][2] before allowing comments/trackbacks.

I haven't really had much of a problem with trackback spam since I installed [this trackback validator plugin][3]. However, as their plugin is written, even though it stops the spam, it still e-mails you about it, which is quite annoying (I gave up wading through the wordpress plugin architecture to figure out why it was still e-mailing).

Making things worse was that I was getting hit by trackback spam by a large botnet (over 100 IPs and counting), most of which were listed on [cbl.abuseat.org][4]. It wasn't getting through, but I was getting 1-2 email notifications an hour, nonetheless.

So, at [Chris][5]'s prodding, I went ahead and hacked up this little plugin to check DNSBLs. I am currently checking [cbl.abuseat.org][4] and [list.dsbl.org][6] for now. If any of you experience any problems leaving comments, let me know.

 [1]: http://chris.quietlife.net/dnsblcheck
 [2]: http://en.wikipedia.org/wiki/DNSBL
 [3]: http://idli.cs.rice.edu/~dsandler/trackback/trackback-validator-plugin/
 [4]: http://cbl.abuseat.org/
 [5]: http://utcc.utoronto.ca/~cks/space/blog/
 [6]: http://dsbl.org/main