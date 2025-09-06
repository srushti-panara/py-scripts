n=int(input('enter a no.:'))
f=1
s=0
for i in range(1,n+1):
    f=f*i
    s=s+(1/f)
print('sum=',s)