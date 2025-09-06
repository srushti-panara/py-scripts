import math
total_prime = 0
total_composite = 0

while(1):
    num = int(input('enter a no.:'))
    if (num ==999):
        break
    elif num<0:
        print('cube root of negative nos. cannot be calculted')
        continue
    else:
        print('cube root of', num, '=', math.cbrt(num))