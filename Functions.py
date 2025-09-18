<<<<<<< HEAD
# Initializing a function with def keyword
# Docstring -> The first string after the function is called the Document string or Docstring in short
def fun():
    """This function prints a message.""" # This is a docstring are always enclosed in triple quotes
    print("This is a function in Functions.py")
    
fun()  # used for calling the function
print(fun.__doc__)  # prints the docstring of the function

# Function to find the whether a number is even or odd and the argument should be int as specified 
def evenOdd(x: int) ->str: # indicates that the function takes an integer and returns a string
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
print(evenOdd(10))  # calling the function with an integer argument

# Default Function Arguments
def myfun(x,y=50):
    print("x:", x, "y:", y)
myfun(10)  # y will take the default value of 50
myfun(10, 20)  # y will take the value of 20

# Keyword Arguments
def student(fname,lname): # here the keyword used is fname and lname
    print(fname,lname)
student(lname="Doe", fname="John")  # order doesn't matter when using keyword arguments

# Positional Arguments
def nameage(name,age):
    print("Hi, I am",name)
    print("My age is",age)
print("\nCase-1:") # \n is used for new line
nameage(30, "Alice")  # here the first argument is age and second is name but the function will print accordingly
print("Case-2:")
print("Alex",25)  # here the first argument is name and second is age

# Arbitrary keyword Arguments -> (*args, and **kwargs) are used as argument names
# Means that the function can take any number of keyword 
def myFun(*args):
    for arg in args:
        print(arg)
myFun("\nHello", "World", 1, 2, 3)  # can take any number of arguments

# A function can also return another function
def Outer_Function():
    s = 'I love GeeksforGeeks'
    def Inner_Function():
        print(s)
    Inner_Function()
Outer_Function()

# Anonymous Functions (Lambda Functions) al;ong with return statement
# Lambda functions are small anonymous functions defined with the lambda keyword
def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda
print(cube(7))
=======
# Initializing a function with def keyword
# Docstring -> The first string after the function is called the Document string or Docstring in short
def fun():
    """This function prints a message.""" # This is a docstring are always enclosed in triple quotes
    print("This is a function in Functions.py")
    
fun()  # used for calling the function
print(fun.__doc__)  # prints the docstring of the function

# Function to find the whether a number is even or odd and the argument should be int as specified 
def evenOdd(x: int) ->str: # indicates that the function takes an integer and returns a string
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
print(evenOdd(10))  # calling the function with an integer argument

# Default Function Arguments
def myfun(x,y=50):
    print("x:", x, "y:", y)
myfun(10)  # y will take the default value of 50
myfun(10, 20)  # y will take the value of 20

# Keyword Arguments
def student(fname,lname): # here the keyword used is fname and lname
    print(fname,lname)
student(lname="Doe", fname="John")  # order doesn't matter when using keyword arguments

# Positional Arguments
def nameage(name,age):
    print("Hi, I am",name)
    print("My age is",age)
print("\nCase-1:") # \n is used for new line
nameage(30, "Alice")  # here the first argument is age and second is name but the function will print accordingly
print("Case-2:")
print("Alex",25)  # here the first argument is name and second is age

# Arbitrary keyword Arguments -> (*args, and **kwargs) are used as argument names
# Means that the function can take any number of keyword 
def myFun(*args):
    for arg in args:
        print(arg)
myFun("\nHello", "World", 1, 2, 3)  # can take any number of arguments

# A function can also return another function
def Outer_Function():
    s = 'I love GeeksforGeeks'
    def Inner_Function():
        print(s)
    Inner_Function()
Outer_Function()

# Anonymous Functions (Lambda Functions) al;ong with return statement
# Lambda functions are small anonymous functions defined with the lambda keyword
def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda
print(cube(7))
>>>>>>> d5a4f36590f1dec64f6b24f7307b0aa4ccb2ff03
print(cube_l(7))