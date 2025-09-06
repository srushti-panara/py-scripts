n=int(input('enter a no.:'))
s=0
i=1
while(i<n):
    if(n%i==0):
        s=s+i
    i=i+1
if(s==n):
    print('given no.is a perfect no.')
else:
    print('given no. is not a perfect no.')
