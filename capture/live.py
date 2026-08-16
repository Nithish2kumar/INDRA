from scapy.all import sniff, IP,IPv6,TCP,UDP,ARP

def processPKT(pkt):
    if ARP in pkt:
        src=pkt[ARP].psrc
        dst=pkt[ARP].pdst
        proto="ARP"
        print(f"{src} → {dst} | {protocol}")
        return

    if IP in pkt:
        src=pkt[IP].src
        dst=pkt[IP].dst
    elif IPv6 in pkt:
        src=pkt[IPv6].src
        dst=pkt[IPv6].dst
    else:
        return

    if TCP in pkt:
        sport=pkt[TCP].sport
        dport=pkt[TCP].dport
        proto="TCP"
    elif UDP in pkt:
        sport=pkt[UDP].sport
        dport=pkt[UDP].dport
    else:
        proto=pkt.lastlayer().name
        sport="-"
        dport="-"

    print(f"{src}:{sport} → {dst}:{dport} | "
        f"{proto} | Size: {len(pkt)}")
    
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
        sniff(iface=inf,prn=process_packet,store=False)

    except PermissionError:
        print("[!] Permission denied.")
        print("[!] Run INDRA with sudo.")

    except KeyboardInterrupt:
        print("\n[*] Capture stopped.")