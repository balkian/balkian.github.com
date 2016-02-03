Arch Linux Fixes
################
:date: 2016-02-03 Wed 20:00
:tags: arch, linux


Black screen and LightDM doesn't unlock
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Add this to your `/etc/lightdm/lightdm.conf` file:

.. code-block:: cfg

                [LightDM]
                logind-check-graphical=true

                
