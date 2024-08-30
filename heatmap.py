import matplotlib.pyplot as plt
import numpy as np
import lineplot

# Example Data: Simulating message loss pattern over rounds and vehicles
message_loss_pattern = np.random.choice([0, 1], size=(
    lineplot.num_vehicles, lineplot.num_rounds), p=[0.9, 0.1])  # 10% message loss

# Plotting the heatmap
plt.imshow(message_loss_pattern, cmap='hot', interpolation='nearest')

plt.xlabel('Round')
plt.ylabel('Vehicle ID')
plt.title('Message Loss Pattern Over Time')
plt.colorbar(label='Message Loss (1 = Lost, 0 = Received)')
plt.show()


# git add .
# git commit -m "Your commit message here"
# git push
