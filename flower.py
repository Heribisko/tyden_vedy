import numpy as np
import matplotlib.pyplot as plt

# Parameters
phi = (1-np.sqrt(5))/2
m = np.arange(1, 1500)
theta = 2 * np.pi * m / phi
r = np.sqrt(m)

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='polar')
ax.scatter(theta, r, s=10, color='red')  # s = point size

# Remove axes and frame
ax.set_frame_on(False)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()
