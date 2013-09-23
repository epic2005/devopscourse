#!/usr/bin/env python

from scapy.all import *

#p = sniff(filter="tcp port 8080", lfilter=lambda x:x.haslayer(Raw),prn=lambda x:x.sprintf('%Raw.load%'))
#p = sniff(filter="src 127.0.0.1 and tcp port 11211",lfilter=lambda x:x.haslayer(Raw),prn=lambda x:x.sprintf('%Raw.load%'))

try:
    p = sniff(filter="src 127.0.0.1 and tcp port 11211", lfilter=lambda x:x.haslayer(Raw),prn=lambda x:x.lastlayer().load.split()[1])
    print p
except: 
    print 'ERROR' 
