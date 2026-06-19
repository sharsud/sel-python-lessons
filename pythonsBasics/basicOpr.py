#+-*/

# mod // **

# a=20
# b=10
# sum=a+b
# print(sum)

# diff=a-b
# print(diff)
#
#
# diff=b-a
# print(diff)

# mult=a*b
# print(mult)
#
# div=a/b
# print(div)
# print(type(div))

# a=2
# b=3
# exp=a**b
# print(exp)

# a=100
# b=10
# mod=a%b
# print(mod)
#
# a=102
# b=10
# mod=a%b
# print(mod)

# #/ vs //
# a=10
# b=3
# div=a/b
# print(div)
#
# a=10
# b=3
# div=a//b  #3
# print(div)

#+
# a="10"
# b="3"
# sum=a+b
# print(sum)
#
# input1="Test"
# input2="Automation"
# print(input1+input2)
#

# inp1=input("Enter your name: ")
# print("Hello "+inp1)

# inp1=input("Enter your First name: ")
# inp2=input("Enter your Last name: ")
# print("Hello "+inp1+" "+inp2)

#input text: John K
# inp1, inp2=input("Enter your Full name: ").split()
# print("Hello "+inp1+" "+inp2)

# inp1=input()
# print(inp1)

# int as input
# age=input("Enter your age: ")
# sal=input("Enter your salary: ")
# tax=input("Enter your tax: ")
# print(age)
# print("Gross Salary: "+sal+tax)


# age=int(input("Enter your age: "))
# sal=float(input("Enter your salary: "))
# tax=float(input("Enter your tax: "))
# print("Age :",age)
# print("Gross Salary: ", sal+tax)

# formatting the Print statement
#.format concept
# name="John"
# age=20
# salary=10000.99
# print("Name: {}, Age: {}, Salary: {}".format(name,age,salary))

# #Print using %
# name="John"
# age=20
# salary=10000.45
# print("Name: %s, Age: %d, Salary: %g"%(name,age,salary))

#%g -> gives you fixed point notations for medium values 1.123
    #  Exponential Notations for very lrge or very small values eg 1.2e+23
    #   rounds of  the vales to default of 6 digit

#%f -> Fixed decimal points
# %e -> Expon notations

# a=0.123456789
# print("%g"%a) #0.123457
# a=12.563
# print("%g"%a) #12.563
# a=0.12345678936
# print("%.5g"%a) #0.12346
# a=12.563
# print("%.2g"%a) #13
# a=12.563
# print("%.4g"%a) #12.56
# a=0.0000000063
# print("%g"%a)  #exponential notation
# a=0.99999999999
# print("%g"%a)   #1

# a=0.0000000063
# print("%f"%a) #0.000000
# print("%e"%a)


# a=0.0000000063
# print("%.10f"%a) #0.000000

#f-string (formatted string literals)

# name="John"
# age=20
# salary=10000.99
# print(f"Name: {name}, Age: {age}, Salary: {salary}")
# #Name: John, Age: 20, Salary: 10000.99

# name="John"
# age=20
# salary=10000.99999999
# print(f"Name: {name}, Age: {age}, Salary: {salary}")
# # Name: John, Age: 20, Salary: 10000.99999999

# a=10
# b=5
# print(f"sum of {a} & {b} is: {a+b}")
# # sum of 10 & 5 is: 15


# del keyword.
# a=10
# print(id(a))
# del a
# print(id(a))

import pk1.mod1

