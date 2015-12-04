---
post_id: 989
title: WordVerify
author: cwage
layout: post
guid: http://chris.quietlife.net/?p=989
permalink: /2005/12/07/wordverify/
dsq_thread_id:
  - 236779310
categories:
  - geek
tags:
  - geek
---
I have hacked up a little WordPress plugin to allow for comment submission verification based on a configurable "codeword". The plugin is called WordVerify, and it's available [here][1].

I've only tested it for WordPress 1.5, and it should be considered super duper mega quadruple beta. But, it works for me on two different WordPress blogs.

The idea is that a lot of commentspam is driven by automation, naturally, and the introduction of a human element in submitting an extra bit of verification can help kill a lot of this spam. [SecureImage][2] is an example of a great plugin that uses ImageMagick to display an image with random letters that the commenter must verify. WordVerify provides a simpler alternative to this method, by just requiring the entry of a single word. This provides a healthy compromise for smaller blogs that don't necessarily need the security of a dynamic image. The chances of any comment spammer bothering to screen-scrape my blog just to comment-spam it, much less OCR an image, are pretty low. For smaller blogs, the simple addition of a codeword is probably more than enough.

Further, WordVerify allows customization of the phrase in which the security word is presented in the form, decreasing the ability of spammers to scrape the word if the plugin gains widespread usage.

The installation is simple, as with all WordPress plugins:

  1. [Download wordverify.php.txt][1]
  2. Rename wordverify.php.txt to wordverify.php
  3. Copy wordverify.php to your WordPress plugins directory (wp-content/plugins).
  4. Go to Plugins and "activate" the plugin.
  5. You can now go to Options -> WordVerify to configure the security word and the phrase it's presented in.

Have fun! Any suggestions are welcome. Feel free to test out the plugin in the comments below. Testing is good.

Thanks to Random, whose implementation of this idea on his [The Whole Truth][3] podcast was the inspiration for this plugin.

**Update:** I have verified that this plugin appears to work fine with WordPress 2.0

**1/5/2006 UPDATE:** There was a documentation error in the instructions that inadvertently instructed you to use "%%SECURITYWORD%%" rather than what the plugin uses for substitution, which is "%%CODEWORD%%". A new version (1.1) of the plugin has been posted that resolves this confusion.

**1/8/2006 UPDATE:** Released a new version, 1.2, that fixes a problem with comment counts. When codeword verification fails, the comment was deleted in a terrible (non-API) way, and hence the comment count was not being updated for the post. This has been fixed.

 [1]: http://chris.quietlife.net/wordverify/wordverify.php.txt
 [2]: http://dev.wp-plugins.org/wiki/SecureImage
 [3]: http://twt.randomcasts.com/