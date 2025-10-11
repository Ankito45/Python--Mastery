# Matplotlib is an open-source visualization library for the Python programming language, widely used for creating static, animated and interactive plots.
# Matplotlib Pyplot: The pyplot module is a collection of functions that make Matplotlib work like MATLAB, providing a simple interface for creating plots.
# Figure and Axes: In Matplotlib, figures represent the overall container, while axes refer to the individual plots within a figure.
# Integration with Pandas: Matplotlib works seamlessly with Pandas DataFrames, enabling efficient data visualization.
# Pyplot is a module within Matplotlib that provides a MATLAB-like interface for making plots.
import matplotlib.pyplot as plt
import numpy as np
# Created a Simple Line Graph   with error points
x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]
y_error = 0.2 # Created error for y-value
x_error = 0.5 # Created error for x-value
plt.plot(x, y)
plt.errorbar(x, y,yerr = y_error,fmt ='o') # Adding error values to y-values
plt.errorbar(x, y,xerr = x_error,fmt ='o') # Adding error values to x-values
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.title("Error Graph")
plt.show()

# Add titles, labels, and other elements using methods like plt.title() - for title, plt.xlabel() -  for x-axis, and plt.ylabel() - for y-axis.
x1 = [0, 2, 4, 6, 8]
y1 = [0, 4, 16, 36, 64]
fig, ax = plt.subplots()
plt.plot(x1, y1, marker='o', label="Data Points")
plt.title("Basic Components of Matplotlib Figure")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.legend()
plt.show()

# illustrating how error bars can be used in different contexts to represent data with varying degrees of precision.
a = np.arange(10)/10 # defining our function 
b = (a + 0.1)**2
b_error = np.linspace(0.05, 0.2, 10) # defining our error 
plt.plot(a,b,marker='o',label="Error Points")
plt.errorbar(a, b, yerr = b_error, fmt ='o')
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.title("Complex Error Graph")
plt.legend()
plt.show()

# Graph to print the line Chart
# ax = np.array([1, 2, 3, 4])  # X-axis 
# ay = ax*2  # Y-axis
# plt.plot(ax, ay)  
# plt.xlabel("X-axis")     # Label for the X-axis
# plt.ylabel("Y-axis")     # Label for the Y-axis
# plt.title("Line Graph")  # Chart title
# plt.show() 

# Line chart with Annotations
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-')
# Add annotations
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')
plt.title('Line Chart with Annotations')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()

# Fil area between two lines and also plotting multiple line Charts
c = np.array([1, 2, 3, 4])
d = c*2
plt.plot(c, d)
c1 = [2, 4, 6, 8]
d1 = [3, 5, 7, 9]
plt.plot(c, d1, '-.')
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('Multiple plots with fill_between')
plt.fill_between(c, d, d1, color='red', alpha=0.5)
plt.show()

# Creating a simple Bar Graph 
# Bar plots/Graph are significant because they provide a clear and intuitive way to visualize categorical data.
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates']
sales = [400, 350, 300, 450]
# color -> is used to give the Bar colors
# width -> uised to give the size of the Bar
plt.bar(fruits, sales,color='Violet', width=0.4,label="fruits") # For plotting the graph in vertical Manner
# plt.barh(fruits, sales,color='Violet') # barh -> used For plotting the graph in Horizontal manner
plt.title('Fruit Sales')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.show()

# Multiple Plotting of Bar Chart
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8)) 
IT = [12, 30, 1, 8, 22] 
ECE = [28, 6, 16, 5, 10] 
CSE = [29, 3, 24, 25, 17] 
br1 = np.arange(len(IT)) 
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2] 
# barwidth -> the width of the bar 
# edgecolour -> outer color of the bar
# label -> text under the bar
plt.bar(br1, IT, color ='r', width = barWidth, edgecolor ='black', label ='IT') 
plt.bar(br2, ECE, color ='g', width = barWidth, edgecolor ='black', label ='ECE') 
plt.bar(br3, CSE, color ='b', width = barWidth, edgecolor ='black', label ='CSE') 
plt.xlabel('Branch', fontweight ='bold', fontsize = 15) 
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15) 
plt.xticks([r + barWidth for r in range(len(IT))], 
        ['2015', '2016', '2017', '2018', '2019'])
plt.legend()
plt.show()

# Stacked bar Graph -> a graph that uses bars to represent data, where each bar is divided into segments that stack on top of each other to show the cumulative total of different categories.
# Stacked bar graphs are useful for comparing the total values across categories while also showing the contribution of each sub-category to the total.
boys = (20, 35, 30, 35, 27)
girls = (25, 32, 34, 20, 25)
boyStd = (2, 3, 4, 1, 2)
girlStd = (3, 5, 2, 3, 3)
ind = np.arange(5)   
width = 0.35  
fig = plt.subplots(figsize =(10, 7))
p1 = plt.bar(ind, boys, width, yerr = boyStd)
p2 = plt.bar(ind, girls, width, bottom = boys, yerr = girlStd)
plt.ylabel('Contribution')
plt.title('Contribution by the teams .. Stacked Graph')
plt.xticks(ind, ('T1', 'T2', 'T3', 'T4', 'T5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('boys', 'girls'))
plt.show()
