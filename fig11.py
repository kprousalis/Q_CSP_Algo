import random
import matplotlib.pyplot as plt

def longest_run(matches):
    max_run = run = 0
    for m in matches:
        if m:
            run += 1
            max_run = max(max_run, run)
        else:
            run = 0
    return max_run

def simulate(p_match, N, trials=500):
    runs = []
    for _ in range(trials):
        matches = [random.random() < p_match for _ in range(N)]
        runs.append(longest_run(matches))
    return runs

def run_experiment(K, N=200, trials=500):
    # Uniform distribution
    p_uniform = 1 / K

    # Biased distribution: one dominant symbol (0.7), rest share 0.3
    p_main = 0.7
    p_rest = 0.3 / (K - 1)
    p_biased = p_main**2 + (K - 1) * (p_rest**2)

    runs_uniform = simulate(p_uniform, N, trials)
    runs_biased = simulate(p_biased, N, trials)

    plt.figure()
    bins = range(1, max(runs_biased) + 2)

    plt.hist(runs_uniform, bins=bins, alpha=0.7)
    plt.hist(runs_biased, bins=bins, alpha=0.7)

    plt.xlabel("Longest diagonal length")
    plt.ylabel("Frequency")
    plt.title(f"Uniform vs Biased Alphabet (K={K}, identical length)")
    plt.show()

# Run for the three cases
run_experiment(K=4)
run_experiment(K=20)
run_experiment(K=26)