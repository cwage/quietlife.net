---
post_id: 273
title: Verisign vs ICANN
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=273
permalink: /2004/02/27/verisign-vs-icann/
dsq_thread_id:
  - 1314405965
categories:
  - geek
tags:
  - geek
---
As you may or may not have heard, [Verisign is suing ICANN][1]. If you want the short version, some less-comprehensive and more spite-fueled history can be found [here][2]. It's a long, torrid story, but I've tried to condense it here as best I could. If there are any corrections that need to be made, let me know -- I'm an engineer, not a historian:

<!--more-->

### ICANN

[ICANN][3] stands for "Internet Corporation For Assigned Names and Numbers". It's a pseudo-governmental entity -- technically a 501c3 non-profit corporation -- that was formed under the authority of the National Science Foundation (now under the Department of Commerce) in order to assume responsibility for the administration of four key areas [[1]][4]:

  * Assignment of numerical addresses to Internet users.
  * Management of the system of registering names for Internet users.
  * Operation of the root server system.
  * Protocol Assignment.

ICANN's true derivation of legal authority has always been a big question mark. Its charter is ambiguously worded, and it's unclear exactly whether or not ICANN is to be considered a governmental administrative organization. If it is, it's in breech of the [Federal Administrative Procedure Act][5], which it does not conform to. If it's not, this raises questions of its legitimacy as a private corporation with its own (profit or otherwise) motives that will continue to come into conflict with its actual charter. What is its main charter? ICANN [claims][6]:

> As a private-public partnership, ICANN is dedicated to preserving the operational stability of the Internet; to promoting competition; to achieving broad representation of global Internet communities; and to developing policy appropriate to its mission through bottom-up, consensus-based processes. 

### ICANN & Verisign

Historically, ICANN's relationship with Verisign has always been love/hate. ICANN originally contracted Network Solutions (which was bought by Verisign) in 1993 to administer the technical side of its authority, with [an agreement][7] that would expire in five years, in 1998. Since then, the agreement has been amended countless times, each time Verisign coming out as the winner with one hell of a sweetheart deal (despite some very favorable and often lower bids from other bidders).

Verisign has since gained a reputation of liberally mixing horrendous customer service with some pretty underhanded business practices. For a comprehensive list, see [their section][8] in Google's "Allegedly Unethical Firms" listing. Probably the most egregious example of this that many people have run into is their habit of sending out "domain expiration" notices to people whose domains are about to expire. Sounds like a convenient measure on their behalf, right? Except, the people they were mailing the notices to weren't their customers. They mailed them to competitor's customers. The form they mailed looked like a simple renewal form, and Verisign was betting (successfully) that most people would just sign it and drop the check in the mail. Only in the fine print did it point out that you were actually **transferring service** from whatever registrar you were with to them.

### Discontent with ICANN

The favored status that Verisign has continued to receive from ICANN, despite their behaviour, as well as other issues, has led to widespread discontent with the company. Although the company is supposed to represent "bottom-up, consensus-based process" and "broad representation of global Internet communities", some have been questioning its veracity. [ICANN Watch][9], a website that keeps an eye on ICANN (hence the name), lists some examples of questionable actions:

>   * Contrary to its early promises that half of its Board of Directors would be elected from an at-large membership, ICANN announced 
>       * that it [had no members][10], and 
>       * only 5 of 18 instead of 9 of 18 directors would be elected at large, and
>       * [four of the initial self-selected directors would stay in office][11] and
>       * ICANN would [conduct a study to determine whether there should be any member elected directors at all!][12]
>   * Most recently, ICANN identified [seven new gTLDs][13] to be added to the root. It declined to recommend 35 others. The selection process was [very controversial][14], and some of the losing applicants [protested][15]. In theory, the losing 35 may be considered later, depending on the experience with the first seven; ICANN, though, hasn't committed to a date for considering a second round.

### Verisign vs. ICANN

ICANN's relationship with Verisign has of late become more and more antagonistic, despite their favored status. Verisign, it seems, wants to get away with far more than ICANN will allow (which is substantial). In January, Verisign attempted to implement a system similar to sitefinder with international <acronym title="Top Level Domain">TLD</acronym>s, but backed down after its proposal was [shot down][16] by the IAB.

The big showdown came in September of 2003 when Verisign decided to roll out its SiteFinder "service". I put "service" in scare quotes because it was less of a service and more of a fundamental change in the way the Internet as we know it works. Verisign added a "wildcard" record in the root zones for .net, .com, and .org. What this means is that for every single domain that was not registered, an IP (Verisign's) was returned. So, if you typed in "thisisiadomainthatprobablydoesntexist.com" into your browser, instead of getting an error like normal, you would get Verisign's "SiteFinder" service, conveniently offering to sell you the domain. This effectively meant that there was no longer such a thing as a "nonexistent domain" for the .com, .net and .or zones.

Over the next few days, the realization of just how many things Verisign had broken began to become apparent. The IAB conveniently compiled a list [here][17]. Network administrators were furious. The first reaction by most was to null-route the Verisign IP so that, if nothing else, at least the traffic for formerly non-existent domains would go nowhere, rather than to Verisign. The developers of BIND, the most prevalent nameserver on the internet, at ISC quickly released a patch that would look for Verisign's IP returned from a domain and instead return an NXDomain like normal. This was a band-aid at best, though, because Verisign could simply change the IP at any time.

Perhaps the most surreal part of Verisign's behaviour was this part of their Terms of Service listed on the SiteFinder site:

> Sole Remedy.  
> YOUR USE OF THE VERISIGN SERVICES IS AT YOUR OWN RISK. IF YOU ARE DISSATISFIED WITH ANY OF THE MATERIALS, RESULTS OR OTHER CONTENTS OF THE VERISIGN SERVICES OR WITH THESE TERMS AND CONDITIONS, OUR PRIVACY STATEMENT, OR OTHER POLICIES, YOUR SOLE REMEDY IS TO DISCONTINUE USE OF THE VERISIGN SERVICES OR OUR SITE. 

That's right. They posted a ToS that recommends "discontinuing use" of the service they were brazenly forcing on the Internet itself.

After lengthy consideration (in the opinion of some, far too lengthy), ICANN issued a letter on October 3rd to Verisign demanding a ["return the operation of the .com and .net domains to their state before the 15 September changes, pending further technical, operational and legal evaluation"][18].

Shortly thereafter, Verisign complied and removed the wildcard from the zones.

To make a long story short, this is what the lawsuit is all about. Verisign is claiming that by forcing them to remove the SiteFinder "service", ICANN was overstepping its legal boundaries:

> "This brazen attempt by ICANN to assume 'regulatory power' over VeriSign's business is a serious abuse of ICANN's technical coordination function," said VeriSign in the suit, which was filed in U.S. court in Los Angeles. 

Now, as laughable and infuriating as it sounds to hear Verisign, of all companies, using the word "brazen" to refer to ICANN, the case may not be as open and shut, legally, as we may like -- if only because no one is really sure **what** ICANN is supposed to do. No doubt the role of ICANN will be at the very least clarified by this ruling -- perhaps modified or redefined. What's not really up for debate, however, is that Verisign was completely and utterly wrong in abusing their power. If there's any justice in the world, however, Verisign will get utterly shit-canned, having demonstrated their inability to be vested with any responsibility for a public good.

 [1]: http://slashdot.org/article.pl?sid=04/02/26/235256&mode=thread
 [2]: http://admin.quietlife.net/mt-search.cgi?IncludeBlogs=2&search=verisign
 [3]: http://www.icann.org/
 [4]: http://www.ntia.doc.gov/ntiahome/domainname/6_5_98dns.htm
 [5]: http://biotech.law.lsu.edu/Courses/study_aids/adlaw/
 [6]: http://www.icann.org/general/
 [7]: http://www.icann.org/nsi/coopagmt-01jan93.htm
 [8]: http://directory.google.com/Top/Society/Issues/Business/Allegedly_Unethical_Firms/Verisign/
 [9]: http://www.icannwatch.org/
 [10]: http://www.icann.org/general/bylaws-amend-redline-8oct99.htm
 [11]: http://personal.law.miami.edu/~froomkin/boardsquat.htm
 [12]: http://www.icann.org/committees/at-large-study/charter-22jan01.htm
 [13]: http://www.icann.org/tlds/
 [14]: http://www.internetdemocracyproject.org/DoClt1.htm
 [15]: http://www.icann.org/committees/reconsideration/index.html
 [16]: http://www.iab.org/documents/docs/icann-vgrs-response.html
 [17]: http://www.iab.org/documents/docs/2003-09-20-dns-wildcards.html
 [18]: http://www.icann.org/correspondence/twomey-to-lewis-03oct03.htm