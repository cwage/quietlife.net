---
post_id: 262
title: johnkerry.com and referral spam
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=262
permalink: /2004/02/23/johnkerrycom-and-referral-spam/
dsq_thread_id:
  - 236777484
categories:
  - misc
tags:
  - misc
---
An update on this. An astute reader left a comment on my comment about the referral spam I received from blog.johnkerry.com:

> There is another possibility, of course - someone could be "Joe Jobbing" the campaign. Trying to set up the Kerry campaign to LOOK like spammers.
> 
> I'm not sure which one I believe - I've written to to info@ and webmaster@ too asking the question, but haven't heard anything back. I'd say both possibilities are equally likely at this point. In digging through my logs a bit more, I've found other StarProse referral spam, all from Democratic candidates. When campaigns as diverse as Kerry, Edwards, and Al Sharpton are showing up with the same software and the same general layout, it raises my suspicions a bit more for the Joe-Job. 

Indeed.

What I know about the spam is that it's being generated with [this software][1]. So, I first searched for that in the User-Agent. These are the hits I got:  
<!--more-->

<table>
  <tr>
    <td>
      IP Address
    </td>
    
    <td>
      Referrer
    </td>
    
    <td>
      Count
    </td>
  </tr>
  
  <tr>
    <td>
      206.65.72.35
    </td>
    
    <td>
      "http://www.blog.johnkerry.com"
    </td>
    
    <td>
      179
    </td>
  </tr>
  
  <tr>
    <td>
      172.144.61.107
    </td>
    
    <td>
      "http://blog.johnkerry.com"
    </td>
    
    <td>
      4
    </td>
  </tr>
  
  <tr>
    <td>
      172.144.61.107
    </td>
    
    <td>
      "http://www.johnedwards2004.com/"
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      206.129.0.134
    </td>
    
    <td>
      "http://www.riaa.com"
    </td>
    
    <td>
      2
    </td>
  </tr>
  
  <tr>
    <td>
      206.65.72.35
    </td>
    
    <td>
      "http://blog.johnkerry.com"
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      172.200.37.120
    </td>
    
    <td>
      "http://blog.johnkerry.com"
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      172.166.255.186
    </td>
    
    <td>
      "http://blog.johnkerry.com"
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      172.164.250.206
    </td>
    
    <td>
      "http://www.drudgereport.com/"
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      172.155.141.2
    </td>
    
    <td>
      "http://www.blog.johnkerry.com"
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      172.145.188.80
    </td>
    
    <td>
      "http://www.joe2004.com"
    </td>
    
    <td>
      1
    </td>
  </tr>
  
  <tr>
    <td>
      172.140.68.49
    </td>
    
    <td>
      "http://blog.johnkerry.com"
    </td>
    
    <td>
      1
    </td>
  </tr>
</table>

Notice that the same AOL IP (172.144.61.107) spammed for Kerry's and Edwards' websites, and also that the IP with the largest number of hits is 206.65.72.35, a "bess proxy" (basically, an open web cache/content filter that can be used to relay traffic).

Judging from this, I can make one conclusion: whoever is doing this is probably **not affiliated** with the John Kerry campaign (because of the hit for the Edwards site from the same IP).

Instead, I think there are a few possibilities:

  1. Some industrious tard is spamming on behalf of Democrats because he thinks it's genuinely a good idea
  2. Someone is purposefully trying to make it look like democratic candidates are spamming for their websites. "Joe-Jobbing" it, as Wade put it.

Frankly, I find 1) pretty unlikely, and given the odd appearance of spam for drudgereport.com from the same block of AOL IPs, I think 2) is the most likely scenario.

That's pretty low.

 [1]: http://www.fileheaven.com/Referrer-Advertising-System/download/10760.htm