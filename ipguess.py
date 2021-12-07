import os
import random
import urllib3

if os.name != "posix":
	exit()

http = urllib3.PoolManager()

def log(watlog):
	asdasd = open('ips.txt', 'a')
	asdasd.write(watlog)
	asdasd.close()

while True:
	openips = open('ips.txt', 'r')
	asd = openips.read()
	ipnum1 = random.randint(0, 255)
	ipnum2 = random.randint(0, 255)
	ipnum3 = random.randint(0, 255)
	ipnum4 = random.randint(0, 255)
	ipnum1 = str(ipnum1)
	ipnum2 = str(ipnum2)
	ipnum3 = str(ipnum3)
	ipnum4 = str(ipnum4)
	ip = ipnum1 + "." + ipnum2 + "." + ipnum3 + "." + ipnum4
	if ip in asd:
		os.system("python3 ipguess.py")
		openips.close()
		exit()
	r = http.request('GET', 'http://ip-api.com/csv/' + ip + '?fields=country,city')
	response = r.data
	response = response.decode(encoding='UTF-8')
	if response == "":
		print('a')
		os.system("python3 ipguess.py")
		openips.close()
		exit()
	print(ip)
	print(response)
	ip = ip + '\n'
	log(ip)
	openips.close()


