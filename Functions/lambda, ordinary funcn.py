def increment(y):
    return(lambda x: x+1)(y)
a=100
print('a=',a)

b=increment(a)
print('a after incrementing=',b)
