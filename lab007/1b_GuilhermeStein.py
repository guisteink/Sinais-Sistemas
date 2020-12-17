'''
Autor: Guilherme Stein Kuhn
Disciplina: Sinais e Sistemas
Período: 2020/1 - earte
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft, fftfreq, fftshift

#lab007 exercicio 1b

# criando o vetor de tempo e definindo a frequencia de amostragem
wam = 500
Tam = 2*np.pi / wam
t = np.arange(-10, 10, Tam)
cont = 0
N = pow(2, 12)

def rampa_unit(cont):
    x = np.arange(-10, 10, Tam)
    y = np.arange(-10, 10, Tam)
    z = np.arange(-10, 10, Tam)

    cont = 0
    for i in range(len(x)):
        if(x[i] < -5):
            x[i] = 0
        else:
            x[i] = cont
            cont += Tam

    cont = 0
    for j in range(len(y)):
        if (y[j] < 0):
            y[j] = 0
        else:
            y[j] = cont
            cont += Tam

    cont = 0
    for k in range(len(z)):
        if(z[k] < 5):
            z[k] = 0
        else:
            z[k] = cont
            cont += Tam

    return x - 2*y + z

##############################################################################################################

# sinal x(t) modulante
corrige_amplitude = 0.2
x = corrige_amplitude * (0.2 * rampa_unit(cont))

# sinal y(t)
y = x * np.cos(10*t)

# y(t) ->[FT]-> Y(jw)
Yjw = (Tam * N)*fft(y, N)/N
jw = fftfreq(len(Yjw), d=(Tam))*(2*np.pi)

# posicionando a frequencia 0 no meio do gráfico
wd = fftshift(jw)
Yd = fftshift(Yjw)

# Magnitude d Yjw
modYjw = np.abs(Yd)

fig, ax = plt.subplots(2, figsize=(6,6))

# plot de y(t)
ax[0].plot(t, y)
ax[0].set_ylabel("Amplitude")
ax[0].set_xlabel("Tempo, em s")
ax[0].set_title("x(t)")
ax[0].set_xlim(-7.5, 7.5)
# plot de Y(jw)
ax[1].plot(wd, modYjw)
ax[1].set_ylabel("Amplitude")
ax[1].set_xlabel("Frequência (rad/s)")
ax[1].set_title("Magnitude de X(jw)")
ax[1].set_xlim(-20, 20)

##############################################################################################################

fig.tight_layout()
plt.show()
