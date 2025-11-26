# Use of the If statement to check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote ")
else:
    print("Not eligible to vote ")

# the use of ternary operator is used in python fro only If Else statement
# Syntax: variable = value_if_true if condition else value_if_false
# Sometimes also called as Conditional Expression
mark = int(input("Enter Your Marks: "))
result = "Pass" if mark >= 45 else "Fail"
print(f"Your result is: {result}")

# The use of If, Elif, and Else statements to categorize age groups
age = 25
if age <= 12:
    print("Adult")
elif age <=19:
    print("Teenager")
elif age <= 35:
    print("Young Adult")
else:
    print("Adult")

# The use of nested If statements to determine senior citizen discounts
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# The use of match-case statement which is the equivalent of switch-case in other languages
day = int(input("Enter a number (1-7) for the day of the week: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 :
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Assigment opeartor like -> ( += , -=, *=, /= , //= ) 
a = 10
a += 5 # similarly for the oter opeartor like the substraction,multiplication, addition, division and dloor division also
print(a)
# Identity Opeartor -> is generally used to compatre the memeory locations of two objects
# It includes -> 'is'  'is not'
l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1  # here l3 and l1 is pointing to one object and the memeory address is same
print(l3 is l1)
print(l3 is not l1)
print(l1 is l2)
# Memebership Opeartor -> used to check whether if sequence is presented in an Object include
# ' in '  & ' not in '
a1 = [1,2,3,4,5]
print(3 in a1)
print(4 not in a1)

# Arithmetic Operators includes -> ( + , - , /, % , * ) like
# The opeartors are used with numeric values to perform common mathematical Problems
print(5*5,5+5,5-5,5/5,5%5)
print(10/5)
print(10//5) # Floor Division Opeartor 
# it divides the first number by second and then rounds the result to the nearest Whole number
# Comparison Opeartor includes -> ( == , != ,< , > , >= , <= ) 
a = 1
b = 2
print(a>b,a<b,a==b,a!=b,a>=b,a<=b)
# Logical Opeartor used to combine Conditional statements
print(a>b and b<a) # Logical AND operator
print(a<b or b>a) #Logical OR operator

# Use of the If statement to check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote ")
else:
    print("Not eligible to vote ")

# the use of ternary operator is used in python fro only If Else statement
# Syntax: variable = value_if_true if condition else value_if_false
# Sometimes also called as Conditional Expression
mark = int(input("Enter Your Marks: "))
result = "Pass" if mark >= 45 else "Fail"
print(f"Your result is: {result}")

# The use of If, Elif, and Else statements to categorize age groups
age = 25
if age <= 12:
    print("Adult")
elif age <=19:
    print("Teenager")
elif age <= 35:
    print("Young Adult")
else:
    print("Adult")

# The use of nested If statements to determine senior citizen discounts
age = 70
is_member = True
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

# The use of match-case statement which is the equivalent of switch-case in other languages
day = int(input("Enter a number (1-7) for the day of the week: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5 :
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Assigment opeartor like -> ( += , -=, *=, /= , //= ) 
a = 10
a += 5 # similarly for the oter opeartor like the substraction,multiplication, addition, division and dloor division also
print(a)
# Identity Opeartor -> is generally used to compatre the memeory locations of two objects
# It includes -> 'is'  'is not'
l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1  # here l3 and l1 is pointing to one object and the memeory address is same
print(l3 is l1)
print(l3 is not l1)
print(l1 is l2)
# Memebership Opeartor -> used to check whether if sequence is presented in an Object include
# ' in '  & ' not in '
a1 = [1,2,3,4,5]
print(3 in a1)
print(4 not in a1)

# Arithmetic Operators includes -> ( + , - , /, % , * ) like
# The opeartors are used with numeric values to perform common mathematical Problems
print(5*5,5+5,5-5,5/5,5%5)
print(10/5)
print(10//5) # Floor Division Opeartor 
# it divides the first number by second and then rounds the result to the nearest Whole number
# Comparison Opeartor includes -> ( == , != ,< , > , >= , <= ) 
a = 1
b = 2
print(a>b,a<b,a==b,a!=b,a>=b,a<=b)
# Logical Opeartor used to combine Conditional statements
print(a>b and b<a) # Logical AND operator
print(a<b or b>a) #Logical OR operator
print(not(a>b and b<a)) # Logical NOT operator