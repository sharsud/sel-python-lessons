# #Set- Mutable, unordered
#
# # my_set={1,2,3,4,5}
# # print(my_set)
#
# myset=set([1,2,3,4,4,5,3,3,1,6])
# print(myset)
#
# #add values
# myset.add(7)
# print(myset)
# #Remove
# # myset.remove(7)
# # print(myset)
# # myset.discard(7)
# # print(myset)
# #
#
# # POP
# ele=myset.pop()
# print(ele)
# print(myset)
#
# #clear
# myset.clear()
# print(myset)

# #mathematical operations
# set1={1,2,3}
# set2={3,4,5}
# #union
# union_set=set1.union(set2)
# print(union_set)
#
# #intersection
# intersection_set=set1.intersection(set2)
# print(intersection_set)
#
# #difference
# diff_set=set1.difference(set2)
# print(diff_set)
#
# #sym diff
# sym_set=set1.symmetric_difference(set2)
# print(sym_set)
#
# setA={1,2,3}
# setB={1,2,3,4,5,6,7,8,9}
#
# #issubset
# print(setA.issubset(setB))
#
# #isupperset
# print(setB.issuperset(setA))
# print(setA.issuperset(setB))
#
# #isdisjoint
# setC={10,11,12}
# print(setC.isdisjoint(setA))
#
# set_copy=setA.copy()
# print(set_copy)

#Iteration
setB={1,2,3,4,5,6,7,8,9}
for item in setB:
    print(item)