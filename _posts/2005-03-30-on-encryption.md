---
post_id: 471
title: on encryption
author: cwage
layout: post
guid: http://chris.quietlife.net/2005/03/30/on-encryption/
permalink: /2005/03/30/on-encryption/
dsq_thread_id:
  - 236777909
categories:
  - geek
tags:
  - geek
---
I give you an annoying conversation (i am "dippo"):  
<!--more-->

`<br />
00:30 <dippo> anyone know of a wiki application that stores its data encrypted in any way?<br />
00:31 <Cyrius> ...encrypted? that seems a bit useless<br />
00:31 <dippo> how so?<br />
00:31 <Cyrius> well, if it's a wiki, it's pretty well open access<br />
00:33 <dippo> not all wiki software is designed to be so open<br />
00:33 <Cyrius> it's not really a wiki then =)<br />
00:33 <dippo> in this case I really like the flexibility and ease of use for documentation and I've thought about using it for personal stuff<br />
00:33 <dippo> but there's no way I am throwing personal data into it unless there's at least some basic symmetric encryption protecting it or something<br />
00:33 <TML> Well, you could store it on an encrypted partition<br />
00:34 <brion> back<br />
00:34 <dippo> i thought about that<br />
00:34 <TML> dippo: No, I've never seen nor heard of a wiki that uses encryption. It doesn't really fit in with the concept of why people generally use wikis.<br />
00:35 <Cyrius> dippo, if someone can compromise your database server, they can probably compromise the web server and get the key<br />
00:36 <dippo> not if it's protected with a passphrase<br />
00:36 <Cyrius> unless you're paranoid enough to isolate the DB from the net, in which case, why encrypt?<br />
00:39 <dippo> i'm just talking about basic encryption with a key protected by a passphrase<br />
00:39 <dippo> TML: the thing about an encrypted partition is, assuming it's a webserver, it'll always be mounted and hence accessible, which doesn't do me much good in the event of a compromise or something<br />
00:39 <Cyrius> I'm just saying that if you're going to be paranoid, there's no reason to not be paranoid in an effective manner<br />
00:40 <TML> dippo: *shrug* If the system is compromised, and the wiki can "decrypt" it, it will be trivial to go see *how* the wiki does so, and repeat that process<br />
00:40 <dippo> not if the process requires a passphrase<br />
00:40 <TML> What?<br />
00:40 <TML> dippo: What does that mean?<br />
00:40 <avar> haha<br />
00:41 <TML> "the process"?<br />
00:41 <TML> Which process are you referring to?<br />
00:41 <dippo> it means that if the process of encrypting/decrypting data requires a passphrase from the user then compromising the machine isn't enough<br />
00:42  * TML blinks<br />
00:42 < @TimStarling> they can just wait for the next valid request and sniff the passphrase 00:42 <dippo> not if it's using SSL 00:42 <TML> dippo: But if the data is decrypted, and viewable, then compromising the machine means you can get to the data 00:42 <dippo> it's not impossible to get the passphrase, but it's a lot more difficult 00:42 <@TimStarling> if they have compromised the machine, SSL doesn't do much good 00:42 <@TimStarling> it's past the endpoint 00:42 <dippo> it's better than nothing 00:42 <TML> If I'm in your box, and the wiki is running, I'll just visit the wiki and get the data 00:42 <@TimStarling> they can just read it from the computer's memory after SSL has finished with it 00:43 <dippo> if you're in my box, and the wiki's encryption has been designed with security in mind, you still have to enter the passphrase to decrypt the data 00:43 <TML> dippo: No, not really, it isn't. Encryption for encryption's sake is worse than useless...it's additional overhead with no added benefit. 00:43 <TML> dippo: No, you just VISIT THE WIKI. 00:43 <Cyrius> no, you just have to sit around and sniff the passphrase 00:43 <TML> A wiki is a website 00:43 <@TimStarling> anyway, the answer to the original question is no, there is no such wiki software 00:44 <dippo> if the website software has been designed with security in mind, you wouldn't be able to "visit" it without the passphrase 00:44 <avar> dippo: you might want to buy a book such as applied cryptography 00:44 <dippo> I own applied cryptography 00:44 <avar> have you read it?;) 00:44 <dippo> your condescension is misapplied 00:44 <Cyrius> dippo: then why are you worrying about it being compromised? 00:45 <dippo> why wouldn't I worry? 00:45 <Cyrius> that's my point 00:45 <Cyrius> you're assuming certain parts are secure, when they're not 00:45 <dippo> like what 00:45 <dippo> what have I assumed is secure? 00:45 <Cyrius> the web server 00:46 <dippo> there are a lot of parts of a webserver. what are you talking about specifically? 00:46 <TML> dippo: Which part of "No" isn't getting through? 00:46 <dippo> TML: is that your way of telling me that you want me to drop it because it's off-topic? 00:46 <Cyrius> dippo, if you compromise the web server, your passphrase is insecure 00:47 <TML> dippo: You can read it that way if you choose. 00:47 <dippo> there are clearer ways to communicate that 00:47 <dippo> but, that's fine 00:47 <dippo> feel free to message me if you want to continue, Cyrius 00:47 <TML> There's no way this can end gracefully. You sound like a nutjob to me, and I think to many of the people here. So it's better if it's just dropped. 00:47 <Cyrius> heh 00:48 <dippo> yeah, I'm a nutjob for worrying about encryption. okay, sparky 00:48 <Cyrius> you're not worrying about it in a reasonable manner 00:49 <Cyrius> if your machines are getting compromised, you're going to have big problems on your hands no matter what 00:49 <Cyrius> and simply encrypting the stored data won't solve that if the decrypter has been compromised 00:49 <dippo> I didn't say I wouldn't have any problems. In fact, I'm not saying anything, since I've been asked to drop it 00:50 <dippo> at least, passive-aggressive-implied asked, or something `

Naturally, I agree that encryption is no panacea, but it's not useless, either. Say, as I'm considering, that you've got a website that uses a database containing all of your personal data. SSN, credit card numbers, embarassing poetry -- everything. I give you two scenarios, both assuming SSL-only access:

Scenario #1:

You don't encrypt anything in the database because you think it's silly. Your webserver is compromised, and the attacker has only to find the code with the database username and password and snags himself a local copy of everything.

Scenarion #2:

You use software on your website that encrypts the data in the database with a symmetric algorithm using a key that is protected in turn with a passphrase. Your webserver is compromised. The attacker finds the code with the database username and password, and snags the data, but realizes it's encrypted. He locates the key used to encrypt the data, but realizes it's protected by a passphrase. The attacker realizes he needs this passphrase and must obtain it from one of the following sources: in memory somewhere from a legitimate user accessing the data, or an SSL man-in-the-middle attack, which he must do successfully before the breach is noticed and his access is terminated.

Are both of these scenarios possible? Absolutely. Are they both equally plausible? Uh, no. Which of these scenarios do you think your average identity-stealing php-vulnerability-exploting shithead is most likely capable of? Ahhuh. And, which scenario would you choose?

That's what I thought.</code>