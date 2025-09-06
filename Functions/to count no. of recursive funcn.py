def func(n, count=0):
    if n==0:
        return count
    else:
        return func(n-1, count +1)
print('No. of times recursive function was invoked=', func(100))