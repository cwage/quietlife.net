---
post_id: 449
title: backup pipe dreams
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=449
permalink: /2005/02/17/backup-pipe-dreams/
dsq_thread_id:
  - 350884640
categories:
  - geek
tags:
  - geek
---
So I'm increasingly annoyed with optical media for backups. It's slow, it's cumbersome, and it's just a PITA. Enough so that I find myself being really bad about doing backups.

I'm also increasingly atracted to hard-drive based backups. I could just buy a giant USB drive and regularly copy stuff to it, but that doesn't help me in a catastrophic failure (i.e. a fire). I'd like to at least be able to rotate something to my firesafe.

I learned recently that SATA is hotswappable (I think?). I then stumbled across [this device][1]:

<!--more-->

> MINI 3.5'' SATA Dual Drive Aluminum Enclosure with USB 2.0 Output
> 
> USBG-SATA-2US (selectable HARDWARE RAID 0 ro RADI 1)

Basically you put two SATA 3.5" drives in it, and it uses RAID-0 or RAID-1 and spits it out via USB (which I am assuming would work in linux with regular USB mass-storage).

Because it's using SATA, I am assuming this means it's hot-swappable which means you could just yank a drive out and it would keep operating. I also assume if you jammed a drive back in there it would rebuild the array on the replacement drive. (Assumptions are fun!)

If all of those assumptions hold true, that would mean I could buy, say, 3 200G SATA drives, that enclosure, + 2 extra trays (it comes with one) and have 200G of fully redundant storage via USB with one extra drive rotated regularly out to my firesafe:

<table border="0">
  <tr>
    <td>
      SATA Dual Drive Aluminum Enclosure:
    </td>
    
    <td>
      $290
    </td>
  </tr>
  
  <tr>
    <td>
      200G SATA drives * 3
    </td>
    
    <td>
      ~$400
    </td>
  </tr>
  
  <tr>
    <td>
      2 extra trays
    </td>
    
    <td>
      $60
    </td>
  </tr>
  
  <tr>
    <td>
      <b>Total:</b>
    </td>
    
    <td>
      <b>$750</b>
    </td>
  </tr>
</table>

Ouch. Okay, definitely out of my price range, but still pretty damn cool.

 [1]: http://www.cooldrives.com/nadusadrenwi.html