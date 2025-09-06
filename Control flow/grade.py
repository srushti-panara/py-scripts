marks1=int(input('Enter the marks in Mathematics: '))
marks2=int(input('Enter the marks in Science:'))
marks3=int(input('Enter the marks in Social Science:'))
marks4=int(input('Enter the marks in Computer:'))
total= marks1+marks2+marks3+marks4
avg=float(total/4)
print('Total=',total,'\t Aggregate=',avg)
if(avg>=75):
    print('Distinction')
elif (avg >= 60 and avg < 75):
    print('First Division')
elif (avg >= 50 and avg < 60):
    print('Second Division')
elif (avg >= 40 and avg < 50):
    print('Third Division')
else:
    print('Fail')
