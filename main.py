import argparse
from capture.live import startCapture

def main():
    parser=argparse.ArgumentParser(description="INDRA - Industrial Network Discovery and Reconnaissance Assistant")
    subparser=parser.add_subparsers(dest="command")
    sniff_parser=subparser.add_parser("sniff",help="Capture live network traffic")
    sniff_parser.add_argument("-i","--interface",required=True,help="Network interface to capture from")
    arg=parser.parse_args()

    if arg.command=="sniff":
        startCapture(arg.interface)
    else:
        parser.print_help()

if __name__=="__main__":
    main()
