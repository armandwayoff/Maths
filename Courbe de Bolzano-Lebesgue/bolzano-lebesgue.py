import matplotlib.pyplot as plt
n = 4
x, y = [k / 3 ** n for k in range(3 ** n + 1)], [0, 1]
for _ in range(n):
    y = (y1 := [c * 2/3 for c in y]) + [2/3 - 1/2 * c for c in y1[1:-1]] + [c + 1/3 for c in y1]
plt.plot(x, y, linewidth=0.8)
plt.show()
