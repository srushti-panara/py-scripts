def pattern(c= '%',n=6, r=1):
    for i in range(r):
        print()
        for j in range(n):
            print(c, end=' ')
c= input('enter the character to be displayed:')
n= int(input('enter the no. of rows:'))
m= int(input('enter the no. of columns:'))
pattern()
pattern(c)
pattern(c,n)
pattern(c,n,m)