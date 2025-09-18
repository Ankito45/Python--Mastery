<<<<<<< HEAD
a = 5
b = 2.3
c = 2 + 4j
s = "My name is Ankit Sahu"
print(type(a))
print(type(b))
print(type(c))
print(type(s))
print(type(True))

# List -> A list is a collection which is ordered and changeable. Allows duplicate members.
x = ["Geeks", "For", "Geeks"]
print(type(x))
print(x[1])  # print(x[-2]) Accessing the second last element of the list
# x.reverse() # Reversing the list

# Tuple -> A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
y = (1,2,3,4,5)
print(type(y))
print(y[-1]) # used to print the last item of the tuple

# Set -> A set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
set1 = set() # the Keyword set() is used to create a set in python a by default empty set
set1.add(1) # adding an element to the set
print(type(set1))
print(set1)

# Dictionary -> A dictionary is a collection of key-value pairs
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(type(d))
print(d[1])  # Accessing the value associated with key 1\
=======
a = 5
b = 2.3
c = 2 + 4j
s = "My name is Ankit Sahu"
print(type(a))
print(type(b))
print(type(c))
print(type(s))
print(type(True))

# List -> A list is a collection which is ordered and changeable. Allows duplicate members.
x = ["Geeks", "For", "Geeks"]
print(type(x))
print(x[1])  # print(x[-2]) Accessing the second last element of the list
# x.reverse() # Reversing the list

# Tuple -> A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
y = (1,2,3,4,5)
print(type(y))
print(y[-1]) # used to print the last item of the tuple

# Set -> A set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
set1 = set() # the Keyword set() is used to create a set in python a by default empty set
set1.add(1) # adding an element to the set
print(type(set1))
print(set1)

# Dictionary -> A dictionary is a collection of key-value pairs
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(type(d))
print(d[1])  # Accessing the value associated with key 1\
>>>>>>> d5a4f36590f1dec64f6b24f7307b0aa4ccb2ff03
print(d.get(2))  # Using get method to access the value associated with key 2