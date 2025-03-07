---
title: Linux Cheatsheet
slug: linux
author: "Fernando Sánchez"
description: Tips and tricks for GNU/Linux and Unix
image: "img/linux.png"
categories:
  - linux
tags:
  - linux
  - arch
---

## Black screen and LightDM doesn't unlock

Add this to your /etc/lightdm/lightdm.conf file:

```cfg
[LightDM]
logind-check-graphical=true
```


##Edit previous commands

`fc` is a shell builtin to list and edit previous commands in an editor.
In addition to editing a single line (which you can also do with `C-x C-e`), it also allows you to edit and run several lines at the same time.
You use it like this:

List previous commands

```shell
$ fc -l
10259  nvim deploy.sh
10260* cd ..
10261* nvim content/cheatsheet/linux.md
10262  cd
```

List commands with date (in zsh)

```shell
$ fc -ld
10260* 19:38  cd ..
10261* 19:38  nvim content/cheatsheet/linux.md
10262  19:40  cd
10263  19:40  fc -l
```

You can add the date too:

```shell
$ fc -fld
10262  1/10/2019 19:40  cd
10263  1/10/2019 19:40  fc -l
10264  1/10/2019 19:40  fc -ld
```

You can edit a range of commands

```shell
$ fc 10262 10264
```


The range can be relative to the current position, so the previous command is equivalent to:

```shell
$ fc -3 -1
```

If you save and exit, all commands are executed as a script, and it will be added to your history.

Source: https://shapeshed.com/unix-fc/

## Prevent logoff from killing tmux sessions

Lately I've noticed that logging out of i3, intentionally or when i3 fails, would also kill any tmux or emacs sessions.
This is extremely annoying.

This is caused by a new default in logind (systemd's login) to kill user process on logoff.
You can revert this setting in your logind.conf (`/etc/systemd/logind.conf`):

```cfg
KillUserProcesses=no
```

Or only for a specific process (e.g., tmux):

```shell
systemd-run --scope --user tmux
```

Source: https://unix.stackexchange.com/questions/490267/prevent-logoff-from-killing-tmux-session


## Upload a temporary file 

Sometimes you just need to copy/paste a file from a server, and copying from the terminal can be a hassle.
These two services are command-line "pastebins" just one curl away:

```shell
<command> | curl -F 'sprunge=<-' http://sprunge.us
# OR

<command> 2>&1 | curl -F 'f:1=<-' ix.io

# OR

<command> | curl -F"file=@-" https://ttm.sh
```


# Install Fortinet SSLVPN support for NetworkManager

UPM (Universidad Politécnica de Madrid) uses a propriatary VPN solution.
The instructions for GNU/Linux on their website involve downloading a specific client (`.tar.gz`) and manually running it.
That works, but it is kind of a hassle.
A much more convenient alternative is installing this NetworkManager plugin:

```shell
pacman -Sy networkmanager-fortisslvpn 
# Or apt get install networkmanager-fortisslvpn 
```

Now you can simply add a new VPN connection in NetworkManager and manage it as you would any other connection.
