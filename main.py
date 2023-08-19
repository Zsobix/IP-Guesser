from os import system as terminal
import random
import urllib3
import time
import base64
import ipinfo
import os



acc_token_input = input("(If you had an old session press ENTER)\n" +"What is your IP-Info API key?\n" + "If you don't have one please register at https://ipinfo.io/ \n" + "API key: ")

try:
	session = open("session.token", "r")
	acc_token_input = session.read()

except:
	session = open("session.token", "w")
	session_write = session.write(acc_token_input)

acc_token = acc_token_input
ipcount = 0
handler = ipinfo.getHandler(acc_token)
https_PoolManager = urllib3.PoolManager()

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
		openips.close()
		continue
	r = https_PoolManager.request('GET', 'http://ip-api.com/csv/' + ip + '?fields=country,city')
	responsecode = r.status
	if responsecode == 429 or "429":
		try:
			print(ip)
			details = handler.getDetails(ip)
			print(details.country + ', ' + details.city)
			print("used server: IP-Info")
		except:
			openips.close()
			continue
	location = r.data
	location = location.decode(encoding='UTF-8')
	if location == "" or "\n":
		openips.close()
		continue
	print(location)
	responsecode = str(responsecode)
	print('response code:' + responsecode + '\n')
	if responsecode == "200" or "429":
		print("used server: ip-api")
	responsecode = int(responsecode)
	ip = ip + ',\n'
	log(ip)
	openips.close()
