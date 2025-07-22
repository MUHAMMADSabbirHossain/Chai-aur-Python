class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        # self.total_car += 1
        Car.total_car += 1

    def hello():
        print("Hello")

    def get_brand(self):
        return self.__brand + " !"
    
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transportation"

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__ (self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")
print(isinstance(my_tesla, ElectricCar))
print(isinstance(my_tesla, Car))
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.brand)
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
# print(safari.fuel_type())

print(Car.total_car)
print(Car.general_description())

my_car = Car("Tata", "Safari")
# my_car.model = "City"
print(my_car.model)
# print(my_car.model())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Car, Battery, Engine):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())

