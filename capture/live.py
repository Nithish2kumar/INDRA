from scapy.all import sniff, IP,IPv6,TCP,UDP,ARP,Ether
from datetime import datetime

def processPKT(pkt):
    timestamp = datetime.fromtimestamp(
        float(pkt.time)
    ).strftime("%H:%M:%S")

    src_mac = "-"
    dst_mac = "-"
    
    if ARP in pkt:
        src=pkt[ARP].psrc
        dst=pkt[ARP].pdst
        proto="ARP"
        print(
            f"[{timestamp}] {src} → {dst} | "
            f"{proto} | "
            f"MAC: {src_mac} → {dst_mac} | "
            f"Size: {len(pkt)}"
        )
        return

    if IP in pkt:
        src=pkt[IP].src
        dst=pkt[IP].dst
    elif IPv6 in pkt:
        src=pkt[IPv6].src
        dst=pkt[IPv6].dst
    else:
        return

    sport = "-"
    dport = "-"
    proto = "Unknown"
    flags = "-"

    if TCP in pkt:
        sport=pkt[TCP].sport
        dport=pkt[TCP].dport
        proto="TCP"
        flags=pkt[TCP].flags
    elif UDP in pkt:
        sport=pkt[UDP].sport
        dport=pkt[UDP].dport
        proto="UDP"

    if Ether in pkt:
        src_mac=pkt[Ether].src
        dst_mac=pkt[Ether].dst
        proto="Ether"

    

    print(
        f"[{timestamp}] "
        f"{src}:{sport} → {dst}:{dport} | "
        f"{proto} | "
        f"MAC: {src_mac} → {dst_mac} | "
        f"Size: {len(pkt)} | "
        f"Flags: {flags}"
    )

    
def startCapture(inf):
    print("INDRA")
    print("Industrial Network Discovery and Reconnaissance Assistant")
    print()
    print(f"[*] Interface : {inf}")
    print("[*] Mode      : Passive")
    print("[*] Capturing...")
    print("[*] Press Ctrl+C to stop")
    print()
    try:
        sniff(iface=inf,prn=processPKT,store=False)

    except PermissionError:
        print("[!] Permission denied.")
        print("[!] Run INDRA with sudo.")

    except KeyboardInterrupt:
        print("\n[*] Capture stopped.")