"""Write a program to demonstrate conditional statements using if if-else and if-elif-else."""

marks = int(input('enter the marks : '))

if(marks>=0 and marks<45):
    print('you are fail.')
else:
    print('you are pass.')

    
if(marks >= 90 and marks <= 100 ):
    print('your grade is A. ')
elif(marks >= 70 and marks < 90):
    print('your grade is B. ')
elif(marks >= 60 and marks < 70):
    print('your grade is C.')
elif(marks >= 45 and marks < 60 ):
    print('your grade is D')
elif(marks >= 0 and marks < 45 ):
    print('your grade is E ')
else:
    ('Enter a valid choice')
