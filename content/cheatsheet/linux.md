---
title: Linux
author: "Unknown Author"
description: Tips and tricks for GNU/Linux and Unix
tags:
  - linux
  - arch

---

# Black screen and LightDM doesn't unlock

Add this to your /etc/lightdm/lightdm.conf file:

```
[LightDM]
logind-check-graphical=true
```


# Edit previous commands

`fc` is a shell builtin to list and edit previous commands in an editor.
In addition to editing a single line (which you can also do with `C-x C-e`), it also allows you to edit and run several lines at the same time.
You use it like this:

List previous commands
```
$ fc -l
10259  nvim deploy.sh
10260* cd ..
10261* nvim content/cheatsheet/linux.md
10262  cd
```

List commands with date (in zsh)

```
$ fc -ld
10260* 19:38  cd ..
10261* 19:38  nvim content/cheatsheet/linux.md
10262  19:40  cd
10263  19:40  fc -l
```

You can add the date too:

```
$ fc -fld
10262  1/10/2019 19:40  cd
10263  1/10/2019 19:40  fc -l
10264  1/10/2019 19:40  fc -ld
```

You can edit a range of commands

```
$ fc 10262 10264
```


The range can be relative to the current position, so the previous command is equivalent to:

```
$ fc -3 -1
```

If you save and exit, all commands are executed as a script, and it will be added to your history.

Source: https://shapeshed.com/unix-fc/
