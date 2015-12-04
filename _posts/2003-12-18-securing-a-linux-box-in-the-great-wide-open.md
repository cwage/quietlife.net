---
post_id: 224
title: Securing a Linux box in the Great Wide Open
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=224
permalink: /2003/12/18/securing-a-linux-box-in-the-great-wide-open/
dsq_thread_id:
  - 236777389
categories:
  - geek
tags:
  - geek
---
Ideally, any GNU/Linux server should be behind a firewall. However, sometimes you don't have a choice. My nameservers are great examples of this -- they just aren't in places where a firewall is practical, and Cisco IOS ACLs are an unsavory alternative because they are easily (inadvertently) blown away.

So, it's important to know how to secure GNU/Linux so that you can confidently put it on the Internet without fear of compromise. It's not as difficult as it may seem.

<!--more-->

No matter what distribution you choose, it's inevitable that it will probably install with more services than you actually need running. The first step, then, is to portscan the server from another machine. (At this point, you should be on a private, protected network behind a firewall -- if you already have the server up and running, open on the internet, it's already too late.) Here's an example, using a newly installed Debian 3.0 server at 192.168.0.6:

<pre>root@scanbox:~# nmap -sS -p 1-65535 192.168.0.6

Starting nmap 3.48 ( http://www.insecure.org/nmap/ ) at 2003-11-06 11:25 CST
Interesting ports on host06.quietlife.net (192.168.0.6):
(The 65523 ports scanned but not shown below are in state: closed)
PORT     STATE SERVICE
9/tcp    open  discard
13/tcp   open  daytime
21/tcp   open  ftp
22/tcp   open  ssh
23/tcp   open  telnet
25/tcp   open  smtp
37/tcp   open  time
79/tcp   open  finger
111/tcp  open  rpcbind
113/tcp  open  auth
515/tcp  open  printer
1026/tcp open  LSA-or-nterm

Nmap run completed -- 1 IP address (1 host up) scanned in 7.759 seconds
</pre>

As you can see, there are quite a few ports open. All these services, without exception, are controlled by daemons running that are spawned from scripts in /etc/init.d/ during startup. The solution then is to isolate the services we don't require and turn them off (and remove the software if it is unnecessary). Let's say we are setting up a DNS server. In the end, we will want nothing but port 22/tcp and 53/udp open.

First, services like "9/tcp open discard" and "13/tcp open daytime" are services run by inetd. inetd is a daemon itself that encompasses many different services, all of which we don't need. Let's turn it off:

<pre>testbox:~# /etc/init.d/inetd stop
Stopping internet superserver: inetd.
</pre>

Now, let's see what nmap looks like:

<pre>root@scanbox:~# nmap -sS -p 1-65535 192.168.0.6

Starting nmap 3.48 ( http://www.insecure.org/nmap/ ) at 2003-11-06 11:31 CST
Interesting ports on host06.quietlife.net (192.168.0.6):
(The 65532 ports scanned but not shown below are in state: closed)
PORT     STATE SERVICE
22/tcp   open  ssh
111/tcp  open  rpcbind
1026/tcp open  LSA-or-nterm

Nmap run completed -- 1 IP address (1 host up) scanned in 7.602 seconds
</pre>

Pretty impressive -- already we have gotten rid of 8 open services, none of which we require. To be thorough, let's go ahead and remove inetd, since we won't be needing it:

<pre>testbox:~# dpkg -l | grep inetd
ii  netkit-inetd   0.10-9         The Internet Superserver
testbox:~# apt-get remove netkit-inetd
Reading Package Lists... Done
Building Dependency Tree... Done
The following packages will be REMOVED:
  fingerd ftpd lpr netbase netkit-inetd pidentd ppp pppconfig pppoe pppoeconf
  talkd telnetd ytalk
0 packages upgraded, 0 newly installed, 13 to remove and 0  not upgraded.
Need to get 0B of archives. After unpacking 2704kB will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 19451 files and directories currently installed.)
Removing fingerd ...
Removing ftpd ...
Removing lpr ...
Stopping printer spooler: lpd.
Removing pppoeconf ...
Removing pppoe ...
Removing pppconfig ...
Removing ppp ...
Stopping all PPP connections...No /usr/sbin/pppd found running; none killed.
done.
dpkg - warning: while removing ppp, directory `/etc/chatscripts' not empty so not removed.
dpkg - warning: while removing ppp, directory `/etc/ppp/ip-down.d' not empty so not removed.
dpkg - warning: while removing ppp, directory `/etc/ppp/peers' not empty so not removed.
Removing pidentd ...
Removing ytalk ...
Removing talkd ...
Removing telnetd ...
Removing netbase ...
Removing netkit-inetd ...
Stopping internet superserver: inetd.
testbox:/etc/init.d# dpkg --purge netkit-inetd
(Reading database ... 19266 files and directories currently installed.)
Removing netkit-inetd ...
Purging configuration files for netkit-inetd ...

</pre>

Now, let's return to our nmap. We still have two services running that we don't require: "111/rpcbind", and "1026/tcp LSA-or-nterm". How do we figure out what daemons are holding those ports open? Enter "lsof". lsof is a program that lists detailed information about files and sockets held open by processes. The output of lsof for open ports will have a line with "LISTEN" in it, which is what we will grep for with "lsof -n" (-n turns off name resolution so it won't hang trying to reverse DNS query IP addresses):

<pre>testbox:~# lsof -n | grep LISTEN
portmap   2642  root    4u  IPv4      19541               TCP *:sunrpc (LISTEN)
rpc.statd 2649  root    5u  IPv4      19625               TCP *:1026 (LISTEN)
sshd      2738  root    4u  IPv4      19782               TCP *:ssh (LISTEN)
</pre>

Now we can see the two daemons responsible for those ports: portmap and rpc.statd. But how do we turn them off? First, we need to find out what init.d script starts them:

<pre>testbox:~# cd /etc/init.d/
testbox:/etc/init.d# egrep -l 'rpc.statd|portmap' *
mountnfs.sh
nfs-common
portmap
</pre>

There you go. It appears that these are both NFS-related services. If you need NFS, naturally, you should leave these alone, but since we don't for our nameserver, we will stop them:

<pre>testbox:/etc/init.d# /etc/init.d/portmap stop
Stopping portmap daemon: portmap.
testbox:/etc/init.d# /etc/init.d/nfs-common stop
Stopping NFS common utilities: statd.
</pre>

You never know when you might need NFS in the future, so I am not going to uninstall it entirely, but we don't want it starting up on reboots in the future, either, so here is how you can remove it from startup:

<pre>testbox:/etc/init.d# update-rc.d -f portmap remove
update-rc.d: /etc/init.d/portmap exists during rc.d purge (continuing)
 Removing any system startup links for /etc/init.d/portmap ...
   /etc/rc0.d/S10portmap
   /etc/rc6.d/S10portmap
   /etc/rcS.d/S41portmap
testbox:/etc/init.d# update-rc.d -f nfs-common remove
update-rc.d: /etc/init.d/nfs-common exists during rc.d purge (continuing)
 Removing any system startup links for /etc/init.d/nfs-common ...
   /etc/rc0.d/K81nfs-common
   /etc/rc1.d/K81nfs-common
   /etc/rc2.d/S19nfs-common
   /etc/rc3.d/S19nfs-common
   /etc/rc4.d/S19nfs-common
   /etc/rc5.d/S19nfs-common
   /etc/rc6.d/K81nfs-common
</pre>

Now these services are stopped, and won't start up on boot. Let's check out "lsof -n" again:

<pre>testbox:/etc/init.d# lsof -n | grep LISTEN
portmap   2642  root    4u  IPv4      19541               TCP *:sunrpc (LISTEN)
sshd      2738  root    4u  IPv4      19782               TCP *:ssh (LISTEN)
</pre>

Hm, that's odd. "portmap" is still running, even though we shut it down. Sometimes, you have to be a little more rude. The second column lists the PID, 2642, so let's kill it:

<pre>testbox:/etc/init.d# kill -9 2642
testbox:/etc/init.d# lsof -n | grep LISTEN
sshd      2738  root    4u  IPv4      19782               TCP *:ssh (LISTEN)
</pre>

Now we can see that only one port is being held open for SSH. We're looking good. Let's doublecheck the portscan to confirm:

<pre>root@scanbox:~# nmap -sS -p 1-65535 192.168.0.6

Starting nmap 3.48 ( http://www.insecure.org/nmap/ ) at 2003-11-06 11:55 CST
Interesting ports on host06.quietlife.net (192.168.0.6):
(The 65534 ports scanned but not shown below are in state: closed)
PORT   STATE SERVICE
22/tcp open  ssh

Nmap run completed -- 1 IP address (1 host up) scanned in 7.376 seconds
</pre>

Looks good! Now let's check "lsof -n" one more time, but this time, we'll look for UDP services, to make sure they are shut down too. We could use nmap to scan for UDP with the "-sU" flag instead of "-sS" but UDP scans are **extremely** slow. This is because [RFC 1812][1] suggests that ICMP error messages be rate-limited, and most operating systems comply. So, we'll just check directly:

<pre>testbox:/etc/init.d# lsof -n | grep UDP
dhclient-  124  root    6u  IPv4         79               UDP *:bootpc
</pre>

Hm, bootpc is listening for DHCP broadcasts. That's okay -- I used DHCP to configure this box on my LAN, but once I put it into production, it will have a static IP and dhclient will not be running.

Now for the last step. Sometimes, even this level of lockdown is sufficient, but there is a lot of information to be gleaned even from normal TCP connection refusals (such as OS fingerprinting and TCP sequence vulnerability). Further, one of the most common tactics in compromising a server is to find a vulnerable service being run (sshd, for example), and get a root shell. The second step is usually to install a root shell listening on a higher, discreet port. By doing this, the attacker gains unfettered access to the box on this port. This is done because often, compromising something like sshd is a one-shot deal, and the daemon will subsequently crash.

To combat this potential, we can go a second step and configure our server to drop packets except destined for services we determine. In GNU/Linux this is done with "iptables" (ipchains is an older form of the same thing in 2.2.x kernels which is highly deprecated). I'll provide a good skeleton script for doing this in an forthcoming entry.

 [1]: http://www.faqs.org/rfcs/rfc1812.html