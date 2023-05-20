import math
n=int(input())
s=0
t=n
a=abs(n)
while(a!=0):
    s=s*10+a%10
    a=a//10
if t>0:
    print(s)
else:
    print(-1*s)