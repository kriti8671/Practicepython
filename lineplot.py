import matplotlib.pyplot as plt
import random

# Example Data: Simulated states of 10 vehicles over 10 rounds
num_vehicles = 10
num_rounds = 10
states_over_time = [[random.random() for _ in range(num_rounds)]
                    for _ in range(num_vehicles)]

# Plotting the state of each vehicle over time
for i in range(num_vehicles):
    plt.plot(states_over_time[i], label=f'Vehicle {i}')

plt.xlabel('Round')
plt.ylabel('State')
plt.title('Fig-1 Vehicle States Over Time')
plt.legend()
plt.show()
