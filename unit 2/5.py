n= input('enter the number : ')

if('.' in n):
    my= n.split('.')
    print(my)
else:
    my=n
    
if(my[1]=='0'):
    n = float(n)
    n=int(n)
else:
    n = float(n)
    
for i in range(1,11):
    print(f'{n}  *   {i}   =   {n*i}')
