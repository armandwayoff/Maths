import matplotlib.pyplot as plt
n = 15
x, y = [i / 2 ** n for i in range(2 ** n + 1)], [0, 1/2, 0]
for k in range(1, n):
    triangles = 2 ** k * [0, 1/2 ** (k+1)] + [0]
    echan = [f for i in range(len(y) - 1) for f in (y[i], (y[i] + y[i+1]) / 2)] + [0]
    y = [echan[i] + triangles[i] for i in range(len(echan))]
plt.title("Courbe du blanc-manger d'ordre " + str(n))
plt.plot(x, y, linewidth=0.8)
plt.show()
