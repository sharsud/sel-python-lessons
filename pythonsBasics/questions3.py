"""
1. What is the difference between a list and a tuple in Python?
 #mutable and immutable
 created
 usages

2. How do you create an empty list and an empty dictionary?

    list=[]
    dictionary={}

3. Can you modify a tuple after it's created? Why or why not?
    No, if modified a new instance is created.

4. How do you add an element to a list? Give an example. """
# my_list=[1,2,3]
# my_list.append(4)
# print(my_list)

"""
5. How can you iterate through a dictionary and print its keys and values?
"""
# mydict={'a':1,'b':2,'c':3}
# for key, value in mydict.items():
#     print(f"Key : {key}, value : {value}")

"""
6. How do you merge two dictionaries in Python 3.9+?
"""
# #  keyword is |
# mydict1={'a':1,'b':2,'c':3}
# mydict2={'d':1,'e':2,'f':3}
# mergeddict=mydict1|mydict2
# print(mergeddict)
"""

7. What will be the output of the following?"""

# x = [1, 2, 3]
# y = x
# z=x.copy()
# y.append(4)
# z.append(5)
# print(x)
# print(z)


"""
8. Explain how list comprehension works. Give an example to filter even numbers from a list. """
#list comprehension is a compact way to create a list.

# numbers = [1, 2, 3, 4, 5]
# evenNumbers = [x for x in numbers if x % 2 ==0]
# print(evenNumbers)



"""
9. How would you convert a list of tuples into a dictionary?
[('a', 1), ('b', 2)] → {'a': 1, 'b': 2}"""
# dictionary=dict([('a', 1), ('b', 2)])
# print(dictionary)
# print(type(dictionary))

"""

10. What is the difference between dict.items() and dict.values()?

11. How do you remove duplicates from a list while maintaining order?
"""
# def remove_duplicates(lst):
#     new_list=[]
#     for item in lst:
#         if item not in new_list:
#             new_list.append(item)
#     return new_list
#
# lst1=[1,3,4,5,6,4,7,7,6,9,2,2]
# print(remove_duplicates(lst1))

"""
12. What’s the output of the following and why?"""
# a = (1, 2, [3, 4])
# print(id(a))
# a[2].append(5)
# print(id(a))
# print(a)
"""
13. Can a dictionary key be a list? Why or why not? No, Keys can only be immutable type i.e. String, Number, tuples
14. What is the difference between is and == when comparing lists?
"""
# a=[1,2]
# b=[1,2]
# print(a==b) #checks for value equality
# print(a is b) # checks for identity i.e. ID comparison


"""
15. Write a function to count the frequency of elements in a list and return a dictionary."""
list1=['a','b','c','b','b','a']
frequency={}
for item in list1:
    frequency[item] = frequency.get(item, 0) + 1 #freq={a:2, b:3, c:1 }
print(frequency)
"""
16. Explain how Python’s dictionary works internally (hashing, collision resolution).
ANS:

#hashtables: uses a hash function- key value to store - retrival is fast
[0,1,2,3,4]

apple->hashfn->2
[0][1][2:'apple',10][3][4]
[0: ("date", 5)] [1: ("banana", 20)] [2: ("apple", 10)] [3] [4: ("cherry", 30)]

#chaining- where we store multiple values in the same index typically using linked list

[0: ("date", 5)]    [1: ("banana", 20)]    [2: ("apple", 10) → ("grape", 15)]    [3]    [4: ("cherry", 30)]


"""