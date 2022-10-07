from os import name as sysname
from os import system as terminal
import random
import urllib3
import time
import base64
import ipinfo

acc_token_b64 = "ODgyZmIwYTNjNTIwZTQ="
acc_token_bytes = base64.b64decode(acc_token_b64)
acc_token = str(acc_token_bytes, "utf-8")
ipcount = 0
handler = ipinfo.getHandler(acc_token)
if sysname != "posix":
	exit()

https_PoolManager = urllib3.PoolManager()

def log(logging_ips):
	logs = open('ips.txt', 'a')
	logs.write(logging_ips)
	logs.close()

def timeout():
	print('Timeout')
	time.sleep(320)

def servertimeout():
	print('Server Timeout')
	print('Please wait')
	time.sleep()

def clear():
	terminal("clear")
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
	r = https_PoolManager.request('GET', 'http://ip-api.com/csv/' + ip + '?fields=country,city')
	responsecode = r.status
	if responsecode == 429 or "429":
		try:
			print(ip)
			details = handler.getDetails(ip)
			print(details.country + ', ' + details.city)
			print("used server: IP-Info")
		except:
			print('')
			terminal('python main.py')
			exit()
	location = r.data
	location = location.decode(encoding='UTF-8')
	if location == "":
		terminal("python3 main.py")
		openips.close()
		exit()
	print(ip)
	print(location)
	responsecode = str(responsecode)
	print('response code:' + responsecode + '\n')
	if responsecode == "200" or "429":
		print("used server: ip-api")
	responsecode = int(responsecode)
	ip = ip + ',\n'
	log(ip)
	openips.close()
