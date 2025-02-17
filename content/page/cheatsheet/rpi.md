---
title: Raspberry Pi
description: Tools, links and configuration for your Raspberry Pi
image: img/rpi.png
tags:
  - rpi
---

## HDMI flickering

Avoid HDMI flickering/intermittent blanking on RPI with a 1400x1050 VGA monitor.

```python

   hdmi_drive=2
   hdmi_group=2
   hdmi_mode=42
   disable_overscan=1
   config_hdmi_boost=7
```
