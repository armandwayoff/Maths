import matplotlib.pyplot as plt
n = 15
x, y = [0, 1/2, 1], [0, 1/2, 0]
# plt.plot(x, y)
for k in range(1, n):
    x = [i / 2 ** (k+1) for i in range(2 ** (k+1) + 1)]
    gene = 2 ** k * [0, 1 / 2 ** (k+1)] + [0]
    echan = []
    for i in range(len(y) - 1):
        echan.append(y[i])
        echan.append((y[i] + y[i + 1]) / 2)
    echan.append(0)
    Y = []
    for i in range(len(echan)):
        Y.append(echan[i] + gene[i])
    y = Y
plt.title("Courbe du blanc-manger d'ordre " + str(n))
plt.plot(x, y, linewidth=0.8)
plt.show()
