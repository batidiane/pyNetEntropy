import pcap
import sys
import string
import time
import socket
import struct
import dpkt
#see http://pylibpcap.sourceforge.net/

protocols={socket.IPPROTO_TCP:'tcp',
           socket.IPPROTO_UDP:'udp',
           socket.IPPROTO_ICMP:'icmp'}

def decodeipv4(ip):
    pktinfos = dict()
    pktinfos['src_addr'] = pcap.ntoa(struct.unpack('i',ip.src)[0])
    pktinfos['dst_addr'] = pcap.ntoa(struct.unpack('i',ip.dst)[0])
    pktinfos['proto'] = ip.p
    
    if dpkt.ip.IP_PROTO_TCP == ip.p: #Check for TCP packets
        tcp = ip.data
        pktinfos['proto_name'] = 'TCP'
        pktinfos['src_port'] = tcp.sport
        pktinfos['dst_port'] = tcp.dport
        payload = tcp.data
    elif dpkt.ip.IP_PROTO_UDP == ip.p: #Check for UDP packets
        udp = ip.data
        pktinfos['proto_name'] = 'UDP'
        pktinfos['src_port'] = udp.sport
        pktinfos['dst_port'] = udp.dport
        payload = udp.data
    elif dpkt.ip.IP_PROTO_ICMP == ip.p: #Check for ICMP packets
        icmp = ip.data
        pktinfos['proto_name'] = 'ICMP'
        pktinfos['src_port'] = 0
        pktinfos['dst_port'] = 0
        payload = str(icmp.data)
    else:
        return None, None
           
    return pktinfos, payload
    

def extractpayload(eth):
    if dpkt.ethernet.ETH_TYPE_IP == eth.type:      # ipv4 packet
        return decodeipv4(eth.data)
    elif dpkt.ethernet.ETH_TYPE_IP6 == eth.type:    # ipv6 packet
        return None, None
    elif dpkt.ethernet.ETH_TYPE_ARP == eth.type:    # arp packet
        return None, None
    elif dpkt.ethernet.ETH_TYPE_REVARP == eth.type:    # rarp packet
        return None, None
    else:
        return None, None