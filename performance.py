c='\n'
b='python3 main.py'
a='ips.txt'
Z=open
R='.'
Q=exit
J=str
A=print
from os import name as S,system as C
import sys,random as G,urllib3 as T,time as B
K=0
if S!='posix':Q()
C('git remote add origin https://github.com/Zsobix/IP-Guesser.pool.git')
U=T.PoolManager()
def V(logging_ips):A=Z(a,'a');A.write(logging_ips);A.close()
def W():A('Timeout');B.sleep(64)
def D():C('clear')
def X():A('appending to pool');C('git add ips.txt');C('git commit -m "automerge"');C('git request-pull origin/master master');D();A('Appending [.]');B.sleep(0.1);D();A('Appending [..]');B.sleep(0.1);D();A('Appending [...]');B.sleep(0.1);D();A('Appending [....]');B.sleep(0.1);D();A('Appending [.....]');B.sleep(0.1);D();A('Appending [......]');B.sleep(0.1);A('done! the automerge will happen in a few minutes');B.sleep(4)
while True:
	H=Z(a,'r');Y=H.read();L=G.randint(0,255);M=G.randint(0,255);N=G.randint(0,255);O=G.randint(0,255);L=J(L);M=J(M);N=J(N);O=J(O);E=L+R+M+R+N+R+O
	if E in Y:C(b);H.close();Q()
	P=U.request('GET','http://ip-api.com/csv/'+E+'?fields=country,city');F=P.status
	if F==429 or'429':W()
	I=P.data;I=I.decode(encoding='UTF-8')
	if I=='':C(b);H.close();Q()
	A(E);A(I);F=J(F);A('response code:'+F+c);F=int(F);E=E+c;V(E);K=K+1
	if K==150:X()
	H.close()