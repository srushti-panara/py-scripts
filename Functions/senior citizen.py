def interest(p,y,s):
    if (s=='y'):
        SI = float((p*y*12)/100)
    else:
        SI = float ((p*y*10)/100)
    return SI
p=float(input('Enter the principle amount:'))
y= float(input('Enter the no. of years:'))
senior = input('Is customer senior citizen(y/n):')
print('Interest:', interest(p,y,senior))