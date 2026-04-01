import numpy as np
import matplotlib.pyplot as plt

# Sequence lengths (log scale)
N = np.logspace(2, 6, 50)  # 10^2 to 10^6

def k_max(N, K):
    p_match = 1 / K
    return np.log(2 * N * N) / (-np.log(p_match))

K_values = [4, 20, 26]

plt.figure()
for K in K_values:
    plt.plot(N, k_max(N, K), label=f"K={K}")

plt.xscale("log")
plt.xlabel("Sequence length (N)")
plt.ylabel("Expected max random diagonal length")
plt.title("Logarithmic scaling of maximum random diagonal length")
plt.legend()

plt.show()