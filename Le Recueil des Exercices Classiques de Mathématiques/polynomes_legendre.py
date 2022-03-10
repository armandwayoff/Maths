import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

COEFF = [
    [1],
    [0, 1],
    [-1/2, 0, 3/2],
    [0, -3/2, 0, 5/2],
    [3/8, 0, -30/8, 0, 35/8],
    [0, 15/8, 0, -70/8, 0, 63/8]
]


def f(x, n):
    s = 0
    for k in range(n + 1):
        s += COEFF[n][k] * (x ** k)
    return s


X = np.arange(-1, 1, 0.01)
for n in range(len(COEFF)):
    Y = [f(x, n) for x in X]
    plt.plot(X, Y, label="$L_{" + str(n) + "}$")
plt.legend()

import tikzplotlib

tikzplotlib.save("polynomes_legendre.tex")
