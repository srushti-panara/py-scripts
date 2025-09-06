def GCD(x,y):
    rem = x%y
    if (rem==0):
        return y
    else:
        return GCD(y,rem)
n= int(input('enter the first no.:'))
m= int(input('enter the second no.:'))
print('The GCD of nos. is', GCD(n,m))