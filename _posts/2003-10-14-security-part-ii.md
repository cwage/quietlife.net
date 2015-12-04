---
post_id: 202
title: security, part II
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=202
permalink: /2003/10/14/security-part-ii/
dsq_thread_id:
  - 237285711
categories:
  - geek
tags:
  - geek
---
So, I've [already discussed][1] the more physical element of my key management. So now let's talk about passphrases and ssh-agent:

<!--more-->

### ssh-agent: friend or foe?

First, a bit of background: You may or may not recall that when you generate a SSH keypair with ssh-keygen, it asks you for a passphrase. The reason for this is another simple layer of security. After it generates the public and private keypair, it encrypts the private key with a symmetric algorithm against your passphrase. This ensures that even if someone gets ahold of your key, they'd still need to know the passphrase. Allow me to be frank, here: using passphraseless keys is sheer lunacy. Especially, for me, since I physically carry my keys around with me on the USB drive. If my USB drive were ever to be lost or stolen, the keys would be freely available without the passphrase.

But, let's face it: entering your passphrase every time you need to use your private key can be a bit annoying. From a convenience perspective, you might as well just use regular password authentication. Enter [ssh-agent][2]. ssh-agent is a daemon that runs and listens on a socket for authentication requests from the ssh client. This allows you to use [ssh-add][3] to add your keys to ssh-agent. It asks you once for the passphrase and then caches the key and the passphrase in memory, allowing your ssh client convenient access to your private key when needed, without bothering you for your password.

But ssh-agent has its downsides. Like everything, it's a compromise. You no longer have to enter your passphrase every time, but you now have your private key **and** passphrase sitting in memory. Personally, I think this is a design flaw and it seems like it would be prudent to at least have an option to only cache the **passphrase**, decrypting the private key each time it's needed. This would be slower, but it would be more secure. Why? Think of my situation: my SSH key is on my USB drive. If I am using ssh-agent, even if I remove the USB drive from the computer, my key and passphrase are both still cached in ssh-agent until I manually do "ssh-add -D".

Leaving ssh-agent running on an unattended machine with your keys and passphrase cached is just asking for it. (This doesn't stop otherwise intelligent people from doing it all the time). For one, if the computer running ssh-agent (or your account on it) were ever to be compromised, it's as simple as finding the socket (/tmp/ssh-XXXXXXXX/agent.<pid> by default) and setting it as your $SSH\_AUTH\_SOCK to access the key and gain access to any machine that your key has. Further, it probably wouldn't be that difficult to extract both the key and the passphrase itself from memory.

Another convenience is a spectacular feature of ssh called "authentication agent forwarding". This enables you to forward authentication requests from a ssh client on another machine back to the original machine running ssh-agent with the cached key and passphrase. For example, say that I am running ssh-agent on Machine A. I ssh to Machine B with authentication agent forwarding turned on (-A or "ForwardAgent yes" in ~/.ssh/config). What this does is creates a tunnel back to Machine A on which Machine B can reach the ssh-agent socket in /tmp/. This means that when I ssh from Machine B to Machine C (provided my public key is in the ~/.ssh/authorized_keys on that machine as well), Machine B can access my private key on Machine A to authenticate to Machine C as well, and so on and so forth ad infinitum.

This is terribly convenient too, but reveals yet another limitation that annoys me. Why is it that you have to use ssh-agent (which necessitates caching your key and passphrase) in order to forward authentication? Couldn't it just forward **access** to the key itself without caching it or the passphrase? If anyone knows a way to do this, let me know.

So, I am not terribly satisfied with the security of ssh-agent, but it's just too convenient (particularly because of the agent forwarding) for me not to use. So my solution was in my screensaver. If I could just run arbitrary commands on going to and from a screensaver, I could make sure that my ssh keys and passphrase were purged whenever I went idle or manually locked my machine. This required that I ditch [xscreensaver][4] (an otherwise great app) because it didn't allow me to do this. Instead, I installed [xautolock][5] and [xlockmore][6]. xautolock is a program that simply allows you to run arbitrary commands after a period of idleness (or a certain cue). xlockmore is the program I use to actually lock the screen. So, in my X startup sequence, I have this command:

<pre>xautolock -locker ~/bin/xscreensaver-lock -time 2 -corners +000 -cornerdelay 2
</pre>

This spawns xautolock in the background, telling it to run ~/bin/xscreensaver-lock after 2 minutes of inactivity. The -corners +000 is a somewhat bizarre flag that means that if I leave the mouse cursor in the left corner for -cornerdelay seconds, it will lock, as well. ~/bin/xscreensaver-lock, in turn, is a simple shell script:

<pre>#!/bin/sh

ssh-add -D
xlock -mode blank +usefirst +echokeys
ssh-add ~/.ssh/corp ~/.ssh/personal
</pre>

This means that after 2 minuts of inactivity, it runs ssh-add -D, which purges my keys and passphrases from ssh-agent. It then runs xlock, which locks the screen until I unlock it with my password. Then it runs ssh-add with my SSH keys, which runs [ssh-askpass][7], giving me a nice dialogue to enter my passphrase.

This in general makes me feel much better. If I'm away from my machine for more than 2 minutes, or if I purposefully lock it, my ssh keys and passphrase are purged, rendering the key useless. Further, depending on how long I think I'll be away from my desk, naturally, I'll just yank the USB drive, as well. I think this is a good compromise between the insecurity of ssh-agent and the convenience that it provides.

 [1]: http://chris.quietlife.net/archives/000312.html
 [2]: http://www.openbsd.org/cgi-bin/man.cgi?query=ssh-agent
 [3]: http://www.openbsd.org/cgi-bin/man.cgi?query=ssh-add
 [4]: http://www.jwz.org/xscreensaver/
 [5]: http://packages.debian.org/stable/x11/xautolock.html
 [6]: http://www.tux.org/~bagleyd/xlockmore.html
 [7]: http://www.openbsd.org/cgi-bin/man.cgi?query=ssh-askpass