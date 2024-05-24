#!/usr/bin/env python3

## IP-Guesser Rewritten
## https://github.com/Zsobix/IP-Guesser

import random
import ipinfo
acc_token = "882fb0a3c520e4"
handler = ipinfo.getHandler(acc_token)
ips = []
while True:
    list = []
    for i in range(4):
        list.append(str(random.randint(1,255)))
    ip = f"{list[0]}.{list[1]}.{list[2]}.{list[3]}"
    try:
        details = handler.getDetails(ip)
        print(f"{details.country},  {details.city}: {ip}")
        ips.append(ip)
    except:
        continue
    if len(ips) > 50:
        with open('ips.txt', 'a') as save:
            for count in range(len(ips)-1):
                save.write(f"{ips[count]}\n")
            save.close()
        ips = []
