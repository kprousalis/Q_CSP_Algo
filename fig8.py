import numpy as np
import matplotlib.pyplot as plt

K = 4

distributions = {
    "Uniform": np.array([0.25, 0.25, 0.25, 0.25]),
    "Mild bias": np.array([0.4, 0.2, 0.2, 0.2]),
    "Strong bias": np.array([0.7, 0.1, 0.1, 0.1])
}

k_values = np.arange(1, 15)

plt.figure()
for label, p in distributions.items():
    p_match = np.sum(p**2)
    plt.plot(k_values, (p_match)**k_values, label=label)

plt.yscale("log")
plt.xlabel("Diagonal length (k)")
plt.ylabel("Probability of random diagonal (log scale)")
plt.title("K = 4")
plt.legend()
plt.show()