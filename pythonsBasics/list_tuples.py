#lists
#ordered, changeable, dup vals.
# []
#
# list1=[1,2,3,4]
# list2=["a","b","c","d"]
# list3=["a", 2, 5.6, True]
#
# #access
# print(list1[0])
# print(list1[1])
# print(list1[2])
#
# print(list2[0])
# print(list2[1])
# print(list2[2])
import copy

# #len
# list1=[1,2,3,4]
# list2=["a","b","c","d"]
#
# len1=len(list1)
# print(len1)
# print(len(list2))
#
# #index
# list1=[1,2,3,4]
# list2=["a","b","c","d"]
#
# ind=list1.index(2)
# print(ind,list1[ind])
# ind2=list2.index("c")
# print(ind2,list2[ind2])

#modify elements & append
# list1=[1,2,3,4]
# list2=["a","b","c","d"]
# list1[1]=5
# print(list1)
# list2.append("e")
# print(list2)

#insert
# list1=[1,2,3,4]
# list2=["a","b","c","d"]
# list2.insert(1,"e")
# print(list2)

# #pop
# list1=[1,2,3,4]
# list2=["a","b","c","d"]
# list1.pop()
# print(list1)
# list2.pop(1)
# print(list2)

#sort
# list3=[1,6,2,8,4,9,3,2]
# list3.sort()
# print(list3)
# # list3.sort(reverse=True)
# # print(list3)
# list3.reverse()
# print(list3)
#
# #extend
# l1=[1,2,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)
# l1.extend([7,8,9])
# print(l1)

# #count
# l1=[1,6,2,8,4,9,3,2,6,6]
# count=l1.count(6)
# print(count)

# #clear
# l1=[1,6,2,8,4,9,3,2,6,6]
# l1.clear()
# print(l1)


#remove
# l1=[1,6,2,8,4,9,3,2,6,6]
# l1.remove(6)
# print(l1)

# #list()
# var1="name"
# var2=["name"]
# print(type(var1))
# print(type(var2))
# print(type(list(var1)))

#del
# list1=[1,2,3]
# del list1[1]
# print(list1)

# shallow vs deep copy

# orig_list = [[1, 2, 3], [4, 5, 6]]
# shallow_cpy= copy.copy(orig_list)
# deep_cpy= copy.deepcopy(orig_list)
#
# orig_list[0][0]="x"
# print(orig_list)
# print(shallow_cpy)
# print(deep_cpy)

# sq=[x**2 for x in range(6)]
# print(sq)
# print(type(sq))
#
# # TUPLES - ()
# # Immutable- cannot edit
#
# my_tuple=(1,2,3,4,5)
# print(my_tuple)
# print(type(my_tuple))

# #accessing
# my_tuple=(1,2,3,4,5)
# print(my_tuple[2])

# #length
# my_tuple=(1,2,3,4,5)
# print(len(my_tuple))

# #max & min & sum
# my_tuple=(1,2,3,4,5)
# maximum=max(my_tuple)
# minimum=min(my_tuple)
# sum=sum(my_tuple)
#
# print(f"maximum: {maximum}")
# print(f"minimum: {minimum}")
# print(f"sum: {sum}")

# #sorting -
# my_tuple=(4,51,2,3,40,0.5)
# sorted_tuple1=tuple(sorted(my_tuple))
# print(f"sorted_tuple: {sorted_tuple1}")
# sorted_tuple=sorted(my_tuple, reverse=True)
# print(f"sorted_tuple: {sorted_tuple}")
# print(type(sorted_tuple))
# print(type(sorted_tuple1))

# # Merging or concat
# my_tuple1=(1,2,3)
# my_tuple2=(4,5)
# my_tuple3=my_tuple1+my_tuple2
# print(f"merged tuple: {my_tuple3}")
# print(id(my_tuple3))
# print(id(my_tuple1))
# print(id(my_tuple2))

my_tuple = (1, 2, 3)
a,b,c = my_tuple
print(a,b,c)