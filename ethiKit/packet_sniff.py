import scapy.all as scapy

def sniff_packets(interface, protocol=None):
    if protocol:
        filter_expression = f"{protocol}"
        scapy.sniff(iface=interface, filter=filter_expression, store=False, prn=process_packet)
    else:
        scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    print(packet.summary())

# User input for the network interface and protocol
interface = input("Enter the network interface to sniff packets (e.g., 'Wi-Fi', 'Ethernet'): ")
protocol = input("Enter the protocol to filter (TCP/UDP), or leave blank for all traffic: ").upper()

# Start sniffing packets on the specified interface and protocol
sniff_packets(interface, protocol)
