import numpy as np
import matplotlib.pyplot as plt

# même pour une formule simple, il faut définir une fonction
def H(omega, omega_0, zeta):
    return omega_0**2/(omega_0**2-omega**2 + 2J*omega*zeta*omega_0)

omega_0 = 2*np.pi*1000
zeta = 0.1

Tomega = 2*np.pi*np.logspace(2,4, 1001)
amplitude = H(Tomega, omega_0, zeta)

fig = plt.figure()
ax1, ax2 = fig.subplots(2, 1, sharex=True)

fig.suptitle(f'($\omega_0/2\pi$={omega_0/(2*np.pi):.2f} Hz et $\zeta={zeta}$)')
ax1.grid(True, which='both')
ax1.loglog(Tomega/(2*np.pi), np.abs(amplitude))
ax1.set_ylabel('Amplitude')

phase_in_deg = np.unwrap(np.angle(amplitude))/(2*np.pi)*360

ax2.semilogx(Tomega/(2*np.pi), phase_in_deg)
ax2.set_ylabel(u'Phase [°]')
ax2.set_xlabel(u'Fréquence [Hz]')
ax2.grid(True, which='both')

fig.tight_layout()