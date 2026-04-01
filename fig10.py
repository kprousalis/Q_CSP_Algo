import matplotlib.pyplot as plt
import numpy as np

# Alphabet sizes
Ks = [4, 20, 26]

# Range of diagonal lengths
k_values = np.arange(1, 21)

# Create plot
plt.figure()

for K in Ks:
    p_match = 1 / K
    probabilities = p_match ** k_values
    plt.plot(k_values, probabilities, label=f"K={K}")

# Log scale for exponential decay visualization
plt.yscale("log")

# Labels and title
plt.xlabel("Diagonal length (k)")
plt.ylabel("Probability of random diagonal (log scale)")
plt.title("Exponential decay of random diagonal probability with diagonal length")

# Legend
plt.legend()

# Show plot
plt.show()