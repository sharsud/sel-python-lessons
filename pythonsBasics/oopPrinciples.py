# Encapsulation
#abstraction
#inheritance
#polymorphism

# public, private ad Protected
#
# class Car:
#     def __init__(self):
#         self.brand = "Toyota" #public
#         self._engine_status= "OFF" #protected
#         self.__sl_id= "856AA21" #private
#
#     def set_engine_status(self, status):
#         self._engine_status = status
#
#     def get_engine_status(self):
#         return self._engine_status
#
#     def set_sl_id(self, sl_id):
#         if isinstance(sl_id, str) and len(sl_id) == 7:
#             self.__sl_id = sl_id
#         else:
#             print("Invalid sl_id")
#
#     def get_sl_id(self):
#         return self.__sl_id
#
# car=Car()
# print(car.get_engine_status())
# car.set_engine_status("ON")
# print(car.get_engine_status())
# car.set_sl_id("TestData")
# print(car.get_sl_id())
# print(car.brand)
# print(car._engine_status)
# print(car._Car__sl_id) #name mangling
# print(car.get_sl_id())

#ABSTRACTION
#ABC -ABStract Base Class Module
#
# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     @abstractmethod
#     def accelerate(self):
#         pass
#     @abstractmethod
#     def decelerate(self):
#         pass
#
# class ElecCar(Car):
#     def __init__(self, brand):
#         self.brand = brand
#         self.speed=0
#     def accelerate(self):
#         self.speed+=5
#         print(f"the car of brand: {self.brand} accelerated by speed: {self.speed}")
#
#     def decelerate(self):
#         self.speed= max(0,self.speed-5)
#         print(f"the car of brand: {self.brand} decelerated by speed: {self.speed}")
#
# kia=ElecCar('KIA')
# kia.accelerate()
# kia.accelerate()
# kia.decelerate()
# kia.decelerate()
# kia.decelerate()
# kia.decelerate()

# car=Car()
# car.accelerate()

#inheritance.
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#     def start(self):
#         print(f"the car : {self.brand} is starting")
#
# class ElecCar(Car):
#     pass
#
# tesla = ElecCar('Tesla')
# tesla.start()

#super KEYWORD
#
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#     def start(self):
#         print(f"the car : {self.brand} is starting")
#
# class ElecCar(Car):
#     def __init__(self, brand, battery_level):
#         super().__init__(brand)
#         self.battery_level = battery_level
#     def charge(self):
#         print(f"the car : {self.brand} is charging at {self.battery_level}%")
#
# tesla = ElecCar('Tesla', 80)
# tesla.charge()

# #MRO
# class Petrolcar:
#     def start(self):
#         print("petrol car is starting")
#
# class ToyCar(Petrolcar):
#     pass
#
# print(ToyCar.mro())
# # [<class '__main__.ToyCar'>, <class '__main__.Petrolcar'>, <class 'object'>]

#polymporphism
 #basic overriding

# class Car:
#     def Start(self):
#         print("Starting with key")
# class ElecCar(Car):
#     def Start(self):
#         print("Starting silently with push buttons")
#
# tesla=ElecCar()
# tesla.Start()

#self
# class car:
#     def __init__(self,brand):
#         self.brand = brand
#     def describe(self):
#         print(f"this is brand {self.brand}")
#
# mycar1 = car("Ford")
# mycar1.describe()
# mycar2 = car("Volkswagen")
# mycar2.describe()

#duck typing

# class PetrolCar:
#     def start(self):
#         print("Petrol car is starting...the engine revs")
#
# class ToyCar():
#     def start(self):
#         print("Toy car is starting...in imagination")
#
# class Bicycle():
#     def pedal(self):
#         print("Pedaling the bicycle.... ")
#
#
# def start_the_engine(car):
#     car.start()
#
# start_the_engine(PetrolCar())
# start_the_engine(ToyCar())
# start_the_engine(Bicycle())

#Overloading

"""
add(n1,n2):
tot=n1+n2

add(n1,n2,n3):
tot=n1+n2+n3
"""
# class Car:
#     def drivemode(self, *args):
#         if len(args)==0:
#             print("Driving in default mode")
#         elif len(args)==1:
#             print(f"Driving at the speed of {args[0]}km/h")
#         elif len(args)==2:
#             print(f"Driving at the speed of {args[0]}km/h and in {args[1]} mode")
#
# car=Car()
# car.drivemode()
# car.drivemode(60)
# car.drivemode(60,"Sports")