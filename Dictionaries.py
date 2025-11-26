# Python dictionary is a data structure that stores the value in key: value pairs. 
# Values in a dictionary can be of any data type and can be duplicated  whereas Keys can be repeated
# Keys in dictionary are IMMUTABLE 
d = {1:'Geeks',2:'For',3:'Geeks'}
print(d.__len__) # counts the length of the string  
d1 = dict(a = "Geeks", b = "for", c = "Geeks") # can be created using the 'dict' keyword
print(d1)
print(d[1]) # Access using key and retrieve value from key 
print(d.get(2))  # access value at key 2 using '.get()' function
print(d.keys()) # getting key values using 'key()' function
d["Name"] = "Ankit" # Adding value in dictionary 
d[1] = "Python dict" # updating the value of key 1 to Python dict
del d["Name"] # use to remove any key from the dictionary -> print the dictionary to get updated
val = d.pop(3) # removes and returns the value given at the pop function for any index
print(val)
key, val = d.popitem() # removes and returns the last key-value pair
print(f"Key: {key}, Value: {val}")
print(d) 

# Iterating in Dictionary 
a = {"Name":"Ankit","age":24,"Skill":"GenAI Engineer"}
for key in a: # iterate over key and values simultaneously 
    print(key)
for key,value in a.items(): # 'dict.items()' contains both key value together iteration 
    print(f"{key}:{value}")

# Example fo nested Dictionaries 
new_dictionary = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(new_dictionary)

# copy of a dictionary can be created using either shallow copy or deep copy
# These methods allow duplicating dictionary objects, but they behave differently when it comes to nested data
import copy
original = {'name': 'Alice', 'marks': {'math': 90, 'science': 95}}
shallow = copy.copy(original) # first import then use the copy function 
# shallow['marks']['math'] = 100
print("Original: ",original) # both show updated 'math' value due to shared data.
print("Shallow copy: ",shallow)
print(original is shallow) # prints false bcz it actually points to that dictionary not copies the actual memory address

original1 = {'name': 'Alice', 'marks': {'math': 90, 'science': 95}}
deep =  copy.deepcopy(original1)
deep['marks']['math'] = 100
print("Original: ",original1)
print("Deep copy: ",deep)  # original remains unchanged, only deep copy shows the updated 'math' value due to complete new obj 
print(original1 is deep)

# Dictionary Comprehension
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
mydict = {k:v for (k,v) in zip(keys,values)}
print(mydict)
# creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)
# creation using string comprehension
sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)


my_dict1 = {'1':'Geeks','2':'For','3':'Geeks'}
print(my_dict1.get('1'))
print(my_dict1.get('Name')) #  no such key is present due to which the answer is false
print(list(my_dict1.items())[2][2]) # prints 'For' bcz it follows a matrix which tells [x][y]
my_dict1.clear() # used to remove all items of the dictionary along with key and value
print(my_dict1)
d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d2 = {'Name': 'Neha', 'Age': '22'}
d2.update({"Work": "Software Engineer"}) # Adding a single key-value pair
d1.update(d2)
d1['key3'] = 'Geeks'
d1['key4'] = 'is'
d1['key5'] = 'portal'
print(d1)
d3 = {'key1': 'geeks', 'key2': 'for'}
d3 = dict(d3, key3='Geeks', key4='is', key5='portal', key6='Computer')
print(d3)
print(list(d1.values()))

# Concatenate Dictionary string values
a = {'gfg': 'a', 'is': 'b', 'best': 'c'}
b = {'gfg': 'd', 'is': 'e', 'best': 'f'}
a.setdefault('d', 4) # setdefault() is often used to ensure a key exists in the dictionary. If the key doesn't exist, it adds it with a default value.
a.setdefault('e', 5)
res = {key: a[key] + b.get(key, '') for key in a.keys()}
print(res)
for key in a:
    if key in b:
        a[key] += b[key]
print(a)
res1 = dict(map(lambda x: (x[0], a.get(x[0], '') + b.get(x[0], '')), a.keys())) # with the help of 'map()' function
print(res1)
from collections import defaultdict
# defaultdict -> advanced dictionary type that provides a default value when a missing key is accessed, this prevents KeyError 
res2 = defaultdict(str) 
for key in a:
    res2[key] = a[key] + b.get(key, '')
print(dict(res2))

# Adding elements to the dictionary
a = ['Name', 'Website', 'Topic', 'Founded']
b = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]
res = {}  # initializes an empty dictionary
for i, j in enumerate(a):
    res[j] = b[i]
print(res)
res1 = dict.fromkeys(a)  # Creates a dictionary with keys and default None values
for i, j in enumerate(a):
    res1[j] = b[i]
print(res1)

# Accessing elements in Dictionary 
from itertools import islice
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = dict(islice(d1.items(), 2)) # Getting the first 2 key-value pairs
d2 = {k: v for i, (k, v) in enumerate(d1.items()) if i < 2} # Getting the first 2 key-value pairs using dictionary 
d2 = {}
for i, (k, v) in enumerate(d1.items()):
    if i < 2:
        d2[k] = v
print(d2)  # created a dictionary using loop

# Creating a dictionary using the ast.literal_eval
import ast
a = "{'a': 1, 'b': 2}"
res = ast.literal_eval(a)
print(type(res),res)


# ------------Dictionary Questions----------------
# Count the items of a nested dictionary using manual counting
d = {"product1": {"name": "Laptop", "price": 800, "stock": 15},
    "product2": {"name": "Smartphone", "price": 500, "stock": 30},
    "product3": {"name": "Tablet", "price": 300, "stock": 25}}
cnt = 0
for key, val in d.items():
    if isinstance(val, dict):  # Check if the value is a nested dictionary
        for i in val:
            cnt += 1  # Count each key in the nested dictionary
    else:
        cnt += 1  # Count the top-level keys
print(cnt)

# check whether if the key exists or not -> using 'in' function and 'key' function 
def checkKey(dic, key):
    if key in dic.keys():
        print("Present, and", end =" ")
        print("value is: ", dic[key])
    else:
        print("Not present")
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
d = {'a':'100','b':'200','c':300}
if d.get('b') == None:  #  finding th key using the 'get' function
  print("Not Present")
else:
  print("Present and value is ",d.get('b'))

# Remove keys with substring values
mydct = {'name1': 'hello world', 'name2': 'python code', 'name3': 'world peace'}
substring = 'world'
keys_to_remove = [k for k, v in d.items() if substring in v]
for k in keys_to_remove: # remove the keys using loops
    del mydct[k]

mydct = {k:v for (k,v) in mydct.items() if substring not in v} # Remove keys where values contain the substring
print(mydct)

# Python program to find the sum of all items in a dictionary
d = {'a':100,'b':200,'c':300}
print(sum(d.values()))
res = 0
for v in d.values(): # using the for loop
    res += v
print("The sum of the dictionary item values are: ",res)
print(sum(map(lambda key: d[key], d))) # Using the Map Function

# wap in Python to find the maximum key value of the dictionary 
d = {'Gfg' : 2, 'for' : 1, 'CS' : 2}
max_val = max(d.values())
result = list(filter(lambda x:d[x] == max_val,d)) # using the list and filter command and also lambda function 
print(result)
temp = max(d.values())
res = [key for key in d if d[key] == temp]
print(res)
max_val = max(d.values())
max_keys = []
for key in d:
    if d[key] == max_val:
        max_keys.append(key)
print("The max value is :",max_keys)

# wap in python to remove duplicate values in dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original Dictionary is : "+ str(test_dict))
temp = []
res = dict()
for key,value in test_dict.items(): # remove duplicates like 'for' and 'geeks' using the FOR loop
    if value not in temp:
        temp.append(value)
        res[key] = value
print("The dictionary after values removal : " + str(res))

# wap in python Counting the Frequencies in a List Using Dictionary 
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
b = {}
for c in a:
    if c in b:
        b[c] += 1
    else:
        b[c] = 1
    # b[c] = b.get(c, 0) + 1  # -> if any value not present in the dictionary then the value at each index gtes append to the empty dictionary 
print("The frequency of each elements",b)
x = list(set(a)) # list of unique items set 
c = {item: a.count(item) for item in x} # used  the list comprehension 
print(c)

# Check if two arrays elements are equal or not
a = [1, 2, 5, 4, 0]
b = [1, 2, 5, 4, 0]
if a == b:  # Actually check all the elements of both the array are equal or not and also we can compare the length
    print("array a and array b are equal.")
else:
    print("array a and array b are not equal.")

# wap in python to check max Distance Between Two Occurrences
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Dist = {}
res = 0
for i in range(len(arr)):
    if arr[i] not in Dist:
        Dist[arr[i]] = i # adding the index of the element to the dictionary
# Python dictionary is a data structure that stores the value in key: value pairs. 
# Values in a dictionary can be of any data type and can be duplicated  whereas Keys can be repeated
# Keys in dictionary are IMMUTABLE 
# d = {1:'Geeks',2:'For',3:'Geeks'}
# print(d.__len__) # counts the length of the string  
d1 = dict(a = "Geeks", b = "for", c = "Geeks") # can be created using the 'dict' keyword
print(d1)
print(d[1]) # Access using key and retrieve value from key 
print(d.get(2))  # access value at key 2 using '.get()' function
print(d.keys()) # getting key values using 'key()' function
d["Name"] = "Ankit" # Adding value in dictionary 
d[1] = "Python dict" # updating the value of key 1 to Python dict
del d["Name"] # use to remove any key from the dictionary -> print the dictionary to get updated
val = d.pop(3) # removes and returns the value given at the pop function for any index
print(val)
key, val = d.popitem() # removes and returns the last key-value pair
print(f"Key: {key}, Value: {val}")
print(d) 

# Iterating in Dictionary 
a = {"Name":"Ankit","age":24,"Skill":"GenAI Engineer"}
for key in a: # iterate over key and values simultaneously 
    print(key)
for key,value in a.items(): # 'dict.items()' contains both key value together iteration 
    print(f"{key}:{value}")

# Example fo nested Dictionaries 
new_dictionary = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(new_dictionary)

# copy of a dictionary can be created using either shallow copy or deep copy
# These methods allow duplicating dictionary objects, but they behave differently when it comes to nested data
import copy
original = {'name': 'Alice', 'marks': {'math': 90, 'science': 95}}
shallow = copy.copy(original) # first import then use the copy function 
# shallow['marks']['math'] = 100
print("Original: ",original) # both show updated 'math' value due to shared data.
print("Shallow copy: ",shallow)
print(original is shallow) # prints false bcz it actually points to that dictionary not copies the actual memory address

original1 = {'name': 'Alice', 'marks': {'math': 90, 'science': 95}}
deep =  copy.deepcopy(original1)
deep['marks']['math'] = 100
print("Original: ",original1)
print("Deep copy: ",deep)  # original remains unchanged, only deep copy shows the updated 'math' value due to complete new obj 
print(original1 is deep)

# Dictionary Comprehension
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
mydict = {k:v for (k,v) in zip(keys,values)}
print(mydict)
# creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)
# creation using string comprehension
sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)
# comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)


my_dict1 = {'1':'Geeks','2':'For','3':'Geeks'}
print(my_dict1.get('1'))
print(my_dict1.get('Name')) #  no such key is present due to which the answer is false
print(list(my_dict1.items())[2][2]) # prints 'For' bcz it follows a matrix which tells [x][y]
my_dict1.clear() # used to remove all items of the dictionary along with key and value
print(my_dict1)
d1 = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
d2 = {'Name': 'Neha', 'Age': '22'}
d2.update({"Work": "Software Engineer"}) # Adding a single key-value pair
d1.update(d2)
d1['key3'] = 'Geeks'
d1['key4'] = 'is'
d1['key5'] = 'portal'
print(d1)
d3 = {'key1': 'geeks', 'key2': 'for'}
d3 = dict(d3, key3='Geeks', key4='is', key5='portal', key6='Computer')
print(d3)
print(list(d1.values()))

# Concatenate Dictionary string values
a = {'gfg': 'a', 'is': 'b', 'best': 'c'}
b = {'gfg': 'd', 'is': 'e', 'best': 'f'}
a.setdefault('d', 4) # setdefault() is often used to ensure a key exists in the dictionary. If the key doesn't exist, it adds it with a default value.
a.setdefault('e', 5)
res = {key: a[key] + b.get(key, '') for key in a.keys()}
print(res)
for key in a:
    if key in b:
        a[key] += b[key]
print(a)
res1 = dict(map(lambda x: (x[0], a.get(x[0], '') + b.get(x[0], '')), a.keys())) # with the help of 'map()' function
print(res1)
from collections import defaultdict
# defaultdict -> advanced dictionary type that provides a default value when a missing key is accessed, this prevents KeyError 
res2 = defaultdict(str) 
for key in a:
    res2[key] = a[key] + b.get(key, '')
print(dict(res2))

# Adding elements to the dictionary
a = ['Name', 'Website', 'Topic', 'Founded']
b = ['GeeksforGeeks', 'https://www.geeksforgeeks.org/', 'Programming', 2009]
res = {}  # initializes an empty dictionary
for i, j in enumerate(a):
    res[j] = b[i]
print(res)
res1 = dict.fromkeys(a)  # Creates a dictionary with keys and default None values
for i, j in enumerate(a):
    res1[j] = b[i]
print(res1)

# Accessing elements in Dictionary 
from itertools import islice
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = dict(islice(d1.items(), 2)) # Getting the first 2 key-value pairs
d2 = {k: v for i, (k, v) in enumerate(d1.items()) if i < 2} # Getting the first 2 key-value pairs using dictionary 
d2 = {}
for i, (k, v) in enumerate(d1.items()):
    if i < 2:
        d2[k] = v
print(d2)  # created a dictionary using loop

# Creating a dictionary using the ast.literal_eval
import ast
a = "{'a': 1, 'b': 2}"
res = ast.literal_eval(a)
print(type(res),res)


# ------------Dictionary Questions----------------
# Count the items of a nested dictionary using manual counting
d = {"product1": {"name": "Laptop", "price": 800, "stock": 15},
    "product2": {"name": "Smartphone", "price": 500, "stock": 30},
    "product3": {"name": "Tablet", "price": 300, "stock": 25}}
cnt = 0
for key, val in d.items():
    if isinstance(val, dict):  # Check if the value is a nested dictionary
        for i in val:
            cnt += 1  # Count each key in the nested dictionary
    else:
        cnt += 1  # Count the top-level keys
print(cnt)

# check whether if the key exists or not -> using 'in' function and 'key' function 
def checkKey(dic, key):
    if key in dic.keys():
        print("Present, and", end =" ")
        print("value is: ", dic[key])
    else:
        print("Not present")
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)
d = {'a':'100','b':'200','c':300}
if d.get('b') == None:  #  finding th key using the 'get' function
  print("Not Present")
else:
  print("Present and value is ",d.get('b'))

# Remove keys with substring values
mydct = {'name1': 'hello world', 'name2': 'python code', 'name3': 'world peace'}
substring = 'world'
keys_to_remove = [k for k, v in d.items() if substring in v]
for k in keys_to_remove: # remove the keys using loops
    del mydct[k]

mydct = {k:v for (k,v) in mydct.items() if substring not in v} # Remove keys where values contain the substring
print(mydct)

# Python program to find the sum of all items in a dictionary
d = {'a':100,'b':200,'c':300}
print(sum(d.values()))
res = 0
for v in d.values(): # using the for loop
    res += v
print("The sum of the dictionary item values are: ",res)
print(sum(map(lambda key: d[key], d))) # Using the Map Function

# wap in Python to find the maximum key value of the dictionary 
d = {'Gfg' : 2, 'for' : 1, 'CS' : 2}
max_val = max(d.values())
result = list(filter(lambda x:d[x] == max_val,d)) # using the list and filter command and also lambda function 
print(result)
temp = max(d.values())
res = [key for key in d if d[key] == temp]
print(res)
max_val = max(d.values())
max_keys = []
for key in d:
    if d[key] == max_val:
        max_keys.append(key)
print("The max value is :",max_keys)

# wap in python to remove duplicate values in dictionary
test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
print("The original Dictionary is : "+ str(test_dict))
temp = []
res = dict()
for key,value in test_dict.items(): # remove duplicates like 'for' and 'geeks' using the FOR loop
    if value not in temp:
        temp.append(value)
        res[key] = value
print("The dictionary after values removal : " + str(res))

# wap in python Counting the Frequencies in a List Using Dictionary 
a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
b = {}
for c in a:
    if c in b:
        b[c] += 1
    else:
        b[c] = 1
    # b[c] = b.get(c, 0) + 1  # -> if any value not present in the dictionary then the value at each index gtes append to the empty dictionary 
print("The frequency of each elements",b)
x = list(set(a)) # list of unique items set 
c = {item: a.count(item) for item in x} # used  the list comprehension 
print(c)

# Check if two arrays elements are equal or not
a = [1, 2, 5, 4, 0]
b = [1, 2, 5, 4, 0]
if a == b:  # Actually check all the elements of both the array are equal or not and also we can compare the length
    print("array a and array b are equal.")
else:
    print("array a and array b are not equal.")

# wap in python to check max Distance Between Two Occurrences
arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Dist = {}
res = 0
for i in range(len(arr)):
    if arr[i] not in Dist:
        Dist[arr[i]] = i # adding the index of the element to the dictionary