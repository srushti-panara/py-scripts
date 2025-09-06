ch=input('enter the sex of the employee(m or f):')
sal=int(input('Enter the salary of the employee:'))
if (ch=='m'):
    bonus=0.05*sal
else:
    bonus=0.10*sal
amt_to_be_paid = sal+bonus
print('Salary=',sal)
print('Bonus=',bonus)
print('****************************************')
print('Amount to be paid:',amt_to_be_paid)