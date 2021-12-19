b='\n'
a='python3 performance.py'
Z='a'
Y='ips.txt'
X=open
Q='.'
P=exit
H=str
D=print
import os as A,random as E,urllib3 as R,time as N
I=0
if A.name!='posix':P()
A.system('git remote add origin https://github.com/Zsobix/IP-Guesser.pool.git')
S=R.PoolManager()
def T(logging_ips):A=X(Y,Z);A.write(logging_ips);A.close()
def U():D(Z);N.sleep(64)
def V():D('appending to pool');A.system('git commit -m "automerge"');A.system('git request-pull origin/master master');D('done! the automerge will happen in a few minutes');N.sleep(4)
while True:
	F=X(Y,'r');W=F.read();J=E.randint(0,255);K=E.randint(0,255);L=E.randint(0,255);M=E.randint(0,255);J=H(J);K=H(K);L=H(L);M=H(M);B=J+Q+K+Q+L+Q+M
	if B in W:A.system(a);F.close();P()
	O=S.request('GET','http://ip-api.com/csv/'+B+'?fields=country,city');C=O.status
	if C==429 or'429':U()
	G=O.data;G=G.decode(encoding='UTF-8')
	if G=='':A.system(a);F.close();P()
	D(B);D(G);C=H(C);D('response code:'+C+b);C=int(C);B=B+b;T(B);I=I+1
	if I==15:V()
	F.close()