#!/bin/python3

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

def append(ipcount):
	print("appending to pool")
	terminal('git add ips.txt')
	terminal('git commit -m "automerge"')
	terminal('git request-pull origin/master master')
	clear()
	print("Appending [.]")
	time.sleep(0.2)
	clear()
	print("Appending [..]")
	time.sleep(0.2)
	clear()
	print("Appending [...]")
	time.sleep(0.2)
	clear()
	print("Appending [....]")
	time.sleep(0.2)
	clear()
	print("Appending [.....]")
	time.sleep(0.2)
	clear()
	print("Appending [......]")
	time.sleep(0.2)
	clear()
	print("Appending [.......]")
	time.sleep(0.2)
	clear()
	print("Appending [........]")
	time.sleep(0.2)
	clear()
	print("Appending [.........]")
	time.sleep(0.2)
	clear()
	print("Appending [..........]")
	time.sleep(0.2)
	clear()
	print("Appending [...........]")
	time.sleep(0.2)
	clear()
	print("Appending [............]")
	time.sleep(0.2)
	print("done! the automerge will happen in a few minutes")
	ipcount = 0

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
		terminal("python3 main.py")
		openips.close()
		exit()
	try:
		print(ip)
		details = handler.getDetails(ip)
		print(details.country + ', ' + details.city)
	except:
		print('')
		terminal('python3 main.py')
		exit()
	ip = ip + ',\n'
	log(ip)
	if ipcount <= 150: 
		ipcount = 0
	ipcount = ipcount+1
	openips.close()
