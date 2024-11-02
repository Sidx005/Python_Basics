# A set is a collection which is unorderedand unindexed.In python sets are within curly brackets.

myset = {"apple", "banana", "cherry"}
print(myset)

for i in myset:
    print(i)

if "apple" in myset:
    print(True)

print("banana1" in myset)  # False since "banana1" is not in the set

myset.add("kiwi")
print(myset)

myset.update(["apple", "grapes"])
print(myset)

myset.remove("apple")
print(myset)

myset.discard("kiwi")
# print(myset.discard("kiwi"))

print(myset)
# myset.remove("apple") Gives error
print(myset)




#Join sets

set1={'a','b','c'}
set2={'d','e','f'}

set3=set1.union(set2)
print(set3)
set4={1,2,3}
set1.update(set4)
print(set1)



