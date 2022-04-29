# StandWithUkraine.py
# Scan for insecure russian VNCs
# update:  fixed prgm still inefficient
# todo:    make sure ip is owned or something, use it on real ip to confirm whether it works [ withgout doxxing urself ]
# - completed insecure vnc scanner
# we need an extremely fast internet connection AND wifi to accomplish this, using multiple repls as a cluster with boosted/always up could work but its not allowed without giving monies
# SO we should make a server at home (gaming pc rtx 10000) for it to be efficient enough
# and then thers socket timeouts so we need to check whether the ip is owned or not

import socket
import random
import os
from termcolor import colored
from pyfiglet import figlet_format

os.system("clear")
print((colored(figlet_format("vnci",font="radical_"), color="blue")))

TCP_PORTS = [443, 5900] # VNC port
CURRENT_INDEX = 0

def portscan():
  # intervalcolor = colored("| ", color=random.choice("red, green, yellow, blue, magenta, cyan, white".split(", ")))
  print(intervalcolor+"Scanning IP: "+generatedip)
  try:
    socket.inet_aton(generatedip)
    print(intervalcolor + "IP exists.")
  except socket.error:
    print(intervalcolor + "Can't scan IP. Next..")
    return 0
  for port in TCP_PORTS:
    portscancolor = colored("| ", color=random.choice("red, green, yellow, blue, magenta, cyan, white".split(", ")))
    print(intervalcolor+portscancolor+"Connecting to port "+str(port)+"..")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    print(intervalcolor+portscancolor+"Creating socket..")
    result = sock.connect_ex((generatedip,port))
    print(intervalcolor+portscancolor+"Connected!")
    if result == 0:
      print(intervalcolor+portscancolor+"Port is open")
      exit(0)
    else:
      print(intervalcolor+portscancolor+"Port is closed")
lead = [[5,136,None,None],[95,24,None,None],[176,208,None,None]]
while True:
  for i in lead:
    for j in range(1,255):
      for k in range(1,255):
        intervalcolor = colored("| ", color=random.choice("red, green, yellow, blue, magenta, cyan, white".split(", ")))
        CURRENT_INDEX += 1
        leadcopy = [i[0],i[1],j,k]
        generatedip = ".".join([str(x) for x in leadcopy])
        print(intervalcolor + generatedip + " @ index "+str(CURRENT_INDEX))
        portscan()

# 10.0.0.0 — 10.255.255.255;
# 172.16.0.0 — 172.31.255.255; 
# 192.168.0.0 — 192.168.255.255
# Example: 10.11.12.13