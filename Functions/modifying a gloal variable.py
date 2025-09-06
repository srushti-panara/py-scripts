var='good'
def show():
    global var
    var='morning'
    print('in function var is=',var)
show()
print('outside function,var is=',var)
var='fantastic'
print('outside function, after modification, var is =',var)