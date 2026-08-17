from scapy.all import sniff, wrpcap, rdpcap
from live import processPKT

def capturePcap(inf, of):

    print("INDRA")
    print("Industrial Network Discovery and Reconnaissance Assistant")
    print()
    print(f"[*] Interface : {inf}")
    print("[*] Mode      : PCAP Capture")
    print(f"[*] Output    : {of}")
    print("[*] Capturing...")
    print("[*] Press Ctrl+C to stop")
    print()

    packets=[]

    try:
        packets=sniff(iface=inf,store=True)

    except PermissionError:
        print("[!] Permission denied.")
        print("[!] Run INDRA with sudo.")
        return

    except KeyboardInterrupt:
        print("\n[*] Capture stopped.")

    if packets:
        wrpcap(of, packets)
        print(f"[+] Saved {len(packets)} packets")
        print(f"[+] PCAP: {of}")
    else:
        print("[!] No packets captured.")


def readPCAP(pcapfile):
    packets=rdpcap(pcapfile)
    for pkt in packets:
        processPKT(pkt)