#IF
#if else
#elif
#nesting
#ternary operator

# age=18
# if age>18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# score=75
# if score>=90:
#     print("your grade is A")
# elif score>=80:
#     print("your grade is B")
# elif score>=70:
#     print("your grade is C")
# else:
#     print("you have not qualified")
#
# a=2
# b=10
# if a<b:
#     pass
# else:
#     print("hello world")

# if 0:
#     print("this is not printed")
# if 1:
#     print("this is 1 and printed")
# if 1.0:
#     print("this is 1.0 and printed")
# if True:
#     print("this is true")
# if False:
#     print("this is false")
#


##relational operators
#==, <=, >=, <,>,!=
# score=10
# if score != 100:
#     print("score is",score)
# else:
#     print("the else score is",score)

#
# score=100
# if score == 100:
#     print("score is",score)
# else:
#     print("the else score is",score)


#Logical operators
# and, or, not
# age=25
# has_licence=True
#
# if age>=18 and has_licence:
#     print("you are eligible to drive")
# else:
#     print("you are not eligible to drive")

#or
# age=16
# has_car=False
# if age>=18 or has_car:  #true or False
#     print("you can rent a car")
# else:
#     print("you cant rent a car")

#Not
# raining=False
# if not raining: # raining=false + Not(reverse the condition) = True
#     print("You not need an umbrella") #true stmt

# #nested if
# age=20
# has_permission=True
# if age>=18:
#     if has_permission:
#         print("You can enter the club")
#     else:
#         print("You are not allowed to enter the club")
# else:
#     print("your age is too young")
# #You can enter the club
#
# age=20
# has_permission=False
# if age>=18:
#     if has_permission:
#         print("You can enter the club")
#     else:
#         print("You are not allowed to enter the club")
# else:
#     print("your age is too young")
# # You are not allowed to enter the club
# age=17
# has_permission=True
# # if age>=18:
# #     if has_permission:
# #         print("You can enter the club")
# #     else:
# #         print("You are not allowed to enter the club")
# # else:
# #     print("your age is too young")
# # #our age is too young
#
# marks=60
# if marks>=50:
#     if marks>=75:
#         print("Distinction")
#     else:
#         print("You have passed")
# else:
#     print("Fail")
#
# marks=80
# if marks>=50:
#     if marks>=75:
#         print("Distinction")
#     else:
#         print("You have passed")
# else:
#     print("Fail")
#
# marks=30
# if marks>=50:
#     if marks>=75:
#         print("Distinction")
#     else:
#         print("You have passed")
# else:
#     print("Fail")
#
#short circuit evaluation
# x=10
# y=0
# if x!=10 and (x/y)>5:
#     print("this is the message i am expecting")
# else:
#     print("this is the message i am not expecting")
#
# # Multiple comparison:
# x=10
# if x>=5 and x<=20:
#     print("x is between 5 and 20")
# if 5<x<20:
#     print("x is between 5 and 20")
#
# #Ternary operators or conditional expr

# age=18
# if age>=18:
#     print("you can vote")
# else:
#     print("you cant vote")
#
# # 2nd approach using ternary oerations
# print("you can vote") if age>=18 else print("you cant vote")

age=16
if age>=18:
    print("you can vote and drive")
elif age>=16:
    print("you cant vote but you can drive")
else:
    print("you cant vote and cant drive")

print("you can vote and drive") if age>=18 else print("you cant vote but you can drive") if age>=16 else print("you cant vote and cant drive")


#Comments and questions
