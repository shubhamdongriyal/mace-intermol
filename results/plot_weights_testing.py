import numpy as np
import matplotlib.pyplot as plt

# painfull to load the data
# Manually defined data
weights = [
    '100:0:1',
    '100:10:1',
    '100:20:1',
    '100:50:1',
    '100:100:1',
    '100:200:1',
    '100:500:1',
    '100:1000:1'
]

rmse_total_forces = [10.5, 13.9, 14.6, 15.7, 21.8, 24.3, 26.2, 34.8]
rmse_intermol =     [28.4, 24.7, 26.4, 30.6, 31.4, 29.2, 31.6, 28.1]
rmse_energy =       [1.6,  1.6,  1.6,  1.6,  1.6,  1.6,  1.6,  1.8]

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 4), sharex=True)

# Plot RMSE_total_forces
axs[0].plot(weights, rmse_total_forces, marker='o', color='tab:blue')
axs[0].set_title('RMSE Total Forces')
axs[0].set_ylabel('RMSE')
axs[0].set_xlabel('Weights (F:Intermol:E)')
axs[0].tick_params(axis='x', rotation=45)

# Plot RMSE_intermol
axs[1].plot(weights, rmse_intermol, marker='o', color='tab:orange')
axs[1].set_title('RMSE Intermol Forces')
axs[1].set_xlabel('Weights (F:Intermol:E)')
axs[1].tick_params(axis='x', rotation=45)

# Plot RMSE_energy
axs[2].plot(weights, rmse_energy, marker='o', color='tab:green')
axs[2].set_title('RMSE Energy')
axs[2].set_xlabel('Weights (F:Intermol:E)')
axs[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('weights_testing_results.png', dpi=300)


