# Numpy helps --> Creating and manipulating arrays,Performing element-wise and matrix operations.
#         --> Generating random numbers and statistical calculations,Conducting linear algebra operations.
#         --> Working with Fourier transformations,Handling missing values efficiently in datasets.
# NumPy arrays are homogeneous, meaning all elements must be the same type, allowing efficient computation.
# Vectorized operations in NumPy can be 10 to 100 times faster than equivalent Python loops.

# numpy.around(arr, decimals = 0, out = None): Helps user to evenly round array elements to a agiven number of decimals
import numpy as np
array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : ", array)
round_off_values = np.around(array)
print ("Rounded values : ", round_off_values)

# --------- All Built in Method for Mathematical calculations in Numpy Array-----------------
# rint()	Round to nearest integer towards zero.
# fix()	Round to nearest integer towards zero.
# floor()	Return the floor of the input, element-wise.
# ceil()	Return the ceiling of the input, element-wise.
# trunc()	Return the truncated value of the input, element-wise.
# log2()	Base-2 logarithm of x.
# mod()	Return the element-wise remainder of division.
# remainder()	Return element-wise remainder of division.
# divmod()	Return element-wise quotient and remainder simultaneously.
# square() Return the element-wise square of the input.

# ------Matrix Manipulation----
import numpy 
x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]]) 
print (numpy.add(x,y)) # this will add the matrix sum 
print(numpy.subtract(x,y)) # this is for the subtraction of elements in matrix
print (numpy.divide(x,y)) # this is for the division of elements inmatrix
print (numpy.multiply(x,y)) # This is for the multiplication of matrix elements wise
print (numpy.dot(x,y)) # this method is used to compute the matrix multiplication, rather than element wise multiplication. 
print (numpy.sum(y,axis=0)) # this method prints the sum of matrix columns wise
print(numpy.sum(y,axis=1)) # this method is used to prints the sum of rows wise

# A straight-forward using (np.linalg.det) way to calulate the the determinant of the matrix using the-built in method of numpy 
A = np.array([[1,2],[3,4]])
print(np.linalg.det(A)) 

# The inverse of a matrix is like the reciprocal of a number.
# (np.linalg.inv) is a Built-in method for finding the inverse of the matrix
M = np.array([[6,1,-1],[4,-2,5],[2,8,7]])
print(np.linalg.inv(M))
# Av=λv the equation to calculate the eigen vectors and eigen values
# A is the matrix, v is associated eigenvector, λ is scalar eigenvalue

# ----------Random Number Generation and Statistics-----------
# numpy.random.randint() is one of the function for doing random sampling in numpy.
# -> returns an array of specified shape and fills it with random integers from low (inclusive) to high (exclusive),
# low : [int] Lowest (signed) integer to be drawn from the distribution.But, it works as a highest integer in the sample if high=None. 
# high : [int, optional] Largest (signed) integer to be drawn from the distribution.
# size   :  [int or tuple of ints, optional] Output shape.
print(numpy.random.randint(low=0,high=3,size=5))
print(numpy.random.randint(2, 10, (2, 3, 4)))

# Normal Distribution also known as the Gaussian Distribution is one of the most important distributions in statistics and data science. 
# Python's NumPy library we can generate random numbers following a Normal Distribution using the numpy.random.normal() method.
# loc -> Specifies the center (mean) of the distribution, where the peak of the bell curve exists.
# scale -> Determines the spread (standard deviation) of the distribution controlling how flat or narrow the graph is.
# size -> Defines the shape of the returned array.
print(np.random.normal())
print(np.random.normal(size=5)) # Array of random numbers using the normal distribution
# Visualization the normal Distribution 
import matplotlib.pyplot as plt
from scipy.stats import norm 
data = np.random.normal(loc=0, scale=1, size=1000)  # mean=0, std=1
plt.hist(data, bins=30, edgecolor='black', density=True)
x = np.linspace(min(data), max(data), 100)
pdf = norm.pdf(x, loc=0, scale=1)   # Probability Density Function
plt.plot(x, pdf, color='red', label='Theoretical PDF')
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()


# numpy.random.binomial() method generates random numbers that follow a Binomial Distribution.
# n : The number of trials (e.g., number of coin flips).
# p : The probability of success in each trial (e.g., probability of getting heads in a coin flip).
# size : The shape of the returned array.
print(np.random.binomial(n=10, p=0.5)) 
print(np.random.binomial(n=10, p=0.5, size=5)) # generating the array of numbers
# Visualization of the Binomial Distribution 
from scipy.stats import binom
n = 10  
p = 0.5  
size = 1000  
data = np.random.binomial(n=n, p=p, size=size)
plt.hist(data, bins=np.arange(-0.5, n+1.5, 1), density=True, edgecolor='black', alpha=0.7, label='Histogram')
x = np.arange(0, n+1)  
pmf = binom.pmf(x, n=n, p=p)  
plt.scatter(x, pmf, color='red', label='Theoretical PMF')
plt.vlines(x, 0, pmf, colors='red', linestyles='dashed')  
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)
plt.show()


# Poisson Distribution model the number of times an event happens within a fixed time or space when we know the average number of occurrences
# Python'sNumPylibrary we can generate random numbers following a Poisson Distribution using the numpy.random.poisson()
# lam -> The average number of events (λ) expected to occur in the interval.
# size -> The shape of the returned array.
print(np.random.poisson(lam=5))
print(np.random.poisson(lam=5, size=5)) # Generate an Array of Random Numbers
# Visualizing the Poisson Distribution
import seaborn as sns
from scipy.stats import poisson
lam = 2  
size = 1000  
data = np.random.poisson(lam=lam, size=size)
sns.displot(data, kde=False, bins=np.arange(-0.5, max(data)+1.5, 1), color='skyblue', edgecolor='black')
plt.title(f"Poisson Distribution (λ={lam})")
plt.xlabel("Number of Events")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Python's NumPy library you can generate random numbers following a Uniform Distribution using the numpy.random.uniform() method.
# low : The lower bound of the range (inclusive). Default is 0.0.
# high : The upper bound of the range (exclusive). Default is 1.0.
# size : The shape of the returned array.
print(np.random.uniform(size = 5))
# Visualizing the Uniform Distribution
low = 10  
high = 20  
size = 1000  
data = np.random.uniform(low=low, high=high, size=size)
sns.histplot(data, bins=30, kde=False, color='skyblue', edgecolor='black')
plt.title(f"Uniform Distribution (Range: {low} to {high})")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Exponential Distribution describe the time between events in a Poisson process where events occur continuously and independently at a constant average rate.
# numpy.random.exponential() method can actually help for generating random number 
print(np.random.exponential(size = 5))
# Visualization of the Exponential Distribution
scale = 2  
size = 1000  
data = np.random.exponential(scale=scale, size=size)
sns.histplot(data, bins=30, kde=True, color='orange', edgecolor='black')
plt.title(f"Exponential Distribution (Scale={scale})")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Chi-Square Distribution  used in statistics when we add up the squares of independent random numbers that follow a standard normal distribution
# Use the numpy.random.chisquare() function to generate random numbers that follow Chi-Square Distribution
# df -> Degrees of freedom (denoted by k) which affects the shape of the distribution.
# size -> The number of random numbers you want to generate or the shape of the returned array.
print(np.random.chisquare(df=2,size=5))
# Visualization of Chi-Square Distribution
df = 1  
size = 1000  
data = np.random.chisquare(df=df, size=size)
sns.displot(data, kind="kde", color='purple', label=f'Chi-Square (df={df})')
plt.title(f"Chi-Square Distribution (df={df})")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.show()