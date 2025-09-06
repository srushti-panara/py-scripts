def exp_rec(x,y):
    if (y==0):
        return 1
    else:
        return (x*exp_rec (x,y-1))
n=int(input('enter the first no.:'))
m= int(input('enter the second no.:'))
print('Result=', exp_rec(n,m))