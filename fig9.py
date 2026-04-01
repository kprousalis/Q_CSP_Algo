"""
The formula is implemented in a numerically stable way:
log(n^M⋅n)=(M+1)logn
to avoid overflow warnings.
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
Ks = [4, 20, 26]  # alphabet sizes
M_values = np.array([2, 3, 4, 5, 6])  # number of sequences (integers)
n_values = [64, 1000, 10000]  # sequence lengths


def k_max(K, M, n):
    """
    Expected maximum random hyperdiagonal length
    """
    p_match = 1 / (K ** (M - 1))
    # use logs safely to avoid overflow
    numerator = (M + 1) * np.log(n)
    denominator = -np.log(p_match)
    return numerator / denominator


# Create one plot per n
for n in n_values:
    plt.figure()

    for K in Ks:
        y_vals = [k_max(K, M, n) for M in M_values]
        plt.plot(M_values, y_vals, marker='o', label=f"K={K}")

    plt.xticks(M_values)  # force integer ticks
    plt.xlabel("Number of sequences (M)")
    plt.ylabel("Expected max random hyperdiagonal length")
    plt.title(f"n = {n}")
    plt.legend()
    plt.tight_layout()
    plt.show()