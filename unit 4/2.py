class Resource:
    def __init__(self,name):
        self.name = name
        print(f"constructor: Resource'{self.name}' allocated.")
        
    def __del__(self):
        print(f"destructor: Resource'{self.name}' released.")
        
obj = Resource("Database Connection")
del obj
