from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        print(f"Source IP: {packet[IP].src} --> Destination IP: {packet[IP].dst} | Protocol: {packet[IP].proto}")

# Sniff 50 packets
sniff(count=50, prn=packet_callback, store=0)
