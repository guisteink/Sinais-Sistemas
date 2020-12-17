'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift

##############################################################################################################

# lab008 ex2
# (a)

L = 100
Fs = 1/5000
t = np.arange(0, L, Fs)

# degrau
degrau = np.zeros(np.size(t))
indice = np.where(t >= 0)
degrau[indice] = 1

# sinal
x = 100 * np.cos(2*np.pi*100*t) * pow(np.e, -100*t) * degrau

# dtft de x
X = Fs*fft(x)

# vetor de frequencia
w = fftfreq(len(X), d=1) * (2 * np.pi)
wd = fftshift(w/(2 * np.pi * Fs))

# magnitude e fase de x
Xd = fftshift(X)
modX = np.abs(Xd)
phaseX = np.angle(Xd)

phaseX[modX < 0.00001] = 0

# Plots
fig, ax = plt.subplots(2, 1)
fig2, ax2 = plt.subplots(1, 1)

ax2.stem(t, x)
ax2.set_ylabel("amp")
ax2.set_xlabel("n")
ax2.set_title("LETRA A: x1[n], Fs=5000")
ax2.set_xlim(0, 0.075)
ax2.grid()

ax[0].plot(wd,modX)
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("Hz")
ax[0].set_title("Magnitude de X[k]")
ax[0].grid()

ax[1].plot(wd, phaseX)
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("Hz")
ax[1].set_title("Fase de X[k]")
ax[1].grid()

fig2.tight_layout()
plt.show()

##############################################################################################################
