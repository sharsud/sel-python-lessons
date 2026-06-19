
#def
#
# def funct_1():
#     print("Hello")
#
# funct_1()
#
# def funct_1():
#     print("Hello World")
#
# funct_1()

# def greet(name):
#     print("Hello " + name)
#
# greet("John")
# greet("")
# greet() #this resulted in error missing positional args.

#Positional and Keyword arguments

# def addition(a , b):
#     return a+b
#
# result=addition(10,20)
# print(result)

# def addition(a , b):
#     return a+b
#
# result=addition(b=10,a=20)
# print(result)

# def greet(name="Guest"):
#     print("Hello " + name)
#
# greet()
# greet("John")

#return values
# def square(num):
#     return num*num
# res=square(5)
# print(res)

# def get_name_and_age():
#     name="Psudo"
#     age="25"
#     return name, age
#
# na, age= get_name_and_age()
# print(f"Name is {na} and age is {age}")

#scope of variable

# def get_name_and_age():
#     name="Psudo"
#     age="25"
#     return name, age
#
# na, age= get_name_and_age()
# print(f"Name is {na} and age is {age}")
# print(f"name is {name}")

#Global variable
# name="Psudo"
# def get_name_and_age():
#     age="25"
#     return name, age
#
# na, age= get_name_and_age()
# print(f"Name is {na} and age is {age}")
# print(f"name is {name}")

#
# counter=0
# def increment():
#     global counter
#     counter+=1
#     return counter
# increment()
# print(counter)
# increment()
# print(counter)
# increment()
# print(counter)
# increment()
# print(counter)

#*args & **kwargs
# def sum_all(*args): #flexible function signature
#     return sum(args)
# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(2.5,3.5,0.5))

# def print_all(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# print_all(name="John",age=25)
# print_all(name="John",age=25,city="New York")

#lambda functions

# def square(num):
#     return num*num
# res=square(5)
# print(res)
#
# res=lambda num:num*num
# print(res(5))

# x=lambda a,b:a*b
# print(x(5,6))

def myFunc(n):
    return lambda a : a*n

double=myFunc(2)    # a*2
triple=myFunc(3)    # a*3

print(double(11))
print(triple(11))