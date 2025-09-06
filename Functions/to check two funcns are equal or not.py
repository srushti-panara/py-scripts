def check_relation(a,b):
    if (a==b):
        return 0
    if (a>b):
        return 1
    if (a<b):
        return -1
a=3
b=5
res = check_relation(a,b)
if (res==0):
    print('a is equal to b')
if (res==1):
    print('a is greater than b')
if (res==-1):
    print('a is less than b')