num1=10
print('Global variable num1 =',num1)
def func(num2):
    print('In Function - Local Variable num2=',num2)
    num3=30
    print('In Function - Local variable num3=',num3)
func(20)
print('num1 again=',num1)
print('num3 outside function=',num3)