import matplotlib.pyplot as plt
import random


num_vehicles = 10
num_rounds = 10

# Example Data: Final states of vehicles after simulation
final_states = [random.random() for _ in range(num_vehicles)]

# Plotting the histogram of final states
plt.hist(final_states, bins=5, color='skyblue', edgecolor='black')

plt.xlabel('State')
plt.ylabel('Frequency')
plt.title('Distribution of Vehicle States After Simulation')
plt.show()
