# what is oop

# storing data and functions in a class and accessing it using the objects
# benefit:
# Reusable
# Modularity
# DRY-Dont Repeat Yourself-


# classes and object
# class Car:
#     pass
# #creating object
# car1 = Car()
# print(type(car1))

#constructors
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
# #creating object
# car1 = Car("BMW","White") #->add the atrributes to my class object.
# print(car1.color)
# print(car1.brand)


# intance attribute (variables)
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
# #creating object
# car1 = Car("BMW","White")
# print(car1.color)
# print(car1.brand)
#
# car2 = Car("BMW","Red")
# print(car2.color)
# print(car2.brand)
# car2.brand="KIA"
# print(car2.brand)


# # class attribute
# class Car:
#     brand="PsudoMotors"
#
# # one way
# car1=Car()
# print(car1.brand)
#
# # second way
# print(Car.brand)

#when to use a class attribute
#     the values are shared across all the object instance.
#         eg: company name, version, warranty period


# instance method (functions inside class)
# class Car:
#     def __init__(self, brand, color, speed=0):
#         self.brand = brand
#         self.color = color
#         self.speed = speed
#
#     def accelerate(self, amount):
#         self.speed +=amount
#         print(f"{self.brand} of color {self.color} accelerated with speed: {self.speed}")
#
#     def brake(self):
#         self.speed=0
#         print(f"{self.brand} of color {self.color} has stopped")
#
# car1= Car("Tesla", "blue")
# car1.accelerate(60)
# car1.brake()

# class methods
# class Car:
#     car_count=0
#     def __init__(self,brand, color):
#         self.brand = brand
#         self.color = color
#         Car.car_count+=1
#     @classmethod
#     def totalCars(cls):
#         print("Total number of cars: ",cls.car_count)
#
# car1=Car("BMW","red")
# car2=Car("BMW","blue")
# car3=Car("BMW","yellow")
# Car.totalCars()

#when do we use class methods?
#to modify or access class level data
#no specific object ref, just belonging to class


# staticmethod
class Car:

    @staticmethod
    def has_number(vehicle_number):
        return vehicle_number.isalnum() and len(vehicle_number) == 6

    car_count=0
    def __init__(self,brand, color):
        self.brand = brand
        self.color = color
        Car.car_count+=1
    @classmethod
    def totalCars(cls):
        print("Total number of cars: ",cls.car_count)

car1=Car("BMW","red")
car2=Car("BMW","blue")
car3=Car("BMW","yellow")
Car.totalCars()

print(Car.has_number("Abc123"))

#when to use static functions?
#grouped inside the class
#no self or cls is used
#these are helper functions, not tied to obj or class state.

