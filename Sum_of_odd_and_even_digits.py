n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,len(l)):
    if (i%2==0):
        s1=s1+l[i]
for j in range(0,len(l)):
    if(j%2!=0):
        s2=s2+l[j]
if(s2-s1==0):
    print("YES")
else:
    print("NO")