import os
import random
import time
import urllib3

nonce = 1
while True:
    a = open("ips.txt", 'r')
    data = a.read()
    point = "."
    space = " "
    ipnum1 = random.randint(0, 255)
    ipnum2 = random.randint(0, 255)
    ipnum3 = random.randint(0, 255)
    ipnum4 = random.randint(0, 255)
    ipnum1 = str(ipnum1)
    ipnum2 = str(ipnum2)
    ipnum3 = str(ipnum3)
    ipnum4 = str(ipnum4)
    fullip = ipnum1 + point + ipnum2 + point + ipnum3 + point + ipnum4
    fullip = str(fullip)
    url = urllib3.PoolManager()
    a = url.request('GET', 'http://ip-api.com/csv/' + fullip + '?fields=country,city')
    cc = a.data
    print("a")
    if cc == b'' or '' or b'\n' or b'/n' or None:
        a.close()
        os.system("python3 ipguess.py")
        exit()
    print("A IP is guessed")
    fullip = fullip + space
    nonce + nonce+1
    print(fullip)
    print(cc)
    if fullip in data:
        a.close()
        time.sleep(1)
        os.system("python3 ipguess.py")
        exit()
    save = open("ips.txt", 'a')
    save.write(fullip)
    save.close()
    nonce = nonce
    if nonce == 340282366920938463463374607431768211456:
        a.close()
        print("Done")
        