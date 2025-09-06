print('Enter choice:')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
Choice=int(input('Enter choice:'))
if (Choice==1):
    a=int(input('enter first no.:'))
    b=int(input('enter second no.:'))
    c=a+b
    print('Addition=',c)
if (Choice==2):
    a = int(input('enter first no.:'))
    b = int(input('enter second no.:'))
    c=a-b
    print('Subtraction=',c)
if (Choice==3):
    a = int(input('enter first no.:'))
    b = int(input('enter second no.:'))
    c=a*b
    print('Multiplication=',c)
if (Choice==4):
    a = int(input('enter first no.:'))
    b = int(input('enter second no.:'))
    c=a/b
    print('Division=',c)