# Python exception handling handles errors that occurs during  the execution of a program 
# In python we don't have try and catch rather we have the try and except indeed and also we have the else and finally block also fro exception Handling 
n = 10
try:
    res = n/0
except ZeroDivisionError:
    print("Can't divide by zero!")
# Exception -> are less less severe than the errors and can be handled by the program. Occurs Mainly due to wrong/invalid Input missing files and network issues
# Errors -> errors are very severe and are not handled by the program. They are mainly due to wrong CODE logic  or configuration that are needed to be fix by the programmer 
# print(hello world) # Raises error -> SyntaxError/InvalidSyntax
# n = 10 
# res = n/0 # called as ZeroDivisionError
# Try -> let us test a block of code for errors python will execute the code in this block and if the exception is found it jumps to the except block
# except ->  enables us to handle the error or exception. If the code inside the try block throws an error, Python jumps to the except block and executes it.
# else -> is optional and if included, must follow all except blocks. The else block runs only if no exceptions are raised in the try block
# finally -> Always runs, regardless of whether an exception occurred or not. It is typically used for cleanup operations (closing files, releasing resources)
try:
    n = 0
    res = 100/n 
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Enter a valid number")
else: # runs if no exception occurs, displaying the result.
    print("Result is ", res)
finally: # runs regardless of the outcome, indicating the completion of the program 
    print("Execution Complete")

# Catching multiple errors in a single block if we need to handle them in the same way or we can separate them if different types of exceptions require different handling.
a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
except (ValueError, TypeError) as e: # Catches the error of the test 'twenty' which is not a int data type
    print("Error", e)
except IndexError:
    print("Index out of range.")

# Raise Exception
def set_age(age): # function set_age checks if the age is negative. If so, it raises a ValueError 
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")
try:
    set_age(-5)
except ValueError as e:
    print(e)

# -----Advantages & Disadvantages of Exception Handling-----
# Adv -> 1. Improved program relibility 
    #    2. Simplified Exception Handling 
    #    3. Cleaner Code and Easier Debugging 
# Disadv -> 1. Performance Overheat
    #       2. Increased Code Complexity 
    #       3. Possible security risks