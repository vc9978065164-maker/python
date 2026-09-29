class Emplyee:
    company_name = "tech crop"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
emp1 = Emplyee("vivek",21000) 
emp2 = Emplyee("prince",22000)

print(f"{emp1.name} work at {emp1.company_name}") 
print(f"{emp2.name} work at {emp2.company_name}")       