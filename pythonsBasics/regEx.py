import re
# str="the rain is raining in the sun"
# print(re.search("rain", str))
# # match will only search from the beginning
# print(re.match("the", str))
#
# print(re.findall("rain", str))


# str="the rain is raining in the sun"
# match=re.search("raining",str)
#
# if match:
#     print("match found!")
#     print("start postion: " , match.start())
#     print("end postion: " , match.end())
#     print("span: " , match.span())
# else:
#     print("no match found")

#
# # meta characters
# # >> . - only once character
# str="acb"
# print(re.match("a.b",str))
# str="adb"
# print(re.match("a.b",str))
# str="accb"
# print(re.match("a.b",str))

# # >> ^ -matches the start of the str
# str="Hello World"
# print(re.match("^Hello",str))
# str="HelloWorld"
# print(re.match("^Hello",str))
# str=" Hello World"
# print(re.match("^Hello",str))

# # >> $ Mtaches the end of the str
# str="Hello World"
# print(re.search("World$",str))
# str="Good bye World"
# print(re.search("World$",str))
# str="Worldwide"
# print(re.search("World$",str))
#
# # >> * matches one or more occurance of prev str.
# str="google"
# print(re.search("go*gle",str))
# str="gooooooooooooooooooooooogle"
# print(re.search("go*gle",str))
# str="ggle"
# print(re.search("go*gle",str))
#
# # >> + match one or more  preceding char
#
# str="google"
# print(re.search("go+gle",str))
# str="ggle"
# print(re.search("go+gle",str))
#
# # >> ? to match zero or one preceding char
#
# str="google"
# print(re.search("go?gle",str))
# str="gogle"
# print(re.search("go?gle",str))
#
# str="colour"
# print(re.search("colou?r",str))
# str="color"
# print(re.search("colou?r",str))


# print(re.findall(r"[aeiou]", "alphabets"))
#
# # \d -matches the string for numbers
# result=re.findall(r'\d+','abc123')
# print(result)
#
# str="the item number 11 costs 44$"
# for item in re.finditer(r'\d+',str):
#     print(item.group(), "at index", item.span())

# #\w matches the word char +number + _
# result=re.findall(r'\w+','abc_123!!')
# print(result)

# # cat --> cat not catalog
# # \b for defining boundaries
# result=re.findall(r'\bcat\b','the cat is not in catalog')
# print(result)
#  # saerch \\
# result=re.findall(r'\\','this is a backslash: \\')
# print(result)

#Grouping
# date="Date= 2025-05-13"
# result=re.search(r"(\d{4})-(\d{2})-(\d{2})",date)
# print(result)
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.groups())

# #nameing
# date="2025-05-13"
# pattern=r"(?P<Year>\d{4})-(?P<Month>\d{2})-(?P<day>\d{2})"
# match=re.match(pattern,date)
# print(match.group("Year"))
# print(match.group("Month"))
# print(match.group("day"))

# #replace we have .sub()
# text= "the sky is pink"
# print(re.sub(r"pink", "blue", text))

#greedy vs non greedy
text = "<p>Hello</p><p>World</p>"
print(re.findall(r"<p>.*</p>", text)) # greedy
print(re.findall(r"<p>.*?</p>", text)) 
