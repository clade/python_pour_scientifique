from matplotlib.pyplot import figure
import numpy as np

fig = figure(figsize=(10, 6))
ax = fig.subplots(1, 1) # Création d'un graphique
X = np.linspace(-2,2, 100)
Y = np.sin(X)**2*np.exp(-X**2)
Y_noise = Y + .1*(np.random.rand(len(X))-0.5)

ax.plot(X,Y, label=u"Theory")
ax.plot(X,Y_noise,'o', label=u"Experiment")
ax.set_xlabel(r'Voltage [V]')
ax.set_ylabel(r'$\zeta$ [m]')
ax.set_title("Nonsense graph")
ax.legend(loc='upper left')
ax.grid(True)