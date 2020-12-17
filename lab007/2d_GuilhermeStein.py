'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#lab007 exercicio 2d

# amostragem e vetor no tempo
wam = 4
Tam = 2/wam

def impulsos(K):
  ti = np.arange(-50, 51, Tam)
  for j in range(len(ti)):

    if ti[j]%K==0:
      ti[j] = 1

    else:
      ti[j] = 0
  return ti
##############################################################################################################

fig, ax = plt.subplots(3, figsize=(13, 6))
t = np.arange(-50, 51, Tam)
N = pow(2, 12)

K = 10
x4 = impulsos(K)

# calculo da FT e da frequencia
X4 = (Tam*N)*fft(x4, N)/N
w4 = fftfreq(len(X4), d=(Tam))*(2*np.pi)

# posicionando os zeros no meio
wd4 = fftshift(w4)
Xd4 = fftshift(X4)

# magnitude e fase da transformada FT
ModX4 = np.abs(Xd4)
phasX4 = np.angle(Xd4)

# plot da letra d
ax[0].stem(t, x4, 'y-')
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("Tempo, em s")
ax[0].set_title("[x4] Trem de impulsos ")

# plot da letra d
ax[1].plot(wd4, ModX4, 'y-')
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("Frequencia, em rad/s")
ax[1].set_title("Magnitude de X4(jw)")
ax[1].set_xlim(-2, 2)

# plot da letra d
ax[2].stem(wd4, phasX4, 'y-')
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("K")
ax[2].set_title("Fase de X4(jw)")
ax[2].set_xlim(-2, 2)










fig.tight_layout()
plt.show()