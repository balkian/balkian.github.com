---
title: Logitech MX Keys for Mac on Linux
date: 2021-10-29 00:00:01
tags:
  - linux
  - logitech
  - keyboard
---

I recently got Logitech MX Keys for Mac keyboard at work.
The German version, to be more precise.
This version was three times cheaper than the Windows equivalent with either US or ES layout.
Since I touch type anyway, I thought it was a bargain.

As soon as I plugged it in, I realized there were some glaring issues with the keyboard.
First of all, the Meta/Super and Alt keys are reversed in this keyboard.
In the normal/full version of this keyboard, Logitech gives an option to choose between Mac, Windows and iOS host, and that changes the behavior of the keys.
In this version, tho, only iOS and Mac are available.

Besides that, there's the issue of the grave (tilde) and angle keys switched as well.

Switching these keys around would be very easy with Xorg, but Wayland once again complicates things...

These issues almost made me return the keyboard.
Luckily, tho, there is another option: configuring the keys one level lower than wayland (and X11), through hwdb.

Long story short, this will configure any Logitech keyboard with the same product id (0x4092) to use a saner configuration:


```cfg
#File: /etc/udev/hwdb.d/90-logitech-keyboard.hwdb

evdev:input:b0003v046Dp4092*
 KEYBOARD_KEY_700e2=leftmeta
 KEYBOARD_KEY_700e3=leftalt
 KEYBOARD_KEY_70039=leftctrl
 KEYBOARD_KEY_70064=102nd
 KEYBOARD_KEY_70035=grave
 KEYBOARD_KEY_700e7=rightalt
 KEYBOARD_KEY_700e6=rightmeta
 KEYBOARD_KEY_7006d=compose

```

After that, simply run:

```
 sudo udevadm hwdb --update && sudo udevadm trigger
```
