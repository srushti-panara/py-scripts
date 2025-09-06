def outer_func():
    var=10
    def inner_funcn():
        var=20
        print('Inner function=',var)
    inner_funcn()
    print('Outer function=',var)
outer_func()