def fact(n):
    f=1
    if (n==0 or n==1):
        return 1
    else:
        for i in range(1,int(n+1)):
            f=f*i
    return f
n=int(input('enter the value of n:'))
s=0
for i in range(1,n+1):
    s=s+(float(i**i)/fact(i))
print('Result:',s)