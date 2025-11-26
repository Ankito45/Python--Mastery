# string is a sequence of characters.
s = "Geeks ForGeeks"
print(s[1]) # access the 2nd Character 
print(s[-10]) # access the 10th Character from end
s1 = s + s[0] # updating a new string 
print(s1)
s2 = "Geeks ForGeeks"
print(s is s2) # check if both strings are the same object
print('G' in s) # check if 'G' or any substring (specified) is present in the string
print(s == s2) # check if both strings are equal
print(s[1:4]) # slicing the string from index 1 to 3
print(s[1:]) # slicing the string from index 1 to end
print(s[:4]) # slicing the string from start to index 3
print(s[::-1]) # reversing the string
print(s[:-1]) # slicing the string from start to second last character
print(s[:-10]) # slicing the string from start to 10th character from end 
print(len(s)) # getting the length of the string
print(s.count('e')) # counting occurrences of 'e' in the string
print(s.upper()) # converting the string to uppercase
print(s.lower()) # converting the string to lowercase
print(s.capitalize()) # capitalizing the first character of the string
print("hello world".title()) # capitalizing the first character of each word in the string
print(s.find('For')) # finding the first occurrence of 'e' in the string nad gives its index
print(s.join(['a', 'b'])) # joining the string with a list of strings
print(s.__len__()) # getting the length of the string

# STRING IMMUTABILITY
# it is not possible to delete individual characters from a string since strings are immutable.
s2 = "GeeksForGeeks"
print(s2.rstrip('s').split('s')) # removing trailing 's' and splitting the string by 's'
# s2[0] = 'g' # trying to change the first character will raise an error
s2 = 'g' +s2[1:] # creating a new string with the first character changed
# s2 = s2 + 's' # appending 's' to the end of the string
s2 = s2.replace('Geeks', 'hello') # replacing 'Geeks' with 'hello'
print(s2)
print(s2.__contains__('F')) # checks whether a string contain that char or not 

# The use of f-strings for formatting strings using curly braces
name = "Ankit"
age = 25
print(f"My name is {name} and I am {age} years old.") # formatted using f-string
print("My name is {} and I am {} years old.".format("Alice", 22))

# string is a sequence of characters.

s = "Geeks ForGeeks"
print(s[1]) # access the 2nd Character 
print(s[-10]) # access the 10th Character from end
s1 = s + s[0] # updating a new string 
print(s1)
s2 = "GeeksForGeeks"
print(s is s2) # check if both strings are the same object
print('G' in s) # check if 'G' or any substring (specified) is present in the string
print(s == s2) # check if both strings are equal and have the same contents
print(s[1:4]) # slicing the string from index 1 to 3
print(s[1:]) # slicing the string from index 1 to end
print(s[:4]) # slicing the string from start to index 3
print(s[::-1]) # reversing the string
print(s[:-1]) # slicing the string from start to second last character
print(s[:-10]) # slicing the string from start to 10th character from end 
print(len(s)) # getting the length of the string
print(s.count('e')) # counting occurrences of 'e' in the string
print(s.upper()) # converting the string to uppercase
print(s.lower()) # converting the string to lowercase
print(s.capitalize()) # capitalizing the first character of the string
print("hello world".title()) # capitalizing the first character of each word in the string
print(s.find('For')) # finding the first occurrence of 'e' in the string nad gives its index
print(s.join(['a', 'b'])) # joining the string with a list of strings
print(s.__len__()) # getting the length of the string

# STRING IMMUTABILITY
# it is not possible to delete individual characters from a string since strings are immutable.
s2 = "GeeksForGeeks"
print(s2.rstrip('s').split('s')) # removing trailing 's' and splitting the string by 's'
# s2[0] = 'g' # trying to change the first character will raise an error
s2 = 'g' +s2[1:] # creating a new string with the first character changed
# s2 = s2 + 's' # appending 's' to the end of the string
s2 = s2.replace('Geeks', 'hello') # replacing 'Geeks' with 'hello'
print(s2)
print(s2.__contains__('F')) # checks whether a string contain that char or not 

# The use of f-strings for formatting strings using curly braces
name = "Ankit"
age = 25
print(f"My name is {name} and I am {age} years old.") # formatted using f-string
print("My name is {} and I am {} years old.".format("Alice", 22))

