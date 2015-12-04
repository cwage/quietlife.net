---
post_id: 354
title: Linux on a Dell X300
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=354
permalink: /2004/05/29/linux-on-a-dell-x300/
dsq_thread_id:
  - 236777676
categories:
  - geek
tags:
  - geek
---
This update is long in coming, mostly because I have been enjoying the new laptop (and using it to, you know.. work). Linux seems to be working almost entirely.

<!--more-->

  
**Distribution**

I am running [Debian testing/unstable][1], mostly because I needed certain things that only the latest [Debian Beta Installer][2] supported -- namely, the broadcom tg3 NIC driver and better support for my high-speed USB CDROM. More about that later. The new beta installer is quite impressive. Give it a try if you haven't. The only weird issue I have run into is that if you enter into the 2.6 kernel install, everything works great except that, in fact, it still installs a 2.4.x kernel. I'm sure that will get worked out in future releases. It is beta, after all.

### Kernel

First, let me say that my dedication to the 2.4.x kernel took a hit with this laptop. I spent a lot of time fighting with it before moving to 2.6.6 and almost everything **just works**. Save yourself some time. The x300 has enough whacky new hardware that 2.6.x is a much better fit.

So, without further ado, here's what works and what doesn't:

ACPI
:   I might as well start with the first abject failure. I couldn't get ACPI to work for shit. Some things work (the processor, for one) marginally but the rest of the modules bombed out with odd errors. I tried various combinations of patches and DSDT replacements as per advice on [acpi.sourceforge.net][3], but nothing seemed to help. To make matters worse, the enabling of ACPI in the kernel in fact disables the dell "function" keys on the keyboard. This includes things like dimming/brightening the LCD, turning the wireless antenna on/off, switching from CRT to LCD, etc. These all now simply handed unhandled scancodes to the kernel. Not having those was unacceptable so my kernel currently has ACPI disabled.

APM
:   APM is the older alternative to ACPI for power management. There is no APM support in the BIOS (A06 as of writing) for the Dell X300. Bummer. I have no access in software to the battery/AC plug status. However, Dell does include a handy-dandy LED button on the back to see the strength of the battery so this is not a huge deal.

CPU Scaling
:   Although ACPI is the usual method for handling CPU frequency scaling (for power-saving), the 2.6.x linux kernel actually has support for this independently of it (CONFIG\_CPU\_FREQ, et al under the power management features). [cpudynd][4] is handy for toggling this based on usage of the laptop, but unfortunately it can't be smart enough to toggle it based on the AC being plugged in or not because, well, no ACPI. Still, you can toggle it manually with *echo "powersave" > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor*.

Synaptics touchpad
:   The Synaptics touchpad is detected by the kernel fine, and works fine as "PS/2" in XFree86, however for the touchpad tap functionality you'll want the [touchpad driver for XFree86][5] to use instead of PS/2.

USB
:   USB 2.0 ( CONFIG\_USB\_EHCI\_HCD) support works well in 2.6.x, unlike in 2.4.x, where it is still experimental and tends to crash a lot. ehci\_hcd is necessary for my USB CDROM, and I also load uhci_hcd and usb-storage for my USB keychain drive, which I use via autofs. (More about this [here][6].) For device detection and module loading, I switched from [usbmgr][7] to hotplug, which seems to work better with 2.6.

Broadcom BCM5705M 10/100/1000 NIC
:   This works great with the Broadcom Tigon3 driver (CONFIG_TIGON3). No problem.

Wireless
:   Dell gives you the option of going with their Dell mini-PCI wireless cards or Intel's 2100 or 2200. I opted for the Intel 2200, because it does 802.11g as well as b, however the downside is that there is no native driver for this card in Linux yet. There is [a project][8] already in the works to write them, but it's only a few weeks old and much less mature than its [sister project][9] for the intel 2100.</p> 
    
    The solution is the very clever idea of writing a wrapper for the windows driver itself. There are two implementations of this idea: [ndiswrapper][10], which is free, and [Linuxant Driverloader][11], which is not. Both of them require the Windows drivers, which you can find [here][12].
    
    I used ndiswrapper with success for a while, however it didn't work after loading the module until I set the ESSID and turned the antenna off and then back on (with the Dell function key -- you can see why ACPI disabling this was particularly crippling now). It also didn't work with WEP. I simply got "invalid argument" trying to set the WEP key.
    
    Both of these issues were fixed with the Linuxant driverloader wrapper, which I am using the 30-day free trial of, but will definitely be purchasing. </dd> 
    
    Sound
    :   The sound card in the Dell x300 is ac97 compatible and works fine with the alsa support in 2.6.x for the intel 810 chipset (CONFIG\_SND\_INTEL8X0). One weird thing I haven't quite figured out yet is why xmix seems to use /dev/mixer fine but gkrellm's volume plugin complains about it. I haven't messed with it because dealing with sound in Linux generally makes me want to open my wrists.</dl> 
    
    You can find my kernel config [here][13].
    
    ### XFree86
    
    I am amazed these days how well running "X -configure" seems to work. The resulting config is what I started with, and it was a simple matter of fixing the mouse pointer (first as PS/2 and later as the synaptics driver) and I was up and running.
    
    My [XF86Config-4][14].

 [1]: http://www.debian.org/releases/testing/
 [2]: http://www.debian.org/devel/debian-installer/
 [3]: http://acpi.sourceforge.net/
 [4]: http://mnm.uib.es/~gallir/cpudyn/
 [5]: http://w1.894.telia.com/~u89404340/touchpad/
 [6]: http://chris.quietlife.net/archives/000312.html
 [7]: http://www.dotaster.com/~shuu/linux/usbmgr/
 [8]: http://ipw2200.sourceforge.net/
 [9]: http://ipw2100.sourceforge.net/
 [10]: http://ndiswrapper.sourceforge.net/
 [11]: http://www.linuxant.com/driverloader/
 [12]: ftp://ftp.vaio-link.com/pub/Vaio/WLAN/WLD_int_80129000.exe
 [13]: http://chris.quietlife.net/x300/config-2.6.6.052904
 [14]: http://chris.quietlife.net/x300/XF86Config-4