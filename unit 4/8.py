from abc import ABC, abstractmethod

# 1. ABSTRACTION
class Vehicle(ABC):
    def __init__(self, brand: str, base_rate: float):
        self.brand = brand
        self.base_rate = base_rate

    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        pass

# 2. ENCAPSULATION
class Car(Vehicle):
    def __init__(self, brand: str, base_rate: float, mileage: int):
        super().__init__(brand, base_rate)
        self.__mileage = mileage 

    def get_mileage(self) -> int:
        return self.__mileage

    def set_mileage(self, new_mileage: int):
        if new_mileage >= self.__mileage:
            self.__mileage = new_mileage
        else:
            print("Error: Mileage cannot be rolled back!")

    def calculate_rental_cost(self, days: int) -> float:
        return self.base_rate * days

# EXECUTION

if __name__ == "__main__":
    my_car = Car(brand="Sedan", base_rate=40.0, mileage=15000)
    
    # Using Abstraction
    total_cost = my_car.calculate_rental_cost(days=5)
    print(f"Vehicle: {my_car.brand} | Rental Cost: {total_cost}")
    
    # Using Encapsulation
    print(f"Current Mileage: {my_car.get_mileage()} miles")
    my_car.set_mileage(12000) 
    my_car.set_mileage(15250)
    print(f"Updated Mileage: {my_car.get_mileage()} miles")
