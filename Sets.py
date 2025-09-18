# Python set is an unordered collection of multiple items having different datatypes
# They are mutable,indexed, do no contain duplicates
# Main advantages of using set is faster mathematical calculation ->  Union Intersection and Difference
# Major disadvantages of using set is -> they do not support indexing and slicing and also difficult of accessing elements in unordered set
set1 = {1,2,3,4}
# set() is a built-in function that creates a set in Python
print(set("GeeksForGeeks"))
tup = (1,2,3,4)
print(set(tup))
dict1 = {'a':1,'b':2}
print(set(dict1)) # only keys are considered while creating a set from a dictionary  like the values are ignored
# Sets do not support indexing. Trying to access an element by index (set[0]) raises a TypeError.
# print(set1[1]) # TypeError: 'set' object is not subscriptable
# add -> used to add a single element to the set
# update -> used to add multiple elements to the set
set1.add(5) 
set1.update([6,7,8]) 
print(set1)
for i in set1: # used for accessing the elements of the set
    print(i,end=" ")
# Only diff between remove and discard is -> if the element to be removed is not present in the set then remove throws an error whereas discard does not throw any error
# print(set1.remove(8)) , print(set1.discard(8))
set1.remove(8)
set1.discard(7)
# Pop() function fo the set only works when the set is in ordered form or-else it throws an error
print(set1.pop()) # removes and returns an arbitrary element from the set
# set1.clear() # removes all the elements from the set
# A frozenset in Python -> built-in data type that is similar to a set but with one key difference that is immutability.
# which means that we can't add,modify or remove elements from a frozenset after its creation.if added it throws an error
set3 = frozenset([1,2,3,4]) # ultimately immutable set and all fixed elements
print(set3)

# --------------Sets Practice Programs-----------------
# wap in python to find that accepts complete vowels in the string using set
s = "Umberella"
v = set("aeiouAEIOU")
if all((i in v) for i in s):
    print("Accepted")
else:
    print("Not Accepted")

# wap to find the common elements in two lists using set
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = set([i for i in list1 if i in list2]) # using the list comprehension
set1 = set(list1)
set2 = set(list2)
# res = {x for x in list1 if x in list2 and x in list3} # using the list comprehension can also be used for finding the common elements in three lists
res = set1.intersection(set2,set3)
print(f"The common elements in the two lists are : {res}")

# wap in python to find whether a string is heterogram or not using set
s = "GeeksforGeeks"
s = s.lower()
if len(set(s)) == len(s):
    print("Yes it's a Heterogram")
else:
    print("Not a Heterogram")

# wap to find the Python Set difference to find lost element from a duplicated array
list1 = [1,2,3,4,5,6]
list2 = [4,5,6]
set1 = set(list1)
set2 = set(list2)
res = set1.difference(set2)
print(f"The lost elements from the duplicated array are : {res}")

# wap in python to find the one least element common in two lists using set
list1 = set([1,2,3,4,5]) 
list2 = set([4,5,6,7,8])
common = list1.intersection(list2)
if any(i in list2 for i in list1):
    print(f"The least common element in the two lists is : {common}")
else:
    print("No common elements")

# Python set is an unordered collection of multiple items having different datatypes
# They are mutable,indexed, do no contain duplicates
# Main advantages of using set is faster mathematical calculation ->  Union Intersection and Difference
# Major disadvantages of using set is -> they do not support indexing and slicing and also difficult of accessing elements in unordered set
set1 = {1,2,3,4}
# set() is a built-in function that creates a set in Python
print(set("GeeksForGeeks"))
tup = (1,2,3,4)
print(set(tup))
dict1 = {'a':1,'b':2}
print(set(dict1)) # only keys are considered while creating a set from a dictionary  like the values are ignored
# Sets do not support indexing. Trying to access an element by index (set[0]) raises a TypeError.
# print(set1[1]) # TypeError: 'set' object is not subscriptable
# add -> used to add a single element to the set
# update -> used to add multiple elements to the set
set1.add(5) 
set1.update([6,7,8]) 
print(set1)
for i in set1: # used for accessing the elements of the set
    print(i,end=" ")
# Only diff between remove and discard is -> if the element to be removed is not present in the set then remove throws an error whereas discard does not throw any error
# print(set1.remove(8)) , print(set1.discard(8))
set1.remove(8)
set1.discard(7)
# Pop() function fo the set only works when the set is in ordered form or-else it throws an error
print(set1.pop()) # removes and returns an arbitrary element from the set
# set1.clear() # removes all the elements from the set
# A frozenset in Python -> built-in data type that is similar to a set but with one key difference that is immutability.
# which means that we can't add,modify or remove elements from a frozenset after its creation.if added it throws an error
set3 = frozenset([1,2,3,4]) # ultimately immutable set and all fixed elements
print(set3)

# --------------Sets Practice Programs-----------------
# wap in python to find that accepts complete vowels in the string using set
s = "Umberella"
v = set("aeiouAEIOU")
if all((i in v) for i in s):
    print("Accepted")
else:
    print("Not Accepted")

# wap to find the common elements in two lists using set
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = set([i for i in list1 if i in list2]) # using the list comprehension
set1 = set(list1)
set2 = set(list2)
# res = {x for x in list1 if x in list2 and x in list3} # using the list comprehension can also be used for finding the common elements in three lists
res = set1.intersection(set2,set3)
print(f"The common elements in the two lists are : {res}")

# wap in python to find whether a string is heterogram or not using set
s = "GeeksforGeeks"
s = s.lower()
if len(set(s)) == len(s):
    print("Yes it's a Heterogram")
else:
    print("Not a Heterogram")

# wap to find the Python Set difference to find lost element from a duplicated array
list1 = [1,2,3,4,5,6]
list2 = [4,5,6]
set1 = set(list1)
set2 = set(list2)
res = set1.difference(set2)
print(f"The lost elements from the duplicated array are : {res}")

# wap in python to find the one least element common in two lists using set
list1 = set([1,2,3,4,5]) 
list2 = set([4,5,6,7,8])
common = list1.intersection(list2)
if any(i in list2 for i in list1):
    print(f"The least common element in the two lists is : {common}")
else:
    print("No common elements")
