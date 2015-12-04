---
post_id: 101
title: Why Trillian Sucks
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=101
permalink: /2002/03/09/why-trillian-sucks/
dsq_thread_id:
  - 236773708
categories:
  - geek
tags:
  - geek
---
[Trillian][1] is a waste of time and resources.  
<!--more-->

Now that I've got your attention, let me say first of all: No, Trillian doesn't **SUCK** across the board. It's a good product written by good people with good intentions. I personally think the UI is written poorly, and it has its bugs, but considering the developers probably spend most of their time hacking around [AOL][2]'s blocks, that's forgivable. The problem is that Trillian is only a bandaid. It's a kludge. It's a waste of time and resources that could be invested in something that is a more comprehensive, standardized solution. Something that comes much closer to being exactly that is [Jabber][3]. However, development of Jabber is faltering amidst the prolific use of Trillian, which is doomed to eventually fail as a solution, and is only prolonging the inevitable.

Trillian surfaced during the heyday of IM clients. To people that found themselves installing 3, 4, and sometimes more IM clients, it was a gift from heaven. Blessed consolidation. I used it too, don't get me wrong, but it reminded me of a technology already being developed -- Jabber -- but I will get to that later. Trillian is one client that connects to multiple IM services, by implementing all the protocols and consolidating them. However, as Trillian's popularity skyrocketed, several of the companies offering IM services took notice -- namely, AOL. There was a period of turmoil where AOL continually blocked Trillian clients from connecting to their service, sending down a message advising them to download an authorized client and reconnect. Trillian would respond remarkably quickly with a fix, and a patch, and AOL would return in kind, finding a way to block that. This went on for almost a week, with a patch every day. It was ridiculous. It has calmed down now, but it can only be the eye of the storm. AOL is in all likelihood developing new additions to their client and service that will prevent Trillian (or any other third party client) from ever hoping to connect. And I find it hard to believe that others aren't considering the same course of action. This is why Trillian is ultimately doomed. The various proprietary IM servers will continue to do everything in their power to prevent third party clients from connecting -- and since they own the servers, they will have no trouble doing so effectively. Trillian is a bandaid at best, and will eventually be rendered useless.

The solution? Jabber. Firstly, let me make it clear that I am not defending the current state of the usability of Jabber's clients or servers. Rather, I am defending the technology and the protocol -- the idea, and the potential. What is it? From [jabber.org's FAQ][4]: "Jabber is a set of XML-based protocols for real-time messaging and presence notification." A simple solution for a simple problem. Furthermore, it's open-source. I will not get too deep into the details of how Jabber works, but the biggest difference requires a change of mentality from how most IM clients work. In the past, all IM clients have been strictly client to server, and so is Jabber, except that there is not just one server. Rather, servers are set up on an organizational basis, just as an e-mail server, or a web server is. There would be (ideally) public servers, private servers, corporate servers, etc. Rather than having a nickname, you have a name@im.mycompany.com exactly like an e-mail address. (This also eliminates the nickname-selection quandary -- no more ChrisWage22423).

The impetus behind Jabber is the need for standardization. Around every system of successful solution is the implementation of a robust standard for communication. This is why we have standards for nearly every method of communication on the internet currently -- except for IM. Why should this be an exception? It shouldn't.

However, the developers of Jabber were not so naive to think that people would quit various proprietary IM services cold-turkey and switch to jabber. Naturally, that would never happen. So, Jabber, like Trillian, supports communication to other IM services as well. However, it is done server-side, with the use of "Agents". You first connect to the Jabber server and then bridge over to other IM clients via the agents.

Let me paint the picture of a scenario that demonstrates where Jabber would be ultimately preferrable over Trillian. Many people at my workplace use IM for internal communication, and a good majority of those people use Trillian. The majority of this communication happened over the AIM protocol. Naturally, when it was continually disconnected it was quite problematic for us to communicate. Now, if all the people that were using Trillian were using Jabber instead, this wouldn't have been a problem. If AOL had prevented service from our jabber server, we would have still been able to communicate just fine using Jabber itself. This is the critical difference. It provides an alternative. It provides a method for transition. It provides a **standard** to make any proprietary solution ultimately obsolete.

However, all is not well in the land of Jabber development. Honestly, from where I sit, it's stagnant. The last major release of the server was over a year ago. The state of the clients for both Windows and UNIX is mediocre at best. They crash often and they work poorly. You have to be a very savvy UNIX sysadmin and familiar with XML to even consider getting a server up and running and to get it talking to other IM protocols (which is helpful for transition). Quite frankly, using jabber is a real pain in the butkus, which is unfortunate, because it's exactly the solution we all need.

This is why Trillian sucks. The resources that are invested day to day into keeping Trillian talking to AIM are ultimately fruitless and pointless. It's an exercise in futility. These same resources could be used in order to spark momentum in the development of Jabber. Hardly anyone uses Jabber, currently. They don't use it because they don't need it. They have Trillian. But they won't for long. Instead of slapping a bandaid on a horrendous problem, and letting proprietary protocols dictate our patterns of communication and cause problems, we could be working together to develop an alternative standard that would benefit everyone.

So what's the answer? Give Jabber a try. Join the mailing list. When things don't work right, let people know. Yell and scream and holler. But use it. Down the road, eventually the proprietary IM services will get the upper hand, and Trillian will be all but useless. We will be back to square one. Why not get the jump on developing a better solution?

Relevant links:

  * [http://www.jabber.org][3]
  * <http://www.jabber.com/>
  * [Winjab][5] - a Windows Jabber client
  * [Gabber][6] - a GNU/Linux jabber client for use with GNOME
  * <http://www.jabbercentral.org/clients/>JabberCentral's comprehensive list of clients
  * <http://www.jabberview.com/> - a list of active jabber servers and their status

 [1]: http://www.ceruleanstudios.com/
 [2]: http://www.aol.com
 [3]: http://www.jabber.org/
 [4]: http://www.jabber.org/faq.html
 [5]: http://winjab.sourceforge.net/
 [6]: http://gabber.sourceforge.net/