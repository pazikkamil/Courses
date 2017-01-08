#!/usr/bin/env bash

# write pcap file
tcpdump -w 08232010.pcap -i eth0

# read pcap file
tcpdump -tttt -r data.pcap

# filter real process
sudo tcpdump -Q "(proc =nc)"