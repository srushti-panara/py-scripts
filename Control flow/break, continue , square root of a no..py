import math
total_prime = 0
total_composite = 0

while(1):
    num = int(input('enter a no.:'))
    if (num ==999):
        break
    elif num<0:
        print('square root of negative nos. cannot be calculted')
        continue
    else:
        print('square root of', num, '=', math.sqrt(num))