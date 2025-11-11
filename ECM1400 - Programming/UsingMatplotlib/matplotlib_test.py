# Import NumPy to generate the values
import numpy as np

# Import Matplotlib to visualise the data
# The functions we require live in the PyPlot submodule
import matplotlib.pyplot as plt


# 100 values between 0 and 10
x = np.linspace(0, 10, 100)

# Generate some noisy values for the sine function
# Method:
#    - Generate sine values
#    - For each value, add a random offset between -0.5 and 0.5 
y_rand = np.sin(x) + np.random.rand(100) - 0.5

# Generate exact values for the sine function
y = np.sin(x)


# Plot a line graph of the sine function
# Style Format:
#    - "--" means dashed line
#    - "g" means green line
plt.plot(x, y, "--g")

# Plot a scatter graph of the noisy sine values
plt.scatter(x, y_rand, marker="x")

# Change the axes limits
plt.xlim(0,10)
plt.ylim(-1.6,1.6)

# Set the title of the graph
plt.title("Sine Graph")

# Set the axes labels
plt.xlabel("x")
plt.ylabel("y = sin(x)")

# Display a grid in the background
plt.grid(True)

# Save the figure to a SVG file
plt.savefig("figure.svg")