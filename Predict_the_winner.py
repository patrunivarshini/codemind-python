n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in l:
    if(i%2==0):
        s1=s1+i
for j in l:
    if(j%2!=0):
        s2=s2+j
if((abs(s1-s2))%4==0):
    print("X")
else:
    print("Y")