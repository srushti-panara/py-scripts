n=int(input('enter a no.:'))
s=0
for i in range(1, n):
    if (n%i==0):
        s=s+i
if(s==n):
    print('given no.is a perfect no.')
else:
    print('given no. is not a perfect no.')
