class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display_info(self):
        print(f"student name: {self.name},age: {self.age}")
        
student1 = Student("vivek",21)
student1.display_info()
