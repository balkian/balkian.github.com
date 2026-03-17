---
title: "Getting rid of your ISP's router"
description: 
date: 2026-04-10T15:18:45+02:00
image: 
math: 
license: 
hidden: false
comments: true
draft: false
---

TL;DR (PPPoE retriever is a nice python multiplatform tool to get your PPPoE credentials)[https://guillermodotn.github.io/posts/Retrieve_PPPoE_credentials/#what-do-i-need]

I recently moved to an ISP that provides provides an ONT+Router combo.
The ONT is a small device that connects a fiber cable to an ethernet one.
The router connects to the ONT through an ethernet cable.
The connection between the ISP and your router is established using PPPoE.
As part of the protocol, the router needs to send a username and password that identify you as a customer.


Before this, I had never had a separate ONT, so I had to run the ISP's router as a dumb bridge that forwards all traffic to my own OpenWrt router, which does all the work.
No WiFi, no actual routing.
This feels wasteful and unnecessary.
Besides, it doesn't look great.
So I was excited to get rid of the ISP's router this time.

Apparently, my ISP will happily send you your credentials if you ask nicely.
They're also required by European law to give you access with your own device.
Still, once I knew the credentials are sent in plain text, I felt compelled to get it myself.

The plan is simple:

* Connect to your ISP's router WAN
* Pretend to be your ISP
* Get the credentials

There are multiple posts that point to a python script to automate step 2 and 3.
It believe it does it like this:

* It runs `pppd` to spin up a server in your machine. It needs to pass it a configuration file with the right ethernet device and VLAN.
* It uses tcpdump/similar to sniff the traffic during the exchange

Other tutorials recommended using wireshark and looking for the credentials manually using your phone number or something similar.
Some users complained that the process is error prone, or that they could only get it to work using a Live CD of Kali or Ubuntu.

The whole process seemed unnecessarily complicated.
From looking at PPPoE's protocol diagrams, it doesn't look that complicated.
So I decided to build a very simple PPPoE server that only does the first steps of authentication, and it spits out the credentials used.
When looking for existing implementations in go and python, I discovered something better.


[PPPoE Retriever](https://github.com/guillermodotn/pppoe-retriever) is even simpler than a mock server: it uses scapy to intercept the right packets and send the appropriate responses to the router.
So I ran it, [after sandboxing it using podman](https://github.com/balkian/pppoe-retriever/), and it worked flawlessly.

With the user, password and VLAN at hand, I only had to create the appropriate device in OpenWRT (VLAN 802.1q on the WAN interface) and change my WAN interface to PPPoE over that device, with the appropriate user and password.

This whole thing might seem a bit silly.
After all, I could have just called my ISP and be done with it.
But then I wouldn't have learned a little bit more about how my internet connection works.
I wouldn't have been reminded that less os more, or learned of an approach that could be useful in the future.
Lastly, I wouldn't get the feeling of doing the impossible/forbidden.

Because the truth is I really enjoy hacking stuff.
Even when the hard (and smart) work is done by others.
Even when my only contribution is running a script.
Even when there is little to be gained.

I like understanding how things work, and being able to customize them.
Even when I do not end up customizing or using them after all.
