"""
Make a python program with the following specifications:

(A) As a first function: the program should be able to generate a dot-matrix plot of 2D dimensions, or a dot-matrix plot of 3D dimensions. The input datasets should be either 2 strings for the 2D dot-matrix plot or 3 strings for the 3D dot-matrix plot. The program should ask the user which dot-matrix plot dimension to run (accepted values lets be {2,3}).  The input strings should be already generated via the program (and not via an interface), so create separate datasets of 2 and 3 strings made by the DNA alphabet (4 letters) all of length 32 letters. The orientation of the strings on the axis of the plot should be the same, starting counting letters from the zero point of the axis. You may place a title or label for each axis to indicate which string represent eg String1, String 2, String 3.

(B) As a second function, after step (A), the program should ask the user how many dot steps to shift the initially created dot-matrix plot, diagonally downward and rightward, concurrently, per s dot steps (where s should be an integer). By shifting the dot plot (not to be meant a cycle shift), we ignore the dots that get out of the boundaries of the dot-plot. The shifting value should not be higher than the maximum length of the strings. For the 3D dot-matrix plot the shifting is applied to all three axis having the orientation. Make sure that the strings of the axes start from the same zero point exactly as in the dot plot of step (A).

(C) As a third function, after shifting is accomplished in step (B), then make a bitwise AND operation point by point between all the cells of the unshifted dot plot instance with all the shifted dot plot instance. The result will be a new dot plot.

(D) Now, plot and view all three participating dot-matrix plots: 1. the unshifted dot plot instance, 2. the shifted dot plot instance, and 3. the final ANDed dot plot instance. Each dot-matrix plot should be accompanied by a plot showing the distribution of all diagonal consecutive (continuous) dot formations (not disrupted dot formation with spaces of one or more dots). For example, x axis may present the degree of diagonal length (integer) while y axis may present the number of the occuring diagonal formations. Axis ticks for both x and y axis should be only integers having the same range in all three instances. All data plots should be viewed in the same window in a format 2x3.

"""

import numpy as np
import matplotlib.pyplot as plt
import random

from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import Axes3D

DNA = ['A','C','G','T']
PROTEIN = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
LENGTH = 64


# --------------------------------------------------
# Generate random DNA string
# --------------------------------------------------

def generate_dna(length=32):
    return ''.join(random.choice(PROTEIN) for _ in range(length))


# --------------------------------------------------
# Create dot matrices
# --------------------------------------------------

def dot_matrix_2d(s1, s2):

    n = len(s1)
    matrix = np.zeros((n,n), dtype=int)

    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                matrix[i,j] = 1

    return matrix


def dot_matrix_3d(s1, s2, s3):

    n = len(s1)
    matrix = np.zeros((n,n,n), dtype=int)

    for i in range(n):
        for j in range(n):
            for k in range(n):

                if s1[i] == s2[j] == s3[k]:
                    matrix[i,j,k] = 1

    return matrix


# --------------------------------------------------
# Shift matrix diagonally
# --------------------------------------------------

def shift_matrix(matrix, shift):

    shifted = np.zeros_like(matrix)

    if matrix.ndim == 2:

        n = matrix.shape[0]

        for i in range(n):
            for j in range(n):

                ni = i + shift
                nj = j + shift

                if ni < n and nj < n:
                    shifted[ni,nj] = matrix[i,j]

    else:

        n = matrix.shape[0]

        for i in range(n):
            for j in range(n):
                for k in range(n):

                    ni = i + shift
                    nj = j + shift
                    nk = k + shift

                    if ni < n and nj < n and nk < n:
                        shifted[ni,nj,nk] = matrix[i,j,k]

    return shifted


# --------------------------------------------------
# Bitwise AND
# --------------------------------------------------

def and_matrix(A,B):

    return np.logical_and(A,B).astype(int)


# --------------------------------------------------
# Diagonal run-length distribution
# --------------------------------------------------

def diagonal_distribution(matrix):

    if matrix.ndim == 3:
        matrix = np.max(matrix, axis=2)

    n = matrix.shape[0]
    counts = {}

    for k in range(-n+1,n):

        diag = np.diagonal(matrix, offset=k)

        run = 0

        for v in diag:

            if v == 1:
                run += 1

            else:

                if run > 0:
                    counts[run] = counts.get(run,0) + 1
                    run = 0

        if run > 0:
            counts[run] = counts.get(run,0) + 1

    return counts


# --------------------------------------------------
# Plot dot matrices
# --------------------------------------------------

def plot_dot_matrix(ax, matrix, dim, title):

    if dim == 2:

        y,x = np.where(matrix == 1)

        ax.scatter(x,y,marker='o')

        ax.set_xlabel("String2")
        ax.set_ylabel("String1")

        ax.set_xlim(-1,LENGTH)
        ax.set_ylim(-1,LENGTH)

    else:

        x,y,z = np.where(matrix == 1)

        ax.scatter(x,y,z,marker='o')

        ax.set_xlabel("String1")
        ax.set_ylabel("String2")
        ax.set_zlabel("String3")

        ax.set_xlim(0,LENGTH)
        ax.set_ylim(0,LENGTH)
        ax.set_zlim(0,LENGTH)

    ax.set_title(title)


# --------------------------------------------------
# Plot distribution
# --------------------------------------------------

def plot_distribution(ax, dist):

    x = list(range(1,LENGTH+1))
    y = [dist.get(i,0) for i in x]

    ax.bar(x,y)

    ax.set_xlabel("HyperDiagonal Length")
    ax.set_ylabel("Occurrences")

    step = 4
    #ax.set_xticks(range(0,LENGTH+1,step))

    max_y = max(y) if y else 1
    #ax.set_yticks(range(0,max_y+1,step))


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

def main():

    dim = int(input("Choose dot-matrix dimension (2 or 3): "))

    if dim not in [2,3]:
        print("Invalid dimension.")
        return


    # generate DNA strings

    #s1 = generate_dna(LENGTH)
    #s2 = generate_dna(LENGTH)

    #if dim == 3:
    #    s3 = generate_dna(LENGTH)
    s1 = "FSMEWFNMARPIFHGYRGWSNLRQCRKIDSRMNSRDIQMNSPMYMNVMCIVDIYIWPWYTKQRV"
    s2 = "PDKVNVMCIVDIYISISESIAVFNMARPIFHGYLVPGFLCNPWPTHIQHLRHTDMVRSPRKSFA"
    s3 = "PEPVPDNVMCIVDIYIPENSREDACAGQVSGASHWFWPIDNMARPIFHGYPCRWREKARPISEH"

    print("\nGenerated DNA strings")
    print("String1:",s1)
    print("String2:",s2)

    if dim == 3:
        print("String3:",s3)


    # build original matrix

    if dim == 2:
        original = dot_matrix_2d(s1,s2)
    else:
        original = dot_matrix_3d(s1,s2,s3)


    # shift value

    shift = int(input("\nEnter shift value (0-32): "))

    if shift > LENGTH:
        print("Shift too large.")
        return


    shifted = shift_matrix(original,shift)

    anded = and_matrix(original,shifted)


    # distributions

    d1 = diagonal_distribution(original)
    d2 = diagonal_distribution(shifted)
    d3 = diagonal_distribution(anded)


    # --------------------------------------------------
    # plotting
    # --------------------------------------------------

    fig = plt.figure(figsize=(16,10))


    if dim == 2:

        ax1 = fig.add_subplot(2,3,1)
        ax2 = fig.add_subplot(2,3,2)
        ax3 = fig.add_subplot(2,3,3)

    else:

        ax1 = fig.add_subplot(2,3,1,projection='3d')
        ax2 = fig.add_subplot(2,3,2,projection='3d')
        ax3 = fig.add_subplot(2,3,3,projection='3d')


    ax4 = fig.add_subplot(2,3,4)
    ax5 = fig.add_subplot(2,3,5)
    ax6 = fig.add_subplot(2,3,6)

    plot_dot_matrix(ax1, original, dim, "Original QDP")
    plot_dot_matrix(ax2, shifted, dim, "Shifted QDP")
    plot_dot_matrix(ax3, anded, dim, "ANDed QDP")

    plot_distribution(ax4, d1)
    plot_distribution(ax5, d2)
    plot_distribution(ax6, d3)

    ax6.yaxis.set_major_locator(MaxNLocator(integer=True))
    #ax6.set_yticks(range(0, 10))

    # --------------------------------------------------
    # show DNA strings above plots
    # --------------------------------------------------

    text = f"String1: {s1}\nString2: {s2}"

    if dim == 3:
        text += f"\nString3: {s3}"


    fig.text(
        0.5,
        0.97,
        text,
        ha='center',
        va='top',
        fontsize=11,
        family='monospace'
    )

    fig.suptitle(
        f"Protein Sequences (length = {LENGTH})   |   Shift parameter s = {shift}\n",
        fontsize=10,
        y=1.00
    )

    plt.tight_layout(rect=[0,0,1,0.92])
    plt.show()


if __name__ == "__main__":
    main()