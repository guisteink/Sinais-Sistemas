'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#lab007 exercicio 2b

# amostragem e vetor no tempo
wam = 3000
Tam = 2*np.pi/wam
t = np.arange(0, 6, Tam)
N = pow(2, 12)


def degrau(t, d1, d2):
    u1 = np.arange(0, 6, Tam)
    for i in range(len(u1)):
        if u1[i] < d1:
            u1[i] = 0
        else:
            u1[i] = 1
    u1 = np.heaviside(t, Tam)

    u2 = np.arange(0, 6, Tam)
    for j in range(len(u2)):
        if u2[j] < d2:
            u2[j] = 0
        else:
            u2[j] = 1

    return (u1 - u2)

##############################################################################################################
# b
#sinal x2
x2 = pow(np.e, -t) * degrau(t, 0, 100)

# calculo da FT e da frequencia
X2 = (Tam*N)*fft(x2, N)/N
w2 = fftfreq(len(X2), d=(Tam))*(2*np.pi)

# posicionando os zeros no meio
wd2 = fftshift(w2)
Xd2 = fftshift(X2)

# magnitude e fase da transformada FT
ModX2 = np.abs(Xd2)
phasX2 = np.angle(Xd2)

fig, ax = plt.subplots(3, figsize=(13,6))

# plot da letra b
ax[0].plot(t, x2, 'r-')
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("Tempo, em s")
ax[0].set_title("[x2] e^(-t) . u(t) ")

# plot da magnitude
ax[1].plot(wd2, ModX2, 'r-')
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("Frequência, em rad/s")
ax[1].set_title("Magnitude de X2(jw)")
ax[1].set_xlim(-50, 50)

# plot da letra b
ax[2].stem(wd2, phasX2, 'r-')
ax[2].set_ylabel("Amplitude")
ax[2].set_xlabel("Frequência, em rad/s")
ax[2].set_title("Fase de X2(jw)")
ax[2].set_xlim(-50, 50)

##############################################################################################################


fig.tight_layout()
plt.show()