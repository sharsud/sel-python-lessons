#
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def __str__(self):
#         return f'{self.brand} {self.model}'
#
#     def __repr__(self):
#         return f'Car({self.brand} {self.model})'
#
# car1 = Car('BMW', 'GT')
# print(car1)
# print(repr(car1))


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def __add__(self, other):
#         newbrand = self.brand +"-"+ other.brand
#         newmodel = self.model +"+"+ other.model
#         return Car(newbrand, newmodel)
#
#     def __str__(self):
#         return self.brand+", "+self.model
#
# car1 = Car("BMW", "x6")
# car2 = Car("Ford", "Mustang")
# add_car=car1 + car2
#
# print(add_car)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def __eq__(self, other):
#         return self.brand == other.brand and self.model == other.model
#
# car1 = Car("BMW", "x6")
# car2 = Car("Ford", "Mustang")
# car3 = Car("BMW", "x6")
# print(car1 == car2)
# print(car1 == car3)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def __len__(self):
#         return len(self.brand) +len(self.model)
#
# car1 = Car("BMW", "x6")
#
# print(len(car1))

# INHERITANCE
#
# class Vehicle:
#     def start(self):
#         print("Starting")
#
# class Car(Vehicle):
#     def drive(self):
#         print("Driving a car")
#
# class ElectricCar(Car):
#     def charge(self):
#         print("Charging electric car")
#
# tesla=ElectricCar()
# tesla.start()
# tesla.drive()
# tesla.charge()


# class Car:
#     def engine(self):
#         print("standard engine")
#
# class PetrolCar(Car):
#     def fuel_type(self):
#         print("Petrol")
#
# class DieselCar(Car):
#     def fuel_type(self):
#         print("Diesel")
#
# honda=PetrolCar()
# honda.engine()
# honda.fuel_type()
#
# ford=DieselCar()
# ford.engine()
# ford.fuel_type()

# Multiple

# class GPS:
#     def locate(self):
#         print("GPS is locating the location")
#
# class InfotainmentSystem:
#     def play_music(self):
#         print("Play Music")
#
# class Car(GPS, InfotainmentSystem):
#     def auto_drive(self):
#         print("Auto Drive is enabled")
#
# kia=Car()
# kia.locate()
# kia.play_music()
# kia.auto_drive()

# class Vehicle:
#     def start(self):
#         print("Vehicle started.")
#
#
# class Car(Vehicle):
#     def start(self):
#         print("Car preparing...")
#         super().start()
#
#
# class ElectricCar(Car):
#     def start(self):
#         print("Electric car initializing battery...")
#         super().start()
#
# tesla=ElectricCar()
# tesla.start()


# Nested Class

# class Car:
#     def __init__(self, brand):
#         self.brand=brand
#         self.engine=self.Engine()
#
#     def show(self):
#         print(self.brand)
#         self.engine.engine_specs()
#
#     class Engine:
#         def engine_specs(self):
#             print("this is a V8 powered engine")
#
# car1=Car("BMW")
# car1.show()


class Car:
    def __init__(self, brand):
        self.brand = brand
        print(f"the brand name is {self.brand}")

    def __del__(self):
        print(f"the brand name {self.brand} is deleted")

print("creating a car")
car = Car("Ford")
print("destroying the car")
# del car