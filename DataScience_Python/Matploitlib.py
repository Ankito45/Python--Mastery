# Matplotlib is an open-source visualization library for the Python programming language, widely used for creating static, animated and interactive plots.
# Matplotlib Pyplot: The pyplot module is a collection of functions that make Matplotlib work like MATLAB, providing a simple interface for creating plots.
# Figure and Axes: In Matplotlib, figures represent the overall container, while axes refer to the individual plots within a figure.
# Integration with Pandas: Matplotlib works seamlessly with Pandas DataFrames, enabling efficient data visualization.
# Pyplot is a module within Matplotlib that provides a MATLAB-like interface for making plots.
import matplotlib.pyplot as plt
# x = [0, 1, 2, 3, 4]
# y = [0, 1, 4, 9, 16]
# plt.plot(x, y)
# plt.show()
# Customize Plot: Add titles, labels, and other elements using methods like plt.title(), plt.xlabel(), and plt.ylabel().
x = [0, 2, 4, 6, 8]
y = [0, 4, 16, 36, 64]
fig, ax = plt.subplots()  
ax.plot(x, y, marker='o', label="Data Points")
ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis") 
ax.set_ylabel("Y-Axis")  
plt.show()