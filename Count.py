n=int(input())
l=list(map(int,input().split()))
c1=0
c2=0
for i in range(n):
    if(l[i]%2==0):
        c1+=1
for j in range(n):
    if(l[j]%2==1):
        c2+=1
print(c1,c2,end=" ")