---
title: "Scrcpy"
description: 
date: 2026-03-05T20:53:35+01:00
image: 
math: 
license: 
hidden: false
comments: true
draft: true
---

There are multiple options to use your phone as a webcam in linux.
In the past I've used DroidCam.
It works relatively well, both with USB and over WiFi.
However, when I last tried it, circa 2020, the experience wasn't great.
First, latency was more than noticeable.
Then, resolution is limited unless you pay for the app (fair).
Lastly, the setup itself was a bit finicky and it didn't always work for me.


This time I went with [scrcpy](https://github.com/Genymobile/scrcpy), which in addition to replacing DroidCam, it can be used to view, control and record your phone's screen.
It can even create a virtual screen which won't show in your device but that will let you control it remotely.
Neat, huh?

As a bonus, you don't even need to install any apps: you only need to have adb enabled in the developer options (which I always do anyways).

Requisites:
- Enable adb debugging. It should also work with wireless debugging, but I've read complains about latency.
- Install scrcpy and adb in your PC. With nix you can run a shell with all the tools with: `nix-shell -p android-tools -p scrcpy`

Create a loopback device for scrcpy:

```
# This creates /dev/video9
sudo modprobe v4l2loopback video_nr=9 card_label="scrcpy" exclusive_caps=1
```

In my case, I got exceptions unless I manually set the size (e.g., `-m1024`) or the camera size.
Some sizes will also lead to invalid video and other problems, so better find a valid camera size for your phone:

```
# Get a list of camera sizes
scrcpy --list-camera-sizes 
```

In my case, I went with 1920x1440.
Then, you only need:

```
scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=back --v4l2-sink=/dev/video9 --no-playback
```

You can test it out with ffmpeg, vlc or your preferred video player:

```
ffplay -i /dev/video9
```

If that works, you can explore using [autoadb](https://github.com/rom1v/autoadb) to launch scrcpy automatically when you connect your phone to your PC.
