import argparse
from capture.live import startCapture
from capture.pcap import capturePcap

def main():
    parser=argparse.ArgumentParser(description="INDRA - Industrial Network Discovery and Reconnaissance Assistant")
    subparser=parser.add_subparsers(dest="command")
    sniff_parser=subparser.add_parser("sniff",help="Capture live network traffic")
    sniff_parser.add_argument("-i","--interface",required=True,help="Network interface to capture from")
    
    pcap_parser=subparser.add_parser("capture",help="Capture traffic and save it as PCAP")
    pcap_parser.add_argument("-i","--interface",required=True,help="Network interface to capture from")
    pcap_parser.add_argument("-o","--output",required=True,help="Output PCAP file")
    arg=parser.parse_args()

    if arg.command=="sniff":
        startCapture(arg.interface)
    elif arg.command=="capture":
        capturePcap(arg.interface,arg.output)
    else:
        parser.print_help()

if __name__=="__main__":
    main()
