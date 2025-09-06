def swap(a,b):
    a,b = b,a
    print('After swap:')
    print('First no.=',a)
    print('Second no.=',b)
a=input('\nEnter the first no.:')
b=input('\nEnter the second no.:')
print('Before swap:')
print('First no.:',a)
print('Second no.',b)
swap(a,b)