---
post_id: 230
title: RSS aggregator
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=230
permalink: /2004/01/13/rss-aggregator/
dsq_thread_id:
  - 236777410
categories:
  - geek
tags:
  - geek
---
A while back, I [posted][1] about a little RSS aggregator I wrote in PHP for my own needs at [http://rss.quietlife.net][2]. Well, despite my complete inability to program, lately it's generated enough interested from a few people (okay, two) that I figured I should make a more detailed post with a link to the code and instructions for installing it.

<!--more-->

### Download:

  * [rss.tar.gz][3] (gzipped tarball)
  * [rss.zip][4] (zipfile)

### Requirements:

  * A webserver (only tested on Apache, but should work as long as you have PHP)
  * PHP - I have only tested with the version in Debian -stable (4.1.2), but I know of no version-specifics.
  * [Magpie][5] PHP RSS aggregator (included)

### Installation:

  1. Unpack the contents of rss.tar.gz (or rss.zip) in an appropriate web-accessible directory. If you don't have shell-access to your webserver, you will need to unpack it on your PC and FTP it up to the webserver.
  2. Permissions on the "rss/cache" directory are important. The scripts basically pull down the RSS feeds and display them, however that would take forever if it had to do it for every request. Instead, it caches the feeds locally and only refreshes if they change. So, the webserver needs write access to the directory it uses (rss/cache). If you are in UNIX, this is accomplished by making the directory writeable by the group of the user running the webserver (e.g. chgrp www-data rss/cache; chmod g+rw rss/cache) or making the directory world-writeable (e.g. chmod o+rw rss/cache). The latter should only be done if the risk of other users on the webserver being able to read and write/corrupt the cached feeds is acceptable. If you cannot modify this, it's not the end of the world -- but any RSS feeds will be pulled down every time you access the page, greatly increasing your wait-time.
  3. Edit your feeds. The structure of this code is such that the feeds are kept in the actual page it loads, and the "meat" of the code is included from dirtywork.php. The default package includes a "page1.php" that includes two feeds as an example. They are simply stored in a PHP array. To edit the feeds, simply add/remove them to this comma-delimited array as you see fit. To create other pages of feeds, just copy the page1.php file to others, e.g. politics.php or sports.php, etc.
  4. Test it out! Go to the URL on your website where /rss should be and see if it loads index.html. This is just a static main index file -- it contains nothing dynamic except for links to .php files where all the magic happens. Feel free to change or remove it at your discretion.
  5. The main index.html has a link to page1.php. Click the link and see if it displays.

### Caveats:

  * I am far from what you'd call a programmer, so this code may break. a lot.
  * The javascript used to do the rollover excerpts is dependent on whether or not the RSS feed provides them. Some do, some don't. Same with the dates. Also, the javascript was tested only so far as "hey, this works!" in Opera, but I haven't seen much problem in any other browsers.
  * Magpie sometimes reports malformed XML for some feeds. (usually because of an errant &). I haven't researched to find out if this is a bug in magpie or if the RSS feeds that cause it are genuinely malformed.
  * The code that displays the feeds iterates over the array of feeds and displays them in a random order. I did this because I found myself only reading the first few feeds listed before being distracted, and hence, only read the same first few feeds every day. Randomizing it was a way for me to mix up my reading. If this annoys you.. uh.. sorry. It's somewhat embedded in the code.
  * I plan on eventually rewriting this in a more accessible and customizable package. Stay tuned for details.

For questions, feel free to e-mail me at <cwage-rss@quietlife.net>.

 [1]: http://chris.quietlife.net/archives/000223.html
 [2]: http://rss.quietlife.net/
 [3]: /software/rss/rss.tar.gz
 [4]: /software/rss/rss.zip
 [5]: http://magpierss.sourceforge.net/