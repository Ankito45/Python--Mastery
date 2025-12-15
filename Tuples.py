# Tuple is a an immutable ordered Collection defined by parentheses -> '()'
# Tuples can contain any data type, including other tuples
tup1 = (1, 2, 3, 4, 5)
tup = (tup1)
print(tup)
# Add tuple to a tuple. 
# Tuples are immutable so we cannot change them but we can concatenate two tuples to form a new tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
print(thistuple + y)
print(tup is tup1)  # This print True bcz tup is pointing to the same object as tup1
# Type conversion of list to tuple and also vice versa
li = [1, 2, 3, 4, 5]
print(tuple(li))  # Converts list to tuple
print(list(tup1))  # Converts tuple to list
tup = tuple("GeeksforGeeks")  # Converting string to tuple -> built-in function to convert string to tuple
print(tup)  # Displays the tuple created from the string

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2) * 3 # This creates a tuple with nested tuples and repeats it 3 times called repetition
print(tup3)
tuple1 = ("Geeks")  # we can even create a tuple with a single element using tuple function
print(tuple1[0]) # accessing the first element of a tuple
print(tuple1[1:4])  # Slicing the tuple to get elements from index 1 to 3
tup = ("Geeks", "for", "Geeks") # packing a tuple with multiple elements
a,b,c = tup  # a -> gets first element b -> rest of th element c -> gets the last element 
print(f"{a}\n{b}\n{c}")  # Displaying the unpacked values
tup2 = (1,2,3,4,5,6,8,9,10)
e, *f, g = tup2 # Tuple Unpacking with Asterisk (*) -> operator can be used in tuple unpacking to grab multiple items into a list.
print(e, f, g)

# Slicing Tuple
tup = tuple('GEEKSFORGEEKS')
tup1 = tup
print(tup[1:]) # Removing the first element
print(tup[::-1]) # Reversing the complete tuple from end to start
print(tup[4:9]) # Making a tuple from the sliced part
print(len(tup)) # to find the length of the tuple
del tup1 # used for deleting a tuple after deleting -> print(tup1) generates an error

# Tuple is a an immutable ordered Collection defined by parentheses -> '()'
# Tuples can contain any data type, including other tuples
tup1 = (1, 2, 3, 4, 5)
tup = (tup1)
print(tup)
print(tup is tup1)  # This print True bcz tup is pointing to the same object as tup1
# Type conversion of list to tuple and also vice versa
li = [1, 2, 3, 4, 5]
print(tuple(li))  # Converts list to tuple
print(list(tup1))  # Converts tuple to list
tup = tuple("GeeksforGeeks")  # Converting string to tuple -> built-in function to convert string to tuple
print(tup)  # Displays the tuple created from the string

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2) * 3 # This creates a tuple with nested tuples and repeats it 3 times called repetition
print(tup3)
tuple1 = ("Geeks")  # we can even create a tuple with a single element using tuple function
print(tuple1[0]) # accessing the first element of a tuple
print(tuple1[1:4])  # Slicing the tuple to get elements from index 1 to 3
tup = ("Geeks", "for", "Geeks") # packing a tuple with multiple elements
a,b,c = tup  # a -> gets first element b -> rest of th element c -> gets the last element 
print(f"{a}\n{b}\n{c}")  # Displaying the unpacked values
tup2 = (1,2,3,4,5,6,8,9,10)
e, *f, g = tup2 # Tuple Unpacking with Asterisk (*) -> operator can be used in tuple unpacking to grab multiple items into a list.
print(e, f, g)

# Slicing Tuple
tup = tuple('GEEKSFORGEEKS')
tup1 = tup
print(tup[1:]) # Removing the first element
print(tup[::-1]) # Reversing the complete tuple from end to start
print(tup[4:9]) # Making a tuple from the sliced part
print(len(tup)) # to find the length of the tuple
del tup1 # used for deleting a tuple after deleting -> print(tup1) generates an error
