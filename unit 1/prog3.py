A = int(input('Enter the number one'))
B = int(input('Enter the number two'))

add = A + B
sub = A - B
mul = A * B
div = A / B

print("addision is",add)
print("substrection is",sub)
print("multilication is",mul)
print("division is",div)

print()


print("***********now relational operater*************")

print("equels:",A==B)
print("not equels:",A!=B)
print("A is greter?",A>B)
print("A is lesser?",A<B)
print("Bis greter?",B>A)
print("B is lesser?",B<A)


print()

print("*********logical operator***********")
 
if(A<B and A>5):
  print(" A is in the range")
elif(B>50 or B<40):
    print("B is in the range")
else:
    print("number are invalid")
if(not (A>B)):
    print("B is bigger")
else:
    print("A is bigger")
    

