---
title: Linux on the Microsoft Surface Go
date: 2019-06-01 00:00:01
tags:
  - linux
  - surface go
  - config
---

Believe it or not, Surface tablets have pretty good linux support, except for the webcams in newer models.
These are some useful notes to get Ubuntu installed in your surface go, as of Summer 2019.


<!--more-->

## Installing the kernel


```shell
git clone --depth 1 https://github.com/jakeday/linux-surface.git ~/linux-surface
cp -a ~/linux-surface /media/<your usb>
```

```shell
cp -a /media/<your usb>/linux-surface ~/
cd ~/linux-surface/
sudo sh setup.sh
```


## Booting ubuntu first

Switch out of Windows S mode.


Boot into the "Command Prompt".

From Windows go to "change advanced startup options" and select "restart now".

When it reboots, choose the "Troubleshoot" option, then choose the "Advanced options" option, and finally choose the "Command Prompt" option.

After the device reboots, login to the command prompt and then you should see a terminal with X:\windows\system32>

At the prompt, check your UEFI entries:

```shell
bcdedit /enum firmware
```

Copy UEFI entry of "Windows Boot Manager" to create a new entry for Ubuntu: bcdedit /copy {bootmgr} /d "Ubuntu"

Copy the printed GUID number including the braces {} using Ctrl+C

Set file path for the new Ubuntu entry. Replace {guid} with the returned GUID of the previous command (Ctrl+V). bcdedit /set {guid} path \EFI\ubuntu\grubx64.efi

Set Ubuntu as the first/ entry in the boot sequence. Again replace {guid} with the returned GUID of the copy command.

```shell
bcdedit /set {fwbootmgr} displayorder {guid} /addfirst
```

Check your UEFI entries again: bcdedit /enum firmware You should see something like this:


```shell

Firmware Boot Manager
---------------------
identifier              {fwbootmgr}
displayorder            {3510232e-f8eb-e811-95ce-9ecab3f9d1c4}
                        {bootmgr}
                        {2148799b-f8eb-e811-95ce-9ecab3f9d1c4}
                        {312e8a67-c2f6-e811-95ce-3c1ab3f9d1de}
                        {312e8a68-c2f6-e811-95ce-3c1ab3f9d1de}
timeout                 0
```

Make sure the GUID you copied is the first one listed in displayorder. Then type exit, turn off the PC and turn it back on. After this my surface go is automatically booting to the grub bootloader which lets me choose between Windows and Ubuntu but defaults to Ubuntu after ten seconds.

