# The use of For loops for the range function and also including the else Statements
# # The range function generates a sequence of numbers, which can be iterated over using a for loop
# n = 4
# for i in range(0,n,1):  # start stop and steps
#     print(i) 
# else:
#     print("Inside Else Block")

# Iterating Over List, Tuple, String and Dictionary Using for Loops in Python
# list = ["geeks", "for", "geeks"]
# for i in list:
#     print(i)
    
# tuple = ("geeks", "for", "geeks")
# for i in tuple:
#     print(i)
    
# string = "Geeks"
# for i in string:
#     print(i)
    
# d = dict({'x':123, 'y':354})
# for i in d:
#     print("%s  %d" % (i, d[i]))
    
# set1 = {1, 2, 3, 4, 5}
# for i in set1:
#     print(i)

# The use of While loop using iteration and initializing 
# Along with the use of the else statement with while loop
# cnt = 0
# while cnt < 3: 
#     cnt += 1 # cnt = cnt + 1    
#     print(cnt)
# else:
#     print("Thank You")

# The use of Infinite Loop
# while(True):
#     print("Hello Greek")

# pattern questions
# n = int(input())
# for i in range(1,n):
#     for j in range(i):
#         print("*", end=' ')
#     print()

# continue and Break and Pass statements
for letter in 'geeksforgeeks':
    # if letter == 'e' or letter == 's':
        # break # stops the loop
        # continue  # skip the letter 
        pass # used for empty loop with no condition 
print('Current Letter :', letter)

# enumerate is used in python to iterate in for loop along with tracking the index
list1 = ["eat","sleep","code"]
for i,j in enumerate(list1):
        print(i,j)

x = int(input("Enter the Number to find its value : "))
n = int(input("Enter the range of table : "))
i=0
while i<n:
        i += 1
# The use of For loops for the range function and also including the else Statements
# # The range function generates a sequence of numbers, which can be iterated over using a for loop
# n = 4
# for i in range(0,n,1):  # start stop and steps
#     print(i) 
# else:
#     print("Inside Else Block")

# Iterating Over List, Tuple, String and Dictionary Using for Loops in Python
# list = ["geeks", "for", "geeks"]
# for i in list:
#     print(i)
    
# tuple = ("geeks", "for", "geeks")
# for i in tuple:
#     print(i)
    
# string = "Geeks"
# for i in string:
#     print(i)
    
# d = dict({'x':123, 'y':354})
# for i in d:
#     print("%s  %d" % (i, d[i]))
    
# set1 = {1, 2, 3, 4, 5}
# for i in set1:
#     print(i)

# The use of While loop using iteration and initializing 
# Along with the use of the else statement with while loop
# cnt = 0
# while cnt < 3: 
#     cnt += 1 # cnt = cnt + 1    
#     print(cnt)
# else:
#     print("Thank You")

# The use of Infinite Loop
# while(True):
#     print("Hello Greek")

# pattern questions
# n = int(input())
# for i in range(1,n):
#     for j in range(i):
#         print("*", end=' ')
#     print()

# continue and Break and Pass statements
for letter in 'geeksforgeeks':
    # if letter == 'e' or letter == 's':
        # break # stops the loop
        # continue  # skip the letter 
        pass # used for empty loop with no condition 
print('Current Letter :', letter)

# enumerate is used in python to iterate in for loop along with tracking the index
list1 = ["eat","sleep","code"]
for i,j in enumerate(list1):
        print(i,j)

x = int(input("Enter the Number to find its value : "))
n = int(input("Enter the range of table : "))
i=0
while i<n:
        i += 1
        print(f"{x} * {i} = {x * i}")