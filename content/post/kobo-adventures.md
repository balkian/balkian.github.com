---
title: "Kobo Adventures"
description: How to get root access on a Kobo without USB
date: 2026-02-10T22:52:20+01:00
image: 
math: 
license: 
hidden: false
comments: true
draft: true
---

TL;DR You can use the UART to access uboot, change the boot args, boot and change the password so you can log in and enable ssh/remote access.

I like technology almost as much as I like a bargain.
For a while now I've been buying used kobos for friends and for personal projects.
Kobos are very friendly for tinkerers: a side-loading mode (no cloud), a simple mechanism to install apps and customize the system and a vibrant community.
This means you can easily install Koreader on it.
After using it on my kindle for years, I just can't use the stock reader. Ok, it's not such a big deal, but I really like the configurability and the extra niceties.

Older kobos are even better, because most of them have an internal SD card instead of an eMMC, so you can easily recover if you mess up the system.
Sadly, newer devices (and h2o models) no longer have an SD card.
Supposedly, for waterproofing
Another recent change is that newer firmwares stopped allowing telnet and ssh access to the device by default.

This post tells the story of how I managed to get remote access and install custom applications on a newer device with a missing USB port.

## What I got

I bought a used Kobo Libra H2O.
The listing said the battery would not charge well or at all after getting it replaced by an unofficial technician.
I risked it, hoping it would be a relatively easy port issue, and I would be able to get around it, even if I needed some ugly hack.

My plan was to fix the port, or at least try, and get it to charge some way.

* Fix the port
* Install Kobo

## Fixing the port

I will skip this section for now.

Long story short: the connector that connects the motherboard to the USB daughterboard was broken.

## Failed attempts

* Hand-wiring a USB connector to contact points in the daughterboard. Either something else was broken or I was missing resistors/components.
* Downloading files from the browser
* Logging using UART

What I didn't try: buying and soldering a new connector.
To be honest, I am not sure I would be able to properly solder it without melting the plastic parts.
Even then, I wasn't sure the rest of the board was functional, because my attempts to manually wire it had failed.

## U-boot

Connect the UART, reboot the reader and press a key while it boots.
You will be greeted by u-boot.

U-boot can actually list your mmc contents, you can load files to memory and write them to specific locations.
If you know how to use that, great, just remove `.kobo/ssh-disabled` from the user partition and create a file named `.kobo/ssh-enabled`.
I personally don't feel too comfortable raw editing the contents of the file system, and I was afraid of breaking something.
Luckily, there is an easier way.


If you take a look at the environment, you will recognize some of the variables that are used for booting.
In particular, one of them has the linux boot parameters.
Use `setenv` to modify it to add this at the end:

```
single init=/bin/sh
```
Now, boot from mmc.

## Changing the root password

Once booted, it is just a matter of changing the password:

```
passwd root
```
There might be some warnings about weak passwords, but it will let you set it anyway.
The user partition is not mounted, and I got errors while trying to do it manually, so just `reboot`.


## Enabling remote access

use `root` and the password you just set to log in the normal system.

```
# I believe these are the correct paths, but check before running the command
cd /mnt/onboard/
rm .kobo/ssh-disabled
touch .kobo/ssh-enabled
reboot
```

## SSH

Connect your Kobo to your wifi, and ssh to it.
You will be asked to change the password on your first login.
