---
post_id: 199
title: key management
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=199
permalink: /2003/10/13/key-management/
dsq_thread_id:
  - 236777324
categories:
  - geek
tags:
  - geek
---
I am currently reading [Secrets and Lies][1], by [Bruce Schneier][2]. Bruce is the well-known author of [Applied Cryptography][3], which is considered the de facto "bible" of cryptographic applications. In the foreword of Secrets and Lies, he describes his inspiration for authoring the book: following the publishing of Applied Cryptography, he was inundated with stories of grotesquely designed security systems, rife with cryptographic acronyms, but lacking in any of the careful design of procedure and process that truly define security. So, he wrote Secrets and Lies from this angle, issuing a warning that cryptography does not make security, and providing a framework for understanding truly security systems.

With this in mind, I have recently re-evaluated some of my own security practices, and finally remedied some of my bad habits, which I will post in a series of posts, beginning with my key management practices below:

<!--more-->

### Key management and security

The key to many secure applications, without fail, lies in, you guessed it, the keys. So many secure applications these days revolve around public-key cryptography. For me, primary among them, are [GnuPG][4] and [OpenSSH][5]. For a long time, I was grossly careless with my keys. I created a keypair on any server I used regularly to ssh to other places. While this may have been convenient, it was far from secure. Instead, for every keypair I generated, I was opening up yet another doorway from system to system. If any of the machines I used were ever compromised, my keys, strewn about carelessly, were wide-open doors to others.

My solution first involved a purchase. I could finally justify my rampant consumerist impulse to buy what would otherwise be a toy, a USB keychain drive. Specifically, I bought a 64M [PQI "intelligent stick"][6], with which I have no gripe except that there's no way to hook or clip it onto anything, making it in fact not much of a "keychain" drive. There's a clip on the cap, which of course is useless, as it would only save the cap. I'd love to get my hands on the engineer responsible for that stroke of genius.

In any event, I formatted the key as ext3fs, and generated new keys for both GPG and SSH, which I placed on the key.

Instead of dealing with having to regularly mount my USB drive every time I wanted to use it, I decided to opt for the convenience of [autofs][7]. This allows me to simply have a directory that is "auto-mounted" by the automount daemon as specified in the autofs configuration:

<pre>keychain        -fstype=ext3                            :/dev/sdc1
</pre>

This creates a directory called "keychain" in the root automount directory (in my case /mnt/removable) which will automatically mount /dev/sdc1 whenever it is accessed.

I then symlinked my .gnupg and .ssh directories as necessary to the files on /mnt/removable/keychain/. (On some machines, where I needed a unique ~/.ssh/authorized\_keys, I symlinked the individual files rather than the whole directory so that ~/.ssh/authorized\_keys could sit on the machine itself, not on my USB drive).

Voila. I now have my SSH and GnuPG keys as accessible as ever, but secure in being on a USB drive that is disconnected and in my pocket when not in use, and automatically mounted when reconnected.

 [1]: http://www.allconsuming.net/item.cgi?id=0471253111&assoc_id=myquietlife-20
 [2]: http://www.schneier.com/
 [3]: http://allconsuming.net/item.cgi?isbn=0471117099&assoc_id=myquietlife-20
 [4]: http://www.gnupg.org/
 [5]: http://www.openssh.org/
 [6]: http://www.pqi1st.com/products/istick.asp
 [7]: http://www.linux-consulting.com/Amd_AutoFS/autofs.html