---
post_id: 462
title: 'Latitude X300 &amp; trackpad'
author: cwage
layout: post
guid: http://chris.quietlife.net/2005/03/16/latitude-x300-trackpad/
permalink: /2005/03/16/latitude-x300-trackpad/
dsq_thread_id:
  - 491215943
categories:
  - geek
tags:
  - geek
---
As I've mentioned before, I am [running Linux][1] on my [Dell Latitude X300][2].

Like most laptops these days, it has a trackpad. While annoying, trackpads are far less annoying than the alternative -- those little button knobs in the middle of the keyboard.

One annoyance though is accidentally clicking the trackpad (which takes as little as a light brush with your thumb), which while typing can have all sorts of unfortunate side-effects .. minimizing the window, closing it, losing focus, etc.

Fortunately, using a combination of hacks, I have tamed the touchpad. (*Yes, I am using "touchpad" and "trackpad" alternately. At first, I did it by accident, but now I am doing it on purpose since people will probably search for both, and I want to be Google Friendly!*) Specifically, what I was interested in was:

<ol type="a">
  <li>
    Disabling the trackpad entirely while I have a USB mouse plugged in.
  </li>
  <li>
    Disabling the trackpad temporarily while typing.
  </li>
  <li>
    Having a transition between the two states be quick and convenient.
  </li>
</ol>

<img src="http://chris.quietlife.net/images/howididit.jpg" width="300" height="225" />

Here's How I Did It:  
<!--more-->

  1. First, you'll need to get and install the [Synaptics touchpad driver for XFree86/Xorg][3] (outside the scope of this document).
  2. The driver comes with two utilities: 
      * synclient -- this program allows you to change various settings for the touchpad, including disabling it entirely.
      * syndaemon -- this handy program runs as a daemon and will detect typing and disable the touchpad until the keyboard is idle for a customizable amount of time.
  3. Customize the following script to your needs. Several things may differ for your specific environment: 
    <pre>#!/bin/bash
PATH=$PATH:/usr/sbin:/sbin
PIDDIR=/home/cwage/var/run/
SYNDAEMON=/usr/local/bin/syndaemon
SYNCLIENT=/usr/local/bin/synclient

while true
do
# There is probably a better way to look for a running Xserver, but this will
# do for now. This exits the script immediately if the X server dies. Prevents
# 80 million copies of the script hanging around if you restart X.
if [ ! -S /tmp/.X11-unix/X0 ];
then
exit
fi
# This next test is how I test for the presence of a USB mouse on my
# system. You could also do "grep -i Mouse /proc/bus/usb/devices" but I
# had a bizarre problem with my laptop wherein the mouse actually
# disappeared from /proc/bus/usb/devices while I moved the mouse (?!)
# Sometimes it's easier to just pretend some things never happened and
# move on.
            if [ -d /sys/class/input/mouse1 ]; then
if $SYNCLIENT -l | grep 'TouchpadOff          = 0' > /dev/null;
# If we've detected a mouse and the touchpad is on, turn it off
# and start syndaemon
then
start-stop-daemon --stop --pid  \
$PIDDIR/syndaemon.pid --exec $SYNDAEMON
                $SYNCLIENT TouchpadOff=1
fi
            else
if $SYNCLIENT -l | grep 'TouchpadOff          = 1' > /dev/null;
then
if ! ps auxw | grep syndaemon | grep -v grep > /dev/null;
then
                $SYNCLIENT TouchpadOff=0
start-stop-daemon --background -m --start --pid \
$PIDDIR/syndaemon.pid --exec $SYNDAEMON -- -i 0.2
fi
else
start-stop-daemon --background -m --start --pid \
$PIDDIR/syndaemon.pid --exec $SYNDAEMON -- -i 0.2
fi
            fi
    sleep 3
done
</pre>

  4. Put this script in your .xsession or something that gets executed when you first log into X. It will run and constantly monitor for a USB mouse, or a lack thereof, and do the right thing. Voila!

 [1]: http://chris.quietlife.net/2004/05/29/linux-on-a-dell-x300/
 [2]: http://chris.quietlife.net/2004/05/21/new-toyhhhtool/
 [3]: http://web.telia.com/~u89404340/touchpad/