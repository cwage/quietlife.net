---
post_id: 1792
title: OpenBSD on alix2c0
author: cwage
layout: post
guid: http://chris.quietlife.net/2008/03/27/openbsd-on-alix2c0/
permalink: /2008/03/27/openbsd-on-alix2c0/
ljID:
  - 954
dsq_thread_id:
  - 236782329
categories:
  - misc
tags:
  - alix
  - alix2c0
  - embedded
  - geek
  - openbsd
  - soekris
---
I recently bought a [alix2c0][1] board and enclosure as a cheaper alternative to my preferred (but somewhat pricier) [Soekris Net4501][2] platform for running OpenBSD for a local firewall/router. I didn't have a modern copy of OpenBSD anymore (my current firewall is still running 3.9), so I didn't have a convenient platform to use [flashdist][3] to dump a working install onto the CF card. Such a thing was necessary back in the day when I was dealing with 64M of space, because you had to be Really Picky (pickier than the barebones install) about what you install. Now, however, I am recycling a 1G CF card for my firewall (I just bought 2 new 4G CF cards for photography, w00t), so I have a reasonable amount of space. I figured I'd try a more standard install. Here were the steps I took:

  * Enable tfp on my firewall in inetd by uncommenting:  
    > tftp dgram udp wait root /usr/libexec/tftpd tftpd -s /tftpboot 

  * kill -HUP inetd
  * added this to /etc/dhcpd.conf:  
    > filename "pxeboot"; 
    
    See the [OpenBSD FAQ section on PXE booting][4] for more on this. (as well as the following steps) </li> 
    
      * kill -HUP dhcpd
      * Hook up the alix2c0 board via a serial null modem (38400, 8N1, no flow control) and turn it on. Hit 'S' during the memory test to enable setup. Hit 'E' to enable PXE/network boot and quit, saving the settings.
      * Grab [pxeboot][5] and [bsd.rd][6] for the version of OpenBSD you want to install
      * Put those two files in a directory called /tftpboot on your dhcpd/tfp server (as referenced in inetd.conf above), along with a /tftpboot/etc/boot.conf with the following:  
        > set tty com0  
        > stty com0 38400  
        > boot bsd.rd 
    
      * Reboot your alix2c0, and it should request an IP via DHCP and then start requesting the aforementioned files via TFTP. If all goes well, it should switch the console to com0, grab bsd.rd and boot you into the OpenBSD kernel with a ramdisk that will dump you into the normal install process. Voila!</ul>

 [1]: http://www.pcengines.ch/alix2c0.htm
 [2]: http://soekris.com/net4501.htm
 [3]: http://www.nmedia.net/flashdist/
 [4]: http://www.openbsd.org/faq/faq6.html#PXE
 [5]: ftp://ftp5.usa.openbsd.org/pub/OpenBSD/4.2/i386/pxeboot
 [6]: ftp://ftp5.usa.openbsd.org/pub/OpenBSD/4.2/i386/bsd.rd