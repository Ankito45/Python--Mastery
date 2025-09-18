<<<<<<< HEAD
# Array in python -> collection of items of the same,mutable,indexed and allows duplicates 
# But while considering the array in python we use the list data type but actually to use the properties of the 
# complete array we use the numpy array module in python
import numpy as np
arr = np.array([1,2,3,4,5])
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr*2) # the value of each element in the array is multiplied by 2 but in list the complete list is repeated twice
print(arr_1)
print(arr_1.shape) # gives the shape of the array like -> 2 X 3 matrix, 4 X 4 matrix
print(arr_1.ndim) # gives the dimension of the array like -> 1D,2D,3D
print(arr[3]) # accessing the elements of the array
np.append(arr,6) # appending the element to the array
print(arr)
print(arr[:3]) # slicing the array
arr[4] = 10 # modifying the element of the array
print(len(arr)) # gives the length of the array
print(*arr) # printing the elements of the array without the square brackets


# ---------------Arrays Practice Programs-----------------
# wap in python to find the second largest element in an array
arr = np.array([1,2,3,4,5])
arr = np.sort(arr) # sorting the array in ascending order
print(f"The second largest element in the array is : {arr[-2]}")

# wap in python to find the maximum product of a triplet in an array
arr1 = np.array([10, 3, 5, 6, 20])
arr1 = np.sort(arr1)
max_product = max(arr1[0] * arr[1] * arr[2],arr1[-1] * arr1[-2] * arr1[-3])
print(f"The maximum product of a triplet in the array is : {max_product}")

# wap in python to Reverse an Array in groups of given size
import numpy as np
arr2 = np.array([1,2,3,4,5,6,7,8])
k = 3
n = len(arr2)
i = 0 
while i < n:
    left = i
    right = min(i+k-1,n-1)
    while left < right:
        arr2[left],arr2[right] = arr2[right],arr2[left] # swapping the elements
        left += 1
        right -= 1
    i += k
print(f"The array after reversing in groups of size {k} is : {arr2}")

# wap to left rotate the array by d positions by rotating one element at a time
def rotateArr(arr, d):
    n = len(arr)
    for i in range(d):
        first = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first 

arr = [1,2,3,4,5,6,7]
d = 3
rotateArr(arr,d)
for i in range(len(arr)):
        print(arr[i], end=" ")

# wap in python top find leader in array
import numpy as np
arr3 = np.array([16,17,4,3,5,2])
n = len(arr3)
result = []
for i in range(n):
     for j in range(i+1,n):
        if arr3[i] <= arr3[j]:
            break
        else:
            if j == n-1:
                result.append(arr3[i])
print(f"The leaders in the array are : {result}")

# wap in python to find the missing and repeating number in an array
import numpy as np
arr4 = np.array([3,1,3,5,4])
n = len(arr4)
seen = set()
repeat = 0
for x in arr4:
    if x in seen:
        repeating = x
    seen.add(x)
missing = sum(range(1, n+1)) - (sum(arr4) - repeat)
print(f"The missing number is : {missing} and the repeating number is : {repeating}")

# wap in python to find the missing ranges of an array
import numpy as np
arr5 = np.array([14, 15, 20, 30, 31, 45])
lower = 10
upper = 50
missing_ranges = []
n = len(arr5)
if arr5[0] > lower:
    missing_ranges.append((lower, arr5[0]-1 if (arr5[0]-1) > lower else lower))
for i in range(n-1):
    if arr5[i+1] > arr5[i] + 1:
        missing_ranges.append((arr5[i]+1, arr5[i+1]-1 if arr5[i+1]-1 > arr5[i]+1 else arr5[i]+1))
if arr5[-1] < upper:
    missing_ranges.append((arr5[-1]+1, upper if arr5[-1]+1 < upper else upper))
print(f"The missing ranges in the array are : {missing_ranges}")

# wap to find the majority element in an array
import numpy as np
arr0 = np.array([3,3,4,2,4,4,2,4,4])
n = len(arr0)
major_element = None
max_count = 0
for i in range(n):
    count = 0
    for j in range(n):
        if arr0[i] == arr0[j]:
            count += 1
    if count > n // 2:
        major_element = arr0[i]
        max_count = count
        break  # since only one majority element can exist
if major_element is not None:
    print(f"The majority element in the array is : {major_element}, repeated {max_count} times")
else:
    print("No majority element found in the array")

# wap to find the maximum subarray sum using kadane's algorithm
import numpy as np
arr6 = np.array([-2,1,-3,4,-1,2,1,-5,4])
n = len(arr6)
result = arr6[0]
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += arr6[j]
        result = max(result,sum)
print(f"The maximum subarray sum is : {result}")

# wap to find the maximum subarray product
import numpy as np
arr7 = np.array([-2, 6, -3, -10, 0, 2])
n = len(arr7)
result1 = arr7[0]
for i in range(n):
    prod = 1
    for j in range(i,n):
        prod *= arr7[j]
        result1 = max(result1,prod)
print(f"The maximum product subarray is : {result1}")

# wap to check whether a number is prime or not 
import math
def checkprime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
n = int(input())
for i in range(n):
    if checkprime(i):
        print(i)
=======
# Array in python -> collection of items of the same,mutable,indexed and allows duplicates 
# But while considering the array in python we use the list data type but actually to use the properties of the 
# complete array we use the numpy array module in python
import numpy as np
arr = np.array([1,2,3,4,5])
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr*2) # the value of each element in the array is multiplied by 2 but in list the complete list is repeated twice
print(arr_1)
print(arr_1.shape) # gives the shape of the array like -> 2 X 3 matrix, 4 X 4 matrix
print(arr_1.ndim) # gives the dimension of the array like -> 1D,2D,3D
print(arr[3]) # accessing the elements of the array
np.append(arr,6) # appending the element to the array
print(arr)
print(arr[:3]) # slicing the array
arr[4] = 10 # modifying the element of the array
print(len(arr)) # gives the length of the array
print(*arr) # printing the elements of the array without the square brackets


# ---------------Arrays Practice Programs-----------------
# wap in python to find the second largest element in an array
arr = np.array([1,2,3,4,5])
arr = np.sort(arr) # sorting the array in ascending order
print(f"The second largest element in the array is : {arr[-2]}")

# wap in python to find the maximum product of a triplet in an array
arr1 = np.array([10, 3, 5, 6, 20])
arr1 = np.sort(arr1)
max_product = max(arr1[0] * arr[1] * arr[2],arr1[-1] * arr1[-2] * arr1[-3])
print(f"The maximum product of a triplet in the array is : {max_product}")

# wap in python to Reverse an Array in groups of given size
import numpy as np
arr2 = np.array([1,2,3,4,5,6,7,8])
k = 3
n = len(arr2)
i = 0 
while i < n:
    left = i
    right = min(i+k-1,n-1)
    while left < right:
        arr2[left],arr2[right] = arr2[right],arr2[left] # swapping the elements
        left += 1
        right -= 1
    i += k
print(f"The array after reversing in groups of size {k} is : {arr2}")

# wap to left rotate the array by d positions by rotating one element at a time
def rotateArr(arr, d):
    n = len(arr)
    for i in range(d):
        first = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first 

arr = [1,2,3,4,5,6,7]
d = 3
rotateArr(arr,d)
for i in range(len(arr)):
        print(arr[i], end=" ")

# wap in python top find leader in array
import numpy as np
arr3 = np.array([16,17,4,3,5,2])
n = len(arr3)
result = []
for i in range(n):
     for j in range(i+1,n):
        if arr3[i] <= arr3[j]:
            break
        else:
            if j == n-1:
                result.append(arr3[i])
print(f"The leaders in the array are : {result}")

# wap in python to find the missing and repeating number in an array
import numpy as np
arr4 = np.array([3,1,3,5,4])
n = len(arr4)
seen = set()
repeat = 0
for x in arr4:
    if x in seen:
        repeating = x
    seen.add(x)
missing = sum(range(1, n+1)) - (sum(arr4) - repeat)
print(f"The missing number is : {missing} and the repeating number is : {repeating}")

# wap in python to find the missing ranges of an array
import numpy as np
arr5 = np.array([14, 15, 20, 30, 31, 45])
lower = 10
upper = 50
missing_ranges = []
n = len(arr5)
if arr5[0] > lower:
    missing_ranges.append((lower, arr5[0]-1 if (arr5[0]-1) > lower else lower))
for i in range(n-1):
    if arr5[i+1] > arr5[i] + 1:
        missing_ranges.append((arr5[i]+1, arr5[i+1]-1 if arr5[i+1]-1 > arr5[i]+1 else arr5[i]+1))
if arr5[-1] < upper:
    missing_ranges.append((arr5[-1]+1, upper if arr5[-1]+1 < upper else upper))
print(f"The missing ranges in the array are : {missing_ranges}")

# wap to find the majority element in an array
import numpy as np
arr0 = np.array([3,3,4,2,4,4,2,4,4])
n = len(arr0)
major_element = None
max_count = 0
for i in range(n):
    count = 0
    for j in range(n):
        if arr0[i] == arr0[j]:
            count += 1
    if count > n // 2:
        major_element = arr0[i]
        max_count = count
        break  # since only one majority element can exist
if major_element is not None:
    print(f"The majority element in the array is : {major_element}, repeated {max_count} times")
else:
    print("No majority element found in the array")

# wap to find the maximum subarray sum using kadane's algorithm
import numpy as np
arr6 = np.array([-2,1,-3,4,-1,2,1,-5,4])
n = len(arr6)
result = arr6[0]
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += arr6[j]
        result = max(result,sum)
print(f"The maximum subarray sum is : {result}")

# wap to find the maximum subarray product
import numpy as np
arr7 = np.array([-2, 6, -3, -10, 0, 2])
n = len(arr7)
result1 = arr7[0]
for i in range(n):
    prod = 1
    for j in range(i,n):
        prod *= arr7[j]
        result1 = max(result1,prod)
print(f"The maximum product subarray is : {result1}")

# wap to check whether a number is prime or not 
import math
def checkprime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
n = int(input())
for i in range(n):
    if checkprime(i):
        print(i)
>>>>>>> d5a4f36590f1dec64f6b24f7307b0aa4ccb2ff03
