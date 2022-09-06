import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([4, 5, 5.5])
erreurs_y = 0.1 * y

plt.errorbar(x, y, erreurs_y, fmt='.', label="données+barres")

plt.xlabel("l'axe des x")
plt.ylabel("l'axe des y")
plt.legend(loc=2)
plt.grid()
plt.title("Le titre")