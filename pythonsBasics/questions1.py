"""
Questions:


	1. How does Python manage memory for variables? Reference counting, Garbage collection
	2. What is a mutable and immutable object in Python? immutable obj- int string tuple || mutable: list dict set
	3. Explain the use of is and == operators. How do they differ?
	        == :compared values
	        is  : obj identity
	4. Swap variable
	5. Why is there no switch-case statement in Python? if elif else, dict+func to simulate a switch case
	6. What are the main reasons Python is so popular compared to other programming languages?
	    readiblity || libraries || cross-platform || versatility
	7. Explain how to run a Python script using the terminal. What command would you use to run a file named example.py?
	    python example.py || python3 example.py
	8. What are the different data types in Python, and how does Python handle type conversion?
	    int || string ||boolean || float || none || collection(list, set, dictionary, tuple)
	    a=3 b=7 c=b/a -> implicity change dta type to float
	    d=int(input("Enter a val")
	9. What does the input() function do in Python, and how does it store the user's input?
	    d=int(input("Enter a val") || by defaulyt it stores as string data type
	10. How do you perform basic arithmetic operations in Python, and how is division (/) different from integer division (//)?
	    / -> float || 9/2=4.5
	    // -> int  || 9//2=4 -> automatically perform floor operation and return an int value
	11. What is the difference between + for numbers and + for strings?
	    int- + is addition
	    str- + is concatenation
	12. Explain the difference between relational operators and logical operators in Python.
	    relation(==, !=, < > <= >=) -compare values - return boolean
	    logical(and, or, not) -combine multiple conditions.
	13. What is the result of evaluating the following expression: True and False? Why?
	    False => bcz of and operation
    14. How would you write an if-else block to check if a number is positive, negative, or zero?
"""

#1
# x=10 # mem alloc
# y=x #x& y have same ref
# del x #ref of 10
# print(y)

#3
# a=[1,2,3]
# b=[1,2,3]
#
# print(a==b) #true
# print(a is b) #false

#4
# a=3
# b=5
# print(f"values before swap {a} and {b}")
# temp=a #temp=3 a=3
# a=b #a=5 temp=3 b=5
# b=temp #b=3
# print(a,b)

# a=3
# b=5
# print(f"values before swap {a} and {b}")
# b,a=a,b
# print(f"values after swap {a} and {b}")

# 14
# n1=int(input("Value to be checked"))
# if n1>0:
#     print("Positive")
# elif n1<0:
#     print("Negative")
# else:
#     print("Zero")

# Floating point precision

# x=1.1
# y=2.2
# total 3.3
# x=1.1+2.2
# print(x==3.3) #false
# print(x)

# # * in string and int
# a="2" * 3 #222  if it was a instead of 2 the op would be aaa
# op1=int(a)+2 #224
# print(op1)
#
# x=""
# if x:
#     print("true")
# else:
#     print("false") #false -> empty variables are considered as false in py
