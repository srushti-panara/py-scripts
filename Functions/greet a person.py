def greet(name, mesg):
    '''This function welcomes the person passed whose name is passes as a parameter'''
    print('Welcome,' + name + '.' + mesg)
mesg= 'Happy Reading. Python is Fun!'
name= input('\nEnter your name:')
greet(name, mesg)