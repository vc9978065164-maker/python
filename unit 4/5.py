# single level inheritance.

class Animal:

    def speak(self):
        print("Animal Speaking")

class Dog(Animal):

    def bark(self):
        print("dog barking")

d = Dog()
d.bark()
d.speak()


# multiple inheritance.
class Calculation1:

    def Summation(self,a,b):
        return a+b;

class Calculation2:

    def Multiplication(self,a,b):
        return a*b;

class Derived(Calculation1,Calculation2):

    def Divide(self,a,b):
        return a/b;

d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))