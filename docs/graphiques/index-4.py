import numpy as np
import matplotlib.pyplot as plt

def fermi_dirac(epsilon, mu, beta):
    return 1/(np.exp(beta*(epsilon - mu))+1)

list_beta = [1, 3, 10, 30, 100]
mu = 1

x = np.linspace(0, 3, num=1000)

fig = plt.figure()
ax = fig.subplots(1, 1)

for beta in list_beta:
    ax.plot(x, fermi_dirac(x, mu=mu, beta=beta),
            label=rf'$\beta={beta}$')

ax.set_xlabel(r'$\epsilon$')
ax.set_ylabel(r'$\bar n$')
ax.set_title('Distribution de Fermi-Dirac')
ax.grid()
ax.legend()