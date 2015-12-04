---
post_id: 439
title: referrer-b-gone
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=439
permalink: /2005/01/16/referrer-b-gone/
dsq_thread_id:
  - 236777821
categories:
  - geek
tags:
  - geek
---
Tom Sherman has [some thoughts][1] on the growing problem of referrer spam, which you've seen me rant about here before. He's got some good ideas, and he's certainly right that simply blacklisting domains or IPs via .htaccess or even firewalling is a losing battle. He does have one suggestion I disagree with, though:

> Referer spam is a problem because spammers can improve their sites' Google PageRank by getting listed on popular sites through spoofing of the HTTP_REFERER field in an HTTP request.
> 
> ...
> 
> If bloggers (and other website maintainers) did not publish this information, spammers would not bother to send these spoofed requests to blogs -- it would be pointless.

I don't agree. This logic is attractive, particularly when you are thinking like a reasonable member of polite society. The problem is, you have to think like a spammer. Trying to get spammers to stop referrer-spamming by convincing people to stop posting referrer info is like thinking that e-mail spam could be stopped if most people would just ignore it. Of course we know that most people **do** ignore spam (and filter/delete it with extreme prejudice).

The problem here is the same as it is in the world of e-mail. The cost of sending spam is low. When faced with a decrease in results, spammers won't **stop** spamming, they will **spam more**, to make sure they hit the one or two people out there still publishing their referer data.

Anyways, that said, using the various anti-spam blacklists out there seems like a good idea and is one I've been meaning to follow up on for some time, so I finally have. Blars has written a great module, [mod\_access\_rbl][2], for Apache, which is a replacement for the default mod_access that also lets you use DNS RBLs to limit access to your website.

Below are the instructions for doing so in debian -stable as I have done tonight:

<!--more-->

First, snag the module source:

<pre>shkaf:~$ wget http://www.blars.org/mod_access_rbl.tar.gz
--23:24:39--  http://www.blars.org/mod_access_rbl.tar.gz
           => `mod_access_rbl.tar.gz'
Resolving www.blars.org... done.
Connecting to www.blars.org[64.81.35.59]:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5,222 [application/x-tar]

100%[====================================>] 5,222         26.56K/s    ETA 00:00

23:24:40 (26.56 KB/s) - `mod_access_rbl.tar.gz' saved [5222/5222]
</pre>

Next we take a look at the tarball, since sometimes people are naughty and create a tarball of files with no parent directory, causing you to untar and clutter up your pretty home directory. So thoughtless!

<pre>shkaf:~$ tar tvfz mod_access_rbl.tar.gz
-rw-r--r-- blarson/666    1397 2000-07-01 01:28:46 README.rbl
-rw-r--r-- blarson/blars 12142 2000-07-01 00:56:37 mod_access_rbl.c
</pre>

I knew it! We'll make our own directory, then:

<pre>shkaf:~$ mkdir mod_access
shkaf:~$ cd mod_access
shkaf:~/mod_access$ tar xfz ../mod_access_rbl.tar.gz
shkaf:~/mod_access$ ls
README.rbl  mod_access_rbl.c
</pre>

Now we use the "apxs" program to compile the module. If you don't have this program, you probably need to apt-get install apache-dev.

<pre>shkaf:~/mod_accessR apxs -c mod_access_rbl.c
gcc -DLINUX=22 -DEAPI -DTARGET="apache" -I/usr/include/db1 -DDEV_RANDOM=/dev/random -DUSE_HSREGEX -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O1 -fPIC -DSHARED_MODULE -I/usr/include/apache-1.3  -c mod_access_rbl.c
gcc -shared -o mod_access_rbl.so mod_access_rbl.o -lc -lm -lcrypt -ldb1 -ldb -lexpat
</pre>

And then su to root to install the module with apxs as well:

<pre>cwage@shkaf:~/mod_access$ su -
Password:
shkaf:~# cd /home/cwage/mod_access
shkaf:/home/cwage/mod_access# apxs -i -n access_module mod_access_rbl.so
cp mod_access_rbl.so /usr/lib/apache/1.3/mod_access_rbl.so
chmod 755 /usr/lib/apache/1.3/mod_access_rbl.so
</pre>

Last but not least, we need to edit /etc/apache/httpd.conf to reflect the changes. mod\_access\_rbl is a drop-in replacement for mod_access so instead of adding it, we will just change:

<pre>LoadModule access_module /usr/lib/apache/1.3/mod_access.so
</pre>

to:

<pre>LoadModule access_module /usr/lib/apache/1.3/mod_access_rbl.so
</pre>

Now simply restart apache and voila, you can now use DNS blacklists in your .htaccess or <Directory> . This is what my .htaccess looks like:

<pre>Order allow,deny
allow from all
deny via sbl-xbl.spamhaus.org
deny via relays.ordb.org
deny via list.dsbl.org
deny via unconfirmed.dsbl.org
</pre>

I may tweak these ongoing and put some more thought into which blacklists are most likely to just catch zombie traffic, but for now, there you have it.

 [1]: http://underscorebleach.net/content/jotsheet/2005/01/proposal_to_solve_referrer_spam_blacklist_stats
 [2]: http://www.blars.org/mod_access_rbl.html