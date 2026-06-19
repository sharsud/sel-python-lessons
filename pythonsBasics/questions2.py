"""

Questions:

    Q1: What is a for loop in Python, and how does it differ from a while loop?"""
from sys import implementation

for i in range(5):
    print(i)

count=0
while count<5:
    print(count)
    count+=1

"""
    Q2: How do you use the range() function in loops?"""

range(5) # 0,1,2,3,4
range(1,5) # 1,2,3,4
range(1,5,2)  #1,3

"""
    Q3: What is the else block used for in a Python loop?
"""
for i in range(5):
    print(i)
else:
    print("Loop completed")
"""
    Q4: How can you terminate a loop early in Python?
"""
for i in range(10):
    if i == 5:
        break
    print(i)
"""
    Q5: How do you skip iterations in a loop?
"""
for i in range(10):
    if i == 5:
        continue
    print(i) #0,1,2,3,4,6,7,8,9
"""
    Q6: Write a Python program to print the Fibonacci sequence using a loop. until 100
"""
#0, 1, 1, 2, 3, 5, 8, 13
n=10
a,b = 0,1
for _ in range(n):
    print(a, end=", ")
    a,b = b,a+b # 1,1 -> 1,2

"""
    Q7: What is an infinite loop, and how do you avoid it?
"""
#~break Stmt
#~conditional loop.
"""
    Q8: Can you nest loops in Python? Provide an example.
"""

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

"""
    Q9: What is the difference between continue and pass in a loop?
"""
for i in range(5):
    if i == 3:
        continue  # Skip the current iteration when i is 3
    print(i)

for i in range(5):
    if i == 3:
        pass  # Does nothing
    print(i)


"""
    Q10: Write a Python program to check whether a number is prime using a loop.
"""
# divisble by 1 or itself.
# loop from 2 until N and check if it is divisible by any number in the loop. use int(n/2)
#10 a,b = 2*5
num=29
is_prime=True
for i in range(2, int(num**0.5)+1):
    print (num, i)
    if num%i==0:
        is_prime=False
        break
if is_prime:
    print(f"The number: {num} is prime")
else:
    print(f"The number: {num} is not prime")
"""
    Q11: How do you define a function in Python?
"""
def greet(name):
    return f"Hello, {name}!"
greet("John")
"""
    Q12: What is the difference between return and print in a function?
"""
def greet(name):
    print( f"Hello, {name}!")
    return f"Hello, {name}!"
var=greet("John")
print(var)
"""
    Q13: Can a function return multiple values? Provide an example.
"""
def greet():
    return 1,2,3
a,b,c=greet()
"""
    Q14: What is recursion? Write a recursive function to calculate the factorial of a number.
"""

# n=5
# n!=5x4x3x2x1

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

"""
    Q15: What are default arguments in Python functions? Provide an example.
"""
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

"""
    Q16: Can you modify a list while iterating over it? What issues can arise? How would you solve them?
"""
# -Make a copy and aceess it
"""
    Q17: What are variable-length arguments (*args and **kwargs) in Python? Provide examples.
"""
def func_with_args(*args):
    for arg in args:
        print(arg)

func_with_args(1, 2, 3)  # Prints: 1 2 3

def func_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

func_with_kwargs(name="Alice", age=30)


"""
    Q18: Can functions be nested in Python? How do closures work in Python? Provide an example.

"""
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
cls_fn=outer_function(10)
print(cls_fn(5))

"""
    Q19: What are decorators in Python, and how can you use them to modify the behavior of a function?
"""
# implemented usin @
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("hello world")

greet()
"""
    Q20: Write a Python function to calculate the nth Fibonacci number using memoization (decorator or dictionary-based).
    
    Q21: Explain how function annotations work in Python. Write a function with annotations.

"""
def addnos(x, y):
    return x+y
def addno(x:int, y:int) -> int:
    return x+y
print(addnos(2,3))
print(addno(2,3))
