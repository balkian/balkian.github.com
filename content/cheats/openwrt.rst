PPTP connections
#################
:date: 2017-01-01
:tags: openwrt, linux, router

PPTP VPN connections will fail on a vanilla openwrt installation.
You need to install this module:

.. code-block:: shell
   
   opkg install kmod-nf-nathelper-extra
