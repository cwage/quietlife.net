---
post_id: 163
title: MT/Livejournal synchronization
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=163
permalink: /2003/04/16/mtlivejournal-synchronization/
dsq_thread_id:
  - 236775623
categories:
  - geek
tags:
  - geek
---
[Jim][1] was asking how I sync'ed my [LJ website][2] with this one. (Why did I do this? Well, I only got the LJ account to post comments on friends' LJ webpages, so I figured I'd just sync the content of my page from here). So, I decided to try to remember, and then post how I did it, just for him! Disclaimer: there are probably more elegant ways to do this than I did.

<!--more-->

Basically, I swiped the idea of [this guy][3], which is using a shell script to control [blagg][4] and its [livejournal-syncing plugin][5] in syncing my movable type website and my livejournal site. I then have this script running in a cronjob every 5 minutes. I tried to make this a CGI script that MT pings when I post, like he did, but failed, and decided not to vest any further effort into something I didn't really care about, and just dumped it into cron.

The bulk of the script follows:

<pre>#!/bin/sh

lockfile=/tmp/lj.lck

blagg=/home/cwage/bin/blagg
plugin=-plugin=livejournal
mode=-mode=automatic
login=-login=chrismwage
password=-passwd=[your password here]

REQUEST_METHOD=

i=1

while [ $i -lt 5 ]; do
        if [ ! -e $lockfile ]; then
                touch $lockfile
                                        cd /home/cwage/bin
                $blagg $plugin $mode $login $password
                rm $lockfile
                i=5
        else
                sleep 60
                i=$(( $i + 1 ))
        fi
done
</pre>

 [1]: http://www.xmlhead.com/
 [2]: http://www.livejournal.com/users/chrismwage/
 [3]: http://popone.innocence.com/archives/000171.html
 [4]: http://www.oreillynet.com/~rael/lang/perl/blagg/
 [5]: http://www.speirs.org/blagg.php