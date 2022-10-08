_B='ips.txt'
_A='python main.py'
from os import system as terminal
import random,urllib3,time,base64,ipinfo
acc_token_b64='ODgyZmIwYTNjNTIwZTQ='
acc_token_bytes=base64.b64decode(acc_token_b64)
acc_token=str(acc_token_bytes,'utf-8')
ipcount=0
handler=ipinfo.getHandler(acc_token)
https_PoolManager=urllib3.PoolManager()
def log(ipvalid):A=open(_B,'a');A.write(ipvalid);A.close()
while True:
        openips=open(_B,'r');openips2=openips.read();ipnum1=random.randint(0,255);ipnum2=random.randint(0,255);ipnum3=random.randint(0,255);ipnum4=random.randint(0,255);ipnum1=str(ipnum1);ipnum2=str(ipnum2);ipnum3=str(ipnum3);ipnum4=str(ipnum4);ip=ipnum1+'.'+ipnum2+'.'+ipnum3+'.'+ipnum4
        if ip in openips2:terminal(_A);openips.close();exit()
        r=https_PoolManager.request('GET','http://ip-api.com/csv/'+ip+'?fields=country,city');responsecode=r.status
        if responsecode==429 or'429':
                try:print(ip);details=handler.getDetails(ip);print(details.country+', '+details.city);print('used server: IP-Info')
                except:print('');terminal(_A);exit()
        location=r.data;location=location.decode(encoding='UTF-8')
        if location==''or'\n':openips.close();terminal(_A);exit()
        print(ip);print(location);responsecode=str(responsecode);print('response code:'+responsecode+'\n')
        if responsecode=='200'or'429':print('used server: ip-api')
        responsecode=int(responsecode);ip=ip+',\n';log(ip);openips.close()