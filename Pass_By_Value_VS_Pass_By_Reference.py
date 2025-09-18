<<<<<<< HEAD
# In pass by reference, the function receives the memory address of the original object, not a copy.
# This means both the caller and the function share the same object.
def same_list(list):
    # list = ["A"]  # Even the value is changed  still my_list refers to the original Subject 
    list.append("Y")  # This will modify the original list because it is passed by reference and not by value
    print("Inside function:", list)
    # The original list is modified, so the change is reflected outside the function as well.
    # return list

my_list = ["X"]
same_list(my_list)
print("Outside function:", my_list)  # This will print the modified list with "Y" added

# In pass-by-value, a copy of the object is passed to the function, so the changes will be in inside the function only.
string = "Hello"
def fun(string):
    string = "GeeksforGeeks"  # This will not affect the original string
    print("Inside function:", string)
fun(string)
print("Outside function:", string)  # This will still print "Hello" because string is passed by value


# variable  and List identity in python
# Identity refers to the memory location of an object, which can be checked using the id()
a = 2
b = 2
print(id(a))
print(id(b))
print(a is b) # return boolean statement if both value are pointing to same object and have same memory
x = [1,2,3]
y = [1,2,3]
print(id(x))
print(id(y))
print(x is y) # return false because list in python creates two diff object one each despite having identical values

# Immutability and mutability of staring and List
# def fun(string):
    # a = "New value"
#     # print("Inside Function : ",a)
# text = "Old value"
# fun(text)  # This will not change the original text because strings are immutable in Python
# print("Before Function Call:", text)
def foo(list):
    # list  = ["A","X"]
    list[0] = "Nothing" # Mutable object is passed instead of creating a new list 
    print("Inside Function:", list)  # This will not change the original list because lists are mutable in Python
list1 = ['Hi', 'how', 'are', 'you', 'doing']
foo(list1)  # This will not change the original list because lists are mutable in Python
print("After Function Call:", list1)  # This will still print the original list because lists are mutable in Python
=======
# In pass by reference, the function receives the memory address of the original object, not a copy.
# This means both the caller and the function share the same object.
def same_list(list):
    # list = ["A"]  # Even the value is changed  still my_list refers to the original Subject 
    list.append("Y")  # This will modify the original list because it is passed by reference and not by value
    print("Inside function:", list)
    # The original list is modified, so the change is reflected outside the function as well.
    # return list

my_list = ["X"]
same_list(my_list)
print("Outside function:", my_list)  # This will print the modified list with "Y" added

# In pass-by-value, a copy of the object is passed to the function, so the changes will be in inside the function only.
string = "Hello"
def fun(string):
    string = "GeeksforGeeks"  # This will not affect the original string
    print("Inside function:", string)
fun(string)
print("Outside function:", string)  # This will still print "Hello" because string is passed by value


# variable  and List identity in python
# Identity refers to the memory location of an object, which can be checked using the id()
a = 2
b = 2
print(id(a))
print(id(b))
print(a is b) # return boolean statement if both value are pointing to same object and have same memory
x = [1,2,3]
y = [1,2,3]
print(id(x))
print(id(y))
print(x is y) # return false because list in python creates two diff object one each despite having identical values

# Immutability and mutability of staring and List
# def fun(string):
    # a = "New value"
#     # print("Inside Function : ",a)
# text = "Old value"
# fun(text)  # This will not change the original text because strings are immutable in Python
# print("Before Function Call:", text)
def foo(list):
    # list  = ["A","X"]
    list[0] = "Nothing" # Mutable object is passed instead of creating a new list 
    print("Inside Function:", list)  # This will not change the original list because lists are mutable in Python
list1 = ['Hi', 'how', 'are', 'you', 'doing']
foo(list1)  # This will not change the original list because lists are mutable in Python
print("After Function Call:", list1)  # This will still print the original list because lists are mutable in Python
>>>>>>> d5a4f36590f1dec64f6b24f7307b0aa4ccb2ff03
# the original list is mutable and can be modified inside the function.