<<<<<<< HEAD
# a list is a built-in dynamic sized array (automatically grows and shrinks).
# List can contain duplicate items.
# List in Python are Mutable. Hence, we can modify, replace or delete the items.
# List are ordered. It maintain the order of elements based on how they are added.
# Accessing items in List can be done directly using their position (index), starting from 0.
# list stores references (pointers) to the actual objects in memory not the actual values

T = [10, 20, "GfG", 40, True,10,98,69,77,"hello"]
# Accessing items in List
print(T[0])  # Accessing the first item
print(T[-1]) # Accessing the last item 
print(type(T[2]))  # string -> checking the type of data types
print(type(T[4]))  # boolean -> checking the type of data types
print(T[1:3])  # Slicing the list from index 1 to 2 (not including index 3)
n = T.__len__()  # Getting the length of the list
print(n)  # Displaying the length of the list
c = T[1:8:n]  # Slicing the list from index 1 to 7 with a step of 3
print(c)  # Displaying the sliced list
print(T.count(10))  # Counting total occurrences of 10 in the list
print(T.index("GfG"))  # Finding the index of "GfG"
print(T.pop())  # Removing and returning the last item from the list
print(T.reverse())  # Reversing the list in place
rev = list(reversed([1,2,3,4,5,6,8,90,45,45])) # Use reversed() to create an iterator
print(rev)  # Displaying the reversed list

p = [10,40,80,30,77,4,48,23,30,4,90]
p.sort()  # Sorting the list in ascending order if it has mixed data types it will raise an error
print(p)  # Displaying the sorted list
del p[0]  # Deleting the first item from the list
print(p)  # Displaying the list after deletion
p.remove(30)  # Removing the first occurrence of 30 from the list
print(p)  # Displaying the list after removing 30
p.pop(2)  # Removing and returning the item at index 2  -> cab use print value to find the value
print(p)  # Displaying the list after popping the item at index 2
# ------------------------------------------------------------------
sum = 0  # Addition of elements to the list
for i in p:  # Iterating through the list
    sum += i
print("Sum of elements in p:", sum)  # Displaying the sum of elements in the list

# list can be integers,strings any other data types also it contain mixed data types
b = [1, 2, 3, 4, 5]
c = [1, 'hello', 3.14, True] # -> mixed data types
print(b)
print(c)
z = list((1, 2, 3, 'apple', 4.5)) # list by passing an iterable (like a string, tuple or another list) to list() function  
print(z)
x = [2] # create a list with repeated elements using the multiplication operator.
print(x*5)

T = []
T.append(10)  # Adding 10 to end of list -> append()
print("After append(10):", T)  
T.insert(0, 5) # Inserting 5 at index 0 -> insert()
print("After insert(0, 5):", T) 
T.extend([15, 20, 25])   # Adding multiple elements  [15, 20, 25] at the end -> extend()
print("After extend([15, 20, 25]):", T)
T[2] = 100 # updating elements
print(T) 

# List Comprehension -> a concise way to create lists in python using a single line of code.   
squares = [x*2 for x in range(10)]  # creating a list of squares of numbers from 0 to 9
print("List Comprehension:", squares)
list1 = [2,3,4,5,6] # -> another way to approach list Comprehension
new_list = [x**3 for x in list1]  # creating a new list with squares of even numbers
print("New List with squares of even numbers:", new_list)



#-----------List Questions-------------------
#  Sum of digits of a number until it becomes a single digit
n = int(input())
# if n<=9:
#     print(n)
while n>9:
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10 # using floor division like 10//3 -> 3.33 but value is 3
    n = sum
print(sum)

# remove duplicates in a list 
arr = [2,2,2,2,2,2,2]
new_arr = []
duplicates = []
for i in range(len(arr)):
    for j in range(len(new_arr)):
        if arr[i] == new_arr[j]:
           duplicates.append(arr[i])
    if arr[i] not in duplicates:
        new_arr.append(arr[i])
print(duplicates)
print(new_arr)

# Rearrange Positive Negative -> first positive and then negative
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
pos = [x for x in arr if x>=0]
neg = [x for x in arr if x<0]
max_len = max(len(pos),len(neg))
result = []
for i in range(max_len):
    if i < len(pos):
        result.append(pos[i])
    if i < len(neg):
        result.append(neg[i])
print(result)

# Maximum Element in a list from the right side (leader problem -> an element is a leader if it is greater than all the elements to its right)
arr = [16, 17, 4, 3, 5, 2]
leaders = []
max_from_right = float('-inf') 
for num in reversed(arr):
        if num >= max_from_right:
            leaders.append(num)
            max_from_right = num # update the maximum from the right
print(leaders) # Reverse to maintain the original order of leaders

# Stock buy and sell problem  with only one transaction allowed
prices = [7, 1, 5, 3, 6, 4]
if not prices:
    print("O")
min_price = float('inf')   # smallest price seen so far
max_profit = 0             # largest profit seen so far
for price in prices:
    if price < min_price:
        min_price = price # found a new lower buy price
    elif price - min_price > max_profit:
        max_profit = price - min_price # found a new higher profit
print(max_profit) # 6 - 1 -> buy at 1 and sell at 6 
# Stock buy and sell problem with multiple transactions allowed
profit = 0
for i in range(1, len(prices)): # loop runs from 1 due to comparing the yesterday's price and not the tomorrow price 
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1] # add the profit from each upward movement  
print(profit)  # Total profit from multiple transactions

#-------------------------------------------------------------------------
""" Your task is to tell whether it is possible to group any same ‘K’ characters 
 and return ‘1’ if it is possible, otherwise return ‘0’."""
n,k = map(int, input().split())
s = input()  # Input a string
counts = {}
for char in s:
    counts[char] = counts.get(char,0) + 1
# print(counts)  # Displaying the character counts in the string
# print(counts.values())  # Displaying the counts of characters like a list 
for count in counts.values():
        if count >= k:
            print("1")
            break
else:
    print("0")  # If no character has a count >= k, print 0

# Missing range of numbers in a list
#User function Template for python3
arr = [14, 15, 20, 30, 31, 45]
lower = 10
upper = 50
if len(arr) == 0:
    print([[lower,upper]])
    missing = []
    if arr[0] > lower:
        missing.append([lower, arr[0] - 1])
        # Pair of consecutive elements 
        for a, b in zip(arr, arr[1:]):
            if b - a > 1:
                missing.append([a + 1, b - 1])
        if arr[-1] < upper:
            missing.append([arr[-1] + 1, upper])    
        print( missing)

# Union of two sorted or unsorted array using set ---> But we will use Two Pointers Technique
a = [1, 2, 3, 4, 4, 5]
b = [2, 3, 4, 5, 6, 7]
i,j = 0, 0
union = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i += 1
    elif a[i] > b[j]:
        if not union or union[-1] != b[j]:
            union.append(b[j])
        j += 1
    else:  # Equal elements
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i += 1
        j += 1
print(union)
# ---- Actually this below is also a part of two pointer method but only used when both arrays have same length
# while i < len(a):
#     if not union or union[-1] != a[i]:
#         union.append(a[i])
#     i += 1
# while j < len(b):
#     if not union or union[-1] != b[j]:
#         union.append(b[j])
#     j += 1
# print(union)


arr =  [2, 4, 1, 7, 5, 0]
n = arr.__len__()
i = n - 2
# Finding the pivot index and element in the given array
# Pivot is the first element from the end which is smaller than its next element
while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1
print("Index of first decreasing element from the end:", arr[i])
if i>=0:
    for j in range(n - 1, i, -1):
        if arr[j] > arr[i]:
            break
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
print("Next permutation of the array:", arr)  # Displaying the next permutation of the array

# Majority Element -> an element that appears more than n/2 times, where n is the size of the array.
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4] 
candidate = None
count = 0
for num in arr:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)
if arr.count(candidate) > len(arr) // 2:
    print("Majority Element:", candidate)
else:
    print("No Majority Element")

# Maximum sum of a subarray of list 
arr = [2, 3, -8, 7, 1, 2, 3]
if all(num >=0 for num in arr):
    print(sum(arr))
max_sum = current_sum = arr[0]  # Initialize with the first element
for num in arr[1:]:
    current_sum = max(num, current_sum + num)  # Either start a new subarray or continue the existing one
    max_sum = max(max_sum, current_sum)  # Update the maximum sum found so far
print(max_sum)

# Equalize the array -> make all elements equal by removing some elements
A = [7, 5, 21, 17]
N,k = 4, 2
if N == 1:
    print(0)  # If there's only one element, no moves are needed
moves = 0 
A.sort()
if N%2 == 1:
    mid = N//2
else:
    mid = N//2-1
for i in range(N):
    s = abs(A[mid]-A[i])
    if s%k != 0:
        print("-1")
    else:
        moves += (s//k)
print("Total moves required to equalize the array:", moves)

# Max distance between same elements in a list
arr = [1, 1, 2, 2, 2, 1]
first_index = {} # used for faster data calculation to store the first occurrence of each element
max_dist = 0
for i, val in enumerate(arr): # enumerate gives both index and value If the value is not in the dictionary, store its index
    if val not in first_index:
        first_index[val] = i
    else:
        max_dist = max(max_dist, i - first_index[val])
print(max_dist) # the subtraction done on the same element's first index and current index gives the maximum distance between same elements in a list

# Min Swaps to Group 1s using Sliding Window Technique
arr = [1, 0, 1, 0, 1]
n = len(arr)
if 1 not in arr:
    print("-1")
k = sum(arr)
ones_in_window = sum(arr[:k])
max_ones = ones_in_window
for i in range(1,n-k+1):
    ones_in_window += arr[i + k - 1] - arr[i - 1]
    if ones_in_window > max_ones:
        max_ones = ones_in_window # swap at index 1 to index 4 
=======
# a list is a built-in dynamic sized array (automatically grows and shrinks).
# List can contain duplicate items.
# List in Python are Mutable. Hence, we can modify, replace or delete the items.
# List are ordered. It maintain the order of elements based on how they are added.
# Accessing items in List can be done directly using their position (index), starting from 0.
# list stores references (pointers) to the actual objects in memory not the actual values

T = [10, 20, "GfG", 40, True,10,98,69,77,"hello"]
# Accessing items in List
print(T[0])  # Accessing the first item
print(T[-1]) # Accessing the last item 
print(type(T[2]))  # string -> checking the type of data types
print(type(T[4]))  # boolean -> checking the type of data types
print(T[1:3])  # Slicing the list from index 1 to 2 (not including index 3)
n = T.__len__()  # Getting the length of the list
print(n)  # Displaying the length of the list
c = T[1:8:n]  # Slicing the list from index 1 to 7 with a step of 3
print(c)  # Displaying the sliced list
print(T.count(10))  # Counting total occurrences of 10 in the list
print(T.index("GfG"))  # Finding the index of "GfG"
print(T.pop())  # Removing and returning the last item from the list
print(T.reverse())  # Reversing the list in place
rev = list(reversed([1,2,3,4,5,6,8,90,45,45])) # Use reversed() to create an iterator
print(rev)  # Displaying the reversed list

p = [10,40,80,30,77,4,48,23,30,4,90]
p.sort()  # Sorting the list in ascending order if it has mixed data types it will raise an error
print(p)  # Displaying the sorted list
del p[0]  # Deleting the first item from the list
print(p)  # Displaying the list after deletion
p.remove(30)  # Removing the first occurrence of 30 from the list
print(p)  # Displaying the list after removing 30
p.pop(2)  # Removing and returning the item at index 2  -> cab use print value to find the value
print(p)  # Displaying the list after popping the item at index 2
# ------------------------------------------------------------------
sum = 0  # Addition of elements to the list
for i in p:  # Iterating through the list
    sum += i
print("Sum of elements in p:", sum)  # Displaying the sum of elements in the list

# list can be integers,strings any other data types also it contain mixed data types
b = [1, 2, 3, 4, 5]
c = [1, 'hello', 3.14, True] # -> mixed data types
print(b)
print(c)
z = list((1, 2, 3, 'apple', 4.5)) # list by passing an iterable (like a string, tuple or another list) to list() function  
print(z)
x = [2] # create a list with repeated elements using the multiplication operator.
print(x*5)

T = []
T.append(10)  # Adding 10 to end of list -> append()
print("After append(10):", T)  
T.insert(0, 5) # Inserting 5 at index 0 -> insert()
print("After insert(0, 5):", T) 
T.extend([15, 20, 25])   # Adding multiple elements  [15, 20, 25] at the end -> extend()
print("After extend([15, 20, 25]):", T)
T[2] = 100 # updating elements
print(T) 

# List Comprehension -> a concise way to create lists in python using a single line of code.   
squares = [x*2 for x in range(10)]  # creating a list of squares of numbers from 0 to 9
print("List Comprehension:", squares)
list1 = [2,3,4,5,6] # -> another way to approach list Comprehension
new_list = [x**3 for x in list1]  # creating a new list with squares of even numbers
print("New List with squares of even numbers:", new_list)



#-----------List Questions-------------------
#  Sum of digits of a number until it becomes a single digit
n = int(input())
# if n<=9:
#     print(n)
while n>9:
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10 # using floor division like 10//3 -> 3.33 but value is 3
    n = sum
print(sum)

# remove duplicates in a list 
arr = [2,2,2,2,2,2,2]
new_arr = []
duplicates = []
for i in range(len(arr)):
    for j in range(len(new_arr)):
        if arr[i] == new_arr[j]:
           duplicates.append(arr[i])
    if arr[i] not in duplicates:
        new_arr.append(arr[i])
print(duplicates)
print(new_arr)

# Rearrange Positive Negative -> first positive and then negative
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
pos = [x for x in arr if x>=0]
neg = [x for x in arr if x<0]
max_len = max(len(pos),len(neg))
result = []
for i in range(max_len):
    if i < len(pos):
        result.append(pos[i])
    if i < len(neg):
        result.append(neg[i])
print(result)

# Maximum Element in a list from the right side (leader problem -> an element is a leader if it is greater than all the elements to its right)
arr = [16, 17, 4, 3, 5, 2]
leaders = []
max_from_right = float('-inf') 
for num in reversed(arr):
        if num >= max_from_right:
            leaders.append(num)
            max_from_right = num # update the maximum from the right
print(leaders) # Reverse to maintain the original order of leaders

# Stock buy and sell problem  with only one transaction allowed
prices = [7, 1, 5, 3, 6, 4]
if not prices:
    print("O")
min_price = float('inf')   # smallest price seen so far
max_profit = 0             # largest profit seen so far
for price in prices:
    if price < min_price:
        min_price = price # found a new lower buy price
    elif price - min_price > max_profit:
        max_profit = price - min_price # found a new higher profit
print(max_profit) # 6 - 1 -> buy at 1 and sell at 6 
# Stock buy and sell problem with multiple transactions allowed
profit = 0
for i in range(1, len(prices)): # loop runs from 1 due to comparing the yesterday's price and not the tomorrow price 
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1] # add the profit from each upward movement  
print(profit)  # Total profit from multiple transactions

#-------------------------------------------------------------------------
""" Your task is to tell whether it is possible to group any same ‘K’ characters 
 and return ‘1’ if it is possible, otherwise return ‘0’."""
n,k = map(int, input().split())
s = input()  # Input a string
counts = {}
for char in s:
    counts[char] = counts.get(char,0) + 1
# print(counts)  # Displaying the character counts in the string
# print(counts.values())  # Displaying the counts of characters like a list 
for count in counts.values():
        if count >= k:
            print("1")
            break
else:
    print("0")  # If no character has a count >= k, print 0

# Missing range of numbers in a list
#User function Template for python3
arr = [14, 15, 20, 30, 31, 45]
lower = 10
upper = 50
if len(arr) == 0:
    print([[lower,upper]])
    missing = []
    if arr[0] > lower:
        missing.append([lower, arr[0] - 1])
        # Pair of consecutive elements 
        for a, b in zip(arr, arr[1:]):
            if b - a > 1:
                missing.append([a + 1, b - 1])
        if arr[-1] < upper:
            missing.append([arr[-1] + 1, upper])    
        print( missing)

# Union of two sorted or unsorted array using set ---> But we will use Two Pointers Technique
a = [1, 2, 3, 4, 4, 5]
b = [2, 3, 4, 5, 6, 7]
i,j = 0, 0
union = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i += 1
    elif a[i] > b[j]:
        if not union or union[-1] != b[j]:
            union.append(b[j])
        j += 1
    else:  # Equal elements
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i += 1
        j += 1
print(union)
# ---- Actually this below is also a part of two pointer method but only used when both arrays have same length
# while i < len(a):
#     if not union or union[-1] != a[i]:
#         union.append(a[i])
#     i += 1
# while j < len(b):
#     if not union or union[-1] != b[j]:
#         union.append(b[j])
#     j += 1
# print(union)


arr =  [2, 4, 1, 7, 5, 0]
n = arr.__len__()
i = n - 2
# Finding the pivot index and element in the given array
# Pivot is the first element from the end which is smaller than its next element
while i >= 0 and arr[i] >= arr[i + 1]:
    i -= 1
print("Index of first decreasing element from the end:", arr[i])
if i>=0:
    for j in range(n - 1, i, -1):
        if arr[j] > arr[i]:
            break
    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
print("Next permutation of the array:", arr)  # Displaying the next permutation of the array

# Majority Element -> an element that appears more than n/2 times, where n is the size of the array.
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4] 
candidate = None
count = 0
for num in arr:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)
if arr.count(candidate) > len(arr) // 2:
    print("Majority Element:", candidate)
else:
    print("No Majority Element")

# Maximum sum of a subarray of list 
arr = [2, 3, -8, 7, 1, 2, 3]
if all(num >=0 for num in arr):
    print(sum(arr))
max_sum = current_sum = arr[0]  # Initialize with the first element
for num in arr[1:]:
    current_sum = max(num, current_sum + num)  # Either start a new subarray or continue the existing one
    max_sum = max(max_sum, current_sum)  # Update the maximum sum found so far
print(max_sum)

# Equalize the array -> make all elements equal by removing some elements
A = [7, 5, 21, 17]
N,k = 4, 2
if N == 1:
    print(0)  # If there's only one element, no moves are needed
moves = 0 
A.sort()
if N%2 == 1:
    mid = N//2
else:
    mid = N//2-1
for i in range(N):
    s = abs(A[mid]-A[i])
    if s%k != 0:
        print("-1")
    else:
        moves += (s//k)
print("Total moves required to equalize the array:", moves)

# Max distance between same elements in a list
arr = [1, 1, 2, 2, 2, 1]
first_index = {} # used for faster data calculation to store the first occurrence of each element
max_dist = 0
for i, val in enumerate(arr): # enumerate gives both index and value If the value is not in the dictionary, store its index
    if val not in first_index:
        first_index[val] = i
    else:
        max_dist = max(max_dist, i - first_index[val])
print(max_dist) # the subtraction done on the same element's first index and current index gives the maximum distance between same elements in a list

# Min Swaps to Group 1s using Sliding Window Technique
arr = [1, 0, 1, 0, 1]
n = len(arr)
if 1 not in arr:
    print("-1")
k = sum(arr)
ones_in_window = sum(arr[:k])
max_ones = ones_in_window
for i in range(1,n-k+1):
    ones_in_window += arr[i + k - 1] - arr[i - 1]
    if ones_in_window > max_ones:
        max_ones = ones_in_window # swap at index 1 to index 4 
>>>>>>> d5a4f36590f1dec64f6b24f7307b0aa4ccb2ff03
print(k - max_ones) # Minimum swaps required to group all 1s together in the array