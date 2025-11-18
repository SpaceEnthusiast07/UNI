# Set up
import matplotlib.pyplot as plt
import numpy as np

# Basic Plots
# Line Plots
x = np.arange(0,10)
y = np.sin(x)

plt.plot(x,y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig('line_plot_example.svg')

