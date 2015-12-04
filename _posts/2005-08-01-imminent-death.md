---
post_id: 706
title: imminent death
author: cwage
layout: post
guid: http://chris.quietlife.net/?p=706
permalink: /2005/08/01/imminent-death/
dsq_thread_id:
  - 236778504
categories:
  - geek
tags:
  - geek
---
When you see things like this:

> top - 15:45:35 up 20:39, 0 users, load average: 313.01, 105.00, 54.96 

and this in dmesg:

> hda: drive_cmd: status=0x51 DriveReady SeekComplete Error  
> hda: drive_cmd: error=0x04 DriveStatusError 

<!--more-->

you know the end is nigh for a hard drive.. I guess the trauma of the move wasn't too good for this little guy. Well, it's like a 10 year old 6G drive -- it had a good run. It's the system drive for quietlife.net (the data itself is tucked away safely on LVM volumes on a much newer drive).

So, the question is, how should I proceed with moving to a new system drive. Should I:

a) dd if=/dev/hda of=/mnt/hdc5/image-of-drive.img; dd of=/dev/newdrive of=/mnt/hdc5/image-of-drive.img

This approach is appealing, since it means very little work of re-installing, but since of cousre the chances of my being able to actually buy another 6G drive these days are virtually nil, it means I'd have to re-size the partitions to take advantage of the rest of a, say, 40G drive, or just deal with wasting 34G, which sucks.

b) tar cfz /mnt/hdc5/tarball-of-drive.tgz; cd /mnt/newdrive/; tar xfz /mnt/hdc5/tarball-of-drive.tgz

This is appealing as well, since it means no actual re-installation. The downside is I'd have to manually partition the drive (this may be a plus, since my partitioning on the original drive was a little retarded) and re-run lilo.

c) Re-install Debian and just restore config files for everything from backup.

I think of all these b) is looking the most appealing. Of course, this all assumes that the old drive survives long enough and through the trauma of all that reading to actually accomplish any of these.