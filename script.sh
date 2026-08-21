#!/bin/bash

cd /home/nk/Documents/Skills/INDRA

python3 main.py sniff -i wlo1
python3 main.py analyze traffic.pcap
python3 main.py capture -i wlo1 -o traffic.pcap