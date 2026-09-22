"""Write a program to check whether a number is 
positive negative or zero using nested 
conditions."""

num = int(input('Enter the number :'))

if(num>=0):
    if(num == 0):
        print('number is 0.')
    else:
        print('number is positive.')
else:
    print('number is negative.')
