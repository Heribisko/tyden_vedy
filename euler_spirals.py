import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

# Parameters
theta_deg = 3.3657 
m = 20000
chunk_size = 1000

# Build turning angle list like Mathematica's Range[m] * theta
angles = np.radians(theta_deg * np.arange(1, m + 1))  # θ * Range[m] in degrees → radians

# Compute cumulative angles for each step
directions = np.cumsum(angles)

# Compute 2D walk using unit vectors
x = np.cumsum(np.cos(directions))
y = np.cumsum(np.sin(directions))

# Colormap setup
cmap = get_cmap("plasma")  # pick a vibrant one
n_chunks = m // chunk_size

# Plot
fig, ax = plt.subplots(figsize=(10, 10))
for i in range(n_chunks):
    start = i * chunk_size
    end = start + chunk_size
    color = cmap(i / n_chunks)
    ax.plot(x[start:end], y[start:end], linewidth=2, color=color)

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.show()
