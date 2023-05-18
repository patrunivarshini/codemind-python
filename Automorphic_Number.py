n=int(input())
l=len(str(n))
s=n*n
m=s%(10**l)
if(m==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")