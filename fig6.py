import random
import numpy as np
import matplotlib.pyplot as plt


def random_sequence(length, alphabet):
    return [random.choice(alphabet) for _ in range(length)]


def longest_run(binary_list):
    max_run = run = 0
    for x in binary_list:
        if x == 1:
            run += 1
            max_run = max(max_run, run)
        else:
            run = 0
    return max_run


def max_diagonal(seqs):
    n = len(seqs[0])
    max_len = 0

    for d in range(-(n - 1), n):
        matches = []
        for i in range(n):
            j = i + d
            if 0 <= j < n:
                symbols = [seq[j] for seq in seqs]
                matches.append(1 if len(set(symbols)) == 1 else 0)
        max_len = max(max_len, longest_run(matches))

    return max_len


def experiment_M(sequence_length=300, trials=20, K=4):
    alphabet = list(range(K))
    Ms = [2, 3, 4, 5]
    results = {}

    for M in Ms:
        vals = []
        for _ in range(trials):
            seqs = [random_sequence(sequence_length, alphabet) for _ in range(M)]
            vals.append(max_diagonal(seqs))
        results[M] = np.mean(vals)

    return results


# Run experiments for different alphabet sizes
Ks = [4, 20, 26]

for K in Ks:
    results = experiment_M(K=K)

    plt.figure()
    plt.plot(list(results.keys()), list(results.values()), marker='o')
    plt.xlabel("Number of sequences (M)")
    plt.ylabel("Average max random diagonal length")
    plt.title(f"Maximum random diagonal length vs number of sequences (K={K})")
    plt.show()