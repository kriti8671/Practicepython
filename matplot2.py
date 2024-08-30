import matplotlib.pyplot as plt
import numpy as np


# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creating a simple line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='--', marker='o')

# Customizing the plot
plt.title('Simple Sine Wave Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)

# Displaying the plot
plt.show()
