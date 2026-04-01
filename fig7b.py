import numpy as np
import matplotlib.pyplot as plt

# Sequence lengths (linear scale)
N = np.linspace(10, 100, 50)

def k_max(N, K):
    p_match = 1 / K
    return np.log(2 * N * N) / (-np.log(p_match))

K_values = [4, 20, 26]

plt.figure()
for K in K_values:
    plt.plot(N, k_max(N, K), label=f"K={K}")

plt.xlabel("Sequence length (N)")
plt.ylabel("Expected max random diagonal length")
plt.title("Maximum random diagonal length for short sequences (N = 10–100)")
plt.legend()

plt.show()