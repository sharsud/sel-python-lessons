"""
1. How does string immutability affect string operations in Python?
    -String are immutable,
    -use  ''.join()


2. What is string interning, and how does it optimize memory usage?
    -uses the same obj rather than creating a new one when vals are same.
"""
# str1="abc"
# str2="abc"
# print(id(str1))
# print(id(str2))
"""

3. Explain how slicing works in Python strings. What does s[::-1] do?
    -Str[start:end:step]
"""
# str="ABCD"
# print(str[::-1]) #DCBA

"""

4. What are f-strings in Python? How are they better than % or .format()?
    -faster because it is evaluated at compile time rather than interpreted
    -readble when using f string

5. How can you check if a string is a palindrome in Python?
"""
# # str="level"
# # str="MADAM"
# str="12345654321"
# def is_palin(s):
#     return s==s[::-1]
# print(is_palin(str))

"""

6. What are some common built-in string methods used for validation (like checking if it's a digit, alphabet, etc.)?
"""
# str="1stwinner"
# print(str.isdigit())
# print(str.isalpha())
# print(str.isalnum())
# print(str.islower())
# print(str.isupper())
# print(str.isspace())
"""

7. What are the different file modes in Python's open() function?
Refer ppt, a, r, w, b & we can club 2 types using + operator


8. What is the difference between read(), readline(), and readlines()?
"""
# file=open("my_file1.txt")
# print(file.read()+ "\n-----------------------------")
# file.seek(0)
# print(file.readline()+"\n------------------------------")
# file.seek(0)
# print(file.readlines())
"""



9. How do you ensure a file is properly closed after reading/writing, even if an error occurs?
10. What is the advantage of using a with statement when working with files?
"""
# with open("my_file.txt") as f:
#     f.read()
"""

11. How would you read a large file line by line without loading it entirely into memory?"""
# first approach
# with open("my_file.txt") as f:
#     for line in f:
#         print(f)
#
# #alternate approach
# file=open("my_file.txt")
# line=file.readline()
# while line:
#     print(line)
#     line=file.readline()
"""
12. How can you append text to an existing file without overwriting it?
    --open it in apprnd mode using "a" instead of "w"
13. What is the difference between syntax errors and exceptions in Python?
    --syntax error: if we write a code in an incorret way, caught before execution
    __exception: occur during runtime.
    

14. Explain the purpose of the else block in a try-except-else-finally construct.
    -else: runs only when there was no exception raised
    
15. What’s the difference between catching a general Exception vs. a specific one like ValueError?
    -except e
        print ("Exception occured")
    except ValueError:
        print ("ValueError occured")

16. How do you raise a custom exception in Python? Provide an example.
"""
# class MyException(Exception):
#     pass
# try:
#     print("")
#     raise MyException("something is fishy.")
# except MyException as e:
#     print(e)


"""

17. What does the finally block do, and when is it executed?
 -last block of code executed for step down. usually for closing files and db connections
18. What is exception chaining in Python and how can it be useful?
"""
# try:
#     int("ABC")
# except ValueError as e:
#     raise RuntimeError("failed to convert") from e


"""
19. Explain how contextlib.suppress() works. When would you use it?

"""

from contextlib import suppress
with suppress(FileNotFoundError):
    open("nofile.txt")