n=int(input('Enter a no.:'))
n1=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print('Reverse=',rev)
print(n1)
if(n1==rev):
    print('given number is palindrome number')
else:
    print('given number is not palindrome number')
