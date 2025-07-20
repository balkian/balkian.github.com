---
title: "Installing Micropython on the Super Mini ESP32-S3"
description: 
date: 2025-07-20T02:30:43+02:00
image: 
math: 
license: 
hidden: false
comments: true
draft: false
---

## Context

Many years ago I bought a "bargain" bluetooth scale.
I wanted a way to automatically log my weight, and the Xiaomi equivalent was more than twice as expensive at the time.
The problem is that it came with a very basic and somewhat sketchy software that required signing up, and none of the typical apps (openscale, gadgetbridge...) supported it.
I looked at how to reverse engineer it, but I did not have much time back then, and I wrote it off as a "future project".
Luckily, it had a screen, so I've been using it as a regular scale.
I did not even bother to check the body composition metrics, because I got a very depressing reading of 35% body fat.

Flash forward to today, when I decided to finally work on it.
In addition to trying nrfConnect, I installed the app to see the actual values..
It turns out the composition data was completely off!!
When a reading starts, the app needs to tell the scale some basic data about you (age, height, sex).
Unfortunately, there is no way (that I know of) to set a default user, so when the phone is not connected, it goes back to the wildly inaccurate reading.

So, I decided to connect one of my idle ESP32 boards to it, to interface with the scale through bluetooth (sending the right user data) and logging the results somewhere through WiFi.

## The problem

Installing the firmware was not too difficult, after I got the board to properly register.

```
❯ uv tool run esptool.py --port /dev/ttyACM4 erase-flash
...
Chip type:          ESP32-S3 (QFN56) (revision v0.2)
Features:           Wi-Fi, BT 5 (LE), Dual Core + LP Core, 240MHz, Embedded Flash 4MB (XMC), Embedded PSRAM 2MB (AP_3v3)
...
❯ uv tool run esptool.py --port /dev/ttyACM4 --baud 460800 write_flash 0 ESP32_GENERIC_S3-20250415-v1.25.0.bin
```

But then, I kept getting this error on boot: `OSError: (-24579, 'ESP_ERR_FLASH_NOT_INITIALISED')`.
And I could not copy any files or install any packages.

After some research, I narrowed the possibilities to:

* A wrong partition table, most likely due to the fact that my board only has 4MB of flash.
* Using an unsupported type of PSRAM (less likely)

## The solution

At this point, I could either try to compile the firmware with a custom partition (kind of tedious), or I could use the wonderful [mp-image-tool-esp32](https://github.com/glenn20/mp-image-tool-esp32) tool to check existing firmwares and modify partition sizes.

I confirmed my suspicion:

```
❯ uv tool run mp-image-tool-esp32  ~/Downloads/ESP32_GENERIC_S3-20250415-v1.25.0.bin 
Running mp-image-tool-esp32 v0.1.1 (Python 3.12.11).                                                                                                                         
Opening /home/j/Downloads/ESP32_GENERIC_S3-20250415-v1.25.0.bin...                                                                                                
Found esp32s3 firmware file (8MB flash).                                                                                                                                     
                        Partition table (flash size: 8MB):                        
╭──────────┬──────┬─────────┬──────────┬──────────┬──────────┬───────┬───────────╮
│ Name     │ Type │ SubType │   Offset │     Size │      End │ Flags │           │
├──────────┼──────┼─────────┼──────────┼──────────┼──────────┼───────┼───────────┤
│ nvs      │ data │ nvs     │   0x9000 │   0x6000 │   0xf000 │   0x0 │ (24.0 kB) │
│ phy_init │ data │ phy     │   0xf000 │   0x1000 │  0x10000 │   0x0 │  (4.0 kB) │
│ factory  │ app  │ factory │  0x10000 │ 0x1f0000 │ 0x200000 │   0x0 │  (1.9 MB) │
│ vfs      │ data │ fat     │ 0x200000 │ 0x600000 │ 0x800000 │   0x0 │  (6.0 MB) │
╰──────────┴──────┴─────────┴──────────┴──────────┴──────────┴───────┴───────────╯
Micropython app fills 79.3% of factory partition (410 kB free)
```


```
❯ uv tool run mp-image-tool-esp32 -f 4MB --resize vfs=2MB ESP32_GENERIC_S3-20250415-v1.25.0.bin
❯ uv tool run esptool.py --port /dev/ttyACM4 --baud 460800 write_flash 0 ESP32_GENERIC_S3-20250415-v1.25.0-4MB-resize=vfs=2097152.bin
```

After that, I was able to install new packages with `mpremote` and `mip`:

```
uv tool run mpremote mip install aioble
```

We can check that we are fully utilizing the 2MB of PSRAM:

```
❯ uv tool run mpremote exec 'import gc;print(gc.mem_free(), "bytes")'
2061456 bytes
```

If you see much less than that, you are probably using the wrong variant (try `SPIRAM_OCT`).
