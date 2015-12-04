---
post_id: 186
title: Verisign Must Go
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=186
permalink: /2003/09/16/verisign-must-go/
dsq_thread_id:
  - 236777318
categories:
  - geek
tags:
  - geek
---
Verisign has pissed off the entire internet. Again.

[Verisign][1] is a company that purchased Network Solutions, a company that was vested with the authority to control the .COM and .NET top level domains (TLDs). Verisign has a history of [thoroughly deceptive and unethical business practices][2].

Now they've taken it to a new level. They have registered a wildcard (*) domain for .COM and .NET, meaning that **any** unregistered .com or .net domain will now resolve to 64.94.110.11 (sitefinder.verisign.com). This allows them to present a "domain not found" page of their own, conveniently allowing you to register it. That is, it's a giant advertising ploy.

Why is this such a big deal?

<!--more-->

From a purely technical/troubleshooting perspective:

  * Any typoed e-mail address resulting in a bogus domain name will go to verisign and result in a bounce (seems like this has legal implications, too). This bounce comes from a fake mailserver that violates their own best practices document, to boot. Pretty funny.
  * If you typo an MX record, any mail will bounce immediately (from verisign) rather than defaulting to secondary or tertiary MX records, etc
  * Numerous spam filtering problems may be caused by this.. People are already reporting issues with spamassassin and defunct RBLs coming back to life because they resolve as the verisign IP now, resulting in false positives and mail being marked as sent from an open relay, etc.
  * "host foobar.com" is no longer a sufficient check to see if a domain name is registered and working. You'll need to make sure the IP is right (not 64.94.110.11) and is actually registered in whois, etc.
  * A request for any website that is an unregistered domain name will no longer immediately return an error, but will redirect to sitefinder.verisign.com. Or, in some cases, like right now, it will just hang indefinitely because verisign's site is down.

From a moral/ethical perspective:

  * Verisign now has the means to monitor closely any traffic bound for a mistyped domain, on **any** service, but currently HTTP and SMTP.
  * For example, if I send mail to cwage@quitelife.net by accident, I get a bounce, and Verisign has my e-mail address in their logs. A tidy profit to sell to some spammers, to be sure.
  * If George W Bush goes to http://whaetehouse.com/military/nuke.html?user=dubbya&password=iluvwar, verisign now has this username and password logged. The amount of sensitive data they could have at their fingerprints is vast.
  * Verisign is the biggest trusted certificate authority. What's to stop them from answering SSL traffic, too? And to stop them from presenting valid certificates for these "accidental" domains as well.

The most hilarious part is from their [Terms of Service][3]:

> Sole Remedy.  
> YOUR USE OF THE VERISIGN SERVICES IS AT YOUR OWN RISK. IF YOU ARE DISSATISFIED WITH ANY OF THE MATERIALS, RESULTS OR OTHER CONTENTS OF THE VERISIGN SERVICES OR WITH THESE TERMS AND CONDITIONS, OUR PRIVACY STATEMENT, OR OTHER POLICIES, YOUR SOLE REMEDY IS TO DISCONTINUE USE OF THE VERISIGN SERVICES OR OUR SITE.

That's right, folks. If you're dissatisfied with this service that has been forced down the throats of the entire internet, discontinue use of it. It? The internet, I guess. Thanks, and come again!

The folks over at [NANOG][4] and [IETF][5] are [hoppin mad][6].

What can we do? Some people are proposing patching software, including BIND, to ignore results for Verisign's IP. There's a patch for BIND 8 [here][7], but I can't vouch for its functionality. People are contacting [Verisign][8] to complain. But, since that historically gets you nowhere, they are also contacting [ICANN][9].

Verisign has shown no ethical restraint whatsoever and has **repeatedly** shown no qualms about using its vested authority in the pursuit of commercial gains. They need to be stripped of this authority, and it needs to be given to a credible, and perhaps federally regulated, disinterested third party.

 [1]: http://www.verisign.com/
 [2]: http://directory.google.com/Top/Society/Issues/Business/Allegedly_Unethical_Firms/Verisign/
 [3]: http://sitefinder.verisign.com/terms.jsp
 [4]: http://marc.theaimsgroup.com/?l=nanog
 [5]: http://marc.theaimsgroup.com/?l=ietf
 [6]: http://marc.theaimsgroup.com/?l=nanog&m=106370054621019&w=2
 [7]: http://achurch.org/bind-verisign-patch.html
 [8]: http://www.verisign.com/corporate/about/contact/index.html
 [9]: http://www.icann.org/general/contact.htm