import matplotlib.pyplot as plt

yerr = [[1,2],[2,1]]
x = [1,2]
y = [1,2]

plt.errorbar(x, y, yerr=yerr)
plt.show()