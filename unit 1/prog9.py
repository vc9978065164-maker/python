#Write a program to define and use user-definedfunctions with different types of arguments
def display(no):
    print(no)
def display1(*str1):
    print('varible lenght argument',str1)
def display2(age,name):
    print(age,name)

display(101)
display1('marawdi','university')
display2(age=21,name='Vivek')
