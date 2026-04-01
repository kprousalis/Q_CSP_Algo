import numpy as np
import random
import matplotlib.pyplot as plt
from collections import Counter
from itertools import product

from matplotlib.ticker import MaxNLocator

DNA = ["A", "C", "G", "T"]
SEQ_LEN = 16


# ------------------------------
# Generate DNA strings
# ------------------------------
def generate_sequences(dim):
    seqs = []
    seqs.append("CGAACGGCGCGGGGCA")
    seqs.append("ATGTAAGCTTCGGTAG")
    seqs.append("TGCCTATACAGGAGCC")
    seqs.append("CGCGCACGATGGGCAA")
    seqs.append("GCAGCATAAGTCCAGT")
    #seqs.append("QHKNTQYRMINYASRLDYPLRLCSTTGTFYWD")
    #seqs.append("MFQSVDVDMQWMWMLCARDRICNNNMVSPGAD")
    #seqs.append("YSRSRYFGLKHFMQCVAWPFHTQNFLWTQFYN")
    #seqs.append("QLVAKTQQMHPTWKARTSLHIDRNHIDLPKHM")
    #seqs.append("QCWVPIKPPYMNDQKLMHIQAMNWTCGIAPKS")
    #for _ in range(dim):
    #    s = "".join(random.choice(DNA) for _ in range(SEQ_LEN))
    #    seqs.append(s)
    return seqs


# ------------------------------
# Build N-dimensional dot matrix
# ------------------------------
def build_dot_matrix(seqs):

    dim = len(seqs)
    shape = [SEQ_LEN] * dim
    matrix = np.zeros(shape, dtype=np.uint8)

    for index in product(range(SEQ_LEN), repeat=dim):

        chars = [seqs[i][index[i]] for i in range(dim)]

        if len(set(chars)) == 1:
            matrix[index] = 1

    return matrix


# ------------------------------
# Diagonal shift
# ------------------------------
def diagonal_shift(matrix, shift):

    dim = matrix.ndim
    shape = matrix.shape
    shifted = np.zeros_like(matrix)

    for index in product(*[range(s) for s in shape]):

        new_index = tuple(i + shift for i in index)

        if all(new_index[d] < shape[d] for d in range(dim)):
            shifted[new_index] = matrix[index]

    return shifted


# ------------------------------
# Find diagonal run lengths
# ------------------------------
def diagonal_runs(matrix):

    dim = matrix.ndim
    N = matrix.shape[0]

    visited = set()
    runs = []

    for index in product(range(N), repeat=dim):

        if matrix[index] == 1 and index not in visited:

            length = 0
            current = index

            while True:

                if any(i >= N for i in current):
                    break

                if matrix[current] == 0:
                    break

                visited.add(current)
                length += 1

                current = tuple(i + 1 for i in current)

            if length > 0:
                runs.append(length)

    return runs


# ------------------------------
# Convert runs to distribution
# ------------------------------
def distribution(runs):
    return Counter(runs)


# ------------------------------
# Plot distributions
# ------------------------------
def plot_distributions(d1, d2, d3, seqs, shift):

    all_x = set(d1.keys()) | set(d2.keys()) | set(d3.keys())

    if not all_x:
        all_x = {0}

    x_max = max(all_x)

    x_vals = list(range(1, x_max + 1))

    y1 = [d1.get(x, 0) for x in x_vals]
    y2 = [d2.get(x, 0) for x in x_vals]
    y3 = [d3.get(x, 0) for x in x_vals]

    y_max = max(max(y1), max(y2), max(y3), 1)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    titles = [
        f"Distribution of Unshifted QDP",
        f"Distribution of Shifted QDP (s = {shift})",
        f"Distribution of ANDed QDP"
    ]

    ys = [y1, y2, y3]

    for ax, y, title in zip(axes, ys, titles):

        ax.bar(x_vals, y)

        ax.set_title(title)
        ax.set_xlabel("HyperDiagonal Length")
        ax.set_ylabel("Count")

        ax.set_xticks(range(0, SEQ_LEN + 1))
        ax.set_yticks(range(0, y_max + 1))
        #ax.set_xticks(x_vals)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # Display sequences and shift parameter above plots
    seq_text = "\n".join([f"S{i+1}: {s}" for i, s in enumerate(seqs)])

    fig.suptitle(
        f"DNA Sequences (length = {SEQ_LEN})   |   Shift parameter s = {shift}\n{seq_text}",
        fontsize=10,
        y=1.00
    )

    plt.tight_layout()
    plt.show()


# ------------------------------
# Main program
# ------------------------------
def main():

    dim = int(input("Choose dot-matrix dimension (4 or 5): "))

    if dim not in [4, 5]:
        print("Invalid dimension")
        return

    seqs = generate_sequences(dim)

    print("\nGenerated sequences:\n")

    for i, s in enumerate(seqs):
        print(f"S{i+1}: {s}")

    dot_matrix = build_dot_matrix(seqs)

    shift = int(input("\nEnter diagonal shift value (0-32): "))

    if shift > SEQ_LEN:
        print("Shift too large")
        return

    shifted = diagonal_shift(dot_matrix, shift)

    and_matrix = dot_matrix & shifted

    runs_original = diagonal_runs(dot_matrix)
    runs_shifted = diagonal_runs(shifted)
    runs_and = runs_shifted
    #runs_and = diagonal_runs(and_matrix)

    d1 = distribution(runs_original)
    d2 = distribution(runs_shifted)
    d3 = distribution(runs_and)

    plot_distributions(d1, d2, d3, seqs, shift)


if __name__ == "__main__":
    main()