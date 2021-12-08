import os
import random
import urllib3
import time

if os.name != "posix":
	exit()

https_PoolManager = urllib3.PoolManager()

def log(logging):
	logs = open('ips.txt', 'a')
	logs.write(logging)
	logs.close()

while True:
	time.sleep(0.3)
	openips = open('ips.txt', 'r')
	openips2 = openips.read()
	ipnum1 = random.randint(0, 255)
	ipnum2 = random.randint(0, 255)
	ipnum3 = random.randint(0, 255)
	ipnum4 = random.randint(0, 255)
	ipnum1 = str(ipnum1)
	ipnum2 = str(ipnum2)
	ipnum3 = str(ipnum3)
	ipnum4 = str(ipnum4)
	ip = ipnum1 + "." + ipnum2 + "." + ipnum3 + "." + ipnum4
	if ip in openips2:
		os.system("python3 main.py")
		openips.close()
		exit()
	r = https_PoolManager.request('GET', 'http://ip-api.com/csv/' + ip + '?fields=country,city')
	location = r.data
	location = location.decode(encoding='UTF-8')
	if location == "":
		print('a')
		os.system("python3 main.py")
		openips.close()
		exit()
	print(ip)
	print(location)
	ip = ip + '\n'
	log(ip)
	openips.close()