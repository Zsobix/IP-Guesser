from os import system as terminal
import random
import time
import base64
import ipinfo

acc_token_b64 = "ODgyZmIwYTNjNTIwZTQ="
acc_token_bytes = base64.b64decode(acc_token_b64)
acc_token = str(acc_token_bytes, "utf-8")
ipcount = 0
handler = ipinfo.getHandler(acc_token)

def log(ipvalid):
	logs = open('ips.txt', 'a')
	logs.write(ipvalid)
	logs.close()

while True:
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
		terminal("python main.py")
		openips.close()
		exit()
	print(ip)
	try:
		details = handler.getDetails(ip)
		print(details.country + ', ' + details.city)
		print("used server: IP-Info")
		if details.country or details.city == "" or "\n":
			openips.close()
			terminal("python main.py")
			exit()
	except:
		terminal('python main.py')
		exit()
	ip = ip + ',\n'
	log(ip)
	openips.close()
