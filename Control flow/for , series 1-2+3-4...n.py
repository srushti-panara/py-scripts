n=int(input('enter a no.:'))
s1=0
s2=0
s=0
for i in range(n+1):
    if(i%2!=0):
        s1=s1+i
    if(i%2==0):
        s2=s2-i
s=s1+s2
print('sum=',s)

