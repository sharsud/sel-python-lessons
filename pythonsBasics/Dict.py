#Dictionaries

#KEY : value

#creation
# my_dict={
#     "name": "Alice",
#     "age": 25,
#     "city": "Bangalore"
# }
#
# print(my_dict)
#
# #accessing
# print(my_dict["name"])

#addition/updation of values

# my_dict["salary"]=50000
# print(my_dict)
#
# my_dict["salary"]=70000
# print(my_dict)
#
# #deletion
# del my_dict["salary"]
# print(my_dict)

# val=my_dict.pop("salary")
# print(val)
# print(my_dict)

#iteration
#
# my_dict={
#     "name": "Alice",
#     "age": 25,
#     "city": "Bangalore"
# }
#
# print(my_dict)
#
# # Key, Value, items
# # for key in my_dict.keys():
# #     print(key)
# #
# # for value in my_dict.values():
# #     print(value)
#
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

#Methods

# my_dict={
#     "name": "Alice",
#     "age": 25,
#     "city": "Bangalore"
# }
# print(my_dict)
# #clear
# my_dict.clear()
# print(my_dict)

# #copy
# new_dict=my_dict.copy()
# print(new_dict)

# #  update
# my_dict.update({"salary":50000})
# print(my_dict)
#
# dict2={"height":170, "Company": "XYZ"}
# my_dict.update(dict2)
# print(my_dict)

# # fromKeys
# keys=["name", "age", "city"]
# mew_dict=dict.fromkeys(keys,"Unknown")
# print(mew_dict)
# print(mew_dict["name"])

#setdefault
# my_dict={
#     "name": "Alice",
#     "age": 25,
#     "city": "Bangalore"
# }
# print(my_dict)
# sal=my_dict.setdefault("salary",10000)
# print(sal)
# print(my_dict)

# my_dict={
#     "name": "Alice",
#     "age": 25,
#     "city": "Bangalore",
#     "salary": 50000
# }
# print(my_dict)
# sal=my_dict.setdefault("salary",10000)
# print(sal)
# print(my_dict)

# creation
my_dict={
    "name": "Alice",
    "age": 25,
    "city": "Bangalore"
}

print(my_dict)

#accessing
print(my_dict.get("names","Not found"))