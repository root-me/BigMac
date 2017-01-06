import sys
import json
import requests
from scapy.all import *

if len(sys.argv) != 2:
    print "Usage: BigMac.py <IP RANGE>"
    sys.exit(1)

MAC_URL = 'http://macvendors.co/api/%s'

conf.verb=0
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),
              timeout=2)

for snd,rcv in ans:
    r = requests.get(MAC_URL % rcv.sprintf(r"%ARP.psrc%"))
    if('error' in r.text):
        print rcv.sprintf(r"%Ether.src% & %ARP.psrc%")
    else:
        binary = r.content
        output = json.loads(binary)
        print recv.sprintf(r"%Ether.src% & %ARP.psrc% &") + output['result']['company']
