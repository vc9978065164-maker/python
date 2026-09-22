##Write a program to explain mutable and immutable objects in Python.
def message(x):
    x.append(44)
    return x

list1 = [11,22,33]
list2=[]

list2= message(list1)
print(list2)

if(len(list2) >= 0):
   print("mutable")
else:
    print("immutable")

print(list2)
