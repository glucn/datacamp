########################################################
# Making multiple updates to weights
# See exercise05.md
#
# Preload
import numpy as np
import matplotlib.pyplot as plt

from preload import get_slope, get_mse

input_data = np.array([1, 2, 3])
weights = np.array([0, 2, 1])
target = 0
########################################################

n_updates = 20
mse_hist = []

# Iterate over the number of updates
for i in range(n_updates):
    # Calculate the slope: slope
    slope = get_slope(input_data, target, weights)

    # Update the weights: weights
    weights = weights - slope * 0.01

    # Calculate mse with new weights: mse
    mse = get_mse(input_data, target, weights)

    # Append the mse to mse_hist
    mse_hist.append(mse)

# Plot the mse history
plt.plot(mse_hist)
plt.xlabel('Iterations')
plt.ylabel('Mean Squared Error')
plt.show()
