import random as rd
import matplotlib.pyplot as plt

P = 6
DIR = (-1, 1)

X, Y = [0], [0]

for i in range(10 ** P):
    X.append(X[i] + rd.choice(DIR))
    Y.append(Y[i] + rd.choice(DIR))


plt.title("Marche aléatoire pour N = 10^" + str(P))
plt.plot(X, Y, linewidth=0.05)
plt.show()
