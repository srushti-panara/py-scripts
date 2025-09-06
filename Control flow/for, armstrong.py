n=int(input('Enter a no.:'))
n1=n
rev=0
for i in range(n+1>0):
    rem=n%10
    rev=rev+ rem*rem*rem
    n=n//10
print('Reverse=',rev)
print(n1)
if(n1==rev):
    print('armstrong of a no. =',rev)
else:
    print('given no. is not armstrong')
