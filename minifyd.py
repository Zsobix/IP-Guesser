W='\n'
V='python3 main.py'
U='ips.txt'
T=open
N='.'
M=print
L=exit
F=str
import os,random as C,urllib3 as O,time
if os.name!='posix':L()
P=O.PoolManager()
def Q(logging_ips):A=T(U,'a');A.write(logging_ips);A.close()
def R():time.sleep(64)
while True:
	D=T(U,'r');S=D.read();G=C.randint(0,255);H=C.randint(0,255);I=C.randint(0,255);J=C.randint(0,255);G=F(G);H=F(H);I=F(I);J=F(J);A=G+N+H+N+I+N+J
	if A in S:os.system(V);D.close();L()
	K=P.request('GET','http://ip-api.com/csv/'+A+'?fields=country,city');B=K.status
	if B==429 or'429':R()
	E=K.data;E=E.decode(encoding='UTF-8')
	if E=='':os.system(V);D.close();L()
	M(A);M(E);B=F(B);M('response code:'+B+W);B=int(B);A=A+W;Q(A);D.close()