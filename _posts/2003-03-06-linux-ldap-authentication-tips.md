---
post_id: 154
title: Linux LDAP authentication tips
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=154
permalink: /2003/03/06/linux-ldap-authentication-tips/
dsq_thread_id:
  - 337948057
categories:
  - geek
tags:
  - geek
---
These are just some tips for making LDAP authentication work in Linux. I am not going to write a full HOWTO, as [that HOWTO][1] already exists, and is very helpful.

What I hope to provide here, instead, is just a list of things that I missed or that weren't clear after reading the HOWTO and found myself really banging my head against, trying to make this work. I have admittedly not done the extensive fact-checking to make sure that this is all 100% accurate as I would have if I had been writing a more official HOWTO, so if anyone finds an error or an inaccuracy, mail me, and I'll update it.  
<!--more-->

  
First, I was a little confused about the different roles that NSS and PAM play in authentication. As I understand it, NSS is an abstraction of the /etc/passwd file, basically. All information that is normally found in the /etc/passwd file can now be found via NSS, pulling from whatever data source it may be (in my case, LDAP). PAM is just an abstraction of the authentication process specifically. Usernames and passwords are authenticated against PAM, and that's it. However, in this application, it also gives the ability to change the password.

So, that said, you can see that LDAP would actually come in handy in either case (or both!) depending on what you need.

So, that said, a few tips:

  * /etc/libnss_ldap.conf must be at least chmod 644 -- that is, it has to be readable by all users. This is because calls are made to NSS as the user, and in order to use the LDAP configuration in order to pull certain information, it has to be able to see this file to know where to go. If you don't do this right, chances are authentication will still work, but once authenticated, your username won't have a user, and won't be able to map uids <-> usernames via LDAP. You'll show up as "I have no username!" or whatever your shell displays when it can't figure out who the hell you are.
  * /etc/ldap.secret must be chmod 600, or NSS and PAM alike will refuse to read it.
  * [strace][2] and [tcpflow][3] are your friends. Numerous times I had some stupid problem or inconsistency preventing successful authentication and a simple strace on sshd or "tcpflow -c port 389" to watch the actual LDAP query and what not was invaluable.

Good luck!

 [1]: http://www.tldp.org/HOWTO/LDAP-Implementation-HOWTO/
 [2]: http://www.wi.leidenuniv.nl/~wichert/strace/
 [3]: http://www.circlemud.org/~jelson/software/tcpflow/