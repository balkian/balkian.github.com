HDMI-VGA adapter issues with Raspberry Pi
=========================================
:date: 2017-01-07 18:00:00 
:tags: rpi

Avoid HDMI flickering/intermittent blanking on RPI with a 1400x1050 VGA monitor.

.. code-block:: python

   hdmi_drive=2
   hdmi_group=2
   hdmi_mode=42
   disable_overscan=1
   config_hdmi_boost=7
