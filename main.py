#!/bin/python3

from os import name as sysname
from os import system as terminal
import sys
import random
import urllib3
import time

ipcount = 0

if sysname != "posix":
	exit()

terminal('git remote add origin https://github.com/Zsobix/IP-Guesser.pool.git')

https_PoolManager = urllib3.PoolManager()

def log(logging_ips):
	logs = open('ips.txt', 'a')
	logs.write(logging_ips)
	logs.close()

def timeout():
	print('Timeout')
	time.sleep(64)

def clear():
	terminal("clear")

def append():
	print("appending to pool")
	terminal('git add ips.txt')
	terminal('git commit -m "automerge"')
	terminal('git request-pull origin/master master')
	clear()
	print("Appending [.]")
	time.sleep(0.1)
	clear()
	print("Appending [..]")
	time.sleep(0.1)
	clear()
	print("Appending [...]")
	time.sleep(0.1)
	clear()
	print("Appending [....]")
	time.sleep(0.1)
	clear()
	print("Appending [.....]")
	time.sleep(0.1)
	clear()
	print("Appending [......]")
	time.sleep(0.1)
	print("done! the automerge will happen in a few minutes")
	time.sleep(4)

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
	r = https_PoolManager.request('GET', 'http://ip-api.com/csv/' + ip + '?fields=country,city')
	responsecode = r.status
	if responsecode == 429 or "429":
		timeout()
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
	responsecode = int(responsecode)
	ip = ip + '\n'
	log(ip)
	ipcount = ipcount+1
	if ipcount == 150:
		append()
	openips.close()