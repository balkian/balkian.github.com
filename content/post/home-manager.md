---
title: "NixOS and Home Manager"
description: 
date: 2025-08-31T18:53:25+02:00
image: /img/nixos.svg
math: 
license: 
hidden: false
comments: true
draft: false
---

Nix is a declarative package manager (and its main language) that allows for reproducible environments (i.e., files in a folder).

One of the cool things about nix is that you can use it to run a package without installing it permanently in your system.
For instance, I recently needed the `readelf` utility and it wasn't installed in my system, so I ran:

```
nix run 'nixpkgs#toybox' -- readelf -l /home/j/.local/share/uv/python/cpython-3.10.11-linux-x86_64-gnu/bin/python | grep interpreter
```

That's it.
No need to deal with dependencies, incompatibilities, or to uninstall the package once you no longer need it.

NixOS is a Linux Operating system that uses this package manager and system configuration (e.g., users, network interfaces, etc.) defined in the Nix language to create reproducible systems.

Home-manager takes the concepts from NixOS to user-space, allowing you to define your personal environment (i.e., home).
It can be used on any system that supports the Nix package manager (e.g., Linux, Mac and Windows).

There is a lot to like 

## Context

(Last year)[https://github.com/balkian/dotfiles/commit/fa7041ff8bde6c5288ad55db6b0d61ed593bbccc] I started experimenting with nix and home-manager to configure my environments.
The context is that for some years now I've been switching devices quite frequently.
It started when my main laptop died (DELL!!), I started using a desktop for most of my work, but I also needed a laptop to teach.
One thing led to another, and I ended up using vanilla Ubuntu or EndeavourOS installations with Gnome and very minimal customization.
That in itself is not wrong.
The thing is that, before that, I was a [tinkerer with a customized environment](https://github.com/balkian/dotfiles).


1. I was being inefficient (and I felt it)
2. That inefficiency turned some easy things into a chore
3. This made work in general less enjoyable.
3. As a result, I became even less productive

The idea was to get back to a usable terminal and editor setup with minimal


## NixOS

I've only been running NixOS for three days now, but so far I like the experience.
My approach is to keep the system definition as simple as possible, and rely on home-manager to install and configure most of my tools.
The basics would be:

* Network configuration
* System users
* Desktop environment (wayland and multiple DE's)

All that goins into my `/etc/nixos/configuration.nix`, and then I do:

```
sudo nixos-rebuild switch
```

If it fails, nothing is changed in your system.
If it works, most of the changes will have been applied (e.g., new services started, others stopped).
The previous configuration does not disappear: you can roll back to it manually or when booting your system.

## Home-Manager

Here's where most of my configuration lives.
I use `homeConfigurations` to keep more than one configuration in the same repo (e.g., work (`j@lenny`) and personal computers (`j`, on any other system)).

To make it easier to install this configuration

### Running on NixOS

There are two ways to run it: as part of your general configuration (i.e., it will be applied using the same `nixos-rebuild` command) or standalone.
I prefer the latter, because it allows me to tinker with the configuration more easily, and it is no different from applying it on other systems (see below).
After you change your config, simply run:

```
home-manager switch
```

### On other systems

Running nix on other operating systems (e.g., Arch Linux) is similar to a standalone installation on NixOS.
The only difference is that you need to [install nix first](https://nix.dev/install-nix.html) and [configure the appropriate channels](https://nix-community.github.io/home-manager/index.xhtml#sec-install-standalone).


## It's a little flakey

Flakes are an experimental feature of nix that use version control and some special conventions to bring more reproducibility guarantees.
For instance, they make it trivial to install a specific commit version of my home-manager config, which in itself could use program definitions from external git repositories.
Flakes are not the only solution to this problem, and they are a bit controversial among hardcore nix users.
However, the community as a whole seems to have embraced flakes.

I personally chose to set up my config as a flake.
I still have not tried to install it on other systems, so time will tell.
