class Car():
    total_cars=0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        Car.total_cars += 1
    def get_brand(self):
        return self.__brand
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return 'Petrol or Diesel'
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return 'Electric Charger'

car1=Car("Brand1","Model1")
print(car1.model)
# print(car1.fuel_type())

# car2=Car("Brand2","Model2")
# print(car2.fuel_type())

# electricCar1=ElectricCar("Tesla","Model 1","20Kwh")
# print(electricCar1.fuel_type())

# print(Car.total_cars)
