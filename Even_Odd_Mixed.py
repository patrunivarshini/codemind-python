n=int(input())
c1=0
c2=0
while n>0:
    t=n%10
    if(t%2==0):
        c1+=1
    else:
        c2+=1
    n=n//10
if(c1>0 and c2==0 ):
    print("Even")
elif(c1==0 and c2>0):
    print("Odd")
else:
    print("Mixed")