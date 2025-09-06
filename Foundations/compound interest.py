P=int(input('enter principal amount='))
R=int(input('enter rate of interest(in %)='))
T=int(input('enter total time span='))
N=int(input('enter no. of times interest is compounded per year='))
CI=(P*(1+(R/100))**(N))-P
print('Compound Interest=',CI)