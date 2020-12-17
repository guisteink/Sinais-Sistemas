'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#lab007 exercicio 2c

# amostragem e vetor no tempo
wam = 10*7500
Tam = 2*np.pi/wam
t = np.arange(-0.35, 0.35, Tam)
N = pow(2, 12)

fig, ax = plt.subplots(3, figsize=(13, 6))
##############################################################################################################

# x3
x3 = np.sin(350*t)

# calculo da FT e da frequencia
X3 = (Tam*N)*fft(x3, N)/N
w3 = fftfreq(len(X3), d=(Tam))*(2*np.pi)

# posicionando os zeros no meio
wd3 = fftshift(w3)
Xd3 = fftshift(X3)

# magnitude e fase da transformada FT
ModX3 = np.abs(Xd3)
phasX3 = np.angle(Xd3)


# plot da letra c
ax[0].plot(t, x3, 'g-')
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("Tempo, em s")
ax[0].set_title("[x3] sen(350t) ")

# plot da magnitude
ax[1].plot(wd3, ModX3, 'g-')
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("Frequência, em rad/s")
ax[1].set_title("Magnitude de X3(jw)")
ax[1].set_xlim(-500, 500)

# plot da fase
ax[2].stem(wd3, phasX3, 'g-')
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("K")
ax[2].set_title("Fase de X3(jw)")
ax[2].set_xlim(-500, 500)

##############################################################################################################



fig.tight_layout()
plt.show()