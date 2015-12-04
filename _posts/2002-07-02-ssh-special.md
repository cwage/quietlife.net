---
post_id: 129
title: ssh special
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=129
permalink: /2002/07/02/ssh-special/
dsq_thread_id:
  - 236773837
categories:
  - geek
tags:
  - geek
---
Any good network administrator uses [<acronym title="Secure SHell">SSH</acronym>][1] extensively.

Of course, any network administrator also interested in security uses public/private key authentication as opposed to password authentication. ssh-agent adds a wonderful convenience to this system, eliminating the need to enter your password for every host you SSH to. Combined with ssh-agent forwarding (-A or ForwardAgent in ssh_config), you would only have to enter your password once when starting ssh-agent the very first time. See [this article][2] for a good lesson in how this works.

In addition, any good sysadmin probably uses [screen][3] in some pretty sick and twisted ways.

The problem is: screen and ssh-agent don't really quite get along. This is because ssh-agent uses an environment variable to point at a socket that ssh uses to pass authentication requests to. If you're re-attaching to a screen session, however, this environment variable will no doubt be out of date.  
<!--more-->

  
Following some advice that I got on the [GNU Screen mailing list][4], I made a few changes that have saved me a lot of headaches.

Basically, I just made my .profile update a symlink to the ssh-agent socket created in /tmp. I then modified my .screenrc to set SSH\_AUTH\_SOCK to point at THIS file rather than the actual socket. This way it never gets out of date.

.profile:

if [ "x$SHLVL" = "x1" ]; then # we are a login shell  
rm -rf /tmp/ssh-agent-sock-screen  
ln -s $SSH\_AUTH\_SOCK /tmp/ssh-agent-sock-screen  
fi

.screenrc:

unsetenv SSH\_AUTH\_SOCK  
setenv SSH\_AUTH\_SOCK /tmp/ssh-agent-sock-screen

Now, when I log into X on my laptop, ssh-agent runs automatically, I add my keys, enter the passwords, and off I go -- I never enter another password again!

 [1]: http://www.openssh.org/
 [2]: http://www-106.ibm.com/developerworks/linux/library/l-keyc3/
 [3]: http://www.gnu.org/software/screen/
 [4]: http://groups.yahoo.com/group/gnu-screen/