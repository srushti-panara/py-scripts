def evenodd(a):
    if(a%2==0):
        return 1
    else:
        return -1
a=int(input('Enter the no.:'))
flag = evenodd(a)
if(flag==1):
    print('No. is even')
if (flag==-1):
    print('No. is odd')