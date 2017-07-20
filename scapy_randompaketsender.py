#!/usr/bin/python

import string
from random import *
from scapy.all import *

#Settings
Beacon_SSID = 'Fake_Beacon'   		#network name
interface = 'wlan0mon'         		#interface
broadcast = "ff:ff:ff:ff:ff:ff" 	#broadcast
bssid = "aa:aa:aa:aa:aa:aa"		#bssid
source = "111.111.111.111"		#source address
destination = "222.222.222.222"		#destination address

#sent 1.000 pakets
for i in range(0,1000):
	if (random.random() > 0.75): 
		#ARP
		arp = ARP()
		arp.psrc = source
		arp.pdst = destination
		arp.hwsrc = bssid
		send(arp, iface = interface)
		print "sent ARP"		

	elif (random.random() > 0.5):	
		#TCP (payload size: 1500 bytes MTU - 20 bytes IP header - 20 bytes TCP header = 1460 bytes)
		#https://stackoverflow.com/a/2257449/8334101
		def random_data(size=randint(1, 1460), chars=string.ascii_uppercase + string.digits):
			return ''.join(random.choice(chars) for _ in range(size))
		tcp = IP(dst=destination, src=source) / TCP() / Raw(load=random_data())
		send(tcp, iface = interface)
		print "sent TCP"

	elif (random.random() > 0.25):	
		#Beacon
		beaconframe = RadioTap() / Dot11(addr1 = broadcast, addr2 = bssid, addr3 = bssid) / Dot11Beacon(cap = 0x1104) / Dot11Elt( ID=0, info = Beacon_SSID) / Dot11Elt (ID=1, info = "\x84\x84\x8b\x96\x24\30\x48\x6c") / Dot11Elt (ID=3, info = "\x0b") / Dot11Elt (ID=5, info = "\x00\x01\x00\x00")
		sendp(beaconframe, iface = interface)
		print "sent beacon"		

	else:
		#ICMP
		icmp = IP(dst=destination, src=source) / ICMP()/"Hello! Just a Ping"
		send(icmp, iface = interface)
		print "sent icmp"

