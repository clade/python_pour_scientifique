import numpy as np
import matplotlib.pyplot as plt

def fermi_dirac(epsilon, mu, beta):
    return 1/(np.exp(beta*(epsilon - mu))+1)

x = np.linspace(0, 3, num=1000)
x_zoom = np.linspace(0.9, 1.1, num=1000)

fig = plt.figure()
ax = fig.subplots(1, 1)

ax.plot(x, fermi_dirac(x, mu=1, beta=100))

axins = ax.inset_axes([0.5, 0.35, 0.47, 0.47])
axins.plot(x_zoom, fermi_dirac(x_zoom, mu=1, beta=100))
ax.indicate_inset_zoom(axins, edgecolor="black")

for a in [ax, axins]:
    a.set_xlabel(r'$\epsilon$')
    a.set_ylabel(r'$\bar n$')
    a.grid()