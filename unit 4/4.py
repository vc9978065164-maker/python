class clacilator:
    brand = "Casio"
    
    def __init__(self,version):
         self.version = version
         
    def get_version(self):
        return F"Clacilator version: {self.version}"
    
    @classmethod
    def get_brand(cls):
        return F"brand: {cls.brand}"
    
    @staticmethod
    def add(x,y):
        return x + y

calc = clacilator("v2.0")
print(calc.get_version())
print(clacilator.get_brand())
print(clacilator.add(5,10))
