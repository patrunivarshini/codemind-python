def sum(s1):
    sum1=0
    for i in s1:
        if i.isdigit()==True:
            z=int(i)
            sum1=sum1+z
    return sum1
s2=input()
print(sum(s2))