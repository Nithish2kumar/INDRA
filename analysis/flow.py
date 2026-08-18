from scapy.all import rdpcap, IP, TCP,UDP

def extractFlow(pcap):
    pkt=rdpcap(pcap)
    flows={}
    for p in pkt:
        if IP not in p:
            continue
        srcIP=p[IP].src
        dstIP=p[IP].dst

        if TCP in p:
            sport=p[TCP].sport
            dport=p[TCP].dport
            proto="TCP"
        elif UDP in p:
            proto="UDP"
            sport=p[UDP].sport
            dport=p[UDP].dport
        else:
            continue

        key=(srcIP,dstIP,sport,dport,proto)
        if key not in flows:
            flows[key]={
                "src_ip":srcIP,
                "dst_ip":dstIP,
                "src_port":sport,
                "dst_port":dport,
                "proto":proto,
                "packets":0,
                "bytes":0,
                "start":float(p.time),
                "end":float(p.time)
            }
        flow=flows[key]
        flow["packets"]+=1
        flow["bytes"]+=len(p)
        flow["end"]=float(p.time)
    return flows
