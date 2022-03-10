import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

COEFF = [
    [1],
    [0, 1],
    [-1, 0, 2],
    [0, -3, 0, 4],
    [1, 0, -8, 0, 8],
    [0, 5, 0, -20, 0, 16]
]


def f(x, n):
    s = 0
    for k in range(n + 1):
        s += COEFF[n][k] * (x ** k)
    return s


X = np.arange(-1, 1, 0.01)
for n in range(len(COEFF)):
    Y = [f(x, n) for x in X]
    plt.plot(X, Y, label="$T_{n}$")
plt.legend()

import tikzplotlib

tikzplotlib.save("polynomes_tchebychev.tex")
