---
post_id: 205
title: security, part III
author: cwage
layout: post
guid: http://wordpress.quietlife.net/?p=205
permalink: /2003/10/23/security-part-iii/
dsq_thread_id:
  - 236777334
categories:
  - geek
tags:
  - geek
---
In the [last installment][1], I discussed ways to make ssh keys as convenient as possible without sacrificing the security of a passphrase. But, unfortunately, there are some situations that require automation during which the entry of a passphrase is not feasible.

Sometimes, you need to accomplish something -- running a command, transferring a file, etc. -- in a scriptable manner. Traditionally, there are two methods used to solve this problem:

<!--more-->

  * Use a passphrase-less SSH key.
  * Run ssh-agent system-wide (perhaps using something like [keychain][2])

First, let me say that it's my opinion that running ssh-agent system-wide is woefully misguided. You might as well use passphraseless keys. Things like [keychain][2] make this insecure solution even worse.

So, we're left with passphrase-less SSH keys. I have already talked about the [obvious downsides][1] to using passphrase-less keys, but sometimes you have no choice. But, there is a compromise. Everyone that uses SSH keypairs is no doubt familiar with the ~/.ssh/authorized_keys file. What not everyone seems to be aware of, though, is that this file gives you more than a place to dump keys -- it lets you specify who this key gives access to, and what they can do with it. I myself wasn't aware of this for the longest time. Amazing what you can learn when you read the man page!

From the [SSHD(8)][3] manpage:

> **AUTHORIZED_KEYS FILE** FORMAT
> 
> *$HOME/.ssh/authorized_keys* is the default file that lists the public keys that are permitted for RSA authentication in protocol version 1 and for public key authentication (PubkeyAuthentication) in protocol version 2. **AuthorizedKeysFile** may be used to specify an alternative file.
> 
> Each line of the file contains one key (empty lines and lines starting with a \`#' are ignored as comments). Each RSA public key consists of the following fields, separated by spaces: options, bits, exponent, modulus, comment. Each protocol version 2 public key consists of: options, key- type, base64 encoded key, comment. The options field is optional; its presence is determined by whether the line starts with a number or not (the options field never starts with a number). The bits, exponent, mod- ulus and comment fields give the RSA key for protocol version 1; the com- ment field is not used for anything (but may be convenient for the user to identify the key). For protocol version 2 the keytype is \`\`ssh-dss'' or \`\`ssh-rsa''.
> 
> Note that lines in this file are usually several hundred bytes long (be- cause of the size of the public key encoding). You don't want to type them in; instead, copy the *identity.pub*, *id_dsa.pub* or the *id_rsa.pub* file and edit it. 
> 
> **sshd** enforces a minimum RSA key modulus size for protocol 1 and protocol 2 keys of 768 bits.
> 
> The options (if present) consist of comma-separated option specifica- tions. No spaces are permitted, except within double quotes. The following option specifications are supported (note that option keywords are case-insensitive): 
> 
> **from="pattern-list"**
> :   Specifies that in addition to public key authentication, the canonical name of the remote host must be present in the comma- separated list of patterns (\`*' and \`?' serve as wildcards). The list may also contain patterns negated by prefixing them with \`!'; if the canonical host name matches a negated pattern, the key is not accepted. The purpose of this option is to optionally increase security: public key authentication by itself does not trust the network or name servers or anything (but the key); how- ever, if somebody somehow steals the key, the key permits an in- truder to log in from anywhere in the world. This additional op- tion makes using a stolen key more difficult (name servers and/or routers would have to be compromised in addition to just the key).
> 
> **command="command"**
> :   Specifies that the command is executed whenever this key is used for authentication. The command supplied by the user (if any) is ignored. The command is run on a pty if the client requests a pty; otherwise it is run without a tty. If an 8-bit clean chan- nel is required, one must not request a pty or should specify **no-** **pty**. A quote may be included in the command by quoting it with a backslash. This option might be useful to restrict certain pub- lic keys to perform just a specific operation. An example might be a key that permits remote backups but nothing else. Note that the client may specify TCP/IP and/or X11 forwarding unless they are explicitly prohibited. Note that this option applies to shell, command or subsystem execution.
> 
> **environment="NAME=value"**
> :   Specifies that the string is to be added to the environment when logging in using this key. Environment variables set this way override other default environment values. Multiple options of this type are permitted. Environment processing is disabled by default and is controlled via the **PermitUserEnvironment** option. This option is automatically disabled if **UseLogin** is enabled.
> 
> **no-port-forwarding**
> :   Forbids TCP/IP forwarding when this key is used for authentica- tion. Any port forward requests by the client will return an er- ror. This might be used, e.g., in connection with the **command** option.
> 
> **no-X11-forwarding**
> :   Forbids X11 forwarding when this key is used for authentication. Any X11 forward requests by the client will return an error.
> 
> **no-agent-forwarding**
> :   Forbids authentication agent forwarding when this key is used for authentication.
> 
> **no-pty**
> :   Prevents tty allocation (a request to allocate a pty will fail).  
>     **permitopen="host:port"** Limit local \`\`ssh -L'' port forwarding such that it may only con- nect to the specified host and port. IPv6 addresses can be spec- ified with an alternative syntax: *host*/*port*. Multiple **permitopen** options may be applied separated by commas. No pattern matching is performed on the specified hostnames, they must be literal do- mains or addresses. 
> 
> **Examples**
> :   1024 33 12121...312314325 ylo@foo.bar  
>     from="*.niksula.hut.fi,!pc.niksula.hut.fi" 1024 35 23...2334 ylo@niksula  
>     command="dump /home",no-pty,no-port-forwarding 1024 33 23...2323 back-up.hut.fi  
>     permitopen="10.2.1.55:80",permitopen="10.2.1.56:25" 1024 33 23...2323 

You can imagine how this can be incredibly useful. For example, I use CVS to control all of the zone files and configurations for my nameservers. To accomplish this, I needed to have the nameservers be able to pull down their configs from another server via CVS (using SSH) in an automated fashion. So, in the ~/.ssh/authorized_keys file on the CVS server's host, I have:

*command="cvs server",no-port-forwarding,no-pty ssh-dss AAAAB3NzaC1kc3MAAA ...*

This restricts the access to the command "cvs server", and disallows port forwarding or PTY allocation. This pretty well limits this particular key to doing nothing but CVS updates.

Sometimes using passphraseless SSH keys is your only choice -- but taking these small extra steps can **greatly** reduce the potential for security problems.

 [1]: http://chris.quietlife.net/archives/000315.html
 [2]: http://www.gentoo.org/proj/en/keychain.xml
 [3]: http://www.openbsd.org/cgi-bin/man.cgi?query=sshd