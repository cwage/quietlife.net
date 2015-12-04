---
post_id: 1522
title: comment verification
author: cwage
layout: post
guid: http://chris.quietlife.net/2006/12/04/comment-verification/
permalink: /2006/12/04/comment-verification/
ljID:
  - 689
dsq_thread_id:
  - 236781184
categories:
  - Uncategorized
tags:
  - blogging
  - comment-spam
  - spam
  - tech
  - wordpress
  - wordverify
---
Some [interesting discussion][1] on NiT on the topic of comment verification, in which my [wordverify plugin][2] is mentioned -- specifically, on the annoyance of the image-based obfuscated letters as verification. I'll just post what I've got on the [wordverify page][2] again, for starters as far as what Wordverify aims to accomplish:

> The idea is that a lot of commentspam is driven by automation, naturally, and the introduction of a human element in submitting an extra bit of verification can help kill a lot of this spam. SecureImage is an example of a great plugin that uses ImageMagick to display an image with random letters that the commenter must verify. WordVerify provides a simpler alternative to this method, by just requiring the entry of a single word. This provides a healthy compromise for smaller blogs that don’t necessarily need the security of a dynamic image. The chances of any comment spammer bothering to screen-scrape my blog just to comment-spam it, much less OCR an image, are pretty low. For smaller blogs, the simple addition of a codeword is probably more than enough. 

Even this description is lacking, however, but I'll get to that. [Mack asks][3]:

> I hate word verification. Most of the time, I have trouble distinguishing the letters, i's and l's, for example, so inevitably I get it wrong, and have to start all over. So, I started wondering, how many people just don't bother to get into the "settings" of their blogger account to turn this decidedly inconvenient feature off? Surely most bloggers don't get enough traffic to warrant having this extra security feature, do they? 

No. but that's not the issue. The issue is that they're all using blogger. Or wordpress. Let me explain:

It's not really an issue of "big" or "small", so much, as it is an issue of whether or not you're a target. You're a target if spam to your blog can be automated -- if the mechanism to comment on your blog is predictable. This means you're a target if you use a popular blogging service like blogspot **or** you're using popular blogging software like WordPress.

You don't have to be a high-profile blogger to get comment spam. You just have to have a blog. Spamming is easy. The [Save Claudia][4] website (running wordpress) was getting comment-spam and trackback spam within a few days of going live.

The idea behind the image-based comment verification is that it introduces a human element into the process -- something that is not easily (or at least cheaply) automated. But this approach is still defeatable. The problem is not the method of verification itself -- the problem is that it's **the same** for every blog on blogspot, or **the same** for every installation of WordPress. It doesn't really matter how complicated you make the verification process -- barring implementing a turing test, it's probably always going to be defeatable. If it's the same on every blog, it can be automated. So, we have two choices: resort to ever-increasingly complicated human-verification methods that we standardize on each blogging platform in a neverending arms-race with comment spammers. That's the decision driving the image-verification approach. It's complicated enough and expensive (resource-wise) enough to defeat that it works. For now.

Alternatively, we can perhaps do something smarter: we give the individual blog owner the control to mix up the verification process and make it harder to predict **what's being asked**, rather than making the question harder. That's the philosophy behind Wordverify, and it's a barebones simple approach to accomplishing that: it allows you to change not just the codeword you need to enter, but also the phrase that asks or demands that you enter it.

This means that the only defeat of my implementation of wordverify requires a human element to go to my blog, see the phrase *Please enter 'confront' without the quotes.* and realize that they need to send codeword=confront in the POST. This can be automated, yes, but if so, it's a simple matter for me of changing the codeword and the phrase so that it again requires a human element to tweak the automated script. This of course is unlikely to happen, since no one spammer cares **that much** about specifically spamming quietlife.net. I'd probably be retired on ad revenue alone if that were the case.

It's for this reason that I beg to differ with [Jeffraham P][5] who says that it's *"cool, but easily defeated by spammers with skillz."* It's not. It's easily defeated by spammers with more free time than me, intent on specifically spamming **my blog**. This is almost guaranteed to never happen. It's been almost a year since I wrote and installed Wordverify, and in that time I've gotten approximately 0 automated comment spam. I don't think MQL has even had a human spammer (the [Centresource blog][6] has, however, but that's [another story][7]).

The point is: comment-spamming happens because comment forms are **all the same**. Normal verification processes are circumventable, because they're **all the same**. Even obfuscated image-based verification processes are defeatable, because you simply add OCR into the mix, and, yep, they're **all the same**. Until there are more options in the mix, spammers are going to continue to target what gets the most bang for the buck.

So, do I think wordverify is the end-all/be-all solution to comment spam? No -- but I think it's more elegant and more to-the-point than the more irritating and convoluted obfuscated-letters-in-an-image techniques. Rather than making the test for a human more complicated, blogging software and services should work on making the process more variable and harder to automate.

 [1]: http://www.nashvilleistalking.com/archives/2006/12/fqtdckop.html#comments
 [2]: http://chris.quietlife.net/wordverify
 [3]: http://coyotechronicles.blogspot.com/2006/12/gotta-say-this-i-really-do.html
 [4]: http://saveclaudia.com/
 [5]: http://jprestonian.blogspot.com/
 [6]: http://blog.centresource.com/
 [7]: http://blog.centresource.com/2006/01/27/human-spam/