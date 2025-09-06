def artriangle(b,h):
    return(0.5*b*h)
b=int(input('enter the base of a triangle='))
h=int(input('enter the height of a triangle='))
result=artriangle(b,h)
print('Area of a triangle',(b,h),'=',result)