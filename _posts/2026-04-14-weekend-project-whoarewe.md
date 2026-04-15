---
title: "Weekend project: whoarewe"
author: cwage
layout: post
permalink: /2026/04/14/weekend-project-whoarewe/
categories:
  - tech
---

## tl;dr

- I used claude code to build an android app that lets two people prove they're talking to each other using shared, rotating codes that only their devices can generate for identity confirmation
- repo: https://github.com/cwage/whoarewe
- OSS: MIT license
- It's not on the play store, and probably never will be, unless I can convince a handful of friends and family to at least try it, much less use it.
- To try it: download the [signed APK from the releases](https://github.com/cwage/whoarewe/releases) on the above github repo and either enable "Install unknown apps" in your Android settings and open it, or sideload it with adb install. If you don't trust this (as you shouldn't), but maybe kind trust me, you can clone the repo, inspect the code and build it yourself. Have clippy review it!

## The problem

Say that you get a phone call from a loved one. They're panicked, crying, says they've been in a car accident. They're freakin out, you're freakin out. They need money, now. It sounds *exactly* like them. What do you do? In a high pressure situation, there's often not time (real or perceived) to establish verifiable identity confirmation. ("Tell me something only you'd know!"). People are often at their least rational or defensive in situations like this, and scammers are increasingly good at engineering precisely these situations to get your guard down. Stuff like this is [starting to happen, with success](https://www.americanbar.org/groups/senior_lawyers/resources/voice-of-experience/2025-september/ai-cloned-voice-scam/).

I'm a pretty skeptical guy, and a year ago, I'd have rolled my eyes at this. Surely you can tell a fake voice from a real one, right? Turns out: not so much. [Some studies](https://arxiv.org/html/2503.02857v2) put human detection of deepfake audio at roughly 48% accuracy (I can't vouch for the methods and scientific rigor here, but seems plausible). Modern voice cloning tools need [as little as a few seconds of sample audio](https://theconversation.com/deepfakes-leveled-up-in-2025-heres-whats-coming-next-271391), cost a pittance, and the source material is stuff that's already out there for anyone with a modest public presence: earnings calls, conference talks, social media clips. Some examples:

- [AI-generated Biden robocall](https://www.npr.org/2024/05/23/nx-s1-4977582/fcc-ai-deepfake-robocall-biden-new-hampshire-political-operative) hit NH primary voters in 2024. Cost about a dollar to produce, took under 20 minutes.
- [Arup, $25.6M stolen](https://www.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk) -- finance employee joined a video call where the CFO and several colleagues were all deepfakes. 15 wire transfers before anyone noticed.
- [Ferrari exec targeted](https://www.thedrive.com/news/ferrari-thwarted-an-ai-deepfake-scammer-posing-as-its-ceo-with-an-age-old-trick) by a deepfake of CEO Benedetto Vigna's voice -- accent and all. Got suspicious, asked a personal question the caller couldn't answer. He was lucky.

Even before the advent of AI-supercharged techniques, social engineering scams were already bilking people out of their life savings regularly. The models are getting better and the detection tools (especially outside a lab) are getting worse.

The uncomfortable truth is that voice and video are no longer reliable signals of identity. They used to be (to an extent), not because they were cryptographically secure, but because faking them was hard. That's no longer the case, so what do we do?

<!--more-->

## The "just slather more AI on it" solution

The lesson here (in this and every other industry) is that these AI/machine learning tools are getting more and more powerful, so an understandable reaction is to employ the same tools in defense, detection and prevention of such things. Many companies are doing that: offering tools to analyze/detect deepfakes. (Hilariously, one such company both sells the deepfake tools and also detection/defensive tools -- like askin your drug dealer advice on kicking your heroin habit.) There are a lot of fundamental problems I see with this approach. There are countless channels of communication, for one: email, SMS, facebook, craigslist, reddit DMs. I wonder how they propose to control/monitor all these channels? I wish them well, but it's gonna be an endless arms race.

It may be a nonstarter in reality, but the technology to rigorously defend against this stuff (by confirming trusted identities) was invented decades ago:

## We sort of solved this problem already

These days, robust encryption and authentication is something we kinda take for granted (to the degree anyone knows it exists at all, but that's another story). It wasn't always that way, of course. Various forms of digital symmetric key encryption were around dating to the 50s, but it was computationally expensive, and the keys still had to be transported cloak-and-dagger style in person. In the late 70s, public key cryptography (PKC) emerged (RSA and Diffie-Hellman key exchange in particular), which obviated key transport as a physical or digital concern. But it was still too computationally expensive to be of much use beyond niche situations. In the early 90s, the advances in computing power and the advent of the internet made for a perfect confluence that got people asking: "Maybe we shouldn't be sending everything across the internet in plaintext."

The emergent result of PKC and modern PKI (infrastructure) exploded and now drives the security of most of the internet in various ways: HTTPS for secure web transport, mobile app stores (all apps are signed using PKI), ssh, even most bank cards these days use PKI. The list goes on. GnuPG is still used to a large degree for software signing/trust in various ways as well, which makes for a good segue. GnuPG itself is a modern OSS implementation of the OpenPGP standard, which originated with PGP in the early 90s. PGP was one of the earliest forms of consumer-available PKC tools. It was designed with e-mail in mind at the time: You could sign messages cryptographically to prove it came from you, and/or encrypt it for a recipient if you wanted.

One of the less-remembered aspiration goals of this was the emergence of a "web of trust". If I can cryptographically attest that I am who I say I am, and my friend can do the same, we can establish digital trust that could extend to a "web" of people doing the same. People would literally (nerd alert!) get together for "key signing parties" in person to do this with PGP at the time. It never took off, unfortunately, but it wasn't really a failure of technology. It was a UX problem. You had to be a pretty big nerd at the time to understand what PGP was at all, much less manage a keyring and be motivated enough to show up in person for a keysigning party. Ain't nobody got time for that.

But the technology still exists, and while the "web of trust" idea might inherently involve too much friction to ever take off, digital identity is still a pretty easy thing to implement and verify using cryptography. AI machine learning tools can hallucinate and lie, but math doesn't.

(For a more in-depth deepdive on PKI in general, RSA and more recently elliptic curve crypto (which this project uses), see [Cloudflare's excellent explainer here](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/))

## "Get to the point already"

This weekend I worked with claude code (gasp, more on that later) to build an android app. It's a basic proof of concept that:

- prompts you to create an "identity" (an Ed25519 keypair) and give it a name (probably yours, but anything really)
- lets you present a QR code containing your public key for others to scan (or send them a screencap)
- lets you scan or import someone else's QR code

You exchange QR codes over any *trusted* (this is the important part) channel: in person, a Signal chat, a secure groupchat where everyone is trusted. The QR code itself is just your public key, so it's not a secret. What matters is that the person on the other end trusts it came from you. I intentionally left it at the users' discretion to decide how much they trust any particular channel of communication to be with someone that is who they say they are.

From then on, both phones show the same rotating (5 min) 6-digit code for each other: much like -- well, exactly like a two-factor auth code, but shared between two people instead of between a person and a service. Someone calls claiming to be your friend? Ask them to read their code. If it matches, they have the device you paired with. If not, hang up.

There are no servers, cloud services or even any internet/data connection required.

### Under the hood

- **Identity**: Ed25519 keypair. The private key never leaves the device (encrypted at rest via Android Keystore-backed keys, biometric/PIN unlock). Public key is what's in the QR code.
- **Pairing**: Two people scan each other's QR codes. Each phone independently derives a shared secret via ECDH (X25519) — deterministic, no negotiation, no server, no network. Alice scans Monday, Bob scans Thursday, same result.
- **Per-contact isolation**: Each pairing produces its own shared secret, stored encrypted on-device. Compromising one doesn't affect the others.
- **Verification**: Shared secret feeds standard TOTP (same algo as e.g. Google Authenticator, 5-minute rotation). Both phones compute the same code at the same time. It matches or it doesn't. The 5-min rotation is notably much longer than most 2FA apps, owing to the reality that communicating such a code in real life might not be as rapid.
- **No recovery**: Lose the device, lose the keys, lose the pairings. This isn't a missing feature. There's no infrastructure to build a backdoor in. The fallback is nothing, which is what most people are working with now.

## "I'm sorry, did you just say you used AI to yolo a crypto app?"

Sorta yes. But, a) I do what I want, and b) not really.

The canonical advice every coder and security professional lives and dies by is: never roll your own crypto. And I didn't, really. Yes, it's an app that uses crypto, via the normal hardened libraries:

- Key generation & ECDH: BouncyCastle (Ed25519, X25519)
- TOTP: javax.crypto.Mac with HmacSHA1 (same algo as Google Authenticator)
- Encryption at rest: AES-256-GCM via javax.crypto.Cipher + Android Keystore
- Entropy: java.security.SecureRandom
- Biometric unlock: AndroidX Biometric

It's not that different than writing my own SSH client or something. I didn't write the crypto, I just know how it works, and I knew how to tell clippy to make it happen.

If you still think it's funny? I agree. But it's OSS (for multiple reasons): clone it and inspect it if you suspect it's a dumpster fire. It works!

## What it's not

- not a comms/messaging app. Single-purpose verification tool that works alongside whatever channel you're already using.
- not recoverable. Lose your phone, lose your pairings. Recovery story is "pair again." This is a feature (no server to breach, no backup to intercept) but it's a real trade-off.

Frankly: It's also not something most anyone will ever use. Most people don't understand security at all much less cryptography. Most people gladly outsource it (whether they know it or not) to trusted 3rd parties and brand names, for better or worse. I could and would gladly be wrong about this -- 30 years ago if you had told me something like Signal would be out there offering genuine end to end encrypted messaging with keys owned by the individuals, I'd call you crazy. Maybe there's hope!
