import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 9  # recursion depth
angle_pos = np.pi / 5 # +60 degrees
angle_neg = -np.pi / 2

# L-system rules
rules = {
    "X": ["Y", angle_pos, "X", angle_pos, "Y"],
    "Y": ["X", angle_neg, "Y", angle_neg, "X"]
}

# Substitution function
def substitute(sequence, depth):
    for _ in range(depth):
        new_seq = []
        for symbol in sequence:
            if symbol in rules:
                new_seq.extend(rules[symbol])
            else:
                new_seq.append(symbol)
        sequence = new_seq
    return sequence

# Generate instruction list
initial = ["X"]
instruction = substitute(initial, n)

# Convert to list of angles (starting with 0)
angle_sequence = [0] + [item for item in instruction if isinstance(item, (float, int))]

# Compute directions
directions = np.cumsum(angle_sequence)

# Convert directions to x, y path
x = np.cumsum(np.cos(directions))
y = np.cumsum(np.sin(directions))

# Plot single continuous curve
fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x, y, color='black', linewidth=1.2)  # single line, no breaks
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.show()
