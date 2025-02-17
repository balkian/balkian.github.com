#/bin/bash
USER=j
IFNAME=enp62s0u1u3
BINARY=test-tftp.bin
ip address flush dev $IFNAME
ip address add 10.1.1.10/24 dev $IFNAME
dnsmasq -i $IFNAME --dhcp-range=10.1.1.50,10.1.1.100 \
        --dhcp-boot=$BINARY \
        --enable-tftp --tftp-root=/home/$USER/Downloads/pxe -d -u $USER -p0 -K --log-dhcp --bootp-dynamic
