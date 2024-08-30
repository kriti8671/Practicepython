import numpy as np

rounds = [2, 3, 4, 2, 5, 3, 6, 2, 4, 7, 3, 8, 9, 4, 3, 10, 2, 5]

# Calculate the 99th percentile
percentile_99 = np.percentile(rounds, 90)

print(f"The 99th percentile is: {percentile_99}")
