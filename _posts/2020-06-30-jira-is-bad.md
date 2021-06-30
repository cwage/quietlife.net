---
post_id: 4250
title: jira is bad
author: cwage
layout: post
guid: http://quietlife.net/?p=4250
permalink: /2020/06/30/jira-is-bad
categories:
  - Uncategorized
tags:
  - jira
  - software
---

Intro
-----

Disclaimer: I am not a project manager. I'm a devops/SRE/security type guy. I could barely explain to you the difference between "agile" and "waterfall" (in practice, anyway). These opinions come from someone that has spent 20 some odd years using every manner of PM tool under the sun in some capacity -- whether as a manager, a developer, an engineer, or all of the above. This is not a solution or a manifesto (I think). It's ungenerous, a complaint, an airing of grievances and a summary of my PTJD (Post Traumatic Jira Disorder).

Jira
----

Jira is an issue tracking, bug management and project management tool. Doesn't sound so bad, does it? But, many people hate Jira. Some people (me) loathe it with the fire of a thousand suns. I won't get into the nitpicky reasons that a lot of people cite for disliking Jira: lack of certain features, things implemented poorly, the choice of Java, etc. These are all valid, but they are points of contention you'll always have with such software. Debates around the merits of various PM tools have existed since the dawn of software engineering and will never go away.

Here are some links to such critiques:

* [Why Jira Sucks](https://whyjirasucks.com/)
* [Why Jira Is an Anti-Pattern](https://techcrunch.com/2018/12/09/jira-is-an-antipattern/)

Instead, I want to talk more about the Jira mindset as it pertains to project management specifically, and how it affects organizations. Jira has other functionality which is "fine" but not at the root of the problem. I will quote part of the top comment on [a hackernews post](https://news.ycombinator.com/item?id=25590846) about one of the above articles that I think gets into the meat of it:

> To me, what sucks about JIRA (and would suck about any well-designed tool that replaces it) is not "feature x" but the entire JIRA mentality. All of it. It encourages micro-management. It encourages more and more process. It is the enemy of getting better at the DORA metrics, which requires streamlining process. tickets in JIRA are not the work itself, never was and never will be, it is a LARP of the work, but it gets taken for the central thing. This is an illusion. Fixing a bug without filing a JIRA ticket is in itself progress. Moving a JIRA card without any other change is not. Yet the second is what's visible and therefor what's rewarded. Any problem gets solved with "more JIRA " which stops working when the remaining problems are caused by too much JIRA. And yet they keep trying, because it gives "control". JIRA is a like metastatic tumour that will grow until it kills the host.

Project Management
------------------

Let's say you're writing some software. You've got a handful of developers and a sourcecode repository and everything is going swimmingly. One day, you add a few more developers and find your team getting confused. There's no consensus on what "we" should be working on as a whole, or individually. You need Project Management! In its simplest form this can be accomplished trivially with a spreadsheet or even sticky notes on a wall in various categories, much like a basic TODO list:

TODO -> Doing -> Done

You assign things to people, move cards around to reflect reality, and everything is peachy. This is basically what Trello is in digital form, and what github issues nabbed for its PM tool as well.

Customization
-------------

What happens next is not surprising: A simple workflow is great, but sometimes you want more info. What if I want a category to reflect "things we were doing but temporarily stopped, so they technically go back into TODO but really are more important", i.e. a "Backburner" status. What if you could "tag" things with metadata? What if you could "group" these todo items into discrete projects somehow. Jira (and many other tools, including trello, to some extent!) chose to support this by adding a powerful and deep ability to customize nearly everything. This affords you a lot of flexibility in creating a workflow in Jira to reflect nearly any internal process. Workflows from the simplest small agile development team to the biggest, most complicated NASA-level complexity waterfall process you can imagine (who, to be honest, might genuinely need something as customizable as Jira). Great, right? But now you find yourself and the other developers spending a non-zero amount of time futzing with your PM software workflow.

Enter the Project Manager
-------------------------

Almost every company has one or more Project Manager employees. Some are good, some are bad. Some are technical leads, some are not. Sometimes it's the developers themselves, but at the end of the day, if you're using a PM tool, someone is "managing" it. A necessary evil, perhaps, but updating, organizing and refining workflows is what we all do to some degree when using a PM tool, and it comprises some portion of your time at work. A friend of mine was fond of focusing on the difference between "working at the job" (i.e. doing your core competency that you were hired for) vs "working on the job" (i.e. time spent on non-core-competency things: checking email, meetings, etc. and of course project management). "Working on the job" is always gonna happen, but obviously you want to minimize it, and this includes time spent in and on project management related stuff. I continue to use the second-person pronoun "You" here to refer to a "project manager" because we're all project managers one way or another and this is not an us-vs-them screed.

Jira Enables and Encourages Complexity
--------------------------------------

The fact that Jira can be infinitely customized makes it very tempting for a project manager to use it to track the "on the ground" reality of what people are working on. You tweak the workflow endlessly. You refactor it from scratch to reflect the Shiny New Workflow you imagined in the shower that morning that will make things much better. It feels good. You've got the solution that finally will let everyone update and observe the reality of a project's progress. You start to get a small rush from finding a new way to tweak the workflow. The problem is that a complex/complicated process that you create is often not scrutable to others because, well, they didn't make it and aren't intimately familiar with it. Anyone who has spent a lot of time making complicated spreadsheets is probably familiar with this. You spend 2 days making a super-awesome spreadsheet and show it off to your coworkers and get blank stares and yawns because it's complicated and they have shit to do.

The Dopamine Hit 
----------------

Despite my aversion to Jira, over the years, I've tried to suck it up and use it. I've really tried. I remember one particular job using Jira extensively, where I had boards and issue backlogs from years prior (before I was even an employee) that hadn't been updated in years and no longer reflected entire projects still in progress (and not), much less individual issues. "I'm gonna clean this up," I thought to myself. And I did. I spent three days burning through coffee and re-familiarizing myself with Jira itself, this company's workflow itself, and updating, closing, archiving, creating issues, etc. I even created a new element of the workflow! Because of course I did! I finally finished and everything was clean and up to date. It felt good. I got a little hit of that dopamine rush from a job well done. That's when it hit me: I just spent three days doing ... nothing. I was hired to do devops and SRE, and I instead spent this time getting our PM tool up to date with a "reality" that was gonna change as soon as I close the tab. We have Actual Problems as far as the eye can see. "What am I doing with my life??"

<center><img src="/images/whatdoyoudo.gif" alt="what do you do here" /></center>

The (Worst Case) Result
-----------------------

You find yourself with one (or more) Project Manager who is enthusiastic about Jira and loves updating it.

You are harangued regularly by the PM for not updating your issues.

You feel guilty and stressed about not doing it.

The PM feels annoyed and resentful because you aren't using the tool and the awesome workflow.

You start attending regular meetings with the entire team to review and update Jira because despite your best intentions Jira no longer reflects reality.

The PM finds themselves exporting data from Jira into spreadsheets because Management is asking for a coherent/simple progress report and, God help you, you can't really figure out how to actually do that with your super awesome complicated workflow in Jira itself. (True story)

You take a look back at where you're spending your time and realize, with horror, you spend more time in meetings and Jira than doing your actual job.

You find yourself hating your job.

Conclusion
----------

None of these problems are, themselves, unique to Jira, and I realize that. It's possible I'm being unfair. But Jira, in my opinion, uniquely enables and encourages this dysfunction. Goodhart's Law is best summarized as "When a measure becomes a target, it ceases to be a good measure." Jira, by way of its infinite customization and complexity enables measurement as the target instead of what it should be: getting the damn job done and shipping.

So what better options are there? It's a hard problem. KISS (Keep It Simple Stupid) is a good guiding rule for many things, including this. The best PM workflow I ever had at any company was as simple as Trello with some webhooks to cross-post updates in/out of slack. Simple, efficient, legible. Github Issues is similarly simple (so far) and has the benefit of tight integration with pull requests and the codebase itself. This is good.

If an organization finds itself with one FTE whose entire job can fairly be summarized as "working in Jira", you're in bad shape. The cancer has taken hold and will start metastasizing. Cut the tumor out before it's too late!
