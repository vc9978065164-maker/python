""" Write a program to find the sum of digits of a 
number using a while loop. """

num = int(input('enter the number : '))
summ=0

while(num>0):
     digit=num%10
     summ=summ+digit
     num=num//10

print(summ)
