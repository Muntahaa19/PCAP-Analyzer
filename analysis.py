import pandas as pd
from collections import Counter

BLACKLISTED_IPS = {"192.168.1.100", "45.33.32.156"}  # Replace with actual malicious IPs

def detect_threats(packets):
    if not packets:
        print("No packets to analyze.")
        return

    df = pd.DataFrame(packets)

    # Port Scanning Detection (Same IP hitting many ports)
    port_scan_threshold = 10
    port_scanners = df.groupby("src_ip")["dst_port"].nunique()
    port_scanners = port_scanners[port_scanners > port_scan_threshold]

    # DDoS Attack Detection (High packet count from one IP)
    ddos_threshold = df["src_ip"].value_counts().mean() * 3
    ddos_attackers = df["src_ip"].value_counts()
    ddos_attackers = ddos_attackers[ddos_attackers > ddos_threshold]

    # ARP Spoofing Detection (Multiple ARP responses)
    arp_spoofing = df[df["arp_opcode"] == "2"].groupby("src_ip").size()
    arp_spoofing = arp_spoofing[arp_spoofing > 5]

    # DNS Spoofing Detection (Same domain but different IPs)
    dns_spoofing = df.groupby("dns_query")["dst_ip"].nunique()
    dns_spoofing = dns_spoofing[dns_spoofing > 1]

    # Blacklisted IP Detection
    blacklisted_hits = df[df["src_ip"].isin(BLACKLISTED_IPS)]

    # Alerts
    if not port_scanners.empty:
        print("\n⚠️ Port Scanning Detected:")
        for ip, count in port_scanners.items():
            print(f" - {ip} scanned {count} ports")

    if not ddos_attackers.empty:
        print("\n🚨 Possible DDoS Attack Detected:")
        for ip, count in ddos_attackers.items():
            print(f" - {ip} sent {count} packets (Suspicious!)")

    if not arp_spoofing.empty:
        print("\n🛑 ARP Spoofing Detected!")
        for ip, count in arp_spoofing.items():
            print(f" - {ip} sent {count} ARP replies without request!")

    if not dns_spoofing.empty:
        print("\n⚠️ DNS Spoofing Detected!")
        for domain, count in dns_spoofing.items():
            print(f" - {domain} resolved to {count} different IPs!")

    if not blacklisted_hits.empty:
        print("\n🔥 Malicious IP Detected!")
        for ip in blacklisted_hits["src_ip"].unique():
            print(f" - {ip} is blacklisted!")

    if port_scanners.empty and ddos_attackers.empty and blacklisted_hits.empty and arp_spoofing.empty and dns_spoofing.empty:
        print("\n✅ No known threats detected!")
