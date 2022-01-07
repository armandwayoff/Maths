import matplotlib.pyplot as plt

n = 4

x = [k / 3 ** n for k in range(3 ** n + 1)]
y = [0, 1]
for k in range(n):
    y1 = [c * 2/3 for c in y]
    y2 = [2/3 - 1/2 * c for c in y1[1:-1]]
    y3 = [c + 1/3 for c in y1]
    y = y1 + y2 + y3
plt.plot(x, y)
plt.show()
