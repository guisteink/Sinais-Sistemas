'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift

##############################################################################################################

# lab008 ex1_a

# (a) x[n] = (0.5^n).u[n]
L = 256
n = np.arange(0, L, 1)
x = pow(0.5, n)

# dtft de x[n]
X = fft(x)

# vetor de frequencia
w = fftfreq(len(X), d=1)*(2*np.pi)
wd = fftshift(w/np.pi)

# magnitude e angulo do espectro
X1 = fftshift(X)
modX1 = np.abs(X1)
phaseX1 = np.angle(X1)
phaseX1[modX1 < 0.00001] = 0

# Plots
fig, ax = plt.subplots(3, 1)
fig2, ax2 = plt.subplots(1, 1)

ax2.stem(n, x, '-r')
ax2.set_ylabel("amp")
ax2.set_xlabel("n")
ax2.set_title("LETRA A")
ax2.set_xlim(0, 10)
ax2.grid()

ax[0].stem(n, x, '-b')
ax[0].set_ylabel("amp")
ax[0].set_xlabel("n")
ax[0].set_title("x[n]")
ax[0].grid()

ax[1].plot(wd, modX1, '-g')
ax[1].set_ylabel("amp")
ax[1].set_xlabel("w/pi")
ax[1].set_title("Magnitude de X[k]")
ax[1].grid()

ax[2].plot(wd, phaseX1, '-y')
ax[2].set_ylabel("amp")
ax[2].set_xlabel("w/pi")
ax[2].set_title("Fase de X[k]")
ax[2].grid()

fig.tight_layout()
plt.show()

##############################################################################################################


