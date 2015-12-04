---
post_id: 152
title: 'Debian vs. Redhat: A biased comparison'
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=152
permalink: /2003/01/14/debian-vs-redhat-a-biased-comparison/
ljID:
  - 944
dsq_thread_id:
  - 236773953
categories:
  - geek
tags:
  - geek
---
What follows is a write-up I made that sortof represents the culmination of my opinions on my choice of GNU/Linux: [Debian][1]. I wrote it for two reasons: 1) I am trying to convince my boss as to its merits for use in a project at work, and 2) I've been wanting to digress on why I prefer Debian for a while. So, with no further ado, here it is:

<!--more-->

<div id="top">
  Debian vs. Redhat: A biased comparison.
</div>

<div class="section">
  First, some background:
</div>

We are tasked with designing a mail system for use of 65,000+ accounts. So, let's consider what factors are crucial in designing such a system:

  * Stability
  * Scalability
  * Security
  * Serviceability

So, drawing from that, we can ascertain that our core servers must be highly-available, scalable, and **very** stable. Furthermore, they must be easily expanded, upgraded and repaired to maintain a lengthy lifespan.

<div class="section">
  Disclaimer
</div>

I gave up any pretense of having this be an objective un-biased comparison of these two distributions. I've used both for a long time, and I've formed my opinions of both, but I don't have the time or resources to provide any sort of comparison that is anything more than opinion (and vitriol!). So, what distribution would I choose for the above task at hand? The answer is simple: Debian GNU/Linux.

So, what follows are the reasons why I have chosen Debian GNU/Linux for most of my GNU/Linux servers, and why I think it's particularly superior to Redhat in this application, broken down by categories as they apply to the above solution, followed by some myths and various miscellaneous points of contention:

<div class="section">
  Stability
</div>

I'm leading with my best material. Redhat and Debian GNU/Linux are two respectable distributions in their own right, but when it comes to stability, Debian is regarded as the holy grail. In my opinion, this is the least refutable point. Debian's reputation for stability exists for a number of reasons:

<div class="sub">
  <div class="subhead">
    .deb/dpkg package maintenance
  </div>
  
  <p>
    Some argue that a packaging system is a simple task, and that .deb and .rpm are both equally sufficient (or inept, depending on who you ask) implementations. I think that's a pretty shortsighted evaluation, though. If you go the route of using packages (as opposed to source or binary tarballs installed by hand), it's crucial that the packages are well-formed, and interoperate well with the system. RPM takes some steps to accomplish this, but in my opinion, .deb has taken it a step further:
  </p>
  
  <ul>
    <li>
      First and foremost, the development of the packages themselves in the Debian development process is superior. They <b>must</b> (in order to be accepted to the debian repository) adhere to the organization of the system, as well as the guidelines laid out in <a href="http://www.debian.org/social_contract#guidelines">the Debian Free Software Guidelines</a>. This is really an invaluable consideration, because with Redhat, you rely on RPMs built by people who may or may not know what they're doing. For example: compiling a program built in BSD and leaving the libraries in /usr/libexec when they should be in /usr/lib. These sound like trivialities, but they can make a quick mess of your system. In Debian, you can be assured that the package was assembled by someone that is a) a registered Debian developer, held responsible for maintenance of the package, and that b) utmost care is put into making sure the package interoperates with the system.
    </li>
    <li>
      Alternatives: Debian introduced the concept of "alternative" packages -- packages that are different implementations of the same program. Example: vi/vim. In redhat, the workaround traditionally is a kludge like just symlinking vim to vi, and renaming vi to something else, etc. Instead, in debian, /usr/bin/vi is simply a symlink to /etc/alternatives/vi, which is a symlink you can change (or packages can change) depending on what is installed.
    </li>
    <li>
      Suggestions: Packages in debian can have more than strict dependencies. They can have packages labelled as "suggested", but not required, i.e., documentation packages, or complementary packages.
    </li>
  </ul>
  
  <div class="subhead">
    Release cycle
  </div>
  
  <p>
    I think this is the area where Debian truly trumps Redhat for this application. Our primary concern is stability, and Debian's entire release cycle is centered around just that -- stability. Conversely, Redhat's release schedule, as far as I can tell, is more centered around "latest and greatest". Naturally both angles have their merit, and I'm not saying that Redhat doesn't also take admirable steps to make their product stable. However, Debian has a wonderful release cycle: You've got <i>unstable (sid)</i>, <i>testing</i>, and <i>stable</i>. Debian releases are made when packages in <i>testing</i> are thoroughly debugged and tested enough that they feel confident they are indeed <i>stable</i>. You can read more about that <a href="http://www.debian.org/releases/">here</a>.
  </p>
</div>

<div class="section">
  Security
</div>

Fortunately, in the Linux world, security is largely a cooperative effort, and security releases are mostly coordinated between distributions indiscriminately (or up the chain through CERT). So, most any distribution will have timely and available security updates as vulnerabilities are discovered. However, for what it's worth, Debian has had consistently fewer vulnerabilities per year since 1997:

<table cellpadding="5" cellspacing="0" border="1">
  <tr>
    <td>
      OS
    </td>
    
    <td>
      1997
    </td>
    
    <td>
      1998
    </td>
    
    <td>
      1999
    </td>
    
    <td>
      2000
    </td>
    
    <td>
      2001
    </td>
  </tr>
  
  <tr>
    <td>
      Debian
    </td>
    
    <td>
      3
    </td>
    
    <td>
      2
    </td>
    
    <td>
      31
    </td>
    
    <td>
      55
    </td>
    
    <td>
      28
    </td>
  </tr>
  
  <tr>
    <td>
      Redhat
    </td>
    
    <td>
      6
    </td>
    
    <td>
      10
    </td>
    
    <td>
      47
    </td>
    
    <td>
      95
    </td>
    
    <td>
      54
    </td>
  </tr>
</table>

* Source: <http://securityfocus.com/vulns/stats.shtml>

However, I think this is a pretty trivial consideration, since the security of a system only comes down to the competence and diligence of the person(s) administering it. Although Redhat did install with a shameful amount of services open out of the box prior to 7.0 releases.

<div class="section">
  Serviceability
</div>

Debian does more than just **provide** packages as a means of installing something instead of compiling software yourself. The distribution is built around its packaging system, to the core. This leads me to the utility that is the reason most people fall in love with debian:

<div class="sub">
  <div class="subhead">
    Apt
  </div>
  
  <p>
    When you bring up apt as a reason to use Debian over Redhat, most people counter that there are plenty of Redhat solutions that accomplish this (autorpm, up2date, to name a few -- there's even a port of apt to work with redhat and RPMs, but its power is lost without Debian's comprehensive repository and the flexibility of the dpkg package format), but these people usually have never used apt. Apt is more than just a tool to "keep your system up to date". It's a tool that interfaces with Debian's package system and Debian's online repository to control everything that's installed on your machine. I think this is best demonstrated through a few simple examples:
  </p>
  
  <p>
    Let's say, for example, we want to install "tkabber", which is a TCL/Tk <a href="http://www.jabber.org/">jabber</a> client. So:
  </p>
  
  <pre>
root@portaptty:~# apt-get install tkabber
Reading Package Lists... Done
Building Dependency Tree... Done
The following extra packages will be installed:
  bwidget tcllib
The following NEW packages will be installed:
  bwidget tcllib tkabber
0 packages upgraded, 3 newly installed, 0 to remove and 3  not upgraded.
Need to get 1132kB of archives. After unpacking 6632kB will be used.
Do you want to continue? [Y/n] y
Get:1 http://ftp.us.debian.org sid/main bwidget 1.3.1.20010713-1 [162kB]
Get:2 http://ftp.us.debian.org sid/main tcllib 1.3-2 [583kB]
Get:3 http://ftp.us.debian.org sid/main tkabber 0.9.3beta-2 [387kB]
Fetched 1132kB in 1s (875kB/s)
Selecting previously deselected package bwidget.
(Reading database ... 59659 files and directories currently installed.)
Unpacking bwidget (from .../bwidget_1.3.1.20010713-1_all.deb) ...
Selecting previously deselected package tcllib.
Unpacking tcllib (from .../archives/tcllib_1.3-2_all.deb) ...
Selecting previously deselected package tkabber.
Unpacking tkabber (from .../tkabber_0.9.3beta-2_i386.deb) ...
Setting up bwidget (1.3.1.20010713-1) ...

Setting up tcllib (1.3-2) ...
Setting up tkabber (0.9.3beta-2) ...
root@portaptty:~#
</pre>
  
  <p>
    And that's it! We're done! Compare this to your average experience with Redhat, which is a comedy of errors until you finally get everything you need. I've spent too many nights pounding my head against my monitor trying to get to rpmfind.net to search for yet another dependency I have to grab down the chain, discoverable by trial and error. My coworkers probably think I'm insane, judging from the streams of obscenities and groans they hear coming from my direction every time I have to deal with Redhat. Apt is much nicer.
  </p>
  
  <p>
    But, the real power of apt ties into both my previous topic up there, stability, as well as Debian's release cycle. Any time there is a bugfix, or a security fix in any package, this package is updated in the repository. This means that to upgrade those new packages, all it takes is <i>"apt-get update"</i> (to update your machine's cache of the current available packages), and then <i>"apt-get upgrade"</i>, which downloads and installs any available upgrades. In my experience maintaining Redhat servers, it was always important to stay on top of the BUGTRAQ and other assorted security lists so that you are alerted to any vulnerabilities so you can go and scope out RPMs, download them, and install them. While you'll never hear me discredit the value of paying attention to security disclosures, honestly, a number of huge security vulnerabilities have flown under my radar, and I've been fine just by virtue of keeping my Debian systems up to date with regular <i>"apt-get update; apt-get upgrade"</i>(some people even cron them, but that's a little irresponsible, I think).
  </p>
  
  <p>
    Furthermore, when it comes to Debian's release cycle, apt is even more powerful. Let's say it's July 19th, 2002, and Debian just announced that Debian 3.0 has been released, and that all the packages in <i>testing</i> have been moved to <i>stable</i>. At this stage, all you have to do, (provided your /etc/apt/sources.list references "stable" and not a distribution codename, in which case it would have to be changed) is <i>"apt-get update; apt-get dist-upgrade"</i>, and if all goes well, it will download and install all the new upgrades and bring your system to a fully-fledged install of Debian 3.0.
  </p>
  
  <p>
    What does all this mean? It means that it's vastly easier to keep many servers running current, secure software with minimal effort. I've encountered too many Redhat servers, even to this day, in my workplace that are running stagnant installations of Redhat 6.2, or even older (that would probably be hacked into oblivion if not for our corporate firewall). Yes, of course, that's partially our fault for not staying on top of the upgrades, but with Debian, that sort of thing is second nature and intrinsically part of the distribution itself, not some add-on or kludge that you have to manually install on every machine.
  </p>
</div>

<div class="section">
  Myths and Questions
</div>

"What about commercial/proprietary software that only distributes binary RPMs?"
:   This question, I think, is indicative of the fact that we've lost focus of the fact that we're talking about different **distributions**, not different **operating systems**. Excluding the possible big obvious internal differences (libc, etc), Linux is Linux. An RPM contains software that will run just as well on a Debian installation, or a Slackware installation. Debian kindly provides a utility called [alien][2], which will let you convert an array of package formats, including RPM, into Debian DPKG packags, and install them. If you're really hard up, it's interesting to note that RPMs can easily be extracted by hand with rpm2cpio and cpio, but I digress.

"Redhat has an established customer base and is a profitable (sometimes) company -- how do I know Debian will be around for long?"
:   People seem to often underestimate Debian's size and potential longevity. Debian isn't going anywhere. Debian's volunteer nature is its power -- there's nothing to dissolve, or to "go out of business". <http://www.debian.org/devel/people> lists over 700 active developers. Debian's main security package repository was completely wiped out in a massive fire at the University of Twente a few months ago, and was back up within a day, because of the vast numbers of mirrors across the world. Not bad. Not to mention that it's already been around for a decade, since 1993 -- longer than Redhat!

"Debian looks great, but most people are familiar with Redhat, and we can't afford to re-train."
:   I think this is another example of people blurring the distinction between a **distribution** and an **operating system**. Debian differs greatly from Redhat in its potential to be administered powerfully, but when it comes down to your average user, things really aren't that different. Honestly, I think if I modified the uname, motd, did *echo "Red Hat Linux release 7.1 (Seawolf)" > /etc/redhat-release"*, and symlinked everything in /etc/init.d to /etc/rc.d/init.d/, most people wouldn't know the difference. It's still GNU/Linux, either way.

<div class="section">
  Miscellaneous Contentions
</div>

This is where I gripe about the small, more trite annoyances and grievances I have with Redhat. Hoorah.

  * I have never been on a Redhat machine that installed apache stuff in the same place. Ever. I am not sure if I can blame this entirely on Redhat, or if I've just run into people compiling it from source and sticking it in weird places. But, honestly. /home/httpd. /usr/local/httpd. /usr/local/apache. /var/www. Make up your damn mind!
  * /etc/sysconfig -- a good idea, gone horribly wrong. Let's put all the configuration files for our customized packages in a central place and then make it so horribly unintuitive that you'll HAVE to pay Redhat for support! Genius!
  * /etc/rc.d/init.d/ -- rc.d/init.d? What is this? Why did Redhat feel compelled to invent this? At least they are starting to come around and at least have /etc/init.d symlinked to /etc/rc.d/init.d.

<div class="section">
  Conclusions
</div>

In short, I think both Redhat and Debian have their place. Debian has its shortcomings too, to be sure. The install process is slow and painful, and very daunting to the unfamiliar. The desktop environment pales in comparison to the work Redhat has done to improve it. But in the areas where we have the greatest need: stability, security, serviceability, Debian is vastly superior to Redhat. Debian's inherent focus is on creating a stable, open distribution of Linux -- it's the choice for anyone that wants a system they can rely on staying up and just **working**. I feel like Redhat's focus is elsewhere -- on a different market. Redhat on a server will work, but it's a lot **more** work.

<!--adsense-->

 [1]: http://www.debian.org/
 [2]: http://packages.debian.org/stable/admin/alien.html