Controlling Zigbee devices with MQTT
====================================
:date: 2019-01-06 10:00:00 
:tags: mqtt, iot, zigbee

This is a short tutorial on connecting a zigbee device (an Aqara cube) to an MQTT server, so you can control your zigbee devices from the network.

If you're anything like me, you're probably a sucker for IoT devices.
For a long time, I've been using WiFi-enabled lights, and Amazon dash buttons to control them.
To keep these (cheap Chinese) internet enabled devices away from your network and their respective cloud services, you'll probably want to set up a dedicated network in your router (more on this on a future post, maybe).
Another disadvantage of WiFi devices is that they're relatively power hungry.

A popular alternative is using ZigBee for communication.
It is a dedicated protocol similar to bluetooth (BLE), with lower power requirements and bitrate.

Take the (super cute) aqara cube as an example.
It is a small cube that detects rotation on all of its axes, and tapping events.
Here's a video:

.. youtube::  5YtqG1wEnng


To connect to zigbee devices you will need a zigbee enabled gateway (a.k.a. hub), which connects to your WiFi network and your zigbee devices.
Once again, this means adding an internet-enabled device to your home, and probably a couple of cloud services.

As an alternative, you can set up your own zigbee gateway, and control it to your home automation platform of choice (e.g. home assistant).
We will cover how to set up a zigbee2mqtt gateway that is also connected to an MQTT server, so you can use MQTT to control your devices and get notifications.

What you need:

- `Aqara cube <https://www.aliexpress.com/item/Original-Xiaomi-Mi-Aqara-Cube-Smart-Home-Controller-6-Action-Operation-Fr-Home-Device-Zigbee-Version/32892947622.html?spm=a2g0s.9042311.0.0.3da24c4dXV8sBI>`__.
- `CC2531 zigbee sniffer <https://www.aliexpress.com/item/Wireless-Zigbee-CC2531-CC2540-Zigbee-Sniffer-Bluetooth-BLE-4-0-Dongle-Capture-Module-USB-Programmer-Downloader/32907587711.html?spm=a2g0s.9042311.0.0.3da24c4dXV8sBI>`__.
- `CC-debugger <https://www.aliexpress.com/item/CFSUNBIRD-CC-DEBUGGER-Debugger-and-Programmer-for-RF-System-on-Chips-TI-ORIGINAL-Fast-hipping/32813122315.html?spm=a2g0s.9042311.0.0.3da24c4dXV8sBI>`__.


You will need to flash your sniffer.
For that, you only need to follow the instructions from the `zigbee2mqtt documentation <https://koenkk.github.io/zigbee2mqtt/>`_.

Once you're done flashing, you're ready to set up the zigbee2mqtt server.
For convenience, I wrote a simple docker-compose to deploy a zigbee2mqtt server and a test mosquitto server:


.. code-block:: docker-compose
      
      version: '2.1'
      services:
	zigbee2mqtt:
	  image: koenkk/zigbee2mqtt
	  container_name: zigbee2mqtt 
	  restart: always
	  volumes:
	    - ./z2m-data/:/app/data/
	  devices:
	    - "/dev/ttyACM0"
	  networks:
	      - hass
	mqtt:
	  image: eclipse-mosquitto
	  ports:
	     - 1883:1883
	     - 9001:9001 
	  networks:
	      - hass
	  volumes:
	    - ./mosquitto.conf:/mosquitto/config/mosquitto.conf
	hass:
	  image: homeassistant/home-assistant   
	  ports:
	    - "8123:8123"
	  networks:
	    - hass
	  volumes:
	    - ./hass-config:/config
	    - "/etc/localtime:/etc/localtime:ro"
      networks:
	hass:
	  driver: overlay
        

You can test your installation with:


.. code-block:: shell
   
    ❯ mosquitto_sub -h localhost -p 1883 -t 'zigbee2mqtt/#'
   online
   {"battery":17,"voltage":2925,"linkquality":149,"action":"rotate_right","angle":12.8}
   {"battery":17,"voltage":2925,"linkquality":141,"action":"slide","side":2}
   {"battery":17,"voltage":2925,"linkquality":120}
   {"battery":17,"voltage":2925,"linkquality":141,"action":"wakeu

zigbee2mqtt supports the following events for the aqara cube: shake, wakeup, fall, tap, slide, flip180, flip90, rotate_left and rotate_right.
Every event has additional information, such as the sides involved, or the degrees turned.

Now you are ready to set up home assistant support in zigbee2mqtt following `this guide <https://koenkk.github.io/zigbee2mqtt/integration/home_assistant.html>`_.
