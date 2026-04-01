import numpy as np
import matplotlib.pyplot as plt

def random_sequence(length, K):
    return np.random.randint(0, K, size=length)

def longest_run(arr):
    padded = np.concatenate(([0], arr, [0]))
    diff = np.diff(padded)
    starts = np.where(diff == 1)[0]
    ends = np.where(diff == -1)[0]
    if len(starts) == 0:
        return 0
    return np.max(ends - starts)

def max_diagonal_length(s1, s2):
    n = len(s1)
    max_len = 0
    for d in range(-(n - 1), n):
        if d < 0:
            a = s1[-d:]
            b = s2[:n + d]
        else:
            a = s1[:n - d]
            b = s2[d:]
        matches = (a == b).astype(int)
        max_len = max(max_len, longest_run(matches))
    return max_len

def experiment(N=500, trials=30, Ks=[2, 4, 8, 16, 32]):
    results = []
    for K in Ks:
        max_vals = []
        for _ in range(trials):
            s1 = random_sequence(N, K)
            s2 = random_sequence(N, K)
            max_vals.append(max_diagonal_length(s1, s2))
        results.append(np.mean(max_vals))
    return Ks, results

# Run experiment
Ks, values = experiment()

# Plot
plt.figure()
plt.plot(Ks, values, marker='o')
plt.xscale('log')
plt.xlabel("Alphabet size (K)")
plt.ylabel("Average maximum diagonal length")
plt.title("Alphabet size vs. maximum random diagonal length")
plt.show()