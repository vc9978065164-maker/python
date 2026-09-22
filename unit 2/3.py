"""Write a program to generate a multiplication 
table using a for loop"""

t = float(input('enter the number :'))

for i in range(1,11):
    print(f'{t} * {i} = {t*i}')
    
