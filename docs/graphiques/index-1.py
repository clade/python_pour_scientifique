import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
X = np.linspace(-2,2, 100)
Y = np.sin(X)**2*np.exp(-X**2)
Y_noise = Y + .1*(np.random.rand(len(X))-0.5)

plt.plot(X,Y, label=u"Theory")
plt.plot(X,Y_noise,'o', label=u"Experiment")
plt.xlabel(r'Voltage [V]')
plt.ylabel(r'$\zeta$ [m]')
plt.title("Nonsense graph")
plt.legend(loc='upper left')
plt.grid(True)

plt.savefig('mafigure.pdf')