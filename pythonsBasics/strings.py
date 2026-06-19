#String data type ' "
# immutable

# #ord
#
# value=ord('a')
# print(value)
#
# #chr
#
# value=chr(97)
# print(value)

# # Upper and lower
#
# str1="Hello World"
# print(str1.upper())
# print(str1.lower())



# #split
#
# str1="Python is amazing"
# var1=str1.split()
# print(type(var1))
# print(var1)
#
# str2="id,name,address,phoneno"
# var2=str2.split(",")
# print(var2)


# #join
#
# list_words=['id', 'name', 'address', 'phoneno']
# sentence= ",".join(list_words)
# print(sentence)


#strip

# str= "        Hello   World     "
# print(str)
# print(str.strip())
#
# url="www.google.com"
# url1=url.strip("w.")
# print(url1)
#
# url="www.google.comwww."
# url1=url.strip("w.")
# print(url1)
#
# url="www.google.comwww.Www"
# url1=url.strip("w.")
# print(url1)


# #replace
# str="John is a good boy"
# new_str=str.replace("John","Smith")
# print(new_str)


# #find and index
#
# string1 = "Hello, i am at the code level indexing"
# print(string1.find("i"))
# print(string1.index("i"))
#
# print(string1.find("Z")) # -1 whn the str is not found
# print(string1.index("Z")) # throw me error saying substring not found

# #starts with and endswith
#
# str1="hello world"
# #true
# print(str1.startswith("hello"))
# print(str1.endswith("world"))
# #false
# print(str1.startswith("hello"))
# print(str1.endswith("world."))
#
#
# #SLICING
# # string[staring, ending+1, step]
str="Python is fun"
# print(str[0:6])
#
# #start
# print(str[:6])
#
# #end
# print(str[7:])
#
# #negetive indexing
# print(str[-3:])

# #Step
# str1="a1b2c3d4e5"
# print(str1[::2]) #all alphabets
# print(str1[1::2]) #all numbers

# string="ECHO"
# print(string[::-1])

#Chekcing for substr
#using in operator

# text="the world is a beautiful place"
#
# print("world" in text)
#
#
# #find
# index=text.find("world")
# if index!=-1:
#     print(f"World is in index: {index}")
#
# #count
# print(text.count("world"))
#
# #Regular expr or regex


# int() -> converts float to int
# # abs
# a=10
# b=-10
# print(abs(a), abs(b))
#
# #pow
# print(pow(2,3))

# # min(), max(), count(), sum(), round()
# #divmod
# quo, rem=divmod(10,3)
# print(quo)
# print(rem)

