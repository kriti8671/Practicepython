import matplotlib.pyplot as plt
import lineplot
import random


# Example Data: Each (x, y) pair represents a communication attempt (round, vehicle ID)
communication_attempts = [(round_num, vehicle_id) for round_num in range(
    lineplot.num_rounds) for vehicle_id in range(lineplot.num_vehicles)]
message_loss = [(round_num, vehicle_id) for round_num in range(lineplot.num_rounds)
                for vehicle_id in range(lineplot.num_vehicles) if random.random() < 0.1]  # 10% message loss

# Plotting successful communications
x_success, y_success = zip(*communication_attempts)
plt.scatter(x_success, y_success, color='blue',
            label='Successful Communication')

# Plotting message loss events
x_loss, y_loss = zip(*message_loss)
plt.scatter(x_loss, y_loss, color='red', label='Message Loss')

plt.xlabel('Round')
plt.ylabel('Vehicle ID')
plt.title('Communication Events and Message Loss')
plt.legend()
plt.show()
