---
post_id: 452
title: essential IT consulting utilities
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=452
permalink: /2005/02/19/essential-it-consulting-utilities/
dsq_thread_id:
  - 236777866
categories:
  - geek
tags:
  - geek
---
In my experience working with clients, I've collected a set of utilities that have proved to be absolutely essential for a variety of tasks, for workstation/PC repair in the wonderful world of Windows.

Below are the utilities I've put on a CD for frequent use and their descriptions:

<!--more-->

  1. [AntiVirus][1]
  2. [Network][2]
  3. [Spyware][3]
  4. [Software Firewalls][4]
  5. [Utilities][5] 
      1. [Registry][6]
  6. [Clients][7]
  7. [Toolbars][8]

<a name="AntiVirus"></a>  


### AntiVirus

[AVG][9]
:   AVG is in my opinion the best free anti-virus package out there. It's comprehensive, unobtrusive and gets the job done. Updates are timely and served from fast mirrors, too. Often times my clients get new PCs from Dell with Mcafee installed. By the time their PC starts up, and McAfee Internet Security, McAfee Privacy Center, McAfee Security Center, McAfee Anti-Virus, McAfee Browser Protector, McAfee Protector of the Universe, and McAfee Coffee Warmer have all loaded, you're lucky if they have any RAM left at all. I usually spend 20 minutes uninstalling all this crap and installing AVG.

[Avast][10]
:   Avast is a close second to AVG in my book, but lost a few points for me when it missed some viruses that AVG caught. I have no expansive body of evidence beyond this. It's pretty good too.

[McAfee Stinger][11]
:   Despite all my slamming of McAfee previously, they do make one great little utility. Their "Stinger" program is nothing but an executable with a pre-loaded set of signatures and code to remove them. It's lightweight and viciously removes anything it finds. It doesn't have an expansive set of signatures, but it's great for a first-pass removal of a badly overridden PC to at least get it to a functional state for further disinfection. This one is a must-have.

<a name="Network"></a>  


### Network

[TCPOptimizer.exe][12] 
:   This is a utility that can come in handy. It optimizes registry settings for various forms of internet access. Oddly, though, when I ran it on a dialup computer, it didn't seem to detect the dialup adapter as something to be tweaked. Oh well.

[WinPcap][13] 
:   WinPCAP is a port of libpcap, a packet capture library, to Windows. Useful in programs like Ethereal, below:

[Ethereal][14] 
:   Ethereal is probably the best GUI sniffer around. In the Windows world, unfortunately sometimes there aren't really many clues to go on for a particular problem. When no logfiles exist, sometimes you gotta make your own. Unfortunately this requires installing software and drivers, which in Windows can screw up as much as it resolves, but desperate times call for desperate measures. If possible, a [passive ethernet tap][15] might be a less obtrusive way to sniff data.

<a name="Spyware"></a>  


### Spyware

[Spybot][16] 
:   Spybot is in my opinion the best anti-spyware application out there, although it didn't do well in a [recent shoot-out][17], in which some others came out on top.. Spybot is worth using for its "TeaTimer" application alone. It's a memory-resident process that sits inthe system tray and watches for changes to startup or the registry and pops up a window asking for your confirmation. It can be confusing for the untrained user, but it's worth explaining to them. I install it on my clients' PC and just tell them "if you see this, and you are not installing software, click no".

[Ad-Aware][18] 
:   Ad-Aware is probably the most popular, and second-best to Spybot. However, they are in [hot water][19] with the anti-spyware community lately over the suspicion of selling out a few spyware vendors. It's an ongoing examination, so more to come on this front. 

[HiJackThis][20] 
:   HijackThis is **essential** for disinfecting a Windows PC badly overridden with spyware. It's a utility that scans for startup entries, browser helper objects, plugins and a myriad of other ways that spyware claws its way into your system. It will thoroughly clean things out of IE that can create an avenue for spyware even after you've cleansed it. Usually my first step is to run hijackthis to purify IE long enough to download firefox (of course, now I have it on this CD!). 

[CWShredder][21] 
:   CWShredder is an application designed specifically to remove a particularly nasty and insidious piece of spyware: CoolWebSearch. This one is so nasty most general spyware-removers have trouble getting it. It's a constant battle. 

[Startuplist][20] 
:   By the same developer of hijackthis. Gives you a comprehensive list of startup items.

[Micrsoft AntiSpyware (beta)][22] 
:   Microsoft's new anti-spyware beta. I haven't tested it extensively, but I put it on my CD. Giant's product is supposed to be very good, and MS bought it and based theirs on it, so I assume it is similar.

<a name="Software_Firewalls"></a>  


### Software Firewalls

[Visnetic Firewall][23] 
:   Finding a straight-forward software firewall for Windows that just lets you create basic filtering rules is difficult. This is the closest I've found and it does a good job. Most windows firewall software is application-centric, laying a foundation for which apps can do what. This is useful, but not always what you want. Sometimes you just need as close as you can get to a real firewall. 

[Sygate Personal][24] 
:   Sygate is probably the best of the free personal firewalls of the application-centric variety.

[Kerio Personal Firewall][25] 
:   Kerio personal firewall also comes highly recommended, although I have not used it extensively.

<a name="Utilities"></a>  


### Utilities

[TreeSizeSetup.exe][26] 
:   A lot of Windows applications are absolutely terrible about disk-space management and log rotation. (While it's rare that windows applications have logs at all, when they do, you can be assured that you'll only discover them, buried somewhere, when they grow until they fill your disk.). When this happens, the lack of an equivalent of the "du" (disk usage) command in UNIX is infuriating. This will give you that functionality.

[7zip][27] 
:   Courtesy of [Random][28], I was recommended 7zip as a free substitute for Winzip and it looks quite nice.

[winzip90.exe][29] 
:   Just in case 7zip doesn't work, winzip is on here as a fallback.

[TweakUiPowertoySetup.exe][30] 
:   The TweakUI program is always a good one for various system and performance modifications and the latest XP version is no slouch.

[X-teq X-Setup][31] 
:   Xteq's X-Setup program is like TweakUI on crack. It lets you change just about everything in the windows registry with a very nice interface. Careful though, it's got things that can hose you if you aren't cautious.

[Microsoft Uninstall Utility][32] 
:   An infuriating problem occurs when a program is broken badly and it won't even uninstall from the "Add/Remove Programs" interface. TweakUI used to at least have a function to remove it manually (but not the program itself). It doesn't anymore, but this program will do it also. This doesn't remove any data or registry settings, as far as I know, but it gets rid of it from the list at least. If anyone knows of a more comprehensive clean-up tool that will trash and burn a broken uninstallable application, let me know. The top hits on download.com for programs that do this are either poor excuses of a wrapper for the existing add/remove functionality or are badly written in other ways.

<a name="Registry"></a>  


### Registry

[Easy Cleaner][33] 
:   This registry cleaner comes highly recommended but I have not used it before. Proceed with caution, mucking with your registry can really screw things up.

[MS Regclean ( Only through Win2k)][34] 
:   This program is hard to track down, but it was Microsoft's registry cleaning utility. It only works up to Windows2000, but it seems to do a good job. Microsoft seems to be disavowing it, or something, as I can't find it on their actual site anywhere.

[Sysinternals utilities][35] 
:   I am not going to list them all here, but sysinternals has compiled a truly awesome collection of their custom-written utilities. I have them all on the CD. Check them out.

<a name="Clients"></a>  


### Clients

[TightVNC][36] 
:   Windows' built-in RDP connections are great and speedy but sometimes it's not an option, or you want an actual-desktop perspective. In this case, VNC is the way to go. TightVNC is the open-source version of VNC.

[RealVNC][37] 
:   RealVNC is the .. uh.. other .. version of VNC. I am unclear on the relationship. This one is also free but I guess not open-source. I actually use it before TightVNC these days because I have run into situations where tightvnc did not work for some reason and RealVNC did.

[putty][38] 
:   Putty is not really useful for my users in any way, but it's useful for me to have at my disposal so that I can have SSH around when I need it, which is almost always.

[Mozilla FireFox 1.0][39] 
:   Mozilla Firefox is the XUL-based re-written browser that is taking the world by storm. No, it's not perfect, nor is it completely free of its own security issues. But it's a lot better than IE. Trust me. There are very few reasons your average user should need to use IE over Firefox.

[Mozilla Thunderbird][40] 
:   For your basic POP3/IMAP-using mail user, there's really no excuse for them to be using Outlook when Thunderbird exists. (Okay, there is -- contacts and calendaring, but don't get me started). Outlook uses IE's rendering engine so is just as much a security hole as IE. It should be replaced whenever possible with Thunderbird.

<a name="Toolbars"></a>  


### Toolbars

[Google Toolbar][41] 
:   Although the reasons mystify me, some people seem unable or unwilling to give up their IE habit. In these cases, a good toolbar can at least block popups and provide **some** semblance of security relief. Google's is good.

<a href="http://toolbar.yahoo.com/" link="http://toolbar.yahoo.com/">Yahoo Toolbar</a>
:   Yahoo's is supposed to be good, too.

 [1]: #AntiVirus
 [2]: #Network
 [3]: #Spyware
 [4]: #Software_Firewalls
 [5]: #Utilities
 [6]: #Registry
 [7]: #Clients
 [8]: #Toolbars
 [9]: http://www.grisoft.com/ "http://www.grisoft.com/"
 [10]: http://www.avast.com/ "http://www.avast.com/"
 [11]: http://vil.nai.com/vil/stinger/ "http://vil.nai.com/vil/stinger/"
 [12]: http://www.speedguide.net/downloads.php "http://www.speedguide.net/downloads.php"
 [13]: http://winpcap.polito.it/ "http://winpcap.polito.it/"
 [14]: http://www.ethereal.com/ "http://www.ethereal.com/"
 [15]: http://www.snort.org/docs/tap/
 [16]: http://security.kolla.de/ "http://security.kolla.de/"
 [17]: http://windowssecrets.com/050127/#story1
 [18]: http://www.lavasoftusa.com/software/adaware/ "http://www.lavasoftusa.com/software/adaware/"
 [19]: http://www.broadbandreports.com/shownews/60449
 [20]: http://www.spywareinfo.com/~merijn/downloads.html "http://www.spywareinfo.com/~merijn/downloads.html"
 [21]: http://www.intermute.com/spysubtract/cwshredder_download.html "http://www.intermute.com/spysubtract/cwshredder download.html"
 [22]: http://www.microsoft.com/athome/security/spyware/software/default.mspx "http://www.microsoft.com/athome/security/spyware/software/default.mspx"
 [23]: http://www.deerfield.com/products/visnetic-firewall/ "http://www.deerfield.com/products/visnetic-firewall/"
 [24]: http://www.sygate.com/free/spf_download.htm "http://www.sygate.com/free/spf download.htm"
 [25]: http://www.kerio.com/us/kpf_home.html "http://www.kerio.com/us/kpf home.html"
 [26]: http://www.programmersheaven.com/zone16/cat762/20602.htm "http://www.programmersheaven.com/zone16/cat762/20602.htm"
 [27]: http://www.7-zip.org/ "http://www.7-zip.org/"
 [28]: http://www.livejournal.com/users/randomgang/
 [29]: http://www.winzip.com/ "http://www.winzip.com/"
 [30]: http://www.microsoft.com/windowsxp/downloads/powertoys/xppowertoys.mspx "http://www.microsoft.com/windowsxp/downloads/powertoys/xppowertoys.mspx"
 [31]: http://www.x-setup.net/ "http://www.x-setup.net/"
 [32]: http://support.microsoft.com/default.aspx?scid=kb;en-us;290301 "http://support.microsoft.com/default.aspx?scid=kb;en-us;290301"
 [33]: http://personal.inet.fi/business/toniarts/ecleane.htm "http://personal.inet.fi/business/toniarts/ecleane.htm"
 [34]: http://windows.about.com/library/regclean.exe "http://windows.about.com/library/regclean.exe"
 [35]: http://www.sysinternals.com/ntw2k/utilities.shtml "http://www.sysinternals.com/ntw2k/utilities.shtml"
 [36]: http://www.tightvnc.com/ "http://www.tightvnc.com/"
 [37]: http://www.realvnc.com/ "http://www.realvnc.com/"
 [38]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html "http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html"
 [39]: http://www.mozilla.org/products/firefox/ "http://www.mozilla.org/products/firefox/"
 [40]: http://www.mozilla.org/products/thunderbird/ "http://www.mozilla.org/products/thunderbird/"
 [41]: http://toolbar.google.com/ "http://toolbar.google.com/"