n=int(input('Enter a no.:'))
i=1; f=1
s=0
while(i<=n):
    f=f*i
    s=(s+f)
    i=i+1
print('Sum=',s)